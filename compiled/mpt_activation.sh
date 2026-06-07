#!/usr/bin/env bash
# TYLER — MPT Activation Script
# Activates MoneyPrinterTurbo, fires pending video compilation payloads,
# and moves completed output to the correct compiled/ directory.
#
# Usage:
#   ./compiled/mpt_activation.sh                        → fire cold open (default)
#   ./compiled/mpt_activation.sh <payload_path>         → fire specific payload
#   ./compiled/mpt_activation.sh --check                → prerequisites check only
#   ./compiled/mpt_activation.sh --cold-open            → fire s01e01 cold open
#
# Build 0019 | Tyler agent | Iduna-registered | Einhorn_Industrial
# Clean builds first.

set -euo pipefail

# ── PATHS ──────────────────────────────────────────────────────────────────────

TYLER_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MPT_DIR="/home/fatbaby/MoneyPrinterTurbo"
MPT_API="http://127.0.0.1:8080"
MPT_CONFIG="${MPT_DIR}/config.toml"

# ── COLORS ─────────────────────────────────────────────────────────────────────

RED='\033[0;31m'
GRN='\033[0;32m'
YLW='\033[1;33m'
BLU='\033[0;34m'
NC='\033[0m'

ok()   { echo -e "${GRN}[OK]${NC}  $*"; }
warn() { echo -e "${YLW}[WARN]${NC} $*"; }
err()  { echo -e "${RED}[ERR]${NC} $*" >&2; }
info() { echo -e "${BLU}[--]${NC}  $*"; }

# ── PREREQUISITES CHECK ─────────────────────────────────────────────────────────

check_prerequisites() {
  local failed=0

  echo ""
  info "TYLER MPT Activation — Prerequisites Check"
  echo "────────────────────────────────────────────"

  # 1. ANTHROPIC_API_KEY
  if [[ -n "${ANTHROPIC_API_KEY:-}" ]]; then
    ok "ANTHROPIC_API_KEY found (${#ANTHROPIC_API_KEY} chars)"
  else
    err "ANTHROPIC_API_KEY not set in environment"
    err "  → export ANTHROPIC_API_KEY=sk-ant-..."
    failed=1
  fi

  # 2. Pexels key in config.toml
  if [[ -f "${MPT_CONFIG}" ]]; then
    local pexels_val
    pexels_val=$(grep -E 'pexels_api_keys\s*=' "${MPT_CONFIG}" | head -1 | sed 's/.*=\s*//' | tr -d '"[]' | xargs)
    if [[ "${pexels_val}" == "YOUR_PEXELS_API_KEY_HERE" ]] || [[ -z "${pexels_val}" ]]; then
      err "Pexels API key not set in ${MPT_CONFIG}"
      err "  → Get a free key at https://www.pexels.com/api/"
      err "  → Set: pexels_api_keys = [\"your-key-here\"] in config.toml"
      failed=1
    else
      ok "Pexels API key found in config.toml"
    fi
  else
    err "config.toml not found at ${MPT_CONFIG}"
    err "  → Run from MoneyPrinterTurbo/: uv run python main.py (generates default config)"
    failed=1
  fi

  # 3. uv available
  if command -v uv &>/dev/null; then
    ok "uv available ($(uv --version 2>/dev/null || echo 'ok'))"
  else
    err "uv not found — required to run MPT"
    err "  → Install: curl -LsSf https://astral.sh/uv/install.sh | sh"
    failed=1
  fi

  # 4. MPT directory
  if [[ -d "${MPT_DIR}" ]]; then
    ok "MoneyPrinterTurbo directory found"
  else
    err "MoneyPrinterTurbo not found at ${MPT_DIR}"
    failed=1
  fi

  # 5. curl available
  if command -v curl &>/dev/null; then
    ok "curl available"
  else
    err "curl not found — required for API calls"
    failed=1
  fi

  echo "────────────────────────────────────────────"
  if [[ $failed -eq 0 ]]; then
    ok "All prerequisites satisfied."
    return 0
  else
    err "Prerequisites not met. Resolve above and rerun."
    return 1
  fi
}

# ── MPT SERVICE MANAGEMENT ──────────────────────────────────────────────────────

mpt_is_running() {
  curl -s --max-time 2 "${MPT_API}/api/v1/videos" &>/dev/null
}

start_mpt() {
  if mpt_is_running; then
    ok "MPT service already running at ${MPT_API}"
    return 0
  fi

  info "Starting MoneyPrinterTurbo..."
  (
    cd "${MPT_DIR}"
    nohup uv run python main.py >> "${TYLER_DIR}/compiled/mpt_service.log" 2>&1 &
    echo $! > "${TYLER_DIR}/compiled/mpt.pid"
  )

  info "Waiting for MPT API to become ready..."
  local attempts=0
  local max_attempts=30
  while ! mpt_is_running; do
    attempts=$((attempts + 1))
    if [[ $attempts -ge $max_attempts ]]; then
      err "MPT service did not become ready after ${max_attempts} attempts"
      err "Check log: ${TYLER_DIR}/compiled/mpt_service.log"
      return 1
    fi
    printf "."
    sleep 2
  done
  echo ""
  ok "MPT service ready at ${MPT_API}"
}

stop_mpt() {
  if [[ -f "${TYLER_DIR}/compiled/mpt.pid" ]]; then
    local pid
    pid=$(cat "${TYLER_DIR}/compiled/mpt.pid")
    if kill -0 "${pid}" 2>/dev/null; then
      kill "${pid}"
      ok "MPT service stopped (PID ${pid})"
    fi
    rm -f "${TYLER_DIR}/compiled/mpt.pid"
  fi
}

# ── VIDEO GENERATION ───────────────────────────────────────────────────────────

fire_payload() {
  local payload_path="$1"
  local output_dir="$2"

  if [[ ! -f "${payload_path}" ]]; then
    err "Payload not found: ${payload_path}"
    return 1
  fi

  info "Firing payload: ${payload_path}"
  info "Output target: ${output_dir}"

  # POST payload to MPT
  local response
  response=$(curl -s -X POST "${MPT_API}/api/v1/videos" \
    -H "Content-Type: application/json" \
    -d @"${payload_path}")

  local task_id
  task_id=$(echo "${response}" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('task_id', d.get('data', {}).get('task_id', '')))" 2>/dev/null || true)

  if [[ -z "${task_id}" ]]; then
    err "No task_id in MPT response:"
    err "${response}"
    return 1
  fi

  ok "Task submitted: ${task_id}"
  info "Polling for completion (this may take several minutes)..."

  # Poll for completion
  local status=""
  local attempts=0
  local max_wait=300  # 5 minutes max
  while [[ "${status}" != "completed" ]] && [[ "${status}" != "failed" ]]; do
    attempts=$((attempts + 1))
    if [[ $attempts -ge $((max_wait / 5)) ]]; then
      warn "Polling timeout — check MPT web UI for task ${task_id}"
      break
    fi
    sleep 5
    local poll_response
    poll_response=$(curl -s "${MPT_API}/api/v1/tasks/${task_id}" 2>/dev/null || echo "{}")
    status=$(echo "${poll_response}" | python3 -c "import sys, json; d=json.load(sys.stdin); print(d.get('status', d.get('data', {}).get('state', 'pending')))" 2>/dev/null || echo "pending")
    printf "\r  Status: %-20s (${attempts} polls)" "${status}"
  done
  echo ""

  if [[ "${status}" == "completed" ]]; then
    ok "Video generation complete!"
    collect_output "${task_id}" "${output_dir}"
  elif [[ "${status}" == "failed" ]]; then
    err "Task failed. Check MPT log: ${TYLER_DIR}/compiled/mpt_service.log"
    return 1
  fi
}

collect_output() {
  local task_id="$1"
  local output_dir="$2"

  # MPT typically writes output to MoneyPrinterTurbo/storage/tasks/<task_id>/
  local mpt_output="${MPT_DIR}/storage/tasks/${task_id}"

  mkdir -p "${output_dir}/selected"
  mkdir -p "${output_dir}/alternates"

  if [[ -d "${mpt_output}" ]]; then
    local count=0
    local first=""
    while IFS= read -r -d '' f; do
      count=$((count + 1))
      if [[ $count -eq 1 ]]; then
        first="${f}"
      fi
    done < <(find "${mpt_output}" -name "*.mp4" -print0 | sort -z)

    if [[ $count -eq 0 ]]; then
      warn "No .mp4 files found in ${mpt_output}"
      warn "MPT may use a different output path — check manually"
      return 0
    fi

    info "Found ${count} video(s) in ${mpt_output}"
    info "Review and select using selection criteria in the build_notes.md"
    echo ""
    echo "  Output files:"
    find "${mpt_output}" -name "*.mp4" | sort | while read -r f; do
      echo "    ${f}"
    done
    echo ""
    echo "  To move selected video:"
    echo "    cp '<selected>.mp4' '${output_dir}/selected/'"
    echo "    cp '<alternates>*.mp4' '${output_dir}/alternates/'"
    echo ""
    ok "Output ready for selection."
  else
    warn "MPT output directory not found at expected path: ${mpt_output}"
    warn "MPT may be writing to a different location."
    info "Check: ${MPT_DIR}/storage/ or ${MPT_DIR}/output/"
  fi
}

# ── PRESET PAYLOADS ────────────────────────────────────────────────────────────

fire_cold_open() {
  local payload="${TYLER_DIR}/compiled/s01e01_cold_open/mpt_payload.json"
  local output="${TYLER_DIR}/compiled/s01e01_cold_open"
  echo ""
  info "TARGET: S01E01 Cold Open (30s portrait)"
  fire_payload "${payload}" "${output}"
}

fire_full_episode() {
  local payload="${TYLER_DIR}/compiled/s01e01/mpt_payload.json"
  local output="${TYLER_DIR}/compiled/s01e01"
  if [[ ! -f "${payload}" ]]; then
    warn "S01E01 full episode payload not yet created."
    warn "Dependency: cold open clip must be confirmed working first."
    warn "Run cold open first: ./compiled/mpt_activation.sh --cold-open"
    return 1
  fi
  echo ""
  info "TARGET: S01E01 Full Episode (landscape)"
  fire_payload "${payload}" "${output}"
}

# ── MAIN ───────────────────────────────────────────────────────────────────────

main() {
  local cmd="${1:---cold-open}"

  case "${cmd}" in
    --check)
      check_prerequisites
      ;;

    --cold-open)
      check_prerequisites || exit 1
      start_mpt
      fire_cold_open
      ;;

    --full-episode)
      check_prerequisites || exit 1
      start_mpt
      fire_full_episode
      ;;

    --stop)
      stop_mpt
      ;;

    *)
      # Treat argument as explicit payload path
      if [[ -f "${cmd}" ]]; then
        check_prerequisites || exit 1
        start_mpt
        fire_payload "${cmd}" "$(dirname "${cmd}")"
      else
        echo "TYLER MPT Activation Script"
        echo ""
        echo "Usage:"
        echo "  ./compiled/mpt_activation.sh              → fire cold open (default)"
        echo "  ./compiled/mpt_activation.sh --check      → prerequisites check only"
        echo "  ./compiled/mpt_activation.sh --cold-open  → fire s01e01 cold open"
        echo "  ./compiled/mpt_activation.sh --full-episode → fire s01e01 full episode"
        echo "  ./compiled/mpt_activation.sh --stop       → stop MPT service"
        echo "  ./compiled/mpt_activation.sh <path>       → fire specific payload JSON"
        echo ""
        echo "Prerequisites:"
        echo "  1. export ANTHROPIC_API_KEY=sk-ant-..."
        echo "  2. Set pexels_api_keys in ${MPT_CONFIG}"
        echo "  3. Run --check to verify"
        echo ""
        echo "Then: ./compiled/mpt_activation.sh --cold-open"
        echo "Cold open confirmed → ./compiled/mpt_activation.sh --full-episode"
        echo ""
        echo "Build 0019 | Tyler agent | Iduna-registered | Clean builds first."
        exit 0
      fi
      ;;
  esac
}

main "$@"
