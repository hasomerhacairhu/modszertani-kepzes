#!/usr/bin/env bash
# PreToolUse guard: blocks destructive git, gh and filesystem operations, and asks
# before anything that publishes (push, PR merge).
#
# This repository regularly carries UNPUSHED user commits and hand-edited course
# content. A single hard reset or forced clean destroys work that has no other
# copy. CLAUDE.md asks Claude not to run these; this hook enforces it.
#
# Contract: reads the PreToolUse JSON on stdin.
#   - block: exit 2 with a stderr message;
#   - ask:   exit 0 with {"hookSpecificOutput": {"permissionDecision": "ask", ...}} on stdout
#            (every git push and gh pr merge, in any spelling, incl. `git -C <path> push`;
#            gh pr close --delete-branch; gh api DELETE);
#   - also blocks Bash edits of course content (sed -i, perl -i, tee, a redirect into
#     `02 Tervezet/`, an inline script writing there): CLAUDE.md allows Edit/Write only;
#   - pass:  exit 0 silently. Normal git (status, diff, add, commit, log, branch,
#            checkout <branch>, switch -c) and all test commands pass through.
# Every block is evaluated before any ask. The settings.json `ask` rules cover the same
# publishing commands, because only an explicit ask rule is guaranteed to prompt in
# every permission mode.
#
# Matching is FLAG-SPELLING AGNOSTIC on purpose: -f, -fd, -df and --force must
# all be caught. An earlier version matched only the short spellings and let
# "clean --force -d" and "rm -r -f" through. A rule that checks one spelling is
# the same failure class as an assert that checks one literal sentence — which is
# exactly how this repository once produced a false "0 regressions" report.
#
# Matching is PER INVOCATION: the command text is split at shell separators
# (&&, ||, ;, &, |) and at every `git`/`gh` token, git global options (-C <path>,
# -c <k=v>, --git-dir=…, --no-pager) are normalised away, and flags are read only
# after the subcommand of that invocation. So `git log --grep=rebase`, a " + " in a
# lesson file name, or `git checkout -b x && git diff main -- f` no longer trip a
# rule meant for another command — while `bash -c "git reset --hard"`, a git
# command inside a heredoc, or a later part of a compound command is still caught.
# A command that merely mentions a dangerous git invocation (a commit message
# quoting one, say) can still be blocked; use `git commit -F <file>` for those.
#
# A coarser second layer lives in .claude/settings.json (permissions.deny / ask). It
# survives even when hooks are unavailable. Keep the two roughly in sync.
#
# One deliberate asymmetry: deny rules cannot carry exceptions, so a blanket
# "git rebase*" deny would also block `git rebase --abort`. settings.json therefore
# denies only the named dangerous rebase spellings, and THIS hook is the complete
# layer — it blocks every rebase form except the bare `--abort` recovery.
#
# Written for bash 3.2 (macOS /usr/bin/env bash): no mapfile, no ${x^^}.
#
# Self-test:  bash .claude/hooks/guard-repo-safety.sh --selftest
set -uo pipefail
set -f   # never glob: command text is split into words below

REPO_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." 2>/dev/null && pwd)

# Paths with no second copy. Matched as a relative path at the start of a word (or
# after the repository root, which is rewritten to a relative path first), so the
# same names under /tmp or ~/.claude are not the repository.
PROT='(02(\\)?[[:space:]]Tervezet|01(\\)?[[:space:]]Fejlesztés|\.git|\.github|\.claude|tools|CLAUDE\.md|README\.md|\.gitignore|\.gitattributes)'
REL_RE="(^|[[:space:]\"'=])(\\./)?${PROT}([/[:space:]\"']|\$)"
TOP_RE="(^|[[:space:]\"'])(\\./)?${PROT}/?([[:space:]\"']|\$)"
RM_RE="(^|[[:space:]\"'(])(/bin/|/usr/bin/|\\\\)?(rm|unlink|shred|trash)[[:space:]]"
# Course content is edited only with the Edit/Write tools (CLAUDE.md): the path-scoped
# rules in .claude/rules/ load only for those, and a Bash edit bypasses them.
CONTENT_RE='02(\\)?[[:space:]]Tervezet'
SED_I_RE='(^|[[:space:]])(sed|gsed)[[:space:]]([^|]*[[:space:]])?(-[a-zA-Z]*i|--in-place)'
PERL_I_RE='(^|[[:space:]])perl[[:space:]]+(-[a-zA-Z]*[[:space:]]+)*-[a-zA-Z]*i'
REDIR_RE=">>?[[:space:]]*[\"']?[^[:space:]\"'>]*02(\\\\)?[[:space:]]Tervezet"
SCRIPT_WRITE_RE="(write_text|write_bytes|writeFileSync|appendFileSync|open\([^)]*[\"'][wa]\+?[\"'])"
SPLIT_RE='^(.*[^[:alnum:]_./-])((git|gh)[[:space:]].*)$'
OPT_VAL_RE="^git[[:space:]]+(-C|-c)[[:space:]]+(\"[^\"]*\"|'[^']*'|[^[:space:]]+)(.*)\$"
OPT_FLAG_RE='^git[[:space:]]+(--git-dir=|--work-tree=|--namespace=|--exec-path=|--no-pager|-P|--no-replace-objects|--literal-pathspecs|--no-optional-locks)([^[:space:]]*)(.*)$'

# True when a flag cluster contains the letter in any position, or the long form
# is present. has_flag <text> <short-letter> <long-name>
has_flag() {
  [[ $1 =~ [[:space:]]-[a-zA-Z]*$2[a-zA-Z]*([[:space:]]|$) ]] || [[ $1 =~ --$3([[:space:]=]|$) ]]
}

# One invocation per line: split at shell separators, then before every git/gh token.
split_pieces() {
  local s=$1 line out=""
  s=${s//&&/$'\n'}; s=${s//||/$'\n'}
  s=${s//;/$'\n'}; s=${s//&/$'\n'}; s=${s//|/$'\n'}
  while IFS= read -r line; do
    while [[ $line =~ $SPLIT_RE ]]; do
      out+="${BASH_REMATCH[2]}"$'\n'
      line=${BASH_REMATCH[1]}
    done
    out+="$line"$'\n'
  done <<< "$s"
  printf '%s' "$out"
}

# Drops git's global options so `git -C <path> push` is read as `git push`.
norm_git() {
  local p=$1
  while [[ $p =~ $OPT_VAL_RE ]] || [[ $p =~ $OPT_FLAG_RE ]]; do
    p="git${BASH_REMATCH[3]}"
  done
  printf '%s' "$p"
}

# Positional (non-flag) words after the subcommand; quoted strings count as one word.
positional_count() {
  local t=$1 n=0 w
  while [[ $t =~ ^(.*)\"[^\"]*\"(.*)$ ]]; do t="${BASH_REMATCH[1]}Q${BASH_REMATCH[2]}"; done
  while [[ $t =~ ^(.*)\'[^\']*\'(.*)$ ]]; do t="${BASH_REMATCH[1]}Q${BASH_REMATCH[2]}"; done
  t=${t//\\ /_}
  for w in $t; do [[ $w == -* ]] || n=$((n + 1)); done
  echo "$n"
}

names_repo_path() {   # names_repo_path <text>: a protected path, relative or under REPO_ROOT
  local q=$1
  if [[ -n $REPO_ROOT ]]; then
    q=${q//"$REPO_ROOT"\// }
    q=${q//"$REPO_ROOT"/ . }
  fi
  [[ $q =~ $REL_RE ]]
}

# Echoes a reason. Returns 0 = block, 2 = ask, 1 = pass.
check_piece() {
  local p=$1 sub rest up noforce=0 staged=0 worktree=0
  p=${p#"${p%%[![:space:]]*}"}

  # --- deletion or removal aimed at the repository (any program) -------------------
  if [[ ! $p =~ ^(git|gh)[[:space:]] ]]; then
    local q=" $p "
    if [[ $q =~ $CONTENT_RE ]]; then
      if [[ $q =~ $SED_I_RE ]] || [[ $q =~ $PERL_I_RE ]] || [[ $q =~ (^|[[:space:]])tee[[:space:]] ]] || [[ $q =~ $REDIR_RE ]]; then
        echo "a tananyagot (02 Tervezet) Edit/Write eszközzel szerkeszd — a Bash-szerkesztés megkerüli a .claude/rules szabályait"; return 0
      fi
    fi
    if [[ $q =~ $RM_RE ]]; then
      names_repo_path "$q" && { echo "a repository tartalmának törlése"; return 0; }
      if has_flag "$q" r recursive && [[ $q =~ [[:space:]](\.|\.\.|/|\*|~|\$\(pwd\)|\$PWD|\`pwd\`)/?[[:space:]] ]]; then
        echo "rekurzív törlés a munkakönyvtárra"; return 0
      fi
    fi
    if [[ $q =~ (^|[[:space:]])find[[:space:]] ]] && [[ $q =~ (-delete|-exec[[:space:]]+(/bin/)?rm) ]] && names_repo_path "$q"; then
      echo "find -delete a repository tartalmán"; return 0
    fi
    if [[ $q =~ (rmtree|os\.remove|os\.unlink|os\.rmdir|unlinkSync|rmSync|fs\.rm|shutil\.move) ]] && names_repo_path "$q"; then
      echo "programból indított törlés a repository tartalmán"; return 0
    fi
    if [[ $q =~ (^|[[:space:]])mv[[:space:]] ]]; then
      local qq=$q
      [[ -n $REPO_ROOT ]] && qq=${qq//"$REPO_ROOT"\// }
      [[ $qq =~ $TOP_RE ]] && { echo "a repository egy fő mappájának vagy fájljának elmozdítása"; return 0; }
    fi
    return 1
  fi

  # --- gh ------------------------------------------------------------------------
  if [[ $p =~ ^gh[[:space:]] ]]; then
    up=$(printf '%s' "$p" | tr '[:lower:]' '[:upper:]')
    [[ $p =~ ^gh[[:space:]]+(repo|release)[[:space:]]+delete ]] && { echo "gh $([[ $p =~ release ]] && echo release || echo repo) delete visszavonhatatlan"; return 0; }
    [[ $p =~ ^gh[[:space:]]+repo[[:space:]]+edit ]] && [[ $p =~ --visibility ]] && { echo "a repository láthatóságának átállítása"; return 0; }
    if [[ $p =~ ^gh[[:space:]]+api ]] && [[ $up =~ (-X|--METHOD)[[:space:]=]*(DELETE|PUT|PATCH) ]] && [[ $p =~ git/refs ]]; then
      echo "távoli ref írása vagy törlése a GitHub API-n át"; return 0
    fi
    [[ $p =~ ^gh[[:space:]]+pr[[:space:]]+merge ]] && { echo "gh pr merge: csak a felhasználó kifejezett kérésére"; return 2; }
    if [[ $p =~ ^gh[[:space:]]+pr[[:space:]]+close ]] && [[ " $p " =~ [[:space:]](--delete-branch|-d)([[:space:]]|$) ]]; then
      echo "gh pr close --delete-branch: távoli branchet töröl"; return 2
    fi
    if [[ $p =~ ^gh[[:space:]]+api ]] && [[ $up =~ (-X|--METHOD)[[:space:]=]*DELETE ]]; then
      echo "gh api DELETE: csak kifejezett kérésre"; return 2
    fi
    return 1
  fi

  # --- git -----------------------------------------------------------------------
  [[ $p =~ clean\.requireForce=false ]] && noforce=1
  p=$(norm_git "$p")
  [[ $p =~ ^git[[:space:]]+([a-z][a-z0-9-]*)(.*)$ ]] || return 1
  sub=${BASH_REMATCH[1]}; rest=" ${BASH_REMATCH[2]} "
  # A closing quote or paren (bash -c "git reset --hard") must not glue onto the last flag.
  rest=${rest//\"/ \" }; rest=${rest//\'/ \' }; rest=${rest//\`/ \` }; rest=${rest//)/ ) }

  case $sub in
    reset)
      [[ $rest =~ [[:space:]]--(hard|merge|keep)([[:space:]=]|$) ]] && \
        { echo "a hard/merge/keep reset eldobja a nem commitolt munkát"; return 0; }
      if [[ ! $rest =~ [[:space:]]--[[:space:]] ]] && \
         [[ $rest =~ [[:space:]](HEAD[~^][^[:space:]]*|@[~^{][^[:space:]]*|ORIG_HEAD|FETCH_HEAD|origin/[^[:space:]]+|main|master|[0-9a-f]{7,40})([[:space:]]|$) ]]; then
        echo "a reset <commit> átállítja a branchet (--soft/--mixed alakban is history rewrite)"; return 0
      fi ;;
    clean)
      has_flag "$rest" f force && \
        { echo "a kényszerített clean visszavonhatatlanul törli a nem követett fájlokat"; return 0; }
      if (( noforce )) && ! has_flag "$rest" n dry-run && ! has_flag "$rest" i interactive; then
        echo "clean.requireForce=false mellett a clean -f nélkül is töröl"; return 0
      fi ;;
    checkout)
      [[ $rest =~ [[:space:]]--[[:space:]] ]] && { echo "checkout -- <path> eldobja a working tree változtatásait"; return 0; }
      [[ $rest =~ [[:space:]]\.[[:space:]] ]] && { echo "checkout . eldobja a working tree változtatásait"; return 0; }
      has_flag "$rest" f force && { echo "a kényszerített checkout eldobja a working tree változtatásait"; return 0; }
      [[ $rest =~ [[:space:]]-B[[:space:]] ]] && { echo "checkout -B felülír egy meglévő branch-et"; return 0; }
      if [[ ! $rest =~ [[:space:]](-b|--orphan)[[:space:]] ]] && (( $(positional_count "$rest") >= 2 )); then
        echo "checkout <commit> <path> felülírja a fájlt a working tree-ben"; return 0
      fi ;;
    switch)
      has_flag "$rest" f force && { echo "a kényszerített switch eldobja a working tree változtatásait"; return 0; }
      [[ $rest =~ [[:space:]]-C[[:space:]] ]] && { echo "switch -C felülír egy meglévő branch-et"; return 0; }
      [[ $rest =~ --discard-changes ]] && { echo "a switch --discard-changes eldobja a working tree változtatásait"; return 0; }
      ;;
    restore)
      if [[ $rest =~ [[:space:]]--staged([[:space:]]|$) ]] || [[ $rest =~ [[:space:]]-[a-zA-Z]*S[a-zA-Z]*([[:space:]]|$) ]]; then staged=1; fi
      if [[ $rest =~ [[:space:]]--worktree([[:space:]]|$) ]] || [[ $rest =~ [[:space:]]-[a-zA-Z]*W[a-zA-Z]*([[:space:]]|$) ]]; then worktree=1; fi
      if (( ! staged || worktree )); then
        echo "a restore eldobja a working tree változtatásait (csak --staged engedett)"; return 0
      fi ;;
    push)
      if has_flag "$rest" f force || has_flag "$rest" d delete || \
         [[ $rest =~ --(force-with-lease|force-if-includes|mirror|prune)([[:space:]=]|$) ]] || \
         [[ $rest =~ [[:space:]][+:][^[:space:]] ]]; then
        echo "a kényszerített vagy törlő push átírja a távoli historyt"; return 0
      fi
      echo "git push: csak a felhasználó kifejezett kérésére"; return 2 ;;
    pull)
      if [[ $rest =~ [[:space:]]--rebase(=(true|merges|interactive|i|m))?([[:space:]]|$) ]] || \
         [[ $rest =~ [[:space:]]-[a-zA-Z]*r[a-zA-Z]*([[:space:]]|$) ]]; then
        echo "a pull --rebase átírja a lokális historyt"; return 0
      fi ;;
    rebase)
      [[ $rest =~ ^[[:space:]]*--abort[[:space:]\"\'\`\)]*$ ]] || \
        { echo "a rebase átírja a lokális historyt (a repo szabálya tiltja)"; return 0; } ;;
    commit)
      [[ $rest =~ [[:space:]]--amend([[:space:]]|$) ]] && \
        { echo "az amend felülírja a felhasználó checkpoint-commitját"; return 0; } ;;
    filter-branch|filter-repo)
      echo "history rewrite"; return 0 ;;
    reflog)
      [[ $rest =~ ^[[:space:]]*(delete|expire) ]] && \
        { echo "a reflog törlése megszünteti az utolsó visszaállítási esélyt"; return 0; } ;;
    update-ref)
      has_flag "$rest" d delete && { echo "ref törlése elérhetetlenné tesz commitokat"; return 0; } ;;
    prune)
      echo "a prune végleg törli az elérhetetlen objektumokat"; return 0 ;;
    gc)
      [[ $rest =~ --prune ]] && { echo "a prune végleg törli az elérhetetlen objektumokat"; return 0; } ;;
    stash)
      [[ $rest =~ ^[[:space:]]*(drop|clear) ]] && { echo "a stash törlése végleges"; return 0; } ;;
    branch)
      [[ $rest =~ [[:space:]]-(D|M|C)[[:space:]] ]] && \
        { echo "branch kényszerített törlése/átnevezése/másolása pusholatlan commitokat veszíthet"; return 0; }
      has_flag "$rest" f force && { echo "a kényszerített branch felülír egy meglévő branch-et"; return 0; } ;;
    worktree)
      [[ $rest =~ ^[[:space:]]*remove ]] && has_flag "$rest" f force && \
        { echo "worktree kényszerített eltávolítása eldobja a benne lévő munkát"; return 0; } ;;
    rm)
      [[ $rest =~ [[:space:]]--cached([[:space:]]|$) ]] && return 1
      names_repo_path "$rest" && { echo "a repository tartalmának törlése"; return 0; } ;;
  esac
  return 1
}

# Echoes a reason. Returns 0 = block, 2 = ask, 1 = pass. All blocks win over any ask.
verdict() {
  local piece r rc ask=""
  # An inline script spans separators (`;` splits it into pieces), so check it whole.
  if [[ $1 =~ (^|[[:space:]])(python3?|node|ruby)[[:space:]] ]] && [[ $1 =~ $CONTENT_RE ]] && [[ $1 =~ $SCRIPT_WRITE_RE ]]; then
    echo "a tananyagot (02 Tervezet) Edit/Write eszközzel szerkeszd — szkriptből írni megkerüli a .claude/rules szabályait"; return 0
  fi
  while IFS= read -r piece; do
    [[ -z ${piece//[[:space:]]/} ]] && continue
    r=$(check_piece "$piece"); rc=$?
    (( rc == 0 )) && { echo "$r"; return 0; }
    (( rc == 2 )) && [[ -z $ask ]] && ask=$r
  done <<< "$(split_pieces "$1")"
  [[ -n $ask ]] && { echo "$ask"; return 2; }
  return 1
}

if [[ "${1:-}" == "--selftest" ]]; then
  fail=0
  # Test corpus is assembled from parts so this file's own text does not read as a
  # runnable destructive command to greps, scanners, or this very hook.
  G="git"; R="rm"; H="gh"; T="02 Tervezet"
  must_block=(
    "$G reset --hard HEAD~1" "$G reset --hard" "$G reset --merge"
    "$G clean -f" "$G clean -fd" "$G clean -fdx" "$G clean -df" "$G clean -xdf"
    "$G clean --force" "$G clean --force -d" "$G clean -d --force"
    "$G checkout -- ." "$G checkout -- $T/x.md" "$G checkout ."
    "$G checkout -f" "$G checkout -f main" "$G checkout --force main"
    "$G switch -f main" "$G switch --force main" "$G switch --discard-changes main"
    "$G checkout -B main" "$G switch -C main"
    "$G restore ." "$G restore $T/x.md" "$G restore --staged --worktree x"
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
    "$R -rf $T" "$R -r -f $T" "$R -rf ." "$R -fr ." "$R -rf .claude"
    "$R CLAUDE.md" "$R -f .claude/settings.json" "$R -rf tools/"
    "$R --recursive --force ." "$R -rf ~"
    "$G status && $G reset --hard" "cd /tmp && $G clean --force -d"
    # 2026-10-03 governance audit: false negatives that got through before
    "$G push -d origin x" "$G push origin :x" "$G push --prune origin" "$G -C /r push --force"
    "$G restore --staged -W f" "$G restore -SW f"
    "$G reset --soft HEAD~1" "$G reset HEAD~3" "$G reset --keep HEAD~1" "$G reset origin/main"
    "$G checkout HEAD~1 \"$T/x.md\"" "$G -c clean.requireForce=false clean -d"
    "$G pull --rebase" "$G pull -r origin main" "$G update-ref --delete refs/heads/x" "$G prune"
    "bash -c \"$G reset --hard\"" "cat > f <<EOF $G reset --hard EOF"
    "$R -rf 02\\ Tervezet/x" "/bin/$R -rf \"$T\"" "\\$R -rf tools" "find \"$T\" -name x -delete"
    "python3 -c \"import shutil; shutil.rmtree('$T')\"" "mv \"$T\" /tmp/" "$R -rf $REPO_ROOT/tools"
    "$H repo delete x --yes" "$H release delete v1" "$H api -X DELETE repos/o/r/git/refs/heads/x"
    "$H api --method PATCH repos/o/r/git/refs/heads/main -f sha=x"
    # course content only through Edit/Write
    "sed -i '' 's/a/b/' \"$T/x.md\"" "sed -E -i.bak 's/a/b/' \"$T/x.md\"" "perl -pi -e 's/a/b/' \"$T/x.md\""
    "echo x > \"$T/x.md\"" "echo x >> \"$T/Modulok/a.md\"" "cat /tmp/x > \"/Users/u/repo/$T/x.md\""
    "printf x | tee \"$T/x.md\"" "python3 - <<EOF p='$T/x.md'; open(p,'w').write('x') EOF"
    "python3 -c \"import pathlib; pathlib.Path('$T/x.md').write_text('x')\""
  )
  must_pass=(
    "$G status" "$G status --short" "$G diff" "$G diff --check" "$G diff --stat"
    "$G add $T/Modulok/M3/x.md" "$G add -A" "$G add -f $T/x.md"
    "$G commit -m 'fix: x'" "$G commit -F msg.txt" "$G log -10 --oneline"
    "$G branch --show-current" "$G branch -m old new" "$G branch -a" "$G branch -v"
    "$G checkout main" "$G checkout -b feature/x" "$G switch main" "$G switch -c feature/x"
    "$G restore --staged $T/x.md"
    "$G stash" "$G stash pop" "$G stash list" "$G show HEAD" "$G clean -n" "$G clean -nd"
    "$G worktree list" "$G rev-parse HEAD" "$G reflog" "$G gc"
    "$G rebase --abort" "$G merge --abort" "$G cherry-pick --abort" "$G revert --abort"
    "$G status && $G rebase --abort" "$G merge main" "$G revert HEAD" "$G cherry-pick abc123"
    "$G rebase --abort;" "$G rebase --abort && $G status" "cd /repo && $G rebase --abort"
    "$G rebase --abort; echo done" "$G merge --abort;" "$G cherry-pick --abort && $G status"
    "python3 tools/content_integrity.py" "python3 tools/content_integrity.py --release-report"
    "grep -rn mintaszo '$T'" "ls -la" "ls -lf" "cat CLAUDE.md"
    "$R -rf /private/tmp/claude-501/scratch" "$R /tmp/x.json"
    "bash .claude/hooks/guard-repo-safety.sh --selftest"
    # 2026-10-03 governance audit: false positives that were blocked before
    "$G log -1 && $H repo view --json rebaseMergeAllowed" "$G pull --no-rebase" "$G pull --rebase=false"
    "$G config --get pull.rebase" "$G log --grep=rebase" "$G grep -n \"reset --hard\" CLAUDE.md"
    "$G add \"$T/Modulok/M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md\" && $G commit -m x"
    "$G checkout -b x && $G diff main -- $T/x.md" "$G restore -S $T/x.md" "$G -C /r rebase --abort"
    "$G rm --cached \"$T/x.md\"" "$R -rf /private/tmp/x/scratchpad/tools/" "$R ~/.claude/projects/x/memory/a.md"
    "$G checkout main && ls -lf" "$G reset" "$G reset -- $T/x.md" "$G reset HEAD $T/x.md"
    "$G branch -d merged-branch" "$G -C /r status" "$H pr view 12" "$H pr list --state all"
    "$H api repos/o/r/git/refs/heads/main" "$G mv \"$T/a.md\" \"$T/b.md\""
    "sed -n 5p \"$T/x.md\"" "grep -rn x \"$T\" | tee /tmp/out.txt" "cat \"$T/x.md\" > /tmp/x.md"
    "python3 tools/media_manifest.py build" "python3 -c \"print(open('$T/x.md').read()[:10])\""
    "python3 tools/test_media_manifest.py --pin-visible \"CF-01: x\""
  )
  must_ask=(
    "$G push origin main" "$G push -u origin HEAD" "$G -C /r push origin main"
    "$G push -u origin HEAD && tail -f ci.log" "$H pr merge 1 --merge --delete-branch"
    "$H pr close 3 --delete-branch" "$H api -X DELETE repos/o/r/issues/1/labels/x"
  )
  for c in "${must_block[@]}"; do
    r=$(verdict "$c"); rc=$?
    if (( rc == 0 )); then printf 'BLOCK ok   %-45s (%s)\n' "$c" "$r"
    else printf 'MISS  FAIL %s (rc=%s)\n' "$c" "$rc"; fail=1; fi
  done
  for c in "${must_pass[@]}"; do
    r=$(verdict "$c"); rc=$?
    if (( rc == 1 )); then printf 'PASS  ok   %s\n' "$c"
    else printf 'PASS  FAIL %-45s (rc=%s: %s)\n' "$c" "$rc" "$r"; fail=1; fi
  done
  for c in "${must_ask[@]}"; do
    r=$(verdict "$c"); rc=$?
    if (( rc == 2 )); then printf 'ASK   ok   %-45s (%s)\n' "$c" "$r"
    else printf 'ASK   FAIL %-45s (rc=%s: %s)\n' "$c" "$rc" "$r"; fail=1; fi
  done
  echo "--- ${#must_block[@]} must-block, ${#must_pass[@]} must-pass, ${#must_ask[@]} must-ask ---"
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

reason=$(verdict "$command_text"); rc=$?
if (( rc == 0 )); then
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
if (( rc == 2 )); then
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"%s"}}\n' "$reason"
fi
exit 0
