# AUTOPILOT-LEDGER — a `/course-autopilot` tartós állapota

> **Audit trail, nem kánon, nem tanulói tartalom.** Egy autopilot-futás egyetlen tartós
> állapotnyilvántartása; egyetlen író: a fő session (`Edit`). Formátum és állapotgép:
> `.claude/skills/course-autopilot/ledger.md`. Ellenőrzés: `python3 tools/autopilot_ledger.py
> validate` (szerkezet) · `check` (végállapot) · `next` (folytatás). A ledger nem bizonyíték: minden
> állapotot a fájlban, a diffben vagy a parancskimenetben bizonyítunk, mielőtt ide kerül.
>
> **Aktív futás: `AP-2026-10-12-01`** (`next-version`, M0–Z): a HUM 14. szakasz 125 döntésének átvezetése. A felhatalmazás teljes
> szövege: `2026-10-12 Projektgazdai felhatalmazás – a HUM 14. szakasz átvezetése, AP-2026-10-12-01.md`. Az előző futás
> (`AP-2026-10-11-01`) ledgere a git-historyban marad (utolsó állapota: `beaea60`).

## Futás

| Kulcs | Érték |
|---|---|
| Run-ID | AP-2026-10-12-01 |
| Állapot | ACTIVE |
| Változat | next-version |
| Scope | M0-Z (M0, M1, M2, M3, M4, M5, M6, M7, Z) és a közös kánoni fájlok |
| Lencsék | pedagogy,assessment,language,safety,implementation |
| Felhatalmazás | next-version — projektgazda, 2026-10-12, szó szerint: „Indítsd a HUM 14. szakaszban rögzített mind a 125 OWNER_DECIDED döntés teljes átvezetését a `next-version/AP-2026-10-11-01` ágon. / A cél a végleges, szakmailag javított M0–Z tananyag előállítása, nem újabb döntés-előkészítés. / - Mind a 125 döntést dolgozd fel, az A és F döntéseket egyaránt. / - Az F döntéseknél alkalmazd az elfogadott óvatos alapértelmezést, amíg a külső feltétel nem teljesül. / - Hajtsd végre a szükséges tartalmi, értékelési, LMS-specifikációs és kanonikus módosításokat. / - Használd a meglévő review → fix → célzott QA → regresszió workflow-t. Ne kezdj újabb teljes alapreview-t. / - A 16 bizonyítékkaput tartsd nyitva, de ne állítsd le miattuk a függetlenül elvégezhető fejlesztést. / - Minden döntéshez rögzítsd az implementációt, a tesztelést és a fennmaradó külső függőséget. / - A végén futtasd le a teljes elérhető validációt, és adj tételes, 125/125 lefedettségi jelentést. / Dolgozz autonóm módon a teljes implementációs körön. A módosításokat commitold és pushold a next-version ágra. / A `main`, a futó M0/M1 pilot és a CC-04 freeze érintetlen marad. A PR #30 maradjon draft. Merge, staging deployment és learner release nem engedélyezett. / A végén különítsd el az IMPLEMENTED, a QA-ra váró és a külső bizonyítéktól függő tételeket. Ne jelölj semmit teljesítettnek tényleges bizonyíték nélkül.” — fix: igen; commit és push: a next-version ágra; PR #30 draft marad; merge/staging deployment/tanulói release/main/governance-módosítás: nem |
| Munkaág | next-version/AP-2026-10-11-01 |
| Bázis-commit | beaea60 |
| Indítva | 2026-10-12 |
| Záró QA | — |
| Korlátok | (1) Bemenet: az `Emberi jóváhagyás szükséges.md` 14. szakasza, 125 `OWNER_DECIDED` döntés; a döntés szövege szó szerint köt; `F` döntésnél a sorban megnevezett óvatos alapértelmezés, amíg a külső feltétel nem teljesül. Új alapreview nincs: a review-t az AP-2026-10-11-01 öt lencséje és a döntési csomag adja (REUSED). (2) A 299 korábbi `BLOCKED_HUMAN` kulcs a lezárt döntéssel javítható: Típus `objektív`, Verdikt `MEGERŐSÍTVE` (lezárt projektgazdai döntés átvezetése, `.claude/rules/safety-and-human-gates.md`); a 31 `EVIDENCE_GATE` kulcs és a 16 bizonyíték-/aláírás-bejegyzés nyitva marad (X-1…X-4). (3) A `main@213a4c5`, a futó M0+M1 pilot és a CC-04 freeze érintetlen; PR #30 draft. (4) Új pedagógiai tartalom (új item, activity, peula, eset) csak a döntés szövege szerinti pontos szöveggel; különben a PRG-4 `/course-develop` csomagjába kerül (a felhasználó indítja, a tervet a projektgazda hagyja jóvá), és a döntés óvatos alapértelmezése érvényes. (5) A `tools/` és a governance nem változik; a TECH-2 átnevezését a felhasználó futtatja a saját termináljában; a VO-1 hangja a VO-gyártási úton készül. (6) Lezárt döntés (HUM 1–14) nem nyílik újra; a szerepek ellenőrzése vétó/QA. (7) Generált médiát csak a `media_manifest.py build`, látható-szöveg pint csak a `--pin-visible` ír. (8) Hangok csak szerepnéven (2026-10-03). |

## Modulok

| Modul | Review | Lencsék | Riport | Review-bázis | Javítás | Bizonyíték | Következő lépés |
|---|---|---|---|---|---|---|---|
| M0 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | FIXING | fix `5484b02`, media `0eeb225`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M0 átvezetés (5484b02), AP-2026-10-12-01.md`; QA-fix `a2445ff`, media `68dc5e9` | kánoni kör (M0 DEFER_CANON blokkjai), utána a Findingok sorai |
| M1 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | FIXING | fix `eb4fa6d`, media `42635db` | célzott QA (3 lencse) kész → verifier fut → QA-fix → kánoni kör |
| M2 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | FIXING | fix `147f3c3`, media `d473ab6` | célzott QA (3 lencse, fut) → verifier → QA-fix → kánoni kör |
| M3 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | PENDING | — | fix-terv (read-only ügynök) → alkalmazás → célzott QA |
| M4 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | FIXING | fix `dd64825`, media `adf1f41`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M4 átvezetés (dd64825), AP-2026-10-12-01.md`; `2026-10-12 Célzott QA – M4 átvezetés, nyelvi lencse és verifier, AP-2026-10-12-01.md`; QA-fix `64a60d1`, media `b409d02` | kánoni kör, utána a Findingok sorai |
| M5 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | FIXING | fix `aadf41b`, media `50f2891`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M5 átvezetés (aadf41b), AP-2026-10-12-01.md`; QA-fix `9764987` | kánoni kör, utána a Findingok sorai |
| M6 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | FIXING | fix `fbebec0`, media `ac49d8b`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M6 átvezetés (fbebec0), AP-2026-10-12-01.md`; QA-fix `511d9e0`, media `b409d02` | kánoni kör, utána a Findingok sorai |
| M7 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | PENDING | — | fix-terv (read-only ügynök) → alkalmazás → célzott QA |
| Z | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | PENDING | — | fix-terv (read-only ügynök) → alkalmazás → célzott QA |

## Külső kapuk

| Kulcs | Típus | Tétel | Kell (mit, kitől) | Állapot |
|---|---|---|---|---|
| X-1 | EVIDENCE_GATE | G1: a Memuna írásos „átnéztem” bejegyzése (GYV-24) | Memuna: egyazon végleges SHA-ra szóló, datált „átnéztem” (PT §9.3), SAFE-7 és az 1:1-kulcsok verdiktje, segélyvonalak review-napi ellenőrzése, tracker #1 lezárása | OPEN |
| X-2 | EVIDENCE_GATE | G2: a DPO írásos release-QA-ja (ADV-E1, ADV-E2, ADV-E3) | DPO / jogi felelős: activitynkénti jóváhagyás (adatmezők, szerepek, megőrzés, export, xAPI/LRS, saved-state, backup), teljes adatleltár, HUM-PRIV-04 AI-kapcsolat QA-ja; tracker #2 | OPEN |
| X-3 | SIGNOFF | Szerepköri jóváhagyások (SIG-1…SIG-6) | értékelési felelős, szakmai lektor, Memuna, jogi jogosult, DPO, szerző: a döntési csomag SIG-bejegyzései szerint | OPEN |
| X-4 | RUNTIME | Célkörnyezeti runtime-bizonyíték (RT-1…RT-6) | LMS-gazda / build-felelős, hozzáférhetőségi gazda, DPO a saját részén: RA 1–26. pont, RT-P0-xx és RT-A11Y sorok | OPEN |
| X-5 | HUMAN_DECISION | Szerepköri bemenetek és vétó/QA az `F` döntésekhez | a döntésben megnevezett szerep (Memuna, DPO, jogász, értékelési felelős, modulgazda, programvezető, LMS-gazda): a fix-tervek alapján tételesen kitöltendő | OPEN |
| X-6 | HUMAN_DECISION | VO-1: egyetlen VO fix pack | médiafelelős / VO-gazda: a kimondott szöveget módosító blokkok újrarenderelése, a többi kiejtési azonosságának igazolása; kurzusoldali alkalmazás fix packként | OPEN |
| X-7 | HUMAN_DECISION | TECH-2: az M6.1/M6.2 átnevezése | a felhasználó futtatja az átnevezési commitot a saját termináljában; utána a hivatkozások, a két `tools/` útvonalkulcs, a baseline-sor, a pin és a média egy change setben | OPEN |
| X-8 | HUMAN_DECISION | PRG-4: célzott `/course-develop` csomag | a felhasználó indítja; a csomagtervet a projektgazda hagyja jóvá; új biztonsági vagy értékelési item csak Memuna- / értékelési jóváhagyással | OPEN |
| X-9 | HUMAN_DECISION | PRG-17: az M0.1 SLIDE 5 kérdése | a pilot-visszajelzéssel együtt dönt a projektgazda / modulgazda (CC-04, HUM 13. és 14. szakasz) | OPEN |

## Findingok

| Kulcs | Súly | Típus | Verdikt | Állapot | Bizonyíték / döntési igény |
|---|---|---|---|---|---|
| M0:BIZT-1 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M0:BIZT-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-3 (`F`) |
| M0:BIZT-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-7 (`F`) |
| M0:BIZT-7 | P0 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-6 (`F`) |
| M0:BIZT-9 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-5 (`F`) |
| M0:ERT-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-2 (`A`) |
| M0:ERT-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Értékelési felelős, 1–2.: Memuna: SIG-1 (X-3) |
| M0:ERT-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-17 (`F`) |
| M0:IMPL-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-8 (`A`) |
| M0:IMPL-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-1 (`A`) |
| M0:IMPL-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-6 (`F`) |
| M0:IMPL-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + programvezető: RT-1 (X-4) |
| M0:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-11 (`A`) |
| M0:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M0:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-1 (`F`) |
| M0:NYELV-G2-22 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-11 (`A`) |
| M0:PED-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M0:PED-8 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-23 (`F`) |
| M1:BIZT-G1-3 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:BIZT-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-13 (`A`) |
| M1:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-22 (`A`) |
| M1:BIZT-G2-1 | P0 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-12 (`A`) |
| M1:BIZT-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-12 (`A`) |
| M1:BIZT-G2-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M1:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-12 (`A`) |
| M1:BIZT-G2-4 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-1 (`F`) |
| M1:BIZT-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-11 (`F`) |
| M1:BIZT-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M1:BIZT-G3-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-6 (`A`) |
| M1:BIZT-G3-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-21 (`A`) |
| M1:BIZT-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-7 (`A`) |
| M1:BIZT-G3-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-13 (`A`) |
| M1:ERT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:ERT-G1-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M1:ERT-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-14 (`A`) |
| M1:ERT-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-15 (`F`) |
| M1:ERT-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-4 (`F`) |
| M1:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-16 (`F`) |
| M1:IMPL-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-4 (`F`) |
| M1:IMPL-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-9 (`F`) |
| M1:IMPL-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-1 (`F`) |
| M1:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-9 (`A`) |
| M1:IMPL-G2-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:IMPL-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-8 (`A`) |
| M1:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-2 (`A`) |
| M1:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M1:NYELV-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-16 (`F`) |
| M1:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M1:NYELV-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-17 (`A`) |
| M1:NYELV-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-16 (`F`) |
| M1:NYELV-G3-16 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-16 (`F`) |
| M1:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M1:PED-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-13 (`A`) |
| M1:PED-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-5 (`F`) |
| M1:PED-G3-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M2:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-1 (`F`) |
| M2:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-4 (`F`) |
| M2:BIZT-G1-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-5 (`F`) |
| M2:BIZT-G1-6 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-1 (`F`) |
| M2:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-10 (`F`) |
| M2:BIZT-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-13 (`A`) |
| M2:BIZT-G1-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M2:BIZT-G2-1 | P0 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-1 (`F`) |
| M2:BIZT-G2-2 | P0 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-2 (`F`) |
| M2:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-1 (`F`) |
| M2:BIZT-G2-4 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-3 (`F`) |
| M2:BIZT-G2-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-4 (`F`) |
| M2:BIZT-G2-6 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-5 (`F`) |
| M2:BIZT-G2-8 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M2:BIZT-G2-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M2:BIZT-G3-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-11 (`F`) |
| M2:BIZT-G3-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-5 (`F`) |
| M2:BIZT-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-20 (`F`) |
| M2:BIZT-G3-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-21 (`A`) |
| M2:BIZT-G3-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M2:BIZT-G3-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-19 (`A`) |
| M2:ERT-G1-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-7 (`F`) |
| M2:ERT-G1-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M2:ERT-G3-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-15 (`F`) |
| M2:IMPL-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-9 (`F`) |
| M2:IMPL-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-18 (`F`) |
| M2:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-12 (`A`) |
| M2:IMPL-G3-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-11 (`A`) |
| M2:IMPL-G3-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M2:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-16 (`F`) |
| M2:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-20 (`F`) |
| M2:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-3 (`A`) |
| M2:PED-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-19 (`F`) |
| M2:PED-G1-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-5 (`F`) |
| M2:PED-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-4 (`F`) |
| M2:PED-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-8 (`F`) |
| M2:PED-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-12 (`A`) |
| M2:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M2:PED-G3-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-5 (`F`) |
| M2:QA-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-13 (`A`) |
| M2:QA-PED-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-8 (`A`) |
| M3:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-3 (`F`) |
| M3:BIZT-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-13 (`A`) |
| M3:BIZT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:BIZT-G1-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-4 (`F`) |
| M3:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-10 (`F`) |
| M3:BIZT-G1-8 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz JOG-1 (`F`) |
| M3:BIZT-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:BIZT-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-14 (`F`) |
| M3:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-3 (`F`) |
| M3:BIZT-G2-4 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-4 (`F`) |
| M3:BIZT-G2-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-2 (`F`) |
| M3:BIZT-G2-7 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-4 (`F`) |
| M3:BIZT-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-3 (`F`) |
| M3:BIZT-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-15 (`F`) |
| M3:BIZT-G3-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-3 (`F`) |
| M3:BIZT-G3-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-16 (`F`) |
| M3:BIZT-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-2 (`F`) |
| M3:ERT-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-5 (`A`) |
| M3:ERT-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-22 (`A`) |
| M3:ERT-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-21 (`F`) |
| M3:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M3:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-7 (`A`) |
| M3:ERT-G3-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-5 (`F`) |
| M3:ERT-G3-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-12 (`F`) |
| M3:ERT-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-21 (`F`) |
| M3:IMPL-G2-11 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-4 (`F`) |
| M3:IMPL-G2-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-23 (`F`) |
| M3:IMPL-G2-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-4 (`F`) |
| M3:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-2 (`A`) |
| M3:IMPL-G2-4 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-9 (`F`) |
| M3:IMPL-G2-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-2 (`F`) |
| M3:IMPL-G2-6 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-3 (`F`) |
| M3:IMPL-G3-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:IMPL-G3-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-11 (`A`) |
| M3:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-1 (`A`) |
| M3:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M3:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M3:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-4 (`F`) |
| M3:NYELV-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz JOG-1 (`F`) |
| M3:NYELV-G2-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M3:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-5 (`A`) |
| M3:NYELV-G3-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M3:NYELV-G3-6 | P3 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-16 (`F`) |
| M3:PED-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M3:PED-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-2 (`F`) |
| M3:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M3:PED-G3-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-6 (`F`) |
| M3:PED-G3-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-12 (`F`) |
| M3:PED-G3-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M3:PED-G3-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M3:QA-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-10 (`F`) |
| M4:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-3 (`F`) |
| M4:BIZT-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-9 (`A`) |
| M4:BIZT-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-19 (`A`) |
| M4:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-14 (`F`) |
| M4:BIZT-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-3 (`F`) |
| M4:BIZT-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-2 (`F`) |
| M4:BIZT-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-7 (`A`) |
| M4:BIZT-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-7 (`A`) |
| M4:BIZT-G2-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M4:BIZT-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-6 (`A`) |
| M4:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-25 (`F`) |
| M4:ERT-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-3 (`F`) |
| M4:ERT-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M4:ERT-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-4 (`F`) |
| M4:ERT-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-4 (`F`) |
| M4:ERT-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-8 (`A`) |
| M4:IMPL-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-3 (`F`) |
| M4:IMPL-G2-12 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + programvezető + a11y: RT-3 (X-4) |
| M4:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M4:NYELV-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TECH-1 (`A`) |
| M4:NYELV-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M4:NYELV-G2-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M4:NYELV-G2-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-16 (`F`) |
| M4:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M4:NYELV-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M4:PED-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-24 (`F`) |
| M4:PED-G1-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M4:PED-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M4:PED-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M4:PED-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-10 (`A`) |
| M4:PED-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M5:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-7 (`F`) |
| M5:BIZT-G1-4 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M5:BIZT-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-9 (`A`) |
| M5:BIZT-G1-6 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Szakmai lektor: SIG-5 (X-3) |
| M5:BIZT-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-7 (`A`) |
| M5:BIZT-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-4 (`F`) |
| M5:BIZT-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-8 (`F`) |
| M5:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-3 (`F`) |
| M5:ERT-G1-11 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Kijelölt szakmai lektor; M5 assessment QA: SIG-4 (X-3) |
| M5:ERT-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-6 (`A`) |
| M5:ERT-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-28 (`F`) |
| M5:ERT-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-29 (`A`) |
| M5:ERT-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-29 (`A`) |
| M5:ERT-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-7 (`A`) |
| M5:ERT-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-10 (`A`) |
| M5:IMPL-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-1 (`A`) |
| M5:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-3 (`F`) |
| M5:NYELV-G1-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TECH-1 (`A`) |
| M5:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-30 (`F`) |
| M5:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-27 (`A`) |
| M5:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-27 (`A`) |
| M5:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-26 (`A`) |
| M5:NYELV-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-26 (`A`) |
| M5:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TECH-1 (`A`) |
| M5:NYELV-G2-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-9 (`A`) |
| M5:NYELV-G2-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-10 (`A`) |
| M5:PED-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-26 (`A`) |
| M5:PED-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TERM-7 (`F`) |
| M5:PED-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-27 (`A`) |
| M5:PED-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-15 (`F`) |
| M5:PED-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-4 (`F`) |
| M5:PED-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-7 (`A`) |
| M5:PED-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-3 (`F`) |
| M5:PED-G2-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-13 (`A`) |
| M5:PED-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M5:QA-PED-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M6:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-8 (`F`) |
| M6:BIZT-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-4 (`F`) |
| M6:BIZT-G1-6 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Jogi jogosult, Memuna, DPO, szerző: SIG-6 (X-3) |
| M6:BIZT-G1-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M6:BIZT-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-16 (`F`) |
| M6:BIZT-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-16 (`F`) |
| M6:BIZT-G2-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M6:BIZT-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-7 (`F`) |
| M6:BIZT-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-10 (`F`) |
| M6:BIZT-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-18 (`F`) |
| M6:BIZT-G3-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-17 (`A`) |
| M6:BIZT-G3-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-8 (`F`) |
| M6:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-31 (`A`) |
| M6:ERT-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-7 (`A`) |
| M6:ERT-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-32 (`F`) |
| M6:ERT-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-34 (`F`) |
| M6:ERT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-6 (`A`) |
| M6:ERT-G2-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M6:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-35 (`A`) |
| M6:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-7 (`A`) |
| M6:ERT-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-36 (`F`) |
| M6:ERT-G3-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-33 (`A`) |
| M6:ERT-G3-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-32 (`F`) |
| M6:IMPL-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-6 (`A`) |
| M6:IMPL-G1-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-4 (`F`) |
| M6:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-4 (`F`) |
| M6:IMPL-G2-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + a11y: RT-4 (X-4) |
| M6:IMPL-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TECH-2 (`F`) |
| M6:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-4 (`F`) |
| M6:NYELV-G1-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-16 (`F`) |
| M6:NYELV-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-6 (`A`) |
| M6:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TECH-2 (`F`) |
| M6:NYELV-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M6:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M6:NYELV-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TECH-2 (`F`) |
| M6:PED-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M6:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-18 (`F`) |
| M6:PED-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-7 (`A`) |
| M6:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M6:PED-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-37 (`A`) |
| M6:PED-G3-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-13 (`A`) |
| M6:QA-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-11 (`F`) |
| M6:QA-BIZT-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-9 (`A`) |
| M6:QA-IMPL-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz TECH-2 (`F`) |
| M7:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-42 (`F`) |
| M7:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-9 (`F`) |
| M7:BIZT-G1-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi: ADV-E3 (X-2) |
| M7:BIZT-G1-4 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-10 (`F`) |
| M7:BIZT-G1-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M7:BIZT-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-5 (`F`) |
| M7:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-10 (`F`) |
| M7:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-12 (`F`) |
| M7:BIZT-G3-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-7 (`F`) |
| M7:BIZT-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-13 (`A`) |
| M7:BIZT-G3-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-3 (`F`) |
| M7:ERT-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-41 (`A`) |
| M7:ERT-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-45 (`A`) |
| M7:ERT-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-6 (`F`) |
| M7:ERT-G1-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Szakmai lektor, assessment, Memuna a gyermekvédelmi résznél: SIG-2 (X-3) |
| M7:ERT-G2-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-49 (`A`) |
| M7:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-4 (`F`) |
| M7:ERT-G3-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M7:ERT-G3-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-15 (`F`) |
| M7:IMPL-G1-11 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + DPO: RT-5 (X-4) |
| M7:IMPL-G1-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-40 (`F`) |
| M7:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-46 (`F`) |
| M7:IMPL-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-5 (`A`) |
| M7:IMPL-G2-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-5 (`F`) |
| M7:IMPL-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + független hozzáférhetőségi QA: RT-6 (X-4) |
| M7:IMPL-G2-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-7 (`F`) |
| M7:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-48 (`A`) |
| M7:IMPL-G2-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-3 (`F`) |
| M7:IMPL-G2-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-4 (`F`) |
| M7:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-6 (`A`) |
| M7:IMPL-G3-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-6 (`F`) |
| M7:IMPL-G3-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-2 (`F`) |
| M7:IMPL-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-8 (`F`) |
| M7:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-14 (`F`) |
| M7:NYELV-G1-16 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-47 (`A`) |
| M7:NYELV-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-41 (`A`) |
| M7:NYELV-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz LMS-5 (`F`) |
| M7:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-41 (`A`) |
| M7:NYELV-G2-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M7:NYELV-G2-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-16 (`F`) |
| M7:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-41 (`A`) |
| M7:NYELV-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-50 (`A`) |
| M7:NYELV-G2-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| M7:NYELV-G3-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M7:NYELV-G3-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-16 (`F`) |
| M7:NYELV-G3-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M7:NYELV-G3-17 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M7:PED-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-43 (`F`) |
| M7:PED-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-44 (`F`) |
| M7:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| M7:PED-G2-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| M7:PED-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-9 (`F`) |
| M7:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-1 (`A`) |
| M7:PED-G3-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-4 (`F`) |
| M7:PED-G3-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-3 (`A`) |
| Z:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-8 (`F`) |
| Z:BIZT-G1-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| Z:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-11 (`F`) |
| Z:BIZT-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-14 (`F`) |
| Z:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-15 (`A`) |
| Z:BIZT-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-4 (`F`) |
| Z:BIZT-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-7 (`A`) |
| Z:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-38 (`A`) |
| Z:ERT-G1-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-39 (`A`) |
| Z:ERT-G1-4 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ERT-3 (`F`) |
| Z:ERT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-6 (`F`) |
| Z:IMPL-G1-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz ADV-3 (`F`) |
| Z:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz GYV-6 (`A`) |
| Z:NYELV-G1-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-16 (`F`) |
| Z:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz VO-1 (`F`) |
| Z:PED-G1-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-2 (`A`) |
| Z:QA-NYELV-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | döntés: HUM 14. szakasz PRG-6 (`F`) |

## Napló

| Idő | Fázis | Esemény |
|---|---|---|
| 2026-10-12 | PREFLIGHT | Munkaág `next-version/AP-2026-10-11-01`, HEAD `beaea60`, tiszta munkafa. Kiinduló gépi állapot: `content_integrity` 0 ERROR; `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` · `LEARNER-RELEASE-VERDICT: NO-GO`. Az előző futás (`AP-2026-10-11-01`) ledgere TERMINAL volt (`beaea60`). Új futás a HUM 14. szakasz 125 döntésének átvezetésére; a felhatalmazás szó szerint: `2026-10-12 Projektgazdai felhatalmazás – a HUM 14. szakasz átvezetése, AP-2026-10-12-01.md`. Findingok: 299 OPEN (lezárt döntés átvezetése), 31 EVIDENCE_GATE. |
| 2026-10-12 | FIX | Fix-tervek mind a 9 modulra (read-only ügynökök, `check_plan` 0 hiba). Alkalmazva: M0 `5484b02`, M5 `aadf41b` (az ERT-28 3 blokkja nem: új itemdöntés kell), M4 `dd64825`, M6 `fbebec0` (a GYV-5 szó szerint, a megállítási protokoll azonosítása nélkül); mind `content_integrity` 0 ERROR, `--pin-visible` a döntés-ID-kkel, `chore(media)` külön. ADV-1 modulközi olvasat: a „csak a mentorod látja” mondat mellé „technikai okból a Moodle rendszergazdája is hozzáférhet” (a döntés: a tájékoztató ne tagadja a technikai admin hozzáférését); az RBAC-igazítás a staging role-matrixig külső függőség. |
| 2026-10-12 | REGRESSION | M0 célzott QA: 18 ID → 13 MEGERŐSÍTVE (2 duplikátum), 2 RÉSZBEN, 4 ELVETVE; 6 objektív javítva `a2445ff`, 5 emberi döntés (QA-BIZT-2/-3/-4, QA-NYELV-3, QA-ERT-1). Riport: `2026-10-12 Célzott QA – M0 átvezetés (5484b02), AP-2026-10-12-01.md`. |
| 2026-10-12 | REGRESSION | M5 célzott QA: 19 ID → 11 MEGERŐSÍTVE, 2 RÉSZBEN, 6 ELVETVE; 9 objektív javítva `9764987`; emberi döntés: QA-ERT-1; bizonyíték-kapu: QA-BIZT-2/-3. M4: 23 ID → 10 MEGERŐSÍTVE, 8 RÉSZBEN, 6 ELVETVE; javítás `64a60d1`; emberi döntés: QA-BIZT-3, QA-BIZT-5. M6: 20 ID → 16 MEGERŐSÍTVE, 3 RÉSZBEN, 1 ELVETVE; javítás `511d9e0`; emberi döntés: QA-BIZT-1…5. Media `b409d02`. |
| 2026-10-12 | FIX | M1 `eb4fa6d` (a terv #39 blokkja nem: a GYV-12 csak az M1.3-at nevezi meg), M2 `147f3c3` (a GYV-5 szó szerint). Pusholva `d473ab6`-ig. |
