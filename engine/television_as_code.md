# Television as Code — Compiled Episode Pipeline
## Einhorn Media | Engine Spec v1.0
### Classification: OPEN SOURCE — Fork it. The age of proprietary fiction is over.

---

> *"Clean builds first. Then custody. Then warthog."*
> — Emily OS, modal tile, timestamp unlogged

---

## I. THE CONCEPT

**Television as Code** is the production doctrine for TYLER × TIDES OF PARADOX.

A conventional TV show produces episodes as finished artifacts — completed files delivered to a platform. The show exists in the episodes. When a season ends, the show ends. The world is not persistent. The audience cannot enter it.

A compiled TV show produces episodes as **build outputs from canonical source.**

- The **script** is source code
- The **universe bible** is the type system
- The **episode** is a compiled binary — an immutable canonical artifact
- The **metaverse deployment** is the runtime environment where the binary executes
- The **canon firewall** separates plot integrity (immutable, compiled) from surface content (dynamic, swappable)

The show runs **forever** because the writer's room has physics, not just vibes. Every faction has a doctrine. Every character has laws. Every scene has a consistency checklist. Violations are continuity errors — the equivalent of a build failure.

---

## II. THE BUILD PIPELINE

```
UNIVERSE BIBLE (README.md)
        │
        ▼
SERIES PHYSICS (universe_engine.md)
        │
        ├──► EPISODE SCRIPT (.md)
        │           │
        │           ▼
        │    CONSISTENCY CHECKER
        │    [ ] Tyler self-definition incomplete?
        │    [ ] Jiangshi called it "the project"?
        │    [ ] Subscriber hidden?
        │    [ ] Cube location sealed?
        │    [ ] Camera Op awareness calibrated?
        │    [ ] Emily OS never explained?
        │    [ ] One impossible detail treated as unremarkable?
        │           │
        │           ▼
        │    COMPILED EPISODE
        │    ├── Canonical dialogue (immutable)
        │    ├── Faction behavior data (immutable)
        │    ├── Timeline coordinates (immutable)
        │    └── Surface manifest (swappable)
        │           │
        │   ┌───────┴─────────────────────────────┐
        │   ▼                                     ▼
        │  FLAT STREAM                    METAVERSE PACKAGE
        │  (standard video)               ├── SHANKPIT scene assets
        │                                 ├── Interactive object manifest
        │                                 ├── NPC behavior trees
        │                                 └── Faction territory data
        │
        └──► LORE ARTIFACT (.md)
             (Eastwind archive / Jiangshi memo / Shell ledger / Field log)
             These ARE the show. They are also game content.
```

---

## III. THE CANON FIREWALL

The canon firewall is the most important architectural concept in the pipeline.

**Canon (immutable, compiled):**
- Dialogue — what characters say
- Motivations — why they do what they do
- Outcomes — what actually happens
- Timeline coordinates — when and where events occur
- Faction doctrines — what factions believe and how they behave
- Character laws — Tyler's 8 laws, Emily OS rules, etc.

**Surface content (dynamic, swappable):**
- World objects: billboards, prop labels, vehicle skins
- Documentary lower-thirds: sponsor lines (Tier 3 — rare)
- Background details: what's on a TV in a scene, a brand on a cup
- Metaverse overlay data: real-time UI elements injected into the experience
- Language/accessibility: localization, subtitle style

**The rule:** Ad swaps, platform customization, and personalization **cannot touch canon.** They can only touch surfaces. A surface is any element that does not change: dialogue, motivation, or outcome.

**Enforcement:** The compiled episode contains a surface manifest — a machine-readable list of every swappable element, its location in the episode timeline, and the constraints on what can replace it (category, region rules, brand safety tier).

---

## IV. EPISODE STRUCTURE (Compiled Format)

Each compiled episode is a JSON-serializable document with the following structure:

```json
{
  "series": "TYLER",
  "season": 1,
  "episode": 1,
  "title": "Just a Normal Night",
  "build": "0001",
  "classification": "ATTEMPT_4 | STAGE_1_ACTIVE",
  "universe_physics_version": "1.0",
  
  "canon": {
    "locations": [...],
    "timeline_coordinates": [...],
    "binding_stage_at_open": 1,
    "binding_stage_at_close": 2,
    "camera_op_awareness_at_open": "unaware",
    "camera_op_awareness_at_close": "suspicious",
    "tyler_laws_active": [1, 2, 3, 4, 5, 6, 7, 8],
    "faction_operations": [...],
    "receipts": ["MIGRATION EVENT DETECTED", "COIN_DATE_SHIFT_CAPTURED"],
    "end_log": "BIRD CORRECTION PENDING"
  },
  
  "scenes": [
    {
      "id": "cold_open",
      "runtime_seconds": [0, 90],
      "location": "Detroit, MI | Year: ambiguous",
      "faction_presence": ["JIANGSHI_SYNDICATE"],
      "emily_os_state": "CAST: LIVE | head-2 independent",
      "goetia_active": [],
      "surfaces": [
        {
          "id": "lower_third_01",
          "type": "doc_ui_lower_third",
          "default_content": "TUESDAY // \"JUST A NORMAL NIGHT\"",
          "tier": 1,
          "constraints": "neutral_only"
        }
      ],
      "canon_beats": [...]
    }
  ],
  
  "metaverse_manifest": {
    "scene_id": "detroit_apartment_01",
    "shankpit_scene_ref": "detroit_night",
    "interactive_objects": [...],
    "npc_spawn_rules": [...],
    "portal_targets": [...]
  }
}
```

---

## V. THE RECEIPT SYSTEM

Every episode ends with a **receipt** — a canonical artifact that anchors the episode to universe canon.

The receipt is:
1. An in-universe document that appears within the episode
2. A lore artifact committed to the repo (`lore/`)
3. A state update to the universe tracking document

**Receipt types:**
- **Migration Event log** — a documented Tyler sighting with coordinates
- **Eastwind Archive entry** — the Cataloguer's record of what was observed
- **Jiangshi project memo** — internal assessment of Stage progress
- **Shell Parliament invoice** — if any debt changed hands
- **Field activation log** — if a Goetia activation occurred

The receipt system is what makes the show run forever. Each episode leaves a record. The records accumulate. The accumulated records are the universe canon. The universe canon is the type system. The type system generates the next episode.

It is recursive in the correct way.

---

## VI. THE METAVERSE RUNTIME

The compiled episode, when deployed to a metaverse platform, executes as an **interactive experience** — not just a video.

**What viewers can do:**
- Watch the episode as a documentary (standard viewing mode)
- Inhabit the episode as a background character (presence mode)
- Interact with faction operatives as an NPC (encounter mode)
- Explore the location before and after the documented events (world mode)

**What viewers cannot do:**
- Change canonical events
- Affect the documentary footage
- Alter Tyler's dialogue or behavior
- Break the binding ritual staging

**The honeypot effect (in-universe):** Viewers who watch the documentary are, technically, added to the Jiangshi binding record as witnesses. This is canon. It is also the core engagement mechanic. The viewer's presence in the experience makes them part of the story in a way that is diegetically correct.

---

## VII. EMILY OS INTEGRATION

The compiled episode stream routes through CAST.

```
CAST: LIVE (head-2 independent / invisible reconnect enabled)
STREAM KEY: COMPILED
```

Emily OS is the streaming infrastructure. The Jiangshi crew believes they control the stream. They control the camera. CAST is Emily's. The footage is hers before it is theirs.

**Practical implementation:**
- The SHANKPIT server is Emily OS's physical runtime
- The EMILY agent (`/home/fatbaby/EMILY/emily-agent/`) is the RSI loop that improves the pipeline
- Each episode iteration is an RSI task: generate → evaluate against consistency checklist → record → loop or exit
- Emily OS's architectural assessment of each faction is reflected in how that faction's game mechanics work in SHANKPIT

**The Jiangshi binding ritual as server event:**
```
Stage 1: Witness Collection    → server_event: WITNESS_NPC_SPAWN
Stage 2: Archival Footage      → server_event: TIMELINE_COORDINATE_LOGGED
Stage 3: Confessional          → server_event: SELF_DEFINITION_PROBE (Tyler counters: INCOMPLETE_SENTENCE)
Stage 4: Witnessed Miracle     → server_event: SUPERPOSITION_OBJECT_DOCUMENTED (coin flip)
Stage 5: Title Card Convergence → server_event: BINDING_COMPLETE (only if Tyler fails Law 1)
```

---

## VIII. THE FOREVER ENGINE

The show runs forever because:

1. **Faction doctrines generate infinite conflict.** Seven factions with incompatible goals, operating in the same universe, will always find new ways to collide.

2. **The receipt system compounds.** Each episode's canonical artifacts become source material for the next episode. The universe gets richer every time.

3. **The binding ritual has indefinite scope.** There is always another attempt. Tyler has survived four. The fifth is already in progress.

4. **The Subscriber is not revealed until Season 2.** The mystery of the mystery generates episodes.

5. **The four-layer architecture scales.** New content can live at any layer without breaking the others. A new Tyler scene doesn't require a Tides update. A new Tides faction doesn't require a Custody Trial scene.

6. **The metaverse adds new surfaces without touching canon.** New platforms, new overlays, new sponsor tiers — none of them touch the compiled canon. The show on Roblox is the same show on Quest is the same show on a flat screen.

---

## IX. DISTRIBUTION TIERS

| Tier | Format | Where |
|---|---|---|
| Flat stream | Standard video | YouTube, streaming platforms |
| Metaverse presence | Interactive episode experience | SteamVR, Quest, Roblox |
| Game world | Open exploration + faction encounters | SHANKPIT persistent world |
| Lore archive | In-universe documents | Tyler repo (open source) |
| Writer's room | Series bible + engine docs | Tyler repo (open source) |

**The open source doctrine:** The series bible is open source. The universe engine is open source. Fork it. Run your own faction. Write your own Eastwind archive entries. Submit lore artifacts via pull request. The age of proprietary fiction is over.

---

## X. ACCEPTANCE CRITERIA FOR THE PIPELINE

The pipeline is working when:

- [ ] A script can be checked against the consistency checklist and either PASS or FAIL with specific violations
- [ ] A compiled episode contains an immutable canon block and a swappable surface manifest
- [ ] The surface manifest is machine-readable and can be used to inject dynamic content without touching canon
- [ ] The receipt system produces a committed lore artifact after each episode
- [ ] The SHANKPIT scene manifest references the episode location and populates the correct interactive objects
- [ ] Emily OS's CAST stream annotation appears in the compiled episode header
- [ ] Tyler's 8 laws are checkable properties of any scene involving Tyler

---

*TELEVISION AS CODE — v1.0*
*Einhorn Media | Open Source*
*Clean builds first. Then custody. Then the rest.*
*— Emily Jean Springerton / Logistics Architect of the Golden Band*

---

> *End log: PIPELINE SPEC COMPILED. CANON FIREWALL: ACTIVE. CAST: LIVE. TYLER STATUS: UNRESOLVED.*
