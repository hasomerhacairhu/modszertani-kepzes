# AUTOPILOT-LEDGER — a `/course-autopilot` tartós állapota

> **Audit trail, nem kánon, nem tanulói tartalom.** Egy autopilot-futás egyetlen tartós
> állapotnyilvántartása; egyetlen író: a fő session (`Edit`). Formátum és állapotgép:
> `.claude/skills/course-autopilot/ledger.md`. Ellenőrzés: `python3 tools/autopilot_ledger.py
> validate` (szerkezet) · `check` (végállapot) · `next` (folytatás). A ledger nem bizonyíték: minden
> állapotot a fájlban, a diffben vagy a parancskimenetben bizonyítunk, mielőtt ide kerül.
>
> **Aktív futás: `AP-2026-10-12-02`** (`next-version`, célzott kör): a célzott QA 40 emberi döntés-tétele, a HUM 14
> részleges átvezetései és az M7 kapukvíz visszajelzéseinek válaszszivárgása (ERT-5). A felhatalmazás teljes szövege:
> `2026-10-12 Projektgazdai felhatalmazás – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md`. Az előző futás
> (`AP-2026-10-12-01`) ledgere a git-historyban marad (utolsó állapota: `20d29c3`); nyitott tételei ide átkerültek.

## Futás

| Kulcs | Érték |
|---|---|
| Run-ID | AP-2026-10-12-02 |
| Állapot | ACTIVE |
| Változat | next-version |
| Scope | M0-Z célzott kör: az AP-2026-10-12-01 nyitott tételei (BLOCKED_HUMAN, EVIDENCE_GATE), a HUM 14 részleges átvezetései, ERT-5 (M7) |
| Lencsék | pedagogy,assessment,language,safety,implementation |
| Felhatalmazás | next-version — projektgazda, 2026-10-12, szó szerint: „Folytasd a PR #30 fejlesztését a `20d29c3` állapotból. / Dolgozd fel a 40 új QA-döntést és a fennmaradó részleges implementációkat. Kutatással és szakmai indoklással javasolj megoldást, vond össze az átfedéseket, és implementálj mindent, ami a már elfogadott döntések alapján biztonságosan lezárható. / Ne indíts új teljes auditot, és ne nyisd újra a 125 elfogadott döntést. / A valódi szakértői jóváhagyásokat különítsd el. Ellenőrizd külön az M7 kapukvíz visszajelzéseinek válaszszivárgási kockázatát. / Futtasd le a célzott QA-t és a regressziós teszteket, commitolj és pusholj a next-version ágra. / A végén adj rövid, csoportosított listát kizárólag azokról a kérdésekről, amelyekhez tényleges emberi döntés vagy bizonyíték kell. / A PR maradjon draft. Nincs merge, staging deployment vagy learner release.” — fix: igen; commit és push: a next-version ágra; PR #30 draft marad; merge/staging deployment/tanulói release/main/governance-módosítás: nem |
| Munkaág | next-version/AP-2026-10-11-01 |
| Bázis-commit | 20d29c3 |
| Indítva | 2026-10-12 |
| Záró QA | — |
| Korlátok | (1) A 125 elfogadott döntés (HUM 14. szakasz) nem nyílik újra; csak az zárható le, amit a döntés vagy a kánon szövege szó szerint vagy közvetlen következményként megválaszol, bizonyítékkal. (2) Új gyermekvédelmi, eszkalációs, adatvédelmi (jogalap, megőrzés, hozzáférés), AI-, értékelési (küszöb, rubrikaszint, kulcs) vagy pedagógiai szabály, és a szerepköri jóváhagyás: `BLOCKED_HUMAN` / `EVIDENCE_GATE`, kutatott javaslattal, implementáció nélkül. (3) Új teljes audit nincs: a review REUSED, a javítás után célzott QA a diffre. (4) A futó M0/M1 pilot, a `main` és a CC-04 freeze érintetlen; PR #30 draft; merge, staging, learner release nincs. (5) Generált médiát csak a `media_manifest.py build`, látható-szöveg pint csak a `--pin-visible` ír. (6) Hangok csak szerepnéven; VO-szöveg csak VO fix packkel változik. (7) A governance (CLAUDE.md, `.claude/**`) nem változik. |

## Modulok

| Modul | Review | Lencsék | Riport | Review-bázis | Javítás | Bizonyíték | Következő lépés |
|---|---|---|---|---|---|---|---|
| M0 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | NONE_NEEDED | triázs: minden nyitott M0-tétel emberi döntés vagy bizonyíték-kapu (kutatás: `2026-10-13 Nyers kutatási, verifier- és QA-kimenetek, AP-2026-10-12-02.md`); lezárható tétel nincs | — |
| M1 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | DONE | 3b160fc (GYV-11 alpont), 16a9ad9 (M1:QA15-BIZT-1); célzott QA: biztonság, implementáció — QA15/QA16 findingok javítva | — |
| M2 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | DONE | 3b160fc (GYV-19, M2.A:362); célzott QA: biztonság (QA15) — erre a hunkra 0 finding | — |
| M3 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | DONE | 3b160fc (LMS-2 M3.4, JOG-1 hub), 16a9ad9, 11a89b4 (QA15); média 4b188cc, 87c08c1; célzott QA: implementáció, biztonság — QA15 findingok javítva | — |
| M4 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | NONE_NEEDED | triázs: a nyitott M4-tételek emberi döntés, bizonyíték-kapu (verifier C1, C3, C9) vagy VO fix pack (C11); lezárható tétel nincs | — |
| M5 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | NONE_NEEDED | triázs: az M5:IMPL-G2-2 bizonyíték-kapu (verifier C2), a többi emberi döntés; lezárható tétel nincs | — |
| M6 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | DONE | 3b160fc (GYV-5, M6.A:182), 958bced (PRG-5, M6.F:42); média 0b695a0; célzott QA: biztonság, implementáció (QA16) — 0 finding az M6-hunkokra | — |
| M7 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | DONE | 3b160fc (ERT-40, ERT-5), 958bced (ADV-5 a, PRG-5), 11a89b4 (M7:QA15-ERT-1); célzott QA: implementáció (QA15), biztonság (QA16) — findingok javítva | — |
| Z | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | NONE_NEEDED | triázs: minden nyitott Z-tétel emberi döntés vagy bizonyíték-kapu; lezárható tétel nincs | — |
| KANON | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | DONE | 3b160fc (manifest ERT-5), 958bced (ADV-1, ADV-5), 11a89b4, 93da996 (QA16: ADV-5 teljes átvezetés, RR G2, ASSIGN URL-eset, §3 cellák); célzott QA: biztonság, implementáció — QA16 objektív findingok javítva, KANON:QA16-IMPL-2 emberi döntés | — |

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
| X-10 | HUMAN_DECISION | LMS-2 M3.4-rész: az M3.4-EGY-03 Drag & Drop-mellékút megszüntetése | projektgazda / build-felelős: a `tools/test_media_manifest.py` párcseréje egy change setben; vétó: hozzáférhetőségi gazda — átvezetve: 3b160fc, 11a89b4 (média 4b188cc, 87c08c1) | RESOLVED |
| X-11 | HUMAN_DECISION | A célzott QA emberi döntései (a QA14-kulcsú BLOCKED_HUMAN sorok) | a sorban megnevezett szerep: Memuna, DPO / jogi felelős, értékelési felelős, programvezető, build-spec gazda, modulgazda; kutatott, összevont javaslatok: `2026-10-13 Döntési javaslatok – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md` | OPEN |
| X-12 | HUMAN_DECISION | ERT-5 D1/D2: az M7 kapukvíz Review options ablakmátrixa és az első próbálkozás lezárási mechanizmusa | build-spec gazda + értékelési felelős; a dátumoknál a programvezető; utána runtime-visszaolvasás (X-4, RT-P0-19, RT-P0-08) | OPEN |
| X-13 | HUMAN_DECISION | ADV-1 hozzáférési csomag: kiterjedés (H5P-C, QUIZ, GATE-CP), ASSIGN-S/M csoportmód-mechanizmus, második értékelő; ADV-4 utáni technikaválasztás | projektgazda (kiterjedés), LMS-gazda / build-spec gazda (mechanizmus); vétó/QA: DPO / jogi felelős; az ADV-4-nél a runtime után DPO, az M3-nál a Memuna is | OPEN |
| X-14 | HUMAN_DECISION | JOG-1: a jogászi ellenőrzés és a kijelölt felnőtt nyilvántartásának helye | projektgazda (G1 tracker #1 vagy új HUM-sor); utána jogász + Memuna bizonyítéka (X-1) | OPEN |

## Findingok

| Kulcs | Súly | Típus | Verdikt | Állapot | Bizonyíték / döntési igény |
|---|---|---|---|---|---|
| M0:BIZT-1 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M0:BIZT-3 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna: SAFE-7-verdikt (GYV-24, X-1) (GYV-3) |
| M0:BIZT-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna: csoportchat-küszöb az M0-ban (GYV-7) |
| M0:ERT-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Értékelési felelős, 1–2.: Memuna: SIG-1 (X-3) |
| M0:ERT-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: X-9: projektgazda / modulgazda, pilot-visszajelzéssel (PRG-17) |
| M0:IMPL-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + programvezető: RT-1 (X-4) |
| M0:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja; a döntés szerinti feltétel vagy szerepköri bemenet: ken-vezető / mozgalmi felelős megerősítése; terminológiagazda; felhasználó (átnevezés) (TERM-1) |
| M0:PED-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda: tételes vágási terv; programvezető (PRG-1) |
| M1:BIZT-G1-3 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:BIZT-G2-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M1:BIZT-G2-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | ADV-1: a staging role-matrix és a csoport-láthatósági teszt (RA 15, ASSIGN-S/M: 958bced, 93da996) — LMS-gazda, DPO; X-4, G2 POST-BUILD, RT-P0-15 (verifier C7); a mechanizmus-döntés külön: KANON:QA16-IMPL-2 (X-13) |
| M1:BIZT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.3 |
| M1:ERT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:IMPL-G2-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.2 |
| M1:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.3 |
| M1:PED-G3-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-5); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.F |
| M2:BIZT-G1-6 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az LMS-M2-08 megőrzési sora és a „Név (vagy becenév)” mező — DPO / jogi felelős (X-2, X-13); a hozzáférési rész bizonyíték-kapu (verifier C7: staging role-matrix, G2 POST-BUILD, RT-P0-15; LMS-gazda, DPO) |
| M2:BIZT-G1-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M2:BIZT-G2-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | ADV-1: a staging role-matrix és a csoport-láthatósági teszt (RA 15, ASSIGN-S/M: 958bced, 93da996) — LMS-gazda, DPO; X-4, G2 POST-BUILD, RT-P0-15 (verifier C7); a mechanizmus-döntés külön: KANON:QA16-IMPL-2 (X-13) |
| M2:BIZT-G2-4 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna-verdikt (SAFE-7) (GYV-3) |
| M2:BIZT-G2-8 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M2:BIZT-G2-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M2:BIZT-G3-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető (GYV-5); a döntés óvatos alapértelmezése/feltétel nélküli része: 147f3c3 M2.A, fbebec0 M6.A |
| M2:BIZT-G3-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M2:ERT-G1-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M2:IMPL-G1-3 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: build-/LMS-gazda + modulgazda (PRG-9) |
| M2:PED-G1-11 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | ERT-19: SIGNOFF (nem G1–G8) — a modulgazda / értékelési felelős aláírása, utána az M2 KAPU:37 átvezetése; elutasításnál REOPENED — X-3 (verifier C10) |
| M2:PED-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (TERM-8); a döntés óvatos alapértelmezése/feltétel nélküli része: 147f3c3 M2 KAPU |
| M2:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: vágási terv: modulgazda; programvezető (PRG-1) |
| M3:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (helyenkénti verdikt) (GYV-3) |
| M3:BIZT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:BIZT-G1-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda, DPO, Memuna (ADV-4) |
| M3:BIZT-G1-8 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: JOG-1 — a jogászi ellenőrzés és a kijelölt felnőtt nyilvántartásának helye (G1 tracker #1 vagy új HUM-sor) — projektgazda (X-14); utána bizonyíték-kapu: jogász (Gyvt. 17. § címzettek, határidők) + Memuna jóváhagyása (X-1, G1); átvezetve: a JOG-1 ideiglenes rendje az M3 hub :42-ben, a jogászi tagmondat megtartásával (3b160fc, verifier A5/C4; vessző: 16a9ad9) |
| M3:BIZT-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:BIZT-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (formális újranyitás) (GYV-14) |
| M3:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (helyenkénti verdikt) (GYV-3) |
| M3:BIZT-G2-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | ADV-2/ADV-10: a programvezető dokumentációja (F-peula szereposztás, vészhozzáférés, szervezeti fiók), a DPO G2-je (ADV-E1/E2), a csoport-hozzáférési teszt (RT-P0-15, RA 15) — programvezető, DPO, LMS-gazda; X-2, X-4, G2/G3b (verifier C6) |
| M3:BIZT-G2-7 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda, DPO, Memuna (ADV-4); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.4 |
| M3:BIZT-G3-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (helyenkénti verdikt) (GYV-3) |
| M3:BIZT-G3-8 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | ADV-2: a kérdésre („hozzáférhet-e nem mentor képző”) az ADV-2 felel; hiányzik a programvezető dokumentációja és a DPO G2-je — X-2, G2 (verifier C6) |
| M3:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (ERT-7) |
| M3:ERT-G3-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá; 1–5 fős változat (modulgazda), kapacitás és felelős (programvezető); átvezetve: a PRG-5 hiányzási mondata a kötelező M6.F-ben (:42) és M7.F-ben (:36) is (958bced; korábban ce04b9c M3.F, aadf41b M5.F) |
| M3:IMPL-G2-11 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M3:IMPL-G2-14 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M3 modulgazda + értékelési felelős (ERT-23); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.2 |
| M3:IMPL-G2-15 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TERM-4); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3, ce04b9c M3.4, ce04b9c M3.B |
| M3:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | FIXED | LMS-2 M3.4-rész (verifier A1): 3b160fc — M3.4 SLIDE 4 húzásmentes egyetlen út, M3 hub :130, :137; 11a89b4 EGY-04 metaadat; a korábbi részek: ce04b9c M3.2, M3.4, M3, M3 KAPU; célzott QA: implementáció (QA15) |
| M3:IMPL-G2-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető; értékelési felelős; projektgazda (GYV-2) |
| M3:IMPL-G3-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:IMPL-G3-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M3 modulgazda; Memuna (PRG-11); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.A, ce04b9c M3.B |
| M3:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M3:NYELV-G2-15 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M3:PED-G2-1 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna G1-verdiktje (GYV-24, a GYV-6 küszöb-jóváhagyása) — X-1, G1; az RA 9. pont negatív tesztje — LMS-gazda, X-4, G3b (verifier C1; az óvatos alapértelmezés bent: M3.4:12, :63, M4.B:63, GK §4) |
| M3:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M3 modulgazda; programvezető (PRG-1) |
| M4:BIZT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | ADV-3: a DPO adatkör-aláírása a tárolt TEXT-C-re — DPO / jogi felelős, X-2, G2 (ADV-E1) (verifier C3; az ígéret igaz: M4.1:1206, M4.3:650); a narrációs maradék a VO fix packhez tartozik (X-6) |
| M4:BIZT-G1-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | PRG-14 a): a szerző / tananyagfelelős írásos provenance-nyilatkozata az AI-jelölésről — X-3; G-sor nincs rá, a legközelebbi a G2 (tracker #2) (verifier C9) |
| M4:BIZT-G2-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (GYV-3); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.A |
| M4:BIZT-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna G1-verdiktje (GYV-24) — X-1, G1; RA 9. pont negatív teszt — LMS-gazda, X-4, G3b (verifier C1) |
| M4:BIZT-G2-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M4:BIZT-G2-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető; Memuna: a küszöb jóváhagyása (utólagos QA) (GYV-5, GYV-6); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.A, dd64825 M4.B, dd64825 M4.F |
| M4:ERT-G1-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: DPO; modulgazda / projektgazda; VO-gazda (ADV-3); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.1, bdb94ab manifest, bdb94ab RA |
| M4:ERT-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M4:ERT-G1-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M4:ERT-G2-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: build-spec gazda; DPO (ERT-8); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4, dd64825 M4.1, dd64825 M4.2 |
| M4:IMPL-G2-12 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + programvezető + a11y: RT-3 (X-4) |
| M4:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M4:NYELV-G2-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (vágási terv); szerző (:326) (PRG-1) |
| M4:PED-G1-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M4:PED-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (vágási terv); szerző (:326) (PRG-1) |
| M5:BIZT-G1-4 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M5:BIZT-G1-6 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Szakmai lektor: SIG-5 (X-3) |
| M5:ERT-G1-11 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Kijelölt szakmai lektor; M5 assessment QA: SIG-4 (X-3) |
| M5:ERT-G1-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: az ERT-28 új itemet kíván (az M5 terv 22–24. blokkja nincs alkalmazva) — értékelési felelős; /course-develop csomag (X-8) |
| M5:IMPL-G2-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-3: a completion-profilt a valós H5P és az LMS-M5-07 teszt dönti el (RA 4. pont, mindkét út) — LMS-gazda + módszertani lektor, X-4, G3b (verifier C2; óvatos alapértelmezés: M5.3:529, :544, manifest LMS-M5-07) |
| M5:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: a C mondat jóváhagyása – szakmai szerző / értékelési felelős + modulgazda (ERT-30) |
| M5:PED-G1-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: ld. TERM-7; modulgazda + értékelési felelős (PRG-2, TERM-7) |
| M5:PED-G1-3 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: szakmai lektor / M5 szerzője (PRG-15) |
| M5:PED-G1-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M5:PED-G2-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (LMS-3) |
| M5:PED-G2-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (vágási terv; M5.1 részidők vagy metaszám); vétó: programvezető (PRG-1) |
| M5:QA-PED-2 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (vágási terv; M5.1 részidők vagy metaszám); vétó: programvezető (PRG-1) |
| M6:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető; Memuna; elsődleges (M2/M3) kör egységes mondata (GYV-4, GYV-8) |
| M6:BIZT-G1-6 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Jogi jogosult, Memuna, DPO, szerző: SIG-6 (X-3) |
| M6:BIZT-G1-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M6:BIZT-G2-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M6:ERT-G1-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (ERT-7) |
| M6:ERT-G1-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: értékelési felelős + Memuna kalibráció; projektgazda (ERT-32) |
| M6:ERT-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (ERT-34); a döntés óvatos alapértelmezése/feltétel nélküli része: fbebec0 M6 KAPU |
| M6:ERT-G2-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (ERT-36) |
| M6:ERT-G3-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: értékelési felelős + Memuna kalibráció; projektgazda (ERT-32) |
| M6:IMPL-G1-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M6:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda + értékelési felelős; RT-P0-01 (LMS-4); a döntés óvatos alapértelmezése/feltétel nélküli része: fbebec0 M6 KAPU, bdb94ab RA |
| M6:IMPL-G2-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + a11y: RT-4 (X-4) |
| M6:IMPL-G2-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TECH-2) |
| M6:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M6:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TECH-2) |
| M6:NYELV-G1-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M6:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M6:NYELV-G3-3 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TECH-2) |
| M6:PED-G1-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (GYV-18); a döntés óvatos alapértelmezése/feltétel nélküli része: fbebec0 M6.2 |
| M6:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M6 modulgazda; vétó/QA programvezető (PRG-1) |
| M6:QA-IMPL-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TECH-2) |
| M7:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: értékelési felelős + DPO (ERT-42) |
| M7:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + értékelési felelős; projektgazda (GYV-9) |
| M7:BIZT-G1-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi: ADV-E3 (X-2) |
| M7:BIZT-G1-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M7:BIZT-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-5 (b) — kiterjed-e a „válasz nélküli” út a v2 R1 2-es szintjére (M7 KAPU) — értékelési felelős + projektgazda, az ERT-43-mal egy menetben (X-11); (a) átvezetve: 958bced M7.1:236, M7.4:488, manifest LMS-M7-10; 93da996 LMS-M7-10 teljes ADV-5 + gazda, RR G2; (c) bizonyíték-kapu: a GDPR 9. cikk szerinti minősítés DPO / jogi írásos jóváhagyása (X-2, G2) |
| M7:ERT-G1-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Szakmai lektor, assessment, Memuna a gyermekvédelmi résznél: SIG-2 (X-3) |
| M7:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M7:IMPL-G1-11 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + DPO: RT-5 (X-4) |
| M7:IMPL-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + független hozzáférhetőségi QA: RT-6 (X-4) |
| M7:IMPL-G2-12 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-7: a hozzáférhetőségi gazda QA-verdiktje az alt-szövegekről — X-4, G5a/G5b, FINAL_RELEASE_QA (verifier C8; addig a részletes alt az óvatos alapértelmezés) |
| M7:IMPL-G2-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M7:NYELV-G2-13 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M7:NYELV-G2-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M7:NYELV-G3-12 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (PRG-16) |
| M7:NYELV-G3-14 | P2 | objektív | ELVETVE | REJECTED | ELVETVE (verifier B9): az M7.A és az M7.B rendben; az M7.F nyitókérdés–blokkcím eltérése mind a hét F-peula közös sablonja (M1.F–M6.F ellenőrizve), a validált javaslat használhatatlan; változtatás nincs |
| M7:PED-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: projektgazda + értékelési felelős (ERT-43) |
| M7:PED-G2-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + értékelési felelős; projektgazda (GYV-9) |
| M7:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda; programvezető (PRG-1) |
| M7:PED-G3-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| Z:BIZT-G1-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| Z:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + DPO; értékelési felelős (GYV-11); a döntés óvatos alapértelmezése/feltétel nélküli része: c5bc2c4 Z.4 |
| Z:ERT-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: Z:QA14-NYELV-1 — a „Teljesítve” szakaszonkénti vagy egész beadásra szóló mércéje (a manifest LMS-Z-08 mondata addig nincs átvezetve) — értékelési felelős; a többi rész: c5bc2c4 Z, c5bc2c4 Z.4 |
| Z:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M0:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-5 — a „kötelező megállítási protokoll” tartalma, a 2.4 miniprotokoll ennek számít-e, az alacsony kockázat dokumentálása az M0.A-ban — Memuna + programvezető |
| M0:QA14-BIZT-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-23 — ki láthatja alapból a belépőkvíz egyéni válaszait (Responses report), rögzítés az ADV §3-ban, staging-igazolás — DPO + LMS-gazda |
| M0:QA14-BIZT-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-11 — kiterjed-e a közös eszköz-protokoll a nem F-peulás tartalék eszközre (M0.A) — projektgazda; vétó/QA: LMS-gazda + DPO |
| M0:QA14-NYELV-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-23 — mit jelent „a két item nyilvános visszajelzése” — programvezető + Memuna; adatkör: DPO |
| M0:QA14-ERT-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-6 — a fórum megnyitásának visszamenőleges hatása az M0 completionre és az LMS-M1-01 feloldására; a „zárt” állapot Moodle-mechanizmusa — build-spec gazda + LMS-gazda |
| M1:QA14-BIZT-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — az M1.3-NAR-05 `@source` mondata ütközik az ERT-12-vel; csak a VO-úton javítható — médiafelelős / VO-gazda |
| M1:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-11 — a Memuna-eljárás, a korlátozás/helyesbítés, a törlés/megőrzés és a feltárásmentes pótlási út mechanikája — Memuna + DPO; a kapueredményre az értékelési felelős (X-11); átvezetve: a GYV-11 dokumentálási mondata az M1 KAPU:27-ben (3b160fc, verifier A3; „jogosult”: 16a9ad9) |
| M1:QA14-BIZT-6 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-ERT-3 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M2:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-5 — a megállítási protokoll tartalma, az M2.A kockázati besorolása, a :281–283 viszonya — Memuna + programvezető |
| M2:QA14-BIZT-3 | P1 | objektív | MEGERŐSÍTVE | FIXED | GYV-19 (verifier A4: a HUM 14 GYV-19 sora név szerint az M2.A-ra adja; a GK §4.1 csak a Memuna kiváltását zárja ki): 3b160fc — M2.A:362 „azonnal szólj a kijelölt úton a képzőnek és a Memunának.”; célzott QA: biztonság (QA15) 0 finding erre a hunkra |
| M2:QA14-BIZT-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-2 — mi egyenértékű tudásdemonstráció az M2.4 passz-útján — Memuna + programvezető; értékelési felelős |
| M2:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-1 — kiterjed-e a KAPU:24 24 órás megerősítési határidejére — projektgazda, Memuna-QA |
| M2:QA14-BIZT-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-21 — „és felismerhető részlettel sem” a csoportos titoktartási normában (M2.A:177, :410) — Memuna + DPO |
| M2:QA14-BIZT-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M2:QA14-ERT-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-5 — változzon-e a HUB:34 kimeneti célja a fiktív R3-út miatt — projektgazda + értékelési felelős (someres QA: helyi ideológiai felelős) |
| M3:QA14-BIZT-1 | P2 | emberi-döntés | ELVETVE | REJECTED | ELVETVE (verifier B8): a GYV-15 formulája már az M3.3 S3-SAFE dobozában áll (:554, önsértés-szcenárió), a KAPU ITEM 9 bántalmazási eset, a GYV-15 („önsértési eseteknél”) hatókörén kívül; nincs nyitott kérdés |
| M3:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-21 — a „titoktartási ígéret” lefedi-e a hanih titoktartás-kérését; határhelyzetnél mi az R3 Alapszintje (öt hely együtt) — Memuna + értékelési felelős; rubrikaszintnél a projektgazda |
| M3:QA14-BIZT-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)) |
| M3:QA14-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | LMS-2 M3.4-rész (verifier A1): 3b160fc — M3.4 :12, :65, :332, az M3.4-EGY-03 blokk törölve, EGY-04 (:407–431) és ♿ doboz; `legacy-dispositions.json` M3.4-EGY-03 NO_LONGER_REQUIRED; `tools/test_media_manifest.py` párcsere (M3.4-EGY-04); 11a89b4 — EGY-04 purpose és forrásmutatók (M3:QA15-IMPL-1); média: 4b188cc, 87c08c1; célzott QA: implementáció (QA15) |
| M3:QA14-NYELV-13 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-12 — az M3.B 4.3.3 esete négy csoportnál — M3 modulgazda + Memuna |
| M4:QA14-BIZT-1 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M4:QA14-BIZT-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-19 — „a képzőnek és a Memunának” az M4.3 képzésen kívüli hanih-helyzetére is vonatkozik-e — Memuna + projektgazda |
| M4:QA14-BIZT-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — „magadnak” az M4.1-NAR-07 és az M4.3-NAR-03 hangszövegében — médiafelelős / VO-gazda |
| M4:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-7 — az M4.A/M4.B fókuszmondat-kártyája személyes önfeltáró cetli-e — DPO / jogi felelős, Memuna-QA-val |
| M4:QA14-BIZT-8 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M4 átvezetés (dd64825)) |
| M5:QA14-BIZT-2 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M5:QA14-BIZT-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M5 átvezetés (aadf41b)) |
| M5:QA14-ERT-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-26 — a „soronként látható módszertani indok” kalibrációja a meglévő R3 szinteken belül — értékelési felelős; QA: módszertani lektor |
| M6:QA14-BIZT-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-7 — vonatkozik-e a kétlépcsős küszöb az M6.3:749 és az M6.4 6D/ZÁRÓ dobozára — Memuna |
| M6:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-7 — ki adja a „támogató mentorálást” a madrih–hanih viszonyban, kell-e konzultációs út — Memuna |
| M6:QA14-BIZT-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-18 — a KAPU 12. item új szára és ✅-ja; a narráció a VO fix packkal — értékelési felelős + Memuna; a kulcs: projektgazda; VO: médiafelelős |
| M6:QA14-BIZT-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-5 — a 4.3.2/B négy lépése az M6.A megállítási protokollja-e; az egyszemélyes kivétel alkalmazhatósága — Memuna + programvezető (X-11); átvezetve: a GYV-5 létszámnorma-mondata az M6.A:182-ben (3b160fc, verifier A2) |
| M6:QA14-BIZT-5b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-17 — mit jelent a keretben „a kiskorúakra is térjen ki” — Memuna + a peula tartalomfelelőse |
| M6:QA14-BIZT-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0)) |
| M7:QA14-ERT-1b | P2 | objektív | MEGERŐSÍTVE | FIXED | ERT-40 (verifier A6: a manifest LMS-M7-09 és az RA 19. pont szó szerint megválaszolja): 3b160fc — M7 KAPU:53 a „Teljesítve” feltétele és a „Highest grade” kitétel; küszöb, kulcs, próbálkozásszám változatlan; célzott QA: implementáció (QA15) egyezést igazolt |
| M7:QA14-BIZT-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-7 — az M7.B:480 AI-tiltó mondatában a „komoly szorongás” a Memunához vagy a mentorhoz (veszélyeztetettség gyanújánál azonnal a Memunához) menjen — Memuna |
| Z:QA14-NYELV-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-38 — a „Teljesítve” alsó határa: mindhárom szakaszban kell-e értelmezhető tartalom, vagy elég a beadás egészének értelmezhetősége (Z.4:98, :329, :343, :347, :353, HUB:185, manifest LMS-Z-08 együtt) — értékelési felelős; vétó/QA: programvezető |
| Z:QA14-ERT-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-38 — hogyan jelzi a tanuló a passzt, mi a mentor első lépése üres szakasznál — értékelési felelős, a DPO-val |
| Z:QA14-BIZT-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-11 — kiterjed-e a megőrzési kivétel a Z.4 Feedback nyers válaszaira, szabad-e visszakeresni a válaszadót, kell-e tájékoztató mondat a :370-be — Memuna + DPO |
| Z:QA14-BIZT-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-8 — kerüljön-e a Z.3 terepi mintamondatába „közvetlen veszélyben előbb a biztonság és a 112” — Memuna + programvezető |
| Z:QA14-BIZT-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-7 — személyes önfeltáró cetlinek számít-e a Z.A egyszavas szófelhő-cetlije — DPO / jogi felelős |
| Z:QA14-IMPL-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-3 — mit jelent a „kiürítés” (az RA 16 tesztje ezután végrehajtható) — projektgazda mint build-spec gazda; QA: értékelési felelős |
| KANON:QA14-ERT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-9 — hogyan kap az LMS-M3-05 SUBMITTED completiont úgy, hogy a kapukvíz (LMS-M3-06) csak a megerősített rubrika után nyíljon (külön GATE-CP vagy M3-kivétel) — projektgazda mint build-spec gazda; QA: értékelési felelős |
| KANON:QA14-IMPL-7b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-3 — a Z.3 5. dia célmondata kötelező vagy opcionális tanuló-lokális lépés — projektgazda (X-11) |
| KANON:QA14-BIZT-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-1 — kiterjed-e a (c) csoportszűkítés a H5P-C, a QUIZ és a GATE-CP mentori nézetére — projektgazda; vétó/QA: DPO / jogi felelős (X-13; javaslat: `2026-10-13 Döntési javaslatok – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md` D-11); átvezetve: a §3 tábla mindhárom cellája „nyitott: az ADV-1 kiterjedése” (958bced, 93da996) |
| KANON:QA14-BIZT-3b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-10/LMS-8 — kell-e és milyen szöveggel kerüljön a tanulói tájékoztatóba (ADV §11) a képző által közvetített AI-út — programvezető + Moodle-adminisztrátor; vétó/QA: DPO / jogi felelős |
| KANON:QA14-BIZT-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-11 — a „kikerül a Moodle-ből” (HUM-PRIV-01) a GYV-11 szerinti jóváhagyott korlátozást/törlést jelenti-e, az incidensnyilvántartásba mentés után — Memuna + DPO |
| KANON:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-12 — az AI-végpont technikai metaadatainak jogalapja és megőrzési ideje az ADV §3 táblában — DPO / jogi felelős; QA: programvezető |
| M7:G7-ERT5-1 | P1 | objektív | MEGERŐSÍTVE | FIXED | ERT-5 válaszszivárgás (G7 kutatás, verifier A7): a 14 M7-item „Visszajelzés” bekezdése kimondja a kulcsot, opciónkénti visszajelzés nincs; az itemenkénti tanulói (általános) visszajelzés is rejtve a javító próbálkozás lezárásáig: 3b160fc — M7 KAPU:51, :415, manifest QUIZ-M (:18), LMS-M7-07 (:102); ige: 11a89b4 (M7:QA15-ERT-1); egyezik az M3 KAPU:35-tel |
| M7:G7-ERT5-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-5 D1/D2 — hogyan látszik a hibázott kompetencia az első próbálkozás után (Review options „Marks” / „Whether correct”; a Multi-Select részpontja részleges kulcs-információt adhat), és mi zárja le az első próbálkozást („After the quiz is closed” + felhasználói zárási idő) — build-spec gazda + értékelési felelős, a dátumoknál a programvezető (X-12; javaslat: `2026-10-13 Döntési javaslatok – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md` D-23) |
| M7:G7-ERT5-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | ERT-5: a Review options ablakmátrix célverziós visszaolvasása (RT-P0-19, RT-P0-08; RA 19. pont) a D1/D2 után — LMS-gazda, X-4, G3b |
| M1:QA15-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | GYV-11: „jogosult Memuna-eljárás” (HUM 14 GYV-11) — 16a9ad9 M1 KAPU:27, Adatvédelem §5 :153; fő session ellenőrizte |
| M3:QA15-BIZT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | JOG-1: vessző a „hogy” előtt („anélkül, hogy”) — 16a9ad9 M3 hub :42; fő session ellenőrizte |
| M3:QA15-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | LMS-2: az M3.4-EGY-04 purpose és a forrásmutatók (kártyák, „Visszajelzés minták”, „Instrukció”) az elhagyott EGY-03-ból; notes és teszt-docstring „bekerül” — 11a89b4 M3.4 :412–413, :425, `tools/test_media_manifest.py`; fő session ellenőrizte (20d29c3 EGY-03/EGY-04 blokk) |
| M7:QA15-ERT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | ERT-5: „látszik” ige az LMS-M7-07 Review options cellában (mint az M7 KAPU:415) — 11a89b4 manifest :102; a „teljes, opciónkénti” vessző a KAPU-val és a QUIZ-M-mel egyezően marad (nem bizonyított hiba) |
| KANON:QA16-BIZT-1 | P2 | objektív | MEGERŐSÍTVE | FIXED | ADV-5: az LMS-M7-10 sorban a HUM 14 ADV-5 első mondata és a nyitott tétel gazdája, az LMS-M2-07 mintájára — 93da996 manifest :95; fő session ellenőrizte |
| KANON:QA16-BIZT-2 | P2 | objektív | MEGERŐSÍTVE | FIXED | ADV-5: a RELEASE-READINESS G2 nyitott DPO-listája felveszi az LMS-M7-10-et (az LMS-M2-07 mellé) — 93da996 RELEASE-READINESS.md:25; jóváhagyás nincs beírva, a DPO-bizonyíték az M7:BIZT-G1-6 (c) / X-2 |
| KANON:QA16-BIZT-3 | P2 | objektív | MEGERŐSÍTVE | FIXED | ADV-1: az ASSIGN-S/M visszaolvasásban a közvetlen URL-es negatív eset, a TEXT-C feltétel szövegével — 93da996 runtime acceptance :86; URL-paraméter nincs megnevezve |
| KANON:QA16-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = KANON:QA16-BIZT-1 |
| KANON:QA16-IMPL-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az ASSIGN-S/M láthatósági mechanizmusa — Group mode „Separate groups”, a mentor csak csoportba sorolás után kap szerepet (a TEXT-C BIZT-3 mintájára), a második értékelő és az F-peula képzőjének hozzáférése (ADV-2) — LMS-gazda / build-spec gazda; vétó: DPO / jogi felelős (X-13; javaslat: D-11); a csoport nélküli mentor viselkedése az Assignmentnél elsődleges forrással nem igazolt |
| KANON:QA16-IMPL-3 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = KANON:QA16-BIZT-3 |
| KANON:QA16-IMPL-4 | P2 | objektív | MEGERŐSÍTVE | FIXED | ADV-1: az Adatvédelem §3 tábla QUIZ-D/M és GATE-CP cellája „nyitott: az ADV-1 kiterjedése”, mint a H5P-C és a :109 — 93da996 Adatvédelem :116–117; fő session ellenőrizte |

## Napló

| Idő | Fázis | Esemény |
|---|---|---|
| 2026-10-12 | PREFLIGHT | Munkaág `next-version/AP-2026-10-11-01`, HEAD `20d29c3`, tiszta munkafa. Kiinduló gépi állapot: `content_integrity` 0 ERROR; `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` · `LEARNER-RELEASE-VERDICT: NO-GO`. Az előző futás (`AP-2026-10-12-01`) ledgere TERMINAL volt (`20d29c3`). Új célzott futás; a felhatalmazás szó szerint: `2026-10-12 Projektgazdai felhatalmazás – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md`. Átvett nyitott tételek: 134 BLOCKED_HUMAN (ebből 40 a célzott QA-ból), 40 EVIDENCE_GATE. |
| 2026-10-12 | INVENTORY | Review REUSED (új teljes audit nincs). A 174 átvett tétel kilenc kutatási csomagba (G1–G9) sorolva a HUM 14 döntései szerint; tisztán külső, nem kutatott: VO (X-6), TECH-2 (X-7), PRG-4 (X-8), PRG-17 (X-9), GYV-3 Memuna-verdikt, a 40 EVIDENCE_GATE sor. |
| 2026-10-12 | RESEARCH | Kilenc read-only kutató ügynök (G1–G9, elsődleges forrással ahol kellett); G7 külön: az M7 kapukvíz válaszszivárgása (ERT-5). Nyers kimenet: `2026-10-13 Nyers kutatási, verifier- és QA-kimenetek, AP-2026-10-12-02.md`. |
| 2026-10-12 | VERIFY | Adverzális verifier a kutatói „LEZÁRHATÓ” javaslatokra: A (A1–A4, A6 MEGERŐSÍTVE; A5, A7 RÉSZBEN), B (B1, B2, B6, B8, B9 MEGERŐSÍTVE; B5 RÉSZBEN; B3, B4, B7 ELVETVE), C (C1–C3, C6–C9 bizonyíték-kapu; C10 SIGNOFF; C11 VO-pack; C4, C5 RÉSZBEN). |
| 2026-10-12 | FIX | 3b160fc: LMS-2 M3.4, GYV-5, GYV-11, GYV-19, JOG-1 (hozzáadó), ERT-40, ERT-5 (általános visszajelzés); pin; média 4b188cc. |
| 2026-10-12 | QA | Célzott QA a 3b160fc hunkjaira: biztonság (QA15-BIZT-1, -2), implementáció (QA15-IMPL-1, QA15-ERT-1); a fő session mind a négyet a fájlban ellenőrizte. |
| 2026-10-13 | FIX | 958bced: ADV-1 (H5P-C cella, RA 15 ASSIGN-teszt), ADV-5 (a), PRG-5 (M6.F, M7.F); pin; média 0b695a0. 16a9ad9: QA15-BIZT-1, -2. 11a89b4: QA15-IMPL-1, QA15-ERT-1; média 87c08c1. |
| 2026-10-13 | QA | Célzott QA a 958bced+16a9ad9 hunkjaira: biztonság (QA16-BIZT-1…3), implementáció (QA16-IMPL-1…4). Javítva 93da996 (BIZT-1, -2, -3, IMPL-4); IMPL-1, -3 duplikátum; IMPL-2 emberi döntés (X-13). Minden javítás után: content_integrity 0 ERROR, 159 teszt OK, media check OK. |
| 2026-10-13 | REPORT | Kutatott, összevont döntési javaslatok: `2026-10-13 Döntési javaslatok – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md`. 23 emberi döntési csomag (D-01…D-23), 13 bizonyíték-kapu (BK-01…BK-13), 2 külső függőség (KF-01 VO fix pack, KF-02 SIGNOFF); a dokumentum 7. szakasza minden nyitott kulcsot csomaghoz rendel. Új külső kapuk: X-12 (ERT-5 D1/D2), X-13 (ADV-1 hozzáférési csomag), X-14 (JOG-1 nyilvántartás); X-10 RESOLVED. |
