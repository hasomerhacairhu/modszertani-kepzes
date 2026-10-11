#!/usr/bin/env bash
# PreToolUse guard (Bash and Monitor). Layers (see CLAUDE.md "Git-biztonság"):
#
# 1. The OS SANDBOX (.claude/settings.json) is the write boundary: sandboxed Bash cannot write
#    anywhere in the repository (`.git` included), however a command is spelled.
# 2. Only calls whose every part is literally `git …` or `gh …` (plus the media build, the
#    visible-text pin and `tools/audit_import.py`, which enforces its own bounds: a finished .md
#    from the session temp area into `01 Fejlesztés/04 Audit/` only, never over a tracked file,
#    after the name check) run OUTSIDE the sandbox. For those this hook is the guard, and it works
#    by ALLOWLIST: git only inside this repository (or a root listed in the untracked
#    `.git/info/guard-allowed-roots`), only known subcommands, no code-executing options
#    (-c except harmless keys, config writes, --upload-pack/--exec/ext::, --output, …), no
#    history rewrite or discarding of work; gh only read-only subcommands, `gh api` GET, and a
#    short list of publishing commands. Bash quote removal is applied before matching
#    (`r"eset"`, `'-'f`, `\+main`); ANSI-C `$'…'` quoting in git/gh is blocked.
# 3. Publishing (`git push`, gh PR/issue writes) passes only in its plain standalone spelling,
#    which a settings ask rule catches in every permission mode; its text is checked by the
#    untracked `.git/hooks/text-name-check` (missing checker = blocked).
# The content rules for other programs are early, readable warnings; the sandbox enforces.
#
# This repository regularly carries UNPUSHED user commits and hand-edited course content.
# Contract: PreToolUse JSON on stdin (command, cwd). Exit 2 + stderr = block; exit 0 = pass.
# The hook never answers "ask". FAIL CLOSED: unparsable input, commands over MAX_LEN bytes and
# any analysis still running after WATCHDOG seconds are blocked. Long text is processed with
# sed/tr/awk single passes (bash 3.2 substitutions are quadratic on it).
# A command that merely MENTIONS a dangerous invocation can be blocked; use `git commit -F`
# or the Write tool for such text. Written for bash 3.2 (macOS); CI runs it on Ubuntu.
# Self-test:  bash .claude/hooks/guard-repo-safety.sh --selftest
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
GUARD_RE="(^|[[:space:]\"'=])(\\./)?(02(\\\\)?[[:space:]]Tervezet|\\.claude/|\\.github/|\\.git/|\\.git([[:space:]\"']|\$)|\\.gitattributes|CLAUDE\\.md|tools/approved-visible-text\\.json|tools/[^[:space:]\"']*\\.py)"
REDIR_RE="(^|[^->=])>[>|]?[[:space:]]*[\"']?"
REDIR_TGT_RE="(^|[^->=])>[>|]?[[:space:]]*(\"[^\"]*\"|'[^']*'|(\\\\[[:space:]]|[^[:space:]])+)"
SED_I_RE='(^|[[:space:]])(sed|gsed)[[:space:]]([^|]*[[:space:]])?(-[a-zA-Z]*i|--in-place)'
PERL_I_RE='(^|[[:space:]])perl[[:space:]]([^|]*[[:space:]])?-[a-zA-Z0-9]*i'
AWK_I_RE='(^|[[:space:]])g?awk[[:space:]]([^|]*[[:space:]])?-i[[:space:]]*inplace'
COPY_RE='(^|[[:space:]])(cp|mv|install|rsync|ln|ditto)[[:space:]]'
WVERB_RE='(^|[[:space:]])(dd|truncate|sponge|touch|mkdir)[[:space:]]'
EDITOR_RE='(^|[[:space:]])(sponge|ex|ed|vi|vim|nvim)[[:space:]]'
INTERP_RE='(^|[[:space:]])(python3?|node|ruby|perl)[[:space:]]'
TRIG_RE='(^|[^[:alnum:]_-])(git|gh|rm|unlink|shred|trash|find|mv|cp|install|rsync|ln|ditto|sed|gsed|perl|awk|gawk|tee|xargs|patch|python3?|node|ruby|cd|pushd|dd|truncate|tar|unzip|curl|wget|sponge|ex|ed|vi|vim|touch|mkdir|rmtree|unlinkSync|rmSync)([^[:alnum:]_]|$)|>|^[[:space:](\"]*[$][{A-Za-z_]'
READONLY_LINE_RE='^[[:space:]({]*(grep|egrep|fgrep|rg|ag|ack)[[:space:]]'
CD_RE="(^|[[:space:]\"'(\`{])(cd|pushd)[[:space:]]+(.*)\$"
SEP_RE=$'[;&|`\n]'
SCRIPT_G='((^|[^/[:alnum:]])02(\\)?[[:space:]]Tervezet|(^|[^/~[:alnum:]])\.git/|(^|[^/~[:alnum:]])\.claude/|(^|[^/~[:alnum:]])\.github/|(^|[^/[:alnum:]])CLAUDE\.md|tools/approved-visible-text\.json)'
PLAIN_PUSH_RE='^git push( |$)'   # from the repo root only: a `git -C` call stays sandboxed
# gh: read-only subcommands pass; the publishing ones need the plain spelling + an ask rule;
# everything else is blocked (the user runs it).
GH_READ_RE='^gh([[:space:]]+((pr|issue)[[:space:]]+(view|list|status)|pr[[:space:]]+(diff|checks)|repo[[:space:]]+view|run[[:space:]]+(list|view|watch)|workflow[[:space:]]+(list|view)|release[[:space:]]+(list|view)|label[[:space:]]+list|gist[[:space:]]+(list|view)|search[[:space:]]+(repos|issues|prs|code|commits)|auth[[:space:]]+status|status|browse|cache[[:space:]]+list|secret[[:space:]]+list|variable[[:space:]]+list|ruleset[[:space:]]+(list|view|check)|version|help|--version|--help)([[:space:]]|$)|[[:space:]]*$)'
GH_PUBLISH_RE='^gh[[:space:]]+(pr[[:space:]]+(create|merge|close|comment|edit|review|reopen|ready)|issue[[:space:]]+(create|comment|edit|close|reopen))([[:space:]]|$)'
PLAIN_GHPR_RE='^gh (pr (create|merge|close|comment|edit|review|reopen|ready)|issue (create|comment|edit|close|reopen))( |$)'
GIT_SUBS=' status diff log show add commit branch checkout switch fetch pull merge push stash rev-parse ls-files ls-tree ls-remote cat-file blame annotate grep remote config worktree cherry-pick revert mv rm restore describe shortlog reflog tag merge-base rev-list diff-tree diff-index diff-files show-ref for-each-ref name-rev notes check-ignore check-attr var version help count-objects fsck gc rerere reset clean cherry range-diff whatchanged show-branch hash-object apply am bisect format-patch archive rebase verify-commit verify-tag '
GIT_C_OK='^(core\.quotepath|color\..+|advice\..+|user\.name|user\.email|i18n\..+|init\.defaultbranch|column\.ui|log\.date|log\.decorate)$'
TEXT_CHECKER=""   # set after REPO_ROOT; the selftest substitutes a stub
US=$'\x1f'   # placeholder for spaces inside quoted words (never part of a real path)

CWD=$REPO_ROOT; IN_REPO=1; CWD_CONTENT=0; CD_CONTENT=0; CD_REPO=0; CONTENT_CTX=0
TEXT_CHECKER="$REPO_ROOT/.git/hooks/text-name-check"
ALLOWED_ROOTS=(); GITCWD_OK=""; DQ_PASS=0

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
  if [[ $s == */git* || $s == */gh* ]]; then
    s=$(printf '%s\n' "$s" | sed -E "s#[^[:space:]\"';&|(\`]*/(git|gh)([[:space:]]|\$)#\\1\\2#g")
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

# Repository roots git may run in: this repository, plus the lines of the untracked
# `.git/info/guard-allowed-roots` (absolute, or relative to the repository root).
init_roots() {
  local f="$REPO_ROOT/.git/info/guard-allowed-roots" line r
  ALLOWED_ROOTS=("$(cd "$REPO_ROOT" 2>/dev/null && pwd -P)")
  if [[ -f $f ]]; then
    while IFS= read -r line || [[ -n $line ]]; do
      [[ -z $line || $line == \#* ]] && continue
      [[ $line == /* ]] || line="$REPO_ROOT/$line"
      r=$(cd "$line" 2>/dev/null && pwd -P) && ALLOWED_ROOTS+=("$r")
    done < "$f"
  fi
}

# in_allowed_root <dir>: the directory (absolute, ~/…, or relative to the command's cwd)
# resolves (symlinks followed) inside an allowed root.
in_allowed_root() {
  local d=$1 real r
  (( ${#ALLOWED_ROOTS[@]} )) || init_roots
  [[ $d == "~/"* ]] && d="$HOME/${d#\~/}"
  [[ $d == /* ]] || d="$CWD/$d"
  real=$(cd "$d" 2>/dev/null && pwd -P) || return 1
  for r in "${ALLOWED_ROOTS[@]}"; do
    [[ $real == "$r" || $real == "$r"/* ]] && return 0
  done
  return 1
}

# Text that goes to GitHub (title, body, --body-file contents) passes the untracked local
# name check. Fail closed: a missing checker, a body file given by variable or stdin, or an
# unreadable body file blocks. Sets REASON when it returns 1.
names_ok_for_publish() {
  local text=$1 w prev="" f
  local files=()
  if [[ -z $TEXT_CHECKER || ! -x $TEXT_CHECKER ]]; then
    REASON="a GitHubra kerülő szöveg névellenőrzője (.git/hooks/text-name-check) hiányzik — a közzétételt a felhasználó futtassa"; return 1
  fi
  while IFS= read -r w; do
    w=${w//$US/ }
    case $prev in --body-file|-F|--notes-file) files+=("$w") ;; esac
    case $w in --body-file=*|--notes-file=*) files+=("${w#*=}") ;; esac
    prev=$w
  done < <(words "$text")
  for f in ${files[@]+"${files[@]}"}; do
    if [[ $f == *'$'* || $f == - || -z $f ]]; then
      REASON="--body-file: szó szerinti fájlútvonal kell (nem változó, nem stdin)"; return 1
    fi
    [[ $f == "~/"* ]] && f="$HOME/${f#\~/}"
    [[ $f == /* ]] || f="$CWD/$f"
    if [[ ! -f $f || ! -r $f ]]; then REASON="--body-file nem olvasható: $f"; return 1; fi
    text+=$'\n'"$(cat -- "$f")"
  done
  # Also the text as bash will pass it (quote removal joins 'X'"Y" into one word).
  text+=$'\n'"$(words "$1" | tr '\n\037' '  ')"
  if ! printf '%s\n' "$text" | "$TEXT_CHECKER" >/dev/null 2>&1; then
    REASON="a GitHubra kerülő szöveg hangnevet vagy privát repónevet tartalmaz (helyi névellenőrzés)"; return 1
  fi
  return 0
}

# Sets REASON. Returns 0 = block, 3 = publishing command (plain spelling decides), 1 = pass.
# Runs in the current shell (no subshell per piece), so cd state carries to the next piece.
check_piece() {
  local p=$1 q dest w
  p=${p#"${p%%[![:space:]]*}"}
  q=" $p "

  # --- redirects into content/governance, any program ----------------------------------
  # A `>` inside a quoted string (a commit message) is not a redirect.
  local qs=$q
  if [[ $q == *'>'* && $q == *[\"\']* ]]; then
    qs=$(printf '%s\n' "$q" | sed -E -e "s/\"[^\"]*\"/Q/g" -e "s/'[^']*'/Q/g")
  fi
  if [[ $qs == *'>'* ]] && [[ $qs =~ $REDIR_RE ]]; then
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
    if [[ $p =~ ^[\"]?\$\{?[A-Za-z_][A-Za-z0-9_]*\}?[\"]?([[:space:]]|$) ]]; then
      REASON="változóból indított parancs: a hook nem látja, mi fut — írd ki a parancsot"; return 0
    fi
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

  # --- git / gh: analysed as written, and again after bash quote removal ----------------
  if [[ $p == *"\$'"* || $p == *'$"'* ]]; then
    REASON="ANSI-C (\$'…') vagy lokalizált (\$\"…\") idézés git/gh parancsban — írd ki szó szerint"; return 0
  fi
  local rc rc2 keep dq
  check_gitgh "$p"; rc=$?
  (( rc == 0 )) && return 0
  if [[ $p == *[\"\'\\]* ]]; then
    keep=$REASON
    dq=$(printf '%s\n' "$p" | tr -d "\"'\\\\")
    DQ_PASS=1; check_gitgh "$dq"; rc2=$?; DQ_PASS=0
    (( rc2 == 0 )) && return 0
    REASON=$keep
  fi
  return $rc
}

check_gitgh() {
  if [[ $1 =~ ^gh([[:space:]]|$) ]]; then check_gh "$1"; else check_git "$1"; fi
}

check_gh() {
  local p=$1 t
  t=" ${p#gh} "
  while [[ $t =~ ^(.*[[:space:]])(-R|--repo)([[:space:]]+|=)[^[:space:]]+(.*)$ ]]; do t="${BASH_REMATCH[1]}${BASH_REMATCH[4]}"; done
  t=${t# }; p="gh ${t% }"; p=${p% }
  [[ $p =~ $GH_READ_RE ]] && return 1
  if [[ $p =~ ^gh[[:space:]]+api([[:space:]]|$) ]]; then check_gh_api "$p"; return $?; fi
  if [[ $p =~ $GH_PUBLISH_RE ]]; then
    local verb="gh ${BASH_REMATCH[1]}"
    if (( ! DQ_PASS )); then names_ok_for_publish "$p" || return 0; fi
    REASON=$verb; return 3
  fi
  REASON="gh: ez a parancs nincs az engedélyezett listán (olvasó alparancsok, gh api GET, PR/issue közzététel) — a felhasználó futtassa"
  return 0
}

check_gh_api() {
  local p=" $1 " m explicit_get=0
  shopt -s nocasematch
  if [[ $p =~ [[:space:]]graphql([[:space:]]|$) ]]; then
    shopt -u nocasematch; REASON="gh api graphql blokkolt (írhat) — olvasáshoz REST GET"; return 0
  fi
  if [[ $p =~ [[:space:]]--input([[:space:]=]|$) ]]; then
    shopt -u nocasematch; REASON="gh api --input: kérés-törzs = írás — a felhasználó futtassa"; return 0
  fi
  while IFS= read -r m; do
    [[ -z $m ]] && continue
    m=${m#*-X}; m=${m#*--method}; m=${m#=}; m=${m#"${m%%[![:space:]]*}"}
    if [[ $m =~ ^(GET|HEAD)$ ]]; then explicit_get=1
    else shopt -u nocasematch; REASON="gh api -X/--method ${m:-?}: írás — a felhasználó futtassa"; return 0; fi
  done < <(printf '%s\n' "$p" | grep -oiE '(^|[[:space:]])(-X|--method)(=|[[:space:]]*)[^[:space:]]*')
  shopt -u nocasematch
  if [[ $p =~ [[:space:]](-[fF][^[:space:]]*|--field|--raw-field)([[:space:]=]|$) ]] && (( ! explicit_get )); then
    REASON="gh api mezőkkel, kifejezett -X GET nélkül = POST (írás) — a felhasználó futtassa"; return 0
  fi
  return 1
}

# git: only in an allowed root, only known subcommands, no code-executing options.
check_git() {
  local p=$1 raw=$1 sub rest w key val pos n path gitc=0 cw
  while :; do
    if [[ $p =~ ^git[[:space:]]+-C[[:space:]]*(\"[^\"]*\"|\'[^\']*\'|[^[:space:]]+)(.*)$ ]]; then
      val=${BASH_REMATCH[1]}; p="git${BASH_REMATCH[2]}"; val=${val#[\"\']}; val=${val%[\"\']}
      if [[ $val == *'$'* ]] || ! in_allowed_root "$val"; then
        REASON="git -C csak ebben a repóban (vagy a .git/info/guard-allowed-roots engedélyezett repójában) futhat: $val"; return 0
      fi
      gitc=1; continue
    fi
    if [[ $p =~ ^git[[:space:]]+-c[[:space:]]*(\"[^\"]*\"|\'[^\']*\'|[^[:space:]]+)(.*)$ ]]; then
      val=${BASH_REMATCH[1]}; p="git${BASH_REMATCH[2]}"; val=${val#[\"\']}; val=${val%[\"\']}; key=${val%%=*}
      shopt -s nocasematch
      if [[ ! $key =~ $GIT_C_OK ]]; then
        shopt -u nocasematch; REASON="git -c $key: csak ártalmatlan kulcs engedett (core.quotePath, color.*, advice.*, user.*, …) — egy -c programot is futtathat"; return 0
      fi
      shopt -u nocasematch; continue
    fi
    if [[ $p =~ ^git[[:space:]]+(--no-pager|-P|-p|--paginate|--no-optional-locks|--literal-pathspecs|--glob-pathspecs|--noglob-pathspecs|--icase-pathspecs|--no-replace-objects|--no-advice)([[:space:]].*)?$ ]]; then
      p="git${BASH_REMATCH[2]-}"; continue
    fi
    break
  done
  if [[ $p =~ ^git[[:space:]]+- ]]; then
    REASON="tiltott vagy ismeretlen git globális opció (pl. --git-dir, --work-tree, --exec-path, --attr-source, --config-env)"; return 0
  fi
  if (( ! gitc )); then
    [[ -n $GITCWD_OK ]] || { if in_allowed_root "$CWD"; then GITCWD_OK=1; else GITCWD_OK=0; fi; }
    if (( ! GITCWD_OK )); then REASON="git csak a repóban futhat (munkakönyvtár: $CWD) — egy idegen repó konfigurációja programot futtathat"; return 0; fi
  fi
  [[ $p =~ ^git[[:space:]]+([^[:space:]]+)(.*)$ ]] || return 1
  sub=${BASH_REMATCH[1]}; rest=" ${BASH_REMATCH[2]} "
  if [[ $GIT_SUBS != *" $sub "* ]]; then
    REASON="git $sub: nincs az engedélyezett git-alparancsok között — a felhasználó futtassa"; return 0
  fi
  if [[ $rest == *[\"\'\`\)]* ]]; then
    rest=$(printf '%s\n' "$rest" | sed -e "s/[\"'\`)]/ & /g")
  fi
  if [[ $rest =~ [[:space:]](--upload-pack|--receive-pack|--exec|--output|--template|--config|--pathspec-from-file)([[:space:]=]|$) ]] || [[ $rest =~ (^|[[:space:]\"\'])(ext|fd):: ]]; then
    REASON="git: programot futtató vagy fájlba író opció (--upload-pack/--exec/--output/--template/ext::) — a felhasználó futtassa"; return 0
  fi

  case $sub in
    reset)
      if has_long "$rest" hard 2 || has_long "$rest" merge 2 || has_long "$rest" keep 1; then
        REASON="a hard/merge/keep reset eldobja a nem commitolt munkát"; return 0
      fi
      local before=${rest%% -- *}
      for w in $(positionals "$before"); do
        path=${w//$US/ }
        [[ $w == HEAD ]] && continue
        [[ -e "$CWD/$path" || ( $path == /* && -e $path ) ]] && continue
        REASON="a reset <commit> átállítja a branchet (--soft/--mixed alakban is) — csak HEAD vagy létező útvonal engedett"; return 0
      done ;;
    clean)
      has_flag "$rest" f force 1 && { REASON="a kényszerített clean visszavonhatatlanul törli a nem követett fájlokat"; return 0; } ;;
    checkout)
      [[ $rest =~ [[:space:]]--[[:space:]] ]] && { REASON="checkout -- <path> eldobja a working tree változtatásait"; return 0; }
      has_flag "$rest" f force 1 && { REASON="a kényszerített checkout eldobja a working tree változtatásait"; return 0; }
      [[ $rest =~ [[:space:]]-B[[:space:]] ]] && { REASON="checkout -B felülír egy meglévő branch-et"; return 0; }
      has_long "$rest" theirs 2 && { REASON="checkout --theirs <path> felülírja a fájlt"; return 0; }
      has_long "$rest" ours 2 && { REASON="checkout --ours <path> felülírja a fájlt"; return 0; }
      if [[ ! $rest =~ [[:space:]](-b|--orphan|-t|--track)[[:space:]] ]]; then
        n=0
        for w in $(positionals "$rest"); do
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
      has_long "$rest" discard-changes 2 && { REASON="a switch --discard-changes eldobja a working tree változtatásait"; return 0; } ;;
    restore)
      local staged=0 worktree=0
      if has_long "$rest" staged 2 || [[ $rest =~ [[:space:]]-[a-zA-Z]*S[a-zA-Z]*([[:space:]]|$) ]]; then staged=1; fi
      if has_long "$rest" worktree 1 || [[ $rest =~ [[:space:]]-[a-zA-Z]*W[a-zA-Z]*([[:space:]]|$) ]]; then worktree=1; fi
      if (( ! staged || worktree )); then REASON="a restore eldobja a working tree változtatásait (csak --staged engedett)"; return 0; fi ;;
    push)
      if has_flag "$rest" f force 2 || has_long "$rest" force-with-lease 7 || has_long "$rest" force-if-includes 7 || \
         has_flag "$rest" d delete 2 || has_long "$rest" mirror 1 || has_long "$rest" prune 3 || has_long "$rest" all 2 || \
         [[ $rest =~ [[:space:]][+:][^[:space:]] ]]; then
        REASON="a kényszerített, törlő vagy tömeges push átírhatja a távoli historyt"; return 0
      fi
      has_long "$rest" no-verify 4 && { REASON="push --no-verify átugorja a helyi pre-push névellenőrzést"; return 0; }
      REASON="git push"; return 3 ;;
    fetch|pull|ls-remote)
      if [[ $sub != pull ]] && has_flag "$rest" u update-head-ok 3; then
        REASON="git $sub -u: programot futtat vagy a lokális branchet írja"; return 0
      fi
      for w in $(positionals "$rest"); do
        [[ $w == *:* ]] || continue
        val=${w#*:}; val=${val//$US/ }
        [[ -z $val || $val == refs/remotes/* || $val == refs/tags/* ]] && continue
        REASON="fetch helyi branchbe (refspec: $w) felülírhatja a lokális branchet"; return 0
      done
      if [[ $sub == pull ]]; then
        if { has_long "$rest" rebase 3 && [[ ! $rest =~ --rebase=(false|no) ]]; } || [[ $rest =~ [[:space:]]-[a-zA-Z]*r[a-zA-Z]*([[:space:]]|$) ]]; then
          REASON="a pull --rebase átírja a lokális historyt"; return 0
        fi
      fi ;;
    config)
      cw=" $(positionals "$rest")"
      if [[ $rest =~ [[:space:]](--add|--unset|--unset-all|--replace-all|--rename-section|--remove-section|-e|--edit|--file|-f|--blob|--global|--system|--worktree|--type)([[:space:]=]|$) ]]; then
        REASON="git config írás vagy más fájl: csak olvasás, vagy a helyi user.name/user.email beállítása engedett"; return 0
      fi
      [[ $rest =~ [[:space:]](--get|--get-all|--get-regexp|--get-urlmatch|-l|--list)([[:space:]]|$) ]] && return 1
      [[ $cw =~ ^[[:space:]]*(get|list)([[:space:]]|$) ]] && return 1
      [[ $cw =~ ^[[:space:]]*[^[:space:]]+[[:space:]]*$ ]] && return 1
      if [[ $cw =~ ^[[:space:]]*([^[:space:]]+)[[:space:]]+[^[:space:]] ]]; then
        key=${BASH_REMATCH[1]}
        shopt -s nocasematch
        if [[ $key =~ ^user\.(name|email)$ ]]; then shopt -u nocasematch; return 1; fi
        shopt -u nocasematch
      fi
      REASON="git config írás: csak olvasás, vagy a helyi user.name/user.email beállítása engedett"; return 0 ;;
    rebase)
      [[ $rest =~ ^[[:space:]]*--abort[[:space:]\"\'\`\)]*$ ]] || { REASON="a rebase átírja a lokális historyt (a repo szabálya tiltja)"; return 0; } ;;
    commit)
      has_long "$rest" amend 2 && { REASON="az amend felülírja a felhasználó checkpoint-commitját"; return 0; } ;;
    reflog) [[ $rest =~ ^[[:space:]]*(delete|expire) ]] && { REASON="a reflog törlése megszünteti az utolsó visszaállítási esélyt"; return 0; } ;;
    gc) has_long "$rest" prune 1 && { REASON="a prune végleg törli az elérhetetlen objektumokat"; return 0; } ;;
    stash) [[ $rest =~ ^[[:space:]]*(drop|clear) ]] && { REASON="a stash törlése végleges"; return 0; } ;;
    branch)
      [[ $rest =~ [[:space:]]-[a-zA-Z]*[DMC][a-zA-Z]*([[:space:]]|$) ]] && { REASON="branch kényszerített törlése/átnevezése/másolása pusholatlan commitokat veszíthet"; return 0; }
      has_flag "$rest" f force 2 && { REASON="a kényszerített branch felülír egy meglévő branch-et"; return 0; } ;;
    tag)
      if has_flag "$rest" d delete 1 || has_flag "$rest" f force 1; then REASON="tag törlése vagy felülírása"; return 0; fi ;;
    worktree)
      if [[ $rest =~ ^[[:space:]]*remove ]] && has_flag "$rest" f force 1; then REASON="worktree kényszerített eltávolítása eldobja a benne lévő munkát"; return 0; fi
      if [[ $rest =~ ^[[:space:]]*add[[:space:]] ]]; then
        pos=$(positionals "${rest#*add}"); path=${pos%% *}; path=${path//$US/ }
        [[ $path == /* ]] || path="$CWD/$path"
        local parent; parent=$(cd "$(dirname "$path")" 2>/dev/null && pwd -P)
        if [[ -z $parent || $parent == "${ALLOWED_ROOTS[0]:-$REPO_ROOT}" || $parent == "${ALLOWED_ROOTS[0]:-$REPO_ROOT}"/* ]]; then
          REASON="worktree a repón belül (vagy nem feloldható helyen): a repó fájljait sandboxon kívül írná"; return 0
        fi
      fi ;;
    notes) [[ $rest =~ ^[[:space:]]*((list|show)([[:space:]]|$)|$) ]] || { REASON="git notes írás"; return 0; } ;;
    remote) [[ $rest =~ ^[[:space:]]*((-v|--verbose)[[:space:]]*)?((show|get-url)([[:space:]]|$)|$) ]] || { REASON="git remote módosítása"; return 0; } ;;
    grep) [[ $rest =~ [[:space:]](-O[^[:space:]]*|--open-files-in-pager)([[:space:]=]|$) ]] && { REASON="git grep -O programot futtat"; return 0; } ;;
    format-patch) [[ $rest =~ [[:space:]]--stdout([[:space:]]|$) ]] || { REASON="format-patch fájlokat ír sandboxon kívül — csak --stdout"; return 0; } ;;
    archive) [[ $rest =~ [[:space:]](-o[^[:space:]]*|--remote)([[:space:]=]|$) ]] && { REASON="git archive fájlba ír vagy távoli programot futtat"; return 0; } ;;
    bisect) [[ $rest =~ ^[[:space:]]*run([[:space:]]|$) ]] && { REASON="git bisect run programot futtat sandboxon kívül"; return 0; } ;;
    apply)
      [[ $rest =~ [[:space:]]--(check|stat|numstat|summary)([[:space:]]|$) ]] && return 1
      REASON="git apply: patch-alkalmazás — a tananyag csak Edit/Write eszközzel változhat"; return 0 ;;
    am) REASON="git am: patch-alkalmazás — a tananyag csak Edit/Write eszközzel változhat"; return 0 ;;
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
  CWD=$cwd; IN_REPO=0; CWD_CONTENT=0; CD_CONTENT=0; CD_REPO=0; CONTENT_CTX=0; GITCWD_OK=""; DQ_PASS=0
  [[ $cwd == "$REPO_ROOT" || $cwd == "$REPO_ROOT"/* ]] && IN_REPO=1
  [[ $cwd == "$REPO_ROOT/02 Tervezet" || $cwd == "$REPO_ROOT/02 Tervezet"/* ]] && CWD_CONTENT=1
  [[ $text =~ $CONTENT_RE ]] && CONTENT_CTX=1
  # Inline scripts span separators, so check them whole for a write whose literal target is a
  # content/governance path (a computed target is the sandbox's job).
  if [[ $text =~ $INTERP_RE ]]; then
    local G=$SCRIPT_G st
    st=$(relpaths "$text")
    if [[ $st =~ open\([^\)]*${G}[^\)]*,[[:space:]]*(mode[[:space:]]*=[[:space:]]*)?[\"\'][wax] ]] || \
       [[ $st =~ open\([^\(\)]*\([^\(\)]*${G}[^\(\)]*\)[^\(\)]*,[[:space:]]*(mode[[:space:]]*=[[:space:]]*)?[\"\'][wax] ]] || \
       [[ $st =~ Path\([^\)]*${G}[^\)]*\)\.(write_text|write_bytes|open\([\"\'][wax]) ]] || \
       [[ $st =~ (writeFileSync|appendFileSync|writeFile|appendFile|copyFileSync|createWriteStream|renameSync)\([^\)]*${G} ]] || \
       [[ $st =~ (shutil\.(copy|copy2|copyfile|move|copytree)|os\.(replace|rename))\([^\)]*,[[:space:]]*[^\)]*${G} ]] || \
       [[ $st =~ open\([[:space:]]*[A-Za-z_]+[[:space:]]*,[[:space:]]*[\"\'][\>+]*[[:space:]]*${G} ]]; then
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
    echo "$pub csak egyszerű, önálló alakban, egyszeres szóközökkel futhat (pl. \`git push origin <branch>\`, \`gh pr merge <n>\`; hosszabb szöveg \`--body-file\`-lal) — így a jóváhagyó kérdés minden módban megjelenik"; return 0
  fi
  return 1
}

if [[ "${1:-}" == "--selftest" ]]; then
  fail=0
  [[ -n ${GUARD_REPO_ROOT:-} ]] && { REPO_ROOT=$GUARD_REPO_ROOT; REPO_BASE=${REPO_ROOT##*/}; }
  # Corpus assembled from parts so this file's own text does not read as runnable.
  G="git"; R="rm"; H="gh"; T="02 Tervezet"; PT="02 Tervezet/Program terv.md"; UT="tools/content_integrity.py"
  # The name check runs against a stub (the real checker is local and private): it rejects
  # the marker ZZNAMEZZ, so the publishing path is tested on every machine, CI included.
  ST=$(mktemp -d "${TMPDIR:-/tmp}/guard-selftest.XXXXXX") || exit 1
  trap 'rm -rf -- "$ST"' EXIT
  printf '#!/bin/sh\n! grep -q ZZNAMEZZ\n' > "$ST/checker"; chmod +x "$ST/checker"; TEXT_CHECKER="$ST/checker"
  printf 'clean body\n' > "$ST/clean.md"; printf 'has ZZNAMEZZ inside\n' > "$ST/named.md"
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
    "cat /tmp/x > \"$REPO_ROOT/$T/x.md\"" "printf x | tee \"$T/x.md\"" "cp /tmp/x \"$T/x.md\"" "mv /tmp/x \"$T/Modulok/x.md\""
    "install /tmp/x \"$T/x.md\"" "rsync -a /tmp/x/ \"$T/\"" "rsync -a --delete /tmp/x/ ./" "cp -R /tmp/x/. ."
    "$G show HEAD:\"$T/x.md\" > \"$T/x.md\"" "patch -p1 < /tmp/p.diff" "dd if=/tmp/x of=\"$T/x.md\"" "truncate -s 0 \"$T/x.md\""
    "python3 tools/audit_import.py /tmp/r.md x.md > \"$T/x.md\""
    "python3 -c \"import pathlib; pathlib.Path('$T/x.md').write_text('x')\"" "x=$G; \$x reset --soft HEAD~3" "\"\$GIT\" status"
    "printf 0123 > .git/refs/heads/main" ": > .git/logs/HEAD" "/opt/homebrew/opt/git/libexec/git-core/$G reset --hard"
    "$H pr create --title x --body 'ZZ''NAME''ZZ'" "$H pr create --title x --body \"ZZ\"NAMEZZ"
    "python3 -c \"open('$T/x.md','wb').write(b'x')\"" "python3 -c \"import shutil; shutil.copy('/tmp/x','$T/x.md')\""
    "python3 -c \"import os; os.replace('/tmp/x', os.path.join('$T','x.md'))\"" "node -e \"require('fs').writeFileSync('$T/x.md','x')\""
    "node -e \"require('fs').createWriteStream('$T/x.md').write('x')\"" "perl -e 'open(F,\">$T/x.md\"); print F 1'"
    "echo '{\"disableAllHooks\":true}' > .claude/settings.local.json" "cp /tmp/x CLAUDE.md" "sed -i '' 's/a/b/' .github/workflows/content-integrity.yml"
    "echo '{}' > tools/approved-visible-text.json" "ex -sc '%s/a/b/|x' \"$T/x.md\"" "vim -c 'wq' \"$T/x.md\""
    "python3 -c \"import os; open(os.path.join('$T','M.md'),'w').write('x')\""
    # git/gh outside the sandbox: code execution, file writes, quoting tricks (verifier 2026-10-03)
    "$G -c core.fsmonitor='sh x.sh' status" "$G -c core.sshCommand=x fetch" "$G -c protocol.ext.allow=always ls-remote 'ext::sh -c x'"
    "$G -c core.hooksPath=/tmp/h commit -m x" "$G config core.fsmonitor x" "$G config include.path /tmp/x" "$G config clean.requireForce false"
    "$G config --global user.name x" "$G clone -u x file:///tmp/r" "$G clone https://e.x/r.git" "$G init /tmp/x" "$G ls-remote --exec=x origin"
    "$G ls-remote -u x origin" "$G push --exec=x origin" "$G diff --output=CLAUDE.md HEAD~1" "$G log -p --output=x.md" "$G merge-file CLAUDE.md a b"
    "$G r\"eset\" --hard HEAD~3" "$G res'et' --hard" "$G \$'reset' --hard" "$G reset -\"-hard\"" "$G --attr-source=HEAD reset --hard"
    "$G reset HEAD@{1}" "$G reset main~2" "$G reset -q feature-x" "$G reset abc123" "$G read-tree -mu HEAD~1" "$G symbolic-ref HEAD refs/heads/x"
    "$G replace a b" "$G update-index --assume-unchanged x" "$G submodule foreach ls" "$G bisect run make" "$G grep -Oless x" "$G difftool"
    "$G format-patch -1" "$G archive -o x.zip HEAD" "$G tag -d v1" "$G branch -Dq x" "$G remote add evil https://e.x" "$G notes add -m x"
    "$G worktree add \"$T/wt\" main" "$G worktree add ./wt main" "$G -C /tmp/x status" "$G --exec-path=/tmp/x status"
    "$G push origin '+'main" "$G push origin \\+main" "$G push '-'f origin main" "$G push origin ':'old" "$G push -'-no-verify' origin main"
    "$G push --all origin" "$G  push origin x" "$H pr  merge 1" "$G -C $REPO_ROOT push origin main"
    "echo x > tools/evil.py" "printf x > .gitattributes" "cp /tmp/x tools/csv.py"
    "$H pr new" "$H issue new" "$H release new" "$H gist new" "$H repo new x" "$H pr update-branch 1" "$H pr revert 1" "$H pr checkout 1"
    "$H repo unarchive x" "$H repo deploy-key add k" "$H project create" "$H alias set --shell x 'ls'" "$H extension install x/y"
    "$H run download 1" "$H release download v1" "$H repo clone x" "$H workflow run x.yml" "$H secret set X" "$H release create v1"
    "$H api -X 'DELETE' repos/o/r/git/refs/heads/x" "$H api --method=\"DELETE\" repos/o/r/x" "$H api -XPOST repos/o/r/issues"
    "$H api repos/o/r/issues -ftitle=x" "$H api graphql --input q.json" "$H api graphql -f query='query{viewer{login}}'" "$H api --input b.json repos/o/r/x"
    "$H pr create --title ZZNAMEZZ --body y" "$H pr create --title x --body-file $ST/named.md" "$H pr comment 1 -F $ST/named.md"
    "$H pr create --title x --body-file \"\$TMPDIR/b.md\"" "$H pr create --title x --body-file -" "$H pr create --title x --body-file /nonexistent/b.md"
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
    "$G rebase --abort" "$G merge --abort" "$G cherry-pick --abort" "$G revert --abort" "$G -C \"$REPO_ROOT\" rebase --abort"
    "$G status && $G rebase --abort" "$G merge main" "$G revert HEAD" "$G worktree add ../wt-x feature"
    "$G rebase --abort;" "$G rebase --abort && $G status" "cd /repo && $G rebase --abort"
    "$G rebase --abort; echo done" "$G merge --abort;" "$G cherry-pick --abort && $G status"
    "$G push origin main" "$G push -u origin HEAD" "$G push" "$H pr merge 1 --merge" "$H pr close 3 --delete-branch"
    "python3 tools/content_integrity.py" "python3 tools/content_integrity.py --release-report" "python3 tools/media_manifest.py build"
    "python3 tools/test_media_manifest.py --pin-visible \"CF-01: x\"" "python3 tools/test_media_manifest.py --pin-visible \"CF-01: a -> $T\""
    "python3 tools/audit_import.py /private/tmp/claude-501/x/scratchpad/r.md \"2026-10-10 Validált findingok – x.md\""
    "python3 tools/audit_import.py \"\$TMPDIR/r.md\" \"x.md\" --replace-untracked"
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
    "$G reset" "$G reset -- $T/x.md" "$G reset HEAD CLAUDE.md" "$G -C \"$REPO_ROOT\" status" "$H pr view 12" "$H pr list --state all"
    "$H api repos/o/r/git/refs/heads/main" "$H api -X GET search/issues -f q=x"
    "$G mv \"$T/a.md\" \"$T/b.md\"" "node --test test/x.test.mjs" "$H pr create --title x --body y"
    "$H pr create --title x --body-file $ST/clean.md" "$H pr comment 1 -F $ST/clean.md" "$H issue create --title x --body y" "$H secret list" "$H run view 9" "$H issue list"
    "vim --version" "printf '%s\\n' a b" "echo 'a\\tb'"
    "$G fetch origin main:refs/remotes/origin/main" "$G tag v1" "$G remote -v" "$G remote get-url origin" "$G ls-remote origin"
    "$G config --list" "$G config get user.name" "$G notes list" "$G format-patch -1 --stdout" "$G grep -n x" "$H" "$H --version"
    "$G commit -m \"a 'b' c\"" "$G log --format='%h %s'" "$G -c core.quotePath=false status" "$G -c color.ui=always log -1"
    "$G --no-pager log -1" "$G worktree add ../wt-y main" "$G bisect start" "$H pr checks 3" "$H run list" "$H api -X GET repos/o/r"
    "mkdir -p \"/tmp/claude-501/02 Tervezet copy\"" "tar -czf /tmp/claude-501/b.tgz \"$T\"" "$G commit -m \"fix: x > CLAUDE.md\""
    "printf x > \"/tmp/claude-501/$T notes.txt\"" "python3 -c \"import shutil,os; s='CLAUDE.md'; d=os.environ['TMPDIR']+'/c'; shutil.copy(s,d)\""
    "cat .git/HEAD > /tmp/claude-501/h.txt"
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
  # git from a foreign working directory: a planted repo's config could run a program.
  if r=$(verdict "$G status" /tmp); then echo "BLOCK ok   [cwd /tmp] $G status ($r)"; else echo "MISS  FAIL [cwd /tmp] $G status"; fail=1; fi
  if r=$(verdict "$G -C \"$REPO_ROOT\" status" /tmp); then echo "PASS  FAIL [cwd /tmp] $G -C <repo> status ($r)"; fail=1
  else echo "PASS  ok   [cwd /tmp] $G -C <repo> status"; fi
  big=$(printf 'x%.0s' $(seq 1 $((MAX_LEN + 10))))
  if r=$(verdict "echo $big"); then echo "BLOCK ok   [túl hosszú parancs]"; else echo "MISS  FAIL [túl hosszú parancs]"; fail=1; fi
  # The real stdin path (JSON parse, background analysis, watchdog, exit code), end to end.
  for pair in "2|$G reset --hard" "0|$G status" "2|$R -rf ."; do
    want=${pair%%|*}; c=${pair#*|}
    printf '{"tool_input":{"command":"%s"},"cwd":"%s"}' "$c" "$REPO_ROOT" | bash "${BASH_SOURCE[0]}" >/dev/null 2>&1; got=$?
    if [[ $got == "$want" ]]; then echo "STDIN ok   exit=$got  $c"; else echo "STDIN FAIL exit=$got (want $want)  $c"; fail=1; fi
  done
  printf '{"tool_input": {"command": "%s"' "$G status" | bash "${BASH_SOURCE[0]}" >/dev/null 2>&1; got=$?
  if [[ $got == 2 ]]; then echo "STDIN ok   exit=2  [nem értelmezhető JSON]"; else echo "STDIN FAIL exit=$got [nem értelmezhető JSON]"; fail=1; fi
  echo "--- ${#must_block[@]} must-block (+5 cwd tananyag/túl hosszú, +$(( ${#OUT[@]} + 1 )) cwd /tmp), ${#must_pass[@]} must-pass (+1 cwd /tmp), 4 stdin ---"
  [[ $fail -eq 0 ]] && echo "--- selftest OK ---" || echo "--- selftest FAILED ---"
  exit $fail
fi

payload=$(cat)
[[ $payload =~ ^[[:space:]]*$ ]] && exit 0
command_text=""; cwd=""; parsed=1
if command -v jq >/dev/null 2>&1; then
  command_text=$(printf '%s' "$payload" | jq -er '(.tool_input.command // .tool_input.cmd // "") | strings' 2>/dev/null) || parsed=0
  cwd=$(printf '%s' "$payload" | jq -er '.cwd // "" | tostring' 2>/dev/null) || parsed=0
elif command -v python3 >/dev/null 2>&1; then
  command_text=$(printf '%s' "$payload" | python3 -c \
    'import json,sys; d=json.load(sys.stdin); t=d.get("tool_input") or {}; c=t.get("command") or t.get("cmd") or ""; sys.exit(1) if not isinstance(c,str) else print(c)' 2>/dev/null) || parsed=0
  cwd=$(printf '%s' "$payload" | python3 -c 'import json,sys; print(json.load(sys.stdin).get("cwd") or "")' 2>/dev/null) || parsed=0
else
  # No JSON parser: fail closed by scanning the raw payload rather than waving it through.
  command_text="$payload"
fi
if (( ! parsed )); then
  echo "BLOKKOLVA (.claude/hooks/guard-repo-safety.sh): a hook bemenete nem értelmezhető JSON — fail closed" >&2; exit 2
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
