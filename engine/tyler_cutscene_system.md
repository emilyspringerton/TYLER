# TYLER Cutscene System
## FFXI-Style Dialogue Scene Spec v0.1 | Einhorn Media × SHANKPIT

*Written: 2026-06-12 | Status: spec only — implementation deferred to GoblinFoxDragon EduScript*

---

## Overview

FFXI-style cutscenes are triggered narrative sequences where gameplay pauses and the player
witnesses or participates in a scripted dialogue exchange. In TYLER Mode, cutscenes are the
primary way the universe communicates directly with individual players — not through UI,
not through ambient NPC behavior, but through a direct, undeniable scene that demands attention.

---

## Trigger Model

Cutscenes trigger when a player enters a trigger zone and the server decides the conditions
are met. Conditions include:
- Player has reached a faction trust threshold
- Server event is in a specific state (e.g., BINDING_RITUAL_ACTIVE at Stage 3)
- First time the player enters this zone (one-shot cutscenes)
- Time-based: event has been live for X minutes (urgency escalation cutscenes)
- Player-initiated: approaching an NPC and pressing USE

The server evaluates conditions — not the client. The client only knows the cutscene has started.

---

## Scene Structure

Each cutscene is a **scene script**: a JSON-defined sequence of lines, pauses, and choice
points. Example:

```json
{
  "id": "jiangshi_documentation_stage3",
  "title": "Stage 3: The Consent Form",
  "trigger": {"event": "BINDING_RITUAL_ACTIVE", "stage": 3, "player_zone": "detroit_apartment"},
  "one_shot": false,
  "lines": [
    {
      "speaker": "CAMERA OP",
      "text": "You're still here.",
      "pause_ms": 1200
    },
    {
      "speaker": "PRODUCER (V.O.)",
      "text": "This is the part where most people leave.",
      "pause_ms": 1500
    },
    {
      "choice": true,
      "prompt": "What do you do?",
      "options": [
        {"label": "Stay", "effect": "advance_stage", "line": "Good. We need a complete record."},
        {"label": "Leave", "effect": "trigger_awareness", "line": "Running is also documentation."}
      ]
    }
  ]
}
```

---

## Fields

### Scene-level
| Field | Type | Notes |
|-------|------|-------|
| `id` | string | Unique cutscene ID |
| `title` | string | Internal title (not shown to player) |
| `trigger` | object | Server-side trigger condition |
| `one_shot` | bool | True = plays once per player per session |
| `lines` | array | Ordered sequence of lines |

### Line-level
| Field | Type | Notes |
|-------|------|-------|
| `speaker` | string | NPC handle or `"SYSTEM"` / `"EMILY OS"` |
| `text` | string | Dialogue text |
| `pause_ms` | int | Delay after this line (default 1000ms) |
| `choice` | bool | If true, this is a choice point |
| `prompt` | string | Choice prompt shown to player |
| `options` | array | `{label, effect, line}` — player choices |

### Effects (choice outcomes)
- `advance_stage` — advance faction mechanic state
- `trigger_awareness` — NPC begins tracking player
- `grant_contact` — add contact to phone Contacts app
- `post_message` — send a phone message after cutscene ends
- `noop` — no mechanical effect; narrative only

---

## Client Implementation

When the server sends `PacketCutsceneStart` (type=8), the client:
1. Pauses player input (movement, shooting)
2. Dims the world (letterbox effect)
3. Shows speaker name + dialogue text in a box at the bottom of the screen
4. Advances through lines automatically (respecting `pause_ms`)
5. On choice: presents option buttons; waits for input
6. Sends `PacketCutsceneChoice` back to server with chosen option index
7. Server applies the effect; sends `PacketCutsceneEnd` (type=9)
8. Client restores normal gameplay

---

## SHANKPIT Scripting Audit

**Question:** Does SHANKPIT have scripting capabilities suitable for cutscene logic?

**Current state (2026-06-12):**
- SHANKPIT Go server has NPC awareness state machine (Jiangshi mechanics)
- Portal trigger system exists and is server-authoritative
- No scripting layer exists in the SHANKPIT repo

**GoblinFoxDragon EduScript (available):**
GoblinFoxDragon has an EduScript entity system with spawn/tick bindings
(commit `35ea513`: "Add EduScript entity system with spawn/tick bindings"). EduScript
is exactly the scripting layer needed for cutscene control:
- `spawn` binding: create NPC entities at trigger entry
- `tick` binding: advance dialogue line-by-line
- Entity lifecycle: NPC exists only for the duration of the cutscene

**Recommendation:** Cutscene execution should live in GoblinFoxDragon using EduScript,
with the SHANKPIT Go server routing trigger events to the GoblinFoxDragon runtime. This
respects the separation of concerns:
- SHANKPIT Go server: trigger detection (proximity, event state)
- GoblinFoxDragon/EduScript: scene execution (NPC spawn, dialogue, choices, effects)
- Client: rendering (dialogue box, choice UI, letterbox)

This is consistent with the WorldBackend interface design: SHANKPIT calls
`WorldBackend.OnPlayerEnterScene()` → GoblinFoxDragon handles scene lifecycle.

---

## Wire Protocol Additions

```
PacketCutsceneStart (type=8):
  [0]     type = 8
  [1:3]   scene_id_len (uint16 LE)
  [3:3+N] scene_id (UTF-8 string)

PacketCutsceneLine (type=9, server→client):
  [0]     type = 9
  [1]     line_index
  [2]     has_choice (0/1)
  [3:5]   text_len (uint16 LE)
  [5:5+N] text (JSON: {speaker, text, options[]})

PacketCutsceneChoice (type=10, client→server):
  [0]     type = 10
  [1]     choice_index

PacketCutsceneEnd (type=11, server→client):
  [0]     type = 11
  [1]     outcome_code (0=clean, 1=effect triggered)
```

---

## Implementation Phases

| Phase | What ships | Dependency |
|-------|-----------|-----------|
| Phase 1 | Scene script parser + server trigger eval | Go server event system |
| Phase 2 | Client letterbox + dialogue rendering | Client UI work |
| Phase 3 | Choice UI + PacketCutsceneChoice routing | Phase 2 + GoblinFoxDragon bridge |
| Phase 4 | EduScript integration for NPC spawn/tick | WorldBackend seam (Milestone 4) |
| Phase 5 | Phone message post-effects | Phone system (Phase 1) |

Phase 1 can be implemented as a pure Go data structure + evaluation loop with hardcoded
test scenes. No client changes required until Phase 2.

---

## Scene Storage

Scene scripts are stored in `TYLER/engine/scenes/` as individual JSON files, named by scene ID.
The game server loads scenes at startup from the configured `SCENES_DIR` path. Hot-reload via
`SIGHUP` allows scene edits without server restart.

The scene library is in the TYLER repo (narrative content) but read by the game server
(runtime logic). This reinforces the Television as Code philosophy: episode content and engine
logic are separate compilation units.
