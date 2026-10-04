# Projektgazdai döntések — BSPEC-02 leltár, D-1…D-6 (2026-10-04)

> A fájlnév a megnyitáskori D-1…D-3 állapotot őrzi; a D-4…D-6 és a H-6 kezelése lent, külön szakaszban.

> **Döntési jegyzőkönyv, a projektgazda szövege szó szerint.** A `2026-10-04 BSPEC-02 leltár – validált mezőleltár,
> 1–7. scope.md` 3.1 szakaszának három blokkoló kérdésére adott válasz, a munkamenetben beillesztett szövegként
> (bázis: `ed82dbb`, munkaág `fix/moodle-build-hardening`). A kanonikus döntési helyre (`02 Tervezet/Emberi jóváhagyás
> szükséges.md`, 10. szakasz) a `/course-fix` vezeti át; addig ez a jegyzőkönyv a bizonyíték. Azonosítók a
> BSPEC-02 leltáron belül: D-1, D-2, D-3 (a BS-D1…D8 sorozattól független). Utólagos ellenőrzés (vétó/QA) a döntés
> szövege szerint: a DPO, a privacy-megoldásra.

## A projektgazda szövege (2026-10-04, szó szerint)

> Projektgazdai döntés D-1–D-3, 2026-10-04. Ezeket durably rögzítsd a BSPEC-02 audit trailben, és ezekkel folytasd a maradék inventory review-kat.
>
> ## D-1 — M1.3 Slide 5
>
> A Slide 5 vezetett S/B/I-mondat **NEM önálló completion condition és NEM tárolandó learner artifact**.
>
> Indok:
> - ez kifejezetten gyakorló/scaffold elem;
> - nincs szükség mentor- vagy értékelői hozzáférésre;
> - a pedagógiai célt tárolás nélkül is teljesíti;
> - a következő, Slide 6 mini-SBI már önálló, kötelező gyakorlati produktum.
>
> Tehát:
>
> - M1.3 Slide 5 → `REQUIRED_BUT_LEARNER_LOCAL`
> - ne kapjon külön manifest row-t;
> - ne legyen a Slide 5 válaszának eltárolása completion-feltétel;
> - a lesson szövegéből/runtime-specből javítsd majd a tárolást/completiont sugalló ellentmondó állításokat.
>
> A Slide 6 mini-SBI ettől külön:
>
> - kötelező;
> - tárolt;
> - új `LMS-M1-07`;
> - 3 mező: S, B, I.
>
> ## D-2 — Z.1 Slide 5
>
> A Z.1 Slide 5 „Az én félévem fénypontjai” reflexió **kötelező pedagógiai gyakorlat, de learner-local**.
>
> Nem készül hozzá új TEXT-C manifest row.
>
> Indok:
> - a Z.1 célja visszatekintő/scaffolding mikrolecke;
> - ugyanennek a reflektív evidenciának a tényleges beadandó változatát a Z.4 kötelező záró reflexió gyűjti;
> - a Z.1-ben ugyanennek névre szóló tárolása pedagógiailag nem szükséges és redundáns adatgyűjtés lenne;
> - az Adatvédelem §2 alapelve szerint a puszta önreflexió a tanulónál marad, ha a tanulási cél nem igényel külön beadandó produktumot.
>
> Tehát:
>
> - Z.1 Slide 5 → `REQUIRED_BUT_LEARNER_LOCAL`
> - nincs mentor-visible tárolt válasz;
> - nincs új manifest TEXT-C;
> - a lesson completion nem a reflexió tartalmának eltárolásától függ;
> - a jelenlegi mentor/értékelő-láthatóságot, beadást, minimális karakterszámot vagy tárolást feltételező szöveget majd /course-fix-ben igazítsd ehhez;
> - a tanuló használhat saját jegyzetet / lokális munkafelületet, és a Z.4-ben később beadja a szükséges záró produktumot.
>
> ## D-3 — Z.2 Slide 5–6
>
> A Z.2 Slide 5 „Saját tanulási pillanatom” és Slide 6 „Nehéz modul / ellenállás” **kötelező pedagógiai reflexiók, de learner-local elemek**.
>
> Nem tároljuk őket Moodle-ben névre szóló szabad szöveges válaszként, és nem készül hozzájuk új TEXT-C manifest row.
>
> Indok:
> - ezek reflektív scaffolding feladatok;
> - a Z.4 a tényleges kötelező, mentor által látható záró reflektív produktum;
> - a személyes/nehéz élményről szóló 5–8 mondatos szövegek névre szóló tárolása nem szükséges ugyanahhoz a pedagógiai célhoz;
> - az adatminimalizálási alapelv alapján a személyes önreflexió alapértelmezésben a learnernél marad;
> - a tanulási folyamat kötelező jellege nem teszi szükségessé a válasz tartalmának központi tárolását.
>
> Tehát:
>
> - Z.2 Slide 5 → `REQUIRED_BUT_LEARNER_LOCAL`
> - Z.2 Slide 6 → `REQUIRED_BUT_LEARNER_LOCAL`
> - Z.2 Slide 7 háromszavas check → továbbra is `REQUIRED_BUT_LEARNER_LOCAL`
> - nincs új TEXT-C row;
> - nincs mentor-visible Z.2 essay storage;
> - a lesson completion a lecke elvégzésére épüljön, ne a reflexió tartalmának beadására;
> - a jelenlegi „beadott válaszaidat csak a kijelölt mentor…” és hasonló tárolást feltételező szövegek /course-fix-ben igazítandók ehhez.
>
> A Z.4-et NE gyengítsd: az marad a formális, tárolt záró reflektív produktum.
>
> A DPO továbbra is QA/veto szerepben ellenőrizheti a privacy-megoldást, de a D-2/D-3 szerinti learner-local megoldást most projektgazdai döntésként kezeld a BSPEC-02 specifikáció lezárásához.
>
> ## Következő lépés
>
> Most fusson le a maradék 13 `/course-review` scope. Még NE indíts /course-fix-et és NE módosíts canonical course fájlokat.
>
> A review-k után:
>
> 1. egyesítsd az 1–20 scope teljes inventoryját;
> 2. minden mezőnek pontosan egy classificationje legyen;
> 3. alkalmazd D-1–D-3-at;
> 4. deduplikáld a findingokat;
> 5. ellenőrizd, maradt-e valódi BSPEC-02 HUMAN_DECISION_REQUIRED;
> 6. csak ezután álljunk át `/course-fix`-re.

## D-4…D-6 és a H-6 kezelése (AskUserQuestion, 2026-10-04)

A 20 scope egyesített leltára (`2026-10-04 BSPEC-02 leltár – egyesített mezőleltár, 1–20. scope.md`, 3. szakasz) után
maradt három BSPEC-02-blokkoló kérdésre és egy lefedettségi résre a projektgazda a munkamenetben, választógombos
kérdésre válaszolt. A kérdések és a választott opciók szó szerint (angolul, ahogy feltettük):

> **D-4:** „M0.1 SLIDE 6, M0.2 SLIDE 6, M5.2 SLIDE 9, M5.4 SLIDE 4–5 and M7.4 SLIDE 3 are mandatory in-lesson writing
> steps. Should they be learner-local, like D-1…D-3, or each get a stored, named TEXT-C row?”
> → **„Learner-local (Recommended)”** — „REQUIRED_BUT_LEARNER_LOCAL: mandatory step, not stored, not a completion
> condition, no TEXT-C row. Stored versions already exist: LMS-M5-05 (M5.2, M5.4), LMS-M7-05 + LMS-M7-10 (M7.4).
> M0.1/M0.2 have no stated storage purpose. /course-fix then aligns PT:225/:238 and PT:319 and rewrites the JIT boxes
> and "mentor sees it" lines.”
>
> **D-5:** „The M6.1–M6.4 practice text answers are the risk answers, open/avoid questions, "mit tanít"/variation
> fields and the M6.4 closing kvuca draft. Should they be learner-local or stored TEXT-C rows?”
> → **„Learner-local (Recommended)”** — „REQUIRED_BUT_LEARNER_LOCAL for all of them. The PT:222 parenthesis narrows to
> the choice items, and the accessibility minimum stays unchanged.”
>
> **D-6:** „The M0.3 SLIDE 7 "miben kérnél még segítséget" field. :318 calls it "jelzés a stábnak"; :44
> ("megoszthatsz") and :350 ("oda viheted") have the learner take it to the help channel. Which is it?”
> → **„Optional, learner-local (Recommended)”** — „Not stored; the learner takes the request to the "Segítség és
> kapcsolatok" channel (HUM-OPS-02). :318 gets aligned.”
>
> **H-6:** „M5.1:605 ("Írj le 1 mondatot (ha szeretnél)") was missing from the BSPEC-02 list. It is optional by its own
> text, so it needs no row, but its runtime template would push it into Moodle storage. How should it be handled?”
> → **„Extend X-1 to M5.1 (Recommended)”** — „Classify as OPTIONAL_LEARNER_LOCAL with no row. /course-fix makes the
> M5.1:24 template field-specific, with no extra review run.”

Utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős a privacy-megoldásra (HUM-PRIV-01), a D-1…D-3-mal azonos módon; a
mentori/gyermekvédelmi tagmondatok átírása (M0.2:457, M3.3, M3.4, Z.1, Z.2) a Memuna utólagos ellenőrzése alá esik.

## Következmények a leltárban (nem új döntés, a szöveg alkalmazása)

- A D-2b (karakterminimum a Z.1-ben) és a D-3b (passz a tárolt Z.2-mezőnél) tárgytalan: mindkettő csak a tárolt ágon
  állt volna fenn.
- A D-1 után az LMS-M1-07 három „Required” kérdése az S, a B és az I (6. dia); az 5. dia mezője nem kerül bele.
- A D-4…D-6 után a BSPEC-02 leltárában nem marad blokkoló emberi döntés; új TEXT-C sor csak a négy
  döntésfüggetlen (LMS-M1-07, LMS-M2-08, LMS-M2-09, LMS-M7-10). A D-4 és a D-5 a Program terv :222, :225, :238 és
  :319 sorának igazítását vonja maga után: a projektgazdai döntés az 1–3. forrás fölött áll.
