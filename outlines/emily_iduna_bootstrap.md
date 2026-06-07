# MEMO: IDUNA Bootstrap Fragility — Options & Recommendation
## To: Emily Springerton | From: System | Re: Tyler agent unblock
### Filed: 2026-06-07 | EINHORN_INDUSTRIAL | Ref: IDUNA-OPS-001

---

> *"Clean builds first. Then custody. Then everything else."*
> Tyler can't authenticate until IDUNA is running. IDUNA can't run until MySQL is running.
> MySQL can't run until a human starts it. That human is the load-bearing dependency.
> This memo is about removing the human from that chain.

---

## The Problem

Tyler's Iduna registration (Build 0016) is architecturally complete. The `tyler-agent` IAM
role is defined. The permissions are scoped. The `.claude/settings.json` carries the
commit identity. The blame path is occupied.

But the **agent authentication endpoint** — `POST /api/v1/auth/agent` — requires IDUNA
running. IDUNA requires MySQL running. MySQL requires a human to start it.

Every time the server restarts, or the MySQL process dies, or someone runs the wrong
command, Tyler can't authenticate. The token chain breaks at the bottom: not at the agent,
not at IDUNA, but at the infrastructure layer below both of them.

That infrastructure layer is currently a human being who knows the DSN.

---

## The Options

### Option A — Script MySQL provisioning

Run a script that SSHs into the server, checks if MySQL is running, starts it if not,
configures the DSN, and calls bootstrap. This can be automated via cron or systemd.

**Why it's still fragile:**
- MySQL dies → script must detect it and restart → retry logic, health checks, process
  supervision. You've now built a MySQL babysitter.
- Server reboots → requires MySQL auto-start config at the OS level. Still a human
  configured that.
- DSN changes, password rotates → script must be updated. Human fragility, deferred.
- SSH → fragile transport layer. Key management, network availability, etc.

This reduces the *frequency* of human intervention but doesn't eliminate the dependency.
The human is still in the blast radius of every failure mode.

**Verdict:** Better than nothing. Not good enough.

---

### Option B — Reimplement the MySQL wire protocol (embedded MySQL-compatible server)

Run an in-process server that speaks the MySQL wire protocol. The existing
`go-sql-driver/mysql` connects to it over TCP (or a unix socket) exactly as if it were
real MySQL — because it is receiving real MySQL protocol responses. The storage backend
can be anything: BoltDB, BadgerDB, flat files, anything.

**Why this is the right long-term architecture:**
- `go run .` starts IDUNA AND the storage layer. One command. No external process.
- When you need real MySQL (replication, prod ops, external tooling), change the DSN.
  Zero code changes. The wire protocol implementation becomes a mock you can swap out.
- External MySQL tooling (Workbench, sequel-ace, any MySQL client) can connect to IDUNA's
  built-in storage during development. No separate MySQL install needed.
- The migration files run unchanged — they're just SQL over the wire protocol.
- Custody is inside the binary. The binary is the supply chain.

**The library that already does this:** `dolthub/go-mysql-server` — a full MySQL-compatible
SQL engine + wire protocol server, embeddable in Go, pluggable storage backends. Used by
Dolt (git for databases). It's production-grade and handles the hard parts of the MySQL
protocol (handshake, auth, query parsing, result encoding).

**Why not right now:**
- `go-mysql-server` is a large dependency. It adds ~30MB to the binary and the SQL engine
  has quirks at the edges of MySQL compatibility.
- The storage adapter needs to be written: a struct that implements the `sql.Database`
  interface Dolt defines. That's real work.
- For Tyler's current needs (IAM tokens for one agent loop), this is 10x the complexity
  needed.

**Verdict:** Correct architecture. Implement when you need external tool access or
MySQL-specific features (JSON functions, replication). Not the fastest path to Tyler
authenticating today.

---

### Option C — Embedded SQLite (recommended for now)

Swap the storage backend to `modernc.org/sqlite` — a pure-Go SQLite implementation (no
CGO, no external binary, compiles into the IDUNA binary directly). IDUNA auto-detects:
if `MYSQL_DSN` is set, use MySQL. If not, create a local SQLite file and use that.

**Why this unblocks Tyler today:**
- `go run .` starts IDUNA with no MySQL dependency. The DB is a file next to the binary.
- `go run ./cmd/bootstrap` runs migrations against SQLite automatically.
- Tyler's agent credentials are written to `var/agent-secrets.env` as normal.
- The `IAMStore` interface is the firewall — swapping SQLite ↔ MySQL = swapping one file.

**What needs to change in the code:**
- Add `modernc.org/sqlite` to `go.mod`
- Write `internal/store/sqlite.go` — SQLiteStore implementing IAMStore
- Write a migration translator (a ~30-line function that adapts MySQL DDL to SQLite dialect)
- Patch `main.go` and `cmd/bootstrap/main.go` to detect embedded mode
- The SQL translation delta is small: `AUTO_INCREMENT` → `AUTOINCREMENT`, `INSERT IGNORE`
  → `INSERT OR IGNORE`, `ENGINE=InnoDB...` → remove, `TIMESTAMP(6)` → `TEXT`,
  `ON UPDATE CURRENT_TIMESTAMP(6)` → remove (handled in Go). Everything else is standard.

**The upgrade path to MySQL wire protocol (Option B):**
- The `IAMStore` interface doesn't change.
- When you're ready for Option B: implement `WireStore` or keep SQLiteStore but back it
  with `go-mysql-server`. The migration translator already exists. The SQL is already
  exercised.
- Swapping backends = one line in `main.go`.

**Verdict:** Implement now. Gets Tyler authenticated. Removes MySQL from the blast radius.
The wire protocol is the destination — SQLite is the bridge.

---

## Recommended Implementation Order

```
1. internal/store/sqlite.go          ← SQLiteStore implements IAMStore
2. internal/store/migrate_sqlite.go  ← SQL translator (MySQL DDL → SQLite DDL)
3. main.go                           ← auto-detect: no MYSQL_DSN → embedded SQLite
4. cmd/bootstrap/main.go             ← same detection, runs migrations against SQLite
5. go.mod                            ← add modernc.org/sqlite
6. migrations/truestore/             ← add tyler-agent seed migration
7. config/agents.json                ← add tyler-agent entry
```

After step 5, `go run .` starts IDUNA with no MySQL. Bootstrap runs. Tyler authenticates.
The human is no longer in the chain.

---

## On "We Have a Server"

The server is the right place for IDUNA to run permanently. The goal is:
- Server boots → systemd starts IDUNA → IDUNA starts its own storage → Tyler authenticates
- No human in that chain

With embedded SQLite, the systemd unit is trivially simple:

```ini
[Unit]
Description=IDUNA IAM Service
After=network.target

[Service]
EnvironmentFile=/etc/iduna/env
ExecStart=/opt/iduna/iduna
Restart=always
RestartSec=5s

[Install]
WantedBy=multi-user.target
```

`/etc/iduna/env` contains the env vars (ANTHROPIC_API_KEY, JWT_SECRET, JWT_ISSUER).
No MYSQL_DSN. IDUNA starts. Tyler authenticates.

When you're ready to move the DB to real MySQL (because you want replication, or external
tooling, or higher concurrency), add `MYSQL_DSN` to `/etc/iduna/env`. Zero code changes.

---

## Code

The prototype SQLite implementation is at:
- `IDUNA/internal/store/sqlite.go` — SQLiteStore
- `IDUNA/internal/store/migrate_sqlite.go` — SQL translator

Read those alongside this memo. The SQL delta is smaller than you think.

---

*IDUNA-OPS-001 | Emily Method applies: MySQL is not the foundation. The foundation is the*
*IAMStore interface. Build from there. The supply chain ends when the binary is self-sufficient.*
*Clean builds first.*
