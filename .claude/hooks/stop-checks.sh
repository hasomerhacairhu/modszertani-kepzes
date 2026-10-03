#!/usr/bin/env bash
# Stop hook: a turn may not end with uncommitted course-content changes that fail the
# objective checks (CLAUDE.md "Kötelező ellenőrzések", "Nincs hamis készjelentés").
# Runs only `content_integrity.py` (≈1 s) and the whitespace check on `02 Tervezet/`;
# the media layer can legitimately be red in the middle of a large fix pack, so it
# stays with /release-check. `stop_hook_active` (and Claude Code's 8-continuation cap)
# prevent a loop: the hook blocks once, then lets the turn end.
set -uo pipefail
ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." 2>/dev/null && pwd)
payload=$(cat)
if command -v jq >/dev/null 2>&1; then
  active=$(printf '%s' "$payload" | jq -r '.stop_hook_active // false' 2>/dev/null)
else
  active=$(printf '%s' "$payload" | python3 -c 'import json,sys; print(str(json.load(sys.stdin).get("stop_hook_active", False)).lower())' 2>/dev/null)
fi
[[ $active == true ]] && exit 0
cd "$ROOT" || exit 0
T="02 Tervezet"
if git diff --quiet HEAD -- "$T" 2>/dev/null && [[ -z $(git ls-files --others --exclude-standard -- "$T" 2>/dev/null) ]]; then
  exit 0
fi
integrity=$(python3 tools/content_integrity.py 2>&1); rc=$?
ws=$( { git diff --check -- "$T"; git diff --cached --check -- "$T"; } 2>&1 )
if (( rc != 0 )) || [[ -n $ws ]]; then
  msg="A tananyag nem commitolt változásai elbuknak az objektív ellenőrzésen — javítsd, mielőtt késznek jelented."
  (( rc != 0 )) && msg+=$'\n\ncontent_integrity.py:\n'"$(printf '%s\n' "$integrity" | grep -E 'ERROR|errors' | head -20)"
  [[ -n $ws ]] && msg+=$'\n\ngit diff --check:\n'"$(printf '%s\n' "$ws" | head -20)"
  python3 -c 'import json,sys; print(json.dumps({"decision": "block", "reason": sys.argv[1]}))' "$msg"
fi
exit 0
