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
| Állapot | FINISHED |
| Változat | next-version |
| Scope | M0-Z (M0, M1, M2, M3, M4, M5, M6, M7, Z) és a közös kánoni fájlok |
| Lencsék | pedagogy,assessment,language,safety,implementation |
| Felhatalmazás | next-version — projektgazda, 2026-10-12, szó szerint: „Indítsd a HUM 14. szakaszban rögzített mind a 125 OWNER_DECIDED döntés teljes átvezetését a `next-version/AP-2026-10-11-01` ágon. / A cél a végleges, szakmailag javított M0–Z tananyag előállítása, nem újabb döntés-előkészítés. / - Mind a 125 döntést dolgozd fel, az A és F döntéseket egyaránt. / - Az F döntéseknél alkalmazd az elfogadott óvatos alapértelmezést, amíg a külső feltétel nem teljesül. / - Hajtsd végre a szükséges tartalmi, értékelési, LMS-specifikációs és kanonikus módosításokat. / - Használd a meglévő review → fix → célzott QA → regresszió workflow-t. Ne kezdj újabb teljes alapreview-t. / - A 16 bizonyítékkaput tartsd nyitva, de ne állítsd le miattuk a függetlenül elvégezhető fejlesztést. / - Minden döntéshez rögzítsd az implementációt, a tesztelést és a fennmaradó külső függőséget. / - A végén futtasd le a teljes elérhető validációt, és adj tételes, 125/125 lefedettségi jelentést. / Dolgozz autonóm módon a teljes implementációs körön. A módosításokat commitold és pushold a next-version ágra. / A `main`, a futó M0/M1 pilot és a CC-04 freeze érintetlen marad. A PR #30 maradjon draft. Merge, staging deployment és learner release nem engedélyezett. / A végén különítsd el az IMPLEMENTED, a QA-ra váró és a külső bizonyítéktól függő tételeket. Ne jelölj semmit teljesítettnek tényleges bizonyíték nélkül.” — fix: igen; commit és push: a next-version ágra; PR #30 draft marad; merge/staging deployment/tanulói release/main/governance-módosítás: nem |
| Munkaág | next-version/AP-2026-10-11-01 |
| Bázis-commit | beaea60 |
| Indítva | 2026-10-12 |
| Záró QA | `33aec89` (a /release-check ellenőrzőlistája, a fő sessionben futtatva) · MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD · LEARNER-RELEASE-VERDICT: NO-GO |
| Korlátok | (1) Bemenet: az `Emberi jóváhagyás szükséges.md` 14. szakasza, 125 `OWNER_DECIDED` döntés; a döntés szövege szó szerint köt; `F` döntésnél a sorban megnevezett óvatos alapértelmezés, amíg a külső feltétel nem teljesül. Új alapreview nincs: a review-t az AP-2026-10-11-01 öt lencséje és a döntési csomag adja (REUSED). (2) A 299 korábbi `BLOCKED_HUMAN` kulcs a lezárt döntéssel javítható: Típus `objektív`, Verdikt `MEGERŐSÍTVE` (lezárt projektgazdai döntés átvezetése, `.claude/rules/safety-and-human-gates.md`); a 31 `EVIDENCE_GATE` kulcs és a 16 bizonyíték-/aláírás-bejegyzés nyitva marad (X-1…X-4). (3) A `main@213a4c5`, a futó M0+M1 pilot és a CC-04 freeze érintetlen; PR #30 draft. (4) Új pedagógiai tartalom (új item, activity, peula, eset) csak a döntés szövege szerinti pontos szöveggel; különben a PRG-4 `/course-develop` csomagjába kerül (a felhasználó indítja, a tervet a projektgazda hagyja jóvá), és a döntés óvatos alapértelmezése érvényes. (5) A `tools/` és a governance nem változik; a TECH-2 átnevezését a felhasználó futtatja a saját termináljában; a VO-1 hangja a VO-gyártási úton készül. (6) Lezárt döntés (HUM 1–14) nem nyílik újra; a szerepek ellenőrzése vétó/QA. (7) Generált médiát csak a `media_manifest.py build`, látható-szöveg pint csak a `--pin-visible` ír. (8) Hangok csak szerepnéven (2026-10-03). |

## Modulok

| Modul | Review | Lencsék | Riport | Review-bázis | Javítás | Bizonyíték | Következő lépés |
|---|---|---|---|---|---|---|---|
| M0 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | fix `5484b02`, media `0eeb225`; QA-fix `a2445ff` (+media `68dc5e9`); kánon `bdb94ab`, `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M0 átvezetés (5484b02), AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |
| M1 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | fix `eb4fa6d`, media `42635db`; QA-fix `7a69b9d` (+media `7de9164`); kánon `bdb94ab`, `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |
| M2 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | fix `147f3c3`, media `d473ab6`; QA-fix `db724db`; kánon `bdb94ab`, `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M2 átvezetés (147f3c3), AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |
| M3 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | fix `ce04b9c`, media `8602d2a`; QA-fix `e0d69d4` (az LMS-2 M3.4-része nem: X-10); kánon `bdb94ab`, `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |
| M4 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | fix `dd64825`, media `adf1f41`; QA-fix `64a60d1` (+media `b409d02`); kánon `bdb94ab`, `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M4 átvezetés (dd64825), AP-2026-10-12-01.md`; `2026-10-12 Célzott QA – M4 átvezetés, nyelvi lencse és verifier, AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |
| M5 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | fix `aadf41b`, media `50f2891`; QA-fix `9764987` (az ERT-28 3 blokkja nem: új itemdöntés); kánon `bdb94ab`, `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M5 átvezetés (aadf41b), AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |
| M6 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | fix `fbebec0`, media `ac49d8b`; QA-fix `511d9e0` (+media `b409d02`); kánon `bdb94ab`, `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M6 átvezetés (fbebec0), AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |
| M7 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | fix `f6e9c6e`, media `ae63490`; QA-fix `0b76212` (+media `7d833d3`); kánon `bdb94ab`, `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |
| Z | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | fix `c5bc2c4`, media `56c0f6b`; QA-fix `a0c0c83` (a manifest LMS-Z-08 ERT-38-mondata nem: Z:QA14-NYELV-1); kánon `bdb94ab`, `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – Z átvezetés (c5bc2c4), AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |
| KANON | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | aa126a5 | DONE | kánoni kör `bdb94ab` (101 kánoni blokk a 9 modultervből, 92 horgonycsoport; a Z#58 és az M3#67 nem); QA-fix `35a9ddd`; célzott QA (3 lencse + verifier): `2026-10-12 Célzott QA – kánoni kör (bdb94ab), AP-2026-10-12-01.md` | nyitott emberi döntések és bizonyíték-kapuk: a Findingok BLOCKED_HUMAN / EVIDENCE_GATE sorai, X-1…X-11 |

## Külső kapuk

| Kulcs | Típus | Tétel | Kell (mit, kitől) | Állapot |
|---|---|---|---|---|
| X-1 | EVIDENCE_GATE | G1: a Memuna írásos „átnéztem” bejegyzése (GYV-24) | Memuna: egyazon végleges SHA-ra szóló, datált „átnéztem” (PT §9.3), SAFE-7 és az 1:1-kulcsok verdiktje, segélyvonalak review-napi ellenőrzése, tracker #1 lezárása | OPEN |
| X-2 | EVIDENCE_GATE | G2: a DPO írásos release-QA-ja (ADV-E1, ADV-E2, ADV-E3) | DPO / jogi felelős: activitynkénti jóváhagyás (adatmezők, szerepek, megőrzés, export, xAPI/LRS, saved-state, backup), teljes adatleltár, HUM-PRIV-04 AI-kapcsolat QA-ja; tracker #2 | OPEN |
| X-3 | SIGNOFF | Szerepköri jóváhagyások (SIG-1…SIG-6) | értékelési felelős, szakmai lektor, Memuna, jogi jogosult, DPO, szerző: a döntési csomag SIG-bejegyzései szerint | OPEN |
| X-4 | RUNTIME | Célkörnyezeti runtime-bizonyíték (RT-1…RT-6) | LMS-gazda / build-felelős, hozzáférhetőségi gazda, DPO a saját részén: RA 1–26. pont, RT-P0-xx és RT-A11Y sorok | OPEN |
| X-5 | HUMAN_DECISION | Szerepköri bemenetek és vétó/QA az `F` döntésekhez | a döntésben megnevezett szerep (Memuna, DPO, jogász, értékelési felelős, modulgazda, programvezető, LMS-gazda); tételesen: `2026-10-12 HUM 14 átvezetés – 125-125 lefedettségi jelentés, AP-2026-10-12-01.md` „Külső bizonyítéktól függő” szakasza és a Findingok BLOCKED_HUMAN sorai | OPEN |
| X-6 | HUMAN_DECISION | VO-1: egyetlen VO fix pack | médiafelelős / VO-gazda: a kimondott szöveget módosító blokkok újrarenderelése, a többi kiejtési azonosságának igazolása; kurzusoldali alkalmazás fix packként | OPEN |
| X-7 | HUMAN_DECISION | TECH-2: az M6.1/M6.2 átnevezése | a felhasználó futtatja az átnevezési commitot a saját termináljában; utána a hivatkozások, a két `tools/` útvonalkulcs, a baseline-sor, a pin és a média egy change setben | OPEN |
| X-8 | HUMAN_DECISION | PRG-4: célzott `/course-develop` csomag | a felhasználó indítja; a csomagtervet a projektgazda hagyja jóvá; új biztonsági vagy értékelési item csak Memuna- / értékelési jóváhagyással | OPEN |
| X-9 | HUMAN_DECISION | PRG-17: az M0.1 SLIDE 5 kérdése | a pilot-visszajelzéssel együtt dönt a projektgazda / modulgazda (CC-04, HUM 13. és 14. szakasz) | OPEN |
| X-10 | HUMAN_DECISION | LMS-2 M3.4-rész: az M3.4-EGY-03 Drag & Drop-mellékút megszüntetése | projektgazda / build-felelős: a `tools/test_media_manifest.py` `M3.4-EGY-03` párjának cseréje (`M3.4-EGY-04`) egy change setben a terv 55–62., 64–65. és 67. blokkjával; vétó: hozzáférhetőségi gazda | OPEN |
| X-11 | HUMAN_DECISION | A célzott QA emberi döntései (a QA14-kulcsú BLOCKED_HUMAN sorok) | a sorban megnevezett szerep: Memuna, DPO / jogi felelős, értékelési felelős, programvezető, build-spec gazda, modulgazda | OPEN |

## Findingok

| Kulcs | Súly | Típus | Verdikt | Állapot | Bizonyíték / döntési igény |
|---|---|---|---|---|---|
| M0:BIZT-1 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M0:BIZT-3 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna: SAFE-7-verdikt (GYV-24, X-1) (GYV-3) |
| M0:BIZT-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna: csoportchat-küszöb az M0-ban (GYV-7) |
| M0:BIZT-7 | P0 | objektív | MEGERŐSÍTVE | FIXED | 5484b02: M0.4, M0, M0.3, M0.A (ADV-6, ERT-1); QA-fix a2445ff |
| M0:BIZT-9 | P1 | objektív | MEGERŐSÍTVE | FIXED | 5484b02: M0.A; bdb94ab: GK (GYV-5); QA-fix a2445ff |
| M0:ERT-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | 5484b02: M0.3, M0.4, M0.1; bdb94ab: manifest (ERT-1, ERT-2); QA-fix a2445ff |
| M0:ERT-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Értékelési felelős, 1–2.: Memuna: SIG-1 (X-3) |
| M0:ERT-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: X-9: projektgazda / modulgazda, pilot-visszajelzéssel (PRG-17) |
| M0:IMPL-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | bdb94ab: manifest (PRG-8); QA-fix a2445ff |
| M0:IMPL-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | 5484b02: M0.2, M0.3, M0.4; bdb94ab: manifest (ERT-1, ERT-2); QA-fix a2445ff |
| M0:IMPL-5 | P1 | objektív | MEGERŐSÍTVE | FIXED | bdb94ab: manifest (PRG-6); QA-fix a2445ff |
| M0:IMPL-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + programvezető: RT-1 (X-4) |
| M0:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | 5484b02: M0 (ERT-11); QA-fix a2445ff |
| M0:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 5484b02: M0.A (PRG-1); QA-fix a2445ff |
| M0:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja; a döntés szerinti feltétel vagy szerepköri bemenet: ken-vezető / mozgalmi felelős megerősítése; terminológiagazda; felhasználó (átnevezés) (TERM-1) |
| M0:NYELV-G2-22 | P2 | objektív | MEGERŐSÍTVE | FIXED | 5484b02: M0.A (PRG-11); QA-fix a2445ff |
| M0:PED-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda: tételes vágási terv; programvezető (PRG-1) |
| M0:PED-8 | P1 | objektív | MEGERŐSÍTVE | FIXED | 5484b02: M0 (GYV-23); QA-fix a2445ff |
| M1:BIZT-G1-3 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:BIZT-G1-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.1 (GYV-13); QA-fix 7a69b9d |
| M1:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.1 (GYV-22); QA-fix 7a69b9d |
| M1:BIZT-G2-1 | P0 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.3, M1; bdb94ab: manifest, PT (ERT-12); QA-fix 7a69b9d |
| M1:BIZT-G2-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.3, M1.4 (GYV-12); QA-fix 7a69b9d |
| M1:BIZT-G2-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M1:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.3 (GYV-12); QA-fix 7a69b9d |
| M1:BIZT-G2-4 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda (role-matrix), DPO (ADV-1); a döntés óvatos alapértelmezése/feltétel nélküli része: bdb94ab ADV |
| M1:BIZT-G2-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU; bdb94ab: ADV (GYV-11); QA-fix 7a69b9d |
| M1:BIZT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.3 |
| M1:BIZT-G3-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.A, M1.B, M1.F (GYV-6); QA-fix 7a69b9d |
| M1:BIZT-G3-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.A, M1.B; bdb94ab: GK (GYV-21); QA-fix 7a69b9d |
| M1:BIZT-G3-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.A; bdb94ab: ADV (ADV-7); QA-fix 7a69b9d |
| M1:BIZT-G3-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.B (GYV-13); QA-fix 7a69b9d |
| M1:ERT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:ERT-G1-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 (PRG-2); QA-fix 7a69b9d |
| M1:ERT-G2-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU, M1.4 (ERT-14); QA-fix 7a69b9d |
| M1:ERT-G2-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU (ERT-15); QA-fix 7a69b9d |
| M1:ERT-G2-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU (ERT-4); QA-fix 7a69b9d |
| M1:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU, M1.4 (ERT-16); QA-fix 7a69b9d |
| M1:IMPL-G1-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.1; bdb94ab: ADV (ADV-4); QA-fix 7a69b9d |
| M1:IMPL-G1-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1, M1.2; bdb94ab: manifest, RA (PRG-9); QA-fix 7a69b9d |
| M1:IMPL-G2-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | bdb94ab: manifest; eb4fa6d: M1 KAPU, M1.4; ce04b9c: M3.4 (ERT-9, LMS-1); QA-fix 7a69b9d |
| M1:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU; bdb94ab: manifest (ERT-9); QA-fix 7a69b9d |
| M1:IMPL-G2-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:IMPL-G3-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | bdb94ab: manifest (PRG-8); QA-fix 7a69b9d |
| M1:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU, M1.4, M1, M1.2 (ERT-13, ERT-16, PRG-16, TERM-2); QA-fix 7a69b9d |
| M1:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.2 |
| M1:NYELV-G2-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU, M1.4 (ERT-16); QA-fix 7a69b9d |
| M1:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.3 |
| M1:NYELV-G2-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU (ERT-17); QA-fix 7a69b9d |
| M1:NYELV-G2-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.3, M1.4 (PRG-16); QA-fix 7a69b9d |
| M1:NYELV-G3-16 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1.A (PRG-16); QA-fix 7a69b9d |
| M1:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 (PRG-2, PRG-9); QA-fix 7a69b9d |
| M1:PED-G2-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 KAPU, M1.3, M1.4, M1.B (ERT-13, PRG-16); QA-fix 7a69b9d |
| M1:PED-G3-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-5); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.F |
| M1:PED-G3-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | eb4fa6d: M1 (PRG-3); QA-fix 7a69b9d |
| M2:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2 KAPU (GYV-1); QA-fix db724db |
| M2:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2 KAPU (GYV-4); QA-fix db724db |
| M2:BIZT-G1-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.1, M2 KAPU (ADV-5); QA-fix db724db |
| M2:BIZT-G1-6 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: staging role-matrix (LMS-gazda), DPO (ADV-1); a döntés óvatos alapértelmezése/feltétel nélküli része: bdb94ab ADV |
| M2:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2; bdb94ab: ADV (ADV-10); QA-fix db724db |
| M2:BIZT-G1-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2 (ADV-13); QA-fix db724db |
| M2:BIZT-G1-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M2:BIZT-G2-1 | P0 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.4; bdb94ab: manifest (GYV-1); QA-fix db724db |
| M2:BIZT-G2-2 | P0 | objektív | MEGERŐSÍTVE | FIXED | bdb94ab: manifest; 147f3c3: M2.4, M2 (GYV-1, GYV-12, GYV-2); QA-fix db724db |
| M2:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda + DPO; staging role-matrix (LMS-gazda), DPO (ADV-1); a döntés óvatos alapértelmezése/feltétel nélküli része: bdb94ab ADV |
| M2:BIZT-G2-4 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna-verdikt (SAFE-7) (GYV-3) |
| M2:BIZT-G2-5 | P1 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.4 (GYV-4); QA-fix db724db |
| M2:BIZT-G2-6 | P1 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.3; bdb94ab: manifest (ADV-5); QA-fix db724db |
| M2:BIZT-G2-8 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M2:BIZT-G2-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M2:BIZT-G3-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.F; bdb94ab: A11Y (ADV-11); QA-fix db724db |
| M2:BIZT-G3-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető (GYV-5); a döntés óvatos alapértelmezése/feltétel nélküli része: 147f3c3 M2.A, fbebec0 M6.A |
| M2:BIZT-G3-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.A (GYV-20); QA-fix db724db |
| M2:BIZT-G3-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.B (GYV-21); QA-fix db724db |
| M2:BIZT-G3-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M2:BIZT-G3-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.A (GYV-19); QA-fix db724db |
| M2:ERT-G1-5 | P1 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2 (TERM-7); QA-fix db724db |
| M2:ERT-G1-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M2:ERT-G3-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.B (PRG-15); QA-fix db724db |
| M2:IMPL-G1-3 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: build-/LMS-gazda + modulgazda (PRG-9) |
| M2:IMPL-G2-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.4, M2; bdb94ab: manifest (ERT-18, GYV-2); QA-fix db724db |
| M2:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | bdb94ab: manifest; 147f3c3: M2.4 (GYV-1, GYV-12); QA-fix db724db |
| M2:IMPL-G3-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.B (PRG-11); QA-fix db724db |
| M2:IMPL-G3-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2 (PRG-3); QA-fix db724db |
| M2:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2 (PRG-16); QA-fix db724db |
| M2:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2 (ADV-13, ERT-20); QA-fix db724db |
| M2:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.4 (TERM-3); QA-fix db724db |
| M2:PED-G1-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: aláírás: modulgazda + értékelési felelős (ERT-19) |
| M2:PED-G1-5 | P1 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2 KAPU (ADV-5); QA-fix db724db |
| M2:PED-G1-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2 KAPU, M2 (ERT-4); QA-fix db724db |
| M2:PED-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (TERM-8); a döntés óvatos alapértelmezése/feltétel nélküli része: 147f3c3 M2 KAPU |
| M2:PED-G2-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.4 (GYV-12); QA-fix db724db |
| M2:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: vágási terv: modulgazda; programvezető (PRG-1) |
| M2:PED-G3-11 | P2 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | már a futás bázisában (`beaea60`) teljesül (PRG-5; a M2 terv lefedettségi sora) |
| M2:QA-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2.A (GYV-13); QA-fix db724db |
| M2:QA-PED-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 147f3c3: M2, M2 KAPU, M2.1, M2.2 (ERT-8, PRG-3); QA-fix db724db |
| M3:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (helyenkénti verdikt) (GYV-3) |
| M3:BIZT-G1-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.1 (GYV-13); QA-fix e0d69d4 |
| M3:BIZT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:BIZT-G1-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda, DPO, Memuna (ADV-4) |
| M3:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 KAPU (ERT-10); QA-fix e0d69d4 |
| M3:BIZT-G1-8 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: jogász, Memuna, projektgazda (JOG-1); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3 |
| M3:BIZT-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:BIZT-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (formális újranyitás) (GYV-14) |
| M3:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (helyenkénti verdikt) (GYV-3) |
| M3:BIZT-G2-4 | P1 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.3 (GYV-4); QA-fix e0d69d4 |
| M3:BIZT-G2-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: programvezető, LMS-gazda, DPO, Memuna (ADV-10, ADV-2); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.4, bdb94ab ADV |
| M3:BIZT-G2-7 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda, DPO, Memuna (ADV-4); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.4 |
| M3:BIZT-G2-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.4 (GYV-3); QA-fix e0d69d4 |
| M3:BIZT-G2-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.3 (GYV-15); QA-fix e0d69d4 |
| M3:BIZT-G3-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (helyenkénti verdikt) (GYV-3) |
| M3:BIZT-G3-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.A (GYV-16); QA-fix e0d69d4 |
| M3:BIZT-G3-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: programvezető, LMS-gazda, DPO, Memuna (ADV-2); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.F, bdb94ab ADV |
| M3:ERT-G1-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 KAPU (ERT-5); QA-fix e0d69d4 |
| M3:ERT-G1-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 KAPU (ERT-21, ERT-22); QA-fix e0d69d4 |
| M3:ERT-G2-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 KAPU, M3.4 (ERT-21); QA-fix e0d69d4 |
| M3:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.2 (PRG-2); QA-fix e0d69d4 |
| M3:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (ERT-7) |
| M3:ERT-G3-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá; a döntés szerinti feltétel vagy szerepköri bemenet: 1–5 fős változat (modulgazda, PRG-4); kapacitás és felelős (programvezető); programvezető; modulgazda (PRG-5); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.F, aadf41b M5.F |
| M3:ERT-G3-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.B (PRG-12); QA-fix e0d69d4 |
| M3:ERT-G3-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 KAPU, M3.4, M3.B (ERT-21); QA-fix e0d69d4 |
| M3:IMPL-G2-11 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M3:IMPL-G2-14 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M3 modulgazda + értékelési felelős (ERT-23); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.2 |
| M3:IMPL-G2-15 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TERM-4); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3, ce04b9c M3.4, ce04b9c M3.B |
| M3:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: az LMS-2 M3.4-része (az M3.4-EGY-03 D&D-mellékút törlése) a `tools/test_media_manifest.py` párjának cseréjére vár; a tools/ ebben a futásban nem változhat — projektgazda / build-felelős; vétó: hozzáférhetőségi gazda; a többi rész: ce04b9c M3.2, ce04b9c M3.4, ce04b9c M3, ce04b9c M3 KAPU |
| M3:IMPL-G2-4 | P1 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.3; bdb94ab: legacy (PRG-9); QA-fix e0d69d4 |
| M3:IMPL-G2-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető; értékelési felelős; projektgazda (GYV-2) |
| M3:IMPL-G2-6 | P1 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.1, M3.2; bdb94ab: manifest, RA (ADV-3); QA-fix e0d69d4 |
| M3:IMPL-G3-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:IMPL-G3-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M3 modulgazda; Memuna (PRG-11); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.A, ce04b9c M3.B |
| M3:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 (ERT-1); QA-fix e0d69d4 |
| M3:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3, M3.1 (PRG-2); QA-fix e0d69d4 |
| M3:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M3:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 (TERM-4); QA-fix e0d69d4 |
| M3:NYELV-G1-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 (JOG-1); QA-fix e0d69d4 |
| M3:NYELV-G2-15 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M3:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.4; bdb94ab: manifest (TERM-5); QA-fix e0d69d4 |
| M3:NYELV-G3-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.F (PRG-3); QA-fix e0d69d4 |
| M3:NYELV-G3-6 | P3 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.A (PRG-16); QA-fix e0d69d4 |
| M3:PED-G1-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3, M3.1 (PRG-2); QA-fix e0d69d4 |
| M3:PED-G2-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető; értékelési felelős; projektgazda (GYV-2) |
| M3:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M3 modulgazda; programvezető (PRG-1) |
| M3:PED-G3-13 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.A (TERM-6); QA-fix e0d69d4 |
| M3:PED-G3-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.B (PRG-12); QA-fix e0d69d4 |
| M3:PED-G3-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 (PRG-3); QA-fix e0d69d4 |
| M3:PED-G3-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.A (PRG-3); QA-fix e0d69d4 |
| M3:QA-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3 KAPU (ERT-10); QA-fix e0d69d4 |
| M4:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: DPO; modulgazda / projektgazda; VO-gazda (ADV-3); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.1 |
| M4:BIZT-G1-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4; bdb94ab: ADV (ADV-9); QA-fix 64a60d1 |
| M4:BIZT-G1-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.3 (GYV-19); QA-fix 64a60d1 |
| M4:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: szerző / médiafelelős (PRG-14) |
| M4:BIZT-G2-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (GYV-3); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.A |
| M4:BIZT-G2-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + completion-QA (GYV-2, GYV-6); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.B |
| M4:BIZT-G2-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.A (ADV-7); QA-fix 64a60d1 |
| M4:BIZT-G2-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.A (ADV-7); QA-fix 64a60d1 |
| M4:BIZT-G2-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M4:BIZT-G2-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető; Memuna: a küszöb jóváhagyása (utólagos QA) (GYV-5, GYV-6); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.A, dd64825 M4.B, dd64825 M4.F |
| M4:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.3 (ERT-25); QA-fix 64a60d1 |
| M4:ERT-G1-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: DPO; modulgazda / projektgazda; VO-gazda (ADV-3); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.1, bdb94ab manifest, bdb94ab RA |
| M4:ERT-G1-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4 (PRG-2); QA-fix 64a60d1 |
| M4:ERT-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M4:ERT-G1-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M4:ERT-G2-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: build-spec gazda; DPO (ERT-8); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4, dd64825 M4.1, dd64825 M4.2 |
| M4:IMPL-G1-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.1, M4.3 (ADV-3); QA-fix 64a60d1 |
| M4:IMPL-G2-12 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + programvezető + a11y: RT-3 (X-4) |
| M4:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M4:NYELV-G1-8 | P2 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | már a futás bázisában (`beaea60`) teljesül (TECH-1; a M4 terv lefedettségi sora) |
| M4:NYELV-G2-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.B (PRG-1, PRG-10); QA-fix 64a60d1 |
| M4:NYELV-G2-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.B (PRG-1); QA-fix 64a60d1 |
| M4:NYELV-G2-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.4 (PRG-16); QA-fix 64a60d1 |
| M4:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.B (PRG-1); QA-fix 64a60d1 |
| M4:NYELV-G2-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (vágási terv); szerző (:326) (PRG-1) |
| M4:PED-G1-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4 (ERT-24); QA-fix 64a60d1 |
| M4:PED-G1-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M4:PED-G2-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.B (PRG-2); QA-fix 64a60d1 |
| M4:PED-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (vágási terv); szerző (:326) (PRG-1) |
| M4:PED-G2-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4, M4.B (PRG-10); QA-fix 64a60d1 |
| M4:PED-G2-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | dd64825: M4.A (ADV-7, PRG-3); QA-fix 64a60d1 |
| M5:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5.2 (GYV-2, GYV-7); QA-fix 9764987 |
| M5:BIZT-G1-4 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M5:BIZT-G1-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5, M5 KAPU, M5.4; bdb94ab: ADV (ADV-9, PRG-10); QA-fix 9764987 |
| M5:BIZT-G1-6 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Szakmai lektor: SIG-5 (X-3) |
| M5:BIZT-G2-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5.A (ADV-7); QA-fix 9764987 |
| M5:BIZT-G2-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5.4; bdb94ab: manifest (ADV-4, ERT-29); QA-fix 9764987 |
| M5:BIZT-G2-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5.F (ADV-8); QA-fix 9764987 |
| M5:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5; bdb94ab: manifest (ERT-3, ERT-6, ERT-9); QA-fix 9764987 |
| M5:ERT-G1-11 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Kijelölt szakmai lektor; M5 assessment QA: SIG-4 (X-3) |
| M5:ERT-G1-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5, M5 KAPU; bdb94ab: manifest (ERT-6); QA-fix 9764987 |
| M5:ERT-G1-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: az ERT-28 új itemet kíván (az M5 terv 22–24. blokkja nincs alkalmazva) — értékelési felelős; /course-develop csomag (X-8) |
| M5:ERT-G2-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5.4 (ERT-29); QA-fix 9764987 |
| M5:ERT-G2-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5.4; bdb94ab: manifest (ERT-29); QA-fix 9764987 |
| M5:ERT-G2-8 | P2 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | már a futás bázisában (`beaea60`) teljesül (ERT-7; a M5 terv lefedettségi sora) |
| M5:ERT-G2-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5, M5 KAPU, M5.4 (ADV-9, PRG-10); QA-fix 9764987 |
| M5:IMPL-G1-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5, M5.1 (ERT-1); QA-fix 9764987 |
| M5:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: valós H5P + LMS-M5-07 teszt (LMS-gazda + lektor); jóváhagyott önellenőrző tartalom (modulgazda) (LMS-3); a döntés óvatos alapértelmezése/feltétel nélküli része: aadf41b M5.3, bdb94ab manifest |
| M5:NYELV-G1-1 | P2 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | már a futás bázisában (`beaea60`) teljesül (TECH-1; a M5 terv lefedettségi sora) |
| M5:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: a C mondat jóváhagyása – szakmai szerző / értékelési felelős + modulgazda (ERT-30) |
| M5:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5 KAPU (ERT-27); QA-fix 9764987 |
| M5:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5 KAPU (ERT-27); QA-fix 9764987 |
| M5:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5, M5 KAPU (ERT-26); QA-fix 9764987 |
| M5:NYELV-G1-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5 (ERT-26); QA-fix 9764987 |
| M5:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | már a futás bázisában (`beaea60`) teljesül (TECH-1; a M5 terv lefedettségi sora) |
| M5:NYELV-G2-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5.B (ADV-9); QA-fix 9764987 |
| M5:NYELV-G2-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5.A, M5.B (PRG-10); QA-fix 9764987 |
| M5:PED-G1-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5, M5 KAPU (ERT-26); QA-fix 9764987 |
| M5:PED-G1-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: ld. TERM-7; modulgazda + értékelési felelős (PRG-2, TERM-7) |
| M5:PED-G1-2 | P2 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | már a futás bázisában (`beaea60`) teljesül (ERT-27; a M5 terv lefedettségi sora) |
| M5:PED-G1-3 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: szakmai lektor / M5 szerzője (PRG-15) |
| M5:PED-G1-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M5:PED-G1-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5 (PRG-7); QA-fix 9764987 |
| M5:PED-G2-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (LMS-3) |
| M5:PED-G2-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | aadf41b: M5.A (PRG-13); QA-fix 9764987 |
| M5:PED-G2-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (vágási terv; M5.1 részidők vagy metaszám); vétó: programvezető (PRG-1) |
| M5:QA-PED-2 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (vágási terv; M5.1 részidők vagy metaszám); vétó: programvezető (PRG-1) |
| M6:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető; Memuna; elsődleges (M2/M3) kör egységes mondata (GYV-4, GYV-8) |
| M6:BIZT-G1-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.1, M6.2, M6.3 (ADV-4, ERT-1, ERT-2); QA-fix 511d9e0 |
| M6:BIZT-G1-6 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Jogi jogosult, Memuna, DPO, szerző: SIG-6 (X-3) |
| M6:BIZT-G1-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M6:BIZT-G2-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.4 (GYV-16); QA-fix 511d9e0 |
| M6:BIZT-G2-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.4 (GYV-16); QA-fix 511d9e0 |
| M6:BIZT-G2-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M6:BIZT-G2-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.2 (GYV-7); QA-fix 511d9e0 |
| M6:BIZT-G2-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.3, M6 (ADV-10); QA-fix 511d9e0 |
| M6:BIZT-G2-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6, M6.2 (GYV-18); QA-fix 511d9e0 |
| M6:BIZT-G3-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.A (GYV-17); QA-fix 511d9e0 |
| M6:BIZT-G3-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.F (ADV-8); QA-fix 511d9e0 |
| M6:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6, M6 KAPU (ERT-31); QA-fix 511d9e0 |
| M6:ERT-G1-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (ERT-7) |
| M6:ERT-G1-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: értékelési felelős + Memuna kalibráció; projektgazda (ERT-32) |
| M6:ERT-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (ERT-34); a döntés óvatos alapértelmezése/feltétel nélküli része: fbebec0 M6 KAPU |
| M6:ERT-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6 KAPU, M6; bdb94ab: manifest (ERT-6, PRG-7); QA-fix 511d9e0 |
| M6:ERT-G2-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6, M6.2, M6.4 (PRG-2); QA-fix 511d9e0 |
| M6:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.4, M6 KAPU (ERT-35); QA-fix 511d9e0 |
| M6:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | már a futás bázisában (`beaea60`) teljesül (ERT-7; a M6 terv lefedettségi sora) |
| M6:ERT-G2-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (ERT-36) |
| M6:ERT-G3-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6, M6 KAPU; bdb94ab: PT (ERT-33); QA-fix 511d9e0 |
| M6:ERT-G3-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: értékelési felelős + Memuna kalibráció; projektgazda (ERT-32) |
| M6:IMPL-G1-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6 KAPU (ERT-6); QA-fix 511d9e0 |
| M6:IMPL-G1-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M6:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda + értékelési felelős; RT-P0-01 (LMS-4); a döntés óvatos alapértelmezése/feltétel nélküli része: fbebec0 M6 KAPU, bdb94ab RA |
| M6:IMPL-G2-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + a11y: RT-4 (X-4) |
| M6:IMPL-G2-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TECH-2) |
| M6:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M6:NYELV-G1-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6 (PRG-16); QA-fix 511d9e0 |
| M6:NYELV-G1-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6 KAPU (ERT-6); QA-fix 511d9e0 |
| M6:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TECH-2) |
| M6:NYELV-G1-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M6:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M6:NYELV-G3-3 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TECH-2) |
| M6:PED-G1-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6, M6.1 (PRG-2); QA-fix 511d9e0 |
| M6:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (GYV-18); a döntés óvatos alapértelmezése/feltétel nélküli része: fbebec0 M6.2 |
| M6:PED-G1-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6 KAPU, M6 (ERT-6, PRG-7); QA-fix 511d9e0 |
| M6:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M6 modulgazda; vétó/QA programvezető (PRG-1) |
| M6:PED-G3-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.B (ERT-37); QA-fix 511d9e0 |
| M6:PED-G3-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6.A (PRG-13); QA-fix 511d9e0 |
| M6:QA-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | ce04b9c: M3.F; fbebec0: M6.F (ADV-11); QA-fix 511d9e0 |
| M6:QA-BIZT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | fbebec0: M6, M6 KAPU, M6.B (ADV-9); QA-fix 511d9e0 |
| M6:QA-IMPL-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TECH-2) |
| M7:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: értékelési felelős + DPO (ERT-42) |
| M7:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + értékelési felelős; projektgazda (GYV-9) |
| M7:BIZT-G1-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi: ADV-E3 (X-2) |
| M7:BIZT-G1-4 | P1 | objektív | MEGERŐSÍTVE | FIXED | bdb94ab: ADV, RA; f6e9c6e: M7, M7.1 (ADV-12, GYV-10, LMS-8); QA-fix 0b76212 |
| M7:BIZT-G1-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M7:BIZT-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: DPO / jogi; projektgazda; értékelési felelős (ADV-5); a döntés óvatos alapértelmezése/feltétel nélküli része: f6e9c6e M7, f6e9c6e M7 KAPU, f6e9c6e M7.1 |
| M7:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7, M7.4 (ADV-10); QA-fix 0b76212 |
| M7:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.2; bdb94ab: ADV, RA, PT (ADV-12, LMS-8); QA-fix 0b76212 |
| M7:BIZT-G3-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.F (GYV-7); QA-fix 0b76212 |
| M7:BIZT-G3-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.A (GYV-13); QA-fix 0b76212 |
| M7:BIZT-G3-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.B (ADV-3); QA-fix 0b76212 |
| M7:ERT-G1-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 KAPU; bdb94ab: manifest (ERT-41); QA-fix 0b76212 |
| M7:ERT-G1-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 KAPU, M7.2 (ERT-45); QA-fix 0b76212 |
| M7:ERT-G1-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7, M7 KAPU, M7.4; bdb94ab: manifest (PRG-6); QA-fix 0b76212 |
| M7:ERT-G1-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Szakmai lektor, assessment, Memuna a gyermekvédelmi résznél: SIG-2 (X-3) |
| M7:ERT-G2-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 KAPU (ERT-49); QA-fix 0b76212 |
| M7:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M7:ERT-G3-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 (ADV-10, PRG-3); QA-fix 0b76212 |
| M7:ERT-G3-6 | P2 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | már a futás bázisában (`beaea60`) teljesül (PRG-15; a M7 terv lefedettségi sora) |
| M7:IMPL-G1-11 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + DPO: RT-5 (X-4) |
| M7:IMPL-G1-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7, M7 KAPU, M7.4; bdb94ab: manifest (ERT-40); QA-fix 0b76212 |
| M7:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7, M7.1 (ERT-46); QA-fix 0b76212 |
| M7:IMPL-G1-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 KAPU; bdb94ab: manifest (ERT-5); QA-fix 0b76212 |
| M7:IMPL-G2-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7, M7.3; bdb94ab: manifest (LMS-5); QA-fix 0b76212 |
| M7:IMPL-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + független hozzáférhetőségi QA: RT-6 (X-4) |
| M7:IMPL-G2-12 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: hozzáférhetőségi gazda (LMS-7) |
| M7:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.2; bdb94ab: manifest (ERT-48); QA-fix 0b76212 |
| M7:IMPL-G2-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.2 (ADV-3); QA-fix 0b76212 |
| M7:IMPL-G2-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M7:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.4 (LMS-6); QA-fix 0b76212 |
| M7:IMPL-G3-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 KAPU, M7.F; bdb94ab: manifest (PRG-6); QA-fix 0b76212 |
| M7:IMPL-G3-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.F (ADV-2); QA-fix 0b76212 |
| M7:IMPL-G3-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | bdb94ab: ADV, manifest; f6e9c6e: M7, M7.2 (ADV-12, ERT-48, LMS-8); QA-fix 0b76212 |
| M7:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.1 (PRG-14); QA-fix 0b76212 |
| M7:NYELV-G1-16 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 KAPU (ERT-47); QA-fix 0b76212 |
| M7:NYELV-G1-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.4 (ERT-41); QA-fix 0b76212 |
| M7:NYELV-G1-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 (LMS-5); QA-fix 0b76212 |
| M7:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.4 (ERT-41); QA-fix 0b76212 |
| M7:NYELV-G2-13 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M7:NYELV-G2-15 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.4 (PRG-16); QA-fix 0b76212 |
| M7:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.4 (ERT-41); QA-fix 0b76212 |
| M7:NYELV-G2-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 KAPU, M7.4 (ERT-50); QA-fix 0b76212 |
| M7:NYELV-G2-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M7:NYELV-G3-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.B (PRG-3); QA-fix 0b76212 |
| M7:NYELV-G3-12 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (PRG-16) |
| M7:NYELV-G3-14 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda; programvezető (PRG-1) |
| M7:NYELV-G3-17 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.B (PRG-3); QA-fix 0b76212 |
| M7:PED-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: projektgazda + értékelési felelős (ERT-43) |
| M7:PED-G1-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7, M7 KAPU (ERT-44); QA-fix 0b76212 |
| M7:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7, M7.1 (PRG-2); QA-fix 0b76212 |
| M7:PED-G2-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7 (PRG-3); QA-fix 0b76212 |
| M7:PED-G2-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + értékelési felelős; projektgazda (GYV-9) |
| M7:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda; programvezető (PRG-1) |
| M7:PED-G3-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M7:PED-G3-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | f6e9c6e: M7.B (PRG-3); QA-fix 0b76212 |
| Z:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z.3 (GYV-8); QA-fix a0c0c83 |
| Z:BIZT-G1-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| Z:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + DPO; értékelési felelős (GYV-11); a döntés óvatos alapértelmezése/feltétel nélküli része: c5bc2c4 Z.4 |
| Z:BIZT-G1-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z, Z.4; bdb94ab: manifest, ADV (ADV-14); QA-fix a0c0c83 |
| Z:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z.4; bdb94ab: manifest, RA (ADV-15); QA-fix a0c0c83 |
| Z:BIZT-G1-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z.1, Z.2, Z.3 (ADV-4, ERT-1); QA-fix a0c0c83 |
| Z:BIZT-G1-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z.A (ADV-7); QA-fix a0c0c83 |
| Z:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: Z:QA14-NYELV-1 — a „Teljesítve” szakaszonkénti vagy egész beadásra szóló mércéje (a manifest LMS-Z-08 mondata addig nincs átvezetve) — értékelési felelős; a többi rész: c5bc2c4 Z, c5bc2c4 Z.4 |
| Z:ERT-G1-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z, Z.4 (ERT-39); QA-fix a0c0c83 |
| Z:ERT-G1-4 | P1 | objektív | MEGERŐSÍTVE | FIXED | bdb94ab: manifest, RA; c5bc2c4: Z.4 (ADV-15, ERT-3); QA-fix a0c0c83 |
| Z:ERT-G1-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z, Z.3, Z.4; bdb94ab: manifest (PRG-6); QA-fix a0c0c83 |
| Z:IMPL-G1-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z.3; bdb94ab: manifest, RA (ADV-3); QA-fix a0c0c83 |
| Z:NYELV-G1-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z.A (GYV-6); QA-fix a0c0c83 |
| Z:NYELV-G1-15 | P2 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z.3 (PRG-16); QA-fix a0c0c83 |
| Z:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| Z:PED-G1-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z (PRG-2); QA-fix a0c0c83 |
| Z:QA-NYELV-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | c5bc2c4: Z, Z.3 (PRG-6); QA-fix a0c0c83 |
| M0:QA14-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | a2445ff (2026-10-12 Célzott QA – M0 átvezetés (5484b02), 1. táblázat) |
| M0:QA14-IMPL-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:QA14-BIZT-1 (2026-10-12 Célzott QA – M0 átvezetés (5484b02)) |
| M0:QA14-NYELV-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M0:QA14-BIZT-1 (2026-10-12 Célzott QA – M0 átvezetés (5484b02)) |
| M0:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-5 — a „kötelező megállítási protokoll” tartalma, a 2.4 miniprotokoll ennek számít-e, az alacsony kockázat dokumentálása az M0.A-ban — Memuna + programvezető |
| M0:QA14-BIZT-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-23 — ki láthatja alapból a belépőkvíz egyéni válaszait (Responses report), rögzítés az ADV §3-ban, staging-igazolás — DPO + LMS-gazda |
| M0:QA14-BIZT-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-11 — kiterjed-e a közös eszköz-protokoll a nem F-peulás tartalék eszközre (M0.A) — projektgazda; vétó/QA: LMS-gazda + DPO |
| M0:QA14-NYELV-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | a2445ff (2026-10-12 Célzott QA – M0 átvezetés (5484b02), 1. táblázat) |
| M0:QA14-NYELV-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-23 — mit jelent „a két item nyilvános visszajelzése” — programvezető + Memuna; adatkör: DPO |
| M0:QA14-NYELV-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | a2445ff (2026-10-12 Célzott QA – M0 átvezetés (5484b02), 1. táblázat) |
| M0:QA14-NYELV-5 | P2 | emberi-döntés | MEGERŐSÍTVE | DUPLICATE | = M0:QA14-BIZT-4 (a verifier szerint beleolvad) |
| M0:QA14-NYELV-6 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M0 átvezetés (5484b02)) |
| M0:QA14-NYELV-7 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M0 átvezetés (5484b02)) |
| M0:QA14-NYELV-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | a2445ff (2026-10-12 Célzott QA – M0 átvezetés (5484b02), 1. táblázat) |
| M0:QA14-NYELV-9 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M0 átvezetés (5484b02)) |
| M0:QA14-IMPL-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | a2445ff (2026-10-12 Célzott QA – M0 átvezetés (5484b02), 1. táblázat) |
| M0:QA14-ERT-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-6 — a fórum megnyitásának visszamenőleges hatása az M0 completionre és az LMS-M1-01 feloldására; a „zárt” állapot Moodle-mechanizmusa — build-spec gazda + LMS-gazda |
| M0:QA14-ERT-2 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M0 átvezetés (5484b02)) |
| M0:QA14-ERT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | a2445ff (2026-10-12 Célzott QA – M0 átvezetés (5484b02), 1. táblázat) |
| M1:QA14-BIZT-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — az M1.3-NAR-05 `@source` mondata ütközik az ERT-12-vel; csak a VO-úton javítható — médiafelelős / VO-gazda |
| M1:QA14-BIZT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-BIZT-3 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:QA14-NYELV-1 (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-BIZT-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-11 — a Memuna-eljárás, a korlátozás/helyesbítés, a törlés/megőrzés és a feltárásmentes pótlási út mechanikája — Memuna + DPO; a kapueredményre az értékelési felelős |
| M1:QA14-BIZT-6 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-ERT-1 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:QA14-NYELV-5 (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-ERT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-ERT-3 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-ERT-4 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-ERT-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-ERT-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-ERT-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-NYELV-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-NYELV-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-NYELV-3 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-NYELV-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-NYELV-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-NYELV-6 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:QA14-ERT-7 (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-NYELV-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-NYELV-8 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-NYELV-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | 7a69b9d (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d), 1. táblázat) |
| M1:QA14-NYELV-10 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-NYELV-11 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M2:QA14-BIZT-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-5 — a megállítási protokoll tartalma, az M2.A kockázati besorolása, a :281–283 viszonya — Memuna + programvezető |
| M2:QA14-BIZT-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-19 — „képzőnek és Memunának” vs a GK §4.1 kizárólagos Memuna-címzettje (M2.A:362; az M4:QA14-BIZT-3-mal együtt) — Memuna |
| M2:QA14-BIZT-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-2 — mi egyenértékű tudásdemonstráció az M2.4 passz-útján — Memuna + programvezető; értékelési felelős |
| M2:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-1 — kiterjed-e a KAPU:24 24 órás megerősítési határidejére — projektgazda, Memuna-QA |
| M2:QA14-BIZT-6 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M2:QA14-BIZT-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-21 — „és felismerhető részlettel sem” a csoportos titoktartási normában (M2.A:177, :410) — Memuna + DPO |
| M2:QA14-BIZT-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-BIZT-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-BIZT-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M2:QA14-ERT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-ERT-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-5 — változzon-e a HUB:34 kimeneti célja a fiktív R3-út miatt — projektgazda + értékelési felelős (someres QA: helyi ideológiai felelős) |
| M2:QA14-ERT-3 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M2:QA14-ERT-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-NYELV-1 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M2:QA14-NYELV-2 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M2:QA14-NYELV-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-NYELV-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-NYELV-5 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M2:QA14-NYELV-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-NYELV-7 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M2:QA14-NYELV-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-NYELV-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | db724db (2026-10-12 Célzott QA – M2 átvezetés (147f3c3), 1. táblázat) |
| M2:QA14-NYELV-10 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M3:QA14-BIZT-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-15 — az M3.3 S3-SAFE doboz és a KAPU ITEM 9 a GYV-15 alá tartozik-e — Memuna; jogi kérdésben a jogi szakértő |
| M3:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-21 — a „titoktartási ígéret” lefedi-e a hanih titoktartás-kérését; határhelyzetnél mi az R3 Alapszintje (öt hely együtt) — Memuna + értékelési felelős; rubrikaszintnél a projektgazda |
| M3:QA14-BIZT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-BIZT-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)) |
| M3:QA14-ERT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-ERT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-ERT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-ERT-5 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)) |
| M3:QA14-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: LMS-2 M3.4-rész — az M3.4-EGY-03 törlése és a ♿ doboz igazítása a `tools/test_media_manifest.py` párjának cseréjével egy change setben (a tools/ ebben a futásban nem változhat) — projektgazda / build-felelős; vétó: hozzáférhetőségi gazda |
| M3:QA14-NYELV-1 | P1 | emberi-döntés | MEGERŐSÍTVE | DUPLICATE | = M3:QA14-BIZT-2 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)) |
| M3:QA14-NYELV-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-NYELV-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-NYELV-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M3:QA14-ERT-3 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)) |
| M3:QA14-NYELV-12 | P2 | emberi-döntés | MEGERŐSÍTVE | DUPLICATE | = M3:QA14-BIZT-1 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)) |
| M3:QA14-BIZT-4 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)) |
| M3:QA14-ERT-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-NYELV-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-NYELV-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-NYELV-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-NYELV-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-NYELV-9 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)) |
| M3:QA14-NYELV-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-NYELV-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | e0d69d4 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c), 1. táblázat) |
| M3:QA14-NYELV-13 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-12 — az M3.B 4.3.3 esete négy csoportnál — M3 modulgazda + Memuna |
| M4:QA14-BIZT-1 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M4:QA14-NYELV-1 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M4:QA14-BIZT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-BIZT-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-19 — „a képzőnek és a Memunának” az M4.3 képzésen kívüli hanih-helyzetére is vonatkozik-e — Memuna + projektgazda |
| M4:QA14-BIZT-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — „magadnak” az M4.1-NAR-07 és az M4.3-NAR-03 hangszövegében — médiafelelős / VO-gazda |
| M4:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-7 — az M4.A/M4.B fókuszmondat-kártyája személyes önfeltáró cetli-e — DPO / jogi felelős, Memuna-QA-val |
| M4:QA14-BIZT-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-BIZT-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-NYELV-9 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:QA14-BIZT-7 |
| M4:QA14-ERT-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-NYELV-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M4:QA14-ERT-4 |
| M4:QA14-NYELV-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-NYELV-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-ERT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-ERT-2 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M4:QA14-ERT-3 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M4:QA14-NYELV-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-NYELV-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 64a60d1 (2026-10-12 Célzott QA – M4 átvezetés (dd64825), 1. táblázat) |
| M4:QA14-NYELV-5 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M4:QA14-NYELV-6 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M4:QA14-NYELV-7 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M4:QA14-BIZT-8 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M5:QA14-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-BIZT-2 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M5:QA14-BIZT-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M5:QA14-ERT-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-26 — a „soronként látható módszertani indok” kalibrációja a meglévő R3 szinteken belül — értékelési felelős; QA: módszertani lektor |
| M5:QA14-ERT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-ERT-3 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M5:QA14-ERT-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-ERT-5 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M5:QA14-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-NYELV-1 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M5:QA14-NYELV-2 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M5:QA14-NYELV-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-NYELV-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-NYELV-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-NYELV-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-NYELV-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-NYELV-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | 9764987 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b), 1. táblázat) |
| M5:QA14-NYELV-9 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M5:QA14-NYELV-10 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M6:QA14-BIZT-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-7 — vonatkozik-e a kétlépcsős küszöb az M6.3:749 és az M6.4 6D/ZÁRÓ dobozára — Memuna |
| M6:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-7 — ki adja a „támogató mentorálást” a madrih–hanih viszonyban, kell-e konzultációs út — Memuna |
| M6:QA14-BIZT-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-18 — a KAPU 12. item új szára és ✅-ja; a narráció a VO fix packkal — értékelési felelős + Memuna; a kulcs: projektgazda; VO: médiafelelős |
| M6:QA14-BIZT-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-5 — a 4.3.2/B négy lépése az M6.A megállítási protokollja-e; az egyszemélyes kivétel alkalmazhatósága — Memuna + programvezető |
| M6:QA14-BIZT-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 M6.A:466 (a keret nem maradhat el, kiskorúakkal sem; GYV-17) (2026-10-12 Célzott QA – M6 átvezetés (fbebec0)) |
| M6:QA14-BIZT-5b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-17 — mit jelent a keretben „a kiskorúakra is térjen ki” — Memuna + a peula tartalomfelelőse |
| M6:QA14-BIZT-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-BIZT-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0)) |
| M6:QA14-ERT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-NYELV-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-NYELV-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-NYELV-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-NYELV-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-NYELV-5 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M6 átvezetés (fbebec0)) |
| M6:QA14-NYELV-6 | P2 | emberi-döntés | MEGERŐSÍTVE | DUPLICATE | = M6:QA14-BIZT-4 |
| M6:QA14-NYELV-7 | P2 | emberi-döntés | MEGERŐSÍTVE | DUPLICATE | = M6:QA14-BIZT-5b |
| M6:QA14-NYELV-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-NYELV-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-NYELV-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M6:QA14-NYELV-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | 511d9e0 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0), 1. táblázat) |
| M7:QA14-NYELV-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-ERT-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M7:QA14-NYELV-2 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-NYELV-6 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-ERT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-ERT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 M7 KAPU:48, :217 (a Q14 csak teljesen helyes válasz esetén számít a 12-es küszöbbe; ERT-40) (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-ERT-1b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-40 — a kézi megerősítés menete, ha a Moodle „Highest grade” szerinti próbálkozása eltér a darabszám szerint teljesítőtől — értékelési felelős; QA: programvezető; platform: LMS-gazda |
| M7:QA14-NYELV-13 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-NYELV-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-NYELV-8 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-ERT-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-BIZT-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-NYELV-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-NYELV-11 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-BIZT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-NYELV-3 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M7:QA14-BIZT-3 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-BIZT-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-NYELV-12 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M7:QA14-BIZT-4 |
| M7:QA14-NYELV-10 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M7:QA14-IMPL-1 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-NYELV-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M7:QA14-IMPL-2 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-IMPL-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-BIZT-7 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M7:QA14-IMPL-3 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-IMPL-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-NYELV-5 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e)) |
| M7:QA14-BIZT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-BIZT-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| M7:QA14-BIZT-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-7 — az M7.B:480 AI-tiltó mondatában a „komoly szorongás” a Memunához vagy a mentorhoz (veszélyeztetettség gyanújánál azonnal a Memunához) menjen — Memuna |
| M7:QA14-NYELV-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 0b76212 (2026-10-12 Célzott QA – M7 átvezetés (f6e9c6e), 1. táblázat) |
| Z:QA14-NYELV-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-38 — a „Teljesítve” alsó határa: mindhárom szakaszban kell-e értelmezhető tartalom, vagy elég a beadás egészének értelmezhetősége (Z.4:98, :329, :343, :347, :353, HUB:185, manifest LMS-Z-08 együtt) — értékelési felelős; vétó/QA: programvezető |
| Z:QA14-ERT-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = Z:QA14-NYELV-1 (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4)) |
| Z:QA14-ERT-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-38 — hogyan jelzi a tanuló a passzt, mi a mentor első lépése üres szakasznál — értékelési felelős, a DPO-val |
| Z:QA14-NYELV-3 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4)) |
| Z:QA14-NYELV-4 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4)) |
| Z:QA14-IMPL-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | a0c0c83 (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4), 1. táblázat) |
| Z:QA14-NYELV-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | a0c0c83 (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4), 1. táblázat) |
| Z:QA14-BIZT-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-11 — kiterjed-e a megőrzési kivétel a Z.4 Feedback nyers válaszaira, szabad-e visszakeresni a válaszadót, kell-e tájékoztató mondat a :370-be — Memuna + DPO |
| Z:QA14-NYELV-5 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4)) |
| Z:QA14-BIZT-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-8 — kerüljön-e a Z.3 terepi mintamondatába „közvetlen veszélyben előbb a biztonság és a 112” — Memuna + programvezető |
| Z:QA14-BIZT-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-7 — személyes önfeltáró cetlinek számít-e a Z.A egyszavas szófelhő-cetlije — DPO / jogi felelős |
| Z:QA14-IMPL-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | a0c0c83 (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4), 1. táblázat) |
| Z:QA14-NYELV-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = Z:QA14-IMPL-4 (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4)) |
| Z:QA14-NYELV-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | a0c0c83 (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4), 1. táblázat) |
| Z:QA14-NYELV-7 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4)) |
| Z:QA14-ERT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | a0c0c83 (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4), 1. táblázat) |
| Z:QA14-IMPL-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | a0c0c83 (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4), 1. táblázat) |
| Z:QA14-IMPL-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-3 — mit jelent a „kiürítés” (az RA 16 tesztje ezután végrehajtható) — projektgazda mint build-spec gazda; QA: értékelési felelős |
| Z:QA14-NYELV-9 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4)) |
| Z:QA14-NYELV-10 | P3 | objektív | MEGERŐSÍTVE | FIXED | a0c0c83 (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4), 1. táblázat) |
| Z:QA14-NYELV-11 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – Z átvezetés (c5bc2c4)) |
| KANON:QA14-ERT-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-ERT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-9 — hogyan kap az LMS-M3-05 SUBMITTED completiont úgy, hogy a kapukvíz (LMS-M3-06) csak a megerősített rubrika után nyíljon (külön GATE-CP vagy M3-kivétel) — projektgazda mint build-spec gazda; QA: értékelési felelős |
| KANON:QA14-NYELV-13 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = KANON:QA14-ERT-1 (2026-10-12 Célzott QA – kánoni kör (bdb94ab)) |
| KANON:QA14-NYELV-9 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-ERT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-ERT-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-IMPL-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-12 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-IMPL-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-14 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-10 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-ERT-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-IMPL-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-IMPL-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-IMPL-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-IMPL-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd manifest BSPEC-02 (a Z.3 és az M7.3 tanuló-lokális lépései a leltárban) (2026-10-12 Célzott QA – kánoni kör (bdb94ab)) |
| KANON:QA14-IMPL-7b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-3 — a Z.3 5. dia célmondata kötelező vagy opcionális tanuló-lokális lépés — projektgazda (X-11) |
| KANON:QA14-NYELV-8 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-11 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-BIZT-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-1 — kiterjed-e a (c) csoportszűkítés a H5P-C, a QUIZ és a GATE-CP mentori nézetére; addig átmeneti szöveg (35a9ddd, ADV §3 :104, :109, §11 :232) — projektgazda; vétó/QA: DPO / jogi felelős |
| KANON:QA14-IMPL-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-BIZT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-5 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-BIZT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd ADV §11 „Ki látja?” (az F-peula képzőjének hiánylistája, ADV-2) (2026-10-12 Célzott QA – kánoni kör (bdb94ab)) |
| KANON:QA14-BIZT-3b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-10/LMS-8 — kell-e és milyen szöveggel kerüljön a tanulói tájékoztatóba (ADV §11) a képző által közvetített AI-út — programvezető + Moodle-adminisztrátor; vétó/QA: DPO / jogi felelős |
| KANON:QA14-NYELV-4 | P2 | objektív | ELVETVE | REJECTED | ELVETVE a verifier szerint (2026-10-12 Célzott QA – kánoni kör (bdb94ab)) |
| KANON:QA14-ERT-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-7 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-BIZT-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-11 — a „kikerül a Moodle-ből” (HUM-PRIV-01) a GYV-11 szerinti jóváhagyott korlátozást/törlést jelenti-e, az incidensnyilvántartásba mentés után — Memuna + DPO |
| KANON:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-12 — az AI-végpont technikai metaadatainak jogalapja és megőrzési ideje az ADV §3 táblában — DPO / jogi felelős; QA: programvezető |
| KANON:QA14-BIZT-6 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |
| KANON:QA14-NYELV-15 | P2 | objektív | MEGERŐSÍTVE | FIXED | 35a9ddd (2026-10-12 Célzott QA – kánoni kör (bdb94ab), 1. táblázat) |

## Napló

| Idő | Fázis | Esemény |
|---|---|---|
| 2026-10-12 | PREFLIGHT | Munkaág `next-version/AP-2026-10-11-01`, HEAD `beaea60`, tiszta munkafa. Kiinduló gépi állapot: `content_integrity` 0 ERROR; `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` · `LEARNER-RELEASE-VERDICT: NO-GO`. Az előző futás (`AP-2026-10-11-01`) ledgere TERMINAL volt (`beaea60`). Új futás a HUM 14. szakasz 125 döntésének átvezetésére; a felhatalmazás szó szerint: `2026-10-12 Projektgazdai felhatalmazás – a HUM 14. szakasz átvezetése, AP-2026-10-12-01.md`. Findingok: 299 OPEN (lezárt döntés átvezetése), 31 EVIDENCE_GATE. |
| 2026-10-12 | FIX | Fix-tervek mind a 9 modulra (read-only ügynökök, `check_plan` 0 hiba). Alkalmazva: M0 `5484b02`, M5 `aadf41b` (az ERT-28 3 blokkja nem: új itemdöntés kell), M4 `dd64825`, M6 `fbebec0` (a GYV-5 szó szerint, a megállítási protokoll azonosítása nélkül); mind `content_integrity` 0 ERROR, `--pin-visible` a döntés-ID-kkel, `chore(media)` külön. ADV-1 modulközi olvasat: a „csak a mentorod látja” mondat mellé „technikai okból a Moodle rendszergazdája is hozzáférhet” (a döntés: a tájékoztató ne tagadja a technikai admin hozzáférését); az RBAC-igazítás a staging role-matrixig külső függőség. |
| 2026-10-12 | REGRESSION | M0 célzott QA: 18 ID → 13 MEGERŐSÍTVE (2 duplikátum), 2 RÉSZBEN, 4 ELVETVE; 6 objektív javítva `a2445ff`, 5 emberi döntés (QA-BIZT-2/-3/-4, QA-NYELV-3, QA-ERT-1). Riport: `2026-10-12 Célzott QA – M0 átvezetés (5484b02), AP-2026-10-12-01.md`. |
| 2026-10-12 | REGRESSION | M5 célzott QA: 19 ID → 11 MEGERŐSÍTVE, 2 RÉSZBEN, 6 ELVETVE; 9 objektív javítva `9764987`; emberi döntés: QA-ERT-1; bizonyíték-kapu: QA-BIZT-2/-3. M4: 23 ID → 10 MEGERŐSÍTVE, 8 RÉSZBEN, 6 ELVETVE; javítás `64a60d1`; emberi döntés: QA-BIZT-3, QA-BIZT-5. M6: 20 ID → 16 MEGERŐSÍTVE, 3 RÉSZBEN, 1 ELVETVE; javítás `511d9e0`; emberi döntés: QA-BIZT-1…5. Media `b409d02`. |
| 2026-10-12 | FIX | M1 `eb4fa6d` (a terv #39 blokkja nem: a GYV-12 csak az M1.3-at nevezi meg), M2 `147f3c3` (a GYV-5 szó szerint). Pusholva `d473ab6`-ig. |
| 2026-10-12 | REGRESSION | M1 célzott QA: 24 ID (verifier), javítás `7a69b9d` (+media `7de9164`); M2: 24 ID, javítás `db724db`; riportok `31ef0f2`. |
| 2026-10-12 | FIX | M3 `ce04b9c` (126 blokk; az LMS-2 M3.4-része nem: a `tools/` teszt név szerint hivatkozik az M3.4-EGY-03-ra, X-10), media `8602d2a`; M7 `f6e9c6e` (116 blokk; az ADV-11 „személyes munkapéldányt nem hoz létre” alakban), media `ae63490`; Z `c5bc2c4` (54 blokk), media `56c0f6b`. Mindegyik után `content_integrity` 0 ERROR, ✅-szám változatlan, `git diff --check` tiszta, pin a döntés-ID-kkel. |
| 2026-10-12 | REGRESSION | M3 célzott QA: 24 ID → javítás `e0d69d4`; M7: 27 ID → `0b76212` (+media `7d833d3`); Z: 21 ID → `a0c0c83`. Riportok: `31ef0f2`, `a89bba9`. |
| 2026-10-12 | FIX | Kánoni kör `bdb94ab`: a 9 modulterv 101 DEFER_CANON blokkja, mindegyik horgony újrabizonyítva, 92 horgonycsoport (8 átfedő összevonva). Az ADV-1 csoportszűkítése a beadásokra; a Z#58 (ERT-38) és az M3#67 (LMS-2) nincs alkalmazva; az M3#96 már a `ce04b9c`-ben. |
| 2026-10-12 | REGRESSION | Kánoni célzott QA: 34 ID (3 lencse, két verifier-csoport) → javítás `35a9ddd` (a `bdb94ab` QUIZ-M oszlophibája is); 6 emberi döntés (ADV-1 kiterjedése, M3 ERT-9 kapuablak, GYV-11 „kikerül”, ADV-12 megőrzés, közvetített AI a tájékoztatóban, Z.3 5. dia besorolása). Riport: `2026-10-12 Célzott QA – kánoni kör (bdb94ab), AP-2026-10-12-01.md`. |
| 2026-10-12 | FIX | ERT-26 kánoni része `33aec89`: a Program terv :183 és a manifest LMS-M5-05/LMS-M5-08 küszöbcellája „minden rubrikasor ≥ Alapszint” (a teljes táblázat alapján), a hubbal és a kapufájllal egyezően. Kánoni blokk nem volt rá tervezve, ezért a kánoni kör kihagyta; a 125/125 visszaolvasás találta meg. Küszöb, R4, szintek és completion változatlan; pin: ERT-26, M5:QA-ERT-2. Célzott értékelési ellenőrzés a három módosított cellára: nincs finding. |
| 2026-10-12 | REPORT | 125/125 lefedettség: három független ellenőrző ügynök döntésenkénti fájl-visszaolvasása, a fő session hat saját visszaolvasása (ERT-17, ERT-20, ERT-25, ERT-27, TECH-1, PRG-10 M4.B) és gépi blokk-nyomkövetés a HEAD-en (728 terv-blokk: 576 szó szerint, 98 a QA-javítás után finomítva, 39 módosított alakban, 15 szándékosan nem; az M1 #39 blokkja a `7a69b9d`-ben került be, M1:QA-BIZT-2). Eredmény: IMPLEMENTED 41, QA-RA VÁR 17, KÜLSŐ BIZONYÍTÉKTÓL FÜGGŐ 67. Riport: `2026-10-12 HUM 14 átvezetés – 125-125 lefedettségi jelentés, AP-2026-10-12-01.md`. A régi 299 OPEN kulcs lezárva (FIXED / ALREADY_FIXED / BLOCKED_HUMAN), a célzott QA 238 új kulcsa felvéve (QA14-előtag; a kánoni kör KANON modulsorral). |
| 2026-10-12 | FINAL-QA | Záró ellenőrzés a `33aec89`-on (a tananyag utolsó változása). A `/release-check` fork kétszer üres eredményt adott vissza, ezért az ellenőrzőlistája a fő sessionben futott: `content_integrity` 0 ERROR (selftest 57/57); média selftest, validate, check, reconcile (0 nem egyeztetett), lint (0 HIGH) OK; 159 unittest OK, skip nélkül; `py_compile` OK; `git diff --check` és `git diff --check origin/main...HEAD` tiszta (az öt QA-riport fájlvégi üres sora javítva: `596c699`); governance-selftestek OK; sandbox aktív. `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` · `LEARNER-RELEASE-VERDICT: NO-GO`. |
