#!/usr/bin/env bash
set -euo pipefail

# Generate deterministic TYLER source construct artifacts from tracked text files.
# Determinism rules:
#   - enumerate git-tracked files only
#   - sort paths with LC_ALL=C
#   - omit run numbers, timestamps, and host-specific metadata
#   - write stable file boundary markers

MANIFEST="${1:-TYLER_MANIFEST.txt}"
CONSTRUCT="${2:-TYLER_CONSTRUCT.txt}"

export LC_ALL=C

tmp_files="$(mktemp)"
trap 'rm -f "$tmp_files"' EXIT

git ls-files -z \
  ':!TYLER_MANIFEST.txt' \
  ':!TYLER_CONSTRUCT.txt' \
  ':!**/TYLER_MANIFEST.txt' \
  ':!**/TYLER_CONSTRUCT.txt' \
  | sort -z > "$tmp_files"

{
  echo "TYLER MANIFEST v1"
  echo "format: sha256  bytes  path"
  echo ""
  echo "files:"
} > "$MANIFEST"

{
  echo "TYLER CONSTRUCT v1"
  echo "format: deterministic concatenation of git-tracked repository files"
  echo ""
} > "$CONSTRUCT"

count=0
while IFS= read -r -d '' file; do
  [ -f "$file" ] || continue

  if ! grep -Iq . "$file" && [ -s "$file" ]; then
    printf 'Refusing to include non-text tracked file: %s\n' "$file" >&2
    exit 1
  fi

  sha="$(sha256sum "$file" | awk '{print $1}')"
  size="$(wc -c < "$file" | tr -d ' ')"
  printf '%s  %s  %s\n' "$sha" "$size" "$file" >> "$MANIFEST"
  count=$((count + 1))

  {
    printf -- '--- FILE START: %s ---\n' "$file"
    cat "$file"
    printf '\n--- FILE END: %s ---\n\n' "$file"
  } >> "$CONSTRUCT"
done < "$tmp_files"

{
  echo ""
  printf 'total_files: %s\n' "$count"
} >> "$MANIFEST"

test -s "$MANIFEST"
test -s "$CONSTRUCT"
