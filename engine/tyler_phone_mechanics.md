# TYLER Phone Mechanics
## In-Game Smartphone System Spec v0.1 | Einhorn Media × SHANKPIT

*Written: 2026-06-12 | Status: spec only — no implementation yet*

---

## Overview

Every player in TYLER Mode carries a smartphone. The phone is a diegetic UI layer — all
interactions feel like using a real phone, not opening a game menu. The phone creates a
persistent, personal layer of the Tyler universe that responds to player actions, faction
activity, and server events.

The phone is toggled by the phone key (default: `F` on keyboard). A notification badge appears
at the edge of the screen when new content arrives — similar to how social media interrupts
attention, reflecting the show's themes.

---

## App Suite

### 1. Messages

Incoming messages from:
- **NPCs** (Jiangshi crew, faction contacts) — triggered by server events (BINDING_RITUAL_ACTIVE,
  player documentation stages, zone transitions)
- **System** — Emily OS transmissions (cryptic, redacted, or dangerously direct)
- **The Producer** — voice memo transcripts from the Jiangshi documentary crew

Message format: sender avatar + handle + message text + timestamp. No reply option for most NPCs
(they speak; the player witnesses). Some factions allow reply via preset options (see Contacts).

**Unread badge:** red dot on Messages app icon.

---

### 2. Contacts

Each faction has 1-3 contacts. Contact cards show:
- Handle (in-universe name, e.g. "CAMERA OP")
- Faction affiliation (displayed as an emoji/sigil)
- Last message preview
- **Trust level**: `observer` → `witness` → `bound` → `documented` (reflects faction mechanic
  progression for the Jiangshi; other factions have their own trust ladder)

Contacts accumulate as the player encounters factions across zones. The Contacts list is the
player's in-universe relationship graph.

**Preset reply options** (some contacts only): 3-4 short options presented when you open the
contact. Choosing one sends a reply and advances faction dialogue. This is the phone's primary
agency mechanic — the phone is how you talk to the universe.

---

### 3. Map

A stylized faction-territory map of the Tyler universe. Shows:
- Current zone (highlighted)
- Portal locations (→ exit arrows)
- Faction presence per zone (icon, not full detail — the map is a surveillance artifact;
  what it shows depends on who gave it to you)
- Pinned waypoints (set by NPC messages)

**Dynamic:** map updates when server events change zone state. During BINDING_RITUAL_ACTIVE,
the Detroit apartment zone is highlighted in the map. During the Eastwind Owls' archive access
event, the Cairngorms zone shows a new glyph.

Map is intentionally imprecise — it is a faction document, not a GPS.

---

### 4. Camera

Players can activate the camera to take in-world screenshots. Photos are stored to the local
in-game gallery (not persisted to disk — session only).

**Faction mechanic:** In Jiangshi zones, activating the camera triggers an escalated awareness
event. The Camera Op NPC begins tracking the player who "documented" something. This reverses
the power dynamic: the player becomes the documentarian.

**Documentation counter:** 10 photos taken in Jiangshi zone = full documentation reversal
(player receives the "Witness" title and the Jiangshi's awareness of them resets to baseline).

---

### 5. Notes

A plaintext scratchpad. No narrative mechanics — just a place for players to track their
own observations. Pre-populated with a single Eastwind Owls briefing note on first login:
*"The archive is not where you think it is. Start with what the building smells like."*

---

## Notification System

Notifications appear as banners at the top of the screen. Clicking opens the relevant app.
Types:
- **Message received** — NPC/faction message arrived
- **Zone alert** — server event changed zone state (faction presence updated, ritual stage changed)
- **Faction unlock** — new contact added to Contacts
- **Emily OS ping** — Emily OS direct communication (rare, high-priority)

**Anti-spam rule:** max 2 notifications per 30 seconds. Queued notifications are batched into
a summary banner.

---

## Server Wire Protocol

The phone system listens for server push packets. New packet type: `PacketPhoneEvent` (type=7).

```
PacketPhoneEvent layout (12 + N bytes):
  [0]     packet type = 7
  [1]     event_type  (1=message, 2=zone_alert, 3=contact_add, 4=emily_ping)
  [2]     sender_id   (0=system, 1-N=NPC ids)
  [3:7]   payload_len (uint32 LE)
  [7:7+N] payload (JSON: {type, handle, text, meta})
```

The payload is JSON for flexibility. The client renders it in the phone overlay.

---

## Implementation Phases

| Phase | What ships | Dependency |
|-------|-----------|-----------|
| Phase 1 | Messages app + notification banner | PacketPhoneEvent in Go server |
| Phase 2 | Contacts app + preset replies | NPC dialogue system |
| Phase 3 | Map app | Zone state sync protocol |
| Phase 4 | Camera + reversal mechanic | NPC awareness system |
| Phase 5 | Emily OS pings | Emily Prime TYLER integration |

Phase 1 can ship with hardcoded NPC messages triggered by existing server events
(BINDING_RITUAL_ACTIVE etc.). No new game mechanics required for Phase 1.

---

## Relationship to Cutscene System

The phone and the cutscene system are complementary. Cutscenes (see
`tyler_cutscene_system.md`) pause gameplay for dialogue. Phone messages arrive during live
play — they are the asynchronous channel. A cutscene might end with "check your phone" —
the NPC message arrives in the Messages app after the cutscene ends.
