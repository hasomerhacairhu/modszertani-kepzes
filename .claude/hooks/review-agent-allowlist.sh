#!/usr/bin/env bash
# Agent-scoped PreToolUse hook of the course-review-orchestrator subagent: it may start
# only the five read-only lens reviewers and the verifier. An `Agent(type, …)` list is
# ignored inside a subagent definition (sub-agents docs), so the allowlist lives here.
# Exit 2 = block (honoured in every permission mode). Self-test: --selftest
set -uo pipefail
ALLOWED='pedagogy-reviewer|assessment-reviewer|hungarian-editorial-reviewer|safety-policy-reviewer|implementation-reviewer|verifier'

check() {
  [[ $1 =~ ^($ALLOWED)$ ]]
}

if [[ "${1:-}" == "--selftest" ]]; then
  fail=0
  for t in pedagogy-reviewer verifier implementation-reviewer; do check "$t" || { echo "FAIL allow $t"; fail=1; }; done
  for t in general-purpose Explore Plan claude "" verifier2 "verifier x"; do check "$t" && { echo "FAIL block '$t'"; fail=1; }; done
  [[ $fail -eq 0 ]] && echo "--- selftest OK ---" || echo "--- selftest FAILED ---"
  exit $fail
fi

payload=$(cat)
if command -v jq >/dev/null 2>&1; then
  t=$(printf '%s' "$payload" | jq -r '.tool_input.subagent_type // empty' 2>/dev/null)
else
  t=$(printf '%s' "$payload" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("subagent_type") or "")' 2>/dev/null)
fi
check "$t" && exit 0
echo "A /course-review csak az öt read-only lencse-reviewert és a verifiert indíthatja (kért: '${t:-?}')." >&2
exit 2
