#!/usr/bin/env bash
# The CI is a read-only checker. On 2026-09-29 (43fd22a) a one-shot job with
# `contents: write` pushed straight to main, around the local hook and the push
# confirmation. This is an ALLOWLIST, used by CI and by /release-check:
#   - every workflow declares a top-level `permissions:` block;
#   - every permission value is `read` or `none` (an allowlist: block, quoted, inline map, a
#     value on the next line), `permissions:` itself only `read-all`/`{}`/a block; no YAML
#     escape sequences (`\x77rite` would decode to `write`);
#   - no secret other than GITHUB_TOKEN (a personal token would bypass the permissions);
#   - no `pull_request_target` trigger;
#   - only first-party `actions/*` actions (block or inline step syntax, quoted or not), and
#     not `actions/github-script` (arbitrary API calls);
#   - no `git push`, no git subcommand from a variable, `gh` only read-only
#     (pr/issue view|list|status|diff|checks, run/release list|view, repo view), no curl/wget
#     to the GitHub API (line continuations are joined first).
# Controls: the read-only token and the absence of other secrets. These text checks read YAML
# as text, not as a parsed document, and may over-block (e.g. an echo that mentions git push).
# Usage: bash .github/read-only-workflows.sh [workflow dir]
#        bash .github/read-only-workflows.sh --selftest
set -uo pipefail

PERM_KEYS='actions|attestations|checks|contents|deployments|discussions|id-token|issues|models|packages|pages|pull-requests|repository-projects|security-events|statuses'
GH_READ='gh[[:space:]]+((pr|issue)[[:space:]]+(view|list|status|diff|checks)|(run|release)[[:space:]]+(list|view)|repo[[:space:]]+view)$'

# Permission values that are not read/none (prints file:line: text).
bad_permissions() {
  awk -v keys="$PERM_KEYS" -v SQ="'" '
    function trim(s) { sub(/^[ \t]+/, "", s); sub(/[ \t]+$/, "", s); return s }
    function unq(s) { s = trim(s); if (length(s) >= 2 && (substr(s, 1, 1) == "\"" || substr(s, 1, 1) == SQ) && substr(s, length(s), 1) == substr(s, 1, 1)) s = substr(s, 2, length(s) - 2); return s }
    function ok(v) { v = unq(v); return v == "read" || v == "none" }
    {
      raw = $0; line = $0; sub(/[ \t]+#.*$/, "", line)
      if (line ~ /^[ \t]*#/ || line ~ /^[ \t]*$/) next
      if (pending != "") {
        ind = match(line, /[^ \t]/) - 1
        if (ind > pind && line !~ /:/ && line !~ /^[ \t]*-/ && !ok(line)) print FILENAME ":" NR ": " raw
        pending = ""
      }
      pk = "^[ \t-]*[\"" SQ "]?permissions[\"" SQ "]?[ \t]*:"
      kk = "^[ \t]*[\"" SQ "]?(" keys ")[\"" SQ "]?[ \t]*:"
      if (match(line, pk)) {
        v = trim(substr(line, RLENGTH + 1))
        if (v == "" || v == "{}" || unq(v) == "read-all") next
        if (v ~ /^\{.*\}$/) {
          n = split(substr(v, 2, length(v) - 2), parts, ",")
          for (i = 1; i <= n; i++) {
            c = index(parts[i], ":")
            if (c == 0 || !ok(substr(parts[i], c + 1))) { print FILENAME ":" NR ": " raw; break }
          }
          next
        }
        print FILENAME ":" NR ": " raw; next
      }
      if (match(line, kk)) {
        v = trim(substr(line, RLENGTH + 1))
        if (v == "") { pending = line; pind = match(line, /[^ \t]/) - 1; next }
        if (!ok(v)) print FILENAME ":" NR ": " raw
      }
    }' "$1"
}

check_dir() {
  local dir=$1 fail=0 f joined
  note() { echo "$1" >&2; fail=1; }
  shopt -s nullglob
  local files=("$dir"/*.yml "$dir"/*.yaml)
  (( ${#files[@]} )) || { echo "nincs workflow: $dir" >&2; return 1; }
  for f in "${files[@]}"; do
    grep -qE "^[\"']?permissions[\"']?[[:space:]]*:" "$f" || note "$f: nincs felső szintű permissions: blokk"
    local bad; bad=$(bad_permissions "$f")
    [[ -n $bad ]] && { printf '%s\n' "$bad" | sed "s|^|nem read/none jog: |" >&2; fail=1; }
    grep -nE "[:{,[:space:]][[:space:]]*[\"']?(write|write-all)[\"']?[[:space:]]*([,}#]|$)|write-all" "$f" | grep -vE '^[0-9]+:[[:space:]]*#' \
      | sed "s|^|$f: írási jog: |" >&2 && fail=1
    grep -nE '\\(x[0-9A-Fa-f]{2}|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8})' "$f" | sed "s|^|$f: YAML escape (nem ellenőrizhető): |" >&2 && fail=1
    grep -nE 'secrets(\.[A-Za-z_]|\[)' "$f" | grep -vE 'secrets\.GITHUB_TOKEN([^A-Za-z0-9_]|$)' | sed "s|^|$f: secret (a tokenjogot megkerülheti): |" >&2 && fail=1
    grep -nE 'pull_request_target' "$f" | sed "s|^|$f: pull_request_target: |" >&2 && fail=1
    grep -noE "(^|[[:space:]{,-])[\"']?uses[\"']?[[:space:]]*:[[:space:]]*[\"']?[^[:space:]\"',}]+" "$f" \
      | grep -vE "uses[\"']?[[:space:]]*:[[:space:]]*[\"']?actions/" | sed "s|^|$f: nem actions/* action: |" >&2 && fail=1
    grep -nE "actions/github-script" "$f" | sed "s|^|$f: actions/github-script (tetszőleges API-hívás): |" >&2 && fail=1
    joined=$(awk '{ if (sub(/\\$/, "")) { buf = buf $0 } else { print buf $0; buf = "" } }' "$f")
    printf '%s\n' "$joined" | grep -nE '(^|[^[:alnum:]_-])git([^[:alnum:]_-].*)?[^[:alnum:]_-]push([^[:alnum:]_-]|$)' | grep -vE '^[0-9]+:[[:space:]]*#' \
      | sed "s|^|$f: git push: |" >&2 && fail=1
    printf '%s\n' "$joined" | grep -nE "(^|[^[:alnum:]_-])git([[:space:]]+-[^[:space:]]+)*[[:space:]]+[\"']?[$]" \
      | sed "s|^|$f: git-alparancs változóból: |" >&2 && fail=1
    printf '%s\n' "$joined" | grep -noE '(^|[^[:alnum:]_-])gh[[:space:]]+[a-z-]+([[:space:]]+[a-z-]+)?' | sed -E 's/^([0-9]+:)[^g]*/\1/' \
      | grep -vE "^[0-9]+:$GH_READ" | sed "s|^|$f: gh (csak olvasó alparancs engedett): |" >&2 && fail=1
    printf '%s\n' "$joined" | grep -nE '(curl|wget)[^#]*(api|uploads)\.github\.com' | sed "s|^|$f: GitHub API curl/wget-tel: |" >&2 && fail=1
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
    $'read-inline-map|0|    permissions: {contents: read, pull-requests: none}'
    $'read-quoted|0|    permissions:\n      contents: \'read\'\n      issues: "none"'
    $'gh-read|0|      - run: gh pr view 1 && gh run list'
    $'token-ok|0|      - env:\n          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}'
    $'write-escape|1|    permissions:\n      contents: "\\x77rite"'
    $'write-folded|1|    permissions:\n      contents: "wri\\\n        te"'
    $'write-next-line|1|    permissions:\n      contents:\n        write'
    $'write-unknown-value|1|    permissions:\n      packages: admin'
    $'pat-secret|1|      - env:\n          GH_TOKEN: ${{ secrets.MY_PAT }}'
    $'pat-secret-bracket|1|      - env:\n          T: ${{ secrets[\'MY_PAT\'] }}'
    $'gh-new|1|      - run: gh pr new --fill'
    $'gh-update-branch|1|      - run: gh pr update-branch 1'
    $'curl-data|1|      - run: curl -d @body.json https://api.github.com/repos/o/r/issues'
    $'git-var-subcommand|1|      - run: P=push; git $P origin main'
    $'github-script|1|      - uses: actions/github-script@v7'
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
