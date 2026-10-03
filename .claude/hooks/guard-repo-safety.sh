#!/usr/bin/env bash
# PreToolUse guard (Bash and Monitor) for git/gh intent and early, readable feedback.
#
# Layers (see CLAUDE.md "Git-biztonság"): the OS-level SANDBOX (.claude/settings.json) is the
# write boundary — sandboxed Bash cannot write `02 Tervezet/`, `.claude/`, `.github/`,
# `CLAUDE.md` or the visible-text pins, however a command is spelled. git, gh and the build
# run OUTSIDE the sandbox (excludedCommands), so for them THIS hook is the guard. Its content
# rules for other programs are an early warning with a clear message; they cannot be complete.
#
# This repository regularly carries UNPUSHED user commits and hand-edited course content.
# A single hard reset or forced clean destroys work that has no other copy.
#
# Contract: reads the PreToolUse JSON on stdin (command, cwd). Exit 2 + stderr = block;
# exit 0 = pass. The hook never answers "ask": a hook ask does not prompt in every permission
# mode, an explicit settings ask rule does. Publishing commands (`git push` and every gh
# command that writes to GitHub, GH_PUBLISH_RE) pass only in their plain standalone spelling,
# which the settings ask rules catch; every other spelling is blocked. FAIL CLOSED: commands
# over MAX_LEN bytes, and any analysis still running after WATCHDOG seconds, are blocked (a
# hook killed by its own timeout would let the command through). Long text is processed with
# sed/tr/awk single passes; bash 3.2 substitutions and regex loops are quadratic on it.
#
# Matching is FLAG-SPELLING AGNOSTIC (short clusters, long forms, git's unambiguous long-option
# prefixes) and PER INVOCATION (split at separators, newlines and every git/gh token; quoted
# or path-qualified git normalised; global options dropped; flags read after the subcommand).
# A command that merely MENTIONS a dangerous invocation can be blocked; use `git commit -F`
# or the Write tool for such text. `grep`/`rg` lines are not split at git tokens.
#
# Second layer: .claude/settings.json (deny / ask / sandbox). Keep them in sync.
# Written for bash 3.2 (macOS). Self-test:  bash .claude/hooks/guard-repo-safety.sh --selftest
set -uo pipefail
set -f            # never glob: command text is split into words below
export LC_ALL=C   # byte-wise regex: fast on long UTF-8 text; every pattern here is byte-exact

SELF_ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." 2>/dev/null && pwd)
REPO_ROOT=$SELF_ROOT
# A COPY of this file outside the repo (tests) may point at the real tree; the installed hook
# (whose own root contains `02 Tervezet`) never honours the override.
if [[ -n ${GUARD_REPO_ROOT:-} && ! -d "$SELF_ROOT/02 Tervezet" ]]; then REPO_ROOT=$GUARD_REPO_ROOT; fi
REPO_BASE=${REPO_ROOT##*/}
MAX_LEN=100000
WATCHDOG=15
[[ -n ${GUARD_WATCHDOG_SECS:-} && ! -d "$SELF_ROOT/02 Tervezet" ]] && WATCHDOG=$GUARD_WATCHDOG_SECS   # tests only

PROT='(02(\\)?[[:space:]]Tervezet|01(\\)?[[:space:]]Fejlesztés|\.git|\.github|\.claude|tools|CLAUDE\.md|README\.md|\.gitignore|\.gitattributes)'
REL_RE="(^|[[:space:]\"'=])(\\./)?${PROT}([/[:space:]\"']|\$)"
TOP_RE="(^|[[:space:]\"'])(\\./)?${PROT}/?([[:space:]\"']|\$)"
RM_RE="(^|[[:space:]\"'(])(/bin/|/usr/bin/|\\\\)?(rm|unlink|shred|trash)[[:space:]]"
CONTENT_RE='02(\\)?[[:space:]]Tervezet'
GUARD_RE="(02(\\\\)?[[:space:]]Tervezet|(^|[[:space:]\"'=])(\\./)?(\\.claude/|\\.github/|CLAUDE\\.md|tools/approved-visible-text\\.json))"
REDIR_RE="(^|[^->=])>[>|]?[[:space:]]*[\"']?"
REDIR_TGT_RE="(^|[^->=])>[>|]?[[:space:]]*(\"[^\"]*\"|'[^']*'|(\\\\[[:space:]]|[^[:space:]])+)"
SED_I_RE='(^|[[:space:]])(sed|gsed)[[:space:]]([^|]*[[:space:]])?(-[a-zA-Z]*i|--in-place)'
PERL_I_RE='(^|[[:space:]])perl[[:space:]]([^|]*[[:space:]])?-[a-zA-Z0-9]*i'
AWK_I_RE='(^|[[:space:]])g?awk[[:space:]]([^|]*[[:space:]])?-i[[:space:]]*inplace'
COPY_RE='(^|[[:space:]])(cp|mv|install|rsync|ln|ditto)[[:space:]]'
WVERB_RE='(^|[[:space:]])(dd|truncate|tar|unzip|curl|wget|sponge|ex|ed|vi|vim|nvim|split|csplit|touch|mkdir)[[:space:]]'
EDITOR_RE='(^|[[:space:]])(sponge|ex|ed|vi|vim|nvim)[[:space:]]'
INTERP_RE='(^|[[:space:]])(python3?|node|ruby|perl)[[:space:]]'
TRIG_RE='(^|[^[:alnum:]_-])(git|gh|rm|unlink|shred|trash|find|mv|cp|install|rsync|ln|ditto|sed|gsed|perl|awk|gawk|tee|xargs|patch|python3?|node|ruby|cd|pushd|dd|truncate|tar|unzip|curl|wget|sponge|ex|ed|vi|vim|touch|mkdir|rmtree|unlinkSync|rmSync)([^[:alnum:]_]|$)|>'
READONLY_LINE_RE='^[[:space:]({]*(grep|egrep|fgrep|rg|ag|ack)[[:space:]]'
CD_RE="(^|[[:space:]\"'(\`{])(cd|pushd)[[:space:]]+(.*)\$"
SEP_RE=$'[;&|`\n]'
SCRIPT_G='(02(\\)?[[:space:]]Tervezet|(^|[^/~[:alnum:]])\.claude/|(^|[^/~[:alnum:]])\.github/|(^|[^/[:alnum:]])CLAUDE\.md|tools/approved-visible-text\.json)'
OPT_VAL_RE="^git[[:space:]]+(-C|-c|--git-dir|--work-tree|--namespace|--config-env|--super-prefix|--exec-path)[[:space:]]+(\"[^\"]*\"|'[^']*'|[^[:space:]]+)(.*)\$"
OPT_FLAG_RE='^git[[:space:]]+(--git-dir=|--work-tree=|--namespace=|--exec-path=|--config-env=|--super-prefix=|--no-pager|-P|--paginate|-p|--bare|--no-replace-objects|--literal-pathspecs|--glob-pathspecs|--noglob-pathspecs|--icase-pathspecs|--no-optional-locks|--no-lazy-fetch|--no-advice)([^[:space:]]*)(.*)$'
PLAIN_PUSH_RE='^git[[:space:]]+(-C[[:space:]]+[^[:space:];&|]+[[:space:]]+)?push([[:space:]]|$)'
# Everything gh does on GitHub other than reading: plain spelling + a settings ask rule.
GH_PUBLISH_RE='^gh[[:space:]]+(pr[[:space:]]+(merge|close|create|edit|comment|review|reopen|ready|lock|unlock)|issue[[:space:]]+(create|edit|comment|close|reopen|transfer|lock|unlock|pin|unpin|develop)|release[[:space:]]+(create|edit|upload|delete-asset)|workflow[[:space:]]+(run|enable|disable)|run[[:space:]]+(cancel|rerun)|(secret|variable)[[:space:]]+(set|delete|remove)|label[[:space:]]+(create|edit|delete|clone)|gist[[:space:]]+(create|edit|delete)|repo[[:space:]]+(create|fork|edit|set-default))([[:space:]]|$)'
PLAIN_GHPR_RE=$GH_PUBLISH_RE
US=$'\x1f'   # placeholder for spaces inside quoted words (never part of a real path)

CWD=$REPO_ROOT; IN_REPO=1; CWD_CONTENT=0; CD_CONTENT=0; CD_REPO=0; CONTENT_CTX=0

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
has_long() { has_flag "$1" '#' "$2" "$3"; }

# Normalise every spelling of the git/gh binary to a bare token.
norm_bins() {
  local s=$1
  if [[ $s == */bin/git* || $s == */bin/gh* ]]; then
    s=$(printf '%s\n' "$s" | sed -E "s#[^[:space:]\"';&|(\`]*/bin/(git|gh)([[:space:]]|\$)#\\1\\2#g")
  fi
  # Shell-quoting tricks that leave the word unchanged for bash: empty quotes (re''set) and a
  # backslash before a letter (g\it). Matching only; the command itself is never rewritten.
  if [[ $s == *\'\'* || $s == *\"\"* || $s == *\\[[:alpha:]]* ]]; then
    s=$(printf '%s\n' "$s" | sed -E -e "s/''//g" -e 's/""//g' -e 's/\\([A-Za-z])/\1/g')
  fi
  s=${s//\$(which git)/git}; s=${s//\$(command -v git)/git}; s=${s//\`which git\`/git}; s=${s//\`command -v git\`/git}
  s=${s//\$(which gh)/gh}; s=${s//\$(command -v gh)/gh}
  s=${s//\"git\"/git}; s=${s//\'git\'/git}; s=${s//\"gh\"/gh}; s=${s//\'gh\'/gh}
  printf '%s' "$s"
}

# One invocation per line: join backslash-newline continuations, split at separators and
# newlines, then before every git/gh token (not inside grep/rg lines). Lines without any
# trigger token are dropped early.
split_pieces() {
  # sed/tr/awk, not ${s//x/y} or regex loops: bash 3.2 is quadratic on long text.
  printf '%s\n' "$1" | sed -e ':a' -e '/\\$/{' -e 'N' -e 's/\\\n/ /' -e 'ba' -e '}' | sed -e 's/>|/>/g' | tr ';&|' '\n\n\n' |
    awk -v trig="$TRIG_RE" -v ro="$READONLY_LINE_RE" '
      $0 !~ trig { next }
      {
        line = $0
        if (line !~ ro) {
          while (match(line, "[^[:alnum:]_./-](git|gh)[[:space:]]")) {
            print substr(line, 1, RSTART); line = substr(line, RSTART + 1)
          }
        }
        print line
      }'
}

norm_git() {
  NG=$1
  while [[ $NG =~ $OPT_VAL_RE ]] || [[ $NG =~ $OPT_FLAG_RE ]]; do
    NG="git${BASH_REMATCH[3]}"
  done
}

# Rewrite repository-absolute, $PWD-, home- and sibling-relative paths to repo-relative.
relpaths() {
  local q=$1
  if (( ${#q} > 2000 )); then
    printf '%s\n' "$q" | awk -v home="$HOME" -v root="$REPO_ROOT" -v base="/$REPO_BASE/" -v inrepo="$IN_REPO" -v SQ="'" '
      function rep(t, a, b,   o, i) { o = ""; while ((i = index(t, a)) > 0) { o = o substr(t, 1, i - 1) b; t = substr(t, i + length(a)) } return o t }
      { t = t (NR > 1 ? "\n" : "") $0 }
      END {
        t = rep(t, "~/", home "/"); t = rep(t, "${HOME}", home); t = rep(t, "$HOME", home)
        if (inrepo == 1) { t = rep(t, "${PWD}/", " "); t = rep(t, "$PWD/", " "); t = rep(t, "$(pwd)/", " ")
                           t = rep(t, "${PWD}", " . "); t = rep(t, "$PWD", " . "); t = rep(t, "$(pwd)", " . ") }
        if (root != "") { t = rep(t, root "/", " "); t = rep(t, root, " . ") }
        o = ""
        while ((i = index(t, base)) > 0) {
          j = i
          while (j > 1) { c = substr(t, j - 1, 1); if (c == " " || c == "\t" || c == "\n" || c == "\"" || c == SQ) break; j-- }
          o = o substr(t, 1, j - 1) " "; t = substr(t, i + length(base))
        }
        printf "%s", o t
      }'
    return
  fi
  q=${q//\~\//$HOME/}; q=${q//\$\{HOME\}/$HOME}; q=${q//\$HOME/$HOME}
  if (( IN_REPO )); then
    q=${q//\$\{PWD\}\// }; q=${q//\$PWD\// }; q=${q//\$(pwd)\// }
    q=${q//\$\{PWD\}/ . }; q=${q//\$PWD/ . }; q=${q//\$(pwd)/ . }
  fi
  if [[ -n $REPO_ROOT ]]; then
    q=${q//"$REPO_ROOT"\// }; q=${q//"$REPO_ROOT"/ . }
  fi
  if [[ $q == *"/$REPO_BASE/"* ]]; then
    while [[ $q =~ ^(.*)[^[:space:]\"\']*/$REPO_BASE/(.*)$ ]]; do q="${BASH_REMATCH[1]} ${BASH_REMATCH[2]}"; done
  fi
  printf '%s' "$q"
}

names_repo_path() { local q; q=$(relpaths "$1"); [[ $q =~ $REL_RE ]]; }
names_guarded() { local q; q=$(relpaths "$1"); [[ $q =~ $GUARD_RE ]]; }

# Quote-aware words, one per line: spaces inside quotes or after a backslash become $US.
words() {
  printf '%s\n' "$1" | awk -v US="$US" -v SQ="'" '
    { s = s (NR > 1 ? " " : "") $0 }
    function emit() { while (substr(w, 1, 1) == US) w = substr(w, 2)
                      while (length(w) && substr(w, length(w), 1) == US) w = substr(w, 1, length(w) - 1)
                      print w; w = ""; inw = 0 }
    END {
      n = length(s); w = ""; q = ""; inw = 0
      for (i = 1; i <= n; i++) {
        c = substr(s, i, 1)
        if (q != "") { if (c == q) q = ""; else w = w ((c == " " || c == "\t") ? US : c); continue }
        if (c == "\"" || c == SQ) { q = c; inw = 1; continue }
        if (c == "\\" && i < n) { i++; c = substr(s, i, 1); w = w ((c == " ") ? US : c); inw = 1; continue }
        if (c == " " || c == "\t") { if (inw) emit(); continue }
        w = w c; inw = 1
      }
      if (inw) emit()
    }'
}

# Positional words after the subcommand; quoted strings count once; flags and redirects dropped.
positionals() {
  words "$1" | awk '
    skip { skip = 0; next }
    /^[0-9]*(<|>|>>|&>|<<|<<<)$/ { skip = 1; next }
    /^[0-9]*[<>&]/ { next }
    /^-/ { next }
    { printf "%s ", $0 }'
}

last_word() { local w; w=$(words "$1" | tail -n 1); printf '%s' "${w//$US/ }"; }

is_relative() { [[ ! $1 =~ ^[\"\']?[/~$] ]]; }

# rm -r aimed at an ancestor of the repository (e.g. the folder that holds it).
targets_ancestor() {
  local q w
  q=${1//\~\//$HOME/}; q=${q//\~/$HOME}; q=${q//\$\{HOME\}/$HOME}; q=${q//\$HOME/$HOME}
  for w in $q; do
    w=${w//\"/}; w=${w//\'/}; w=${w%/}
    [[ $w == /* && -n $w ]] || continue
    [[ $REPO_ROOT == "$w" || $REPO_ROOT == "$w"/* ]] && return 0
  done
  return 1
}

# Optional local name check for text published to GitHub (untracked .git/hooks/text-name-check).
names_ok_for_publish() {
  local checker="$REPO_ROOT/.git/hooks/text-name-check" text=$1 f
  [[ -x $checker ]] || return 0
  for f in $(printf '%s' "$text" | grep -oE -- '(--body-file|--notes-file|-F)[[:space:]=]+[^[:space:]]+' | sed -E 's/^[^[:space:]=]+[[:space:]=]+//'); do
    [[ -f $f ]] && text+=$'\n'"$(cat -- "$f")"
  done
  printf '%s' "$text" | "$checker" >/dev/null 2>&1
}

# Sets REASON. Returns 0 = block, 3 = publishing command (plain spelling decides), 1 = pass.
# Runs in the current shell (no subshell per piece), so cd state carries to the next piece.
check_piece() {
  local p=$1 q sub rest up dest w staged=0 worktree=0
  p=${p#"${p%%[![:space:]]*}"}
  q=" $p "

  # --- redirects into content/governance, any program ----------------------------------
  if [[ $q == *'>'* ]] && [[ $q =~ $REDIR_RE ]]; then
    local tw
    while IFS= read -r tw; do
      tw=${tw#*>}; tw=${tw#[>|]}; tw=${tw#"${tw%%[![:space:]]*}"}
      [[ $tw == '&'* || -z $tw ]] && continue
      tw=${tw#[\"\']}; tw=${tw%[\"\']}
      if names_guarded " $tw" || { (( CD_CONTENT || CWD_CONTENT )) && is_relative "$tw"; }; then
        REASON="Bash-átirányítás a tananyagba vagy governance-fájlba — használd az Edit/Write eszközt"; return 0
      fi
    done < <(printf '%s\n' "$q" | grep -oE "$REDIR_TGT_RE")
  fi

  if [[ ! $p =~ ^(git|gh)[[:space:]] ]]; then
    if [[ $q =~ $CD_RE ]]; then
      w=${BASH_REMATCH[3]}
      if names_guarded " $w" || { (( CWD_CONTENT )) && is_relative "$w" && [[ ! $w =~ ^[\"\']?\.\. ]]; }; then CD_CONTENT=1; fi
      if names_repo_path " $w" || [[ $(relpaths " $w") =~ ^[[:space:]]*\.?[[:space:]]*$ ]] || { (( IN_REPO )) && is_relative "$w" && [[ ! $w =~ ^[\"\']?\.\. ]]; }; then CD_REPO=1; fi
      return 1
    fi
    # Read-only search lines (grep/rg/ag/ack) only write through a redirect, checked above.
    [[ $q =~ $READONLY_LINE_RE || $p =~ $READONLY_LINE_RE ]] && [[ ! $q =~ [[:space:]]--pre([[:space:]=]|$) ]] && return 1
    if [[ $q =~ $SED_I_RE ]] || [[ $q =~ $PERL_I_RE ]] || [[ $q =~ $AWK_I_RE ]]; then
      if names_guarded "$q" || (( CD_CONTENT || CWD_CONTENT || CONTENT_CTX )); then
        REASON="helyben szerkesztés (sed/perl/awk) a tananyagon — használd az Edit eszközt"; return 0
      fi
    fi
    if [[ $q =~ (^|[[:space:]])tee[[:space:]] ]]; then
      if names_guarded "$q" || (( CD_CONTENT || CWD_CONTENT )); then
        REASON="tee a tananyagba vagy governance-fájlba — használd a Write eszközt"; return 0
      fi
    fi
    if [[ $q =~ $COPY_RE ]]; then
      dest=$(last_word "$p")
      if names_guarded " $dest" || { [[ $q =~ [[:space:]](-t|--target-directory)[[:space:]=] ]] && names_guarded "$q"; } \
         || { (( CD_CONTENT || CWD_CONTENT )) && is_relative "$dest"; } \
         || { (( IN_REPO || CD_REPO )) && [[ $(relpaths " $dest") =~ ^[[:space:]]*(\.|\./|\*|\./\*)?[[:space:]]*$ ]]; }; then
        REASON="másolás/áthelyezés a tananyagba, governance-fájlba vagy a repó gyökerébe — használd az Edit/Write eszközt"; return 0
      fi
    fi
    # Editors take their target after a script that may contain separators, so a command
    # that names the content folder anywhere counts (like sed -i above).
    if { [[ $q =~ $WVERB_RE ]] && { names_guarded "$q" || (( CD_CONTENT || CWD_CONTENT )); }; } || \
       { [[ $q =~ $EDITOR_RE ]] && (( CONTENT_CTX )); }; then
      REASON="író parancs a tananyagon vagy governance-fájlon — használd az Edit/Write eszközt"; return 0
    fi
    if [[ $q =~ (^|[[:space:]])patch[[:space:]] ]] && (( IN_REPO || CD_REPO )); then
      REASON="patch-alkalmazás a repóban — a tananyag csak Edit/Write eszközzel változhat"; return 0
    fi
    if [[ $q =~ $RM_RE ]]; then
      names_repo_path "$q" && { REASON="a repository tartalmának törlése"; return 0; }
      if has_flag "$q" r recursive; then
        [[ $(relpaths "$q") =~ [[:space:]](\.|\.\.|/|\*|\./\*|~|\$\(pwd\)|\$PWD|\`pwd\`)/?[[:space:]] ]] && { REASON="rekurzív törlés a munkakönyvtárra"; return 0; }
        (( CD_REPO || CD_CONTENT )) && { REASON="rekurzív törlés a repóban (cd után)"; return 0; }
        (( IN_REPO )) && [[ $(positionals "$q") == *[\*\?\[]* ]] && { REASON="rekurzív, mintás törlés a repóban"; return 0; }
        targets_ancestor "$q" && { REASON="rekurzív törlés a repót tartalmazó mappára"; return 0; }
      fi
      if (( CWD_CONTENT )); then
        for w in $(positionals "${q#*rm}"); do is_relative "$w" && { REASON="törlés a tananyag mappájában"; return 0; }; done
      fi
    fi
    if [[ $q =~ (^|[[:space:]])xargs[[:space:]] ]] && [[ $q =~ [[:space:]]([^[:space:]]*/)?(rm|unlink|shred)[[:space:]] ]] && (( IN_REPO || CD_REPO )); then
      REASON="xargs rm a repóban"; return 0
    fi
    if [[ $q =~ (^|[[:space:]])find[[:space:]] ]] && [[ $q =~ (-delete|-exec[[:space:]]+[^[:space:]]*rm[[:space:]]) ]]; then
      if names_repo_path "$q" || targets_ancestor "$q" || { (( IN_REPO || CD_REPO )) && [[ $(relpaths "$q") =~ find[[:space:]]+[\"\']?[[:space:]]*(\.|\./[^[:space:]\"\']*)[[:space:]\"\'] ]]; }; then
        REASON="find -delete a repository tartalmán"; return 0
      fi
    fi
    if [[ $q =~ (^|[[:space:]])mv[[:space:]] ]]; then
      [[ $(relpaths "$q") =~ $TOP_RE ]] && { REASON="a repository egy fő mappájának vagy fájljának elmozdítása"; return 0; }
    fi
    if [[ $q =~ (rmtree|os\.remove|os\.unlink|os\.rmdir|unlinkSync|rmSync|fs\.rm|shutil\.move) ]] && names_repo_path "$q"; then
      REASON="programból indított törlés a repository tartalmán"; return 0
    fi
    return 1
  fi

  # --- gh ---------------------------------------------------------------------------
  if [[ $p =~ ^gh[[:space:]] ]]; then
    while [[ $p =~ ^gh[[:space:]]+(.*)[[:space:]](-R|--repo)[[:space:]=]+[^[:space:]]+(.*)$ ]]; do p="gh ${BASH_REMATCH[1]}${BASH_REMATCH[3]}"; done
    while [[ $p =~ ^gh[[:space:]]+(-R|--repo)[[:space:]=]+[^[:space:]]+(.*)$ ]]; do p="gh${BASH_REMATCH[2]}"; done
    up=$(printf '%s' "$p" | tr '[:lower:]' '[:upper:]')
    [[ $p =~ ^gh[[:space:]]+repo[[:space:]]+(delete|sync|archive|rename) ]] && { REASON="gh repo ${BASH_REMATCH[1]}: távoli repó módosítása — csak a felhasználó futtatja"; return 0; }
    [[ $p =~ ^gh[[:space:]]+release[[:space:]]+delete ]] && { REASON="gh release delete visszavonhatatlan"; return 0; }
    [[ $p =~ ^gh[[:space:]]+repo[[:space:]]+edit ]] && [[ $p =~ --visibility ]] && { REASON="a repository láthatóságának átállítása"; return 0; }
    if [[ $p =~ ^gh[[:space:]]+api[[:space:]] ]]; then
      if [[ $up =~ (-X|--METHOD)[[:space:]=]*(POST|PUT|PATCH|DELETE) ]]; then REASON="gh api írás — csak a felhasználó futtatja"; return 0; fi
      if [[ ! $up =~ (-X|--METHOD)[[:space:]=]*(GET|HEAD) ]] && [[ $q =~ [[:space:]](-f|-F|--field|--raw-field|--input)[[:space:]=] ]] && [[ ! $p =~ [[:space:]]graphql([[:space:]]|$) ]]; then
        REASON="gh api mezőkkel = implicit POST (írás) — csak a felhasználó futtatja"; return 0
      fi
      if [[ $p =~ [[:space:]]graphql([[:space:]]|$) ]] && { [[ $up =~ MUTATION ]] || [[ $p =~ =@ ]]; }; then
        REASON="gh api graphql mutation vagy fájlból olvasott lekérdezés — csak a felhasználó futtatja"; return 0
      fi
      return 1
    fi
    [[ $p =~ ^gh[[:space:]]+(issue|run|cache)[[:space:]]+delete ]] && { REASON="gh ${BASH_REMATCH[1]} delete visszavonhatatlan"; return 0; }
    if [[ $p =~ $GH_PUBLISH_RE ]]; then
      names_ok_for_publish "$p" || { REASON="a GitHubra kerülő szöveg hangnevet vagy privát repónevet tartalmaz (helyi névellenőrzés)"; return 0; }
      REASON="gh ${BASH_REMATCH[1]}"; return 3
    fi
    return 1
  fi

  # --- git --------------------------------------------------------------------------
  [[ $p =~ -c[[:space:]]+[\"\']?alias\. ]] && { REASON="git -c alias.*: egy alias bármit elrejthet — futtasd a parancsot közvetlenül"; return 0; }
  local raw=$p
  norm_git "$p"; p=$NG
  p=${p/#git \"/git }; p=${p/#git \'/git }
  [[ $p =~ ^git[[:space:]]+([a-z][a-z0-9-]*)[\"\']?(.*)$ ]] || return 1
  sub=${BASH_REMATCH[1]}; rest=" ${BASH_REMATCH[2]} "
  if [[ $rest == *[\"\'\`\)]* ]]; then
    rest=$(printf '%s\n' "$rest" | sed -e "s/[\"'\`)]/ & /g")
  fi
  [[ $rest =~ --pathspec-from-file ]] && [[ $sub =~ ^(checkout|restore|reset|rm|add|stash)$ ]] && { REASON="--pathspec-from-file: a célfájlok itt nem láthatók — futtasd kifejtett útvonalakkal"; return 0; }

  case $sub in
    reset)
      if has_long "$rest" hard 2 || has_long "$rest" merge 2 || has_long "$rest" keep 1; then
        REASON="a hard/merge/keep reset eldobja a nem commitolt munkát"; return 0
      fi
      if [[ ! $rest =~ [[:space:]]--[[:space:]] ]] && \
         [[ $rest =~ [[:space:]](HEAD[~^][^[:space:]]*|@[~^{][^[:space:]]*|ORIG_HEAD|FETCH_HEAD|origin/[^[:space:]]+|main|master|[0-9a-f]{7,40})([[:space:]]|$) ]]; then
        REASON="a reset <commit> átállítja a branchet (--soft/--mixed alakban is history rewrite)"; return 0
      fi ;;
    clean)
      has_flag "$rest" f force 1 && { REASON="a kényszerített clean visszavonhatatlanul törli a nem követett fájlokat"; return 0; }
      if [[ $raw =~ clean\.requireForce[[:space:]]*=[[:space:]]*false ]] && ! has_flag "$rest" n dry-run 1 && ! has_flag "$rest" i interactive 1; then
        REASON="clean.requireForce=false mellett a clean -f nélkül is töröl"; return 0
      fi ;;
    checkout)
      [[ $rest =~ [[:space:]]--[[:space:]] ]] && { REASON="checkout -- <path> eldobja a working tree változtatásait"; return 0; }
      has_flag "$rest" f force 1 && { REASON="a kényszerített checkout eldobja a working tree változtatásait"; return 0; }
      [[ $rest =~ [[:space:]]-B[[:space:]] ]] && { REASON="checkout -B felülír egy meglévő branch-et"; return 0; }
      has_long "$rest" theirs 2 && { REASON="checkout --theirs <path> felülírja a fájlt"; return 0; }
      has_long "$rest" ours 2 && { REASON="checkout --ours <path> felülírja a fájlt"; return 0; }
      if [[ ! $rest =~ [[:space:]](-b|--orphan|-t|--track)[[:space:]] ]]; then
        local pos n=0 path
        pos=$(positionals "$rest")
        for w in $pos; do
          n=$((n + 1)); path=${w//$US/ }
          if [[ $w == . || $w == ./ || $w == :/ || $w == *[\*\?\[]* ]] || [[ -e "$CWD/$path" && ! -e "$REPO_ROOT/.git/refs/heads/$path" ]] || [[ $path == */* && -e "$REPO_ROOT/$path" ]]; then
            REASON="checkout <path> felülírja a fájlt a working tree-ben"; return 0
          fi
        done
        (( n >= 2 )) && { REASON="checkout <commit> <path> felülírja a fájlt a working tree-ben"; return 0; }
      fi ;;
    switch)
      has_flag "$rest" f force 1 && { REASON="a kényszerített switch eldobja a working tree változtatásait"; return 0; }
      [[ $rest =~ [[:space:]]-C[[:space:]] ]] && { REASON="switch -C felülír egy meglévő branch-et"; return 0; }
      has_long "$rest" discard-changes 2 && { REASON="a switch --discard-changes eldobja a working tree változtatásait"; return 0; }
      ;;
    restore)
      if has_long "$rest" staged 2 || [[ $rest =~ [[:space:]]-[a-zA-Z]*S[a-zA-Z]*([[:space:]]|$) ]]; then staged=1; fi
      if has_long "$rest" worktree 1 || [[ $rest =~ [[:space:]]-[a-zA-Z]*W[a-zA-Z]*([[:space:]]|$) ]]; then worktree=1; fi
      if (( ! staged || worktree )); then REASON="a restore eldobja a working tree változtatásait (csak --staged engedett)"; return 0; fi ;;
    checkout-index)
      if has_flag "$rest" f force 1 || has_flag "$rest" a all 1; then REASON="checkout-index -f/-a felülírja a working tree fájljait"; return 0; fi ;;
    read-tree)
      if [[ $rest =~ [[:space:]]-u([[:space:]]|$) ]] || has_long "$rest" reset 3; then REASON="read-tree -u/--reset felülírja a working tree-t"; return 0; fi ;;
    push)
      if has_flag "$rest" f force 2 || has_long "$rest" force-with-lease 7 || has_long "$rest" force-if-includes 7 || \
         has_flag "$rest" d delete 2 || has_long "$rest" mirror 1 || has_long "$rest" prune 3 || \
         [[ $rest =~ [[:space:]][+:][^[:space:]] ]]; then
        REASON="a kényszerített vagy törlő push átírja a távoli historyt"; return 0
      fi
      has_long "$rest" no-verify 4 && { REASON="push --no-verify átugorja a helyi pre-push névellenőrzést"; return 0; }
      REASON="git push"; return 3 ;;
    fetch)
      if [[ $rest =~ [[:space:]]\+[^[:space:]]*: ]] || [[ $rest =~ [[:space:]][^-[:space:]][^[:space:]]*:[^[:space:]]+ ]] || has_long "$rest" update-head-ok 3; then
        REASON="fetch helyi branchbe (refspec kettősponttal) felülírhatja a lokális branchet"; return 0
      fi ;;
    config)
      if [[ $rest =~ (^|[[:space:]])(alias\.|core\.hookspath|core\.hooksPath|pull\.rebase|branch\.[^[:space:]]*\.rebase|rebase\.) ]] && [[ ! $rest =~ [[:space:]](--get|--get-all|--get-regexp|-l|--list)([[:space:]]|$) ]]; then
        REASON="git config: alias, hooksPath vagy rebase beállítása megkerülné a védelmet"; return 0
      fi ;;
    pull)
      if has_long "$rest" rebase 3 && [[ ! $rest =~ --rebase=(false|no) ]] || [[ $rest =~ [[:space:]]-[a-zA-Z]*r[a-zA-Z]*([[:space:]]|$) ]] || \
         [[ $raw =~ -c[[:space:]]+pull\.rebase[[:space:]]*=[[:space:]]*(true|merges|interactive|i|m) ]]; then
        REASON="a pull --rebase átírja a lokális historyt"; return 0
      fi ;;
    rebase)
      [[ $rest =~ ^[[:space:]]*--abort[[:space:]\"\'\`\)]*$ ]] || { REASON="a rebase átírja a lokális historyt (a repo szabálya tiltja)"; return 0; } ;;
    commit)
      has_long "$rest" amend 2 && { REASON="az amend felülírja a felhasználó checkpoint-commitját"; return 0; } ;;
    filter-branch|filter-repo) REASON="history rewrite"; return 0 ;;
    reflog) [[ $rest =~ ^[[:space:]]*(delete|expire) ]] && { REASON="a reflog törlése megszünteti az utolsó visszaállítási esélyt"; return 0; } ;;
    update-ref) REASON="az update-ref közvetlenül átírja vagy törli a ref-eket"; return 0 ;;
    prune) REASON="a prune végleg törli az elérhetetlen objektumokat"; return 0 ;;
    gc) has_long "$rest" prune 1 && { REASON="a prune végleg törli az elérhetetlen objektumokat"; return 0; } ;;
    stash) [[ $rest =~ ^[[:space:]]*(drop|clear) ]] && { REASON="a stash törlése végleges"; return 0; } ;;
    branch)
      [[ $rest =~ [[:space:]]-(D|M|C)[[:space:]] ]] && { REASON="branch kényszerített törlése/átnevezése/másolása pusholatlan commitokat veszíthet"; return 0; }
      has_flag "$rest" f force 2 && { REASON="a kényszerített branch felülír egy meglévő branch-et"; return 0; } ;;
    worktree) [[ $rest =~ ^[[:space:]]*remove ]] && has_flag "$rest" f force 1 && { REASON="worktree kényszerített eltávolítása eldobja a benne lévő munkát"; return 0; } ;;
    apply|am)
      [[ $sub == apply && $rest =~ [[:space:]]--(check|stat|numstat|summary)([[:space:]]|$) ]] && return 1
      REASON="git $sub: patch-alkalmazás — a tananyag csak Edit/Write eszközzel változhat"; return 0 ;;
    rm)
      [[ $rest =~ [[:space:]]--cached([[:space:]]|$) ]] && return 1
      local rpos; rpos=" $(positionals "$rest")"
      [[ $rpos =~ [[:space:]](\.|\./|\*|:/)[[:space:]] ]] && { REASON="git rm . — a teljes munkakönyvtár törlése"; return 0; }
      names_repo_path "$rest" && { REASON="a repository tartalmának törlése"; return 0; } ;;
  esac
  return 1
}

# Echoes a reason. Returns 0 = block, 1 = pass. Publishing commands pass only in their
# plain standalone spelling (the settings ask rule then prompts in every mode).
verdict() {
  local text cwd piece r rc pub="" npieces=0 trimmed
  if (( ${#1} > MAX_LEN )); then
    echo "a parancs túl hosszú (${#1} bájt > $MAX_LEN) ahhoz, hogy a hook megbízhatóan ellenőrizze — írd a tartalmat fájlba a Write eszközzel"; return 0
  fi
  text=$(norm_bins "$1"); cwd=${2:-$REPO_ROOT}
  CWD=$cwd; IN_REPO=0; CWD_CONTENT=0; CD_CONTENT=0; CD_REPO=0; CONTENT_CTX=0
  [[ $cwd == "$REPO_ROOT" || $cwd == "$REPO_ROOT"/* ]] && IN_REPO=1
  [[ $cwd == "$REPO_ROOT/02 Tervezet" || $cwd == "$REPO_ROOT/02 Tervezet"/* ]] && CWD_CONTENT=1
  [[ $text =~ $CONTENT_RE ]] && CONTENT_CTX=1
  # Inline scripts span separators, so check them whole: a write whose target is a
  # content/governance path, or a write to a non-literal target in a script naming one.
  if [[ $text =~ $INTERP_RE ]]; then
    local G=$SCRIPT_G st
    st=$(relpaths "$text")
    if [[ $st =~ open\([^\)]*${G}[^\)]*,[[:space:]]*(mode[[:space:]]*=[[:space:]]*)?[\"\'][wax] ]] || \
       [[ $st =~ open\([^\(\)]*\([^\(\)]*${G}[^\(\)]*\)[^\(\)]*,[[:space:]]*(mode[[:space:]]*=[[:space:]]*)?[\"\'][wax] ]] || \
       [[ $st =~ Path\([^\)]*${G}[^\)]*\)\.(write_text|write_bytes|open\([\"\'][wax]) ]] || \
       [[ $st =~ (writeFileSync|appendFileSync|writeFile|appendFile|copyFileSync|createWriteStream|renameSync)\([^\)]*${G} ]] || \
       [[ $st =~ (shutil\.(copy|copy2|copyfile|move|copytree)|os\.(replace|rename))\([^\)]*,[[:space:]]*[^\)]*${G} ]] || \
       { [[ $st =~ $G ]] && { [[ $st =~ open\([[:space:]]*[^\"\'[:space:]][^\)]*,[[:space:]]*(mode[[:space:]]*=[[:space:]]*)?[\"\'][wax] ]] || \
                               [[ $st =~ [[:alnum:]_\)]\.(write_text|write_bytes)\( ]] || \
                               [[ $st =~ (os\.(replace|rename)|createWriteStream|File\.write|IO\.write)\( ]] || \
                               [[ $st =~ open\([[:space:]]*[A-Za-z_]+[[:space:]]*,[[:space:]]*[\"\'][\>+] ]]; }; }; then
      echo "szkriptből írás a tananyagba vagy governance-fájlba — használd az Edit/Write eszközt"; return 0
    fi
  fi
  while IFS= read -r piece; do
    [[ $piece =~ ^[[:space:]]*$ ]] && continue
    npieces=$((npieces + 1))
    REASON=""; check_piece "$piece"; rc=$?
    (( rc == 0 )) && { echo "$REASON"; return 0; }
    (( rc == 3 )) && [[ -z $pub ]] && pub=$REASON
  done < <(split_pieces "$text")
  if [[ -n $pub ]]; then
    trimmed=${1#"${1%%[![:space:]]*}"}
    if (( npieces == 1 )) && { [[ $trimmed =~ $PLAIN_PUSH_RE ]] || [[ $trimmed =~ $PLAIN_GHPR_RE ]]; } && [[ ! $trimmed =~ $SEP_RE ]] && [[ ! $trimmed =~ \$\( ]]; then
      return 1
    fi
    echo "$pub csak egyszerű, önálló alakban futhat (pl. \`git push origin <branch>\`, \`gh pr merge <n>\`; hosszabb szöveg \`--body-file\`-lal) — így a jóváhagyó kérdés minden módban megjelenik"; return 0
  fi
  return 1
}

if [[ "${1:-}" == "--selftest" ]]; then
  fail=0
  [[ -n ${GUARD_REPO_ROOT:-} ]] && { REPO_ROOT=$GUARD_REPO_ROOT; REPO_BASE=${REPO_ROOT##*/}; }
  # Corpus assembled from parts so this file's own text does not read as runnable.
  G="git"; R="rm"; H="gh"; T="02 Tervezet"; PT="02 Tervezet/Program terv.md"; UT="tools/content_integrity.py"
  must_block=(
    "$G reset --hard HEAD~1" "$G reset --hard" "$G reset --merge" "$G reset --har" "$G reset --ha HEAD" "$G reset --kee"
    "$G clean -f" "$G clean -fd" "$G clean -fdx" "$G clean -df" "$G clean -xdf"
    "$G clean --force" "$G clean --force -d" "$G clean -d --force" "$G clean --forc -d" "$G clean --f"
    "$G checkout -- ." "$G checkout -- $T/x.md" "$G checkout ." "$G checkout ./" "$G checkout \"$PT\"" "$G checkout --theirs x.md"
    "$G checkout $UT" "$G checkout --pathspec-from-file=f.txt"
    "$G checkout -f" "$G checkout -f main" "$G checkout --force main"
    "$G switch -f main" "$G switch --force main" "$G switch --discard-changes main"
    "$G checkout -B main" "$G switch -C main" "$G checkout-index -f -a" "$G read-tree -u --reset HEAD"
    "$G restore ." "$G restore $T/x.md" "$G restore --staged --worktree x" "$G restore --staged -W f" "$G restore -SW f"
    "$G push --force" "$G push -f origin main" "$G push origin main -f" "$G push --forc origin main" "$G push --no-verify origin main"
    "$G push --force-with-lease origin HEAD" "$G push --mirror" "$G push origin --delete x" "$G push -d origin x"
    "$G push origin :x" "$G push --prune origin" "$G -C /r push --force" "$G fetch origin +main:main" "$G fetch origin main:main"
    "$G rebase -i HEAD~3" "$G rebase main" "$G rebase --continue" "$G rebase --skip"
    "$G rebase --onto main HEAD~2" "$G rebase --quit" "$G rebase --aborted"
    "$G rebase --abort && $G rebase -i HEAD~3" "$G commit --amend --no-edit" "$G commit --amen"
    "$G filter-branch --tree-filter x" "$G filter-repo --path x"
    "$G branch -D audit-fixes-2026-08-25" "$G branch --force main HEAD~2" "$G branch -M main"
    "$G stash clear" "$G stash drop" "$G reflog expire --expire=now --all"
    "$G gc --prune=now" "$G update-ref -d refs/heads/x" "$G update-ref --delete refs/heads/x" "$G update-ref refs/heads/main HEAD~3" "$G prune"
    "$G worktree remove --force ../wt" "$G worktree remove -f ../wt"
    "$G reset --soft HEAD~1" "$G reset HEAD~3" "$G reset --keep HEAD~1" "$G reset origin/main" $'git reset \\\n--hard'
    "$G checkout HEAD~1 \"$T/x.md\"" "$G -c clean.requireForce=false clean -d"
    "$G pull --rebase" "$G pull -r origin main" "$G -c pull.rebase=true pull"
    "\"$G\" reset --hard" "$G 'reset' --hard" "\$(which $G) reset --hard" "\$(command -v $G) reset --hard" "/usr/bin/$G reset --hard"
    "$G -c alias.x='reset --hard' x" "$G config alias.x 'reset --hard'" "$G config core.hooksPath /dev/null"
    "$G --git-dir .git reset --hard" "$G --work-tree . reset --hard" "$G --glob-pathspecs reset --hard" "$G --config-env=a.b=C reset --hard"
    "$G rm -rf ." "$G apply /tmp/p.diff" "$G am /tmp/p.mbox"
    "$G status && $G reset --hard" "cd /tmp && $G clean --force -d" "bash -c \"$G reset --hard\"" "cat > f <<EOF $G reset --hard EOF"
    # publishing: only the plain standalone spelling may pass (settings ask prompts)
    "$G push -u origin HEAD && tail -f ci.log" "$G add -A && $G commit -m x && $G push" "$G -c k=v push origin main"
    "$G --no-pager push origin main" "bash -c \"$G push origin main\"" "/usr/bin/$G push origin main"
    "$H pr --repo o/r merge 12" "$H pr view 1 && $H pr merge 1" "$H pr view 1 && $H pr create --title x --body y"
    "$H -R o/r pr create --title x --body y" "$H issue delete 3" "$H run delete 9" "bash -c \"$H workflow run x.yml\""
    "\`command -v $G\` reset --hard" "g\\it reset --hard" "$G re''set --hard" "$G \"\"reset --hard"
    # deletion aimed at the repository
    "$R -rf $T" "$R -r -f $T" "$R -rf ." "$R -fr ." "$R -rf .claude" "$R -rf ./*" "$R -rf 02*"
    "$R CLAUDE.md" "$R -f .claude/settings.json" "$R -rf tools/" "$R --recursive --force ." "$R -rf ~"
    "$R -rf 02\\ Tervezet/x" "/bin/$R -rf \"$T\"" "\\$R -rf tools" "find \"$T\" -name x -delete" "find . -name \"*.md\" -delete"
    "cd \"$T\" && $R -rf Modulok" "$R -rf ../$REPO_BASE/02\\ Tervezet" "$R -rf $REPO_ROOT/tools" "$R -rf \"\$PWD/$T\""
    "$R -rf ${REPO_ROOT%/*}" "find . -name x | xargs $R" "$G ls-files -z | xargs -0 $R -f" "find . -exec /usr/bin/$R {} +"
    "find \"\$PWD\" -name x -delete" $'rm -r \\\n"02 Tervezet"'
    "python3 -c \"import shutil; shutil.rmtree('$T')\"" "mv \"$T\" /tmp/"
    "$H repo delete x --yes" "$H release delete v1" "$H repo sync --force" "$H api -X DELETE repos/o/r/git/refs/heads/x"
    "$H api --method PATCH repos/o/r/git/refs/heads/main -f sha=x" "$H api -X PUT repos/o/r/pulls/12/merge"
    "$H api -X GET repos/o/r -X POST" "$H api repos/o/r/merges -f base=main -f head=x" "$H api graphql -f query='mutation{x}'"
    "$H api graphql -F query=@q.graphql" "$H api -X DELETE repos/o/r/issues/1/labels/x"
    # course content and governance only through Edit/Write (the sandbox is the real boundary)
    "sed -i '' 's/a/b/' \"$T/x.md\"" "sed -E -i.bak 's/a/b/' \"$T/x.md\"" "perl -pi -e 's/a/b/' \"$T/x.md\""
    "perl -pe 's/a/b/' -i \"$T/x.md\"" "perl -0777 -pi -e 's/a/b/' \"$T/x.md\"" "awk -i inplace '{print}' \"$T/x.md\""
    "grep -rl x \"$T\" | xargs sed -i '' 's/a/b/'" "find \"$T\" -name \"*.md\" -exec sed -i '' 's/a/b/' {} +"
    "for f in \"$T\"/Modulok/*.md; do sed -i '' 's/a/b/' \"\$f\"; done" "(cd \"$T\" && sed -i '' 's/a/b/' x.md)"
    "bash -c 'cd \"$T\" && sed -i \"\" s/a/b/ x.md'" "pushd \"$T\" && sed -i '' s/a/b/ x.md" $'sed -i \'\' s/a/b/ \\\n"02 Tervezet/x.md"'
    "cd \"$T/Modulok\" && sed -i '' 's/a/b/' x.md" "echo x > \"$T/x.md\"" "echo x >> \"$T/Modulok/a.md\"" "echo x >| \"$T/x.md\""
    "cat /tmp/x > \"/Users/u/repo/$T/x.md\"" "printf x | tee \"$T/x.md\"" "cp /tmp/x \"$T/x.md\"" "mv /tmp/x \"$T/Modulok/x.md\""
    "install /tmp/x \"$T/x.md\"" "rsync -a /tmp/x/ \"$T/\"" "rsync -a --delete /tmp/x/ ./" "cp -R /tmp/x/. ."
    "$G show HEAD:\"$T/x.md\" > \"$T/x.md\"" "patch -p1 < /tmp/p.diff" "dd if=/tmp/x of=\"$T/x.md\"" "truncate -s 0 \"$T/x.md\""
    "curl -o \"$T/x.md\" https://e.x" "tar -xf /tmp/a.tar -C \"$T\"" "unzip -o /tmp/a.zip -d \"$T\""
    "python3 - <<EOF p='$T/x.md'; open(p,'w').write('x') EOF" "python3 -c \"import pathlib; pathlib.Path('$T/x.md').write_text('x')\""
    "python3 -c \"open('$T/x.md','wb').write(b'x')\"" "python3 -c \"import shutil; shutil.copy('/tmp/x','$T/x.md')\""
    "python3 -c \"import os; os.replace('/tmp/x', os.path.join('$T','x.md'))\"" "node -e \"require('fs').writeFileSync('$T/x.md','x')\""
    "node -e \"require('fs').createWriteStream('$T/x.md').write('x')\"" "perl -e 'open(F,\">$T/x.md\"); print F 1'"
    "echo '{\"disableAllHooks\":true}' > .claude/settings.local.json" "cp /tmp/x CLAUDE.md" "sed -i '' 's/a/b/' .github/workflows/content-integrity.yml"
    "echo '{}' > tools/approved-visible-text.json" "ex -sc '%s/a/b/|x' \"$T/x.md\"" "vim -c 'wq' \"$T/x.md\""
    "python3 -c \"import os; open(os.path.join('$T','M.md'),'w').write('x')\""
  )
  must_pass=(
    "$G status" "$G status --short" "$G diff" "$G diff --check" "$G diff --stat" "$G diff --check origin/main...HEAD"
    "$G add $T/Modulok/M3/x.md" "$G add -A" "$G add -f $T/x.md" "$G add -N \"$T/x.md\""
    "$G commit -m 'fix: x'" "$G commit -F msg.txt" "$G log -10 --oneline" "$G checkout -" "$G switch -" "$G stash show -p"
    "$G branch --show-current" "$G branch -m old new" "$G branch -a" "$G branch -v" "$G branch -d merged-branch"
    "$G checkout main" "$G checkout -b feature/x" "$G switch main" "$G switch -c feature/x" "$G checkout main 2>&1" "$G checkout main 2>/dev/null"
    "$G restore --staged $T/x.md" "$G restore -S $T/x.md" "$G cherry-pick abc1234" "$G show abc1234:\"$T/x.md\" > /tmp/x.md"
    "$G stash" "$G stash pop" "$G stash list" "$G show HEAD" "$G clean -n" "$G clean -nd" "$G fetch --quiet origin main" "$G fetch origin"
    "$G worktree list" "$G rev-parse HEAD" "$G reflog" "$G gc" "$G apply --check /tmp/p.diff" "$G config --get pull.rebase" "$G config user.name x"
    "$G rebase --abort" "$G merge --abort" "$G cherry-pick --abort" "$G revert --abort" "$G -C /r rebase --abort"
    "$G status && $G rebase --abort" "$G merge main" "$G revert HEAD" "$G worktree add ../wt-x feature"
    "$G rebase --abort;" "$G rebase --abort && $G status" "cd /repo && $G rebase --abort"
    "$G rebase --abort; echo done" "$G merge --abort;" "$G cherry-pick --abort && $G status"
    "$G push origin main" "$G push -u origin HEAD" "$G push" "$G -C /r push origin main" "$H pr merge 1 --merge" "$H pr close 3 --delete-branch"
    "python3 tools/content_integrity.py" "python3 tools/content_integrity.py --release-report" "python3 tools/media_manifest.py build"
    "python3 tools/test_media_manifest.py --pin-visible \"CF-01: x\"" "python3 tools/test_media_manifest.py --pin-visible \"CF-01: a -> $T\""
    "grep -rn mintaszo '$T'" "ls -la" "ls -lf" "cat CLAUDE.md" "sed -n 5p \"$T/x.md\"" "grep -rn x \"$T\" | tee /tmp/out.txt"
    "grep -rn \"$G push\" CLAUDE.md .claude/" "grep -rn \"$R -rf\" .claude/hooks/" "rg \"sed -i\" .claude/" "grep -n \"$G reset --hard\" CLAUDE.md"
    "cat \"$T/x.md\" > /tmp/x.md" "cp \"$T/x.md\" /tmp/x.md" "cp -r \"$T/Modulok\" /tmp/backup" "cd \"$T\" && grep -rn x ." "cd \"$T\" && ls > /tmp/list.txt"
    "python3 -c \"print(open('$T/x.md').read()[:10])\"" "wc -l \"$T\"/Modulok/*/*.md > /tmp/wc.txt" "find \"$T\" -name '*.md' | wc -l"
    "python3 - <<EOF t=open('$T/x.md').read(); open('/private/tmp/o.json','w').write(t) EOF"
    "$G commit -m \"fix -> $T\"" "$R -rf /private/tmp/claude-501/scratch" "$R /tmp/x.json" "$R -rf /private/tmp/x/scratchpad/tools/"
    "$R ~/.claude/projects/x/memory/a.md" "bash .claude/hooks/guard-repo-safety.sh --selftest" "bash .github/read-only-workflows.sh"
    "$G log -1 && $H repo view --json rebaseMergeAllowed" "$G pull --no-rebase" "$G pull --rebase=false" "$G pull"
    "$G log --grep=rebase" "$G grep -n \"reset --hard\" CLAUDE.md"
    "$G add \"$T/Modulok/M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md\" && $G commit -m x"
    "$G checkout -b x && $G diff main -- $T/x.md" "$G rm --cached \"$T/x.md\"" "$G checkout main && ls -lf"
    "$G reset" "$G reset -- $T/x.md" "$G reset HEAD $T/x.md" "$G -C /r status" "$H pr view 12" "$H pr list --state all"
    "$H api repos/o/r/git/refs/heads/main" "$H api -X GET search/issues -f q=x" "$H api graphql -f query='query{viewer{login}}'"
    "$G mv \"$T/a.md\" \"$T/b.md\"" "node --test test/x.test.mjs" "$H pr create --title x --body y"
    "$H pr create --title x --body-file /tmp/b.md" "$H workflow run x.yml" "$H secret list" "$H run view 9" "$H issue list"
    "vim --version" "printf '%s\\n' a b" "echo 'a\\tb'"
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
  # A command in a content folder: relative deletes and edits are blocked there.
  CWDC="$REPO_ROOT/02 Tervezet/Modulok"
  for c in "$R -rf M3" "$R x.md" "sed -i '' s/a/b/ x.md" "echo x > x.md"; do
    if r=$(verdict "$c" "$CWDC"); then printf 'BLOCK ok   [cwd tananyag] %-30s (%s)\n' "$c" "$r"
    else printf 'MISS  FAIL [cwd tananyag] %s\n' "$c"; fail=1; fi
  done
  # From outside the repository: the repository named by absolute, ~ or $HOME path.
  OUT=( "$R -rf \"$REPO_ROOT\"" "find $REPO_ROOT -name x -delete" "$R -rf ${REPO_ROOT%/*}" )
  [[ $REPO_ROOT == "$HOME"/* ]] && OUT+=( "$R -rf \"\$HOME${REPO_ROOT#"$HOME"}\"" "find ~${REPO_ROOT#"$HOME"} -name x -delete" )
  for c in "${OUT[@]}"; do
    if r=$(verdict "$c" /tmp); then printf 'BLOCK ok   [cwd /tmp] %-34s (%s)\n' "$c" "$r"
    else printf 'MISS  FAIL [cwd /tmp] %s\n' "$c"; fail=1; fi
  done
  big=$(printf 'x%.0s' $(seq 1 $((MAX_LEN + 10))))
  if r=$(verdict "echo $big"); then echo "BLOCK ok   [túl hosszú parancs]"; else echo "MISS  FAIL [túl hosszú parancs]"; fail=1; fi
  # The real stdin path (JSON parse, background analysis, watchdog, exit code), end to end.
  for pair in "2|$G reset --hard" "0|$G status" "2|$R -rf ."; do
    want=${pair%%|*}; c=${pair#*|}
    printf '{"tool_input":{"command":"%s"},"cwd":"%s"}' "$c" "$REPO_ROOT" | bash "${BASH_SOURCE[0]}" >/dev/null 2>&1; got=$?
    if [[ $got == "$want" ]]; then echo "STDIN ok   exit=$got  $c"; else echo "STDIN FAIL exit=$got (want $want)  $c"; fail=1; fi
  done
  echo "--- ${#must_block[@]} must-block (+5 cwd tananyag/túl hosszú, +${#OUT[@]} cwd /tmp), ${#must_pass[@]} must-pass, 3 stdin ---"
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

# Watchdog: the analysis runs in the background; if it is still running after WATCHDOG
# seconds, the command is blocked. A hook killed by its own timeout would let it through.
out=$(mktemp "${TMPDIR:-/tmp}/guard-repo-safety.XXXXXX") || { echo "BLOKKOLVA: a hook nem tud ideiglenes fájlt nyitni" >&2; exit 2; }
trap 'rm -f -- "$out" "$out.r"' EXIT
set -m   # the analysis gets its own process group, so a timeout kills all of it
( set +m; if verdict "$command_text" "${cwd:-$REPO_ROOT}" > "$out.r"; then printf 'B' > "$out"; else printf 'P' > "$out"; fi
) </dev/null >/dev/null 2>&1 &
vpid=$!
set +m
( trap 'kill "$sp" 2>/dev/null; exit 0' TERM; sleep "$WATCHDOG" & sp=$!; wait "$sp"; kill -TERM -- "-$vpid" 2>/dev/null
) </dev/null >/dev/null 2>&1 &
wpid=$!
wait "$vpid" 2>/dev/null
kill -TERM "$wpid" 2>/dev/null
res=$(cat -- "$out" 2>/dev/null)
case $res in
  P) exit 0 ;;
  B) reason=$(cat -- "$out.r" 2>/dev/null) ;;
  *) reason="a parancs elemzése $WATCHDOG mp alatt nem fejeződött be — biztonsági okból blokkolva; tagold kisebb parancsokra, vagy írd a tartalmat fájlba a Write eszközzel" ;;
esac
cat >&2 <<MSG
BLOKKOLVA (.claude/hooks/guard-repo-safety.sh): $reason

Parancs (első 400 karakter): ${command_text:0:400}

Ezen a branchen pusholatlan felhasználói commitok és kézzel szerkesztett tananyag van.
Destruktív git- és törlőműveletek, valamint a tananyag/governance Bash-szerkesztése
tiltott — lásd CLAUDE.md "Git-biztonság". Tananyag: Edit/Write eszköz.
Ha ez tényleg kell, a felhasználó futtassa kézzel.
MSG
exit 2
