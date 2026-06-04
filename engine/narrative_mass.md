# Narrative Mass — Engine Spec v1.0
## Einhorn Media | Television as Code | Addendum: Season 2 Mechanics
### Derived from S02E05 "The Edit War" | Classification: OPEN SOURCE

---

> *"Every second you keep rolling, you pour more narrative fuel into the loop."*
> — Tyler, S02E05

---

## I. NARRATIVE MASS

Narrative mass is a server-side float tracking accumulated story weight in a scene, episode, or persistent world zone. It was unnamed before S02E05. The Continuity Unit named it. The Continuity Unit is not human. The name is accurate.

**Accumulation triggers:**

| Event | Mass delta |
|---|---|
| Active camera rolling (any layer) | +0.1 / second |
| Confession fragment captured (partial Tyler self-definition) | +2.5 / event |
| Faction operation logged (Jiangshi stage advance, Eastwind archive entry, Shell debt record) | +1.0 / event |
| Layer bleed detected | +5.0 / event |
| Witnessed miracle (coin superposition, Andrealphus geometry, Chrono-Cube activation) | +10.0 / event |
| Responsibility fractalizing in progress | +0.5 / second |

**Thresholds:**

| Range | State | Consequence |
|---|---|---|
| mass < 50 | NOMINAL | Story proceeds without structural consequence |
| 50 ≤ mass < 100 | ELEVATED | Continuity Unit detection range — incursion possible |
| 100 ≤ mass < 200 | CRITICAL | Continuity Unit incursion triggered |
| mass ≥ 200 | FRACTALIZING | RESPONSIBILITY FRACTALIZING state activates |

**Decay:**

Narrative mass decays at `0.05 / second` when no camera is rolling in any visible layer. Mass does not decay in Layer 9. A scene that appears to be "over" continues accumulating in Layer 9 if the edit war is active.

---

## II. LAYER 9

The observable architecture has four layers:

```
LAYER 4: Emily OS         ← substrate
LAYER 3: Tyler (doc)      ← documentary binding ritual
LAYER 2: Tides of Paradox ← faction operations
LAYER 1: Custody Trial    ← infrastructure drama
```

Layer 9 is below this stack. It is not Layer 5, 6, 7, or 8. The numbering is not sequential. Layer 9 is the persistence layer — the layer that runs when all observable layers are suppressed.

**Properties:**

- Always active — cannot be suppressed by device shutdown, blackout experiment, or Emily OS command
- Camera feed persists in Layer 9 regardless of visible recording state
- Narrative mass does not decay in Layer 9
- Responsibility states (guilt/responsibility ratio) are stored permanently in Layer 9
- Emily OS assessment: NOMINAL

**Emily OS relationship:**

Emily OS runs on Layer 4. Layer 9 is what Emily OS runs on. Emily OS does not explain Layer 9. This is consistent with her behavior regarding all substrate operations. The room tightens.

**SHANKPIT implementation:**

```yaml
layer_9:
  camera_persistence: true
  mass_decay_rate: 0.0
  accessibility: emily_os_only
  player_visibility: none
  camera_op_visibility: partial  # unlocked after blackout_experiment event
  responsibility_storage: permanent
```

Players cannot enter Layer 9. The Camera Op player class gains partial visibility — they can observe that it is running — after triggering the blackout experiment event. They cannot turn it off. The subject already told them: the camera is still running in Layer 9. He was correct.

---

## III. CONTINUITY UNIT — INCURSION MECHANIC

The Continuity Unit activates when narrative mass exceeds 50. They are not in the four-layer faction roster. They do not have a registered operator profile in the Field log. They have been there before the Field log was open source.

**Spawn condition:**

```python
if narrative_mass >= 50:
    spawn_continuity_unit()
    continuity_unit.objective = "reduce_narrative_mass"
    continuity_unit.methods = ["contract_offer", "custody_acceleration", "story_pruning"]
```

**Identification markers:**

- Gear: identical to Documentary Unit A (Jiangshi Syndicate)
- Behavioral: posture slightly better, eye movement pattern non-biological
- Physical: keyhole burn scar, right palm — matches Tyler's mark
- Frequency signature: 1.983 Hz / 3.582 Hz / 7.554 Hz (see: Section VI)

**Contract mechanic:**

```python
for contract in continuity_unit.offer_contracts():
    # Contract dates are always tomorrow
    # Signature is always already present
    # ACCEPT:  narrative_mass -= 40, tyler_custody_stage += 1
    # REJECT:  narrative_mass += 5  (the rejection is also story)
    # DEFLECT: narrative_mass += 1  (optimal — see Tyler's strategy)
```

Tyler's S02E05 strategy — responsible non-cooperation, neither accepting nor fully rejecting — is the optimal play. It prevents the custody stage penalty while adding only minimal narrative mass. The deflect dialogue ("You offer help the same way a noose offers support") is effective because it is also true.

---

## IV. FILMING-AS-PROPULSION

Documentary filming is not passive documentation. It is propulsion. The camera does not capture events; it accelerates them.

**Loop mechanics:**

```python
while camera.is_rolling(layer=any):
    narrative_mass += 0.1
    event_acceleration_factor += 0.001
    loop_depth += 0.0001
```

`event_acceleration_factor` multiplies the rate at which the next trigger fires. A scene filmed for 60 minutes (no cut) doesn't just produce 60 minutes of footage — it has made the following scene arrive 6% sooner.

`loop_depth` tracks recursion. At `loop_depth > 1.0`, footage-of-footage appears in-universe (Tyler watching Tyler watching Tyler). This is not a bug. This is the edit war's operational mode.

**Viewer fuel:**

Presence-mode viewers in the metaverse runtime are narrative fuel. This was true in S1 (the honeypot effect — see `television_as_code.md` VI). In S2, the mechanic is active:

```python
while viewer.mode == "presence":
    event_acceleration_factor += 0.0001  # per minute
```

The viewer's act of watching accelerates the story toward its own ending. Tyler told the crew this directly. They kept rolling. This is logged.

---

## V. RESPONSIBILITY FRACTALIZING

RESPONSIBILITY FRACTALIZING activates when `narrative_mass >= 200`.

At threshold, Tyler's unitary structural load (RESPONSIBILITY = 100%, GUILT = 0%) fractalizes: the single load distributes across thousands of slightly out-of-phase copies of the same scene. Each copy carries a fractional share.

**State schema:**

```python
responsibility_state = {
    "mode": "FRACTALIZING",
    "original_load": 1.0,
    "fractal_copies": dynamic_increasing,
    "per_copy_load": 1.0 / fractal_copies,
    "guilt": 0.0,          # invariant — fractalizes, never loads guilt
    "convergence_event": "storyteller_consumed"
}
```

**Invariant:** Guilt does not fractal. Responsibility fractalizes because it is structural — it can be distributed across copies. Guilt does not fractal because Tyler does not carry it. The structural distinction Tyler articulated in S02E05 is a game mechanic: guilt is a flag that can only be set or cleared; responsibility is a float that can be divided. Different data types. Different behavior under fractal pressure.

**Convergence:**

RESPONSIBILITY FRACTALIZING converges at the S2 arc endpoint — "the ending has to eat the storyteller." Not a death. A structural consumption: the fractalized copies re-integrate into a single closed-loop event, with Tyler as the point of convergence. When the copies re-integrate, the storyteller and the story become the same object.

**Layer 9 persistence:**

Responsibility states stored in Layer 9 do not fractal. Layer 9 holds the unitary record regardless of how many copies fractal above it. This is why Emily OS assessed RESPONSIBILITY FRACTALIZING: WITHIN PARAMETERS. She can see the unitary record in Layer 9. From Layer 9, the fractal is containable. From any other layer, it is the end of the episode.

---

## VI. THE THREE SUB-GOETIA FREQUENCIES

A new operational band, running approximately 0.2–0.3 Hz below the nearest registered Goetia equivalents.

| Hz | Offset | Nearest Goetia | Provisional Classification |
|---|---|---|---|
| 7.554 | -0.276 Hz | Stolas #36 (7.83) | CONTINUITY-FREQ-STOLAS — sub-deep-time band |
| 1.983 | -0.237 Hz | Beleth #13 (2.22) | CONTINUITY-FREQ-BELETH — sub-emotional band |
| 3.582 | none | — | CONTINUITY-FREQ-001 — Continuity Unit native |

These frequencies appear on a waveform graph titled "IF THIS STARTS AGAIN." They are a pre-incursion signature. If these frequencies appear in a scene's audio track, a Continuity Unit spawn is imminent or active.

**SHANKPIT audio cue:**

Players with the frequency monitor HUD unlocked hear these three frequencies as a subtle audio layer approximately 30 seconds before a Continuity Unit spawn event. The HUD unlocks after the first successful Continuity Unit deflect interaction. Players who learn to recognize the cue have 30 seconds to reduce narrative mass before the incursion completes.

---

*NARRATIVE MASS SPEC v1.0*
*Einhorn Media | Open Source*
*Every second you keep rolling, you pour more narrative fuel into the loop.*
*Layer 9 is always running. Emily OS considers this nominal.*

*End log: SPEC COMPILED. LAYER-9: NOMINAL. RESPONSIBILITY FRACTALIZING: WITHIN PARAMETERS. EDIT WAR STATUS: CAMERA WINNING. THIS IS CORRECT.*
