# Tyler Mode — The Hum Mechanic
## SHANKPIT Implementation Spec v1.0
### Tyler × SHANKPIT | First Concrete Mechanic Bridge

---

> *"The hum is a 7/8 disruption field. Not a disguise. A frequency."*
> — Tyler's 8 Laws, Law 3

---

## What This Is

The Hum Mechanic is the first implementation bridge between the TYLER TV universe and the SHANKPIT game engine. It translates Tyler's Law 3 directly into a server-authoritative game mechanic.

**In the show:** Tyler hums when Jiangshi operatives or Kuroshio entities are near. The hum disrupts observation. It is not evasion — it is interference.

**In the game:** Players can activate a Hum, which projects a 7/8 disruption field around them. Jiangshi-faction NPC targeting degrades. Documentation accumulation slows. The field is server-authoritative and visible to other players as a faint audio/visual overlay.

This is not flavor. It is universe physics running in the engine.

---

## Server Event Model

### HUM_FIELD_ACTIVE

| Field | Value |
|---|---|
| Event name | `HUM_FIELD_ACTIVE` |
| Trigger | Player activates Hum emote (key: `H` by default) |
| Duration | 45 seconds (matches Law 3 consistency window) |
| Cooldown | 90 seconds |
| Radius | 6 game units (comparable to a small room) |
| Server authority | Yes — position, radius, and effect calculated server-side |

### Effect on Jiangshi NPCs

When a Jiangshi NPC is inside a player's active HUM_FIELD_ACTIVE radius:

| Jiangshi State | Normal behavior | During Hum |
|---|---|---|
| Unaware | Patrol | Patrol (no change) |
| Sighting | Approaches, locks camera on player | Stops approach at field edge |
| Documentation | Accumulates Documentation stack | Stack accumulation rate reduced 80% |
| Stage 3+ | Player is "being documented" — can't leave zone without ward | Ward requirement suspended while hum active |

The Jiangshi NPC does not show confusion or retreat. It simply cannot close the distance. This is intentional — the show never explains the hum. The game shouldn't either.

### Effect on Kuroshio Arachnid NPCs

When a Kuroshio NPC is inside the HUM_FIELD_ACTIVE radius:

- NPC silk-trap placement paused
- Thread-sensor range reduced to 0 (they cannot detect movement)
- NPC enters a kind of stillness — no aggression, no retreat
- On Hum expiry: normal behavior resumes

---

## Player Experience

### Activation

```
Player presses [H]
→ Client sends HUM_ACTIVATE UserCmd to server
→ Server: checks cooldown, creates HUM_FIELD entity (radius=6, duration=45s)
→ Server: broadcasts HUM_FIELD_START event to all players in zone
→ Client: plays hum audio (7.83 Hz drone, low volume, 3D positional)
→ Client: renders faint ring at player feet (subtle, not glowing — Tyler would not glow)
```

### Visibility rules

- Own hum: light audio + minimal VFX (the player knows they are humming)
- Nearby player's hum: faint drone heard within 8 units, no ring visible (you sense it)
- Jiangshi Camera Op (special NPC): can see all active Hum fields — the show says the camera is aware

### Cancel conditions

- Hum expires naturally after 45s
- Player dies (Hum field collapses)
- Player enters a no-hum zone (some zones in the Jiangshi territory are electromagnetically shielded — this is lore, not arbitrary)

---

## Coin Interaction (Law 4 crossover)

When a player activates the Hum while also in Superposition State (holding an unflipped coin — Law 4 mechanic, future spec), the field radius doubles to 12 units. This is the only cross-law multiplier and is intentionally the most powerful option.

It is also the most detectable by the Cataloguer NPC.

---

## SHANKPIT Go Implementation

### Files to modify

```
apps/server/faction/jiangshi.go      — NPC behavior tree: check HUM_FIELD_ACTIVE
apps/server/world/field_events.go    — HUM_FIELD entity lifecycle
apps/server/game/usercmd.go          — parse HUM_ACTIVATE from client
apps/server/game/player_state.go     — add CooldownHum, HumExpiry fields
apps/client/vfx/hum.go              — client-side audio/ring render
apps/shared/protocol/events.go       — HUM_FIELD_START / HUM_FIELD_STOP event defs
```

### New event types (apps/shared/protocol/events.go)

```go
const (
    EvtHumFieldStart = "HUM_FIELD_START"
    EvtHumFieldStop  = "HUM_FIELD_STOP"
)

type HumFieldEvent struct {
    PlayerID  uint32  `msgpack:"player_id"`
    X, Y, Z  float32 `msgpack:"x,y,z"`
    Radius    float32 `msgpack:"radius"`  // 6.0 or 12.0 (coin multiplier)
    ExpiresAt int64   `msgpack:"exp"`     // unix timestamp
}
```

### Player state addition (apps/server/game/player_state.go)

```go
type PlayerState struct {
    // ... existing fields ...
    HumActiveUntil  time.Time `json:"hum_active_until,omitempty"`
    HumCooldownUntil time.Time `json:"hum_cooldown_until,omitempty"`
    InSuperposition bool      `json:"in_superposition,omitempty"` // Law 4 setup
}

func (ps *PlayerState) CanHum() bool {
    return time.Now().After(ps.HumCooldownUntil) && ps.HumActiveUntil.IsZero()
}

func (ps *PlayerState) ActivateHum(coinMultiplier bool) {
    radius := float32(6.0)
    if coinMultiplier && ps.InSuperposition {
        radius = 12.0
    }
    duration := 45 * time.Second
    ps.HumActiveUntil = time.Now().Add(duration)
    ps.HumCooldownUntil = time.Now().Add(90 * time.Second)
    // Field entity creation happens in world.go
    _ = radius
}
```

### Jiangshi NPC behavior tree check (apps/server/faction/jiangshi.go)

```go
// In the NPC tick function, before approach/document logic:
if worldState.HasActiveHumInRadius(npc.TargetPlayer, npc.Position, 6.0) {
    // Player is humming — pause documentation accumulation
    npc.DocumentationAccumRate *= 0.20
    // Stop approach at field edge
    distToTarget := distance(npc.Position, target.Position)
    if distToTarget < humFieldRadius {
        npc.SetState(JiangshiState_Held)
        return
    }
}
```

---

## Acceptance Criteria

1. Player presses `H`, server creates HUM_FIELD entity in zone state
2. Jiangshi NPC within 6 units stops approaching (holds at boundary)
3. Documentation accumulation on any player within the field drops to 20% of normal
4. Hum expires after 45s; Jiangshi NPC resumes normal behavior
5. Cooldown prevents re-activation for 90s
6. Audio and minimal VFX play on activation (not announcing, not glowing)
7. Cross-law: with coin-in-superposition, radius = 12 units

**Out of scope for v1.0:**
- Kuroshio NPC stillness (needs Kuroshio faction NPCs to be added first)
- Camera Op visibility of Hum fields (needs Camera Op NPC implementation)
- Coin superposition state (Law 4 — future spec)

---

## Why This Mechanic First

The Hum is the lowest-coupling, highest-canon bridge:

1. **It's Tyler's most consistent visible behavior** — he hums in Season 1, Season 2, Season 3. It's the most documented of the 8 Laws.
2. **It requires no new NPC types** — Jiangshi NPCs are already specced. Just modify their behavior tree.
3. **It's server-authoritative** — no client-side cheating possible on a mechanic this important to the canon.
4. **It's testable** — spawn one Jiangshi NPC, activate Hum, verify approach stops. Done.

The coin mechanic is more dramatically important (Law 4) but requires more infrastructure (superposition state, date-change events). The Hum is the load-bearing dependency. Build the Hum first.

---

## RSI Receipts

This mechanic bridges:
- **TYLER** (TV show): Tyler's 8 Laws → game physics
- **SHANKPIT** (game engine): server-authoritative faction events
- **TIDES OF PARADOX** (Faction layer): Jiangshi documentation debuff system

When implemented, file:
- Eastwind TYLER-XXX: "First documented instance of the Hum Field becoming mechanically reproducible by parties other than the subject" (the Cataloguer has strong feelings about this)
- Field Activation Log: `HUM_FIELD_ACTIVE` added to Goetia event registry (Stolas #36 / 7.83 Hz operational)
- Shell Parliament: New account type — Field Replication Fees (any non-Tyler use of the hum generates a small Shell Mark debt)

---

*Tyler Mode / Hum Mechanic Spec v1.0*
*Build: 0019-pending*
*The hum is not an ability. It is a frequency that exists independent of the player.*
*The mechanic is an approximation. The real thing is older.*
