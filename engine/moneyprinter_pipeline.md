# MoneyPrinterTurbo — Tyler Flat Stream Pipeline
## Einhorn Media | Engine Spec v1.0
### Classification: OPEN SOURCE

---

> *"Clean builds first. Then custody. Then the rest."*
> — Emily OS

---

## I. WHAT THIS IS

MoneyPrinterTurbo (`/home/fatbaby/MoneyPrinterTurbo`) is the **flat stream compilation engine**
for TYLER × TIDES OF PARADOX episodes.

In the `engine/television_as_code.md` build pipeline:

```
COMPILED EPISODE
      │
      ├──► FLAT STREAM              ← MoneyPrinterTurbo handles this branch
      │    (standard video)
      │
      └──► METAVERSE PACKAGE        ← SHANKPIT handles this branch
```

MPT takes a topic or narration script and generates: copy, stock footage, subtitles,
background music → HD video. No manual editing required. The pipeline is batch-capable.

---

## II. SYSTEM COMPONENTS

| Component | Location | Role |
|---|---|---|
| MoneyPrinterTurbo | `/home/fatbaby/MoneyPrinterTurbo/` | Video synthesis engine |
| WebUI | `http://127.0.0.1:8501` | Interactive generation (Streamlit) |
| API | `http://127.0.0.1:8080` | Programmatic generation |
| Config | `MoneyPrinterTurbo/config.toml` | API keys, LLM provider, paths |
| Episode scripts | `TYLER/episodes/*.md` | Canonical source (input) |
| Compiled output | `TYLER/compiled/` | Video artifacts (output) |

---

## III. CONFIGURATION

Copy `config.example.toml` to `config.toml` and set:

```toml
[app]
video_source = "pexels"

pexels_api_keys = ["<YOUR_PEXELS_KEY>"]

llm_provider = "openai"
openai_api_key = "<ANTHROPIC_API_KEY>"
openai_base_url = "https://api.anthropic.com/v1"
openai_model_name = "claude-sonnet-4-6"
```

ImageMagick must be installed: `sudo apt-get install imagemagick`

---

## IV. TYLER MPT GENERATION PROFILE

These parameters apply to all Tyler episode compilations. See `engine/tyler_mpt_profile.md`
for the full spec once it is written.

| Parameter | Value | Why |
|---|---|---|
| Voice | `en-GB-RyanNeural` | Documentary register; dry, precise |
| Format | Portrait 9:16 (shorts) / Landscape 16:9 (full) | Platform-appropriate |
| Subtitle font | `Anton` | Legible, minimal, not decorative |
| Subtitle color | white | Contrast on dark documentary footage |
| Subtitle position | bottom | Standard documentary |
| Background music volume | 0.1 | Atmospheric, not distracting |
| Segment duration | 3–5s | Matches documentary cut rhythm |
| Batch size | 3 | Generate 3, select best |
| Resolution | 1920×1080 (landscape) / 1080×1920 (portrait) | HD |

---

## V. EPISODE → VIDEO: THE COMPILATION PROCESS

### Step 1: Extract the MPT topic from the episode script

The MPT topic is derived from the episode script's opening description — not the dialogue,
not the full plot. It is a 1–3 sentence present-tense summary of what the documentary
crew is witnessing. Tyler's laws apply: no self-definition, no completed bindings.

**S01E01 example topic:**
> *A time-traveler who refuses to be documented is followed by a camera crew through
> a Detroit apartment building at night. He washes his hands too carefully. The footage
> timestamp says 1901.*

The topic is the seed. MPT generates narration and footage selection from it.

### Step 2: Optionally provide custom narration

For sequences where canonical dialogue must appear verbatim, write the narration script
directly in MPT's "custom copy" field. This preserves Tyler's 8 laws in the output.

The canon firewall applies here: MPT's LLM-generated narration is **surface content**.
If MPT generates narration that would complete a Tyler self-definition, override with
custom copy. The LLM does not know the laws. The consistency checker does.

### Step 3: Run MPT and select best output

```bash
cd /home/fatbaby/MoneyPrinterTurbo
uv run python main.py  # starts API server
# or: uv run streamlit run ./webui/Main.py --browser.gatherUsageStats=False
```

Via API:
```bash
curl -X POST http://127.0.0.1:8080/api/v1/videos \
  -H "Content-Type: application/json" \
  -d '{
    "video_subject": "<TYLER MPT TOPIC>",
    "video_language": "en",
    "voice_name": "en-GB-RyanNeural",
    "video_aspect": "landscape",
    "video_count": 3,
    "subtitle_enabled": true,
    "bgm_type": "random",
    "bgm_volume": 0.1
  }'
```

### Step 4: Move output to `compiled/`

```bash
mkdir -p /home/fatbaby/TYLER/compiled/<episode_id>/
cp <mpt_output>/*.mp4 /home/fatbaby/TYLER/compiled/<episode_id>/
```

---

## VI. EMILY RSI LOOP INTEGRATION

When the RSI loop is fully wired, episode compilation is automatic:

```
1. Claude Code writes episode script → episodes/s01e03_confessional.md
2. Observation-watcher detects new .md in episodes/
3. Trigger: extract MPT topic from script header comment
4. POST to MPT API → poll task completion
5. Move output to compiled/s01e03/
6. Emily Prime observation: "S01E03 flat stream compiled"
7. Next RSI task: evaluate clip against Tyler laws, write run report
```

The trigger mechanism lives in the observation-watcher configuration.
Implementation depends on MPT API confirmed running end-to-end.

---

## VII. SHANKPIT → MPT LOCAL MATERIALS (FUTURE)

When SHANKPIT's Tyler-mode renderer produces scene output, that footage can replace
Pexels stock footage as MPT local materials.

```
SHANKPIT render → TYLER/shankpit_renders/<scene_id>/ → MPT local_materials path
```

This makes the game engine the visual production pipeline. The show looks like
the game because the show IS the game at a different zoom level.

Spec for this bridge: `engine/shankpit_mpt_bridge.md` (not yet written).
Dependency: `engine/shankpit_tyler_mode.md`.

---

## VIII. CANON FIREWALL REMINDER

MPT generates **surface content**. The video is a compiled artifact, not canon.

| Canon (in the script) | Surface (in the video) |
|---|---|
| What Tyler says | Which stock footage MPT picks |
| The binding stage at episode close | The background music track |
| The Camera Op's awareness level | Subtitle font/color |
| The end log text | Video duration |
| Faction presence in the scene | MPT narration phrasing |

MPT narration phrasing is swappable. If MPT generates narration that violates a Tyler law
(completes a self-definition, names the ritual, reveals the Subscriber), override it.
The episode script is the source of truth. The video is a build output.

---

## IX. ACCEPTANCE CRITERIA

The MPT pipeline is working when:

- [ ] `config.toml` configured with working Pexels key and LLM provider
- [ ] MPT generates a clean 1080x1920 test video (any topic) without errors
- [ ] S01E01 cold open (30s) compiles from topic derived from pilot script
- [ ] Output video contains subtitles matching generated narration
- [ ] Output committed to `compiled/s01e01_cold_open/`
- [ ] CAST stream annotation appears in episode header (in-universe: Emily OS's)
- [ ] Tyler's 8 laws are not violated in any narration output (verified manually)

---

*MONEYPRINTERTURBO PIPELINE SPEC — v1.0*
*Einhorn Media | Open Source*
*The flat stream is now buildable. Clean builds first.*

---

> *End log: MPT PIPELINE SPEC COMPILED. FLAT STREAM: PENDING. TYLER STATUS: UNRESOLVED.*
