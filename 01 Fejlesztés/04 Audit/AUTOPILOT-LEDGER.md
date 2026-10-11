# AUTOPILOT-LEDGER — a `/course-autopilot` tartós állapota

> **Audit trail, nem kánon, nem tanulói tartalom.** Egy autopilot-futás egyetlen tartós
> állapotnyilvántartása; egyetlen író: a fő session (`Edit`). Formátum és állapotgép:
> `.claude/skills/course-autopilot/ledger.md`. Ellenőrzés: `python3 tools/autopilot_ledger.py
> validate` (szerkezet) · `check` (végállapot) · `next` (folytatás). A ledger nem bizonyíték: minden
> állapotot a fájlban, a diffben vagy a parancskimenetben bizonyítunk, mielőtt ide kerül.
>
> **Aktív futás: `AP-2026-10-11-01`** (`next-version`, M0–Z, öt lencse). A felhatalmazás teljes szövege:
> `2026-10-11 Projektgazdai felhatalmazás – next-version M0–Z autopilot.md`. Az előző (harness v2-es) sablon
> a git-historyban marad (`99ba147`).

## Futás

| Kulcs | Érték |
|---|---|
| Run-ID | AP-2026-10-11-01 |
| Állapot | ACTIVE |
| Változat | next-version |
| Scope | M0-Z (M0, M1, M2, M3, M4, M5, M6, M7, Z) |
| Lencsék | pedagogy,assessment,language,safety,implementation |
| Felhatalmazás | next-version — projektgazda, 2026-10-11, szó szerint: „Projektgazdaként kifejezetten engedélyezem a módszertani képzés következő verziójának teljes M0–M7 + Z felülvizsgálatát, valamennyi validált objektív hiba javítását, beleértve a korábban POST-PILOT besorolású M0/M1 javításokat is, külön next-version munkaágon, a jelenlegi pilot változatának módosítása nélkül. Engedélyezem a szükséges rutinmódosításokat, ellenőrzéseket, generált médiakimenetek frissítését és helyi checkpoint-commitokat. Új szakpolitikai, gyermekvédelmi, adatvédelmi vagy értékelési döntést nem hozhatsz helyettem.” — fix: igen; commit: helyi munkaágon; push/PR/merge/governance-módosítás/éles Moodle/tanulói release: nem |
| Munkaág | next-version/AP-2026-10-11-01 |
| Bázis-commit | 213a4c5 |
| Indítva | 2026-10-11 |
| Záró QA | — |
| Korlátok | (1) Az M0+M1 pilot-freeze (2026-10-05) és a `POST-PILOT` címke ezen az ágon nem halasztási ok (felhatalmazás); a futó pilot forrása, a `main`, nem változik. (2) Lezárt döntés érvényes és nem nyílik újra: HUM 1–12. szakasz (N-M1-04: `2026-10-10 Projektgazdai döntés – N-M1-04…`), D-a…D-j, PILOT-1…4, a 2026-10-05-i scope-korrekció, a 2026-10-10-i Anna-döntések (CC-04: az M0.1 SLIDE 5 finomítása; CC-06: Moodle-összevetés külön build/runtime feladat; külső kutatási hivatkozás nem igazolt bizonyíték; kerülendő a szükségtelen módosítás és Anna természetes szövegezésének romlása). (3) Új szakpolitikai, gyermekvédelmi, adatvédelmi, értékelési döntés → `BLOCKED_HUMAN`; DPO-, szakértői, runtime-bizonyíték → `EVIDENCE_GATE`. (4) Hangok csak szerepnéven (nyilvános repó, 2026-10-03). (5) Generált médiát csak a `media_manifest.py build`, látható-szöveg pint csak a `--pin-visible` ír. |

## Modulok

| Modul | Review | Lencsék | Riport | Review-bázis | Javítás | Bizonyíték | Következő lépés |
|---|---|---|---|---|---|---|---|
| M0 | PENDING | pedagogy,assessment,implementation,safety | `2026-10-10 Validált findingok – M0 course-review, B sáv.md` | 82d0c7c | PENDING | — | REVIEW: csak a hiányzó `language` lencse (`/course-review M0 --lens language --run AP-2026-10-11-01`); a négy lefutott lencse REUSED (M0 a 82d0c7c óta nem változott) |
| M1 | PENDING | pedagogy,assessment,implementation,safety | `2026-10-10 Validált findingok – M1 course-review, B sáv.md` | 82d0c7c | PENDING | — | REVIEW: csak a hiányzó `language` lencse; a 82d0c7c óta csak az M1.1 (és MAN LMS-M1-01, RA 24., HUM 12.) változott (N-M1-04, PR #29) — az ott lévő findingok NEEDS_RECHECK |
| M2 | PENDING | — | — | — | PENDING | — | REVIEW: öt lencse, teljes modul |
| M3 | PENDING | — | — | — | PENDING | — | REVIEW: öt lencse, teljes modul |
| M4 | PENDING | — | — | — | PENDING | — | REVIEW: öt lencse, teljes modul |
| M5 | PENDING | — | — | — | PENDING | — | REVIEW: öt lencse, teljes modul |
| M6 | PENDING | — | — | — | PENDING | — | REVIEW: öt lencse, teljes modul — a 2026-10-04-i M6 nyelvi review (régi formátum) után a modul változott (PR #19), ezért lefedettséget nem ad |
| M7 | PENDING | — | — | — | PENDING | — | REVIEW: öt lencse, teljes modul |
| Z | PENDING | — | — | — | PENDING | — | REVIEW: öt lencse, teljes modul |

## Külső kapuk

| Kulcs | Típus | Tétel | Kell (mit, kitől) | Állapot |
|---|---|---|---|---|
| X-1 | PRECONDITION | Az N-M1-04 átvezetése (M1.1 SLIDE 5, HUM 12. szakasz, manifest, runtime-teszt) | RESOLVED 2026-10-11: PR #29 mergelve, `213a4c5` (tartalom: `ebf311e`, `96996e2`; `origin/fix/m1-privacy-learner-local` = `6dde193` a `main` őse) | RESOLVED |
| X-2 | PRECONDITION | A harness v2 mergelve, és a futás új sessionben, a repó gyökeréből indul | RESOLVED 2026-10-11: PR #26 mergelve, `d48bc2a` (`origin/gov/claude-harness-v2` = `ffee45e` a `main` őse); a session a repó gyökeréből indult, a projekt-sandbox és -settings betöltve | RESOLVED |
| X-3 | HUMAN_DECISION | Az Anna-megfeleltetés és a 2026-10-10-i döntési jegyzőkönyv a mainen | RESOLVED 2026-10-11: PR #28 mergelve, `0c7e299` (`695e5e4` a `main` őse). A CC-04/CC-06 HUM-átvezetése innen objektív tétel: `M0:ERT-8`, `M1:IMPL-G1-2` | RESOLVED |
| X-4 | HUMAN_DECISION | Adatkör, megőrzés, hozzáférés — DPO-döntések | DPO / jogi felelős: `M0:BIZT-7` (a bemutatkozó fórum megőrzési sora és tájékoztatója; a Program terv :228 szerint addig adatgyűjtő activity nem nyitható meg) | OPEN |
| X-5 | HUMAN_DECISION | Gyermekvédelmi szabály-alkalmazás (Memuna, HUM-SAFE-02 QA) | Memuna (egyes tételeknél programvezető, DPO): `M0:BIZT-3` (SAFE-7 kiterjed-e az M0.4 SLIDE 3 2. helyzetére), `M0:BIZT-5` (csoportchat-szívatás jelzési küszöbe), `M0:BIZT-9` (két felnőtt az M0.A-n), `M0:PED-8` (egyéni utánkövetés a belépőkvíz 1–2. itemén; adatkör: DPO) | OPEN |
| X-6 | HUMAN_DECISION | Completion- és értékelési jelentésdöntések | projektgazda; QA: értékelési felelős: `M0:IMPL-3` (H5P-C completion = összefoglaló dia elérése vagy kikényszerített megválaszolás), `M0:ERT-3` (a D-d/D-i pontozatlan-választó elv általános-e) | OPEN |
| X-7 | EVIDENCE_GATE | Memuna írásos „átnéztem” bejegyzése (G1) | Memuna, G1 (GK :17, tracker #1): `M0:BIZT-1` | OPEN |
| X-8 | RUNTIME | Célkörnyezeti Moodle-visszaolvasás | LMS-gazda, G3b/G4b/G8: `M0:IMPL-9` (a „Segítség és kapcsolatok” blokk kitöltése, RT-17, tanulói fiókkal) | OPEN |
| X-9 | SIGNOFF | Értékelési szerepköri QA | értékelési felelős (az 1–2. itemnél Memuna): `M0:ERT-4` (a belépőkvíz projektgazdai itemszövegének utólagos QA-ja; answer key nem változik) | OPEN |

## Findingok

| Kulcs | Súly | Típus | Verdikt | Állapot | Bizonyíték / döntési igény |
|---|---|---|---|---|---|
| M0:ERT-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:ERT-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:IMPL-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:IMPL-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:ERT-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:ERT-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:ERT-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:PED-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:PED-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:PED-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:PED-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:BIZT-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:BIZT-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:BIZT-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:BIZT-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:IMPL-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:IMPL-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:IMPL-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:PED-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-1 |
| M0:BIZT-4 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-1 |
| M0:IMPL-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-1 |
| M0:IMPL-4 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-2 |
| M0:ERT-6 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:IMPL-2 |
| M0:PED-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-7 |
| M0:PED-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:ERT-8 (az IMPL-6 (d) része is ide olvadt; az IMPL-6 (b) része = M0:ERT-9) |
| M0:BIZT-7 | P0 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a bemutatkozó fórumposzt/-válasz megőrzési ideje és §3-sora, a „Bemutatkozó fal” külön review-ja, a megőrzési tájékoztató — DPO / jogi felelős (X-4) |
| M0:BIZT-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kiterjed-e a SAFE-7 (HUM :567) az M0.4 SLIDE 3 2. helyzetére (késő esti 1:1 üzenet) — Memuna, HUM-SAFE-02 QA (X-5) |
| M0:BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a csoportchat-szívatás minden esetben Memuna-jelzés (M0.2), vagy csak súlyosság felett (M0.4, belépőkvíz) — Memuna (X-5) |
| M0:BIZT-9 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kötelező-e két felnőtt jelenléte az M0.A-n — programvezető + Memuna (X-5) |
| M0:PED-8 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: egyéni, támogató utánkövetés a belépőkvíz 1–2. itemének első téves válasza után, és ki láthatja ehhez az egyéni válaszokat — programvezető + Memuna; adatkör: DPO (X-5) |
| M0:IMPL-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a H5P-C completion jelentése (összefoglaló dia elérése, és a Completion-sorok ehhez igazodnak — vagy a megválaszolás kikényszerítése, szerkezeti átépítéssel) — projektgazda; QA: értékelési felelős (X-6) |
| M0:ERT-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a pontozatlan választók completion-elve (D-d/D-i) általános, vagy csak a felsorolt tételekre szól (az M0.1 completionje csak pontozatlan választókból áll) — projektgazda; QA: értékelési felelős (X-6) |
| M0:BIZT-1 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna, G1 (GK :17, tracker #1): írásos „átnéztem” az M0 gyermekvédelmi elemeire (X-7) |
| M0:IMPL-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda, G8/G4b, RT-17: a „Segítség és kapcsolatok” blokk kitöltése és visszaolvasása tanulói fiókkal (X-8) |
| M0:BIZT-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M0:IMPL-9 |
| M0:ERT-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | értékelési felelős (az 1–2. itemnél Memuna), G-kapu: értékelési QA: a belépőkvíz itemszövegének utólagos QA-ja (X-9) |
| M0:PED-7 | P2 | objektív | ELVETVE | REJECTED | ízlésbeli: a SLIDE 7 szándékosan sűrít; kár nem bizonyított (verifier) |
| M0:PED-9 | P2 | objektív | ELVETVE | REJECTED | pedagógiai preferencia: az M0.4 SLIDE 4 1. szabálya az M0.2:430 megerősítő ismétlése (verifier) |
| M0:ERT-5 | P1 | objektív | ELVETVE | REJECTED | az M0.1-rész a PED-3 duplikátuma; a hub 2.2/2.5 mérés nélkülisége a lezárt D-4-ből és a puha kapuból következik (verifier) |
| M0:ERT-10 | P2 | objektív | ELVETVE | REJECTED | item-írási preferencia: az M0.3:193 formatív, a visszajelzés tanít (verifier) |

## Napló

| Idő | Fázis | Esemény |
|---|---|---|
| 2026-10-11 | — | A ledger létrehozva a harness v2-vel; nincs aktív futás. |
| 2026-10-11 | PREFLIGHT | `AP-2026-10-11-01` indul (`next-version`), bázis `main@213a4c5`, munkaág `next-version/AP-2026-10-11-01`. Kiinduló gépi állapot: `content_integrity.py` → „Objective integrity errors: 0”, kilépési kód 0; `--release-report` → `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`, `LEARNER-RELEASE-VERDICT: NO-GO`. A #26–#29 merge-commitok a `main`-ben; X-1, X-2, X-3 RESOLVED (git-bizonyíték a kapusorokban). |
| 2026-10-11 | INVENTORY | M0: a 82d0c7c óta nincs változás a modulban → a négy lencse REUSED, a `language` hiányzik. 40 ID a ledgerben (18 OPEN, 7 DUPLICATE, 7 BLOCKED_HUMAN, 3 EVIDENCE_GATE + 1 DUPLICATE kapu, 4 REJECTED). M1: kivonatolás folyamatban. |
