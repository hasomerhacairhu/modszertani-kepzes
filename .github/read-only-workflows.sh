#!/usr/bin/env bash
# The CI is a read-only checker. On 2026-09-29 (43fd22a) a one-shot job with
# `contents: write` pushed straight to main, around the local hook and the push
# confirmation. This check fails when any workflow gains a write permission, pushes,
# merges a PR or writes through the GitHub API. Used by CI and by /release-check, so
# the two cannot drift. Usage: bash .github/read-only-workflows.sh [workflow dir]
set -uo pipefail
dir="${1:-.github/workflows}"
pattern='(contents|pull-requests|actions|packages|deployments|id-token|issues|statuses|checks|pages|security-events|repository-projects):[[:space:]]*write'
pattern+='|write-all'
pattern+='|git[[:space:]]+(-C[[:space:]]+[^[:space:]]+[[:space:]]+)?push'
pattern+='|gh[[:space:]]+pr[[:space:]]+merge'
pattern+='|gh[[:space:]]+api[^|]*(-X|--method)[[:space:]=]*(POST|PUT|PATCH|DELETE)'
if hits=$(grep -RInE "$pattern" "$dir"); then
  echo "Írási jog, push, merge vagy API-írás egy workflow-ban (a CI kizárólag olvasó-ellenőrző):" >&2
  echo "$hits" >&2
  exit 1
fi
echo "workflows read-only OK"
