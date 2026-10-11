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
| M0 | VERIFIED | pedagogy,assessment,implementation,safety,language | `2026-10-10 Validált findingok – M0 course-review, B sáv.md`; `2026-10-11 Validált findingok – M0, nyelvi lencse, AP-2026-10-11-01.md` | 82d0c7c (négy lencse); 886165b (language) | PENDING | — | FIX (a review-fázis után) |
| M1 | VERIFIED | pedagogy,assessment,implementation,safety,language | `2026-10-10 Validált findingok – M1 course-review, B sáv.md`; `2026-10-11 Validált findingok – M1, nyelvi lencse, AP-2026-10-11-01.md` | 82d0c7c (négy lencse); 886165b (language) | PENDING | — | RECHECK (12 NEEDS_RECHECK), majd FIX |
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
| X-4 | HUMAN_DECISION | Adatkör, megőrzés, hozzáférés — DPO-döntések | DPO / jogi felelős: `M0:BIZT-7` (a bemutatkozó fórum megőrzési sora és tájékoztatója; a Program terv :228 szerint addig adatgyűjtő activity nem nyitható meg); `M1:BIZT-G2-4` (ASSIGN-M csoportszűkítés, szerkesztő tanári/menedzseri hozzáférés); `M1:IMPL-G1-5` (M1.1 SLIDE 1–2 választós tartalékútjának rögzítése); `M1:BIZT-G3-8` (M1.A Johari-cetlik sorsa, a tábla fotózása); DPO-vétó vagy -rész még: `M1:BIZT-G2-1`, `M1:BIZT-G2-6`, `M1:BIZT-G3-5`, `M1:ERT-G1-3`, `M1:ERT-G2-4`, `M1:IMPL-G2-10`, `M0:PED-8` | OPEN |
| X-5 | HUMAN_DECISION | Gyermekvédelmi szabály-alkalmazás (Memuna, HUM-SAFE-02 QA) | Memuna (egyes tételeknél programvezető, DPO, szakmai lektor): `M0:BIZT-3` (SAFE-7 kiterjed-e az M0.4 SLIDE 3 2. helyzetére), `M0:BIZT-5` (csoportchat-szívatás jelzési küszöbe), `M0:BIZT-9` (két felnőtt az M0.A-n), `M0:PED-8` (egyéni utánkövetés a belépőkvíz 1–2. itemén; adatkör: DPO); `M1:BIZT-G1-4` (Memuna-mondat az M1.1 SLIDE 5 írása előtt), `M1:BIZT-G1-7` (kiskorú madrih önfeltárásának határa), `M1:BIZT-G2-10` (egyedi „nagyon nehéz helyzet” szöveg ↔ támogató blokk), `M1:BIZT-G2-6` (feltárást tartalmazó kapubeadvány kezelése), `M1:BIZT-G3-2` (facilitátori minimum a peulákban), `M1:BIZT-G3-5` (anonimizálási korlát szóbeli példákra), `M1:BIZT-G3-9` (Memuna-utalás az M1.B terepi vállalásánál) | OPEN |
| X-6 | HUMAN_DECISION | Completion- és értékelési jelentésdöntések | projektgazda / build-spec gazda; QA: értékelési felelős, módszertani lektor: `M0:IMPL-3` (H5P-C completion = összefoglaló dia elérése vagy kikényszerített megválaszolás), `M0:ERT-3` (a D-d/D-i pontozatlan-választó elv általános-e); `M1:BIZT-G2-1` (N-1: valós, névtelenített helyzet az LMS-M1-07-ben; DPO-vétó), `M1:PED-G2-1` (az SBI kánoni hossza), `M1:ERT-G2-1` (a kész minta-SBI visszaadásának értékelői szabálya), `M1:ERT-G2-2` (B-sor ↔ hangnem-sor kettős levonás), `M1:IMPL-G2-2` (ASSIGN-M completion, D-h kiterjesztése), `M1:ERT-G2-4` (a KAPU item-bank tanulói activity vagy szerzői pool); `M1:NYELV-G2-4` (KAPU:55 S-„Erős” horgony olvasata; az M1:ERT-G2-5 S-része ettől függ), `M1:NYELV-G2-8` (KAPU:79 zárójel jelentése); `M0:NYELV-G1-14` (a belépőkvíz projektgazdai itemszövegének nyelvi javíthatósága) | OPEN |
| X-7 | EVIDENCE_GATE | Memuna írásos „átnéztem” bejegyzése (G1) | Memuna, G1 (GK :17, tracker #1): `M0:BIZT-1` | OPEN |
| X-8 | RUNTIME | Célkörnyezeti Moodle-visszaolvasás | LMS-gazda, G3b/G4b/G8: `M0:IMPL-9` (a „Segítség és kapcsolatok” blokk kitöltése, RT-17, tanulói fiókkal); `M1:BIZT-G1-3` (RT-P0-24, N-M1-04), `M1:ERT-G1-2` (RT-P0-09/-13/-14, M1.1–M1.2 completion/unlock), `M1:BIZT-G2-2` (RT-P0-15 láthatóság), `M1:IMPL-G2-4` (RT-P0-01/-08/-09/-19, „Allowed attempts”) | OPEN |
| X-9 | SIGNOFF | Értékelési szerepköri QA | értékelési felelős (az 1–2. itemnél Memuna): `M0:ERT-4` (a belépőkvíz projektgazdai itemszövegének utólagos QA-ja; answer key nem változik) | OPEN |
| X-10 | HUMAN_DECISION | Programszintű és modulszerkezeti döntések | programvezető / modulgazda (egyes tételeknél build-felelős, médiafelelős, DPO): `M1:ERT-G1-3` (a hub 4. kompetenciájának záróreflexiós produktuma), `M1:PED-G1-8` (M1.1→M1.2 visszacsatolás, „4/5” mérés), `M1:PED-G3-9` (hub vagy peulafájl az irányadó), `M1:IMPL-G3-8` (PT:219 „Peulák” / „Extra / F-peula” blokk ↔ manifest, N-M4-07); `M1:NYELV-G2-9` (az SBI-sablon S-rése), `M1:NYELV-G3-16` (M1.A:277 „tedd meg nyugodtan”); `M0:NYELV-G2-22` (M0.A:347 „páratlan a létszám”) | OPEN |
| X-11 | HUMAN_DECISION | LMS-konfigurációs döntések | LMS-gazda + DPO + hozzáférhetőségi gazda: `M1:IMPL-G2-10` (az M1.4 kapu „Accepted file types” és fájlszám, korpusz-szinten) | OPEN |
| X-13 | HUMAN_DECISION | Terminológiai / kánoni forrásütközés (modul ↔ Glosszárium) | modulgazda + értékelési felelős, a Glosszárium gazdájával (ken-vezető / mozgalmi felelős QA): `M1:NYELV-G1-14` (SBI „S” = helyzet vagy szituáció); projektgazda (QA: ken-vezető / mozgalmi felelős): `M0:NYELV-G2-11` (a Glosszárium:27 „kerüld” szabálya a kisbetűs „dugma isit vagy” alakra) | OPEN |
| X-12 | EVIDENCE_GATE | DPO írásos jóváhagyása (G2) | DPO, G2: `M1:BIZT-G1-3` (N-M1-04 DPO QA, BIZT-QA-1), `M1:BIZT-G2-2` (LMS-M1-05/-07 adatkezelés, ADV:230) | OPEN |

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
| M0:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (a javítás után Memuna-QA: M0:BIZT-1 / G1) |
| M0:NYELV-G1-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (csak „kisebb tétű”; az M0:ERT-1-gyel egy menetben) |
| M0:NYELV-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (a javítás után Memuna-QA: M0:BIZT-1 / G1) |
| M0:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G1-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (a 45’-es részen az M0:PED-5-tel egy lépésben) |
| M0:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (az M0:PED-10-zel egy lépésben) |
| M0:NYELV-G2-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G2-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (csak a :565 utolsó pontja) |
| M0:NYELV-G2-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G2-16 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (az M0:BIZT-8-cal és az M0:IMPL-7-tel összehangolva) |
| M0:NYELV-G2-17 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G2-18 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (a Z.A négy helye a Z-javítással egy menetben) |
| M0:NYELV-G2-21 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M0:NYELV-G2-11 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a Glosszárium:27 „kerüld” szabálya kiterjed-e a kisbetűs „dugma isit vagy / dugma isit madrih” alakra (M0.2:26, :417; M0.4:25, :154, :248, :293, :296, :486; HUB:144, :238; M0.4-ILL-03; a HUB:235 projektgazdai itemtörzs) — projektgazda; QA: ken-vezető / mozgalmi felelős (X-13) |
| M0:NYELV-G1-14 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a belépőkvíz projektgazdai itemszövege (HUB:180) nyelvileg javítható-e (7. item „a completion állapotát” különírás; 4. item alanya) — projektgazda, az értékelési felelős QA-jával (X-6) |
| M0:NYELV-G2-22 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M0.A:347 „vagy páratlan a létszám” feltételének jelentése — modulgazda / projektgazda (X-10) |
| M0:NYELV-G1-1 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M0:NYELV-G2-11 (az M0.2:26 és a HUB:144 hely átvéve) |
| M0:NYELV-G1-3 | P2 | objektív | ELVETVE | REJECTED | a csatornaszabály szerkezete a korpusz kánoni alakja; a csere szűkítene (verifier) |
| M0:NYELV-G1-4 | P2 | objektív | ELVETVE | REJECTED | közvetlen hangnem, nem magázás (verifier) |
| M0:NYELV-G1-9 | P2 | objektív | ELVETVE | REJECTED | bevett fordulat (verifier) |
| M0:NYELV-G1-10 | P2 | objektív | ELVETVE | REJECTED | H5P típusnév, érvényes Markdown-escape (verifier) |
| M0:NYELV-G1-16 | P2 | objektív | ELVETVE | REJECTED | a nagykötőjel viszonyt is jelöl; preferencia (verifier) |
| M0:NYELV-G1-17 | P2 | objektív | ELVETVE | REJECTED | a beágyazott strong CommonMark szerint helyes (verifier) |
| M0:NYELV-G1-18 | P2 | objektív | ELVETVE | REJECTED | jelentésében többes alany; preferencia (verifier) |
| M0:NYELV-G1-19 | P2 | objektív | ELVETVE | REJECTED | informális, de egyértelmű címke (verifier) |
| M0:NYELV-G1-20 | P2 | objektív | ELVETVE | REJECTED | bevett szerkezet (verifier) |
| M0:NYELV-G2-2 | P2 | objektív | ELVETVE | REJECTED | szabályos különírás, diaszöveg (verifier) |
| M0:NYELV-G2-7 | P2 | objektív | ELVETVE | REJECTED | korpusz-szintű konvenció; a javasolt csere rontana (verifier) |
| M0:NYELV-G2-8 | P2 | objektív | ELVETVE | REJECTED | távirati képzői stílus (verifier) |
| M0:NYELV-G2-9 | P2 | objektív | ELVETVE | REJECTED | a „jelen lenni” kánoni alak (verifier) |
| M0:NYELV-G2-10 | P2 | objektív | ELVETVE | REJECTED | a szakszó megengedett; a csere jelentéseltolás (verifier) |
| M0:NYELV-G2-13 | P2 | objektív | ELVETVE | REJECTED | a hub is „komment”-et ír (verifier) |
| M0:NYELV-G2-15 | P2 | objektív | ELVETVE | REJECTED | szabályos szerkezet (verifier) |
| M0:NYELV-G2-19 | P2 | objektív | ELVETVE | REJECTED | szabályos szórend; a K1 (ERT-1) átírja (verifier) |
| M0:NYELV-G2-20 | P2 | objektív | ELVETVE | REJECTED | szabályos olvasat; nyomtatott biztonsági kártyát írna át (verifier) |
| M1:ERT-G1-1 | P0 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | ebf311e, 96996e2 (N-M1-04, PR #29): M1.1:98 „Moodle-oldali mező és tartalékút nem épül hozzá”, :763/:768 saját jegyzetes alapút, :792–794 a döntés szövege („lehetőleg”: 0 találat); MAN:45, :308; RA 24. pont (:105, LMS-M1-01); HUM 12. szakasz — célzott újraellenőrzés: `2026-10-11 Célzott újraellenőrzés – M1 NEEDS_RECHECK, AP-2026-10-11-01.md` |
| M1:IMPL-G1-2 | P1 | objektív | MEGERŐSÍTVE | ALREADY_FIXED | ebf311e (N-M1-04): HUM 12. szakasz (:576–586) és a `04 Audit` jegyzőkönyv a szó szerinti szöveggel — célzott újraellenőrzés 2026-10-11; a finding CC-04/CC-06 HUM-átvezetési része nem ez a kulcs: = M0:ERT-8 (ott javítandó) |
| M1:PED-G1-4 | P1 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:BIZT-G3-1 | P1 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:BIZT-G2-5 | P1 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:BIZT-G2-3 | P1 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:PED-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:IMPL-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:ERT-G1-3.obj | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:ERT-G1-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (csak az M1.2-rész; az M1.1 Q2-rész elvetve: opciónkénti visszajelzést forrás nem ígér, preferencia) |
| M1:IMPL-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:ERT-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:ERT-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:ERT-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:ERT-G2-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:BIZT-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:PED-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:IMPL-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:IMPL-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:IMPL-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:ERT-G3-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:IMPL-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:BIZT-G3-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:PED-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:BIZT-G3-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:IMPL-G3-4 | P3 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:IMPL-G3-9 | P3 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:PED-G1-8.obj | P2 | objektív | MEGERŐSÍTVE | OPEN | — (recheck 2026-10-11: fennáll; korlát: csak a HUB:102 zárójele, pl. a „besorolás, ” törlése; a :93/:97/:99 és az M1.2 Check érintetlen) |
| M1:BIZT-G3-8.obj | P2 | objektív | MEGERŐSÍTVE | OPEN | — (recheck 2026-10-11: fennáll; korlát: egy képzői hivatkozás az M1.A-ba a HUM-PRIV-02-re és az Adatvédelem 6. szakaszára, legfeljebb a szó szerinti alapértelmezéssel; a cetlik sorsáról semmit nem állít — az a BIZT-G3-8 DPO-kérdése) |
| M1:ERT-G1-11 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: az állítás lényege igaz, a „hasznos információ” laza, de nem hamis; item-írási preferencia (a PED-G1-7 ugyanezt elvetette) |
| M1:ERT-G2-12 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: az M1.4:491–492 nem mond ellent a KAPU:300-nak; a szabály a tanulónak kedvez, kár nem bizonyított |
| M1:ERT-G3-11 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: a KAPU:255, :307 soronkénti M→H→K visszajelzést ír elő minden próbálkozásra; új bukott minta új értékelési tartalom lenne |
| M1:ERT-G3-12 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: bizonyított hiba nélkül elosztó nem cserélhető; item-írási preferencia (a fordítási rész = M1:NYELV-G3-8) |
| M1:IMPL-G3-12 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: múlt idejű történeti metaadat, tanulói/build-hatás nincs |
| M1:IMPL-G3-13 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: a `human` provenance kánonszerű; korpuszszintű minta, nincs szabály, amelyhez képest hibás |
| M1:PED-G3-11 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: az átfedést a forrás deklarálja (M1.A:372); új példa új pedagógiai tartalom; preferencia |
| M1:PED-G3-12 | P2 | objektív | ELVETVE | REJECTED | recheck 2026-10-11: ugyanaz a tényállás, mint az elvetett M1:BIZT-G3-6 (fokozatos nyitás, nem megszegett ígéret) |
| M1:BIZT-G1-2 | P0 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-1 |
| M1:IMPL-G1-1 | P0 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-1 (a javaslat (a), (b), (f) pontja — „beviteli elem nem épül” — nem használható) |
| M1:IMPL-G1-3 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-1 (a MAN:308 datált kiegészítésének módszere ebből) |
| M1:PED-G1-1 | P0 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-1 |
| M1:BIZT-G1-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G1-2 (a mátrix-frissítési javaslat nem használható) |
| M1:ERT-G1-5 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:PED-G1-4 (a mondatcsere-javaslat túlmegy a minimálison) |
| M1:PED-G3-1 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:BIZT-G3-1 |
| M1:ERT-G3-5 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:PED-G1-3 |
| M1:ERT-G1-10 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G1-6 |
| M1:PED-G1-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:IMPL-G1-6 (objektív rész); tárolási rész = M1:IMPL-G1-5; a :80-as rész elvetve (nem bizonyított hiba) |
| M1:BIZT-G1-5 | P1 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-3.obj; a 4. kompetencia adatvédelmi korlátja = M1:ERT-G1-3 |
| M1:IMPL-G1-7 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G1-3.obj (a HUB:81 „6–8 slide” rész nem hiba, elhagyva) |
| M1:PED-G2-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G2-6 (az M1.4-MUNK-01-rész nem bizonyított hiba) |
| M1:IMPL-G2-5 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | szövegrész = M1:ERT-G2-5; megjelenítési rész = M1:ERT-G2-6 |
| M1:PED-G2-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G2-7 |
| M1:ERT-G2-11 | P2 | objektív | — | DUPLICATE | = M1:BIZT-G2-7 (levágott P2, beolvadt) |
| M1:IMPL-G2-9 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:PED-G2-6 |
| M1:PED-G2-11 | P2 | objektív | — | DUPLICATE | = M1:IMPL-G2-6 (levágott P2, beolvadt) |
| M1:PED-G3-2 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:ERT-G3-1 (az (a) rész); a (b) rész (hangnem-kulcspont) elvetve |
| M1:ERT-G3-4 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G3-3 |
| M1:PED-G3-3 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G3-3 (a többletjavaslatok — A–D sarokjelölő, új „→” visszajelzés — nem kellenek) |
| M1:IMPL-G3-11 | P2 | objektív | — | DUPLICATE | = M1:PED-G3-8 (levágott P2, beolvadt) |
| M1:ERT-G3-9 | P3 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G3-4 |
| M1:PED-G3-4 | P3 | objektív | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G3-4 (a „kézjel” alternatíva szerzői választás) |
| M1:ERT-G3-13 | P2 | objektív | — | DUPLICATE | = M1:IMPL-G3-9 (levágott P2, beolvadt) |
| M1:ERT-G1-8 | P2 | objektív | MEGERŐSÍTVE | DUPLICATE | HUB:102-rész = M1:PED-G1-8.obj; a HUB:93 „4/5”-rész = M1:PED-G1-8 |
| M1:PED-G2-12 | P2 | emberi-döntés | — | DUPLICATE | = M1:BIZT-G2-1 (levágott P2, beolvadt) |
| M1:ERT-G1-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G2-1 |
| M1:ERT-G2-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G2-1 |
| M1:ERT-G3-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G2-1 |
| M1:PED-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G2-1 |
| M1:PED-G2-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G2-2 |
| M1:PED-G1-5 | P1 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G1-3 |
| M1:IMPL-G2-3 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | döntési rész = M1:BIZT-G2-4; visszaolvasási rész (RT-P0-15) = M1:BIZT-G2-2 |
| M1:PED-G2-3 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G2-4 |
| M1:IMPL-G2-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:ERT-G2-4 |
| M1:ERT-G3-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:ERT-G3-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:IMPL-G3-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:IMPL-G3-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:IMPL-G3-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:PED-G3-9 |
| M1:BIZT-G1-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:IMPL-G1-5 |
| M1:PED-G1-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:BIZT-G1-7 (a pedagógiai rész — áthelyezés SLIDE 3/4-re — preferencia, elvetve) |
| M1:IMPL-G1-4 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M1:BIZT-G1-3 |
| M1:PED-G1-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M1:BIZT-G1-3 |
| M1:IMPL-G3-2 | P2 | bizonyíték-kapu | MEGERŐSÍTVE | DUPLICATE | = M1:IMPL-G2-4 (az „Allowed attempts” értéke, RT-P0-19; a peula-szöveg szűkítése nem javasolt) |
| M1:BIZT-G2-1 | P0 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: N-1 — kerülhet-e az LMS-M1-07 (M1.3 saját mini-SBI, tárolt, névhez kötött TEXT-C) mezőbe valós, névtelenített helyzet, vagy – mint az M1.4-ben – csak kitalált (MAN:48 nyitott; BSPEC-02 leltár: learner-release emberi döntés) — projektgazda; vétó: DPO (X-6) |
| M1:PED-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az SBI kánoni hossza 2–3 mondat (PT:106/:138/:142, hub, KAPU:21/:197) vagy 1–2 (M1.3:45/:801, M1.4:10/:450, M1.B:359, KAPU 4.1-minta); lezárt döntés nincs, a rubrika a hosszt nem pontozza — projektgazda / modulgazda + értékelési felelős (X-6) |
| M1:ERT-G2-1 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.4:475–476 kész SBI a B kapuhelyzetre — kapjon-e a KAPU §5 értékelői szabályt a minta (közel) szó szerinti visszaadására, és cserélődjön-e a példa (a csere önmagában nem elég, M1.4:457) — értékelési felelős; QA: módszertani lektor (X-6) |
| M1:ERT-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a B-sor („becsúszik egy ítélkező szó”) és a hangnem-sor („enyhe minősítés”) ugyanazt vonja-e le (KAPU:126 „nincs kettős súlyozás”), és a 4.1 határeset-minta B ↔ hangnem indoklása közül melyik érvényes — értékelési felelős + módszertani lektor (X-6) |
| M1:ERT-G1-3 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a hub 4. kompetenciájának „záróreflexiós” produktuma sehol nincs — meglévő elemekre képeződjön le (és kerüljön ki a „reflexiós produktum” kitétel), vagy legyen új lépés; tárolt produktumként új adatkör (HUM-PRIV-01/DPO) — programvezető; DPO, ha tárolt (objektív része: M1:ERT-G1-3.obj) (X-10) |
| M1:IMPL-G2-2 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az LMS-M1-05 (ASSIGN-M) saját completion-beállítása nincs rögzítve; kiterjeszthető-e a D-h kétállapotú mintája (SUBMITTED / CONFIRMED) az ASSIGN-M sorokra (a D-f szó szerint nem fedi) — projektgazda / build-spec gazda (X-6) |
| M1:BIZT-G2-4 | P1 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.4:502 „a kijelölt mentorod/értékelőd látja” mögött nyitott az ASSIGN-M csoport szerinti szűkítése (BIZT-5) és a szerkesztő tanári/menedzseri hozzáférés (BIZT-2) (ADV:104, :117); a mondat a döntés előtt nem változik — DPO (X-4) |
| M1:ERT-G2-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU §3 item-bankja tanulói activity (manifest-sor: profil, completion, privacy a szabad szöveges Item 5–6-ra) vagy szerzői itempool (a KAPU:11/:28/:200/:308 igazodik) — projektgazda + értékelési felelős; DPO, ha activity (X-6) |
| M1:PED-G1-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a hub M1.1→M1.2 visszacsatolást és Johari-felidézést ígér (HUB:97/:99), és „4/5”-öt mér (HUB:93), a leckében egyik sincs — bekerüljön (Moodle-intróba), vagy a hub igazodjon — programvezető (objektív része: M1:PED-G1-8.obj) (X-10) |
| M1:PED-G3-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: modulon belül a hub vagy a részletes peulafájl az irányadó — M1.A percbontás (hub:147–151), M1.F fogalomtérkép-poszter és „cél 4” (hub:172–203, :221–222), M1.B-végi analitikai kérdés (hub:275–278) — modulgazda / programvezető (a poszterről médiafelelős) (X-10) |
| M1:IMPL-G3-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a PT:219 minden modulban „Peulák” és „Extra / F-peula” Moodle-blokkot ír, a manifest egyiket sem (MAN:114, :248) — MAN-bővítés vagy PT-pontosítás, programszintű, az N-M4-07-hez kötve — programvezető + build-felelős (X-10) |
| M1:IMPL-G2-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.4 kapu fájlos útjának „Accepted file types” és fájlszám-beállítása (üres mező = minden típus), a „két egyenértékű út” akadálymentességére figyelve; korpusz-szintű hiány — LMS-gazda + DPO + hozzáférhetőségi gazda (X-11) |
| M1:IMPL-G1-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: megengedett-e, hogy az M1.1 SLIDE 1–2 érzelmi önbevallásának választós tartalékútja követett H5P-C-ben tanulónként rögzítsen (a próbálkozás-riportot a nem szerkesztő tanár is látja, ADV:115; a D-d/D-i, a D-j és az N-M1-04 nem fedi) — DPO; addig a build a nem rögzítő szöveg + Tovább utat követheti (X-4) |
| M1:BIZT-G1-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kapjon-e az M1.1 SLIDE 5 a mező (írás) előtt feltárást a Memunához irányító mondatot a Z.2:307 mintájára; „csak nálad marad” mondat az RT-P0-24 visszaolvasásáig tilos — Memuna. A hely a 82d0c7c óta változott (M1.1:763, :768; ebf311e, 96996e2: alapból nincs beviteli elem, „a saját jegyzetedbe … Nem kell beküldened”); a jegyzőkönyv 3. szakasza szerint a kérdés nyitott (X-5) |
| M1:BIZT-G1-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.1:926 a (kiskorú) madrih önfeltárását a kvucához való közelség eszközeként keretezi határ-mondat nélkül — kell-e határ az M1.A:282 mintájára (az M1 nincs a Memuna G1-hatókörében, GK:17) — Memuna + szakmai lektor (X-5) |
| M1:BIZT-G2-10 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.3:914–916 és az M1.4:506–507 egyedi „ha nagyon nehéz helyzet” szövege kiváltandó támogató blokk (Gyermekvédelem §4.3:102), vagy feladatszintű adattakarékossági utasítás; az M1.4:508 Memuna-mondata nem törölhető — Memuna (X-5) |
| M1:BIZT-G2-6 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU:27 eszkalációjánál ki és hogyan veszi ki a feltárást tartalmazó beadványt (ADV:75), mi lesz a kapueredménnyel, és mi az alternatív beadási út (az M3-ra N-9-ként nyitott) — Memuna + DPO; értékelési felelős (X-5) |
| M1:BIZT-G3-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: mi lesz az M1.A önfeltáró Johari-cetlijeivel a peula után (kézírásos plakát, név nélküli munkalap vagy visszaadás), és fotózható-e a tábla — DPO (a HUM:149-hivatkozás átvezetése: M1:BIZT-G3-8.obj) (X-4) |
| M1:BIZT-G3-2 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a peulák képzői in-the-moment utasításának (M1.A:503–505, M1.B:389–391, M1.F:107) szó szerint át kell-e vennie a HUM-SAFE-03 facilitátori minimumát (felkavart kiskorút nem küldünk ki egyedül), vagy elég a képzőképzés (HUM-SAFE-05) — Memuna (X-5) |
| M1:BIZT-G3-5 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kiterjedjen-e a „név és felismerhető részlet nélkül” korlát a szóbeli peula-példákra (M1.A:372 „a saját kvucádra szabva”, M1.B:157) — Memuna + DPO (X-5) |
| M1:BIZT-G3-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: kell-e az M1.B 4.4.2 terepi SBI-vállalásához „valódi gyermekvédelmi aggálynál vond be a Memunát” utalás (az M1.4:508 ugyanennek a tanulónak kimondja) — Memuna (X-5) |
| M1:BIZT-G1-3 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda (RT-P0-24, G3b); DPO (G2): N-M1-04 — az M1.1 H5P-C a SLIDE 5 szövegét nem tárolja-e (próbálkozás-riport, mentett állapot/`enablesavestate`, mentori hozzáférés, completion-függetlenség); RT-P0-24 `IMPLEMENTATION_TEST_REQUIRED`, DPO QA nyitott (BIZT-QA-1); addig saját jegyzetes, adatmentes út. Ide olvadt: IMPL-G1-4, PED-G1-2, az ERT-G1-2 SLIDE 5-része (X-8, X-12) |
| M1:ERT-G1-2 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda, G3b: az M1.1–M1.2 completion/unlock runtime-ja — SLIDE 1–2 pontozatlan választói, CP-completion, az M1.2 húzásmentes útja (RT-P0-09, RT-P0-13, RT-P0-14); csak a többletrész, a SLIDE 5-része = M1:BIZT-G1-3 (X-8) |
| M1:BIZT-G2-2 | P0 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | DPO (G2; ADV:230, Adatvédelem §9 :207/:209); LMS-gazda (RT-P0-15, G3b): az LMS-M1-05 és az LMS-M1-07 adatkezelési jóváhagyása és láthatósági visszaolvasása két mentorral, két csoporttal, tesztfiókkal; ha más mentor is látja a beadást: P0. Ide olvadt: az IMPL-G2-3 visszaolvasási része (X-8, X-12) |
| M1:IMPL-G2-4 | P1 | bizonyíték-kapu | MEGERŐSÍTVE | EVIDENCE_GATE | LMS-gazda, G3b: RT-P0-08 (0/1/2/2 = 5 negatív eset, GATE-CP állapotmátrix), RT-P0-19 (javító próbálkozás az F-peula előtt nem indul, kézi nyitás, a legjobb megerősített eredmény számít; az „Allowed attempts” értéke a repóban nincs), RT-P0-01 (Max grade 8, Grade to pass 5), RT-P0-09 (LMS-M1-03 → -07 → -04 → -05 lánc). Ide olvadt: IMPL-G3-2 (X-8) |
| M1:ERT-G1-6 | P1 | objektív | ELVETVE | REJECTED | a „háromszor”-jel és az abszolút disztraktorok a tanított szabályt alkalmazzák; bizonyított hiba nélküli disztraktorcsere = preferencia (verifier) |
| M1:ERT-G3-3 | P1 | objektív | ELVETVE | REJECTED | az M1.B trió-checklist a saját deklarált célját követi, kánon nem köti a kapurubrikához; a háromfokú átalakítás tervezési preferencia (verifier) |
| M1:BIZT-G3-3 | P1 | emberi-döntés | ELVETVE | REJECTED | a cetliket a teljes csoportnak tették láthatóvá, a felolvasás név nélküli; szabálysértés (§4:61 passz) nem igazolható, a kézírás-felismerés spekuláció (verifier) |
| M1:ERT-G3-2 | P1 | objektív | ELVETVE | REJECTED | a Blokk 3 a kapus hiányokra fókuszál, a hangnem lényegét a „címke = ítélet” magyarázat fedi; negyedik kulcspont a fix 10’-be preferencia (verifier) |
| M1:IMPL-G3-1 | P1 | objektív | ELVETVE | REJECTED | az F-peula „jelenléti completion” útja szó szerint a lezárt 2026-10-02-i döntés (MAN:20, :149, RT:90), a MAN:248 kezeli; ellentmondás nincs (verifier) |
| M1:ERT-G1-9 | P2 | objektív | ELVETVE | REJECTED | formatív, nem kapuzott mikrocél; a Q1 opciói mind a 4 mezőt megnevezik; a mikrocél átírása célszöveg-preferencia (verifier) |
| M1:IMPL-G1-9 | P2 | objektív | ELVETVE | REJECTED | az M1.1-ILL-02 a11y-jegyzete egyezik a dia szabályával; a :952 zárójele laza fogalmazás, nem ellentmondás; az IKO-jegyzetek feltételesek (verifier) |
| M1:IMPL-G1-10 | P2 | objektív | ELVETVE | REJECTED | a Label-megjelenítési hatás feltételezés; a linkformát kánoni szabály nem írja elő — formázási preferencia (verifier) |
| M1:PED-G1-6 | P2 | objektív | ELVETVE | REJECTED | a rács és a narráció példái parafrázisok, az asset-spec szándékosan így rögzíti — multimédia-preferencia (verifier) |
| M1:PED-G1-7 | P2 | emberi-döntés | ELVETVE | REJECTED | a két T/F szándékosan ellentétes polaritással kérdez (M1.1:501); itemcsere bizonyított hiba nélkül — preferencia (verifier) |
| M1:PED-G2-5 | P2 | objektív | ELVETVE | REJECTED | a trió-checklist (M1.B:134–139) a saját célját követi; az M1.3 önellenőrzés átvétele preferencia (verifier, K17) |
| M1:ERT-G2-9 | P2 | emberi-döntés | ELVETVE | REJECTED | repón belül nincs ellentmondás (a KAPU:87 megengedi az én-perspektívás I-t); answer keyhez bizonyíték nélkül nem nyúlunk (verifier) |
| M1:ERT-G2-10 | P2 | objektív | ELVETVE | REJECTED | a KAPU a régi szóhasználatot történetiként jelöli (:43, :97, :100), a döntési szabály egyértelmű; kalibrációs zaj nem bizonyított (verifier) |
| M1:PED-G2-9 | P2 | objektív | ELVETVE | REJECTED | a tanulói narráció (M1.4:146–147) már őszintén keretez, a :154 kimondja, hogy a választás nem kerül át az Assignmentbe — élményminőségi preferencia (verifier) |
| M1:BIZT-G2-8 | P2 | emberi-döntés | ELVETVE | REJECTED | az M1.4:526 már a lezárt HUM-PRIV-01 szövegét alkalmazza, a .docx-út egyenértékű; az M1 SBI-beadandó a külön review listán van (ADV:80) (verifier) |
| M1:BIZT-G2-9 | P2 | emberi-döntés | ELVETVE | REJECTED | a KAPU:212/:224 „a hely külön kérdés” tényszerű tévesztő-magyarázat, nem ad négyszemközti utasítást, nem ütközik a HUM-SAFE-02-vel — ízlés (verifier) |
| M1:PED-G3-10 | P2 | objektív | ELVETVE | REJECTED | azonos tényállás a BIZT-G3-3-mal; az „előre jelezd” javaslat preferencia (verifier) |
| M1:BIZT-G3-6 | P2 | emberi-döntés | ELVETVE | REJECTED | nincs bizonyítható ellentmondás: az M1.A a vakfolt valódi feltárását halasztja, az M1.B opcionális, pozitív, passzolható visszajelzést köt — fokozatos nyitás (verifier) |
| M1:ERT-G3-6 | P2 | objektív | ELVETVE | REJECTED | a 4. kérdés opciói mellett típusjegyzet áll (M1.B:242–245); kár nem bizonyított, képzői szinten áthidalható (verifier) |
| M1:PED-G2-10 | P2 | objektív | ELVETVE | REJECTED | az M1.4:500 már kimondja, hogy az önkéntes újrabeadás nem veszélyezteti a teljesítést; tájékoztatási finomítás, kár nem bizonyított (verifier) |
| M1:IMPL-G3-10 | P2 | objektív | ELVETVE | REJECTED | a hozzáférhetőségi sztenderdben nincs mozgásra vonatkozó követelmény; nem pontozott bemelegítő játékok, a képző helyben alkalmazkodik (verifier) |
| M1:PED-G3-5 | P2 | objektív | ELVETVE | REJECTED | a 4 fős csoport forgása alulspecifikált, de végrehajtható (M1.B:350 „3 vagy 4 kör”, puffer); a forgásszabály új tervezés (verifier) |
| M1:PED-G3-6 | P2 | objektív | ELVETVE | REJECTED | a képző előzetesen átnézte az M1.1–M1.4-et; az „érzés az I-ben” válasza a fájlban (M1.F:331) és a mintakvízben ott áll; kár nem bizonyított (verifier) |
| M1:PED-G3-7 | P2 | objektív | ELVETVE | REJECTED | a „nézd meg a Moodle-ben” magában foglalja a belépést; sorrendi finomítás, kár nem bizonyított (verifier) |
| M1:NYELV-G1-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G1-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G1-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (`@source` M1.2-NAR-04 + spec :573: a javítás útja VO-fix pack) |
| M1:NYELV-G1-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G1-9 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G1-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G1-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G1-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G1-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G1-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (részben: a „bulletpontokkal” és a „személyes kapcsolás” elvetve) |
| M1:NYELV-G2-1 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G2-2 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G2-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G2-5 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (KAPU:200 itt javítható; az M1.3:1059 `@source` VO-fix pack) |
| M1:NYELV-G2-6 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G2-7 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G2-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (az M1:ERT-G2-5-tel egy lépésben) |
| M1:NYELV-G2-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G2-14 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G3-3 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G3-4 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G3-8 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G3-10 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (az M1:BIZT-G3-1-gyel egy lépésben) |
| M1:NYELV-G3-11 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (az M1:BIZT-G3-1-gyel egy lépésben) |
| M1:NYELV-G3-12 | P2 | objektív | MEGERŐSÍTVE | OPEN | — (az M1:NYELV-G2-5-tel és a BIZT-G3-1-gyel egy lépésben) |
| M1:NYELV-G3-13 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G3-15 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G3-24 | P2 | objektív | MEGERŐSÍTVE | OPEN | — |
| M1:NYELV-G1-14 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az SBI „S” elemének kánoni magyar neve — „helyzet” (Glosszárium:138, HUB:33, :231) vagy „szituáció” (HUB:241, KAPU:47 rubrikasor-név, M1.2:936, M1.4:482, M1.A:534, M1.B:181); 2. ↔ 3. kánoni forrás ütközik — modulgazda + értékelési felelős, a Glosszárium gazdájával (X-13) |
| M1:NYELV-G2-4 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU:55 S-„Erős” horgonyának („idő ÉS/VAGY hely ÉS a helyzet szakasza”) érvényes olvasata; az M1:ERT-G2-5 S-horgony-átvezetése ettől függ — értékelési felelős (X-6) |
| M1:NYELV-G2-8 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: a KAPU:79 4. rubrikasor vezérkérdésének „(megtartható kapcsolatban)” zárójele külön szempont vagy magyarázat — értékelési felelős / modulgazda (X-6) |
| M1:NYELV-G2-9 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az SBI-sablon S-rése határozói vagy tagmondatos (M1.3:803–805, :889–893; M1.4:470–471; M1.4-MUNK-01 spec — a sablon ellentmond a saját példáinak) — modulgazda; QA: értékelési felelős (X-10) |
| M1:NYELV-G3-16 | P2 | emberi-döntés | EMBERI DÖNTÉS | BLOCKED_HUMAN | EMBERI DÖNTÉS: az M1.A:277 „tedd meg nyugodtan” gyakorlati vonzata (új cetlire írás, ha a 3 kiosztott elfogyott); az (a)/(b) rész elvetve — modulgazda (X-10) |
| M1:NYELV-G3-19 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:NYELV-G1-14 (helyei: M1.A:534, M1.B:181, M1.F:338, :343) |
| M1:NYELV-G1-7 | P2 | emberi-döntés | EMBERI DÖNTÉS | DUPLICATE | = M1:BIZT-G1-7 (az M1.1:926 „ez” kétértelműsége: nyelvi többlet, azzal egy döntésben) |
| M1:NYELV-G1-1 | P2 | objektív | ELVETVE | REJECTED | bevett fordulat („amit mások látnak rólad”); answer-key opció átírása szükségtelen (verifier) |
| M1:NYELV-G1-4 | P2 | objektív | ELVETVE | REJECTED | természetes, a :471 definícióval következetes; VO-újragyártást nem indokol (verifier) |
| M1:NYELV-G1-5 | P2 | objektív | ELVETVE | REJECTED | hallgathatósági preferencia (verifier) |
| M1:NYELV-G1-16 | P2 | objektív | ELVETVE | REJECTED | stílus; szükségtelen mondatcsere (verifier) |
| M1:NYELV-G2-10 | P2 | objektív | ELVETVE | REJECTED | a konjunktív szabály közvetlenül előtte kétszer kimondva; félreolvasás nem bizonyított (verifier) |
| M1:NYELV-G2-12 | P2 | objektív | ELVETVE | REJECTED | enyhe anakoluthon, egyértelmű jelentés; stílus, Anna-szövegezés (verifier) |
| M1:NYELV-G3-1 | P2 | objektív | ELVETVE | REJECTED | az „ilyen lapjai” vonatkozása nem bizonyítottan hibás (verifier) |
| M1:NYELV-G3-2 | P2 | objektív | ELVETVE | REJECTED | a „mondotok” szabályos alak (verifier) |
| M1:NYELV-G3-5 | P2 | objektív | ELVETVE | REJECTED | bevett távirati képzői stílus (verifier) |
| M1:NYELV-G3-6 | P2 | objektív | ELVETVE | REJECTED | a „kapus” a korpusz bevett melléknévi alakja (verifier) |
| M1:NYELV-G3-7 | P2 | objektív | ELVETVE | REJECTED | produktív szóalkotás, ízlés (verifier) |
| M1:NYELV-G3-9 | P2 | emberi-döntés | ELVETVE | REJECTED | a visszajelzés kontextusban érthető (verifier) |
| M1:NYELV-G3-14 | P2 | objektív | ELVETVE | REJECTED | szabályos normamondat a gyermekvédelmi keretben (verifier) |
| M1:NYELV-G3-17 | P2 | objektív | ELVETVE | REJECTED | a „4 fős trió” a modul következetes csoportegység-neve (verifier) |
| M1:NYELV-G3-18 | P2 | objektív | ELVETVE | REJECTED | érthető; átfogalmazás regressziós kockázat (verifier) |
| M1:NYELV-G3-20 | P2 | objektív | ELVETVE | REJECTED | több fájlra kiterjedő stílusegységesítés (verifier) |
| M1:NYELV-G3-21 | P2 | objektív | ELVETVE | REJECTED | regiszter-preferencia képzői szövegben (verifier) |
| M1:NYELV-G3-22 | P2 | objektív | ELVETVE | REJECTED | kánoni határ-mondat, nem változtatható (verifier) |
| M1:NYELV-G3-23 | P2 | objektív | ELVETVE | REJECTED | bevett távirati stílus (verifier) |
| M1:NYELV-G3-25 | P2 | objektív | ELVETVE | REJECTED | szándékos kulcsüzenet; a csere rontana (verifier) |
| M1:NYELV-G3-26 | P2 | objektív | ELVETVE | REJECTED | a szerkezetből levezethető (verifier) |
| M1:NYELV-G3-27 | P2 | objektív | ELVETVE | REJECTED | az idősávok azonosítják a blokkot (verifier) |

## Napló

| Idő | Fázis | Esemény |
|---|---|---|
| 2026-10-11 | — | A ledger létrehozva a harness v2-vel; nincs aktív futás. |
| 2026-10-11 | PREFLIGHT | `AP-2026-10-11-01` indul (`next-version`), bázis `main@213a4c5`, munkaág `next-version/AP-2026-10-11-01`. Kiinduló gépi állapot: `content_integrity.py` → „Objective integrity errors: 0”, kilépési kód 0; `--release-report` → `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`, `LEARNER-RELEASE-VERDICT: NO-GO`. A #26–#29 merge-commitok a `main`-ben; X-1, X-2, X-3 RESOLVED (git-bizonyíték a kapusorokban). |
| 2026-10-11 | INVENTORY | M0: a 82d0c7c óta nincs változás a modulban → a négy lencse REUSED, a `language` hiányzik. 40 ID a ledgerben (18 OPEN, 7 DUPLICATE, 7 BLOCKED_HUMAN, 3 EVIDENCE_GATE + 1 DUPLICATE kapu, 4 REJECTED). M1: kivonatolás folyamatban. |
| 2026-10-11 | INVENTORY | M1: 132 sor (116 verdiktes ID + 13 levágott P2 + 3 részsor): 25 OPEN, 12 NEEDS_RECHECK (ERT-G1-1, IMPL-G1-2 az N-M1-04 javítása miatt; 2 részsor; 8 verdikt nélküli levágott P2), 46 DUPLICATE, 21 BLOCKED_HUMAN, 4 EVIDENCE_GATE, 24 REJECTED. A 82d0c7c óta változott M1-helyek (M1.1, MAN :45/:308, RA 24., HUM 12.) más megtartott objektív findinget nem érintenek. Külső kapuk: X-4…X-12. REVIEW indul: M0/M1 `language`, M2 öt lencse. |
| 2026-10-11 | REVIEW | M1 `language` VERIFIED: `2026-10-11 Validált findingok – M1, nyelvi lencse, AP-2026-10-11-01.md` (57 nyers, 57/57 verdikt: 28 MEGERŐSÍTVE + objektív, 7 EMBERI DÖNTÉS (2 duplikátum), 22 ELVETVE); read-only bizonyíték a mentés előtt egyezik. Az M1-re mind az öt lencse lefutott. |
| 2026-10-11 | REVIEW | M0 `language` VERIFIED: `2026-10-11 Validált findingok – M0, nyelvi lencse, AP-2026-10-11-01.md` (42 nyers, 42/42 verdikt: 20 MEGERŐSÍTVE + objektív, 4 EMBERI DÖNTÉS (1 duplikátum), 18 ELVETVE); read-only bizonyíték egyezik. Az M0-ra mind az öt lencse lefutott. M1 NEEDS_RECHECK (12) célzott verifierrel folyamatban; M2 lencsék futnak. |
| 2026-10-11 | RECHECK | M1 12 NEEDS_RECHECK lezárva (`2026-10-11 Célzott újraellenőrzés – M1 NEEDS_RECHECK, AP-2026-10-11-01.md`): ERT-G1-1 és IMPL-G1-2 ALREADY_FIXED (ebf311e, 96996e2; a CC-04/CC-06 rész = M0:ERT-8), PED-G1-8.obj és BIZT-G3-8.obj OPEN, a 8 levágott P2 REJECTED. |
