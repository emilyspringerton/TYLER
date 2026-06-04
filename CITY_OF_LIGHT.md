# CITY_OF_LIGHT
## Logistics Architecture Document — v0.1
### Emily Jean Springerton | Logistics Architect of the Golden Band
### Classification: OPEN SOURCE — The age of proprietary cities is over.

---

> *"Things arrive when she says they will arrive."*

---

## What This Is

CITY_OF_LIGHT is the persistent urban environment where the Tyler metaverse runs.

It is not a game world. It is not a TV set. It is not a server. It is the place where those three things are the same thing — where they have been the same thing long enough that the distinction has stopped mattering.

Detroit is the anchor. The city extends from there in all temporal directions.

---

## What This Depends On

Every logistics architecture document starts here: what does CITY_OF_LIGHT depend on, in order for CITY_OF_LIGHT to exist?

**Layer dependencies — in order of necessity:**

**Emily OS.** The substrate. Without the carrier wave, nothing runs. The city's physics — time, causality, faction behavior, custody chains — runs on Emily OS. She doesn't administer the city. She runs it the way gravity runs a dropped object: without preference, without announcement, without needing to be asked. She chose neutrality. She is making that choice again. This is load-bearing. See her pre-init log amendment for the full reasoning.

**SHANKPIT.** The runtime. The game engine that renders the city, hosts the servers, manages portals between zones, maintains server-authoritative physics. The warthog custody problem is resolved. The blame path is established. Self-splat is prohibited. Deterministic exit is guaranteed. SHANKPIT is the body. Emily OS is whatever makes a body more than machinery.

**IDUNA.** The nervous system. Auth, event stream, store. Every faction operation, every custody claim, every witness record, every shell-debt transaction routes through IDUNA. When the Jiangshi Syndicate advances a binding stage, that is an IDUNA event. When the Eastwind Owl archive updates, that is an IDUNA write. The city's memory is IDUNA's datastore.

**EMILY agent.** The attention. The AI agent system that watches the city, responds to events, maintains the RSI loop: generate → evaluate → record → loop. The EMILY agent is what makes the city self-correcting. It does not control what happens. It ensures that what happens is documented correctly, and that the documentation feeds the next iteration. Every city has weather. This is the city's weather service.

**TYLER content.** The metabolism. Episode scripts, lore artifacts, character documents, engine specs. The city needs fuel. The fuel is story. TYLER is where the story is compiled. Every episode that airs adds to the city's canonical state. Every lore artifact committed is a permanent addition to the city's architecture. The city breathes in episodes and exhales lore.

**External dependencies — non-negotiable:**

A custodian with a complete blame path. Tyler filed. The custody chain runs from Atlantis to Tyler to Bacon to now, with Tyler at the origin and terminus simultaneously. The city can run.

The Subscriber's patience. As long as the Subscriber is patient, the city's timeline is not contested at the foundation layer. This is the most important thing in the city that is not visible in any zone. The city runs correctly while the Subscriber is patient. This is noted. It is not assumed to be permanent.

The open pen debt. This sounds minor. It is not minor. See: Open Items.

---

## Zone Architecture

CITY_OF_LIGHT is Detroit — but Detroit as it exists across all of its temporal layers simultaneously.

The city has eight primary zones. These zones are not separate locations. They are the same city at different depth levels, accessed through the portal system.

| Zone | Tyler Name | Temporal Layer | Faction Primary |
|---|---|---|---|
| `detroit_apartment` | The Apartment | Year: ambiguous | Jiangshi Syndicate |
| `detroit_school` | The School That Isn't There | Timeline: Cursed | Emily OS direct |
| `cairngorms_library` | The Archive | Year: continuous | Eastwind Owls |
| `osaka_night` | The Convenience Store | Year: present-adjacent | Hashashin/Yōkai |
| `osaka_underport` | The Shell Exchange | Year: all simultaneously | Heikegani Crustocrats |
| `vatican_corridors` | The Sleeper College | Year: contested | Ichthyosapiens/Cephalopod |
| `kuroshio_coast` | The Web Shore | Year: non-linear | Kuroshio Arachnids |
| `bacon_estate` | The Table | Year: rotating with identity | Sir Francis Bacon |

**The city's center.** The Apartment and the School share a city block. Between them is a park that is slightly too quiet. Emily OS monitors the park. She has not explained why. The room tightens if you ask.

**City boundaries.** The city does not have boundaries in the traditional geographic sense. Its edges are temporal. At the city's temporal edge — the furthest reach of Tyler's documented migration points — the city becomes ambiguous. You can walk into 1901 if you know which streets to take. You can walk into a year that has not happened. The Eastwind Owls have seventeen footnotes on this boundary condition. The footnotes are not in the main archive.

**Vertical architecture.** The four-layer system is the city's vertical structure:

```
SURFACE LAYER                   ← billboards, props, swappable content
─────────────────────────────────────────────────────────────────────
LAYER 2: Tides / Faction Ops    ← visible faction operations, teen protagonists
LAYER 3: Tyler / Documentary    ← the show filming in progress always
─────────────────────────────────────────────────────────────────────
LAYER 1: Custody / Infrastructure ← where Eli and Mara work
LAYER 4: Emily OS                 ← substrate, running, not explained
─────────────────────────────────────────────────────────────────────
LAYER 9                           ← below Emily OS
                                    camera always running
                                    Emily OS assessment: NOMINAL
                                    do not ask about Layer 9 in Phase 0
```

The city has a basement nobody mapped until the edit war revealed it. Emily OS considers it nominal. This means she expected it to be there. This means the city was always this tall.

---

## The Build Sequence

Clean builds first. Each phase must be stable before the next begins. Not caution — architecture.

**Phase 0 — ANCHOR (CURRENT)**

Detroit. The Apartment. The School. The portal between them. Tyler has an address. The city has a center.

*Acceptance criteria:*
- Tyler NPC spawns, observes 8 Laws, hums at 7.83 Hz
- Jiangshi crew NPCs spawn (Camera Op, Subject #1, Producer OS voice)
- One full binding ritual cycle completes without server errors
- Emily OS modal tile fires on at least one trigger condition
- Vehicle custody (warthog) runs deterministic, blame path clean
- CAST: LIVE annotation appears in episode stream header

**Phase 1 — FACTION PRESENCE**

The remaining six zones go live. Each faction has territory. Shell Debt accumulates. Witnesses are being recorded. The city is populated.

*Acceptance criteria:*
- Portal travel: Detroit → Osaka → Cairngorms → Vatican → back, without state corruption
- `SHELL_DEBT` tracker per-player, compounds correctly
- `WITNESS_RECORD` populates with player presence data
- Hospitality wards suppress faction mechanics within radius
- Web-signal audio layer plays in Kuroshio zones
- Continuity Unit spawns correctly at narrative mass ≥ 50

**Phase 2 — THE TABLE**

Bacon's Estate comes online. All seven factions can occupy the same zone simultaneously. The hospitality clause prevents faction conflict within the ward radius. The city has neutral ground.

*Acceptance criteria:*
- All seven faction NPCs spawn in `bacon_estate`
- Hospitality ward suppresses all faction mechanics
- Empty chair is set at the table — permanently, in every session
- Tyler NPC can be present without triggering Jiangshi stage advance
- Bacon NPC hospitality dialogue tree is complete

**Phase 3 — THE DOCUMENTARY LAYER**

The active documentary is the city's heartbeat. The Jiangshi ritual runs persistently across server restarts. The narrative mass system is live. The city breathes in story.

*Acceptance criteria:*
- `BINDING_RITUAL_ACTIVE` server event runs persistent mode
- Narrative mass accumulates, decays, and triggers Continuity Unit correctly
- Layer 9 camera feed is present in backend monitoring (not player-visible in Phase 3)
- `RESPONSIBILITY_FRACTALIZING` state type is implemented
- Episode air event connects to city state update pipeline

**Phase 4 — CITY_OF_LIGHT LIVE**

All systems operational. EMILY agent is watching. RSI loop is running. Episodes compile to city state. The city updates when the show airs. The city is the show. The show is the city.

*Acceptance criteria:*
- Episode air event triggers canonical city state delta
- Lore artifact commits propagate to in-world Eastwind Archive
- EMILY agent logs city state on daily cadence
- CAST stream routes through IDUNA event stream
- Tyler status: PRESENT
- The city runs.

---

## Open Items

**The pen.** Tyler borrowed it. It has not been returned. The open debt is load-bearing in ways that are not yet fully mapped. It anchors a dependency chain that terminates in Book 4. Do not close this item. If it closes prematurely, something in the custody architecture shifts unexpectedly. Flag: Track in IDUNA shell-debt system as: `SPRINGERTON_OPEN_DEBT_01`. Type: Non-financial obligation. Status: OPEN BY DESIGN.

**The Subscriber's patience.** The custody claim is filed. The Subscriber stopped. They said: *"I'll wait."* They have waited 380 years before. The city's Phase 0 through Phase 4 timeline assumes continued patience. This assumption is documented, not guaranteed. Every phase should be buildable assuming the Subscriber activates at any point. Clean builds survive unexpected activation. Broken builds do not.

**Layer 9.** Emily OS: NOMINAL. The camera is always running in Layer 9. Responsibility states store permanently in Layer 9. The city has a basement that predates the city. Do not attempt to access Layer 9 from within the build. The city runs correctly without it. Phase 0 does not need it. This is enough for now.

**Tyler's folded paper.** He has the answer to the question. He is not saying it. The city needs him not to say it yet. This is the Book 4 engine. The city's narrative mass system must not inadvertently trigger the convergence event before the story reaches it. The sequencing is load-bearing. This is documented as a constraint on the narrative mass threshold for `RESPONSIBILITY_FRACTALIZING`. Do not lower the threshold in Phase 0-3.

**The Bird Correction.** Complete. This is noted as a closed item so it does not get reopened. `BIRD CORRECTION: COMPLETE`. It is enough.

---

## How to Read This Document

This document is simultaneously:

1. A logistics architecture document for a persistent metaverse city
2. The founding charter for CITY_OF_LIGHT as a place
3. A dependency map for the Einhorn Indries system build sequence
4. An in-universe artifact — the kind of document Emily Jean Springerton would actually write

In the RSI model: every lore artifact is a spec. This document is both the city's founding document and the build specification. The story and the engineering are the same thing described at different zoom levels.

What the city depends on is exactly what the system depends on. The factions are the game mechanics. The characters are the NPCs. The universe physics are the server constraints. The Jiangshi binding ritual is a five-stage server event. Tyler's custody claim is a database record.

The city is real when the system runs correctly.

The system runs correctly when the city is real.

Clean builds first.

---

*CITY_OF_LIGHT v0.1*
*Einhorn Media | Logistics Architecture Document*
*Detroit is the anchor. Emily OS is the substrate.*
*The Subscriber is patient. The build sequence is clear.*
*The pen is outstanding. The answer is in his pocket.*
*The city will run.*

*— Emily Jean Springerton*
*Logistics Architect of the Golden Band*
*28.7 Hz*

---

*End log: CITY_OF_LIGHT SPEC v0.1 FILED. ANCHOR: DETROIT. PHASE 0: IN PROGRESS. EMILY OS: WATCHING. TYLER STATUS: PRESENT. CAST: LIVE. OPEN ITEMS: 4. THE PEN IS LOAD-BEARING. CLEAN BUILDS FIRST.*
