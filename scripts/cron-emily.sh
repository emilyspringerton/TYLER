#!/bin/bash
# cron-emily.sh — Cron-safe wrapper for emily.sh (Tyler RSI loop)
#
# Runs one RSI iteration. Safe to call from crontab every 4 hours.
# Checks IDUNA is alive before running (IDUNA must be up for Apple posting).
# Lock-file guarded — concurrent runs are skipped, not queued.
#
# Crontab entry:
#   0 */4 * * * /home/fatbaby/TYLER/scripts/cron-emily.sh >> /home/fatbaby/TYLER/var/cron.log 2>&1
#
# Requires:
#   IDUNA running at http://localhost:8080 (or IDUNA_BASE_URL)
#   ANTHROPIC_API_KEY in environment (set in crontab or sourced from .env)

set -euo pipefail

LOCK_FILE="/tmp/tyler-emily-sh.lock"
LOG_PREFIX="[$(date '+%Y-%m-%d %H:%M:%S')] cron-emily:"
BASE_URL="${IDUNA_BASE_URL:-http://localhost:8080}"
TYLER_DIR="/home/fatbaby/TYLER"
SECRETS="/home/fatbaby/IDUNA/var/agent-secrets.env"

log() { echo "$LOG_PREFIX $*"; }

# ── Lock guard ────────────────────────────────────────────────────────────────

if [ -f "$LOCK_FILE" ]; then
  LOCK_PID=$(cat "$LOCK_FILE" 2>/dev/null || echo 0)
  if kill -0 "$LOCK_PID" 2>/dev/null; then
    log "skip — already running (PID $LOCK_PID)"
    exit 0
  fi
  log "stale lock file removed (PID $LOCK_PID no longer exists)"
  rm -f "$LOCK_FILE"
fi

echo $$ > "$LOCK_FILE"
trap 'rm -f "$LOCK_FILE"' EXIT

# ── IDUNA check ───────────────────────────────────────────────────────────────

if ! curl -sf "${BASE_URL}/api/v1/agents" --max-time 5 >/dev/null 2>&1; then
  log "skip — IDUNA not reachable at ${BASE_URL} (Apple submission would fail)"
  log "  Start IDUNA: cd /home/fatbaby/IDUNA && go run . &"
  exit 0
fi
log "IDUNA: reachable at ${BASE_URL}"

# ── Export IDUNA credentials ──────────────────────────────────────────────────

if [ -f "$SECRETS" ]; then
  # shellcheck disable=SC1090
  source "$SECRETS"
  export IDUNA_BASE_URL="$BASE_URL"
  export IDUNA_AGENT_NAME="TYLER"
  export IDUNA_AGENT_SECRET="${IDUNA_SECRET_TYLER:-}"
  log "IDUNA credentials loaded (agent: TYLER)"
else
  log "WARNING: secrets file not found at $SECRETS — Apple posting disabled"
fi

# ── Git pull ──────────────────────────────────────────────────────────────────

log "git pull TYLER..."
cd "$TYLER_DIR"
git pull --rebase origin main --quiet 2>&1 | sed "s/^/$LOG_PREFIX git: /"

# ── Run emily.sh (1 iteration) ────────────────────────────────────────────────

PENDING=$(grep -c '^\- \[ \]' BACKLOG.md 2>/dev/null || echo 0)
if [ "$PENDING" -eq 0 ]; then
  log "backlog empty — nothing to do"
  exit 0
fi

log "running emily.sh — $PENDING tasks pending"
mkdir -p var/

bash emily.sh 1 2>&1 | tee -a var/cron.log | sed "s/^/$LOG_PREFIX /"
log "emily.sh completed"

# ── Git push ──────────────────────────────────────────────────────────────────

git push origin main --quiet 2>&1 | sed "s/^/$LOG_PREFIX git push: /" || log "git push failed (non-fatal)"
log "done"
