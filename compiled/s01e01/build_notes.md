# S01E01 Full Episode — MPT Build Package
## "Just a Normal Night" — Landscape Compilation
### Build 0020 | Tyler Agent | Iduna-registered

---

**STATUS:** `PACKAGE COMPLETE — VIDEO GENERATION PENDING: COLD OPEN CONFIRMATION + MPT ACTIVATION`
**Target platform:** YouTube / streaming platforms
**Format:** Landscape 16:9 / 1920×1080
**Duration target:** 90–120 seconds (documentary summary register)
**Source script:** `episodes/s01e01_pilot.md` — full episode
**Build scope:** Topic derived, narration written, API payload compiled, consistency check passed.
Video generation blocked on: (1) cold open clip confirmed working, (2) Pexels API key set,
(3) MPT service active.

**To fire when prerequisites are met:**
```bash
./compiled/mpt_activation.sh --full-episode
```

---

## I. DEPENDENCY NOTE

This package depends on the cold open clip (Build 0017) being confirmed working first.
The cold open is `[~]` — package complete, video pending Pexels key.

Once the cold open generates cleanly:
1. Review cold open output per `compiled/s01e01_cold_open/build_notes.md §VI`
2. Select best cold open version → move to `compiled/s01e01_cold_open/selected/`
3. Mark cold open `[x]` in BACKLOG.md
4. Fire full episode: `./compiled/mpt_activation.sh --full-episode`

The activation script already has `fire_full_episode()` defined. The payload at
`compiled/s01e01/mpt_payload.json` is now ready.

---

## II. EPISODE ARC — BEAT EXTRACTION

S01E01 covers Stages 1 → 2 of the Jiangshi binding protocol. The full episode arc:

| Segment | Timestamp | Narrative beat | Inclusion |
|---|---|---|---|
| Cold open | 00:00–01:30 | First encounter; 1901 timestamp; coin; "you become part of it" | Summarized |
| Production van | 01:30–03:00 | Crew context; hum on every mic | Summarized |
| First interview (Subject #1) | 03:00–06:00 | Witness collection; acceptance | Compressed |
| Archive footage introduction | 06:00–09:00 | Stage 2 initiated; Eastwind first frame | Compressed |
| Tyler / Suit confrontation | 09:00–14:00 | "You only rename it"; faction presence | Summarized |
| Camera Op awareness escalation | 14:00–19:00 | First unease; Stage 1 closing | Compressed |
| End log | 22:00–25:00 | BIRD CORRECTION PENDING; Stage 2 initiated | Referenced |

The MPT topic seeds footage selection. The custom narration (§IV) provides the canonical
voice track for override if MPT generates a Law-violating narration.

---

## III. MPT TOPIC

Per `engine/tyler_mpt_profile.md` — 3–5 sentence present-tense witness perspective.
No self-definition. Surface behavior only.

```
Tyler — a man who refuses to be documented — is followed by a camera crew through a Detroit
night. He washes his hands too carefully. A security camera placed him in this city in 1901;
the footage was shot tonight. A coin in his pocket carries a date that keeps changing. The
camera is always half a second too late to catch it. The crew keeps filming.
```

*(Source: derived from BACKLOG.md task spec + pilot episode cold open.)*

---

## IV. CUSTOM NARRATION — LANDSCAPE 90s VERSION

For override when MPT-generated narration violates Tyler's 8 Laws.
Designed for documentary register at 145 wpm → approximately 90–100 seconds with
dramatic pauses.

---

*Detroit. Night. A documentary crew has been following a man named Tyler.*

*They hired a crew. They rented a van. They made a production plan.*

*Then they found out what they were documenting.*

*A security camera placed him in this city in 1901.*
*The footage was shot tonight.*
*Both things are true.*

*Tyler washes his hands at a kitchen sink with methodical care.*
*The kind of care that looks like habit.*
*Or practice.*
*Or a very old necessity.*

*He knew the camera was there.*
*He was waiting for it.*

*He flips a coin.*
*The date on the face changes.*
*The camera is always half a second late to catch it.*

*Someone in a clean suit tells him they can end this quietly.*

*Tyler doesn't turn.*

*"You've never ended anything," he says.*
*"You only rename it."*

*The crew keeps filming.*

*The end log reads: BIRD CORRECTION PENDING.*
*The archive records the coin as active since 1623.*

*Nobody has counted right yet.*

*But the crew is still in the van.*
*The hum is on every mic.*
*Even the ones not pointed at him.*

---

**Word count:** 163 words
**Reading pace (en-GB-RyanNeural, documentary register):** ~145 wpm → ~67 seconds narration
**With dramatic pauses (marked by line breaks):** ~90–100 seconds total runtime
**Line breaks above:** pacing marks for TTS — do not concatenate.

---

## V. MPT API PAYLOAD

Endpoint: `POST http://127.0.0.1:8080/api/v1/videos`

```json
{
  "video_subject": "Tyler — a man who refuses to be documented — is followed by a camera crew through a Detroit night. He washes his hands too carefully. A security camera placed him in this city in 1901; the footage was shot tonight. A coin in his pocket carries a date that keeps changing. The camera is always half a second too late to catch it. The crew keeps filming.",
  "video_language": "en",
  "voice_name": "en-GB-RyanNeural",
  "video_aspect": "landscape",
  "video_size": "1920x1080",
  "video_count": 3,
  "video_clip_duration": 5,
  "subtitle_enabled": true,
  "subtitle_font": "Anton",
  "subtitle_color": "#FFFFFF",
  "subtitle_size": 60,
  "subtitle_position": "bottom",
  "bgm_type": "random",
  "bgm_volume": 0.08
}
```

**To execute when cold open is confirmed and MPT is active:**

```bash
./compiled/mpt_activation.sh --full-episode
```

Or directly:
```bash
curl -X POST http://127.0.0.1:8080/api/v1/videos \
  -H "Content-Type: application/json" \
  -d @/home/fatbaby/TYLER/compiled/s01e01/mpt_payload.json
```

---

## VI. CONSISTENCY CHECK — TYLER'S 8 LAWS

Run against both the MPT topic and the custom narration copy.

- [x] **Law 1 — No self-definition:** Tyler is described by behavior only.
  "He washes his hands with methodical care" / "He knew the camera was there" —
  observation of action, not statement of identity. "A man named Tyler" is naming, not defining.
  Watch MPT-generated output for "Tyler is a..." or "He is someone who..." — override immediately.

- [x] **Law 2 — Camera awareness calibrated:** "He knew the camera was there. He was waiting for it."
  This is Stage 1 (witness collection, 60% complete) — oblique acknowledgment is correct.
  No direct gaze language in narration. The two-second sustained look is in-episode; the
  narration describes his anticipation, not his direct address to the lens.

- [x] **Law 3 — Hum present:** "The hum is on every mic. Even the ones not pointed at him."
  Stolas 7.83 Hz noted in narration. Not explained. Tyler does not comment on it. Correct.
  Jiangshi crew is present (they own the production van) — hum notation required.

- [x] **Law 4 — Coin superposition:** "The date on the face changes. The camera is always half
  a second late to catch it." Coin not explained. Date not revealed. Camera timing intentional.
  Tyler does not comment on the coin in narration.

- [x] **Law 5 — Small debts:** No new contact in narration. Emily Springerton pen debt
  outstanding (Book 2). No new obligations created.

- [x] **Law 6 — Smile:** Not in narration. Smile is in-episode; the narration describes
  behavior at the surface level only.

- [x] **Law 7 — Bacon:** "The archive records the coin as active since 1623." Coin anchor
  to 1623 is documented. Bacon not mentioned. No location implied.

- [x] **Law 8 — Chrono-Cube:** Not referenced. 1623 noted as coin anchor only,
  not as Cube handoff event. Clean.

- [x] **No ritual naming:** Documentary not called a ritual. Jiangshi not named in narration
  (referenced as "crew" / "someone in a clean suit").

- [x] **Subscriber sealed:** Not implied.

- [x] **Cube location sealed:** Not applicable.

**CONSISTENCY CHECK: PASSED.** Custom narration is clean.
Monitor MPT-generated narration at output time — override any sentence that begins
"Tyler is..." or "He is a man who..." or attempts to complete his identity.

---

## VII. SELECTION CRITERIA — CHOOSING FROM BATCH OF 3

When MPT generates 3 landscape versions, select using:

1. **Narration quality first:** Documentary register maintained? No over-explanation?
   No self-definition completed? Reject immediately if Law 1 is violated.
   Use custom narration override (§IV) if all three fail.

2. **Footage pacing second:** 5-second clips for landscape — does the footage breathe?
   Urban night footage preferred (Detroit context). Avoid obviously cheerful stock footage.
   The coin beat needs stillness — close-up or slow-motion clip.

3. **Music fit third:** Atmospheric undercurrent. Not dramatic. Not triumphant.
   The full episode register is understated and accumulating. Reject any version where
   the music announces itself in the opening 15 seconds.

4. **Landscape-specific check:** Is the 16:9 framing well-used? MPT shouldn't letterbox
   or crop awkwardly. The landscape format should feel like a deliberate choice, not a
   portrait video rotated.

If all three fail on narration: use custom copy override (§IV) and resubmit with
`video_subject` replaced by the custom copy as a single block.

---

## VIII. OUTPUT STRUCTURE

When video generation completes, this directory should contain:

```
compiled/s01e01/
├── build_notes.md              ← this file
├── mpt_payload.json            ← API payload (ready)
├── selected/
│   └── s01e01_full_v1.mp4         ← selected best
└── alternates/
    ├── s01e01_full_v2.mp4          ← rejected alternative
    └── s01e01_full_v3.mp4          ← rejected alternative
```

---

## IX. DEPENDENCY CHAIN

```
[~] S01E01 Cold Open (Build 0017/0019)
    Blocked on: Pexels API key + MPT service
    ↓ confirmed working
[~] S01E01 Full Episode (this file — Build 0020)
    Package: COMPLETE
    Blocked on: cold open confirmation + MPT active
    ↓ confirmed working
[ ] S01E02 Compiled Clip
    Blocked on: full episode pipeline confirmed
    ↓
[ ] Emily RSI loop → MPT trigger
    Blocked on: full pipeline end-to-end
```

When MPT fires and the cold open confirms:
1. Set Pexels key in `MoneyPrinterTurbo/config.toml`
2. `./compiled/mpt_activation.sh --cold-open` → select from batch → move to `selected/`
3. Mark S01E01 Cold Open `[x]` in BACKLOG.md
4. `./compiled/mpt_activation.sh --full-episode` → select from batch → move to `selected/`
5. Mark S01E01 Full Episode `[x]` in BACKLOG.md
6. Proceed to S01E02 compiled clip

---

*S01E01 Full Episode — MPT Build Package*
*Build 0020 | Tyler agent | Iduna-registered | Einhorn_Industrial*
*The package is ready. The cold open needs to fire first. That is a known state.*
*Clean builds first.*
