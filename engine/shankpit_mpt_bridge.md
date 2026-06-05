# SHANKPIT → MPT LOCAL MATERIALS BRIDGE
## Game Engine as Visual Production Pipeline
### Engine Spec v1.0 | Einhorn Media
### Build 0038 | TYLER × TIDES OF PARADOX × MoneyPrinterTurbo

---

> *"The game engine renders the world. The compiler assembles the episode."*
> — `engine/television_as_code.md`

---

## I. WHAT THIS IS

MoneyPrinterTurbo can accept local video materials in place of Pexels/Pixabay stock footage. SHANKPIT's Tyler-mode renderer produces scene frame output. This spec defines the bridge: how SHANKPIT-rendered Tyler-universe visuals become the material layer for compiled TYLER episodes.

**Why this matters:**

Stock footage produces a generic documentary aesthetic. SHANKPIT renders the Tyler universe as a first-person metaverse — the same Detroit apartment, the same Bacon's library, the same round table — with faction-accurate geometry and lighting. Using SHANKPIT output as MPT local materials means compiled episodes draw on the actual universe geometry rather than approximations from a stock library.

The game engine is the visual production pipeline. MPT is the assembly pipeline. The bridge connects them.

---

## II. DEPENDENCIES

This spec depends on the following existing:

| Dependency | File | Status |
|---|---|---|
| SHANKPIT Tyler-mode scene map | `engine/shankpit_tyler_mode.md` | Complete |
| MPT configuration and profile | `engine/tyler_mpt_profile.md` | Complete |
| MPT local materials API | MoneyPrinterTurbo documentation | Supported |
| SHANKPIT Tyler-mode renderer frame output | SHANKPIT runtime | Requires SHANKPIT running |
| ffmpeg | System dependency | Required for format conversion |

The bridge is not operational until SHANKPIT is running and producing frame output from Tyler-mode scenes. This spec defines the contract between the two systems.

---

## III. SHANKPIT OUTPUT CONTRACT

**Frame capture mode:**

SHANKPIT Tyler-mode renderer supports a `--capture` flag that records a scene session to disk. Output structure:

```
var/shankpit/captures/
  <scene_id>/
    <timestamp>/
      frames/
        0000.png ... N.png     # raw frames at game render rate (configurable)
      metadata.json            # scene_id, camera_angle, time_of_day, faction_state
```

**`metadata.json` schema:**

```json
{
  "scene_id": "bacon_estate",
  "camera_angle": "wide_room | table_focus | door_focus | overhead",
  "time_of_day": "morning | afternoon | evening | night",
  "faction_state": {
    "tyler_present": true,
    "camera_op_present": false,
    "door_open": true
  },
  "frame_count": 1200,
  "fps": 30,
  "duration_seconds": 40
}
```

**Naming conventions:**

Scene IDs match `engine/shankpit_tyler_mode.md` scene map:
- `detroit_apartment`
- `bacon_estate`
- `cairngorms_library`
- `detroit_school`
- `osaka_night`
- `osaka_underport`
- `vatican_corridors`
- `kuroshio_coast`

A capture session corresponds to one visual segment in an episode. Camera angles, faction state, and time-of-day are set before capture. The capture runs for the duration of the scene requirement.

---

## IV. BRIDGE PROCESS

**Input:** SHANKPIT frame capture directory + episode script segment list
**Output:** MPT `local_materials/` directory ready for assembly

### Step 1 — Segment manifest from episode script

Each episode script (`episodes/s*.md`) has a SCENE LIST header block:

```
## SCENE LIST
- [bacon_estate | morning | door_open | 30s] — Tyler reads at the table
- [detroit_apartment | night | tyler_present | 20s] — Tyler washes hands
- [cairngorms_library | afternoon | no_actors | 45s] — Archive pan
```

The bridge reads this block and produces a segment manifest: which scenes are needed, what configuration, what duration.

### Step 2 — Capture selection or scheduling

For each segment in the manifest, the bridge checks `var/shankpit/captures/` for an existing capture that matches scene_id + camera_angle + time_of_day within duration requirements.

If a matching capture exists: use it.
If not: log a `CAPTURE_NEEDED` entry to `var/bridge/pending.json`. These are dispatched to SHANKPIT for capture in the next session.

```json
{
  "pending": [
    {
      "scene_id": "bacon_estate",
      "camera_angle": "table_focus",
      "time_of_day": "morning",
      "duration_seconds": 30,
      "faction_state": { "door_open": true },
      "requested_by": "s03e05",
      "created_at": "2026-06-05"
    }
  ]
}
```

### Step 3 — Frame sequence → video clip conversion

For each selected capture, convert the frame sequence to an MP4 clip using ffmpeg:

```bash
ffmpeg -framerate 30 -i var/shankpit/captures/<scene_id>/<timestamp>/frames/%04d.png \
  -c:v libx264 -pix_fmt yuv420p -crf 18 \
  -t <duration_seconds> \
  var/bridge/clips/<scene_id>_<camera_angle>_<timestamp>.mp4
```

Output clips land in `var/bridge/clips/`. Clips are reusable across episodes.

### Step 4 — MPT local materials directory assembly

MPT expects local materials as a directory of video files with a manifest:

```
MoneyPrinterTurbo/local_materials/
  <episode_id>/
    clip_00.mp4
    clip_01.mp4
    ...
    manifest.json
```

**`manifest.json`:**

```json
{
  "episode": "s03e05",
  "clips": [
    {
      "file": "clip_00.mp4",
      "scene_id": "bacon_estate",
      "description": "Library interior, morning, door open",
      "duration_seconds": 30
    },
    {
      "file": "clip_01.mp4",
      "scene_id": "detroit_apartment",
      "description": "Apartment at night, Tyler visible",
      "duration_seconds": 20
    }
  ]
}
```

The bridge writes this directory from the segment manifest + converted clips. When the directory is ready, MPT can be invoked with the local materials path instead of a Pexels query.

### Step 5 — MPT invocation with local materials

```bash
# Via MPT API
curl -X POST http://127.0.0.1:8080/api/v1/videos \
  -H "Content-Type: application/json" \
  -d '{
    "videoScript": "<narration from episode script>",
    "videoTerms": "Tyler universe documentary",
    "videoAspect": "16:9",
    "videoLanguage": "en-US",
    "localMaterials": "MoneyPrinterTurbo/local_materials/s03e05"
  }'
```

When `localMaterials` is provided, MPT uses the clips from that directory rather than querying Pexels. The bridge has constructed those clips from SHANKPIT renders.

---

## V. OUTPUT PIPELINE

```
Episode script (episodes/s03e05.md)
         ↓
Segment manifest (scene list block)
         ↓
Capture check (var/shankpit/captures/)
         ↓        ↓
   Match found    No match → var/bridge/pending.json → SHANKPIT session
         ↓
Frame sequence → ffmpeg → clip (var/bridge/clips/)
         ↓
MPT local_materials directory assembly
         ↓
MPT API invocation (local materials mode)
         ↓
Compiled episode (compiled/<episode_id>/)
         ↓
Emily Prime observation → next build target
```

---

## VI. CAPTURE LIBRARY MANAGEMENT

Captures are reusable. A `bacon_estate` morning wide-room capture can serve multiple episodes. The library grows over time.

**Library path:** `var/shankpit/captures/`
**Clip cache:** `var/bridge/clips/`
**Episode materials:** `MoneyPrinterTurbo/local_materials/<episode_id>/`

The clip cache is the working set. Episode materials directories are ephemeral — assembled per compilation run and cleared after output is committed to `compiled/`.

**Capture priority:**

When SHANKPIT is available for a capture session, prioritize by `pending.json` queue order. Captures needed for the next episode in the build queue take precedence.

---

## VII. FALLBACK BEHAVIOR

When no SHANKPIT capture is available for a required segment, the bridge falls back to Pexels/Pixabay stock footage for that segment only. The MPT invocation proceeds with a hybrid materials configuration:

```json
{
  "localMaterials": "MoneyPrinterTurbo/local_materials/s03e05",
  "fallbackToPexels": true,
  "pexelsQuery": "documentary interior dark cinematic"
}
```

Mixed episodes (some SHANKPIT, some stock) are valid output. The goal is maximum SHANKPIT coverage; 100% is the target state, not the launch requirement.

---

## VIII. RSI LOOP INTEGRATION

The bridge is invoked automatically when the RSI loop writes a new episode script.

`cmd/observation-watcher` monitors `episodes/` for new files. On detection, it:

1. Reads the SCENE LIST block from the new episode file
2. Invokes the bridge to check capture availability
3. If all captures available: invokes MPT immediately
4. If captures pending: writes to `var/bridge/pending.json`, logs "capture session required before compilation," continues with the build queue

This integrates SHANKPIT session work into the RSI loop as a non-blocking dependency. The compilation step waits for captures; the writing step does not.

---

## IX. DEPENDENCIES FOR ACTIVATION

The bridge is **specified but not yet executable** pending:

1. SHANKPIT Tyler-mode renderer producing frame output (Tyler-mode capture mode not yet implemented)
2. `var/bridge/` directory initialized
3. ffmpeg confirmed installed at system level (`which ffmpeg`)
4. MPT local materials API confirmed supporting the `localMaterials` parameter in the current MPT version

When all four conditions are met, the bridge is operational. Until then, the MPT pipeline uses Pexels stock footage per `engine/tyler_mpt_profile.md`.

**Activation checklist:**

- [ ] Verify MPT local materials parameter: `MoneyPrinterTurbo/docs/` or test POST to `/api/v1/videos`
- [ ] Confirm ffmpeg: `which ffmpeg`
- [ ] Implement SHANKPIT `--capture` flag in Tyler-mode (SHANKPIT codebase, not TYLER codebase)
- [ ] Write first capture: `bacon_estate`, morning, wide room, 30 seconds
- [ ] Run bridge end-to-end with S03E05 as test episode

---

*End log: SHANKPIT→MPT BRIDGE SPECIFIED. GAME ENGINE IS THE VISUAL PIPELINE. SHANKPIT RENDERS. MPT ASSEMBLES. THE EPISODE IS THE OUTPUT. ACTIVATION PENDING CAPTURE MODE. BUILD WHAT COMES NEXT.*
