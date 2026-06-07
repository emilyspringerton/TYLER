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

## VI. EMILY RSI LOOP → MPT COMPILATION TRIGGER

When the RSI loop is fully wired, episode compilation is automatic. This section
is the full implementation spec. The trigger script lives at
`compiled/mpt_episode_trigger.sh`.

### VI.A — Episode Script Header Standard

Every episode script must include an `MPT_TOPIC` field in its header block,
positioned after the `EMILY OS STATUS` line:

```markdown
**MPT_TOPIC:** [1–3 sentence present-tense documentary synopsis. Tyler's 8 Laws
apply: no self-definition, no completed bindings, no Subscriber identity, no ritual
language in Jiangshi-adjacent framing. The topic is the compilation seed — MPT
generates narration and footage from it alone.]
```

**Example — S01E01:**
```
**MPT_TOPIC:** A man who does not stay in his own year is followed by a documentary
crew through a Detroit apartment building at night. He washes his hands too carefully.
The footage timestamp says 1901.
```

**Example — S03E02:**
```
**MPT_TOPIC:** Near a tree in Detroit, a man moves a coin from his left pocket to his
right. He says one sentence. Four hundred years of unfinished business resolves into
a single present-tense fact. The camera is running.
```

The topic cannot complete a Tyler self-definition. If the episode's subject is Tyler
saying who he is, the topic describes the scene — not the sentence.

### VI.B — Trigger Script Interface

```bash
# Auto-trigger: fires when episode file is written
./compiled/mpt_episode_trigger.sh <episode_file>

# Examples:
./compiled/mpt_episode_trigger.sh episodes/s01e03_confessional.md
./compiled/mpt_episode_trigger.sh episodes/s05e12_day_two_fifteen.md

# Dry run: extract topic and generate payload without firing MPT
./compiled/mpt_episode_trigger.sh --dry-run episodes/s01e03_confessional.md

# Check: prerequisites only
./compiled/mpt_episode_trigger.sh --check
```

What the trigger does, in order:

```
1. Extract MPT_TOPIC from episode header (see VI.C)
2. Derive episode_id from filename
3. Check prerequisites (ANTHROPIC_API_KEY, Pexels key, MPT service)
4. Generate compiled/<episode_id>/mpt_payload.json
5. Start MPT service if not running
6. POST payload to http://127.0.0.1:8080/api/v1/videos
7. Poll for completion
8. Route output to compiled/<episode_id>/
9. Write Emily Prime observation to compiled/<episode_id>/emily_prime_obs.md
10. Log completion to compiled/<episode_id>/trigger.log
```

### VI.C — Topic Extraction Algorithm

The trigger reads the `MPT_TOPIC` field from the episode header.
If absent, it constructs a fallback topic from the EPISODE and LOCATION fields.
This means existing episodes (S01E01–S05E12) compile without header modification.

```bash
extract_topic() {
  local script_file="$1"
  local topic

  # Primary: read MPT_TOPIC field
  topic=$(grep -m1 '^\*\*MPT_TOPIC:\*\*' "${script_file}" \
    | sed 's/\*\*MPT_TOPIC:\*\*[[:space:]]*//')

  # Fallback: construct from EPISODE title + LOCATION + TIMELINE POSITION
  if [[ -z "${topic}" ]]; then
    local title location timeline
    title=$(grep -m1 '^\*\*EPISODE:\*\*' "${script_file}" \
      | sed 's/^\*\*EPISODE:\*\*[[:space:]]*//' \
      | sed 's/^[0-9]*[[:space:]]*—[[:space:]]*//')
    location=$(grep -m1 '^\*\*LOCATION:\*\*' "${script_file}" \
      | sed 's/^\*\*LOCATION:\*\*[[:space:]]*//')
    timeline=$(grep -m1 '^\*\*TIMELINE POSITION:\*\*' "${script_file}" \
      | sed 's/^\*\*TIMELINE POSITION:\*\*[[:space:]]*//')
    topic="A documentary episode: ${title}. Location: ${location}. ${timeline}."
  fi

  echo "${topic}"
}
```

### VI.D — Episode ID Derivation

```bash
derive_episode_id() {
  local filepath="$1"
  # episodes/s01e03_confessional.md → s01e03
  basename "${filepath}" .md | grep -oE '^s[0-9]+e[0-9]+'
}
```

### VI.E — Payload Generation

The trigger generates a portrait (9:16) payload for clips and a landscape (16:9)
payload for full episodes. Default: portrait clips (shorts-first distribution).

```json
{
  "video_subject": "<extracted MPT_TOPIC>",
  "video_language": "en",
  "voice_name": "en-GB-RyanNeural",
  "video_aspect": "portrait",
  "video_count": 3,
  "subtitle_enabled": true,
  "subtitle_font_name": "Anton",
  "subtitle_font_size": 60,
  "subtitle_color": "#FFFFFF",
  "subtitle_stroke_color": "#000000",
  "subtitle_stroke_width": 1.5,
  "bgm_type": "random",
  "bgm_volume": 0.1,
  "segment_min_duration": 3,
  "segment_max_duration": 5,
  "terms": ["documentary", "urban", "night", "candid footage", "film noir"]
}
```

`terms` guides Pexels footage selection toward documentary register.
The terms list is not canon. Stock footage is surface content. The law applies
to narration, not to footage.

### VI.F — Hook Wiring

Two wiring paths, in priority order:

**Path 1: PostToolUse hook (Claude Code native, preferred)**

The hook fires after every Write tool call. If the written file is in `episodes/`,
the trigger fires.

Spec for `.claude/settings.json` hooks block:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash -c 'f=\"$TOOL_RESULT_FILE_PATH\"; if [[ \"$f\" == */episodes/*.md ]]; then /home/fatbaby/TYLER/compiled/mpt_episode_trigger.sh \"$f\" >> /home/fatbaby/TYLER/compiled/hook.log 2>&1; fi'"
          }
        ]
      }
    ]
  }
}
```

Note: `.claude/settings.json` is write-protected for the Tyler agent. This hook
must be added manually or by Emily OS (who has settings.json access).

**Path 2: emily.sh loop check (agent-native, current fallback)**

At the end of each emily.sh build iteration, the loop runs the sweep:
```bash
for script in /home/fatbaby/TYLER/episodes/*.md; do
  ep_id=$(basename "${script}" .md | grep -oE '^s[0-9]+e[0-9]+')
  payload="/home/fatbaby/TYLER/compiled/${ep_id}/mpt_payload.json"
  if [[ -n "${ep_id}" ]] && [[ ! -f "${payload}" ]]; then
    /home/fatbaby/TYLER/compiled/mpt_episode_trigger.sh --dry-run "${script}"
  fi
done
```

`--dry-run` generates the payload without firing MPT, so the loop can complete
without depending on live API access. Manual activation (`--cold-open`, etc.)
remains the fire step.

**Current status:** Path 2 (loop sweep) is the operative path until
`.claude/settings.json` hooks are configured.

### VI.G — Output Routing

```
compiled/
  <episode_id>/
    mpt_payload.json          ← generated by trigger (or manually: Builds 0017–0021)
    trigger.log               ← trigger run log (appended each run)
    emily_prime_obs.md        ← Emily Prime observation (see VI.H)
    selected/                 ← final selected video(s)
    alternates/               ← remaining batch videos
```

The `selected/` directory is not populated by the trigger. Human or Emily Prime
selects. The trigger generates the batch and logs the options.

### VI.H — Emily Prime Observation Protocol

After video generation completes, the trigger writes an observation entry.
This is a build output, not a canon event.

**File:** `compiled/<episode_id>/emily_prime_obs.md`

**Template:**
```markdown
# Emily Prime Observation — <episode_id>
## Generated: <ISO 8601 timestamp>

### Compilation Result
- Task ID: <mpt_task_id>
- Status: COMPLETE / FAILED / TIMEOUT
- Output count: <n> video(s)
- Output path: compiled/<episode_id>/

### 8 Laws Surface Check
- [ ] Tyler self-definition: not completed in narration
- [ ] Documentary: not called a ritual in any Jiangshi-adjacent framing
- [ ] Subscriber identity: not revealed or implied
- [ ] Chrono-Cube location: not confirmed in narration
- [ ] Camera Op awareness: calibrated to episode timeline position
- [ ] Emily OS: does not explain herself in any surface content

Surface check is performed by reviewing the generated narration text (available
in MPT task output). If a violation is found, override with custom narration
before selecting the video.

### Selection Guidance
[Populated from episode build_notes.md §Selection if present. Otherwise: select
the clip where stock footage best matches the episode's LOCATION field.]

### Next RSI Target
[Populated from BACKLOG.md: first remaining [ ] item after this episode's entry.]

---
*Emily Prime does not explain her observations. The observation is the tile.*
```

The Emily Prime observation file is committed alongside any selected video.
If no video is selected yet, the observation file is committed on generation
(the batch exists; the selection is pending).

---

### VI.I — Full Automation Flow (When Wired)

```
Claude Code writes episode script → episodes/s03e07_something.md
        │
        ▼ (PostToolUse hook fires OR emily.sh loop sweep detects)
        │
        ▼
compiled/mpt_episode_trigger.sh episodes/s03e07_something.md
        │
        ├── extracts MPT_TOPIC from header
        ├── derives episode_id: s03e07
        ├── checks prerequisites (key, MPT service)
        ├── generates compiled/s03e07/mpt_payload.json
        ├── starts MPT service (if not running)
        ├── POSTs to http://127.0.0.1:8080/api/v1/videos
        ├── polls until complete (5-min timeout)
        ├── reports output paths to compiled/s03e07/
        ├── writes compiled/s03e07/emily_prime_obs.md
        └── logs to compiled/s03e07/trigger.log
                │
                ▼
        Emily Prime observation: "S03E07 flat stream batch: 3 clips generated"
                │
                ▼
        Human selects best clip → compiled/s03e07/selected/
                │
                ▼
        8 Laws surface check (VI.H)
                │
                ▼
        Commit: "Build NNNN — S03E07 compiled clip | TYLER agent | Iduna-registered"
```

**Implementation status:** Spec complete (this document). Trigger script not yet
written — requires `Write(compiled/*)` added to `.claude/settings.json` allow list
(currently outside Tyler agent write scope). Hook wiring requires settings.json
modification outside Tyler agent scope. Both are one-line additions; neither is a
dependency of the spec. Loop sweep (Path 2) is available once the script exists.

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
