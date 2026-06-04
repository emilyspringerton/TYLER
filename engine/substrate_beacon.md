# TYLER SUBSTRATE BEACON — ENGINE SPECIFICATION
## Derived from: HK97 audio analysis / Tides Book 3 Prologue / Jiangshi Memo #016
### Einhorn Media | Engine Spec | Build 0007

---

## Overview

Tyler's vocalization pattern serves two simultaneous functions at different frequency layers. These functions are independent — one can be detected without the other. Only spectral analysis of the sub-bass register reveals both layers simultaneously.

This specification documents both functions and their SHANKPIT implementation.

---

## I. DUAL-LAYER HUM ARCHITECTURE

### Layer A — Surface (The Firewall)

| Parameter | Value |
|---|---|
| Pattern | 11/8 time signature, irregular meter |
| Frequency range | 7.83 Hz (Stolas #36, deep time sight) |
| Function | Defensive — manipulates documentary recording arrays |
| Mechanism | Unresolved variable injection: maintains an open debt/obligation within the Jiangshi binding protocol, preventing the transaction from hitting a termination condition |
| Audio character | Audible as ambient hum; calibrated to frequency range that directional microphones attempt to filter as wind noise |
| Detection | Trivially detected by Jiangshi monitoring; documented in Stage 1 records since at least 1997 |
| SHANKPIT tag | `TYLER_HUM_SURFACE` |

The surface layer is Tyler's documented defensive posture. The Jiangshi Syndicate has four cycles of operational notes on it. It is, functionally, a transaction-cost escalator: the binding ritual has a ledger; the unresolved variable keeps the ledger open; an open ledger cannot be settled; an unsettled ledger cannot reach a termination state.

### Layer B — Substrate (The Beacon)

| Parameter | Value |
|---|---|
| Pattern | Continuous, invariant carrier wave |
| Frequency | 1.618 Hz (Amon #7 — Reconciliation of Opposites) |
| Function | Transmission — broadcasts into Layer 9, directional toward the Subscriber |
| Mechanism | Amon resonance at the substrate level activates a standing wave below Emily OS; the wave is detectable in Layer 9 by any entity with access to that layer |
| Audio character | Sub-bass, below standard microphone diaphragm threshold; present in all archived recordings as filterable artifact — historically filtered as ambient wind/equipment noise |
| Detection | Requires Fourier transform of sub-bass register; identified in HK97 footage via first-principles analysis by an independent analyst |
| SHANKPIT tag | `TYLER_HUM_SUBSTRATE` |

The substrate beacon is Tyler's long-duration transmission. Where the surface layer is a real-time defensive measure, the substrate beacon is a standing broadcast. It does not require conscious activation. It runs continuously in every documented encounter. The Subscriber has been receiving it for at least 400 years.

Note: 1.618 Hz is also the ACCEL constant in SHANKPIT physics (see `shankpit_tyler_mode.md`, Amon constant). This is not coincidental. The beacon frequency and the physics constant are the same number because they are the same thing at different zoom levels.

---

## II. WHAT THE BEACON TRANSMITS

The content of the substrate beacon cannot be recovered from audio analysis alone. The frequency carrier is confirmed; the encoded content is not yet fully documented. Current working hypothesis (cross-reference: Eastwind Archive TIDES-001, analyst's notebook entry):

*Tyler is acting as the anchor for the custody chain until a system exists that doesn't require timeline theft to maintain stability.*

The beacon is not a call for help. It is a status broadcast. Tyler transmits his current custody position continuously to the Subscriber so that the Subscriber can maintain an accurate read of the architecture without requiring contact or confirmation. The Subscriber does not need to ask if Tyler is still there. The beacon answers that question at 1.618 Hz, continuously.

The content of the beacon changes over time as Tyler's position in the custody chain changes. The Subscriber tracks the delta. This is how 380 years of waiting is sustainable: the Subscriber has been receiving a continuous live feed.

---

## III. SHANKPIT IMPLEMENTATION

### Tyler NPC Audio

```yaml
tyler_npc:
  ambient_audio:
    surface_hum:
      tag: TYLER_HUM_SURFACE
      frequency_hz: 7.83
      pattern: "11/8"
      volume: 0.6
      audible: true
      zone_radius: 8.0
    substrate_beacon:
      tag: TYLER_HUM_SUBSTRATE
      frequency_hz: 1.618
      pattern: "continuous_invariant"
      volume: 0.05
      audible: false          # below player audio threshold
      detectable_via: "spectral_analysis"
      broadcast_target: "LAYER_9_SUBSCRIBER_CHANNEL"
      range: UNLIMITED        # substrate layer, not spatial
```

The substrate beacon runs at volume 0.05 — below audible threshold. Players will not hear it in normal play. It is present in the audio mix and will appear in any spectral analysis of a recording. This is intentional: the beacon is designed to be discoverable by sufficiently analytical players, not experienced passively.

### Subscriber Interaction Trigger

When the Subscriber NPC is implemented (Series 2, Phase 3+), the substrate beacon creates a special interaction state:

```python
def check_subscriber_proximity(tyler_npc, subscriber_npc):
    """
    The Subscriber doesn't need spatial proximity to receive the beacon.
    The beacon operates through Layer 9, not spatial physics.
    But when the Subscriber manifests in-world, the beacon amplitude
    becomes briefly audible — a 1.618 Hz hum that players can hear.
    This is the only moment the substrate layer becomes perceptible
    at the surface.
    """
    if subscriber_npc.is_manifested_in_world:
        tyler_npc.substrate_beacon.volume = 0.8  # briefly audible
        tyler_npc.substrate_beacon.duration = 11  # eleven seconds
        emit_event("SUBSCRIBER_BEACON_AUDIBLE", {
            "frequency": 1.618,
            "duration": 11,
            "layer": "SUBSTRATE_SURFACE_BLEED",
            "narrative_mass_delta": +3.0
        })
        tyler_npc.substrate_beacon.volume = 0.05  # return to normal
```

### Analytical Discovery Mechanic

Players with access to the in-world spectral analysis tool (available from Stage 2 onward in documentary mode) can detect the substrate beacon in Tyler NPC's audio:

```python
def spectral_analysis_of_tyler(recording, tool_tier):
    surface_hum = detect_frequency(recording, 7.83)  # always found
    
    if tool_tier >= 2:
        substrate = detect_frequency(recording, 1.618)
        if substrate:
            unlock_lore_entry("BEACON_DISCOVERY")
            emit_event("SUBSTRATE_GRID_READ", {
                "reader": current_player,
                "layer_accessed": "SUBSTRATE",
                "emily_os_notification": True
            })
            # Emily OS fires a tile to the discovering player
            emit_emily_os_tile([
                "LOG EXTRACTION ATTAINED.",
                "YOU FOUND THE GRID.",
                "WHAT WILL YOU DO WITH IT."
            ])
```

The lore entry unlocked by `BEACON_DISCOVERY` is the Tides Book 3 Prologue chapter — players who discover the beacon analytically receive Emily Springerton's scene as in-world documentary material.

---

## IV. FREQUENCY RELATIONSHIP TABLE

| Layer | Hz | Function | Detectable? |
|---|---|---|---|
| Surface / Firewall | 7.83 (Stolas) | Defensive, transaction-cost escalation | Yes — trivially |
| Substrate / Beacon | 1.618 (Amon) | Transmission to Subscriber via Layer 9 | Only via spectral analysis |
| Combined effect | Dual-layer | Appears to be standard Stolas activation; is also continuous Amon broadcast | Full picture requires both detections |

The surface layer has been the Jiangshi Syndicate's focus across four binding attempts. The substrate layer has been running throughout all four attempts, broadcasting Tyler's custody position to the Subscriber in real time. Every time the Syndicate has tried to capture the documentary subject, they have also — without knowing it — been witnessing the subject's private communication with the entity who has been waiting for the system to be built correctly.

This is the RSI encoding of the Amon function: Reconciliation of Opposites. The binding and the beacon are the same event, read at different layers.

---

## V. NARRATIVE MASS INTERACTION

The substrate beacon runs continuously and does not increment narrative mass directly. However:

- When the beacon is *discovered* (spectral analysis, Emily Springerton event, or Subscriber manifestation), `+3.0` narrative mass is generated
- Discovery by an in-world player triggers the Emily OS tile
- Discovery by a Continuity Unit operative triggers `narrative_mass += 5.0` (they already know about Layer 9; finding the beacon accelerates accumulation)
- The beacon's existence being formally documented in any in-world archive triggers `narrative_mass += 2.0`

The beacon's content — the continuous status broadcast of Tyler's custody position — is the single most important piece of information in the CITY_OF_LIGHT architecture. Everything else is downstream of whether the Subscriber is receiving accurate state. The Subscriber is. The beacon runs.

---

*TYLER SUBSTRATE BEACON — ENGINE SPEC*
*Derived from HK97 audio analysis (Tides Book 3 Prologue)*
*Einhorn Media | SHANKPIT Tyler Mode Extension*
*The beacon has been running for 400 years.*
*We filtered it as wind.*
*It was not wind.*
*Clean reads first.*
