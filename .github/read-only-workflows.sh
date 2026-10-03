#!/usr/bin/env bash
# The CI is a read-only checker. On 2026-09-29 (43fd22a) a one-shot job with
# `contents: write` pushed straight to main, around the local hook and the push
# confirmation. This is an ALLOWLIST, used by CI and by /release-check:
#   - every workflow declares a top-level `permissions:` block;
#   - no permission value anywhere is `write` / `write-all`;
#   - no `pull_request_target` trigger;
#   - only first-party `actions/*` actions;
#   - no command that pushes, merges a PR or writes through the GitHub API (line
#     continuations are joined first).
# Usage: bash .github/read-only-workflows.sh [workflow dir]
set -uo pipefail
dir="${1:-.github/workflows}"
fail=0
note() { echo "$1" >&2; fail=1; }
shopt -s nullglob
files=("$dir"/*.yml "$dir"/*.yaml)
(( ${#files[@]} )) || { echo "nincs workflow: $dir" >&2; exit 1; }
for f in "${files[@]}"; do
  grep -qE '^permissions:' "$f" || note "$f: nincs felső szintű permissions: blokk"
  grep -nE '(^|[[:space:]])[a-z-]+:[[:space:]]*write([[:space:]]|$)|write-all' "$f" | sed "s|^|$f: írási jog: |" >&2 && fail=1
  grep -nE 'pull_request_target' "$f" | sed "s|^|$f: pull_request_target: |" >&2 && fail=1
  grep -nE '^[[:space:]-]*uses:[[:space:]]*' "$f" | grep -vE 'uses:[[:space:]]*actions/' | sed "s|^|$f: nem actions/* action: |" >&2 && fail=1
  joined=$(awk '{ if (sub(/\\$/, "")) { buf = buf $0 } else { print buf $0; buf = "" } }' "$f")
  printf '%s\n' "$joined" | grep -nE '(^|[^[:alnum:]_-])git([^[:alnum:]_-].*)?[^[:alnum:]_-]push([^[:alnum:]_-]|$)' | grep -vE '^[0-9]+:[[:space:]]*#' \
    | sed "s|^|$f: git push: |" >&2 && fail=1
  printf '%s\n' "$joined" | grep -nE 'gh[[:space:]]+pr[[:space:]]+merge|gh[[:space:]]+api.*((-X|--method)[[:space:]=]*(POST|PUT|PATCH|DELETE)|[[:space:]](-f|-F|--field|--raw-field|--input)[[:space:]])|curl.*-X[[:space:]]*(POST|PUT|PATCH|DELETE).*api\.github\.com' \
    | sed "s|^|$f: GitHub-írás: |" >&2 && fail=1
done
(( fail )) && { echo "A CI kizárólag olvasó-ellenőrző lehet (CLAUDE.md, Git-biztonság)." >&2; exit 1; }
echo "workflows read-only OK (${#files[@]} fájl)"
