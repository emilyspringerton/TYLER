# Tyler MPT Generation Profile
## Einhorn Media | MoneyPrinterTurbo Configuration Standard
### Build 0015 | Flat Stream Pipeline

---

> *"The flat stream is still the show. Surface content, swappable. Canon, immutable."*

---

## PURPOSE

This document defines the standard generation parameters for Tyler × Tides of Paradox episode
compilations using MoneyPrinterTurbo. These parameters apply to all flat stream output
(YouTube, streaming platforms, short-form distribution).

They are not suggestions. They are the build configuration.

---

## STANDARD PROFILE: TYLER DOCUMENTARY (LANDSCAPE 16:9)

For full episodes and long-form clips.

| Parameter | Value |
|---|---|
| `video_language` | `en` |
| `video_aspect` | `landscape` |
| `video_size` | `1920x1080` |
| `voice_name` | `en-GB-RyanNeural` |
| `voice_volume` | 1.0 |
| `bgm_type` | `random` |
| `bgm_volume` | 0.08 |
| `subtitle_enabled` | `true` |
| `subtitle_font` | `Anton` |
| `subtitle_color` | `#FFFFFF` |
| `subtitle_size` | 60 |
| `subtitle_position` | `bottom` |
| `video_clip_duration` | 4 |
| `video_count` | 3 |
| `video_source` | `pexels` |

**Why these choices:**
- `en-GB-RyanNeural` — dry, precise, documentary register; sits under the footage rather than above it
- `bgm_volume 0.08` — atmospheric, not competing with narration
- `video_clip_duration 4` — matches documentary cut rhythm; slower than commercial content
- `video_count 3` — batch of 3, select best against Tyler laws consistency check

---

## STANDARD PROFILE: TYLER SHORTS (PORTRAIT 9:16)

For cold opens, clips, and short-form distribution (YouTube Shorts, TikTok).

| Parameter | Value |
|---|---|
| `video_language` | `en` |
| `video_aspect` | `portrait` |
| `video_size` | `1080x1920` |
| `voice_name` | `en-GB-RyanNeural` |
| `voice_volume` | 1.0 |
| `bgm_type` | `random` |
| `bgm_volume` | 0.06 |
| `subtitle_enabled` | `true` |
| `subtitle_font` | `Anton` |
| `subtitle_color` | `#FFFFFF` |
| `subtitle_size` | 72 |
| `subtitle_position` | `bottom` |
| `video_clip_duration` | 3 |
| `video_count` | 3 |
| `video_source` | `pexels` |

**Why smaller `bgm_volume` for shorts:** Mobile playback; the music competes more on small speakers.

---

## TOPIC EXTRACTION PROTOCOL

The MPT topic is extracted from the episode script's cold open description. Rules:

1. **Present tense.** MPT performs better with present-tense descriptions.
2. **Witness perspective.** Write from the documentary crew's point of view — what they are observing, not what is canonically happening.
3. **Surface detail only.** The topic describes surfaces: what the camera sees. Not Tyler's internal state. Not the binding ritual. Not the faction's operational intent.
4. **No self-definition.** The topic must not complete a Tyler self-definition. Tyler's 8 laws apply to the narration the topic seeds.
5. **Length:** 2–4 sentences.

### Template

```
[Setting: what the camera sees, where it is, what time it is.]
[Subject behavior: what Tyler is doing, described as documentary observation.]
[Impossible detail: one thing that is wrong, stated matter-of-factly.]
[Crew state: optional — what the crew is experiencing, one sentence.]
```

### Examples

**S01E01 "Just a Normal Night" topic:**
> A camera crew follows a man through a Detroit apartment building at night. He washes his hands at
> the kitchen sink with methodical care — too much care, like someone practicing ordinariness. A
> 1901 security camera timestamp appears on footage shot tonight. The crew keeps rolling.

**S01E02 "The School That Isn't There" topic:**
> A school has appeared overnight on a vacant lot in Detroit that has been empty for eleven years.
> Students are arriving for classes in a building whose brick is wrong for the decade. A man in a
> plaid jacket stands across the street and watches like he has been expecting this. The weeds at
> the base of the chain-link fence are old enough that the school has always been there.

**S01E03 "The Confessional" topic:**
> A documentary crew has set up a confessional interview in a Detroit hotel room. The subject has
> been answering questions for forty minutes. None of the answers have completed a sentence about
> who he is. A secondary audio frequency — 2.22 Hz — appears in the recording equipment that has
> no documented source. The Camera Op has started writing by hand.

---

## CONSISTENCY CHECK (POST-GENERATION)

Before accepting any MPT output, verify against Tyler laws:

- [ ] **Law 1:** Narration does not complete a Tyler self-definition. Watch for: "Tyler is a...", "He is...", any sentence that pins him to a fixed identity.
- [ ] **Law 2:** If Tyler appears in narration, he is not described as looking directly into camera for more than 2 seconds (except in designated taunt beats).
- [ ] **Law 3:** Stolas hum (7.83 Hz) described as present in any scene with Jiangshi or Kuroshio presence.
- [ ] **No ritual naming:** The documentary is not called a ritual in any narration the Jiangshi crew would hear.
- [ ] **Subscriber sealed:** Subscriber identity not implied.
- [ ] **Cube location sealed:** Bacon's custody of the Cube not confirmed before Tides Act Two.

If MPT-generated narration violates any of these: override with custom copy. The LLM does not know the laws. The pipeline knows the laws.

---

## LOCAL MATERIALS (SHANKPIT INTEGRATION — FUTURE)

When SHANKPIT Tyler-mode renders scene output, replace Pexels footage with local materials:

```toml
[app]
video_source = "local"
local_video_dir = "/home/fatbaby/TYLER/shankpit_renders/<scene_id>/"
```

This makes the game engine the visual production pipeline. The show looks like the game because
the show is the game at a different zoom level.

See `engine/shankpit_mpt_bridge.md` (not yet written).

---

## COMPILED OUTPUT STRUCTURE

```
TYLER/compiled/
├── s01e01_cold_open/     ← 30s portrait clip
├── s01e01/               ← full episode landscape
├── s01e02_cold_open/     ← 30s portrait clip
├── s01e02/               ← full episode landscape
├── s01e03_cold_open/     ← 30s portrait clip
└── s01e03/               ← full episode landscape
```

Each directory contains: the selected MP4, the two rejected alternatives (for reference), and
a `build_notes.md` recording: which topic was used, which batch was selected, any narration
overrides applied, consistency check results.

---

*TYLER MPT GENERATION PROFILE — Build 0015*
*Einhorn Media | Flat Stream Pipeline*
*The profile is the law. The law runs the build.*

---

> *End log: MPT PROFILE: COMPILED. TOPIC EXTRACTION: DOCUMENTED. CONSISTENCY CHECK: DEFINED. FLAT STREAM: PENDING FIRST BUILD.*
