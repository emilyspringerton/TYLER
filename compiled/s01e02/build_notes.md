# S01E02 Compiled Clip — MPT Build Package
## "The School That Isn't There" — Portrait Clip
### Build 0021 | Tyler Agent | Iduna-registered

---

**STATUS:** `PACKAGE COMPLETE — VIDEO GENERATION PENDING S01E01 PIPELINE CONFIRMATION`
**Target platform:** YouTube Shorts / TikTok
**Format:** Portrait 9:16 / 1080×1920
**Duration target:** 40–45 seconds
**Source script:** `episodes/s01e02_school.md`
**Build scope:** Topic extracted, narration written, API payload compiled, activation script updated,
consistency check passed. Video generation blocked on: (1) S01E01 full episode pipeline confirmed,
(2) Pexels API key set, (3) MPT service active.

**To fire when prerequisites are met:**
```bash
./compiled/mpt_activation.sh --s01e02
```

---

## I. DEPENDENCY NOTE

This package depends on the S01E01 full episode pipeline being confirmed working first.
The S01E01 full episode is `[~]` — package complete, video pending Pexels key and cold open
confirmation.

Dependency chain:
1. Set Pexels key in `MoneyPrinterTurbo/config.toml`
2. `./compiled/mpt_activation.sh --cold-open` → select best → mark cold open `[x]`
3. `./compiled/mpt_activation.sh --full-episode` → select best → mark S01E01 full episode `[x]`
4. `./compiled/mpt_activation.sh --s01e02` → select best → mark S01E02 `[x]`

The activation script has `fire_s01e02()` defined (Build 0021). The payload at
`compiled/s01e02/mpt_payload.json` is ready.

---

## II. EPISODE ARC — BEAT EXTRACTION

S01E02 covers Stage 2 archival mode → Stage 3 initiated. The clip compresses the episode
into its five load-bearing moments:

| Timestamp | Beat | Why it stays |
|---|---|---|
| 00:00–00:30 | Lot was empty Thursday / school appears / weeds grown around it | The central impossibility — stated by a neighbor, flatly |
| 01:06–02:00 | Emily OS typography on fire exit map | Second impossible thing — unremarked, filmed for 8 seconds |
| [II.A] | Tyler walks directly to room 204 without checking numbers | His certainty — the walk of someone who has been somewhere nearby enough times |
| [II.B] | File: TYLER — CUSTODY STATUS — UNCLAIMED — since 1623 / "I'm a—" [stops] | Law 1 in full effect. Attempt 47 of this century. Documented. |
| [III.C] | Camera Op seals first log entry / "It's not a documentary" | Closing beat — awareness escalating; something has changed |

Dropped: Tides interface lower-thirds (contextual), love triangle (separate story), production
van dialogue (too technical for 40-second clip), Hana's full exchange (serves episode arc,
not clip hook).

---

## III. MPT TOPIC

Per `engine/tyler_mpt_profile.md` extraction protocol: present tense, witness perspective,
surface detail only, no self-definition, 2–4 sentences.

```
A vacant Detroit lot has a school in it Friday morning. The weeds at the base of the fence
have been growing around it for years. On the third floor, a door marked CUSTODY. A file:
TYLER — CUSTODY STATUS — UNCLAIMED — open since 1623. He starts the sentence. He doesn't
finish it. That night the Camera Op seals their first production log entry. They say, to
the dark: it's not a documentary.
```

---

## IV. CUSTOM NARRATION — 40s PORTRAIT VERSION

If MPT-generated narration violates Tyler's 8 Laws, override with this custom copy.
Approximately 71 words / ~40 seconds at en-GB-RyanNeural documentary pace.

8 Laws check:
- Tyler's self-defining sentence incomplete: PASSES ("I'm a—" stops — Law 1)
- No Jiangshi-POV content calling the documentary a ritual: PASSES (no Jiangshi voice)
- Camera Op awareness at SUSPICIOUS / escalating: PASSES (first sealed entry, S01E02)
- One impossible detail treated as unremarkable: PASSES (school + grown weeds)

---

*The lot was empty Thursday.*
*Friday morning: a school.*
*The weeds at the fence had been growing around it for years.*

*Third floor. A door marked CUSTODY.*
*A girl named Hana. A file: Tyler — Custody Status — Unclaimed.*
*Open since 1623.*

*He started the sentence.*
*"I'm a—"*
*He stopped.*

*The Camera Op sealed their first log entry.*
*To the dark, alone in their apartment:*
*It's not a documentary.*

*They already knew this.*

---

## V. PAYLOAD SPEC

```json
{
  "video_subject": "[see §III above]",
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

Portrait format matches cold open (S01E01 cold open was also a portrait clip).
Full landscape episode format is reserved for S01E02 full episode — not in scope for this build.

---

## VI. SELECTION CRITERIA

After MPT generates 3 candidates:

1. **Verify narration Law compliance** — does it complete a Tyler self-definition? If yes:
   reject. Use custom narration (§IV above) with direct MPT narration override if supported,
   or re-generate.

2. **Visual pacing** — 3-second clips at documentary subject matter. Does the footage feel
   institutional / urban / slightly wrong? Vacant lots, brick buildings, city infrastructure
   preferred over generic office or lifestyle footage.

3. **Subtitle readability** — Anton font, bottom position, white. Verify legibility against
   dark and light backgrounds in the clip mix.

4. **Tonal register** — documentary unease, not thriller. The impossible is unremarked.
   Reject clips where music is too dramatic or footage too overtly cinematic.

Move selected version to `compiled/s01e02/selected/`.
Move alternates to `compiled/s01e02/alternates/`.

---

## VII. NEXT STEPS

On video generation completion:
1. Review 3 candidates per §VI selection criteria
2. Select → `compiled/s01e02/selected/`
3. Mark S01E02 `[x]` in BACKLOG.md
4. RSI receipts: none required (production artifact — canon is in the script, not the video)
5. Consider: S01E02 full episode (landscape) as separate BACKLOG item if clip performs

---

*Build 0021 | Tyler agent | Iduna-registered | Clean builds first.*
