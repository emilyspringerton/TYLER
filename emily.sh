#!/bin/bash
# emily.sh — TYLER RSI Loop Orchestrator
# The Emily Method: find the load-bearing dependency. That is your actual work.
#
# Usage: ./emily.sh [max_iterations]
#   max_iterations defaults to 20 if not supplied
#
# What this does:
#   Each iteration: picks the next incomplete task from BACKLOG.md, generates
#   all required RSI artifacts across applicable faction files, commits the
#   build, updates activity.md and BACKLOG.md, and repeats until the backlog
#   is empty or the iteration budget is exhausted.
#
# Stop condition: Claude outputs <promise>COMPLETE</promise> when every item
#   in BACKLOG.md is checked complete.
#
# To run a single build iteration interactively instead:
#   claude --permission-mode acceptEdits

set -euo pipefail

MAX_ITERATIONS="${1:-20}"

# Verify we're in the right repo
if [ ! -f "CLAUDE.md" ] || [ ! -f "BACKLOG.md" ]; then
  echo "ERROR: Run emily.sh from the TYLER repo root."
  echo "Expected: CLAUDE.md and BACKLOG.md in current directory."
  exit 1
fi

# The prompt. References:
#   @BACKLOG.md  — atomic task queue with RSI receipt specs
#   @activity.md — what was built in prior iterations (context continuity)
#
# Instruction design follows the Emily Method:
#   1. Identify the next incomplete task
#   2. Follow its dependency chain to the load-bearing foundation
#   3. Build from the foundation up — no partial builds
#   4. File all RSI receipts (every narrative event generates artifacts
#      across all applicable faction files per the RSI model in CLAUDE.md)
#   5. Commit with the next sequential build number
#   6. Update state files so the next iteration has full context

PROMPT='Review @BACKLOG.md and @activity.md.

Apply the Emily Method:
1. Find the next incomplete task in BACKLOG.md (first unchecked item)
2. Identify its load-bearing dependencies — generate nothing until the foundation is correct
3. Generate ALL required RSI artifacts for this task:
   - New files (lore, engine, manuscripts, episodes) as specified
   - Updates to applicable faction files (Eastwind archive, Jiangshi memos,
     Shell Parliament ledger, Field activation logs, engine specs)
   - Every narrative event generates receipts. No partial builds.
4. Commit the build to git with the next sequential build number, push to origin
5. Mark the completed task in BACKLOG.md (change [ ] to [x])
6. Append a build entry to activity.md in this format:
   ## Build NNNN — [task name]
   [list of files created/modified]
   [key narrative elements added — 2-3 sentences max]

If BACKLOG.md has no remaining incomplete tasks, output <promise>COMPLETE</promise>.
Otherwise complete exactly one task per iteration, then stop and wait for the next iteration.'

echo "=== TYLER RSI Loop | Emily Method | Max iterations: $MAX_ITERATIONS ==="
echo "=== Backlog: $(grep -c '^\- \[ \]' BACKLOG.md 2>/dev/null || echo 0) tasks pending ==="
echo ""

for ((i=1; i<=MAX_ITERATIONS; i++)); do
  PENDING=$(grep -c '^\- \[ \]' BACKLOG.md 2>/dev/null || echo 0)
  if [ "$PENDING" -eq 0 ]; then
    echo "=== Backlog empty. All builds complete. ==="
    break
  fi

  echo "--- Iteration $i / $MAX_ITERATIONS | $(date '+%Y-%m-%d %H:%M') | $PENDING tasks remaining ---"

  result=$(claude -p "$PROMPT" --permission-mode acceptEdits 2>&1) || true
  echo "$result"
  echo ""

  if [[ "$result" == *"<promise>COMPLETE</promise>"* ]]; then
    echo "=== All RSI tasks finalized after $i iterations. ==="
    break
  fi

  # Brief pause between iterations — avoids hammering the API
  if [ "$i" -lt "$MAX_ITERATIONS" ]; then
    sleep 5
  fi
done

REMAINING=$(grep -c '^\- \[ \]' BACKLOG.md 2>/dev/null || echo 0)
DONE=$(grep -c '^\- \[x\]' BACKLOG.md 2>/dev/null || echo 0)
echo ""
echo "=== Loop finished. Complete: $DONE | Remaining: $REMAINING ==="
