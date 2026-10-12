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
| M0 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |
| M1 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |
| M2 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |
| M3 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |
| M4 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |
| M5 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |
| M6 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |
| M7 | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |
| Z | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |
| KANON | REUSED | pedagogy,assessment,implementation,safety,language | `2026-10-12 Projektgazdai döntési csomag – next-version, AP-2026-10-11-01.md`; `2026-10-12 Projektgazdai döntés – a 125 döntési javaslat elfogadása, AP-2026-10-11-01.md` | 20d29c3 | PENDING | — | triázs: a modul nyitott tételeinek lezárhatósága a 125 döntés alapján |

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
| M0:ERT-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Értékelési felelős, 1–2.: Memuna: SIG-1 (X-3) |
| M0:ERT-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: X-9: projektgazda / modulgazda, pilot-visszajelzéssel (PRG-17) |
| M0:IMPL-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + programvezető: RT-1 (X-4) |
| M0:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja; a döntés szerinti feltétel vagy szerepköri bemenet: ken-vezető / mozgalmi felelős megerősítése; terminológiagazda; felhasználó (átnevezés) (TERM-1) |
| M0:PED-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda: tételes vágási terv; programvezető (PRG-1) |
| M1:BIZT-G1-3 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:BIZT-G2-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M1:BIZT-G2-4 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda (role-matrix), DPO (ADV-1); a döntés óvatos alapértelmezése/feltétel nélküli része: bdb94ab ADV |
| M1:BIZT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.3 |
| M1:ERT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:IMPL-G2-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Moodle/LMS-gazda, a11y szerep, DPO a saját részén: RT-2 (X-4) |
| M1:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.2 |
| M1:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.3 |
| M1:PED-G3-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-5); a döntés óvatos alapértelmezése/feltétel nélküli része: eb4fa6d M1.F |
| M2:BIZT-G1-6 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: staging role-matrix (LMS-gazda), DPO (ADV-1); a döntés óvatos alapértelmezése/feltétel nélküli része: bdb94ab ADV |
| M2:BIZT-G1-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M2:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda + DPO; staging role-matrix (LMS-gazda), DPO (ADV-1); a döntés óvatos alapértelmezése/feltétel nélküli része: bdb94ab ADV |
| M2:BIZT-G2-4 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna-verdikt (SAFE-7) (GYV-3) |
| M2:BIZT-G2-8 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M2:BIZT-G2-9 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi felelős: ADV-E1 (X-2) |
| M2:BIZT-G3-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető (GYV-5); a döntés óvatos alapértelmezése/feltétel nélküli része: 147f3c3 M2.A, fbebec0 M6.A |
| M2:BIZT-G3-7 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO/jogi és programvezető: ADV-E2 (X-2) |
| M2:ERT-G1-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M2:IMPL-G1-3 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: build-/LMS-gazda + modulgazda (PRG-9) |
| M2:PED-G1-11 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: aláírás: modulgazda + értékelési felelős (ERT-19) |
| M2:PED-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (TERM-8); a döntés óvatos alapértelmezése/feltétel nélküli része: 147f3c3 M2 KAPU |
| M2:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: vágási terv: modulgazda; programvezető (PRG-1) |
| M3:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (helyenkénti verdikt) (GYV-3) |
| M3:BIZT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:BIZT-G1-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda, DPO, Memuna (ADV-4) |
| M3:BIZT-G1-8 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: jogász, Memuna, projektgazda (JOG-1); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3 |
| M3:BIZT-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:BIZT-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (formális újranyitás) (GYV-14) |
| M3:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (helyenkénti verdikt) (GYV-3) |
| M3:BIZT-G2-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: programvezető, LMS-gazda, DPO, Memuna (ADV-10, ADV-2); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.4, bdb94ab ADV |
| M3:BIZT-G2-7 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: LMS-gazda, DPO, Memuna (ADV-4); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.4 |
| M3:BIZT-G3-4 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (helyenkénti verdikt) (GYV-3) |
| M3:BIZT-G3-8 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: programvezető, LMS-gazda, DPO, Memuna (ADV-2); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.F, bdb94ab ADV |
| M3:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (ERT-7) |
| M3:ERT-G3-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá; a döntés szerinti feltétel vagy szerepköri bemenet: 1–5 fős változat (modulgazda, PRG-4); kapacitás és felelős (programvezető); programvezető; modulgazda (PRG-5); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.F, aadf41b M5.F |
| M3:IMPL-G2-11 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M3:IMPL-G2-14 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M3 modulgazda + értékelési felelős (ERT-23); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.2 |
| M3:IMPL-G2-15 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: TECH-2 átnevezés (X-7) — a felhasználó futtatja (TERM-4); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3, ce04b9c M3.4, ce04b9c M3.B |
| M3:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: az LMS-2 M3.4-része (az M3.4-EGY-03 D&D-mellékút törlése) a `tools/test_media_manifest.py` párjának cseréjére vár; a tools/ ebben a futásban nem változhat — projektgazda / build-felelős; vétó: hozzáférhetőségi gazda; a többi rész: ce04b9c M3.2, ce04b9c M3.4, ce04b9c M3, ce04b9c M3 KAPU |
| M3:IMPL-G2-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető; értékelési felelős; projektgazda (GYV-2) |
| M3:IMPL-G3-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Memuna: GYV-24 (X-1) |
| M3:IMPL-G3-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M3 modulgazda; Memuna (PRG-11); a döntés óvatos alapértelmezése/feltétel nélküli része: ce04b9c M3.A, ce04b9c M3.B |
| M3:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M3:NYELV-G2-15 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M3:PED-G2-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + programvezető; értékelési felelős; projektgazda (GYV-2) |
| M3:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: M3 modulgazda; programvezető (PRG-1) |
| M4:BIZT-G1-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: DPO; modulgazda / projektgazda; VO-gazda (ADV-3); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.1 |
| M4:BIZT-G1-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: szerző / médiafelelős (PRG-14) |
| M4:BIZT-G2-1 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna (GYV-3); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.A |
| M4:BIZT-G2-10 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: Memuna + completion-QA (GYV-2, GYV-6); a döntés óvatos alapértelmezése/feltétel nélküli része: dd64825 M4.B |
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
| M5:IMPL-G2-2 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: valós H5P + LMS-M5-07 teszt (LMS-gazda + lektor); jóváhagyott önellenőrző tartalom (modulgazda) (LMS-3); a döntés óvatos alapértelmezése/feltétel nélküli része: aadf41b M5.3, bdb94ab manifest |
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
| M7:BIZT-G1-6 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: DPO / jogi; projektgazda; értékelési felelős (ADV-5); a döntés óvatos alapértelmezése/feltétel nélküli része: f6e9c6e M7, f6e9c6e M7 KAPU, f6e9c6e M7.1 |
| M7:ERT-G1-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | Szakmai lektor, assessment, Memuna a gyermekvédelmi résznél: SIG-2 (X-3) |
| M7:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M7:IMPL-G1-11 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + DPO: RT-5 (X-4) |
| M7:IMPL-G2-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda + független hozzáférhetőségi QA: RT-6 (X-4) |
| M7:IMPL-G2-12 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: hozzáférhetőségi gazda (LMS-7) |
| M7:IMPL-G2-5 | P1 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: PRG-4 /course-develop csomag (X-8) — a felhasználó indítja, a tervet a projektgazda hagyja jóvá (PRG-4) |
| M7:NYELV-G2-13 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M7:NYELV-G2-9 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: VO fix pack (X-6) — médiafelelős / VO-gazda (VO-1) |
| M7:NYELV-G3-12 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda (PRG-16) |
| M7:NYELV-G3-14 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: a döntés szerinti feltétel vagy szerepköri bemenet: modulgazda; programvezető (PRG-1) |
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
| M1:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-11 — a Memuna-eljárás, a korlátozás/helyesbítés, a törlés/megőrzés és a feltárásmentes pótlási út mechanikája — Memuna + DPO; a kapueredményre az értékelési felelős |
| M1:QA14-BIZT-6 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M1:QA14-ERT-3 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M1 átvezetés (eb4fa6d)) |
| M2:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-5 — a megállítási protokoll tartalma, az M2.A kockázati besorolása, a :281–283 viszonya — Memuna + programvezető |
| M2:QA14-BIZT-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-19 — „képzőnek és Memunának” vs a GK §4.1 kizárólagos Memuna-címzettje (M2.A:362; az M4:QA14-BIZT-3-mal együtt) — Memuna |
| M2:QA14-BIZT-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-2 — mi egyenértékű tudásdemonstráció az M2.4 passz-útján — Memuna + programvezető; értékelési felelős |
| M2:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-1 — kiterjed-e a KAPU:24 24 órás megerősítési határidejére — projektgazda, Memuna-QA |
| M2:QA14-BIZT-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-21 — „és felismerhető részlettel sem” a csoportos titoktartási normában (M2.A:177, :410) — Memuna + DPO |
| M2:QA14-BIZT-10 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M2 átvezetés (147f3c3)) |
| M2:QA14-ERT-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-5 — változzon-e a HUB:34 kimeneti célja a fiktív R3-út miatt — projektgazda + értékelési felelős (someres QA: helyi ideológiai felelős) |
| M3:QA14-BIZT-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-15 — az M3.3 S3-SAFE doboz és a KAPU ITEM 9 a GYV-15 alá tartozik-e — Memuna; jogi kérdésben a jogi szakértő |
| M3:QA14-BIZT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-21 — a „titoktartási ígéret” lefedi-e a hanih titoktartás-kérését; határhelyzetnél mi az R3 Alapszintje (öt hely együtt) — Memuna + értékelési felelős; rubrikaszintnél a projektgazda |
| M3:QA14-BIZT-5 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M3 átvezetés (ce04b9c)) |
| M3:QA14-IMPL-1 | P2 | objektív | MEGERŐSÍTVE | BLOCKED_HUMAN | EMBERI DÖNTÉS: LMS-2 M3.4-rész — az M3.4-EGY-03 törlése és a ♿ doboz igazítása a `tools/test_media_manifest.py` párjának cseréjével egy change setben (a tools/ ebben a futásban nem változhat) — projektgazda / build-felelős; vétó: hozzáférhetőségi gazda |
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
| M6:QA14-BIZT-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-5 — a 4.3.2/B négy lépése az M6.A megállítási protokollja-e; az egyszemélyes kivétel alkalmazhatósága — Memuna + programvezető |
| M6:QA14-BIZT-5b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-17 — mit jelent a keretben „a kiskorúakra is térjen ki” — Memuna + a peula tartalomfelelőse |
| M6:QA14-BIZT-7 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | szerepköri bizonyíték, G1–G8 (2026-10-12 Célzott QA – M6 átvezetés (fbebec0)) |
| M7:QA14-ERT-1b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-40 — a kézi megerősítés menete, ha a Moodle „Highest grade” szerinti próbálkozása eltér a darabszám szerint teljesítőtől — értékelési felelős; QA: programvezető; platform: LMS-gazda |
| M7:QA14-BIZT-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-7 — az M7.B:480 AI-tiltó mondatában a „komoly szorongás” a Memunához vagy a mentorhoz (veszélyeztetettség gyanújánál azonnal a Memunához) menjen — Memuna |
| Z:QA14-NYELV-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-38 — a „Teljesítve” alsó határa: mindhárom szakaszban kell-e értelmezhető tartalom, vagy elég a beadás egészének értelmezhetősége (Z.4:98, :329, :343, :347, :353, HUB:185, manifest LMS-Z-08 együtt) — értékelési felelős; vétó/QA: programvezető |
| Z:QA14-ERT-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-38 — hogyan jelzi a tanuló a passzt, mi a mentor első lépése üres szakasznál — értékelési felelős, a DPO-val |
| Z:QA14-BIZT-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-11 — kiterjed-e a megőrzési kivétel a Z.4 Feedback nyers válaszaira, szabad-e visszakeresni a válaszadót, kell-e tájékoztató mondat a :370-be — Memuna + DPO |
| Z:QA14-BIZT-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-8 — kerüljön-e a Z.3 terepi mintamondatába „közvetlen veszélyben előbb a biztonság és a 112” — Memuna + programvezető |
| Z:QA14-BIZT-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-7 — személyes önfeltáró cetlinek számít-e a Z.A egyszavas szófelhő-cetlije — DPO / jogi felelős |
| Z:QA14-IMPL-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-3 — mit jelent a „kiürítés” (az RA 16 tesztje ezután végrehajtható) — projektgazda mint build-spec gazda; QA: értékelési felelős |
| KANON:QA14-ERT-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ERT-9 — hogyan kap az LMS-M3-05 SUBMITTED completiont úgy, hogy a kapukvíz (LMS-M3-06) csak a megerősített rubrika után nyíljon (külön GATE-CP vagy M3-kivétel) — projektgazda mint build-spec gazda; QA: értékelési felelős |
| KANON:QA14-IMPL-7b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-3 — a Z.3 5. dia célmondata kötelező vagy opcionális tanuló-lokális lépés — projektgazda (X-11) |
| KANON:QA14-BIZT-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-1 — kiterjed-e a (c) csoportszűkítés a H5P-C, a QUIZ és a GATE-CP mentori nézetére; addig átmeneti szöveg (35a9ddd, ADV §3 :104, :109, §11 :232) — projektgazda; vétó/QA: DPO / jogi felelős |
| KANON:QA14-BIZT-3b | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-10/LMS-8 — kell-e és milyen szöveggel kerüljön a tanulói tájékoztatóba (ADV §11) a képző által közvetített AI-út — programvezető + Moodle-adminisztrátor; vétó/QA: DPO / jogi felelős |
| KANON:QA14-BIZT-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: GYV-11 — a „kikerül a Moodle-ből” (HUM-PRIV-01) a GYV-11 szerinti jóváhagyott korlátozást/törlést jelenti-e, az incidensnyilvántartásba mentés után — Memuna + DPO |
| KANON:QA14-BIZT-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: ADV-12 — az AI-végpont technikai metaadatainak jogalapja és megőrzési ideje az ADV §3 táblában — DPO / jogi felelős; QA: programvezető |

## Napló

| Idő | Fázis | Esemény |
|---|---|---|
| 2026-10-12 | PREFLIGHT | Munkaág `next-version/AP-2026-10-11-01`, HEAD `20d29c3`, tiszta munkafa. Kiinduló gépi állapot: `content_integrity` 0 ERROR; `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` · `LEARNER-RELEASE-VERDICT: NO-GO`. Az előző futás (`AP-2026-10-12-01`) ledgere TERMINAL volt (`20d29c3`). Új célzott futás; a felhatalmazás szó szerint: `2026-10-12 Projektgazdai felhatalmazás – QA-döntések és részleges átvezetések, AP-2026-10-12-02.md`. Átvett nyitott tételek: 134 BLOCKED_HUMAN (ebből 40 a célzott QA-ból), 40 EVIDENCE_GATE. |
