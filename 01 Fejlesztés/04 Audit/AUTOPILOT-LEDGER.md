# AUTOPILOT-LEDGER — a `/course-autopilot` tartós állapota

> **Audit trail, nem kánon, nem tanulói tartalom.** Egy autopilot-futás egyetlen tartós
> állapotnyilvántartása; egyetlen író: a fő session (`Edit`). Formátum és állapotgép:
> `.claude/skills/course-autopilot/ledger.md`. Ellenőrzés: `python3 tools/autopilot_ledger.py
> validate` (szerkezet) · `check` (végállapot) · `next` (folytatás). A ledger nem bizonyíték: minden
> állapotot a fájlban, a diffben vagy a parancskimenetben bizonyítunk, mielőtt ide kerül.
>
> **Jelenleg nincs aktív futás.** Az előre kitöltött sorok az első futás PREFLIGHT-jának
> kiindulópontjai (a harness v2 bevezetésekor, 2026-10-11); a PREFLIGHT mindegyiket a kánonból és
> a git-állapotból újraellenőrzi.

## Futás

| Kulcs | Érték |
|---|---|
| Run-ID | — |
| Állapot | NONE |
| Scope | — |
| Lencsék | — |
| Felhatalmazás | — |
| Munkaág | — |
| Bázis-commit | — |
| Indítva | — |
| Záró QA | — |
| Korlátok | M0+M1 pilot-freeze (2026-10-05; a pilot 2026-10-10 óta fut): ott csak freeze-kivétel javítható, a többi `OWNER_DEFERRED` (POST-PILOT) — a PREFLIGHT a kánonból újraellenőrzi |

## Modulok

| Modul | Review | Riport | Review-bázis | Javítás | Bizonyíték | Következő lépés |
|---|---|---|---|---|---|---|
| M0 | PENDING | `2026-10-10 Validált findingok – M0 course-review, B sáv.md` | 82d0c7c | PENDING | — | INVENTORY: REUSE-ellenőrzés (lencsék: pedagógia, értékelés, implementáció, biztonság-jog) |
| M1 | PENDING | `2026-10-10 Validált findingok – M1 course-review, B sáv.md` | 82d0c7c | PENDING | — | INVENTORY: REUSE-ellenőrzés; az N-M1-04 átvezetése után a változott M1-fájlok NEEDS_RECHECK |
| M2 | PENDING | — | — | PENDING | — | review |
| M3 | PENDING | — | — | PENDING | — | review |
| M4 | PENDING | — | — | PENDING | — | review |
| M5 | PENDING | — | — | PENDING | — | review |
| M6 | PENDING | — | — | PENDING | — | review (a 2026-10-04-i M6 nyelvi review lezárva, PR #19 — csak a nyelvi lencsére újrahasznosítható) |
| M7 | PENDING | — | — | PENDING | — | review |
| Z | PENDING | — | — | PENDING | — | review |

## Külső kapuk

| Kulcs | Típus | Tétel | Kell (mit, kitől) | Állapot |
|---|---|---|---|---|
| X-1 | PRECONDITION | Az N-M1-04 átvezetése (M1.1 SLIDE 5, HUM 12. szakasz, manifest, runtime-teszt) a `fix/m1-privacy-learner-local` ágon, nem commitolt — az M1-et tartalmazó futás előfeltétele | projektgazda: diff-review, commit és merge — vagy a futás kifejezetten erről az ágról indul | OPEN |
| X-2 | PRECONDITION | A harness v2 (`gov/claude-harness-v2`) mergelve, és a futás új sessionben, a repó gyökeréből indul | projektgazda: PR-review és merge | OPEN |
| X-3 | HUMAN_DECISION | Az Anna-megfeleltetés és a 2026-10-10-i döntési jegyzőkönyv (`audit/anna-traceability-20261010`, 695e5e4) nincs a mainen; a CC-04/CC-06 HUM-átvezetése (M0 ERT-8) erre a forrásra hivatkozik | projektgazda: az ág mergelése, vagy a jegyzőkönyv más úton a mainre | OPEN |

## Findingok

| Kulcs | Súly | Típus | Verdikt | Állapot | Bizonyíték / döntési igény |
|---|---|---|---|---|---|

## Napló

| Idő | Fázis | Esemény |
|---|---|---|
| 2026-10-11 | — | A ledger létrehozva a harness v2-vel; nincs aktív futás. |
