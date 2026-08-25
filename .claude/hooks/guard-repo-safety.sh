#!/usr/bin/env bash
# PreToolUse guard: blocks destructive git and filesystem operations.
#
# This repository regularly carries UNPUSHED user commits and hand-edited course
# content. A single hard reset or forced clean destroys work that has no other
# copy. CLAUDE.md asks Claude not to run these; this hook enforces it.
#
# Contract: reads the PreToolUse JSON on stdin, exits 2 with a stderr message to
# block, exits 0 to stay out of the way. Normal git (status, diff, add, commit,
# log, branch, checkout <branch>) and all test commands pass through untouched.
#
# Matching is FLAG-SPELLING AGNOSTIC on purpose: -f, -fd, -df and --force must
# all be caught. An earlier version matched only the short spellings and let
# "clean --force -d" and "rm -r -f" through. A rule that checks one spelling is
# the same failure class as an assert that checks one literal sentence — which is
# exactly how this repository once produced a false "0 regressions" report.
#
# Matching runs against the WHOLE command text, so a compound command is caught
# by any of its parts. Consequence: a command that merely *contains* one of these
# strings (writing this file with a heredoc, for example) is also blocked. That
# is deliberate over-blocking; use the Write tool for such files.
#
# A coarser second layer lives in .claude/settings.json (permissions.deny). It
# survives even when hooks are unavailable. Keep the two roughly in sync.
#
# One deliberate asymmetry: deny rules cannot carry exceptions, so a blanket
# "git rebase*" deny would also block `git rebase --abort`. settings.json therefore
# denies only the named dangerous rebase spellings, and THIS hook is the complete
# layer — it blocks every rebase form except the bare `--abort` recovery.
#
# Self-test:  bash .claude/hooks/guard-repo-safety.sh --selftest
set -uo pipefail

# True when a flag cluster contains the letter in any position, or the long form
# is present. has_flag <cmd> <short-letter> <long-name>
has_flag() {
  [[ $1 =~ [[:space:]]-[a-zA-Z]*$2[a-zA-Z]*([[:space:]]|$) ]] || [[ $1 =~ --$3([[:space:]=]|$) ]]
}

# Echoes a reason and returns 0 when the command must be blocked.
verdict() {
  local cmd=" ${1} "

  # Recovery invocations RESTORE a previous state instead of destroying one, so they
  # must stay available — an in-progress rebase or merge is exactly when you need
  # them. Strip the four exact invocations before the destructive checks run.
  #
  # This is NOT a blanket allowance for anything containing "--abort". The pattern
  # includes the trailing space, and `cmd` is space-padded and whitespace-collapsed
  # before it gets here, so only a complete invocation is removed:
  #   "git rebase --abort"    -> stripped, allowed
  #   "git rebase --aborted"  -> NOT stripped (next char is "e"), still blocked
  #   "git rebase --abort && git rebase -i HEAD~3" -> only the first is stripped,
  #                                                  the second still matches, blocked
  # `--continue`, `--skip` and `--quit` are deliberately NOT recovery: they carry an
  # in-progress history rewrite forward, or leave it half-applied.
  #
  # Shell separators are padded first, so a recovery command written as
  # `git rebase --abort;` or `...--abort&&x` still ends on a space boundary and is
  # recognised as complete. This also tightens the path checks further down.
  cmd="${cmd//;/ ; }"
  cmd="${cmd//&/ & }"
  cmd="${cmd//|/ | }"
  cmd="${cmd//git rebase --abort / }"
  cmd="${cmd//git merge --abort / }"
  cmd="${cmd//git cherry-pick --abort / }"
  cmd="${cmd//git revert --abort / }"

  if [[ $cmd =~ [[:space:]]git[[:space:]] ]]; then
    [[ $cmd =~ git\ .*reset ]] && [[ $cmd =~ --(hard|merge) ]] && \
      { echo "a hard/merge reset eldobja a nem commitolt munkát"; return 0; }
    [[ $cmd =~ git\ .*clean ]] && has_flag "$cmd" f force && \
      { echo "a kényszerített clean visszavonhatatlanul törli a nem követett fájlokat"; return 0; }
    [[ $cmd =~ git\ .*checkout ]] && [[ $cmd =~ [[:space:]]--[[:space:]] ]] && \
      { echo "checkout -- <path> eldobja a working tree változtatásait"; return 0; }
    [[ $cmd =~ git\ .*checkout[[:space:]]\.[[:space:]] ]] && \
      { echo "checkout . eldobja a working tree változtatásait"; return 0; }
    [[ $cmd =~ git\ .*(checkout|switch) ]] && has_flag "$cmd" f force && \
      { echo "a kényszerített checkout/switch eldobja a working tree változtatásait"; return 0; }
    [[ $cmd =~ git\ .*(checkout|switch) ]] && [[ $cmd =~ [[:space:]]-[BC][[:space:]] ]] && \
      { echo "checkout -B / switch -C felülír egy meglévő branch-et"; return 0; }
    [[ $cmd =~ git\ .*switch ]] && [[ $cmd =~ --discard-changes ]] && \
      { echo "a switch --discard-changes eldobja a working tree változtatásait"; return 0; }
    [[ $cmd =~ git\ .*restore ]] && { [[ ! $cmd =~ --staged ]] || [[ $cmd =~ --worktree ]]; } && \
      { echo "a restore eldobja a working tree változtatásait (csak --staged engedett)"; return 0; }
    [[ $cmd =~ git\ .*push ]] && \
      { has_flag "$cmd" f force || [[ $cmd =~ (--force-with-lease|--mirror|--delete|[[:space:]]\+) ]]; } && \
      { echo "a kényszerített vagy törlő push átírja a távoli historyt"; return 0; }
    [[ $cmd =~ git\ .*rebase ]] && \
      { echo "a rebase átírja a lokális historyt (a repo szabálya tiltja)"; return 0; }
    [[ $cmd =~ git\ .*commit ]] && [[ $cmd =~ --amend ]] && \
      { echo "az amend felülírja a felhasználó checkpoint-commitját"; return 0; }
    [[ $cmd =~ git\ .*(filter-branch|filter-repo) ]] && \
      { echo "history rewrite"; return 0; }
    [[ $cmd =~ git\ .*reflog[[:space:]]+(delete|expire) ]] && \
      { echo "a reflog törlése megszünteti az utolsó visszaállítási esélyt"; return 0; }
    [[ $cmd =~ git\ .*update-ref ]] && [[ $cmd =~ [[:space:]]-d[[:space:]] ]] && \
      { echo "ref törlése elérhetetlenné tesz commitokat"; return 0; }
    [[ $cmd =~ git\ .*gc ]] && [[ $cmd =~ --prune ]] && \
      { echo "a prune végleg törli az elérhetetlen objektumokat"; return 0; }
    [[ $cmd =~ git\ .*stash[[:space:]]+(drop|clear) ]] && \
      { echo "a stash törlése végleges"; return 0; }
    [[ $cmd =~ git\ .*branch ]] && [[ $cmd =~ [[:space:]]-(D|M)[[:space:]] ]] && \
      { echo "branch kényszerített törlése/átnevezése pusholatlan commitokat veszíthet"; return 0; }
    [[ $cmd =~ git\ .*branch ]] && has_flag "$cmd" f force && \
      { echo "a kényszerített branch felülír egy meglévő branch-et"; return 0; }
    [[ $cmd =~ git\ .*worktree[[:space:]]+remove ]] && has_flag "$cmd" f force && \
      { echo "worktree kényszerített eltávolítása eldobja a benne lévő munkát"; return 0; }
  fi

  # Deletion aimed at the repository. The ecosystem and the course content are the
  # things with no second copy, so ANY delete naming them is blocked, flags or not.
  if [[ $cmd =~ [[:space:]](rm|unlink|shred|trash)[[:space:]] ]]; then
    if [[ $cmd =~ (02\ Tervezet|01\ Fejlesztés|\.git|\.claude|tools/|CLAUDE\.md|README\.md|\.gitignore) ]]; then
      echo "a repository tartalmának törlése"; return 0
    fi
    if has_flag "$cmd" r recursive && [[ $cmd =~ [[:space:]](\.|\.\.|/|\*|~|\$\(pwd\)|\$PWD)[[:space:]] ]]; then
      echo "rekurzív törlés a munkakönyvtárra"; return 0
    fi
  fi

  return 1
}

if [[ "${1:-}" == "--selftest" ]]; then
  fail=0
  # Test corpus is assembled from parts so this file's own text does not read as a
  # runnable destructive command to greps, scanners, or this very hook.
  G="git"; R="rm"
  must_block=(
    "$G reset --hard HEAD~1" "$G reset --hard" "$G reset --merge"
    "$G clean -f" "$G clean -fd" "$G clean -fdx" "$G clean -df" "$G clean -xdf"
    "$G clean --force" "$G clean --force -d" "$G clean -d --force"
    "$G checkout -- ." "$G checkout -- 02 Tervezet/x.md" "$G checkout ."
    "$G checkout -f" "$G checkout -f main" "$G checkout --force main"
    "$G switch -f main" "$G switch --force main" "$G switch --discard-changes main"
    "$G checkout -B main" "$G switch -C main"
    "$G restore ." "$G restore 02 Tervezet/x.md" "$G restore --staged --worktree x"
    "$G push --force" "$G push -f origin main" "$G push origin main -f"
    "$G push --force-with-lease origin HEAD" "$G push --mirror" "$G push origin --delete x"
    "$G rebase -i HEAD~3" "$G rebase main" "$G rebase --continue" "$G rebase --skip"
    "$G rebase --onto main HEAD~2" "$G rebase --quit" "$G rebase --aborted"
    "$G rebase --abort && $G rebase -i HEAD~3" "$G commit --amend --no-edit"
    "$G filter-branch --tree-filter x" "$G filter-repo --path x"
    "$G branch -D audit-fixes-2026-08-25" "$G branch --force main HEAD~2" "$G branch -M main"
    "$G stash clear" "$G stash drop" "$G reflog expire --expire=now --all"
    "$G gc --prune=now" "$G update-ref -d refs/heads/x"
    "$G worktree remove --force ../wt" "$G worktree remove -f ../wt"
    "$R -rf 02 Tervezet" "$R -r -f 02 Tervezet" "$R -rf ." "$R -fr ." "$R -rf .claude"
    "$R CLAUDE.md" "$R -f .claude/settings.json" "$R -rf tools/"
    "$R --recursive --force ." "$R -rf ~"
    "$G status && $G reset --hard" "cd /tmp && $G clean --force -d"
  )
  must_pass=(
    "$G status" "$G status --short" "$G diff" "$G diff --check" "$G diff --stat"
    "$G add 02 Tervezet/Modulok/M3/x.md" "$G add -A" "$G add -f 02 Tervezet/x.md"
    "$G commit -m 'fix: x'" "$G commit -F msg.txt" "$G log -10 --oneline"
    "$G branch --show-current" "$G branch -m old new" "$G branch -a" "$G branch -v"
    "$G checkout main" "$G checkout -b feature/x" "$G switch main" "$G switch -c feature/x"
    "$G push origin main" "$G push -u origin HEAD" "$G restore --staged 02 Tervezet/x.md"
    "$G stash" "$G stash pop" "$G stash list" "$G show HEAD" "$G clean -n" "$G clean -nd"
    "$G worktree list" "$G rev-parse HEAD" "$G reflog" "$G gc"
    "$G rebase --abort" "$G merge --abort" "$G cherry-pick --abort" "$G revert --abort"
    "$G status && $G rebase --abort" "$G merge main" "$G revert HEAD" "$G cherry-pick abc123"
    "$G rebase --abort;" "$G rebase --abort && $G status" "cd /repo && $G rebase --abort"
    "$G rebase --abort; echo done" "$G merge --abort;" "$G cherry-pick --abort && $G status"
    "python3 tools/content_integrity.py" "python3 tools/content_integrity.py --release-report"
    "grep -rn mintaszo '02 Tervezet'" "ls -la" "ls -lf" "cat CLAUDE.md"
    "$R -rf /private/tmp/claude-501/scratch" "$R /tmp/x.json"
    "bash .claude/hooks/guard-repo-safety.sh --selftest"
  )
  for c in "${must_block[@]}"; do
    if r=$(verdict "$c"); then printf 'BLOCK ok   %-45s (%s)\n' "$c" "$r"
    else printf 'MISS  FAIL %s\n' "$c"; fail=1; fi
  done
  for c in "${must_pass[@]}"; do
    if r=$(verdict "$c"); then printf 'BLOCK FAIL %-45s (%s)\n' "$c" "$r"; fail=1
    else printf 'PASS  ok   %s\n' "$c"; fi
  done
  echo "--- ${#must_block[@]} must-block, ${#must_pass[@]} must-pass ---"
  [[ $fail -eq 0 ]] && echo "--- selftest OK ---" || echo "--- selftest FAILED ---"
  exit $fail
fi

payload=$(cat)
if command -v jq >/dev/null 2>&1; then
  command_text=$(printf '%s' "$payload" | jq -r '.tool_input.command // empty' 2>/dev/null)
elif command -v python3 >/dev/null 2>&1; then
  command_text=$(printf '%s' "$payload" | python3 -c \
    'import json,sys; print(json.load(sys.stdin).get("tool_input",{}).get("command",""))' 2>/dev/null)
else
  # No JSON parser: fail closed by scanning the raw payload rather than waving it through.
  command_text="$payload"
fi
[[ -z "$command_text" ]] && exit 0

command_text=$(printf '%s' "$command_text" | tr '\n' ' ' | tr -s ' ')

if reason=$(verdict "$command_text"); then
  cat >&2 <<MSG
BLOKKOLVA (.claude/hooks/guard-repo-safety.sh): $reason

Parancs: $command_text

Ezen a branchen pusholatlan felhasználói commitok és kézzel szerkesztett tananyag van.
Destruktív git- és törlőműveletek tiltottak — lásd CLAUDE.md "Git-biztonság".

Ehelyett: status/diff olvasás, stash (drop nélkül), vagy új branch és commit.
Ha ez tényleg kell, a felhasználó futtassa kézzel.
MSG
  exit 2
fi
exit 0
