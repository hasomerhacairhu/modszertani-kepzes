#!/usr/bin/env bash
# The CI is a read-only checker. On 2026-09-29 (43fd22a) a one-shot job with
# `contents: write` pushed straight to main, around the local hook and the push
# confirmation. This is an ALLOWLIST, used by CI and by /release-check:
#   - every workflow declares a top-level `permissions:` block;
#   - no permission value anywhere is `write` / `write-all` (quoted, block or inline map);
#   - no `pull_request_target` trigger;
#   - only first-party `actions/*` actions (block or inline step syntax, quoted or not);
#   - no command that pushes, or writes to GitHub through gh, the API or curl (line
#     continuations are joined first).
# The real control is the token: with no write permission it cannot write. These text
# checks are a second layer and read YAML as text, not as a parsed document.
# Usage: bash .github/read-only-workflows.sh [workflow dir]
#        bash .github/read-only-workflows.sh --selftest
set -uo pipefail

check_dir() {
  local dir=$1 fail=0 f joined
  note() { echo "$1" >&2; fail=1; }
  shopt -s nullglob
  local files=("$dir"/*.yml "$dir"/*.yaml)
  (( ${#files[@]} )) || { echo "nincs workflow: $dir" >&2; return 1; }
  for f in "${files[@]}"; do
    grep -qE "^[\"']?permissions[\"']?[[:space:]]*:" "$f" || note "$f: nincs felső szintű permissions: blokk"
    grep -nE "[:{,[:space:]][[:space:]]*[\"']?(write|write-all)[\"']?[[:space:]]*([,}#]|$)|write-all" "$f" | grep -vE '^[0-9]+:[[:space:]]*#' \
      | sed "s|^|$f: írási jog: |" >&2 && fail=1
    grep -nE 'pull_request_target' "$f" | sed "s|^|$f: pull_request_target: |" >&2 && fail=1
    grep -noE "(^|[[:space:]{,-])[\"']?uses[\"']?[[:space:]]*:[[:space:]]*[\"']?[^[:space:]\"',}]+" "$f" \
      | grep -vE "uses[\"']?[[:space:]]*:[[:space:]]*[\"']?actions/" | sed "s|^|$f: nem actions/* action: |" >&2 && fail=1
    joined=$(awk '{ if (sub(/\\$/, "")) { buf = buf $0 } else { print buf $0; buf = "" } }' "$f")
    printf '%s\n' "$joined" | grep -nE '(^|[^[:alnum:]_-])git([^[:alnum:]_-].*)?[^[:alnum:]_-]push([^[:alnum:]_-]|$)' | grep -vE '^[0-9]+:[[:space:]]*#' \
      | sed "s|^|$f: git push: |" >&2 && fail=1
    printf '%s\n' "$joined" | grep -nE 'gh[[:space:]]+(pr|issue|release|repo|workflow|run|secret|variable|label|gist|cache)[[:space:]]+(create|edit|comment|review|merge|close|reopen|delete|upload|enable|disable|cancel|rerun|set|remove|sync|archive|rename|fork|transfer|lock|ready|run)([[:space:]]|$)|gh[[:space:]]+api.*((-X|--method)[[:space:]=]*(POST|PUT|PATCH|DELETE)|[[:space:]](-f|-F|--field|--raw-field|--input)[[:space:]=]|mutation)|curl.*(-X|--request)[[:space:]=]*(POST|PUT|PATCH|DELETE).*api\.github\.com' \
      | grep -vE '^[0-9]+:[[:space:]]*#' | sed "s|^|$f: GitHub-írás: |" >&2 && fail=1
  done
  (( fail )) && { echo "A CI kizárólag olvasó-ellenőrző lehet (CLAUDE.md, Git-biztonság)." >&2; return 1; }
  echo "workflows read-only OK (${#files[@]} fájl)"
}

if [[ "${1:-}" == "--selftest" ]]; then
  # Explicit template: macOS mktemp ignores $TMPDIR otherwise, and the Claude sandbox only
  # allows writes under $TMPDIR.
  tmp=$(mktemp -d "${TMPDIR:-/tmp}/ro-workflows.XXXXXX") || exit 1
  trap 'rm -rf -- "$tmp"' EXIT
  ok=0
  base=$'on: [push]\npermissions:\n  contents: read\njobs:\n  a:\n    runs-on: ubuntu-latest\n    steps:\n'
  # name|expected (0 = passes the allowlist, 1 = rejected)|extra YAML
  cases=(
    $'clean|0|      - uses: actions/checkout@v4\n      - run: python tools/content_integrity.py'
    $'quoted-first-party|0|      - uses: "actions/checkout@v4"'
    $'comment-mentions-push|0|      # never git push from CI\n      - run: echo ok'
    $'write-block|1|    permissions:\n      contents: write'
    $'write-quoted|1|    permissions:\n      contents: "write"'
    $'write-inline-map|1|    permissions: {contents: write, pull-requests: read}'
    $'write-all|1|    permissions: write-all'
    $'third-party|1|      - uses: evil/action@v1'
    $'third-party-quoted|1|      - uses: \'evil/action@v1\''
    $'third-party-inline-step|1|      - {uses: evil/action@v1}'
    $'docker-action|1|      - uses: docker://alpine:3'
    $'target-trigger|1|      - run: echo pull_request_target'
    $'git-push|1|      - run: git push origin HEAD:main'
    $'git-push-continued|1|      - run: git -C . \\\n          push origin main'
    $'gh-merge|1|      - run: gh pr merge 1 --squash'
    $'gh-release|1|      - run: gh release create v1'
    $'gh-api-field|1|      - run: gh api repos/o/r/issues -f title=x'
    $'gh-graphql-mutation|1|      - run: gh api graphql -f query=\'mutation{x}\''
    $'curl-api|1|      - run: curl -X POST https://api.github.com/repos/o/r/issues'
  )
  for c in "${cases[@]}"; do
    name=${c%%|*}; rest=${c#*|}; want=${rest%%|*}; yaml=${rest#*|}
    mkdir -p "$tmp/$name"; printf '%s%s\n' "$base" "$yaml" > "$tmp/$name/w.yml"
    check_dir "$tmp/$name" >/dev/null 2>&1; got=$?
    if [[ $got == "$want" ]]; then echo "ok    $name"; else echo "FAIL  $name (exit $got, want $want)"; ok=1; fi
  done
  mkdir -p "$tmp/no-perms"; printf 'on: [push]\njobs: {}\n' > "$tmp/no-perms/w.yml"
  if check_dir "$tmp/no-perms" >/dev/null 2>&1; then echo "FAIL  no-perms"; ok=1; else echo "ok    no-perms"; fi
  echo "--- ${#cases[@]} + 1 cases ---"; [[ $ok == 0 ]] && echo "--- selftest OK ---" || echo "--- selftest FAILED ---"
  exit $ok
fi

check_dir "${1:-.github/workflows}"
