#!/usr/bin/env python3
"""Structure, terminal-state and next-step check for the /course-autopilot ledger.

The ledger (`01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md`) is the single durable state of an
autopilot run: one table for the run, one per module, one for external gates and one for
findings. The format and the state machine are described in
`.claude/skills/course-autopilot/ledger.md`. This tool never writes; the main session edits
the ledger with the Edit tool.

    python3 tools/autopilot_ledger.py validate   # structure only (CI)
    python3 tools/autopilot_ledger.py check      # exit 0 only in a verified terminal state
    python3 tools/autopilot_ledger.py next       # the next resumable action
    python3 tools/autopilot_ledger.py --selftest

`check` also runs live checks instead of trusting the ledger's own claims: the final-QA commit
exists, `02 Tervezet/` and `tools/` are unchanged since it, and `content_integrity.py` passes.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
AUDIT = ROOT / '01 Fejlesztés' / '04 Audit'
LEDGER = AUDIT / 'AUTOPILOT-LEDGER.md'

RUN_KEYS = ('Run-ID', 'Állapot', 'Scope', 'Lencsék', 'Felhatalmazás', 'Munkaág',
            'Bázis-commit', 'Indítva', 'Záró QA')
RUN_STATES = ('NONE', 'ACTIVE', 'FINISHED')
MODULE_COLS = ('Modul', 'Review', 'Riport', 'Review-bázis', 'Javítás', 'Bizonyíték',
               'Következő lépés')
REVIEW_OPEN, REVIEW_DONE = ('PENDING', 'REVIEWING', 'RAW_SAVED'), ('VERIFIED', 'REUSED', 'SKIPPED')
FIX_OPEN, FIX_DONE = ('PENDING', 'FIXING'), ('DONE', 'NONE_NEEDED', 'NOT_AUTHORIZED')
GATE_COLS = ('Kulcs', 'Típus', 'Tétel', 'Kell (mit, kitől)', 'Állapot')
GATE_TYPES = ('PRECONDITION', 'HUMAN_DECISION', 'EVIDENCE_GATE', 'RUNTIME', 'SIGNOFF')
GATE_STATES = ('OPEN', 'RESOLVED')
FINDING_COLS = ('Kulcs', 'Súly', 'Típus', 'Verdikt', 'Állapot', 'Bizonyíték / döntési igény')
SEVERITIES = ('P0', 'P1', 'P2', 'P3')
FINDING_TYPES = ('objektív', 'emberi-döntés', 'bizonyíték-kapu')
VERDICTS = ('—', 'MEGERŐSÍTVE', 'ELVETVE', 'EMBERI DÖNTÉS')
FINDING_OPEN = ('OPEN', 'IN_PROGRESS', 'NEEDS_RECHECK')
FINDING_DONE = ('FIXED', 'ALREADY_FIXED', 'REJECTED', 'DUPLICATE', 'BLOCKED_HUMAN',
                'EVIDENCE_GATE', 'OWNER_DEFERRED', 'NOT_AUTHORIZED')
SECTIONS = ('Futás', 'Modulok', 'Külső kapuk', 'Findingok')
SHA_RE = re.compile(r'(?<![0-9a-f])[0-9a-f]{7,40}(?![0-9a-f])')
EMPTY = ('', '—', '-')


def parse(text: str) -> tuple[dict[str, list[list[str]]], list[str]]:
    """Section name → table rows (header first), and structural errors."""
    tables: dict[str, list[list[str]]] = {}
    errors: list[str] = []
    section = None
    for n, line in enumerate(text.splitlines(), 1):
        if line.startswith('## '):
            section = line[3:].strip()
            continue
        if section not in SECTIONS or not line.startswith('|'):
            continue
        cells = [c.strip().replace('\\|', '|')
                 for c in line.replace('\\|', '\x00').strip().strip('|').split('|')]
        cells = [c.replace('\x00', '|') for c in cells]
        if all(re.fullmatch(r':?-{3,}:?', c) for c in cells):
            continue
        rows = tables.setdefault(section, [])
        if rows and len(cells) != len(rows[0]):
            errors.append(f'{n}. sor ({section}): {len(cells)} cella, a fejléc {len(rows[0])}')
            continue
        rows.append(cells)
    for name in SECTIONS:
        if name not in tables:
            errors.append(f'hiányzó szakasz vagy táblázat: ## {name}')
    return tables, errors


def as_dicts(rows: list[list[str]], cols: tuple[str, ...], where: str, errors: list[str]):
    if not rows:
        return []
    if tuple(rows[0]) != cols:
        errors.append(f'{where}: a fejléc legyen | {" | ".join(cols)} |')
        return []
    return [dict(zip(cols, r)) for r in rows[1:]]


def load(text: str):
    tables, errors = parse(text)
    run_rows = tables.get('Futás', [])
    run = {}
    if run_rows:
        if tuple(run_rows[0]) != ('Kulcs', 'Érték'):
            errors.append('Futás: a fejléc legyen | Kulcs | Érték |')
        run = {r[0]: r[1] for r in run_rows[1:] if len(r) == 2}
    modules = as_dicts(tables.get('Modulok', []), MODULE_COLS, 'Modulok', errors)
    gates = as_dicts(tables.get('Külső kapuk', []), GATE_COLS, 'Külső kapuk', errors)
    findings = as_dicts(tables.get('Findingok', []), FINDING_COLS, 'Findingok', errors)
    return run, modules, gates, findings, errors


def structure_errors(run, modules, gates, findings) -> list[str]:
    errors = [f'Futás: hiányzó kulcs: {k}' for k in RUN_KEYS if k not in run]
    if run.get('Állapot') not in RUN_STATES:
        errors.append(f'Futás/Állapot: {run.get("Állapot")!r} — megengedett: {", ".join(RUN_STATES)}')
    names = [m['Modul'] for m in modules]
    errors += [f'Modulok: duplikált modul {n}' for n in sorted({n for n in names if names.count(n) > 1})]
    for m in modules:
        if m['Review'] not in REVIEW_OPEN + REVIEW_DONE:
            errors.append(f'{m["Modul"]}: ismeretlen Review-állapot {m["Review"]!r}')
        if m['Javítás'] not in FIX_OPEN + FIX_DONE:
            errors.append(f'{m["Modul"]}: ismeretlen Javítás-állapot {m["Javítás"]!r}')
    keys = [g['Kulcs'] for g in gates] + [f['Kulcs'] for f in findings]
    errors += [f'duplikált kulcs: {k}' for k in sorted({k for k in keys if keys.count(k) > 1})]
    for g in gates:
        if g['Típus'] not in GATE_TYPES:
            errors.append(f'{g["Kulcs"]}: ismeretlen kapu-típus {g["Típus"]!r}')
        if g['Állapot'] not in GATE_STATES:
            errors.append(f'{g["Kulcs"]}: ismeretlen kapu-állapot {g["Állapot"]!r}')
    for f in findings:
        k = f['Kulcs']
        if ':' not in k or k.split(':', 1)[0] not in names:
            errors.append(f'{k}: a kulcs alakja <Modul>:<ID>, és a modul szerepeljen a Modulok táblában')
        if f['Súly'] not in SEVERITIES:
            errors.append(f'{k}: ismeretlen súlyosság {f["Súly"]!r}')
        if f['Típus'] not in FINDING_TYPES:
            errors.append(f'{k}: ismeretlen típus {f["Típus"]!r}')
        if f['Verdikt'] not in VERDICTS:
            errors.append(f'{k}: ismeretlen verdikt {f["Verdikt"]!r}')
        if f['Állapot'] not in FINDING_OPEN + FINDING_DONE:
            errors.append(f'{k}: ismeretlen állapot {f["Állapot"]!r}')
    return errors


def finding_terminal_errors(f: dict, keys: set[str]) -> list[str]:
    k, state, ev = f['Kulcs'], f['Állapot'], f['Bizonyíték / döntési igény']
    if state in FINDING_OPEN:
        return [f'{k}: nem lezárt ({state})']
    if ev in EMPTY:
        return [f'{k}: {state} bizonyíték nélkül']
    if state in ('FIXED', 'ALREADY_FIXED'):
        if f['Verdikt'] != 'MEGERŐSÍTVE' or f['Típus'] != 'objektív':
            return [f'{k}: {state} csak MEGERŐSÍTVE + objektív findingnál lehet']
        if not SHA_RE.search(ev):
            return [f'{k}: {state} — a bizonyíték nevezzen meg commitot']
    if state == 'REJECTED' and f['Verdikt'] != 'ELVETVE':
        return [f'{k}: REJECTED csak ELVETVE verdikttel']
    if state == 'DUPLICATE' and not any(o in ev for o in keys - {k}):
        return [f'{k}: DUPLICATE — a bizonyíték nevezze meg a megtartott kulcsot']
    if state == 'BLOCKED_HUMAN' and not ev.startswith('EMBERI DÖNTÉS:'):
        return [f'{k}: BLOCKED_HUMAN — a bizonyíték „EMBERI DÖNTÉS: <mit, kitől>” alakú']
    if state == 'EVIDENCE_GATE' and f['Típus'] != 'bizonyíték-kapu':
        return [f'{k}: EVIDENCE_GATE csak bizonyíték-kapu típusnál']
    return []


def terminal_errors(run, modules, gates, findings) -> list[str]:
    errors = []
    if run.get('Állapot') != 'FINISHED':
        errors.append(f'Futás/Állapot: {run.get("Állapot")} (FINISHED kell)')
    if not modules:
        errors.append('Modulok: üres')
    for m in modules:
        name = m['Modul']
        if m['Review'] not in REVIEW_DONE:
            errors.append(f'{name}: review nem lezárt ({m["Review"]})')
        elif m['Review'] in ('VERIFIED', 'REUSED'):
            report = m['Riport'].strip('`')
            if report in EMPTY or not (AUDIT / report).is_file():
                errors.append(f'{name}: a riport nem található az 04 Audit mappában: {m["Riport"]}')
            if not SHA_RE.search(m['Review-bázis']):
                errors.append(f'{name}: hiányzó Review-bázis commit')
        if m['Javítás'] not in FIX_DONE:
            errors.append(f'{name}: javítás nem lezárt ({m["Javítás"]})')
        elif m['Javítás'] == 'DONE' and not SHA_RE.search(m['Bizonyíték']):
            errors.append(f'{name}: DONE — a bizonyíték nevezzen meg commitot')
        elif m['Javítás'] != 'DONE' and m['Bizonyíték'] in EMPTY:
            errors.append(f'{name}: {m["Javítás"]} indoklás nélkül')
    for g in gates:
        if g['Típus'] == 'PRECONDITION' and g['Állapot'] == 'OPEN':
            errors.append(f'{g["Kulcs"]}: nyitott előfeltétel')
    keys = {f['Kulcs'] for f in findings}
    for f in findings:
        errors += finding_terminal_errors(f, keys)
    qa = run.get('Záró QA', '')
    if not SHA_RE.search(qa) or 'MOODLE-BUILD-VERDICT:' not in qa or 'LEARNER-RELEASE-VERDICT:' not in qa:
        errors.append('Futás/Záró QA: commit és a két verdikt-sor szó szerint kell')
    return errors


def git(*args: str) -> subprocess.CompletedProcess:
    env = dict(os.environ, GIT_OPTIONAL_LOCKS='0')
    return subprocess.run(['git', '-C', str(ROOT), *args], capture_output=True, text=True, env=env)


def live_errors(run) -> list[str]:
    """Checks that do not trust the ledger: QA commit, unchanged content since QA, integrity."""
    errors = []
    m = SHA_RE.search(run.get('Záró QA', ''))
    if m:
        sha = m.group(0)
        if git('cat-file', '-e', f'{sha}^{{commit}}').returncode != 0:
            errors.append(f'Záró QA: a {sha} commit nem létezik')
        else:
            paths = ('02 Tervezet', 'tools')
            if git('diff', '--quiet', sha, '--', *paths).returncode != 0:
                errors.append(f'Záró QA óta ({sha}) változott a 02 Tervezet/ vagy a tools/ — új záró QA kell')
            if git('ls-files', '--others', '--exclude-standard', '--', *paths).stdout.strip():
                errors.append('nem követett fájl a 02 Tervezet/ vagy a tools/ alatt')
    ci = subprocess.run([sys.executable, str(ROOT / 'tools' / 'content_integrity.py')],
                        capture_output=True, text=True)
    if ci.returncode != 0:
        errors.append('content_integrity.py: nem 0 a kilépési kód')
    return errors


def next_action(run, modules, gates, findings) -> str:
    if run.get('Állapot') == 'NONE':
        return 'PREFLIGHT — nincs aktív futás: indítsd a /course-autopilot <scope>-pal'
    for g in gates:
        if g['Típus'] == 'PRECONDITION' and g['Állapot'] == 'OPEN':
            return f'BLOCKED {g["Kulcs"]} — {g["Tétel"]}; kell: {g["Kell (mit, kitől)"]}'
    for m in modules:
        if m['Review'] not in REVIEW_DONE:
            return f'REVIEW {m["Modul"]} ({m["Review"]}) — {m["Következő lépés"]}'
    for phase, states in (('RECHECK', ('NEEDS_RECHECK',)), ('FIX', ('IN_PROGRESS', 'OPEN'))):
        for m in modules:
            todo = [f['Kulcs'] for f in findings
                    if f['Kulcs'].split(':', 1)[0] == m['Modul'] and f['Állapot'] in states]
            if todo:
                more = f' (+{len(todo) - 6})' if len(todo) > 6 else ''
                return f'{phase} {m["Modul"]} — {len(todo)} tétel: {", ".join(todo[:6])}{more}'
    for m in modules:
        if m['Javítás'] not in FIX_DONE:
            return f'FIX {m["Modul"]} ({m["Javítás"]}) — {m["Következő lépés"]}'
    if terminal_errors(dict(run, **{'Állapot': 'FINISHED'}), modules, gates, findings):
        return 'FINAL-QA — /release-check, majd a Záró QA sor kitöltése a commit-tal és a két verdikt-sorral'
    if run.get('Állapot') != 'FINISHED':
        return 'FINISH — Futás/Állapot: FINISHED, a ledger commitja, majd check'
    return 'TERMINAL'


def counts(modules, findings) -> str:
    done_m = sum(m['Review'] in REVIEW_DONE and m['Javítás'] in FIX_DONE for m in modules)
    done_f = sum(f['Állapot'] in FINDING_DONE for f in findings)
    by = {}
    for f in findings:
        by[f['Állapot']] = by.get(f['Állapot'], 0) + 1
    detail = ', '.join(f'{s} {by[s]}' for s in FINDING_OPEN + FINDING_DONE if s in by)
    return (f'AUTOPILOT-COUNTS: modulok {done_m}/{len(modules)} lezárva; '
            f'findingok {done_f}/{len(findings)} lezárva' + (f' ({detail})' if detail else ''))


def run_command(cmd: str, text: str, live: bool = True) -> tuple[int, list[str]]:
    run, modules, gates, findings, errors = load(text)
    errors += structure_errors(run, modules, gates, findings) if not errors else []
    if errors:
        return 1, ['AUTOPILOT-LEDGER: INVALID'] + [f'  {e}' for e in errors[:40]]
    if cmd == 'validate':
        return 0, ['AUTOPILOT-LEDGER: VALID', counts(modules, findings)]
    if cmd == 'next':
        return 0, [f'AUTOPILOT-NEXT: {next_action(run, modules, gates, findings)}',
                   counts(modules, findings)]
    errors = terminal_errors(run, modules, gates, findings)
    if not errors and live:
        errors = live_errors(run)
    if errors:
        more = [f'  … és még {len(errors) - 40}'] if len(errors) > 40 else []
        return 1, (['AUTOPILOT-LEDGER: INCOMPLETE', counts(modules, findings)]
                   + [f'  {e}' for e in errors[:40]] + more)
    return 0, ['AUTOPILOT-LEDGER: TERMINAL', counts(modules, findings)]


def ledger_text(run=None, modules=(), gates=(), findings=()) -> str:
    """Build a ledger (selftest and documentation of the exact layout)."""
    base = {'Run-ID': 'AP-TEST', 'Állapot': 'FINISHED', 'Scope': 'M0', 'Lencsék': 'all',
            'Felhatalmazás': 'fix, commit', 'Munkaág': 'autopilot/AP-TEST',
            'Bázis-commit': 'abc1234', 'Indítva': '2026-10-11',
            'Záró QA': '`abc1234` · MOODLE-BUILD-VERDICT: X · LEARNER-RELEASE-VERDICT: Y'}
    base.update(run or {})
    out = ['# AUTOPILOT-LEDGER', '', '## Futás', '', '| Kulcs | Érték |', '|---|---|']
    out += [f'| {k} | {v} |' for k, v in base.items()]
    for title, cols, rows in (('Modulok', MODULE_COLS, modules), ('Külső kapuk', GATE_COLS, gates),
                              ('Findingok', FINDING_COLS, findings)):
        out += ['', f'## {title}', '', '| ' + ' | '.join(cols) + ' |', '|' + '---|' * len(cols)]
        out += ['| ' + ' | '.join(r) + ' |' for r in rows]
    return '\n'.join(out) + '\n'


def selftest() -> int:
    fails = 0

    def expect(name, text, cmd, rc, needle=''):
        nonlocal fails
        got, lines = run_command(cmd, text, live=False)
        ok = got == rc and (needle in '\n'.join(lines))
        print(f'{"ok  " if ok else "FAIL"} {name}: rc={got} {lines[0]}')
        if not ok:
            fails += 1
            print('     ' + '\n     '.join(lines[1:6]))

    with tempfile.TemporaryDirectory() as tmp:
        global AUDIT
        saved, AUDIT = AUDIT, Path(tmp)
        (AUDIT / 'r.md').write_text('x', encoding='utf-8')
        mod_ok = ('M0', 'VERIFIED', '`r.md`', 'abc1234', 'DONE', 'def5678 integrity 0', '—')
        fixed = ('M0:PED-1', 'P1', 'objektív', 'MEGERŐSÍTVE', 'FIXED', 'def5678 M0.1:12')
        blocked = ('M0:BIZT-2', 'P0', 'emberi-döntés', 'EMBERI DÖNTÉS', 'BLOCKED_HUMAN',
                   'EMBERI DÖNTÉS: jelzési lánc — gyermekvédelmi felelős')
        gate = ('X-1', 'PRECONDITION', 'harness PR', 'merge — projektgazda', 'RESOLVED')
        good = ledger_text(modules=[mod_ok], gates=[gate], findings=[fixed, blocked])
        expect('terminal ledger', good, 'check', 0, 'TERMINAL')
        expect('validate', good, 'validate', 0, 'VALID')
        expect('next on terminal', good, 'next', 0, 'TERMINAL')
        expect('run not finished', ledger_text({'Állapot': 'ACTIVE'}, [mod_ok], [gate], [fixed]),
               'check', 1, 'FINISHED kell')
        expect('open finding', ledger_text(modules=[mod_ok], findings=[fixed[:4] + ('OPEN', '—')]),
               'check', 1, 'nem lezárt')
        expect('fixed without commit', ledger_text(modules=[mod_ok], findings=[fixed[:5] + ('M0.1:12',)]),
               'check', 1, 'commitot')
        expect('fixed but human type', ledger_text(modules=[mod_ok], findings=[
            ('M0:X-1', 'P1', 'emberi-döntés', 'MEGERŐSÍTVE', 'FIXED', 'abc1234')]), 'check', 1, 'objektív')
        expect('blocked without decision text', ledger_text(modules=[mod_ok], findings=[
            blocked[:5] + ('kérdés',)]), 'check', 1, 'EMBERI DÖNTÉS:')
        expect('duplicate names kept key', ledger_text(modules=[mod_ok], findings=[
            fixed, ('M0:ERT-1', 'P1', 'objektív', 'MEGERŐSÍTVE', 'DUPLICATE', '= M0:PED-1')]), 'check', 0)
        expect('duplicate without kept key', ledger_text(modules=[mod_ok], findings=[
            ('M0:ERT-1', 'P1', 'objektív', 'MEGERŐSÍTVE', 'DUPLICATE', 'ugyanaz')]), 'check', 1, 'megtartott')
        expect('open precondition', ledger_text(modules=[mod_ok], gates=[gate[:4] + ('OPEN',)]),
               'check', 1, 'előfeltétel')
        expect('missing report file', ledger_text(modules=[('M0', 'REUSED', '`nincs.md`', 'abc1234',
                                                            'NONE_NEEDED', 'nincs objektív', '—')]),
               'check', 1, 'riport')
        expect('qa without verdicts', ledger_text({'Záró QA': '`abc1234`'}, [mod_ok]), 'check', 1, 'Záró QA')
        expect('unknown state', ledger_text(modules=[mod_ok], findings=[fixed[:4] + ('DONE', 'x')]),
               'validate', 1, 'ismeretlen állapot')
        expect('finding of unknown module', ledger_text(modules=[mod_ok], findings=[
            ('M9:PED-1',) + fixed[1:]]), 'validate', 1, '<Modul>:<ID>')
        expect('missing section', good.replace('## Külső kapuk', '## Egyéb'), 'validate', 1, 'Külső kapuk')
        expect('cell count', good.replace('| M0:PED-1 | P1 |', '| M0:PED-1 |'), 'validate', 1, 'cella')
        expect('escaped pipe', ledger_text(modules=[mod_ok], findings=[
            fixed[:5] + ('def5678 a \\| b',)]), 'check', 0)
        none = ledger_text({'Állapot': 'NONE', 'Záró QA': '—'},
                           [('M0', 'PENDING', '—', '—', 'PENDING', '—', 'review')])
        expect('template validates', none, 'validate', 0, 'VALID')
        expect('template next', none, 'next', 0, 'PREFLIGHT')
        active = ledger_text({'Állapot': 'ACTIVE', 'Záró QA': '—'},
                             [mod_ok, ('M1', 'REVIEWING', '—', '—', 'PENDING', '—', 'verifier 2/3')],
                             [], [fixed])
        expect('next review', active, 'next', 0, 'REVIEW M1')
        active2 = ledger_text({'Állapot': 'ACTIVE', 'Záró QA': '—'}, [mod_ok],
                              [], [fixed[:4] + ('OPEN', '—'), blocked])
        expect('next fix', active2, 'next', 0, 'FIX M0 — 1 tétel: M0:PED-1')
        active3 = ledger_text({'Állapot': 'ACTIVE', 'Záró QA': '—'}, [mod_ok], [], [fixed])
        expect('next final qa', active3, 'next', 0, 'FINAL-QA')
        AUDIT = saved
    print('--- selftest OK ---' if not fails else f'--- selftest FAILED ({fails}) ---')
    return 1 if fails else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ['--selftest']:
        return selftest()
    if not argv or argv[0] not in ('validate', 'check', 'next'):
        print(__doc__.strip().split('\n\n')[1])
        return 2
    path = Path(argv[argv.index('--ledger') + 1]) if '--ledger' in argv else LEDGER
    if not path.is_file():
        print(f'AUTOPILOT-LEDGER: MISSING ({path})')
        return 1
    rc, lines = run_command(argv[0], path.read_text(encoding='utf-8'))
    print('\n'.join(lines))
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
