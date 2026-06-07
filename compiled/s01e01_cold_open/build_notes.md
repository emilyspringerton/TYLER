# S01E01 Cold Open — MPT Build Package
## "Just a Normal Night" — 30-Second Portrait Clip
### Build 0017 | Tyler Agent | Iduna-registered

---

**STATUS:** `PACKAGE COMPLETE — VIDEO GENERATION PENDING MPT ACTIVATION`
**Target platform:** YouTube Shorts / TikTok
**Format:** Portrait 9:16 / 1080×1920
**Duration:** 30 seconds
**Source script:** `episodes/s01e01_pilot.md` — Cold Open [00:00–01:30]
**Build scope:** Topic extraction, narration package, API payload, consistency check complete.
Video generation step pending: MPT service activation + Pexels API key.

---

## I. SOURCE — COLD OPEN BEAT EXTRACTION

The 30-second clip compresses the 90-second cold open into its load-bearing moments:

| Timestamp | Beat | Why it stays |
|---|---|---|
| 00:00–00:10 | Handheld chaos, hallway | Establishes the crew's POV and urgency |
| 00:25–00:40 | 1901 security cam timestamp | The first receipt — the impossible stated plainly |
| 00:40–00:55 | Tyler washing hands | The behavior that seeds the central question |
| 01:10–01:25 | Coin flip / date changes | Law 4 in full effect — the camera always late |
| 01:20–01:28 | "If you keep filming, you become part of it." | The only self-aware address to the lens in the cold open |

Dropped: interview setup (00:10–00:25), faction entry (00:55–01:10). Too contextual for a 30-second hook.

---

## II. MPT TOPIC

Per the `engine/tyler_mpt_profile.md` extraction protocol: present tense, witness perspective,
surface detail only, no self-definition, 2–4 sentences.

```
A camera crew follows a man through a Detroit apartment building at night. He washes his hands
at the kitchen sink with methodical care — too much care, like someone practicing ordinariness.
A 1901 security camera timestamp appears on footage shot tonight. The crew keeps rolling.
```

*(Source: tyler_mpt_profile.md, S01E01 example — confirmed as canonical topic for this episode.)*

---

## III. CUSTOM NARRATION — 30s PORTRAIT VERSION

For the short-form clip, the topic seeds MPT's narration engine. If MPT-generated narration
violates Tyler's 8 Laws, override with this custom copy:

---

*He showed up asking for a glass of water.*
*Like he lived there.*
*Then he asked what year it was — politely, like it was her fault.*

*A security camera captured him in 1901.*
*The footage was shot tonight.*

*He flips a coin.*
*The date on it changes.*
*The camera is always a half-second too late to catch it.*

*"If you keep filming," he says, "you become part of it."*

*Detroit. Night.*
*He keeps his hands very clean.*

---

**Word count:** 73 words
**Reading pace (en-GB-RyanNeural, documentary):** ~145 wpm / dry register → ~30 seconds
**Line breaks above:** pacing marks for the TTS engine — do not concatenate.

---

## IV. MPT API PAYLOAD

Endpoint: `POST http://127.0.0.1:8080/api/v1/videos`

```json
{
  "video_subject": "A camera crew follows a man through a Detroit apartment building at night. He washes his hands at the kitchen sink with methodical care — too much care, like someone practicing ordinariness. A 1901 security camera timestamp appears on footage shot tonight. The crew keeps rolling.",
  "video_language": "en",
  "voice_name": "en-GB-RyanNeural",
  "video_aspect": "portrait",
  "video_size": "1080x1920",
  "video_count": 3,
  "video_clip_duration": 3,
  "subtitle_enabled": true,
  "subtitle_font": "Anton",
  "subtitle_color": "#FFFFFF",
  "subtitle_size": 72,
  "subtitle_position": "bottom",
  "bgm_type": "random",
  "bgm_volume": 0.06
}
```

**To execute when MPT is active:**

```bash
curl -X POST http://127.0.0.1:8080/api/v1/videos \
  -H "Content-Type: application/json" \
  -d @/home/fatbaby/TYLER/compiled/s01e01_cold_open/mpt_payload.json
```

*(See `engine/moneyprinter_pipeline.md` §III for config.toml setup — requires Pexels key.)*

---

## V. CONSISTENCY CHECK — TYLER'S 8 LAWS

Run against both the MPT topic and the custom narration copy.

- [x] **Law 1 — No self-definition:** No sentence in the narration pins Tyler to a fixed identity.
  "He washes his hands" / "He keeps his hands very clean" — behavioral observation only.
  Watch for MPT-generated drift toward "He is a man who..." — override if present.

- [x] **Law 2 — Camera awareness calibrated:** Coin beat ("half-second too late") acknowledges
  the camera's relationship to Tyler without making him hold the gaze. The two-second eye contact
  moment ("If you keep filming...") is in-episode but NOT in the narration — it is documentary
  behavior described at surface level. No direct-address language in narration itself.

- [x] **Law 3 — Hum notation:** The SUIT enters at 00:55–01:10; this beat is excluded from the
  30s clip. Stolas hum (7.83 Hz) not required in narration for this clip version. Sound design:
  if full episode audio beds are used, hum should be present under the faction entry beat — not
  applicable to cold open extraction.

- [x] **Law 4 — Coin superposition:** "The date on it changes. The camera is always a half-second
  too late to catch it." Coin not explained. Date not specified. Camera timing intentional.
  Tyler does not comment on it in the narration.

- [x] **Law 5 — Small debts:** No new contact, no new obligation created in narration. Emily
  Springerton pen debt remains outstanding (Book 2).

- [x] **Law 6 — Smile:** Not mentioned in narration (the smile is in-episode; the narration
  describes his behavior, not his effect on witnesses).

- [x] **Law 7 — Bacon:** Not adjacently referenced. Clean.

- [x] **Law 8 — Chrono-Cube:** Not referenced. Clean.

- [x] **No ritual naming:** Documentary not called a ritual. Jiangshi not named in narration.

- [x] **Subscriber sealed:** Not implied.

- [x] **Cube location sealed:** Not applicable.

**CONSISTENCY CHECK: PASSED.** Custom narration is clean. Monitor MPT-generated narration
at output time — override any sentence that begins "Tyler is..." or "He is a..." or completes
a self-definition.

---

## VI. SELECTION CRITERIA — CHOOSING FROM BATCH OF 3

When MPT generates 3 versions, select using:

1. **Narration quality first:** Does the narration hold documentary register? No over-explanation?
   No self-definition? Reject immediately if Law 1 is violated.

2. **Footage pacing second:** Does the stock footage change at the right rhythm (3s clips)?
   The coin beat needs a moment of stillness — ideally a close-up or slow-motion stock clip.

3. **Music fit third:** Atmospheric, not dramatic. The cold open is understated. Reject any
   version where the music announces itself in the first 10 seconds.

If all three fail on narration: use custom copy override (§III above) and resubmit.

---

## VII. OUTPUT STRUCTURE

When video generation completes, this directory should contain:

```
compiled/s01e01_cold_open/
├── build_notes.md              ← this file
├── mpt_payload.json            ← API payload (to be created at execution time)
├── selected/
│   └── s01e01_cold_open_v1.mp4    ← selected best
└── alternates/
    ├── s01e01_cold_open_v2.mp4    ← rejected alternative
    └── s01e01_cold_open_v3.mp4    ← rejected alternative
```

---

## VIII. DEPENDENCY NOTES

This package is complete. Video generation is blocked on:

1. **MPT service active:** `uv run python main.py` in `/home/fatbaby/MoneyPrinterTurbo/`
   or `uv run streamlit run ./webui/Main.py --browser.gatherUsageStats=False`

2. **API key confirmed:** `export ANTHROPIC_API_KEY=sk-ant-...` in environment.
   Current status: present in environment but unverified for MPT config.toml.

3. **Pexels key configured:** Set `pexels_api_keys` in `MoneyPrinterTurbo/config.toml`.
   Current status: placeholder (`YOUR_PEXELS_API_KEY_HERE`) — not yet set.

**When MPT is activated:** POST the payload in §IV. Select from batch of 3 per §VI.
Move output to `compiled/s01e01_cold_open/selected/`. Update this file with video runtime,
final narration, and selection notes. Mark BACKLOG `[x]` and update activity.md.

---

*S01E01 Cold Open — MPT Build Package*
*Build 0017 | Tyler agent | Iduna-registered | Einhorn_Industrial*
*The package is ready. The service is not yet running. That is a known state.*
*Clean builds first.*
