# Lefedettségi jelentés – a 171 átvett tétel és a QA17-kulcsok, AP-2026-10-13-01

> **Audit trail, nem kánon.** A projektgazda 2026-10-13-i felhatalmazásának 4. és 9. pontja szerinti konszolidáció: a
> D-01…D-23 csomagok, a 119 `BLOCKED_HUMAN` és 52 `EVIDENCE_GATE` tétel (az `AP-2026-10-12-02` futás `3dfc451`-es
> ledgeréből), valamint a futás célzott QA-jának új kulcsai. Az állapotok a ledger (`AUTOPILOT-LEDGER.md`, `AP-2026-10-13-01`)
> szerintiek; a ledger nem bizonyíték, minden `FIXED` / `ALREADY_FIXED` sor a fájlban, commit-tal bizonyított.
>
> **Ami nem zárul le ezzel:** a runtime-bizonyíték (G3b, G5b), a szerepköri jóváhagyások és aláírások (G1, G2, SIGNOFF), a
> VO fix pack, a futó pilot (`main@213a4c5`, CC-04), a staging és a learner release. A jelentés nem release-jóváhagyás.
>
> **Csomagnevek a táblákban** (mind az `01 Fejlesztés/04 Audit/` mappában):
> - Memuna-csomag: `2026-10-13 Jóváhagyási csomag – Memuna, AP-2026-10-13-01.md`
> - DPO-csomag: `2026-10-13 Jóváhagyási csomag – DPO, AP-2026-10-13-01.md`
> - jogász-csomag: `2026-10-13 Jóváhagyási csomag – jogász, AP-2026-10-13-01.md`
> - értékelési csomag: `2026-10-13 Jóváhagyási csomag – értékelési felelős, AP-2026-10-13-01.md`
> - modulgazdai csomag (D-20): `2026-10-13 Jóváhagyási csomag – modulgazdák, D-20 vágási tervek, AP-2026-10-13-01.md`
> - VO fix pack csomag: `2026-10-13 Jóváhagyási csomag – médiafelelős, VO fix pack, AP-2026-10-13-01.md`
> - LMS-gazda/a11y bizonyítékcsomag: `2026-10-13 Bizonyítékcsomag – LMS-gazda és hozzáférhetőségi gazda, AP-2026-10-13-01.md`
> - D-21 terv: `2026-10-13 course-develop terv – 1–5 fős F-peula keret, D-21, AP-2026-10-13-01.md`
> - TECH-2 parancscsomag: `2026-10-13 TECH-2 parancsok és regressziós terv, AP-2026-10-13-01.md`
> - célzott QA: `2026-10-13 Célzott QA – D-csomagok átvezetése (8bb4d7d), AP-2026-10-13-01.md`

## 1. Összesítés

- Átvett nyitott tételek (`3dfc451`): **171** — BLOCKED_HUMAN 119, EVIDENCE_GATE 52.
- Ugyanezek most: ALREADY_FIXED 1, BLOCKED_HUMAN 96, EVIDENCE_GATE 54, FIXED 20.
- A futás új kulcsai (célzott QA, QA17): **36** — BLOCKED_HUMAN 7, DUPLICATE 3, FIXED 26.
- `FIXED` / `ALREADY_FIXED` csak lezárt projektgazdai döntés (HUM 15) vagy validált objektív finding átvezetése, a fájlban bizonyítva; a runtime- és szerepköri bizonyíték ettől nyitva marad (X-1…X-4).

## 2. A D-01…D-23 csomagok állapota

| D | Állapot | Kulcsok | Hol (commit) | Ki dönt / hagyja jóvá | Kész anyag |
|---|---|---|---|---|---|
| D-01 | NYITOTT – szerepköri döntésre vár (HUM 15) | M0:QA14-BIZT-2, M2:QA14-BIZT-2, M6:QA14-BIZT-4, M2:BIZT-G3-2, M4:BIZT-G2-9 | — | Memuna + programvezető | Memuna-csomag D01-a…e |
| D-02 | LEZÁRT (HUM 15), szövegváltozás nem kell | M6:QA14-BIZT-5b | 8bb4d7d (HUM 15) | vétó/QA: Memuna + tartalomfelelős | — |
| D-03 | LEZÁRT (HUM 15), ÁTVEZETVE | M3:QA14-NYELV-13, M3:IMPL-G3-9 | 8bb4d7d, 9788c05 (M3:QA17-ERT-2, -NYELV-4) | vétó/QA: M3 modulgazda + Memuna; a 4. eset Memuna-reviewja (PRG-12) bizonyíték | Memuna-csomag (PRG-12 lap); modulgazdai csomag (QA17-NYELV-14) |
| D-04 | NYITOTT – szerepköri döntésre vár (HUM 15) | M6:QA14-BIZT-1, M6:QA14-BIZT-2, M7:QA14-BIZT-6, Z:QA14-BIZT-2, M4:QA14-BIZT-3, M0:BIZT-5, M6:BIZT-G1-1 | — | Memuna (GYV-8: + programvezető); 6D/ZÁRÓ: az M6-NY-D27 feloldása is (projektgazda) | Memuna-csomag D04-a1…f |
| D-05 | NYITOTT – szerepköri döntésre vár (HUM 15), SÜRGŐS | M3:BIZT-G2-2 | — | Memuna (a HUM:471 formális újranyitása) | Memuna-csomag D05-1…10, elsődleges források (2026-10-13); jogász-csomag |
| D-06 | LEZÁRT (HUM 15), ÁTVEZETVE | M3:BIZT-G1-8 (a hely); a bizonyíték nyitott | 8bb4d7d, 9788c05 (KANON:QA17-BIZT-4) | jogász (ellenőrzés), Memuna (jóváhagyás) – bizonyíték-kapu, X-1 | jogász-csomag; a #1 issue-komment kész szövege a záró jelentésben |
| D-07 | NYITOTT – szerepköri döntésre vár (HUM 15) | M3:QA14-BIZT-2, M6:QA14-BIZT-3, M7:BIZT-G1-2, M7:PED-G2-4, M6:ERT-G1-2, M6:ERT-G3-4 | — | értékelési felelős + Memuna; rubrikaszint, kulcs: projektgazda | értékelési csomag D-07 (a)–(d) |
| D-08 (a) | NYITOTT – szerepköri döntésre vár (HUM 15) | M2:QA14-BIZT-4 | — | Memuna + programvezető; kapus belépő: értékelési felelős | Memuna-csomag D08-1…4 |
| D-08 (b) | LEZÁRT (HUM 15), ÁTVEZETVE; a mechanizmus nyitott | M3:IMPL-G2-5; M3:QA17-IMPL-1 | 8bb4d7d | a megjelenítési mód: projektgazda (build-spec), Memuna-QA | Memuna-csomag kiegészítés; LMS-csomag RA 11 |
| D-09 | NYITOTT – szerepköri döntésre vár (HUM 15) | M2:QA14-BIZT-5 | — | Memuna + DPO | Memuna-csomag 3. pont |
| D-10 | NYITOTT – szerepköri döntésre vár (HUM 15) | M1:QA14-BIZT-5, KANON:QA14-BIZT-4, Z:QA14-BIZT-1, Z:BIZT-G1-2 | — | Memuna + DPO; pótlás: értékelési felelős + programvezető | Memuna-csomag 4.; DPO-csomag DPO-1a–c; értékelési csomag |
| D-11 | LEZÁRT (HUM 15), ÁTVEZETVE; ADV-4 technika nyitott | KANON:QA14-BIZT-1, M0:QA14-BIZT-3, KANON:QA16-IMPL-2; M3:BIZT-G1-5, M3:BIZT-G2-7 (ADV-4) | 8bb4d7d, 9788c05 (QA17-IMPL-2, -BIZT-2, -BIZT-6) | vétó/QA: DPO; ADV-4: DPO + Memuna a BK-05 után; FEEDBACK-N csoportmód: DPO | DPO-csomag DPO-2, DPO-6.7; LMS-csomag RA 15 |
| D-12 | LEZÁRT (HUM 15), ÁTVEZETVE | M0:QA14-NYELV-3 | 8bb4d7d | vétó/QA: programvezető + Memuna; adatkör: DPO | DPO-csomag DPO-3 |
| D-13 (a), (e) | LEZÁRT (HUM 15), ÁTVEZETVE; az (e) megőrzése nyitott | M0:QA14-BIZT-4; M2:BIZT-G1-6 (megőrzés) | 8bb4d7d | (a) LMS-gazda + DPO; (e) megőrzés: DPO | DPO-csomag DPO-4e |
| D-13 (b), (c), (d) | NYITOTT – szerepköri döntésre vár (HUM 15) | M4:QA14-BIZT-5, Z:QA14-BIZT-3, M2:QA14-BIZT-7 | — | (b), (c) DPO; (d) Memuna + DPO | DPO-csomag DPO-4b, -4c; Memuna-csomag D13d-1…4 |
| D-14 | NYITOTT – szerepköri döntésre vár (HUM 15) (az inaktív alapállapot érvényes) | KANON:QA14-BIZT-5, KANON:QA14-BIZT-3b | — | DPO; programvezető + Moodle-adminisztrátor | DPO-csomag DPO-5a, -5b |
| D-15 (a)–(f) | LEZÁRT (HUM 15), ÁTVEZETVE | KANON:QA14-ERT-2, KANON:QA14-IMPL-7b, M4:ERT-G2-4, M6:IMPL-G1-7, M2:IMPL-G1-3, M0:QA14-ERT-1 | 8bb4d7d, 9788c05 (QA17-IMPL-4, -IMPL-5, -BIZT-5) | vétó/QA soronként (HUM 15); (c) build-paraméterek: projektgazda (KANON:QA17-ERT-3) | LMS-csomag RA 8, 21, 26, 27 |
| D-16 | LEZÁRT (HUM 15), ÁTVEZETVE; (b) és a besorolás nyitott | Z:QA14-NYELV-1, Z:ERT-G1-1, Z:QA14-IMPL-3; Z:QA14-ERT-2 (b); KANON:QA17-BIZT-3b | 8bb4d7d, 9788c05 (QA17-BIZT-3) | vétó/QA: értékelési felelős, programvezető, DPO; (b): értékelési felelős + DPO; besorolás: projektgazda + értékelési felelős | értékelési csomag D-16 |
| D-17 (d) | LEZÁRT (HUM 15), szövegváltozás nem kell | M7:BIZT-G1-6 (b) — a (c) GDPR-minősítés bizonyíték | 8bb4d7d (HUM 15) | DPO (GDPR 9., BK-11) | DPO-csomag DPO-6.1 |
| D-17 (a)–(c) | NYITOTT – szerepköri döntésre vár (HUM 15) | M5:QA14-ERT-1, M7:BIZT-G1-1, M7:PED-G1-1 | — | értékelési felelős (+ DPO az ERT-42-nél); ERT-43: + projektgazda és előzetes tájékoztató | értékelési csomag D-17 |
| D-18 | NYITOTT – szerepköri döntésre vár (HUM 15) | M3:IMPL-G2-14, M5:ERT-G1-9, M5:NYELV-G1-11, M5:PED-G1-3 | — | értékelési felelős + modulgazda / M5 szerző / szakmai lektor | értékelési csomag D-18 |
| D-19 (b) | LEZÁRT (HUM 15), ÁTVEZETVE | M4:ERT-G1-10 | 8bb4d7d | vétó/QA: M4 modulgazda, értékelési felelős | — |
| D-19 (a), (c) | NYITOTT – szerepköri döntésre vár (HUM 15) | M5:PED-G1-10, M2:QA14-ERT-2 | — | modulgazda / értékelési felelős; (c) + projektgazda, someres QA | értékelési csomag D-19 |
| D-20 | NYITOTT – szerepköri döntésre vár (HUM 15) | M0:PED-5, M2:PED-G3-1, M3:PED-G3-1, M4:PED-G2-2, M4:NYELV-G2-6, M5:PED-G2-6, M5:QA-PED-2, M6:PED-G3-1, M7:PED-G3-1 | — | modulgazdák (M3.B: + Memuna); vétó/QA: programvezető; B-változat: + projektgazda | modulgazdai csomag (D-20) |
| D-21 | NYITOTT – szerepköri döntésre vár (HUM 15) | M3:ERT-G3-10 | 8bb4d7d (csak az M1.F kapacitásmondata) | projektgazda (a terv elfogadása), modulgazda, Memuna (1:1), programvezető | D-21 terv |
| D-22 | LEZÁRT (HUM 15), ÁTVEZETVE | M7:NYELV-G3-12 | 8bb4d7d | vétó/QA: M7 modulgazda | — |
| D-23 | LEZÁRT (HUM 15), ÁTVEZETVE | M7:G7-ERT5-2; runtime: M7:G7-ERT5-3 | 8bb4d7d, 9788c05 (QA17-ERT-1, -IMPL-6) | vétó/QA: értékelési felelős; mentori kulcs-átbeszélés: értékelési felelős (M7:QA17-ERT-1b) | LMS-csomag RA 19 |

## 3. Bizonyíték-kapuk és külső függőségek (a döntési dokumentum BK-01…BK-13, KF-01/02 szerint)

| ID | Állapot most | Kulcsok | Kinek a bizonyítéka | Kész anyag |
|---|---|---|---|---|
| BK-01 | nyitott | M3:PED-G2-1, M4:BIZT-G2-10, M4:BIZT-G2-9 (küszöb-QA) | Memuna (GYV-24, GYV-6); LMS-gazda (RA 9) | Memuna-csomag; LMS-csomag |
| BK-02 | nyitott | M5:IMPL-G2-2 | LMS-gazda + módszertani lektor (RA 4) | LMS-csomag |
| BK-03 | nyitott | M4:BIZT-G1-2 | DPO (ADV-E1) | DPO-csomag DPO-6.2 |
| BK-04 | nyitott | M3:BIZT-G1-8 | jogász, Memuna | jogász-csomag; Memuna-csomag (JOG-1 lap) |
| BK-05 | nyitott | M3:BIZT-G1-5, M3:BIZT-G2-7 | LMS-gazda; utána DPO + Memuna (technika) | LMS-csomag; DPO-csomag DPO-6.7 |
| BK-06 | nyitott | M3:BIZT-G2-5, M3:BIZT-G3-8 | programvezető, DPO, LMS-gazda, Memuna | DPO-csomag DPO-6.3 |
| BK-07 | nyitott (a mechanizmus eldőlt: D-11) | M1:BIZT-G2-4, M2:BIZT-G2-3, M2:BIZT-G1-6 (hozzáférés) | LMS-gazda, DPO (RT-P0-15) | LMS-csomag RA 15; DPO-csomag DPO-2 |
| BK-08 | nyitott | M7:IMPL-G2-12 | hozzáférhetőségi gazda | LMS-csomag |
| BK-09 | nyitott | M4:BIZT-G1-7 | szerző / tananyagfelelős, médiafelelős | — |
| BK-10 | nyitott (a mátrix eldőlt: D-23) | M7:G7-ERT5-3 | LMS-gazda / TEST_OWNER (RT-P0-19, RT-P0-08) | LMS-csomag RA 19 |
| BK-11 | nyitott | M7:BIZT-G1-6 (c) | DPO | DPO-csomag DPO-6.1 |
| BK-12 | nyitott | (D-03-hoz) | Memuna | Memuna-csomag (PRG-12 lap) |
| BK-13 | nyitott | (a D-tételek runtime- és szerepköri bizonyítékai) | LMS-gazda, értékelési felelős, Memuna, DPO | LMS-csomag; a szerepköri csomagok |
| KF-01 | nyitott | M1:QA14-BIZT-1, M4:QA14-BIZT-4 (+ az X-6 kulcsai) | médiafelelős / VO-gazda; DPO-vétó | VO fix pack csomag |
| KF-02 | nyitott | M2:PED-G1-11 | modulgazda + értékelési felelős (SIGNOFF) | értékelési csomag ERT-19 |

## 4. Konszolidált külső kapuk (a ledger Külső kapuk táblája)

| Kulcs | Típus | Tétel | Kell (mit, kitől) | Állapot |
|---|---|---|---|---|
| X-1 | EVIDENCE_GATE | G1: a Memuna írásos „átnéztem” bejegyzése (GYV-24) | Memuna: egyazon végleges SHA-ra szóló, datált „átnéztem” (PT §9.3), SAFE-7 és az 1:1-kulcsok verdiktje, segélyvonalak review-napi ellenőrzése, tracker #1 lezárása | OPEN |
| X-2 | EVIDENCE_GATE | G2: a DPO írásos release-QA-ja (ADV-E1, ADV-E2, ADV-E3) | DPO / jogi felelős: activitynkénti jóváhagyás (adatmezők, szerepek, megőrzés, export, xAPI/LRS, saved-state, backup), teljes adatleltár, HUM-PRIV-04 AI-kapcsolat QA-ja; tracker #2 | OPEN |
| X-3 | SIGNOFF | Szerepköri jóváhagyások (SIG-1…SIG-6) | értékelési felelős, szakmai lektor, Memuna, jogi jogosult, DPO, szerző: a döntési csomag SIG-bejegyzései szerint | OPEN |
| X-4 | RUNTIME | Célkörnyezeti runtime-bizonyíték (RT-1…RT-6) | LMS-gazda / build-felelős, hozzáférhetőségi gazda, DPO a saját részén: RA 1–27. pont, RT-P0-xx és RT-A11Y sorok; a 2026-10-13-i új és módosult tesztlépések (RA 8, 11, 15, 16, 19, 21, 26, 27): LMS-gazda/a11y bizonyítékcsomag | OPEN |
| X-5 | HUMAN_DECISION | Szerepköri bemenetek és vétó/QA az `F` döntésekhez | a döntésben megnevezett szerep (Memuna, DPO, jogász, értékelési felelős, modulgazda, programvezető, LMS-gazda); tételesen: `2026-10-12 HUM 14 átvezetés – 125-125 lefedettségi jelentés, AP-2026-10-12-01.md` „Külső bizonyítéktól függő” szakasza és a Findingok BLOCKED_HUMAN sorai | OPEN |
| X-6 | HUMAN_DECISION | VO-1: egyetlen VO fix pack | médiafelelős / VO-gazda: a kimondott szöveget módosító blokkok újrarenderelése, a többi kiejtési azonosságának igazolása; kurzusoldali alkalmazás fix packként; kész terv: VO fix pack csomag (2026-10-13) | OPEN |
| X-7 | HUMAN_DECISION | TECH-2: az M6.1/M6.2 átnevezése | a felhasználó futtatja az átnevezési commitot a saját termináljában; utána a hivatkozások, a két `tools/` útvonalkulcs, a baseline-sor, a pin és a média egy change setben; ellenőrzött parancsok és regressziós terv: TECH-2 parancscsomag (2026-10-13) | OPEN |
| X-8 | HUMAN_DECISION | PRG-4: célzott `/course-develop` csomag | a felhasználó indítja; a csomagtervet a projektgazda hagyja jóvá; új biztonsági vagy értékelési item csak Memuna- / értékelési jóváhagyással; a PRG-5 (D-21) terve kész: D-21 /course-develop terv (2026-10-13), elfogadásra vár | OPEN |
| X-9 | HUMAN_DECISION | PRG-17: az M0.1 SLIDE 5 kérdése | a pilot-visszajelzéssel együtt dönt a projektgazda / modulgazda (CC-04, HUM 13. és 14. szakasz) | OPEN |
| X-10 | HUMAN_DECISION | LMS-2 M3.4-rész: az M3.4-EGY-03 Drag & Drop-mellékút megszüntetése | projektgazda / build-felelős: a `tools/test_media_manifest.py` párcseréje egy change setben; vétó: hozzáférhetőségi gazda — átvezetve: 3b160fc, 11a89b4 (média 4b188cc, 87c08c1) | RESOLVED |
| X-11 | HUMAN_DECISION | A célzott QA emberi döntései (QA14, QA17) és a HUM 15 nyitott sorai | a sorban megnevezett szerep: Memuna, DPO / jogi felelős, jogász, értékelési felelős, programvezető, modulgazda; kitöltött elfogadási javaslatok: a 2026-10-13-i szerepköri csomagok (Memuna, DPO, jogász, értékelési, modulgazdai, VO, LMS/a11y); lefedettség: `2026-10-13 Lefedettségi jelentés – 171 tétel és a QA17-kulcsok, AP-2026-10-13-01.md` | OPEN |
| X-12 | HUMAN_DECISION | ERT-5 D1/D2: az M7 kapukvíz Review options ablakmátrixa és az első próbálkozás lezárási mechanizmusa | eldőlt: HUM 15 D-23 (projektgazda, 2026-10-13), átvezetve: 8bb4d7d, 9788c05; vétó/QA: értékelési felelős; runtime: X-4 (M7:G7-ERT5-3) | RESOLVED |
| X-13 | HUMAN_DECISION | ADV-1 hozzáférési csomag: kiterjedés és mechanizmus (eldőlt: HUM 15 D-11, 8bb4d7d, 9788c05); ADV-4 utáni technikaválasztás (nyitott) | a kiterjedés és a mechanizmus átvezetve; nyitott: az ADV-4 tárolásmentes technikájának választása a BK-05 runtime-visszaolvasás után (DPO + Memuna); a FEEDBACK-N csoportmódja (DPO); vétó/QA: DPO / jogi felelős | OPEN |
| X-14 | HUMAN_DECISION | JOG-1: a jogászi ellenőrzés és a kijelölt felnőtt nyilvántartásának helye | eldőlt: HUM 15 D-06 (G1 tracker #1, nyilvános, személyes adat nélkül), átvezetve: 8bb4d7d, 9788c05; a bizonyíték (jogász + Memuna) X-1; az issue-komment szövegét a felhasználó teszi közzé (VÉDETT gh-írás) | RESOLVED |
| X-15 | HUMAN_DECISION | A projektgazda saját döntései a 2026-10-13-i futás után | projektgazda: (1) a D-21 /course-develop terv elfogadása (+E7); (2) a D-20 B-változatainak blokkhatár-eltolása a modulgazdákkal; (3) az ERT-43 hatálybalépése és az előzetes tanulói tájékoztató (D-17 (c)); (4) az M6-NY-D27 feloldása a D-04 M6.4 6D/ZÁRÓ küszöbéhez; (5) a D-08 (b) működő megjelenítési módja (M3:QA17-IMPL-1, Memuna-QA); (6) az LMS-M4-05 rubrika build-paraméterei (KANON:QA17-ERT-3); (7) a D-16 besorolása az értékelési felelőssel (KANON:QA17-BIZT-3b) | OPEN |

## 5. Tételes lefedettség

Minden átvett és új kulcs pontosan egyszer. „Besorolás”: a döntési dokumentum lefedettségi listája (D-xx, BK-xx, KF-xx), illetve a külső kapu. A teljes bizonyíték- és döntési-igény szöveg a ledgerben áll.

| Kulcs | Súly | Előtte | Most | Besorolás |
|---|---|---|---|---|
| M0:BIZT-1 | P0 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| M0:BIZT-3 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | GYV-3 (Memuna helyenkénti verdikt) |
| M0:BIZT-5 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-04 |
| M0:ERT-4 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-3 |
| M0:ERT-8 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-9 |
| M0:IMPL-9 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-4 |
| M0:NYELV-G2-11 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-7 |
| M0:PED-5 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-20 |
| M1:BIZT-G1-3 | P0 | EVIDENCE_GATE | EVIDENCE_GATE | X-4 |
| M1:BIZT-G2-2 | P0 | EVIDENCE_GATE | EVIDENCE_GATE | X-2 |
| M1:BIZT-G2-4 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | BK-07 |
| M1:BIZT-G2-7 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M1:ERT-G1-2 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-4 |
| M1:IMPL-G2-4 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-4 |
| M1:NYELV-G1-6 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M1:NYELV-G2-5 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M1:PED-G3-8 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M2:BIZT-G1-6 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | BK-07 (hozzáférés); D-13 (megőrzés, névmező) |
| M2:BIZT-G1-9 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-2 |
| M2:BIZT-G2-3 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | BK-07 |
| M2:BIZT-G2-4 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | GYV-3 (Memuna helyenkénti verdikt) |
| M2:BIZT-G2-8 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| M2:BIZT-G2-9 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-2 |
| M2:BIZT-G3-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-01 |
| M2:BIZT-G3-7 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | X-2 |
| M2:ERT-G1-7 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| M2:IMPL-G1-3 | P2 | BLOCKED_HUMAN | FIXED | D-15; BK-13 (RT-P0-21) |
| M2:PED-G1-11 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | KF-02 (SIGNOFF) |
| M2:PED-G2-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M2:PED-G3-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-20 |
| M3:BIZT-G1-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | GYV-3 (Memuna helyenkénti verdikt) |
| M3:BIZT-G1-2 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| M3:BIZT-G1-5 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | BK-05; D-11 (technikaválasztás) |
| M3:BIZT-G1-8 | P1 | BLOCKED_HUMAN | EVIDENCE_GATE | D-06 (nyilvántartási hely); BK-04 (jogász, Memuna) |
| M3:BIZT-G2-10 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| M3:BIZT-G2-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-05 |
| M3:BIZT-G2-3 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | GYV-3 (Memuna helyenkénti verdikt) |
| M3:BIZT-G2-5 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | BK-06 |
| M3:BIZT-G2-7 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | BK-05; D-11 (technikaválasztás) |
| M3:BIZT-G3-4 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | GYV-3 (Memuna helyenkénti verdikt) |
| M3:BIZT-G3-8 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | BK-06 |
| M3:ERT-G2-7 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M3:ERT-G3-10 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-21 (hiányzási mondat: 5.2) |
| M3:IMPL-G2-11 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M3:IMPL-G2-14 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-18 |
| M3:IMPL-G2-15 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-7 |
| M3:IMPL-G2-5 | P1 | BLOCKED_HUMAN | FIXED | D-08 |
| M3:IMPL-G3-4 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| M3:IMPL-G3-9 | P2 | BLOCKED_HUMAN | FIXED | D-03 |
| M3:NYELV-G1-13 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M3:NYELV-G2-15 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M3:PED-G2-1 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | BK-01 |
| M3:PED-G3-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-20 |
| M4:BIZT-G1-2 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | BK-03; KF-01 (narráció) |
| M4:BIZT-G1-7 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | BK-09 |
| M4:BIZT-G2-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | GYV-3 (Memuna helyenkénti verdikt) |
| M4:BIZT-G2-10 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | BK-01 |
| M4:BIZT-G2-7 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | X-2 |
| M4:BIZT-G2-9 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-01 (besorolás); BK-01 (GYV-6 küszöb-QA) |
| M4:ERT-G1-10 | P2 | BLOCKED_HUMAN | FIXED | D-19 |
| M4:ERT-G1-6 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M4:ERT-G1-9 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M4:ERT-G2-4 | P2 | BLOCKED_HUMAN | FIXED | D-15 |
| M4:IMPL-G2-12 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | X-4 |
| M4:NYELV-G1-12 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M4:NYELV-G2-6 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-20 |
| M4:PED-G1-7 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| M4:PED-G2-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-20 |
| M5:BIZT-G1-4 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | X-2 |
| M5:BIZT-G1-6 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | X-3 |
| M5:ERT-G1-11 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | X-3 |
| M5:ERT-G1-9 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-18 |
| M5:IMPL-G2-2 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | BK-02 |
| M5:NYELV-G1-11 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-18 |
| M5:PED-G1-10 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-19 |
| M5:PED-G1-3 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-18 |
| M5:PED-G1-4 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M5:PED-G2-11 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M5:PED-G2-6 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-20 |
| M5:QA-PED-2 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-20 |
| M6:BIZT-G1-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-04 |
| M6:BIZT-G1-6 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-3 |
| M6:BIZT-G1-7 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | X-2 |
| M6:BIZT-G2-3 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| M6:ERT-G1-10 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M6:ERT-G1-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-07 |
| M6:ERT-G1-6 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M6:ERT-G2-8 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M6:ERT-G3-4 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-07 |
| M6:IMPL-G1-5 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M6:IMPL-G1-7 | P2 | BLOCKED_HUMAN | FIXED | D-15; BK-13 (RT-P0-01) |
| M6:IMPL-G2-2 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-4 |
| M6:IMPL-G2-5 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-7 |
| M6:IMPL-G2-7 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M6:NYELV-G1-11 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-7 |
| M6:NYELV-G1-7 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M6:NYELV-G2-1 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M6:NYELV-G3-3 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-7 |
| M6:PED-G1-8 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M6:PED-G3-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-20 |
| M6:QA-IMPL-5 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-7 |
| M7:BIZT-G1-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-17 |
| M7:BIZT-G1-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-07 |
| M7:BIZT-G1-3 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-2 |
| M7:BIZT-G1-5 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| M7:BIZT-G1-6 | P2 | BLOCKED_HUMAN | EVIDENCE_GATE | D-17 ((b) rész); BK-11 ((c) rész); (a) rész: 5.2 |
| M7:ERT-G1-5 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-3 |
| M7:ERT-G2-7 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M7:IMPL-G1-11 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | X-4 |
| M7:IMPL-G2-10 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-4 |
| M7:IMPL-G2-12 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | BK-08 |
| M7:IMPL-G2-5 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| M7:NYELV-G2-13 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M7:NYELV-G2-9 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M7:NYELV-G3-12 | P2 | BLOCKED_HUMAN | FIXED | D-22 |
| M7:PED-G1-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-17 |
| M7:PED-G2-4 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-07 |
| M7:PED-G3-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-20 |
| M7:PED-G3-11 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-8 |
| Z:BIZT-G1-10 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | X-1 |
| Z:BIZT-G1-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-10 |
| Z:ERT-G1-1 | P1 | BLOCKED_HUMAN | FIXED | D-16 |
| Z:NYELV-G1-6 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | X-6 |
| M0:QA14-BIZT-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-01 |
| M0:QA14-BIZT-3 | P2 | BLOCKED_HUMAN | FIXED | D-11 |
| M0:QA14-BIZT-4 | P2 | BLOCKED_HUMAN | FIXED | D-13 |
| M0:QA14-NYELV-3 | P2 | BLOCKED_HUMAN | FIXED | D-12 |
| M0:QA14-ERT-1 | P2 | BLOCKED_HUMAN | FIXED | D-15 |
| M1:QA14-BIZT-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | KF-01 |
| M1:QA14-BIZT-5 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-10 (alpont: 5.2) |
| M1:QA14-BIZT-6 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | G1–G8 szerepköri bizonyíték |
| M1:QA14-ERT-3 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | G1–G8 szerepköri bizonyíték |
| M2:QA14-BIZT-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-01 |
| M2:QA14-BIZT-4 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-08 |
| M2:QA14-BIZT-5 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-09 |
| M2:QA14-BIZT-7 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-13 |
| M2:QA14-BIZT-10 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | G1–G8 szerepköri bizonyíték |
| M2:QA14-ERT-2 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-19 |
| M3:QA14-BIZT-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-07 |
| M3:QA14-BIZT-5 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | G1–G8 szerepköri bizonyíték |
| M3:QA14-NYELV-13 | P2 | BLOCKED_HUMAN | FIXED | D-03; BK-12 |
| M4:QA14-BIZT-1 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | G1–G8 szerepköri bizonyíték |
| M4:QA14-BIZT-3 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-04 |
| M4:QA14-BIZT-4 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | KF-01 |
| M4:QA14-BIZT-5 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-13 |
| M4:QA14-BIZT-8 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | G1–G8 szerepköri bizonyíték |
| M5:QA14-BIZT-2 | P2 | EVIDENCE_GATE | EVIDENCE_GATE | G1–G8 szerepköri bizonyíték |
| M5:QA14-BIZT-3 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | G1–G8 szerepköri bizonyíték |
| M5:QA14-ERT-1 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-17 |
| M6:QA14-BIZT-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-04 |
| M6:QA14-BIZT-2 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-04 |
| M6:QA14-BIZT-3 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-07; KF-01 (narráció) |
| M6:QA14-BIZT-4 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-01 (kísérő javítás: 5.2) |
| M6:QA14-BIZT-5b | P2 | BLOCKED_HUMAN | ALREADY_FIXED | D-02 |
| M6:QA14-BIZT-7 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | G1–G8 szerepköri bizonyíték |
| M7:QA14-BIZT-6 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-04 |
| Z:QA14-NYELV-1 | P1 | BLOCKED_HUMAN | FIXED | D-16 |
| Z:QA14-ERT-2 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-16 |
| Z:QA14-BIZT-1 | P1 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-10 |
| Z:QA14-BIZT-2 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-04 |
| Z:QA14-BIZT-3 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-13 |
| Z:QA14-IMPL-3 | P2 | BLOCKED_HUMAN | FIXED | D-16 |
| KANON:QA14-ERT-2 | P1 | BLOCKED_HUMAN | FIXED | D-15 |
| KANON:QA14-IMPL-7b | P2 | BLOCKED_HUMAN | FIXED | D-15 |
| KANON:QA14-BIZT-1 | P1 | BLOCKED_HUMAN | FIXED | D-11 |
| KANON:QA14-BIZT-3b | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-14 ((a) rész: 5.1) |
| KANON:QA14-BIZT-4 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-10 |
| KANON:QA14-BIZT-5 | P2 | BLOCKED_HUMAN | BLOCKED_HUMAN | D-14 |
| M7:G7-ERT5-2 | P1 | BLOCKED_HUMAN | FIXED | D-23 |
| M7:G7-ERT5-3 | P1 | EVIDENCE_GATE | EVIDENCE_GATE | BK-10 |
| KANON:QA16-IMPL-2 | P2 | BLOCKED_HUMAN | FIXED | D-11 |
| M3:QA17-PED-1 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-03, D-20 |
| M2:QA17-PED-2 | P2 | új (QA17) | FIXED | célzott QA (QA17) |
| M1:QA17-PED-3 | P2 | új (QA17) | FIXED | célzott QA (QA17) |
| KANON:QA17-IMPL-2 | P1 | új (QA17) | FIXED | célzott QA (QA17); D-11 |
| KANON:QA17-BIZT-1 | P1 | új (QA17) | DUPLICATE | célzott QA (QA17) |
| KANON:QA17-BIZT-2 | P1 | új (QA17) | FIXED | célzott QA (QA17); D-11 |
| KANON:QA17-BIZT-2b | P1 | új (QA17) | BLOCKED_HUMAN | célzott QA (QA17) |
| KANON:QA17-IMPL-3 | P2 | új (QA17) | DUPLICATE | célzott QA (QA17) |
| M3:QA17-IMPL-1 | P1 | új (QA17) | BLOCKED_HUMAN | célzott QA (QA17); D-08 |
| KANON:QA17-IMPL-6 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-23 |
| KANON:QA17-BIZT-7 | P2 | új (QA17) | BLOCKED_HUMAN | célzott QA (QA17) |
| KANON:QA17-BIZT-6 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-11 |
| KANON:QA17-BIZT-3 | P1 | új (QA17) | FIXED | célzott QA (QA17); D-16 |
| KANON:QA17-BIZT-3b | P1 | új (QA17) | BLOCKED_HUMAN | célzott QA (QA17); D-16 |
| KANON:QA17-BIZT-4 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-06 |
| M2:QA17-BIZT-5 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-15 |
| KANON:QA17-IMPL-4 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-15 |
| KANON:QA17-IMPL-5 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-15 |
| M7:QA17-ERT-1 | P1 | új (QA17) | FIXED | célzott QA (QA17); D-23 |
| M7:QA17-ERT-1b | P1 | új (QA17) | BLOCKED_HUMAN | célzott QA (QA17) |
| M3:QA17-ERT-2 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-03 |
| KANON:QA17-ERT-3 | P2 | új (QA17) | BLOCKED_HUMAN | célzott QA (QA17) |
| KANON:QA17-NYELV-1 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-16 |
| KANON:QA17-NYELV-2 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-08 |
| M0:QA17-NYELV-3 | P2 | új (QA17) | FIXED | célzott QA (QA17) |
| M3:QA17-NYELV-4 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-03 |
| M7:QA17-NYELV-5 | P2 | új (QA17) | FIXED | célzott QA (QA17) |
| Z:QA17-NYELV-6 | P2 | új (QA17) | FIXED | célzott QA (QA17) |
| KANON:QA17-NYELV-7 | P2 | új (QA17) | FIXED | célzott QA (QA17) |
| KANON:QA17-NYELV-8 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-13 |
| KANON:QA17-NYELV-9 | P2 | új (QA17) | FIXED | célzott QA (QA17) |
| M2:QA17-NYELV-10 | P2 | új (QA17) | FIXED | célzott QA (QA17) |
| M7:QA17-NYELV-11 | P1 | új (QA17) | DUPLICATE | célzott QA (QA17) |
| KANON:QA17-NYELV-12 | P2 | új (QA17) | FIXED | célzott QA (QA17); D-11 |
| KANON:QA17-NYELV-13 | P2 | új (QA17) | FIXED | célzott QA (QA17) |
| M3:QA17-NYELV-14 | P2 | új (QA17) | BLOCKED_HUMAN | célzott QA (QA17); D-03 |

## 6. Mi kell a staging buildhez, és mi a learner release-hez

- **Gépi állapot (`content_integrity.py --release-report`):** `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` · `LEARNER-RELEASE-VERDICT: NO-GO`.
- **Staging build:** a gépi verdikt engedi; a tényleges staging deploymenthez a projektgazda külön, kifejezett engedélye kell (ebben a futásban nem volt), és a G4 build-előfeltételei (dátumok, kontaktok, tracker #4).
- **Learner release:** a runtime-tesztek `RUNTIME_VERIFIED` állapota (G3b, G5b; LMS-csomag), a G1 Memuna-„átnéztem” (GYV-24), a G2 DPO release-QA (ADV-E1–E3), a SIGNOFF-ok (SIG-1…SIG-6, ERT-19), a média-jogosultsági kapuk (J1, J2, V1, V3), a VO fix pack, a HUM 15 nyitott szerepköri sorai, majd a `FINAL_RELEASE_QA` és a go/no-go döntés.
- A futó M0/M1 pilot (`main@213a4c5`) és a CC-04 freeze változatlan; PR #30 draft.
