# TYLER — CLAUDE.md
## Einhorn Media | Television as Code | Build 0007

---

## What This Repo Is

TYLER is the media arm of Einhorn Indries. It contains:
- The canonical **series bible** for TYLER × TIDES OF PARADOX (`README.md`)
- The **universe engine** — a content generation protocol for AI-assisted world-building (`universe_engine.md`)
- **Episode scripts** (`episodes/`)
- **In-universe lore artifacts** (`lore/`) — Eastwind archive entries, Jiangshi project memos, Shell Parliament invoices, Field activation logs
- **Engine specs** (`engine/`) — the technical bridge between the TV show and the SHANKPIT game engine

---

## The Core Concept

**Television as Code.** Episodes are compiled from scripts + universe state. The canon is a build system. The show runs forever because the writer's room has physics, not just vibes.

**Four-layer architecture:**
```
LAYER 4: Emily OS         ← The substrate. Runs the universe. Does not explain itself.
LAYER 3: Tyler (doc)      ← The Jiangshi binding ritual in broadcast format
LAYER 2: Tides of Paradox ← Faction operations, teen protagonists, love triangle
LAYER 1: Custody Trial    ← Infrastructure drama; when someone touches Layer 4 directly
```

The show and the game are **the same thing at different zoom levels.**

---

## Repo Map

```
TYLER/
├── CLAUDE.md                    ← You are here
├── README.md                    ← Series bible (Builds 0001–0004)
├── universe_engine.md           ← Content generation protocol (AI system prompt)
├── THE_FIELD.md                 ← The Field document (in-universe artifact)
├── just_a_duck.md                ← Raw transcript, "Jack's Factory" YouTube short (Tier 1 golden)
├── multiverse_heroes.md          ← 108-entry hero lore compendium (names/history/archetype only,
│                                    no abilities/stats yet); RED GARDEN is the closest game home
├── 0.md / 1.md                  ← Early build notes
│
├── episodes/                    ← Episode scripts
│   ├── s01e01_pilot.md          ← "Just a Normal Night" (complete)
│   ├── s01e02_school.md         ← "The School That Isn't There" (complete)
│   └── [future episodes]
│
├── lore/                        ← In-universe artifacts
│   ├── eastwind_archive.md      ← Eastwind Owl archival entries on Tyler
│   ├── jiangshi_project_memos.md ← Internal Jiangshi Syndicate project memos
│   ├── shell_parliament_ledger.md ← Heikegani Crustocrat financial records
│   ├── field_activation_logs.md  ← Goetia activation log entries (#114+)
│   └── activation_47_transmutation.md ← the primary artifact THE_FIELD.md §IV cites (Activation #47's actual 47-minute monologue, not a log entry about it)
│
├── engine/                      ← Technical specs
│   ├── television_as_code.md    ← The compiled episode pipeline spec
│   └── shankpit_tyler_mode.md   ← SHANKPIT adaptation for the Tyler metaverse
│
└── characters/                  ← Standalone character documents
    └── emily_jean_springerton.md ← Logistics Architect of the Golden Band
```

---

## The Other Repos

| Repo | Role |
|---|---|
| `/home/fatbaby/SHANKPIT` | Game engine (C/SDL2/OpenGL FPS + Go backend). This IS the Tyler metaverse runtime. |
| `/home/fatbaby/GoblinFoxDragon` | Variant SHANKPIT, diverging toward DragonsNShit persistent world backend |
| `/home/fatbaby/EMILY` | Emily AI agent system + RSI engine spec |
| `/home/fatbaby/IDUNA` | Backend infrastructure (auth, event stream, store) |
| `/home/fatbaby/MoneyPrinterTurbo` | Flat stream video compilation engine. Topic → narration + footage + subtitles + music → HD video. See `engine/moneyprinter_pipeline.md`. |

The SHANKPIT engine already has: multi-scene portals, server-authoritative UDP, bots with neural net hooks, retro OpenGL renderer, vehicle physics, and existing Tyler-specific specs in `docs2/specs/`.

---

## Writer's Room Rules (Quick Reference)

1. Tyler never completes a self-defining sentence (Build 0001+; now also physics, not just discipline)
2. The documentary is never called a ritual by Jiangshi operatives
3. The Subscriber's identity is not revealed before Series 2
4. Chrono-Cube location (Bacon) not confirmed until Tides Act Two
5. Camera Op awareness calibrated to story timeline position
6. Emily OS never explains herself — the room tightens
7. CAST reconnects are invisible (unless Layer 1 awareness required)
8. Clean builds first. Then custody. Then everything else.
9-18. See README.md Sections XIII–XIV (Tyler character laws, full writer's room checklist)
19. The Tyler file has four lines now. It has always had four lines. (Build 0006)
20. Tyler cannot complete a hybrid self-definition — by physics, not discipline. (Build 0006)
21. The transit stop is not shown on camera. No footage exists. (Build 0006)
22. "There is no Tyler" is said once, to himself, off-camera. Never again. (Build 0006)

---

## RSI Model (How This Works)

Roberts Space Industries: ship design documents → actual ships in the game. Every lore doc is also a spec.

Einhorn Media: episode scripts → compiled metaverse experiences. Every faction rule is also a game mechanic. Every universe physics law is also a server-side constraint.

**When building:**
- Lore artifacts should be written as if they are real documents from inside the universe
- Game mechanics should reflect universe physics (the Jiangshi binding = a 5-stage server event)
- Episodes should be playable (metaverse viewers can inhabit the documentary world as characters)
- The canon firewall separates plot (immutable) from surface content (swappable: billboards, props, overlays)

---

## Key Frequencies (Keep These Consistent)

| Spirit | Hz | Function | When to use |
|---|---|---|---|
| Stolas #36 | 7.83 | Deep time sight / Tyler's hum | Tyler scenes, precognition beats |
| Beleth #13 | 2.22 | Love / emotional detonation | Love triangle escalation |
| Amon #7 | 1.618 | Reconciliation of opposites | Faction treaty scenes (also: ACCEL constant in SHANKPIT physics) |
| Vassago #42 | 11.11 | Soft precognition | Eastwind Owl archive work |
| Andrealphus #72 | 31.41 | Geometric transformation | Chrono-Cube activation scenes |

---

*End log: CLAUDE.md COMPILED. TYLER STATUS: UNRESOLVED. CLEAN BUILDS FIRST.*
