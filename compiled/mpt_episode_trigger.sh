#!/usr/bin/env bash
# mpt_episode_trigger.sh — TYLER × MoneyPrinterTurbo compilation trigger
# See: TYLER/engine/moneyprinter_pipeline.md §VI for full spec
#
# Usage:
#   mpt_episode_trigger.sh <episode_file>
#   mpt_episode_trigger.sh --dry-run <episode_file>
#   mpt_episode_trigger.sh --check

set -euo pipefail

# ── config ─────────────────────────────────────────────────────────────────────
TYLER_DIR="/home/fatbaby/TYLER"
MPT_DIR="/home/fatbaby/MoneyPrinterTurbo"
MPT_API="http://127.0.0.1:8080"
MPT_POLL_INTERVAL=10
MPT_TIMEOUT=300  # 5 minutes

DRY_RUN=false
CHECK_ONLY=false

# ── cli parsing ────────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
  case "$1" in
    --dry-run) DRY_RUN=true; shift ;;
    --check)   CHECK_ONLY=true; shift ;;
    -*)        echo "Unknown flag: $1" >&2; exit 1 ;;
    *)         EPISODE_FILE="$1"; shift ;;
  esac
done

# ── prerequisites check ────────────────────────────────────────────────────────
check_prereqs() {
  local ok=true

  if [[ -z "${ANTHROPIC_API_KEY:-}" ]]; then
    echo "WARN: ANTHROPIC_API_KEY not set"
  else
    echo "OK: ANTHROPIC_API_KEY set"
  fi

  if python3 -c "import tomllib; d = tomllib.load(open('${MPT_DIR}/config.toml', 'rb')); k = d.get('app', {}).get('pexels_api_keys', []); exit(0 if k and k[0] and 'YOUR_' not in k[0] else 1)" 2>/dev/null; then
    echo "OK: Pexels API key configured"
  else
    echo "WARN: Pexels API key not configured in config.toml"
    ok=false
  fi

  if curl -sf --max-time 2 "${MPT_API}/api/v1/health" > /dev/null 2>&1; then
    echo "OK: MPT service reachable at ${MPT_API}"
  else
    echo "WARN: MPT service not running at ${MPT_API}"
  fi

  [[ "$ok" == "true" ]]
}

if [[ "$CHECK_ONLY" == "true" ]]; then
  check_prereqs
  exit 0
fi

if [[ -z "${EPISODE_FILE:-}" ]]; then
  echo "Usage: $0 [--dry-run] [--check] <episode_file>" >&2
  exit 1
fi

if [[ ! -f "$EPISODE_FILE" ]]; then
  echo "Error: episode file not found: $EPISODE_FILE" >&2
  exit 1
fi

# ── step 1: extract topic ──────────────────────────────────────────────────────
extract_topic() {
  local script_file="$1"
  local topic

  topic=$(grep -m1 '^\*\*MPT_TOPIC:\*\*' "${script_file}" \
    | sed 's/\*\*MPT_TOPIC:\*\*[[:space:]]*//' || true)

  if [[ -z "${topic}" ]]; then
    local title location timeline
    title=$(grep -m1 '^\*\*EPISODE:\*\*' "${script_file}" \
      | sed 's/^\*\*EPISODE:\*\*[[:space:]]*//' \
      | sed 's/^[0-9]*[[:space:]]*—[[:space:]]*//' || true)
    location=$(grep -m1 '^\*\*LOCATION:\*\*' "${script_file}" \
      | sed 's/^\*\*LOCATION:\*\*[[:space:]]*//' || true)
    timeline=$(grep -m1 '^\*\*TIMELINE POSITION:\*\*' "${script_file}" \
      | sed 's/^\*\*TIMELINE POSITION:\*\*[[:space:]]*//' || true)
    topic="A documentary episode: ${title:-untitled}. Location: ${location:-unknown}. ${timeline:-}."
  fi

  echo "${topic}"
}

# ── step 2: derive episode id ──────────────────────────────────────────────────
derive_episode_id() {
  local filepath="$1"
  basename "${filepath}" .md | grep -oE '^s[0-9]+e[0-9]+'
}

TOPIC=$(extract_topic "${EPISODE_FILE}")
EPISODE_ID=$(derive_episode_id "${EPISODE_FILE}")

if [[ -z "${EPISODE_ID}" ]]; then
  echo "Error: could not derive episode_id from filename: ${EPISODE_FILE}" >&2
  exit 1
fi

echo "[trigger] Episode: ${EPISODE_ID}"
echo "[trigger] Topic: ${TOPIC}"

# ── step 3: output dirs ────────────────────────────────────────────────────────
OUT_DIR="${TYLER_DIR}/compiled/${EPISODE_ID}"
mkdir -p "${OUT_DIR}/selected" "${OUT_DIR}/alternates"

LOG="${OUT_DIR}/trigger.log"
exec 1> >(tee -a "${LOG}") 2>&1
echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) TRIGGER START ==="

# ── step 4: generate payload ───────────────────────────────────────────────────
PAYLOAD_FILE="${OUT_DIR}/mpt_payload.json"
python3 - <<EOF
import json, sys
payload = {
  "video_subject": ${TOPIC@Q},
  "video_language": "en",
  "voice_name": "en-GB-RyanNeural",
  "video_aspect": "portrait",
  "video_count": 3,
  "subtitle_enabled": True,
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
with open("${PAYLOAD_FILE}", "w") as f:
    json.dump(payload, f, indent=2)
print(f"[trigger] Payload written: ${PAYLOAD_FILE}")
EOF

if [[ "$DRY_RUN" == "true" ]]; then
  echo "[trigger] DRY RUN complete. Payload generated at: ${PAYLOAD_FILE}"
  echo "[trigger] To compile: $0 ${EPISODE_FILE}"
  exit 0
fi

# ── step 5: start MPT if not running ──────────────────────────────────────────
if ! curl -sf --max-time 2 "${MPT_API}/api/v1/health" > /dev/null 2>&1; then
  echo "[trigger] Starting MPT service..."
  cd "${MPT_DIR}"
  uv run python main.py &
  MPT_PID=$!
  echo "[trigger] MPT PID: ${MPT_PID}"
  # Wait up to 30s for service to come up.
  for i in $(seq 1 30); do
    if curl -sf --max-time 2 "${MPT_API}/api/v1/health" > /dev/null 2>&1; then
      echo "[trigger] MPT service ready."
      break
    fi
    sleep 1
  done
fi

# ── step 6: POST payload ───────────────────────────────────────────────────────
echo "[trigger] Submitting to MPT API..."
TASK_RESPONSE=$(curl -sf -X POST "${MPT_API}/api/v1/videos" \
  -H "Content-Type: application/json" \
  -d @"${PAYLOAD_FILE}")

TASK_ID=$(echo "${TASK_RESPONSE}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('task_id',''))" 2>/dev/null || true)

if [[ -z "${TASK_ID}" ]]; then
  echo "[trigger] ERROR: no task_id in response: ${TASK_RESPONSE}" >&2
  exit 1
fi
echo "[trigger] Task ID: ${TASK_ID}"

# ── step 7: poll for completion ────────────────────────────────────────────────
ELAPSED=0
STATUS="pending"
while [[ "$STATUS" != "complete" && "$STATUS" != "failed" && $ELAPSED -lt $MPT_TIMEOUT ]]; do
  sleep "${MPT_POLL_INTERVAL}"
  ELAPSED=$((ELAPSED + MPT_POLL_INTERVAL))
  TASK_STATUS=$(curl -sf "${MPT_API}/api/v1/videos/${TASK_ID}" 2>/dev/null || echo '{}')
  STATUS=$(echo "${TASK_STATUS}" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('status','pending'))" 2>/dev/null || echo "pending")
  echo "[trigger] Status: ${STATUS} (${ELAPSED}s elapsed)"
done

if [[ "$STATUS" == "failed" ]]; then
  echo "[trigger] ERROR: MPT task failed." >&2
  FINAL_STATUS="FAILED"
elif [[ $ELAPSED -ge $MPT_TIMEOUT ]]; then
  echo "[trigger] ERROR: MPT task timed out." >&2
  FINAL_STATUS="TIMEOUT"
else
  FINAL_STATUS="COMPLETE"
fi

# ── step 8: route output ───────────────────────────────────────────────────────
OUTPUT_PATHS=$(echo "${TASK_STATUS}" | python3 -c "
import sys, json
d = json.load(sys.stdin)
for item in d.get('videos', []):
    print(item)
" 2>/dev/null || true)

OUTPUT_COUNT=0
if [[ "$FINAL_STATUS" == "COMPLETE" && -n "${OUTPUT_PATHS}" ]]; then
  while IFS= read -r vpath; do
    if [[ -f "$vpath" ]]; then
      fname=$(basename "$vpath")
      if [[ $OUTPUT_COUNT -eq 0 ]]; then
        cp "$vpath" "${OUT_DIR}/alternates/${fname}"
      else
        cp "$vpath" "${OUT_DIR}/alternates/${fname}"
      fi
      OUTPUT_COUNT=$((OUTPUT_COUNT + 1))
    fi
  done <<< "${OUTPUT_PATHS}"
  echo "[trigger] Routed ${OUTPUT_COUNT} video(s) to ${OUT_DIR}/alternates/"
fi

# ── step 9: write Emily Prime observation ─────────────────────────────────────
TS=$(date -u +%Y-%m-%dT%H:%M:%SZ)
cat > "${OUT_DIR}/emily_prime_obs.md" <<OBS
# Emily Prime Observation — ${EPISODE_ID}
## Generated: ${TS}

### Compilation Result
- Task ID: ${TASK_ID}
- Status: ${FINAL_STATUS}
- Output count: ${OUTPUT_COUNT} video(s)
- Output path: compiled/${EPISODE_ID}/

### 8 Laws Surface Check
- [ ] Tyler self-definition: not completed in narration
- [ ] Documentary: not called a ritual in any Jiangshi-adjacent framing
- [ ] Subscriber identity: not revealed or implied
- [ ] Chrono-Cube location: not confirmed in narration
- [ ] Camera Op awareness: calibrated to episode timeline position
- [ ] Emily OS: does not explain herself in any surface content

### Selection Guidance
Review alternates/ and move selected clip to selected/.
The topic seed was: ${TOPIC}

### Next RSI Target
Check EMILY/BACKLOG.md for next [ ] item.

---
*Emily Prime does not explain her observations. The observation is the tile.*
OBS

echo "[trigger] Emily Prime observation written: ${OUT_DIR}/emily_prime_obs.md"

# ── step 10: log completion ────────────────────────────────────────────────────
echo "=== $(date -u +%Y-%m-%dT%H:%M:%SZ) TRIGGER END: ${FINAL_STATUS} ==="

[[ "$FINAL_STATUS" == "COMPLETE" ]]
