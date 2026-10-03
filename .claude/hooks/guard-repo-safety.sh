#!/usr/bin/env bash
# PreToolUse guard (Bash and Monitor): blocks destructive git, gh and filesystem
# operations and Bash edits of course content or governance files.
#
# This repository regularly carries UNPUSHED user commits and hand-edited course
# content. A single hard reset or forced clean destroys work that has no other copy.
# CLAUDE.md asks Claude not to run these; this hook enforces it.
#
# Contract: reads the PreToolUse JSON on stdin (command, cwd). Exit 2 + stderr = block;
# exit 0 = pass. The hook never answers "ask": a hook ask is not guaranteed to prompt in
# every permission mode, an explicit settings ask rule is. So publishing commands
# (`git push`, `gh pr merge`, `gh pr close`) PASS here only in their plain, standalone
# spelling, which the settings ask rules match; every other spelling (compound command,
# `git -c … push`, `bash -c "git push"`, `/usr/bin/git push`, `gh pr --repo x merge`) is
# BLOCKED with a "rewrite it plainly" message, so it cannot slip past the prompt.
#
# Matching is FLAG-SPELLING AGNOSTIC: short clusters (-fd), long forms and git's
# unambiguous long-option prefixes (--har, --forc, --amen) are all caught. A rule that
# checks one spelling is the same failure class as an assert that checks one literal
# sentence — which is how this repository once produced a false "0 regressions" report.
#
# Matching is PER INVOCATION: the text is split at shell separators and newlines and at
# every git/gh token; quoted or path-qualified git (`"git"`, `/usr/bin/git`,
# `$(which git)`) is normalised, git global options are dropped, and flags are read only
# after the subcommand. Course-content guard: Bash may not write into `02 Tervezet/`,
# `.claude/`, `.github/` or `CLAUDE.md` (sed/perl/awk in place, tee, redirects, cp/mv/
# install/rsync/ln, patch/git apply, inline scripts writing there, `cd` into the folder
# then editing). Known residual: a script FILE (`python3 fix.py`) or variable
# indirection cannot be read here — CLAUDE.md forbids them all the same.
#
# A command that merely MENTIONS a dangerous invocation (a commit message quoting one)
# can be blocked; use `git commit -F <file>` or the Write tool for such text.
#
# Second layer: .claude/settings.json (deny / ask). Keep the two in sync. Deny rules
# cannot carry exceptions, so `git rebase --abort` stays allowed only here.
# Written for bash 3.2 (macOS /usr/bin/env bash). Self-test:
#   bash .claude/hooks/guard-repo-safety.sh --selftest
set -uo pipefail
set -f   # never glob: command text is split into words below

REPO_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." 2>/dev/null && pwd)
REPO_BASE=${REPO_ROOT##*/}

PROT='(02(\\)?[[:space:]]Tervezet|01(\\)?[[:space:]]Fejlesztés|\.git|\.github|\.claude|tools|CLAUDE\.md|README\.md|\.gitignore|\.gitattributes)'
REL_RE="(^|[[:space:]\"'=])(\\./)?${PROT}([/[:space:]\"']|\$)"
TOP_RE="(^|[[:space:]\"'])(\\./)?${PROT}/?([[:space:]\"']|\$)"
RM_RE="(^|[[:space:]\"'(])(/bin/|/usr/bin/|\\\\)?(rm|unlink|shred|trash)[[:space:]]"
# Files edited only through the Edit/Write tools: course content and governance.
CONTENT_RE='02(\\)?[[:space:]]Tervezet'
GUARD_RE="(02(\\\\)?[[:space:]]Tervezet|(^|[[:space:]\"'=])(\\./)?(\\.claude/|\\.github/|CLAUDE\\.md))"
REDIR_RE="(^|[^->=])>[>|]?[[:space:]]*[\"']?"
SED_I_RE='(^|[[:space:]])(sed|gsed)[[:space:]]([^|]*[[:space:]])?(-[a-zA-Z]*i|--in-place)'
PERL_I_RE='(^|[[:space:]])perl[[:space:]]([^|]*[[:space:]])?-[a-zA-Z0-9]*i'
AWK_I_RE='(^|[[:space:]])g?awk[[:space:]]([^|]*[[:space:]])?-i[[:space:]]*inplace'
COPY_RE='(^|[[:space:]])(cp|mv|install|rsync|ln|ditto)[[:space:]]'
INTERP_RE='(^|[[:space:]])(python3?|node|ruby|perl)[[:space:]]'
TRIG_RE='(^|[^[:alnum:]_-])(git|gh|rm|unlink|shred|trash|find|mv|cp|install|rsync|ln|ditto|sed|gsed|perl|awk|gawk|tee|xargs|patch|python3?|node|ruby|cd|rmtree|unlinkSync|rmSync)([^[:alnum:]_]|$)|>'
SEP_RE=$'[;&|`\n]'
SCRIPT_G='(02(\\)?[[:space:]]Tervezet|(^|[^/~[:alnum:]])\.claude/|(^|[^/~[:alnum:]])\.github/|(^|[^/[:alnum:]])CLAUDE\.md)'
OPT_VAL_RE="^git[[:space:]]+(-C|-c)[[:space:]]+(\"[^\"]*\"|'[^']*'|[^[:space:]]+)(.*)\$"
OPT_FLAG_RE='^git[[:space:]]+(--git-dir=|--work-tree=|--namespace=|--exec-path=|--no-pager|-P|--no-replace-objects|--literal-pathspecs|--no-optional-locks|--paginate|-p)([^[:space:]]*)(.*)$'
SPLIT_RE='^(.*[^[:alnum:]_./-])((git|gh)[[:space:]].*)$'
PLAIN_PUSH_RE='^git[[:space:]]+(-C[[:space:]]+[^[:space:];&|]+[[:space:]]+)?push([[:space:]]|$)'
PLAIN_GHPR_RE='^gh[[:space:]]+pr[[:space:]]+(merge|close)([[:space:]]|$)'

CWD=$REPO_ROOT; IN_REPO=1; CWD_CONTENT=0; CD_CONTENT=0; CD_REPO=0

# has_flag <text> <short-letter> <long-name> [min-prefix-length]: a short cluster with the
# letter, the long form, or an unambiguous prefix of it (git accepts --har for --hard).
has_flag() {
  local t=$1 s=$2 long=$3 min=${4:-0} i
  [[ $t =~ [[:space:]]-[a-zA-Z]*$s[a-zA-Z]*([[:space:]]|$) ]] && return 0
  [[ $t =~ [[:space:]]--$long([[:space:]=]|$) ]] && return 0
  if (( min > 0 )); then
    for (( i = min; i < ${#long}; i++ )); do
      [[ $t =~ [[:space:]]--${long:0:i}([[:space:]=]|$) ]] && return 0
    done
  fi
  return 1
}
# has_long <text> <long-name> <min-prefix-length>: long option or an unambiguous prefix.
has_long() { has_flag "$1" '#' "$2" "$3"; }

# Normalise every spelling of the git/gh binary to a bare token.
norm_bins() {
  local s=$1 r
  while [[ $s =~ ^(.*[[:space:]\"\'\;\&\|\(\`])?[^[:space:]\"\'\;\&\|\(\`]*/bin/(git|gh)([[:space:]].*)$ ]]; do
    s="${BASH_REMATCH[1]-}${BASH_REMATCH[2]}${BASH_REMATCH[3]}"
  done
  s=${s//\$(which git)/git}; s=${s//\`which git\`/git}; s=${s//\\git /git }
  s=${s//\"git\"/git}; s=${s//\'git\'/git}; s=${s//\"gh\"/gh}; s=${s//\'gh\'/gh}
  printf '%s' "$s"
}

# One invocation per line: split at separators and newlines, then before every git/gh
# token. Lines without any trigger token are dropped early (long heredocs stay fast).
split_pieces() {
  local s=$1 line out=""
  s=${s//>|/>}
  s=${s//&&/$'\n'}; s=${s//||/$'\n'}
  s=${s//;/$'\n'}; s=${s//&/$'\n'}; s=${s//|/$'\n'}
  while IFS= read -r line; do
    [[ $line =~ $TRIG_RE ]] || continue
    while [[ $line =~ $SPLIT_RE ]]; do
      out+="${BASH_REMATCH[2]}"$'\n'
      line=${BASH_REMATCH[1]}
    done
    out+="$line"$'\n'
  done <<< "$s"
  printf '%s' "$out"
}

norm_git() {
  local p=$1
  while [[ $p =~ $OPT_VAL_RE ]] || [[ $p =~ $OPT_FLAG_RE ]]; do
    p="git${BASH_REMATCH[3]}"
  done
  printf '%s' "$p"
}

# Rewrite repository-absolute, home-relative and sibling-relative paths to repo-relative.
relpaths() {
  local q=$1
  q=${q//\~\//$HOME/}
  if [[ -n $REPO_ROOT ]]; then
    q=${q//"$REPO_ROOT"\// }; q=${q//"$REPO_ROOT"/ . }
  fi
  while [[ $q =~ ^(.*)[^[:space:]\"\']*/$REPO_BASE/(.*)$ ]]; do q="${BASH_REMATCH[1]} ${BASH_REMATCH[2]}"; done
  printf '%s' "$q"
}

names_repo_path() { local q; q=$(relpaths "$1"); [[ $q =~ $REL_RE ]]; }
names_guarded() { local q; q=$(relpaths "$1"); [[ $q =~ $GUARD_RE ]]; }

# Positional words after the subcommand; quoted strings count once; redirects dropped.
positionals() {
  local t=$1 w out="" a b inner
  while [[ $t =~ ^(.*)[\"\']([^\"\']*)[\"\'](.*)$ ]]; do
    a=${BASH_REMATCH[1]}; inner=${BASH_REMATCH[2]}; b=${BASH_REMATCH[3]}
    inner=${inner#"${inner%%[![:space:]]*}"}; inner=${inner%"${inner##*[![:space:]]}"}
    t="$a ${inner//[[:space:]]/_} $b"
  done
  t=${t//\\ /_}
  while [[ $t =~ ^(.*)[[:space:]][0-9]*[\>\<]+\&?[[:space:]]*[^[:space:]]*(.*)$ ]]; do t="${BASH_REMATCH[1]}${BASH_REMATCH[2]}"; done
  for w in $t; do [[ $w == -* ]] || out+="$w "; done
  printf '%s' "$out"
}

# The last word of a piece (the destination of cp/mv/install/rsync/ln).
last_word() {
  local t=$1
  t=${t%"${t##*[![:space:]]}"}
  if [[ $t =~ \"([^\"]*)\"$ ]] || [[ $t =~ \'([^\']*)\'$ ]] || [[ $t =~ ((\\[[:space:]]|[^[:space:]])+)$ ]]; then
    printf '%s' "${BASH_REMATCH[1]}"
  fi
}

is_relative() { [[ ! $1 =~ ^[\"\']?[/~] ]]; }

# Echoes a reason. Returns 0 = block, 3 = publishing command (plain spelling decides), 1 = pass.
check_piece() {
  local p=$1 q sub rest up dest w staged=0 worktree=0
  p=${p#"${p%%[![:space:]]*}"}
  q=" $p "

  # --- writes into content/governance, any program -------------------------------
  if [[ $q =~ $REDIR_RE ]]; then
    local pre=${q%%"${BASH_REMATCH[0]}"*} tgt tw=""
    tgt=${q:$(( ${#pre} + 1 ))}
    if [[ $tgt =~ ^\>[\>\|]?[[:space:]]*\"([^\"]*)\" ]] || [[ $tgt =~ ^\>[\>\|]?[[:space:]]*\'([^\']*)\' ]] || [[ $tgt =~ ^\>[\>\|]?[[:space:]]*((\\[[:space:]]|[^[:space:]])+) ]]; then
      tw=${BASH_REMATCH[1]}
    fi
    if [[ -n $tw ]] && { names_guarded " $tw" || { (( CD_CONTENT || CWD_CONTENT )) && is_relative "$tw"; }; }; then
      echo "Bash-átirányítás a tananyagba vagy governance-fájlba — használd az Edit/Write eszközt"; return 0
    fi
  fi

  if [[ ! $p =~ ^(git|gh)[[:space:]] ]]; then
    if [[ $p =~ ^cd[[:space:]]+(.*)$ ]]; then
      w=${BASH_REMATCH[1]}
      if names_guarded " $w"; then CD_CONTENT=1; fi
      if names_repo_path " $w" || [[ $(relpaths " $w") =~ ^[[:space:]]*\.?[[:space:]]*$ ]]; then CD_REPO=1; fi
      return 1
    fi
    if [[ $q =~ $SED_I_RE ]] || [[ $q =~ $PERL_I_RE ]] || [[ $q =~ $AWK_I_RE ]]; then
      if names_guarded "$q" || (( CD_CONTENT || CWD_CONTENT )) || { [[ $q =~ (^|[[:space:]])(xargs|-exec)[[:space:]] ]] && (( CONTENT_CTX )); }; then
        echo "helyben szerkesztés (sed/perl/awk) a tananyagon — használd az Edit eszközt"; return 0
      fi
    fi
    if [[ $q =~ (^|[[:space:]])tee[[:space:]] ]]; then
      if names_guarded "$q" || (( CD_CONTENT || CWD_CONTENT )); then
        echo "tee a tananyagba vagy governance-fájlba — használd a Write eszközt"; return 0
      fi
    fi
    if [[ $q =~ $COPY_RE ]]; then
      dest=$(last_word "$p")
      if names_guarded " $dest" || { [[ $q =~ [[:space:]](-t|--target-directory)[[:space:]=] ]] && names_guarded "$q"; } \
         || { (( CD_CONTENT || CWD_CONTENT )) && is_relative "$dest"; }; then
        echo "másolás/áthelyezés a tananyagba vagy governance-fájlba — használd az Edit/Write eszközt"; return 0
      fi
    fi
    if [[ $q =~ (^|[[:space:]])patch[[:space:]] ]] && (( IN_REPO || CD_REPO )); then
      echo "patch-alkalmazás a repóban — a tananyag csak Edit/Write eszközzel változhat"; return 0
    fi
    if [[ $q =~ $RM_RE ]]; then
      names_repo_path "$q" && { echo "a repository tartalmának törlése"; return 0; }
      if has_flag "$q" r recursive && [[ $(relpaths "$q") =~ [[:space:]](\.|\.\.|/|\*|\./\*|~|\$\(pwd\)|\$PWD|\`pwd\`)/?[[:space:]] ]]; then
        echo "rekurzív törlés a munkakönyvtárra"; return 0
      fi
      if has_flag "$q" r recursive && (( CD_REPO || CD_CONTENT )); then
        echo "rekurzív törlés a repóban (cd után)"; return 0
      fi
    fi
    if [[ $q =~ (^|[[:space:]])find[[:space:]] ]] && [[ $q =~ (-delete|-exec[[:space:]]+(/bin/)?rm) ]]; then
      if names_repo_path "$q" || { (( IN_REPO || CD_REPO )) && [[ $q =~ find[[:space:]]+(\.|\./[^[:space:]]*|[\"\']\.)[[:space:]] ]]; }; then
        echo "find -delete a repository tartalmán"; return 0
      fi
    fi
    if [[ $q =~ (^|[[:space:]])mv[[:space:]] ]]; then
      [[ $(relpaths "$q") =~ $TOP_RE ]] && { echo "a repository egy fő mappájának vagy fájljának elmozdítása"; return 0; }
    fi
    if [[ $q =~ (rmtree|os\.remove|os\.unlink|os\.rmdir|unlinkSync|rmSync|fs\.rm|shutil\.move) ]] && names_repo_path "$q"; then
      echo "programból indított törlés a repository tartalmán"; return 0
    fi
    return 1
  fi

  # --- gh ---------------------------------------------------------------------------
  if [[ $p =~ ^gh[[:space:]] ]]; then
    while [[ $p =~ ^gh[[:space:]]+(.*)[[:space:]](-R|--repo)[[:space:]=]+[^[:space:]]+(.*)$ ]]; do p="gh ${BASH_REMATCH[1]}${BASH_REMATCH[3]}"; done
    while [[ $p =~ ^gh[[:space:]]+(-R|--repo)[[:space:]=]+[^[:space:]]+(.*)$ ]]; do p="gh${BASH_REMATCH[2]}"; done
    up=$(printf '%s' "$p" | tr '[:lower:]' '[:upper:]')
    [[ $p =~ ^gh[[:space:]]+repo[[:space:]]+(delete|sync|archive|rename) ]] && { echo "gh repo ${BASH_REMATCH[1]}: távoli repó módosítása — csak a felhasználó futtatja"; return 0; }
    [[ $p =~ ^gh[[:space:]]+release[[:space:]]+delete ]] && { echo "gh release delete visszavonhatatlan"; return 0; }
    [[ $p =~ ^gh[[:space:]]+repo[[:space:]]+edit ]] && [[ $p =~ --visibility ]] && { echo "a repository láthatóságának átállítása"; return 0; }
    if [[ $p =~ ^gh[[:space:]]+api[[:space:]] ]]; then
      if [[ $up =~ (-X|--METHOD)[[:space:]=]*([A-Z]+) ]]; then
        local method=${BASH_REMATCH[2]}
        if [[ ! $method =~ ^(GET|HEAD)$ ]]; then echo "gh api írás ($method) — csak a felhasználó futtatja"; return 0; fi
      fi
      if [[ ! $up =~ (-X|--METHOD)[[:space:]=]*(GET|HEAD) ]] && [[ $q =~ [[:space:]](-f|-F|--field|--raw-field|--input)[[:space:]=] ]] && [[ ! $p =~ [[:space:]]graphql([[:space:]]|$) ]]; then
        echo "gh api mezőkkel = implicit POST (írás) — csak a felhasználó futtatja"; return 0
      fi
      [[ $p =~ [[:space:]]graphql([[:space:]]|$) ]] && [[ $up =~ MUTATION ]] && { echo "gh api graphql mutation (írás) — csak a felhasználó futtatja"; return 0; }
      return 1
    fi
    [[ $p =~ ^gh[[:space:]]+pr[[:space:]]+(merge|close) ]] && { echo "gh pr ${BASH_REMATCH[1]}"; return 3; }
    return 1
  fi

  # --- git --------------------------------------------------------------------------
  [[ $p =~ -c[[:space:]]+[\"\']?alias\. ]] && { echo "git -c alias.*: egy alias bármit elrejthet — futtasd a parancsot közvetlenül"; return 0; }
  local raw=$p
  p=$(norm_git "$p")
  p=${p/#git \"/git }; p=${p/#git \'/git }
  [[ $p =~ ^git[[:space:]]+([a-z][a-z0-9-]*)[\"\']?(.*)$ ]] || return 1
  sub=${BASH_REMATCH[1]}; rest=" ${BASH_REMATCH[2]} "
  rest=${rest//\"/ \" }; rest=${rest//\'/ \' }; rest=${rest//\`/ \` }; rest=${rest//)/ ) }

  case $sub in
    reset)
      if has_long "$rest" hard 2 || has_long "$rest" merge 2 || has_long "$rest" keep 1; then
        echo "a hard/merge/keep reset eldobja a nem commitolt munkát"; return 0
      fi
      if [[ ! $rest =~ [[:space:]]--[[:space:]] ]] && \
         [[ $rest =~ [[:space:]](HEAD[~^][^[:space:]]*|@[~^{][^[:space:]]*|ORIG_HEAD|FETCH_HEAD|origin/[^[:space:]]+|main|master|[0-9a-f]{7,40})([[:space:]]|$) ]]; then
        echo "a reset <commit> átállítja a branchet (--soft/--mixed alakban is history rewrite)"; return 0
      fi ;;
    clean)
      has_flag "$rest" f force 1 && { echo "a kényszerített clean visszavonhatatlanul törli a nem követett fájlokat"; return 0; }
      if [[ $raw =~ clean\.requireForce[[:space:]]*=[[:space:]]*false ]] && ! has_flag "$rest" n dry-run 1 && ! has_flag "$rest" i interactive 1; then
        echo "clean.requireForce=false mellett a clean -f nélkül is töröl"; return 0
      fi ;;
    checkout)
      [[ $rest =~ [[:space:]]--[[:space:]] ]] && { echo "checkout -- <path> eldobja a working tree változtatásait"; return 0; }
      has_flag "$rest" f force 1 && { echo "a kényszerített checkout eldobja a working tree változtatásait"; return 0; }
      [[ $rest =~ [[:space:]]-B[[:space:]] ]] && { echo "checkout -B felülír egy meglévő branch-et"; return 0; }
      has_long "$rest" theirs 2 && { echo "checkout --theirs <path> felülírja a fájlt"; return 0; }
      has_long "$rest" ours 2 && { echo "checkout --ours <path> felülírja a fájlt"; return 0; }
      if [[ ! $rest =~ [[:space:]](-b|--orphan|-t|--track)[[:space:]] ]]; then
        local pos n=0
        pos=$(positionals "$rest")
        for w in $pos; do
          n=$((n + 1))
          if [[ $w == . || $w == ./ || $w == :/ || $w == *[\*\?\[]* ]] || [[ -e "$CWD/${w//_/ }" && ! -d "$CWD/.git/refs/heads/${w//_/ }" ]] || [[ $w == */* && -e "$REPO_ROOT/${w//_/ }" ]]; then
            echo "checkout <path> felülírja a fájlt a working tree-ben"; return 0
          fi
        done
        (( n >= 2 )) && { echo "checkout <commit> <path> felülírja a fájlt a working tree-ben"; return 0; }
      fi ;;
    switch)
      has_flag "$rest" f force 1 && { echo "a kényszerített switch eldobja a working tree változtatásait"; return 0; }
      [[ $rest =~ [[:space:]]-C[[:space:]] ]] && { echo "switch -C felülír egy meglévő branch-et"; return 0; }
      has_long "$rest" discard-changes 2 && { echo "a switch --discard-changes eldobja a working tree változtatásait"; return 0; }
      ;;
    restore)
      if has_long "$rest" staged 2 || [[ $rest =~ [[:space:]]-[a-zA-Z]*S[a-zA-Z]*([[:space:]]|$) ]]; then staged=1; fi
      if has_long "$rest" worktree 1 || [[ $rest =~ [[:space:]]-[a-zA-Z]*W[a-zA-Z]*([[:space:]]|$) ]]; then worktree=1; fi
      if (( ! staged || worktree )); then echo "a restore eldobja a working tree változtatásait (csak --staged engedett)"; return 0; fi ;;
    checkout-index)
      if has_flag "$rest" f force 1 || has_flag "$rest" a all 1; then echo "checkout-index -f/-a felülírja a working tree fájljait"; return 0; fi ;;
    push)
      if has_flag "$rest" f force 2 || has_long "$rest" force-with-lease 7 || has_long "$rest" force-if-includes 7 || \
         has_flag "$rest" d delete 2 || has_long "$rest" mirror 1 || has_long "$rest" prune 3 || \
         [[ $rest =~ [[:space:]][+:][^[:space:]] ]]; then
        echo "a kényszerített vagy törlő push átírja a távoli historyt"; return 0
      fi
      echo "git push"; return 3 ;;
    pull)
      if has_long "$rest" rebase 3 && [[ ! $rest =~ --rebase=(false|no) ]] || [[ $rest =~ [[:space:]]-[a-zA-Z]*r[a-zA-Z]*([[:space:]]|$) ]] || \
         [[ $raw =~ -c[[:space:]]+pull\.rebase[[:space:]]*=[[:space:]]*(true|merges|interactive|i|m) ]]; then
        echo "a pull --rebase átírja a lokális historyt"; return 0
      fi ;;
    rebase)
      [[ $rest =~ ^[[:space:]]*--abort[[:space:]\"\'\`\)]*$ ]] || { echo "a rebase átírja a lokális historyt (a repo szabálya tiltja)"; return 0; } ;;
    commit)
      has_long "$rest" amend 2 && { echo "az amend felülírja a felhasználó checkpoint-commitját"; return 0; } ;;
    filter-branch|filter-repo) echo "history rewrite"; return 0 ;;
    reflog) [[ $rest =~ ^[[:space:]]*(delete|expire) ]] && { echo "a reflog törlése megszünteti az utolsó visszaállítási esélyt"; return 0; } ;;
    update-ref) echo "az update-ref közvetlenül átírja vagy törli a ref-eket"; return 0 ;;
    prune) echo "a prune végleg törli az elérhetetlen objektumokat"; return 0 ;;
    gc) has_long "$rest" prune 1 && { echo "a prune végleg törli az elérhetetlen objektumokat"; return 0; } ;;
    stash) [[ $rest =~ ^[[:space:]]*(drop|clear) ]] && { echo "a stash törlése végleges"; return 0; } ;;
    branch)
      [[ $rest =~ [[:space:]]-(D|M|C)[[:space:]] ]] && { echo "branch kényszerített törlése/átnevezése/másolása pusholatlan commitokat veszíthet"; return 0; }
      has_flag "$rest" f force 2 && { echo "a kényszerített branch felülír egy meglévő branch-et"; return 0; } ;;
    worktree) [[ $rest =~ ^[[:space:]]*remove ]] && has_flag "$rest" f force 1 && { echo "worktree kényszerített eltávolítása eldobja a benne lévő munkát"; return 0; } ;;
    apply|am)
      [[ $sub == apply && $rest =~ [[:space:]]--(check|stat|numstat|summary)([[:space:]]|$) ]] && return 1
      echo "git $sub: patch-alkalmazás — a tananyag csak Edit/Write eszközzel változhat"; return 0 ;;
    rm)
      [[ $rest =~ [[:space:]]--cached([[:space:]]|$) ]] && return 1
      local rpos; rpos=" $(positionals "$rest")"
      [[ $rpos =~ [[:space:]](\.|\./|\*|:/)[[:space:]] ]] && { echo "git rm . — a teljes munkakönyvtár törlése"; return 0; }
      names_repo_path "$rest" && { echo "a repository tartalmának törlése"; return 0; } ;;
  esac
  return 1
}

# Echoes a reason. Returns 0 = block, 1 = pass. Publishing commands pass only in their
# plain standalone spelling (the settings ask rule then prompts in every mode).
verdict() {
  local text cwd piece r rc pub="" npieces=0 trimmed
  text=$(norm_bins "$1"); cwd=${2:-$REPO_ROOT}
  CWD=$cwd; IN_REPO=0; CWD_CONTENT=0; CD_CONTENT=0; CD_REPO=0; CONTENT_CTX=0
  [[ $cwd == "$REPO_ROOT" || $cwd == "$REPO_ROOT"/* ]] && IN_REPO=1
  [[ $cwd == "$REPO_ROOT/02 Tervezet" || $cwd == "$REPO_ROOT/02 Tervezet"/* ]] && CWD_CONTENT=1
  [[ $text =~ $CONTENT_RE ]] && CONTENT_CTX=1
  # Inline scripts span separators, so check them whole: a write whose target is a
  # content/governance path, or a write to a bare variable in a script naming one.
  if [[ $text =~ $INTERP_RE ]]; then
    local G=$SCRIPT_G st
    st=$(relpaths "$text")
    if [[ $st =~ open\([^\)]*${G}[^\)]*,[[:space:]]*(mode[[:space:]]*=[[:space:]]*)?[\"\'][wax] ]] || \
       [[ $st =~ Path\([^\)]*${G}[^\)]*\)\.(write_text|write_bytes|open\([\"\'][wax]) ]] || \
       [[ $st =~ (writeFileSync|appendFileSync|writeFile|appendFile|copyFileSync)\([^\)]*${G} ]] || \
       [[ $st =~ shutil\.(copy|copy2|copyfile|move|copytree)\([^\)]*,[[:space:]]*[^\)]*${G} ]] || \
       { [[ $st =~ $G ]] && [[ $st =~ open\([[:alpha:]_][[:alnum:]_.]*[[:space:]]*,[[:space:]]*(mode[[:space:]]*=[[:space:]]*)?[\"\'][wax] ]]; } || \
       { [[ $st =~ $G ]] && [[ $st =~ [[:alpha:]_][[:alnum:]_]*\.(write_text|write_bytes)\( ]]; }; then
      echo "szkriptből írás a tananyagba vagy governance-fájlba — használd az Edit/Write eszközt"; return 0
    fi
  fi
  while IFS= read -r piece; do
    [[ -z ${piece//[[:space:]]/} ]] && continue
    npieces=$((npieces + 1))
    r=$(check_piece "$piece"; echo "|$?|$CD_CONTENT|$CD_REPO")
    rc=${r##*|}; rc=${r%|*|*}; rc=${rc##*|}
    local tail=${r#*|*|}; CD_CONTENT=${tail%%|*}; CD_REPO=${tail##*|}
    r=${r%%|*}
    (( rc == 0 )) && { echo "$r"; return 0; }
    (( rc == 3 )) && [[ -z $pub ]] && pub=$r
  done <<< "$(split_pieces "$text")"
  if [[ -n $pub ]]; then
    trimmed=${1#"${1%%[![:space:]]*}"}
    if (( npieces == 1 )) && { [[ $trimmed =~ $PLAIN_PUSH_RE ]] || [[ $trimmed =~ $PLAIN_GHPR_RE ]]; } && [[ ! $trimmed =~ $SEP_RE ]] && [[ ! $trimmed =~ \$\( ]]; then
      return 1
    fi
    echo "$pub csak egyszerű, önálló alakban futhat (pl. \`git push origin <branch>\`, \`gh pr merge <n>\`) — így a jóváhagyó kérdés minden módban megjelenik"; return 0
  fi
  return 1
}

if [[ "${1:-}" == "--selftest" ]]; then
  fail=0
  # Test-only: run a copy of this file against the real tree (never honoured on live calls).
  [[ -n ${GUARD_REPO_ROOT:-} ]] && { REPO_ROOT=$GUARD_REPO_ROOT; REPO_BASE=${REPO_ROOT##*/}; }
  # Corpus assembled from parts so this file's own text does not read as runnable.
  G="git"; R="rm"; H="gh"; T="02 Tervezet"; PT="02 Tervezet/Program terv.md"
  must_block=(
    "$G reset --hard HEAD~1" "$G reset --hard" "$G reset --merge" "$G reset --har" "$G reset --ha HEAD" "$G reset --kee"
    "$G clean -f" "$G clean -fd" "$G clean -fdx" "$G clean -df" "$G clean -xdf"
    "$G clean --force" "$G clean --force -d" "$G clean -d --force" "$G clean --forc -d" "$G clean --f"
    "$G checkout -- ." "$G checkout -- $T/x.md" "$G checkout ." "$G checkout ./" "$G checkout \"$PT\"" "$G checkout --theirs x.md"
    "$G checkout -f" "$G checkout -f main" "$G checkout --force main"
    "$G switch -f main" "$G switch --force main" "$G switch --discard-changes main"
    "$G checkout -B main" "$G switch -C main" "$G checkout-index -f -a"
    "$G restore ." "$G restore $T/x.md" "$G restore --staged --worktree x" "$G restore --staged -W f" "$G restore -SW f"
    "$G push --force" "$G push -f origin main" "$G push origin main -f" "$G push --forc origin main"
    "$G push --force-with-lease origin HEAD" "$G push --mirror" "$G push origin --delete x" "$G push -d origin x"
    "$G push origin :x" "$G push --prune origin" "$G -C /r push --force"
    "$G rebase -i HEAD~3" "$G rebase main" "$G rebase --continue" "$G rebase --skip"
    "$G rebase --onto main HEAD~2" "$G rebase --quit" "$G rebase --aborted"
    "$G rebase --abort && $G rebase -i HEAD~3" "$G commit --amend --no-edit" "$G commit --amen"
    "$G filter-branch --tree-filter x" "$G filter-repo --path x"
    "$G branch -D audit-fixes-2026-08-25" "$G branch --force main HEAD~2" "$G branch -M main"
    "$G stash clear" "$G stash drop" "$G reflog expire --expire=now --all"
    "$G gc --prune=now" "$G update-ref -d refs/heads/x" "$G update-ref --delete refs/heads/x" "$G update-ref refs/heads/main HEAD~3" "$G prune"
    "$G worktree remove --force ../wt" "$G worktree remove -f ../wt"
    "$G reset --soft HEAD~1" "$G reset HEAD~3" "$G reset --keep HEAD~1" "$G reset origin/main"
    "$G checkout HEAD~1 \"$T/x.md\"" "$G -c clean.requireForce=false clean -d"
    "$G pull --rebase" "$G pull -r origin main" "$G -c pull.rebase=true pull"
    "\"$G\" reset --hard" "$G 'reset' --hard" "\$(which $G) reset --hard" "/usr/bin/$G reset --hard" "$G -c alias.x='reset --hard' x"
    "$G rm -rf ." "$G apply /tmp/p.diff" "$G am /tmp/p.mbox"
    "$G status && $G reset --hard" "cd /tmp && $G clean --force -d" "bash -c \"$G reset --hard\"" "cat > f <<EOF $G reset --hard EOF"
    # publishing: only the plain standalone spelling may pass (settings ask prompts)
    "$G push -u origin HEAD && tail -f ci.log" "$G add -A && $G commit -m x && $G push" "$G -c k=v push origin main"
    "$G --no-pager push origin main" "bash -c \"$G push origin main\"" "/usr/bin/$G push origin main"
    "$H pr --repo o/r merge 12" "$H pr view 1 && $H pr merge 1"
    # deletion aimed at the repository
    "$R -rf $T" "$R -r -f $T" "$R -rf ." "$R -fr ." "$R -rf .claude" "$R -rf ./*"
    "$R CLAUDE.md" "$R -f .claude/settings.json" "$R -rf tools/" "$R --recursive --force ." "$R -rf ~"
    "$R -rf 02\\ Tervezet/x" "/bin/$R -rf \"$T\"" "\\$R -rf tools" "find \"$T\" -name x -delete" "find . -name \"*.md\" -delete"
    "cd \"$T\" && $R -rf Modulok" "$R -rf ../$REPO_BASE/02\\ Tervezet" "$R -rf $REPO_ROOT/tools"
    "python3 -c \"import shutil; shutil.rmtree('$T')\"" "mv \"$T\" /tmp/"
    "$H repo delete x --yes" "$H release delete v1" "$H repo sync --force" "$H api -X DELETE repos/o/r/git/refs/heads/x"
    "$H api --method PATCH repos/o/r/git/refs/heads/main -f sha=x" "$H api -X PUT repos/o/r/pulls/12/merge"
    "$H api repos/o/r/merges -f base=main -f head=x" "$H api graphql -f query='mutation{x}'" "$H api -X DELETE repos/o/r/issues/1/labels/x"
    # course content and governance only through Edit/Write
    "sed -i '' 's/a/b/' \"$T/x.md\"" "sed -E -i.bak 's/a/b/' \"$T/x.md\"" "perl -pi -e 's/a/b/' \"$T/x.md\""
    "perl -pe 's/a/b/' -i \"$T/x.md\"" "perl -0777 -pi -e 's/a/b/' \"$T/x.md\"" "awk -i inplace '{print}' \"$T/x.md\""
    "grep -rl x \"$T\" | xargs sed -i '' 's/a/b/'" "find \"$T\" -name \"*.md\" -exec sed -i '' 's/a/b/' {} +"
    "cd \"$T/Modulok\" && sed -i '' 's/a/b/' x.md" "echo x > \"$T/x.md\"" "echo x >> \"$T/Modulok/a.md\"" "echo x >| \"$T/x.md\""
    "cat /tmp/x > \"/Users/u/repo/$T/x.md\"" "printf x | tee \"$T/x.md\"" "cp /tmp/x \"$T/x.md\"" "mv /tmp/x \"$T/Modulok/x.md\""
    "install /tmp/x \"$T/x.md\"" "rsync -a /tmp/x/ \"$T/\"" "$G show HEAD:\"$T/x.md\" > \"$T/x.md\"" "patch -p1 < /tmp/p.diff"
    "python3 - <<EOF p='$T/x.md'; open(p,'w').write('x') EOF" "python3 -c \"import pathlib; pathlib.Path('$T/x.md').write_text('x')\""
    "python3 -c \"open('$T/x.md','wb').write(b'x')\"" "python3 -c \"import shutil; shutil.copy('/tmp/x','$T/x.md')\""
    "node -e \"require('fs').writeFileSync('$T/x.md','x')\"" "echo '{\"disableAllHooks\":true}' > .claude/settings.local.json"
    "cp /tmp/x CLAUDE.md" "sed -i '' 's/a/b/' .github/workflows/content-integrity.yml"
  )
  must_pass=(
    "$G status" "$G status --short" "$G diff" "$G diff --check" "$G diff --stat" "$G diff --check origin/main...HEAD"
    "$G add $T/Modulok/M3/x.md" "$G add -A" "$G add -f $T/x.md" "$G add -N \"$T/x.md\""
    "$G commit -m 'fix: x'" "$G commit -F msg.txt" "$G log -10 --oneline"
    "$G branch --show-current" "$G branch -m old new" "$G branch -a" "$G branch -v" "$G branch -d merged-branch"
    "$G checkout main" "$G checkout -b feature/x" "$G switch main" "$G switch -c feature/x" "$G checkout main 2>&1" "$G checkout main 2>/dev/null"
    "$G restore --staged $T/x.md" "$G restore -S $T/x.md" "$G cherry-pick abc1234" "$G show abc1234:\"$T/x.md\" > /tmp/x.md"
    "$G stash" "$G stash pop" "$G stash list" "$G show HEAD" "$G clean -n" "$G clean -nd"
    "$G worktree list" "$G rev-parse HEAD" "$G reflog" "$G gc" "$G apply --check /tmp/p.diff"
    "$G rebase --abort" "$G merge --abort" "$G cherry-pick --abort" "$G revert --abort" "$G -C /r rebase --abort"
    "$G status && $G rebase --abort" "$G merge main" "$G revert HEAD"
    "$G rebase --abort;" "$G rebase --abort && $G status" "cd /repo && $G rebase --abort"
    "$G rebase --abort; echo done" "$G merge --abort;" "$G cherry-pick --abort && $G status"
    "$G push origin main" "$G push -u origin HEAD" "$G push" "$G -C /r push origin main" "$H pr merge 1 --merge" "$H pr close 3 --delete-branch"
    "python3 tools/content_integrity.py" "python3 tools/content_integrity.py --release-report" "python3 tools/media_manifest.py build"
    "python3 tools/test_media_manifest.py --pin-visible \"CF-01: x\"" "python3 tools/test_media_manifest.py --pin-visible \"CF-01: a -> $T\""
    "grep -rn mintaszo '$T'" "ls -la" "ls -lf" "cat CLAUDE.md" "sed -n 5p \"$T/x.md\"" "grep -rn x \"$T\" | tee /tmp/out.txt"
    "cat \"$T/x.md\" > /tmp/x.md" "cp \"$T/x.md\" /tmp/x.md" "cp -r \"$T/Modulok\" /tmp/backup"
    "python3 -c \"print(open('$T/x.md').read()[:10])\""
    "python3 - <<EOF t=open('$T/x.md').read(); open('/private/tmp/o.json','w').write(t) EOF"
    "$G commit -m \"fix -> $T\"" "$R -rf /private/tmp/claude-501/scratch" "$R /tmp/x.json" "$R -rf /private/tmp/x/scratchpad/tools/"
    "$R ~/.claude/projects/x/memory/a.md" "bash .claude/hooks/guard-repo-safety.sh --selftest" "bash .github/read-only-workflows.sh"
    "$G log -1 && $H repo view --json rebaseMergeAllowed" "$G pull --no-rebase" "$G pull --rebase=false" "$G pull"
    "$G config --get pull.rebase" "$G log --grep=rebase" "$G grep -n \"reset --hard\" CLAUDE.md"
    "$G add \"$T/Modulok/M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md\" && $G commit -m x"
    "$G checkout -b x && $G diff main -- $T/x.md" "$G rm --cached \"$T/x.md\"" "$G checkout main && ls -lf"
    "$G reset" "$G reset -- $T/x.md" "$G reset HEAD $T/x.md" "$G -C /r status" "$H pr view 12" "$H pr list --state all"
    "$H api repos/o/r/git/refs/heads/main" "$H api -X GET search/issues -f q=x" "$H api graphql -f query='query{viewer{login}}'"
    "$G mv \"$T/a.md\" \"$T/b.md\"" "node --test test/x.test.mjs" "$H pr create --title x --body y"
    $'rm -f /private/tmp/x.txt\nbash .github/read-only-workflows.sh'
  )
  for c in "${must_block[@]}"; do
    if r=$(verdict "$c"); then printf 'BLOCK ok   %-45s (%s)\n' "$c" "$r"
    else printf 'MISS  FAIL %s\n' "$c"; fail=1; fi
  done
  for c in "${must_pass[@]}"; do
    if r=$(verdict "$c"); then printf 'PASS  FAIL %-45s (%s)\n' "$c" "$r"; fail=1
    else printf 'PASS  ok   %s\n' "$c"; fi
  done
  echo "--- ${#must_block[@]} must-block, ${#must_pass[@]} must-pass ---"
  [[ $fail -eq 0 ]] && echo "--- selftest OK ---" || echo "--- selftest FAILED ---"
  exit $fail
fi

payload=$(cat)
command_text=""; cwd=""
if command -v jq >/dev/null 2>&1; then
  command_text=$(printf '%s' "$payload" | jq -r '.tool_input.command // .tool_input.cmd // empty' 2>/dev/null)
  cwd=$(printf '%s' "$payload" | jq -r '.cwd // empty' 2>/dev/null)
elif command -v python3 >/dev/null 2>&1; then
  command_text=$(printf '%s' "$payload" | python3 -c \
    'import json,sys; d=json.load(sys.stdin); t=d.get("tool_input",{}); print(t.get("command") or t.get("cmd") or "")' 2>/dev/null)
  cwd=$(printf '%s' "$payload" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("cwd",""))' 2>/dev/null)
else
  # No JSON parser: fail closed by scanning the raw payload rather than waving it through.
  command_text="$payload"
fi
[[ -z "$command_text" ]] && exit 0

if reason=$(verdict "$command_text" "${cwd:-$REPO_ROOT}"); then
  cat >&2 <<MSG
BLOKKOLVA (.claude/hooks/guard-repo-safety.sh): $reason

Parancs (első 400 karakter): ${command_text:0:400}

Ezen a branchen pusholatlan felhasználói commitok és kézzel szerkesztett tananyag van.
Destruktív git- és törlőműveletek, valamint a tananyag/governance Bash-szerkesztése
tiltott — lásd CLAUDE.md "Git-biztonság". Tananyag: Edit/Write eszköz.
Ha ez tényleg kell, a felhasználó futtassa kézzel.
MSG
  exit 2
fi
exit 0
