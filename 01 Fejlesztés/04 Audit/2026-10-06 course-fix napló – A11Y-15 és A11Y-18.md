# course-fix napló — A11Y-15 és A11Y-18 statikus előfeltételek (2026-10-06)

**Bemenet:** `01 Fejlesztés/04 Audit/2026-10-06 Fix pack – A11Y-15 és A11Y-18 statikus előfeltételek.md` (a 2026-10-06-i célzott `/course-review` validált findingjai: IMPL-15-1, IMPL-15-2, valamint az IMPL-18-1 és az IMPL-18-2 szűkített része).
**Bázis:** `fix/moodle-build-hardening`, HEAD `9ef2b25` + a Command 5 nem commitolt állapota.
**Alkalmazási sorrend:** A15-01…A15-28, majd B18-01…B18-09.
**Nem alkalmazandó (riport):** IMPL-15-3, IMPL-18-4 és az IMPL-18-1 M7 v2-es része (emberi döntés); IMPL-15-4, IMPL-18-5 (bizonyíték-kapu); IMPL-18-3 (elvetve).
**Megállási feltétel:** `media_manifest.py build`/`check` hiba, új `MEDIA-REQUIRED-*` sor, vagy a `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` sor változása.

## Lépések

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| A15-01 | SLIDE 4 címe típussemleges | M3.1 | alkalmazva | csere hozzáadott sor nélkül |
| A15-02 | „Mit látunk?”: alapból húzásmentes, mellette D&D | M3.1 | alkalmazva | |
| A15-03 | „rossz helyre húzásánál” → „rossz besorolásánál” | M3.1 | alkalmazva | |
| A15-04 | ♿ blokk: szerepcsere | M3.1 | alkalmazva | a completion-mondat változatlan |
| A15-05 | ♿ blokk: Single Choice Set → Multiple Choice egyválaszos | M3.1 | alkalmazva | |
| A15-06 | EGY-01 `spec` típusnév | M3.2 | alkalmazva | |
| A15-07 | EGY-02 `title` | M3.2 | alkalmazva | |
| A15-08 | EGY-02 `spec` | M3.2 | alkalmazva | |
| A15-09 | EGY-02 `technical` | M3.2 | alkalmazva | |
| A15-10 | „Mit látunk?” sorrend | M3.2 | alkalmazva | |
| A15-11 | ♿ blokk típusnév | M3.2 | alkalmazva | |
| A15-12 | Formátum-sor „Besorolás” | M3.4 | alkalmazva | csere hozzáadott sor nélkül; a „7 slide” változatlan |
| A15-13 | SLIDE 4 címe | M3.4 | alkalmazva | |
| A15-14 | EGY-03 `title` | M3.4 | alkalmazva | |
| A15-15 | EGY-03 `a11y` | M3.4 | alkalmazva | |
| A15-16 | EGY-04 `title` | M3.4 | alkalmazva | |
| A15-17 | EGY-04 `spec` | M3.4 | alkalmazva | |
| A15-18 | EGY-04 `technical` | M3.4 | alkalmazva | |
| A15-19 | EGY-04 `notes` | M3.4 | alkalmazva | |
| A15-20 | „Mit lát a tanuló?” | M3.4 | alkalmazva | |
| A15-21 | ♿ blokk: szerepcsere | M3.4 | alkalmazva | a completion-mondat változatlan |
| A15-22 | ♿ blokk típusnév | M3.4 | alkalmazva | |
| A15-23 | M3.1 eszközsor | M3 hub | alkalmazva | |
| A15-24 | M3.1 tartalomsor | M3 hub | alkalmazva | |
| A15-25 | M3.4 eszközsor „Besorolás” | M3 hub | alkalmazva | csere hozzáadott sor nélkül |
| A15-26 | M3.4 eszközsor D&D | M3 hub | alkalmazva | |
| A15-27 | M3.4 tartalomsor | M3 hub | alkalmazva | |
| A15-28 | formatív elemek felsorolása | M3 kapu | alkalmazva | |
| B18-01 | új `@asset` M1.4-MUNK-01 | M1.4 | alkalmazva | a blokk bájtra egyezik a fix packkal |
| B18-02 | új `@asset` M2-HUB-MUNK-01 | M2 hub | alkalmazva | a blokk bájtra egyezik a fix packkal |
| B18-03 | M2-HUB-DIA-01 `notes` igazítása | M2 hub | alkalmazva | |
| B18-04 | új `@asset` M3.4-MUNK-01 | M3.4 | alkalmazva | a blokk bájtra egyezik a fix packkal |
| B18-05 | új `@asset` M4.4-MUNK-01 | M4.4 | alkalmazva | a blokk bájtra egyezik a fix packkal |
| B18-06 | új `@asset` M7.4-MUNK-01 | M7.4 | alkalmazva | a blokk bájtra egyezik a fix packkal |
| B18-07 | File submissions ✅ | M1.4 | alkalmazva | |
| B18-08 | File submission ✅ | M1 kapu | alkalmazva | |
| B18-09 | EGY-07 `technical` beadási mód | M3.4 | alkalmazva | |

Összesítés: 37 lépés, mind `alkalmazva`; kihagyott vagy megállított lépés nincs. Mind a 31 csere régi szövege a futás előtt pontosan egyszer szerepelt; az öt új `@asset` blokk bájtra egyezik a fix packkal.

## Célzott újraellenőrzés (a diff-hunkokra) és a hurokzáró javítások

Implementációs és nyelvi lencse futott a futás saját változásain. A saját szerkesztésben talált objektív hibákat ugyanebben a futásban javítottam (hurokzáró szabály); utójavító kör nincs.

| ID | lencse | hely | állapot | megjegyzés |
|---|---|---|---|---|
| C7-IMPL-1 | implementáció | M3.2 :599, :679 | **megállva: emberi döntés** | az M3.2 alapértelmezett, koppintásos párosításának példatípusa ugyanaz, mint az EGY-02 húzásmentes változatáé; ez a kettőzés a futás előtt is megvolt (Single Choice Settel), a futás csak a típusnevet cserélte. Döntés: azonos-e a kettő (M3 modulgazda / build-felelős) |
| C7-NYELV-1 | nyelv | M3.4 :509; M3.2 :679 | alkalmazva | „Ez az út **csak billentyűzettel**…”: a „Single Choice Set nem alkalmas” mondat után a követelmény alanya visszaállítva |
| C7-NYELV-2 | nyelv | M3.2 :679 | alkalmazva | a gondolatjeles beékelés helyett zárójel |
| C7-NYELV-3 | nyelv | M3.1 :576; M3.2 :679; M3.4 :509 | alkalmazva | „válaszonkénti visszajelzéssel (`chosenFeedback`)”; az M3.1-ben a Single Choice Set-mondat önálló mondat lett |
| C7-NYELV-4 | nyelv | M3.1 :576; M3.4 :509 | alkalmazva | „alapból húzás nélkül teljesíthető” (a félrevezető „is” kikerült) |
| C7-NYELV-5 | nyelv | M3.1 :576; M3.4 :509 | alkalmazva | „a húzásmentes forma mellett elérhető Drag & Drop” |
| C7-NYELV-6 | nyelv | M3.1 :553 | alkalmazva | „6–8 „kártya” … , a Drag & Drop-változatban az oszlopcímek alatt.”: a kártyaszám mindkét formára vonatkozik, az „alul” csak a Drag & Dropra; a kártyaszám változatlan |
| C7-NYELV-7 | nyelv | M3 kapu :42 | alkalmazva | „– mellettük Drag & Drop is –, valamint minikvíz” |
| C7-NYELV-8 | nyelv | M3 hub :137 | alkalmazva | „mellette H5P Drag & Drop két célzónával” (az A15-26 alakja) |
| C7-NYELV-9 | nyelv | M4.4-MUNK-01 `purpose` | alkalmazva | „Az online szöveges leadással egyenértékű” |
| C7-NYELV-10 | nyelv | az öt új asset `purpose` mezője; M7.4-MUNK-01 `a11y` | alkalmazva | „fájlalapú”, „táblázatstruktúra”; az M5.4 és az M3.B azonos alakja nem e futás változása, nem javítva |

## Záró futás

- A teljes diff visszaolvasva (a futás 10 tananyagfájlja).
- Média: `media_manifest.py build` kétszer a csomag után, és kétszer a nyelvi javítások után, mindkét párnál azonos kimenettel (420 asset, 913 deliverable); `check`: 10 generált kimenet naprakész, 747 történeti sor egyeztetve; `reconcile`: nem egyeztetett 0.
- Megállási feltétel nem teljesült: `--release-report` → `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` (build-spec blockers: 0), új `MEDIA-REQUIRED-*` sor nincs; `LEARNER-RELEASE-VERDICT: NO-GO` (learner-release blockers: 7, változatlan).
- Pin: a csomag után egy `--pin-visible` (7 fájl); a nyelvi hurokzáró javítások a látható szöveget újra módosították, ezért ugyanehhez a változáskészlethez egy második `--pin-visible` is futott (5 fájl).
- `content_integrity.py` 0 hiba; `--selftest` 57/57; `unittest tools.test_media_manifest`: 159 teszt OK; `py_compile` OK; `git diff --check` és a PR-tartomány `--check`-je tiszta.
- Nem került lezárásra: a hozzáférhetőségi sztenderd :128 és :132 tétele (release-evidence), IMPL-15-3, IMPL-18-4, az M7 v2 sablon (emberi döntés), IMPL-15-4, IMPL-18-5 (bizonyíték-kapu), C7-IMPL-1 (emberi döntés).
- Nem commitolva, nem pusholva.
