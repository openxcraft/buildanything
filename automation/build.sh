#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-$(git -C "$ROOT" log -1 --format=%ct 2>/dev/null || date +%s)}"
mkdir -p "$ROOT/dist" "$ROOT/release-readiness/validation-reports"
printf "SOURCE_DATE_EPOCH=%s\n" "$SOURCE_DATE_EPOCH" > "$ROOT/release-readiness/tool-versions.txt"
python3 "$ROOT/automation/render_formats.py"
python3 "$ROOT/automation/update_manifest.py"
