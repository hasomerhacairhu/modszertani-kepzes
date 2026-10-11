#!/usr/bin/env python3
"""Kész audit-fájl bemásolása az ideiglenes munkaterületről az `01 Fejlesztés/04 Audit/` mappába.

MIÉRT
-----
A Bash sandbox az egész repót írásvédetté teszi (CLAUDE.md „Git-biztonság”), a Write/Edit eszköz pedig
nagy, kész fájlt csak újragenerálva tud beírni: lassú, és a szöveg elcsúszhat. Ez az egyetlen,
sandboxon kívül futó másolóút (`.claude/settings.json` `sandbox.excludedCommands`), ezért a határait
maga az eszköz kényszeríti ki:

- forrás: csak sima (nem szimbolikus linkes) `.md` fájl a munkamenet ideiglenes területén
  (`$TMPDIR`, illetve `/private/tmp/claude-<uid>/`), legfeljebb 16 MB, UTF-8, NUL-bájt nélkül;
- cél: csak egy fájlnév (útelválasztó és `..` nélkül, `.md` végű), mindig az `01 Fejlesztés/04 Audit/`
  mappába — tananyagba (`02 Tervezet/`), governance-fájlba vagy a `.git`-be nem ír;
- git által követett fájlt nem ír felül; nem követett, már létező fájlt csak `--replace-untracked`
  mellett;
- írás előtt a tartalom átmegy a helyi névellenőrzőn (`.git/hooks/text-name-check`): ha hiányzik vagy
  bukik, nincs írás (fail closed);
- atomikus írás, majd visszaolvasás és SHA-256-összevetés.

A bemásolt fájl audit trail: commit, push és PR továbbra is csak kifejezett kérésre. Utána a szokásos
ellenőrzés: `python3 tools/content_integrity.py`.

Használat:
    python3 tools/audit_import.py <forrás.md> "<célfájl neve.md>" [--replace-untracked]
"""
import hashlib
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
AUDIT = REPO / '01 Fejlesztés' / '04 Audit'
NAME_CHECK = REPO / '.git' / 'hooks' / 'text-name-check'
MAX_BYTES = 16 * 1024 * 1024


def fail(msg):
    print(f'audit_import: {msg} — nincs írás.', file=sys.stderr)
    sys.exit(2)


def allowed_roots():
    roots = [Path(f'/private/tmp/claude-{os.getuid()}'), Path(tempfile.gettempdir())]
    if os.environ.get('TMPDIR'):
        roots.append(Path(os.environ['TMPDIR']))
    return [r.resolve() for r in roots if r.exists()]


def check_source(arg):
    p = Path(arg)
    if p.is_symlink() or not p.is_file():
        fail(f'a forrás nem sima fájl: {arg}')
    rp = p.resolve()
    if rp.suffix != '.md':
        fail('a forrás nem .md fájl')
    if not any(rp.is_relative_to(r) for r in allowed_roots()):
        fail('a forrás nem a munkamenet ideiglenes területén van ($TMPDIR vagy /private/tmp/claude-<uid>/)')
    if rp.is_relative_to(REPO):
        fail('a forrás a repón belül van')
    data = rp.read_bytes()
    if len(data) > MAX_BYTES:
        fail('a forrás nagyobb 16 MB-nál')
    if b'\0' in data:
        fail('a forrás NUL-bájtot tartalmaz')
    try:
        data.decode('utf-8')
    except UnicodeDecodeError:
        fail('a forrás nem érvényes UTF-8')
    return data


def check_target(name, replace_untracked):
    if (not name or '/' in name or '\\' in name or name.startswith('.') or not name.endswith('.md')
            or any(ord(c) < 32 for c in name) or len(name.encode()) > 240):
        fail(f'érvénytelen célfájlnév (csak fájlnév, .md végű, útelválasztó nélkül): {name!r}')
    if not (REPO / '02 Tervezet').is_dir() or AUDIT.is_symlink() or not AUDIT.is_dir():
        fail('az auditmappa nem található, vagy szimbolikus link')
    target = AUDIT / name
    if target.is_symlink():
        fail('a cél szimbolikus link')
    if target.exists():
        rel = target.relative_to(REPO).as_posix()
        tracked = subprocess.run(['git', '-C', str(REPO), 'ls-files', '--error-unmatch', '--', rel],
                                 capture_output=True).returncode == 0
        if tracked:
            fail(f'a cél git által követett fájl, nem írom felül: {rel}')
        if not replace_untracked:
            fail(f'a cél már létezik (nem követett); felülíráshoz: --replace-untracked: {rel}')
    return target


def name_check(data):
    if not os.access(NAME_CHECK, os.X_OK):
        fail('a névellenőrző (.git/hooks/text-name-check) hiányzik')
    r = subprocess.run([str(NAME_CHECK)], input=data, capture_output=True)
    if r.returncode != 0:
        fail('a névellenőrző elutasította a tartalmat: ' + r.stderr.decode('utf-8', 'replace').strip()[:500])


def main(argv):
    args = [a for a in argv if a != '--replace-untracked']
    if len(args) != 2 or any(a.startswith('--') for a in args):
        print(__doc__.split('Használat:')[1].strip(), file=sys.stderr)
        sys.exit(2)
    data = check_source(args[0])
    target = check_target(args[1], '--replace-untracked' in argv)
    name_check(data)
    try:
        fd, tmp = tempfile.mkstemp(dir=AUDIT, prefix='.audit_import-', suffix='.tmp')
    except PermissionError:
        fail('a sandbox nem engedi az írást: a parancs csak önállóan, `python3 tools/audit_import.py …` '
             'alakban fut sandboxon kívül (átirányítás, `cd`, `;` vagy `|` nélkül)')
    try:
        with os.fdopen(fd, 'wb') as f:
            f.write(data)
            f.flush()
            os.fsync(f.fileno())
        os.chmod(tmp, 0o644)
        os.replace(tmp, target)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)
    if hashlib.sha256(target.read_bytes()).digest() != hashlib.sha256(data).digest():
        print('audit_import: a visszaolvasott fájl eltér a forrástól!', file=sys.stderr)
        sys.exit(1)
    lines = data.count(b'\n')
    print(f'kész: {target.relative_to(REPO).as_posix()} — {len(data)} bájt, {lines} sor, '
          f'sha256 {hashlib.sha256(data).hexdigest()[:16]}. Következő: python3 tools/content_integrity.py')


if __name__ == '__main__':
    main(sys.argv[1:])
