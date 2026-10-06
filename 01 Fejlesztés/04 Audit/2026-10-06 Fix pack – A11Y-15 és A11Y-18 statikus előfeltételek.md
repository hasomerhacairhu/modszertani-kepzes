# Fix pack – A11Y-15 és A11Y-18 statikus előfeltételek (2026-10-06)

**Forrás:** célzott `/course-review` (2026-10-06), a Command 5 utáni, nem commitolt working tree-n. Két lencse (implementáció: A11Y-15 / R-13 és A11Y-18 / R-15), egyetlen adverzális `verifier`-kör az összes findingra. Ez a fájl a validált findingok tartós rögzítése és a `/course-fix` bemenete; audit trail, nem tanulói tartalom.

**Lezárt döntés, amelyet a csomag követ:** `Emberi jóváhagyás szükséges.md`, „Az A11Y-15 és az A11Y-18 besorolása” sor: „Ha valamelyik tételnek statikus, repóban javítható előfeltétele van, azt még aznap be kell fejezni; a runtime/renderelt bizonyíték RELEASE-EVIDENCE marad.” A hozzáférhetőségi sztenderd :128 és :132 checklist-tétele ezért **nyitva marad** (release-evidence); a csomag ezekhez nem nyúl.

**Verdiktek:**
- R-13 (A11Y-15): **CONFIRMED.**
- R-15 (A11Y-18): **CONFIRMED, szűkítve.** Az M5 (LMS-M5-05) megoldott (`M5.4-MUNK-01` + online text + fájl). Az M4 és az M2 online text + fájl része is rendben; az M6 és az M7 beadási módjáról a lecke hallgat, ott a manifest ASSIGN-S/ASSIGN-M profilja irányadó.
- Build-regresszió a Command 5-höz képest: **nincs.** A `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` nem nyílik újra.

**A verifier számai:** 4 MEGERŐSÍTVE (IMPL-15-1, IMPL-15-2; bizonyíték-kapu: IMPL-15-4, IMPL-18-5), 2 RÉSZBEN (IMPL-18-1, IMPL-18-2), 1 ELVETVE (IMPL-18-3), 2 EMBERI DÖNTÉS (IMPL-15-3, IMPL-18-4); az IMPL-18-1 M7 v2-es része külön emberi döntés.

---

## Alkalmazandó (objektív, MEGERŐSÍTVE / RÉSZBEN)

Általános korlát minden lépésre:
- **Tilos:** ✅ és bármely helyes válasz, kártyaszöveg, helyes besorolás, visszajelzés-szöveg (köztük az M3.4 6–8. kártya HUM-SAFE-04-alapú és a 10. kártya red flag-visszajelzése), completion-szemantika (a két forma egyenértékű, mindkettő önmagában completiont ad), kártyaszámok („6–8”, „7”, „8–10 (ténylegesen 10)”), a „7 slide” szám, a meglévő asset-ID-k, Tab+Enter / ≥24px, rubrika, küszöb, BSPEC-05/06/07, GATE-CP, a „puszta fájlfeltöltés nem completion” mondatok, minden adatvédelmi, just-in-time és biztonsági szöveg, valamint a hozzáférhetőségi sztenderd :128 és :132 checkboxa.
- **Nem írható:** Drag & Drop-indoklás (IMPL-15-3, emberi döntés), és a Drag & Drop nem törölhető: a csomag csak az alapértelmezett és a második forma sorrendjét cseréli.
- **Cserénél:** a „Régi” blokk szövege pontosan egyszer szerepel a megnevezett fájlban (2026-10-06-án ellenőrizve: mind a 31 csere egyedi); előbb `grep -cF` a régi szövegre, és ha a találat nem 1, a lépés kihagyandó és jelentendő. A blokkok tartalma szó szerint értendő, a sor eleji szóközökkel együtt.

### IMPL-15-1 + IMPL-15-2 — M3: a húzásmentes forma az alapértelmezett, típusa Multiple Choice egyválaszos módban

- **ID:** IMPL-15-1 (P2, objektív, MEGERŐSÍTVE) és IMPL-15-2 (P1, objektív, MEGERŐSÍTVE)
- **Probléma:** az M3.1 és az M3.4 elsődleges, címbeli típusa Drag & Drop, a húzásmentes út csak „alternatíva”, miközben az M3.2-ben a koppintásos párosítás az alapértelmezett; és mindhárom lecke húzásmentes útja H5P Single Choice Set-et ír elő kártyánkénti visszajelzéssel, holott a Single Choice Setnek nincs válaszonkénti visszajelzése.
- **Bizonyíték:**
  - hozzáférhetőségi sztenderd :32 „A **Drag & Drop kerülendő** ennél a mobil-first célközönségnél” · :34 „Az interakció-típus legyen **következetes a modulon belül**”
  - M3.1 :548 „* H5P **Drag & Drop**: felül 4 nagy, jól látható oszlopcím:” · M3.4 :400 „### SLIDE 4 – ACTIVITY: H5P Drag and Drop – „OK / Nem OK madrihként”” ↔ M3.2 :679 „A párosítást alapból **ujjbarát, koppintásos párosításként** vidd be”
  - M3.4 :509 „H5P **Single Choice Set**, kártyánként egy kérdés. … a per-kártya visszajelzés ugyanaz, mint a húzós verzióban” ↔ runtime acceptance :80 „a Single Choice Setben … válaszonkénti visszajelző mezője nincs”; precedens a cserére: M0.2 :253 (Multiple Choice egyválaszos módban, `chosenFeedback`), sztenderd :31 (mindkét típus húzásmentes)
- **Javítás:** az alábbi szó szerinti cserék, ebben a sorrendben. Új szöveg csak a típusnév, a szerepcsere és a sztenderd :32 szó szerinti indoka.

**A15-01** — `02 Tervezet/Modulok/M3/Online leckék/M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md`

Régi:
```text
### SLIDE 4 – ACTIVITY: „Találd ki, melyik szakaszban jár a kvuca!” – Drag\&Drop
```
Új:
```text
### SLIDE 4 – ACTIVITY: „Találd ki, melyik szakaszban jár a kvuca!”
```

**A15-02** — ugyanaz a fájl (M3.1)

Régi:
```text
* H5P **Drag & Drop**: felül 4 nagy, jól látható oszlopcím:
```
Új:
```text
* Alapból kártyánként egy húzásmentes, rádiógombos kérdés a 4 Tuckman-szakasszal (lásd lent: ♿); mellette H5P **Drag & Drop** is, amelyben felül 4 nagy, jól látható oszlopcím áll:
```

**A15-03** — M3.1

Régi:
```text
* Minden kártya rossz helyre húzásánál 1 mondatos, barátságos magyarázat:
```
Új:
```text
* Minden kártya rossz besorolásánál 1 mondatos, barátságos magyarázat:
```

**A15-04** — M3.1

Régi:
```text
> ♿ **Kötelező húzásmentes alternatíva (LMS a11y-sztenderd, 3. szakasz + kapus pre-flight):** mivel ez a lecke a kapu belépő feltétele (activity completion), a Drag & Drop **nem lehet az egyetlen út**. Tedd be ugyanezt a 6–8 szituációt **húzás nélkül is teljesíthető** formában:
```
Új:
```text
> ♿ **Kötelező húzásmentes út – ez az alapértelmezett forma (LMS a11y-sztenderd, 3. szakasz + kapus pre-flight):** mivel ez a lecke a kapu belépő feltétele (activity completion), és a sztenderd szerint a Drag & Drop kerülendő, a 6–8 szituáció **alapból húzás nélkül is teljesíthető** formában szerepel; a mellette elérhető Drag & Drop **nem lehet az egyetlen út**. A forma:
```

**A15-05** — M3.1

Régi:
```text
(H5P **Single Choice Set**, kártyánként egy kérdés; legördülős kitöltés Course Presentationben nem érhető el). Az alternatíva **csak billentyűzettel**
```
Új:
```text
(kártyánként egy H5P **Multiple Choice** elem egyválaszos – „Single Choice (Radio Buttons)” – módban, a visszajelzés válaszonként, `chosenFeedback`; a Single Choice Set nem alkalmas, mert válaszonkénti visszajelzése nincs; legördülős kitöltés Course Presentationben nem érhető el). Ez az út **csak billentyűzettel**
```

**A15-06** — `02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md` (M3.2-EGY-01 `spec`)

Régi:
```text
(a konkrét H5P-típust, pl. jelenetenként Single Choice Set, a runtime acceptance-ben kell igazolni)
```
Új:
```text
(a konkrét H5P-típust, pl. jelenetenként egy Multiple Choice elem egyválaszos – „Single Choice (Radio Buttons)” – módban, válaszonkénti visszajelzéssel, a runtime acceptance-ben kell igazolni)
```

**A15-07** — M3.2 (M3.2-EGY-02 `title`)

Régi:
```text
"title": "Húzásmentes párosító alternatíva (Single Choice Set)",
```
Új:
```text
"title": "Húzásmentes párosító változat (Multiple Choice egyválaszos módban)",
```

**A15-08** — M3.2 (M3.2-EGY-02 `spec`)

Régi:
```text
– H5P Single Choice Set (legördülős kitöltés Course Presentationben nem érhető el).
```
Új:
```text
– jelenetenként egy H5P Multiple Choice elem egyválaszos („Single Choice (Radio Buttons)”) módban, válaszonkénti visszajelzéssel (`chosenFeedback`); legördülős kitöltés Course Presentationben nem érhető el.
```

**A15-09** — M3.2 (M3.2-EGY-02 `technical`)

Régi:
```text
"note": "H5P Single Choice Set, billentyűzettel navigálható,
```
Új:
```text
"note": "H5P Multiple Choice egyválaszos („Single Choice (Radio Buttons)”) módban, válaszonkénti visszajelzéssel (`chosenFeedback`), billentyűzettel navigálható,
```

**A15-10** — M3.2

Régi:
```text
* H5P **Drag & Drop** vagy koppintásos párosítás.
```
Új:
```text
* Alapból koppintásos párosítás, mellette H5P **Drag & Drop** is (lásd lent: ♿).
```

**A15-11** — M3.2

Régi:
```text
– **Single Choice Set** (legördülős kitöltés Course Presentationben nem érhető el).
```
Új:
```text
– jelenetenként egy H5P **Multiple Choice** elem egyválaszos – „Single Choice (Radio Buttons)” – módban, a visszajelzés válaszonként, `chosenFeedback`; a Single Choice Set nem alkalmas, mert válaszonkénti visszajelzése nincs (legördülős kitöltés Course Presentationben nem érhető el).
```

**A15-12** — `02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md` (a `**Formátum:**` sorban)

Régi:
```text
Besorolás (Drag and Drop)
```
Új:
```text
Besorolás
```

**A15-13** — M3.4

Régi:
```text
### SLIDE 4 – ACTIVITY: H5P Drag and Drop – „OK / Nem OK madrihként”
```
Új:
```text
### SLIDE 4 – ACTIVITY: Besorolás – „OK / Nem OK madrihként”
```

**A15-14** — M3.4 (M3.4-EGY-03 `title`)

Régi:
```text
"title": "H5P Drag and Drop (két célzóna) – „OK / Nem OK madrihként” (SLIDE 4)",
```
Új:
```text
"title": "H5P Drag and Drop (két célzóna) – „OK / Nem OK madrihként” (SLIDE 4, a húzásmentes alapértelmezett út mellett)",
```

**A15-15** — M3.4 (M3.4-EGY-03 `a11y`)

Régi:
```text
"note": "Kötelező húzásmentes alternatíva (lásd M3.4-EGY-04); billentyűzetes elérés"
```
Új:
```text
"note": "A húzásmentes alapértelmezett út az M3.4-EGY-04; billentyűzetes elérés"
```

**A15-16** — M3.4 (M3.4-EGY-04 `title`)

Régi:
```text
"title": "Húzásmentes a11y-alternatíva – Single Choice Set (SLIDE 4)",
```
Új:
```text
"title": "Húzásmentes alapértelmezett út – Multiple Choice egyválaszos módban (SLIDE 4)",
```

**A15-17** — M3.4 (M3.4-EGY-04 `spec`)

Régi:
```text
H5P Single Choice Set (kártyánként egy kérdés). Csak billentyűzettel
```
Új:
```text
kártyánként egy H5P Multiple Choice elem egyválaszos („Single Choice (Radio Buttons)”) módban, válaszonkénti visszajelzéssel (`chosenFeedback`). Csak billentyűzettel
```

**A15-18** — M3.4 (M3.4-EGY-04 `technical`)

Régi:
```text
"note": "H5P Single Choice Set, billentyűzetes,
```
Új:
```text
"note": "H5P Multiple Choice egyválaszos („Single Choice (Radio Buttons)”) módban, kártyánként egy elem, válaszonkénti visszajelzéssel (`chosenFeedback`), billentyűzetes,
```

**A15-19** — M3.4 (M3.4-EGY-04 `notes`)

Régi:
```text
"notes": "Az M3.4-EGY-03 besoroló (Drag and Drop) feladat kötelező alternatívája; azonos kártyakészlet és visszajelzés.",
```
Új:
```text
"notes": "A SLIDE 4 alapértelmezett, húzásmentes besorolója; mellette az M3.4-EGY-03 (Drag and Drop) is elérhető; azonos kártyakészlet és visszajelzés.",
```

**A15-20** — M3.4

Régi:
```text
* H5P **Drag & Drop** (két célzóna):
```
Új:
```text
* Alapból kártyánként egy húzásmentes, kétopciós rádiógombos kérdés (lásd lent: ♿); mellette H5P **Drag & Drop** is, két célzónával:
```

**A15-21** — M3.4

Régi:
```text
> ♿ **Kötelező húzásmentes alternatíva (LMS a11y-sztenderd, 3. szakasz + kapus pre-flight):** mivel ez a lecke a kapu belépő feltétele (activity completion), a Drag & Drop **nem lehet az egyetlen út**. Vidd be ugyanezt a 8–10 helyzetkártyát **húzás nélkül is teljesíthető** formában:
```
Új:
```text
> ♿ **Kötelező húzásmentes út – ez az alapértelmezett forma (LMS a11y-sztenderd, 3. szakasz + kapus pre-flight):** mivel ez a lecke a kapu belépő feltétele (activity completion), és a sztenderd szerint a Drag & Drop kerülendő, a 8–10 helyzetkártya **alapból húzás nélkül is teljesíthető** formában szerepel; a mellette elérhető Drag & Drop **nem lehet az egyetlen út**. A forma:
```

**A15-22** — M3.4

Régi:
```text
– H5P **Single Choice Set**, kártyánként egy kérdés.
```
Új:
```text
– kártyánként egy H5P **Multiple Choice** elem egyválaszos („Single Choice (Radio Buttons)”) módban, a visszajelzés válaszonként (`chosenFeedback`); a Single Choice Set nem alkalmas, mert válaszonkénti visszajelzése nincs.
```

**A15-23** — `02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md`

Régi:
```text
  * H5P Drag & Drop + Single Choice Set
```
Új:
```text
  * Húzásmentes besorolás (kártyánként egy H5P Multiple Choice elem egyválaszos módban) + H5P Drag & Drop
```

**A15-24** — M3 hub

Régi:
```text
  * Drag & Drop feladat: 6–8 helyzet → megfelelő Tuckman-szakasz.
```
Új:
```text
  * Besorolási feladat (alapból húzásmentes, mellette Drag & Drop): 6–8 helyzet → megfelelő Tuckman-szakasz.
```

**A15-25** — M3 hub (az M3.4 eszközsorában)

Régi:
```text
Besorolás (Drag and Drop)
```
Új:
```text
Besorolás
```

**A15-26** — M3 hub

Régi:
```text
  * H5P Drag & Drop két célzónával – „OK / Nem OK madrihként”
```
Új:
```text
  * Húzásmentes besorolás (kártyánként egy H5P Multiple Choice elem egyválaszos módban) + H5P Drag & Drop két célzónával – „OK / Nem OK madrihként”
```

**A15-27** — M3 hub

Régi:
```text
Csoportosító feladat (H5P Drag & Drop, két célzóna)
```
Új:
```text
Csoportosító feladat (alapból húzásmentes, mellette H5P Drag & Drop, két célzóna)
```

**A15-28** — `02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md`

Régi:
```text
(Drag & Drop, koppintásos párosítás, minikvíz)
```
Új:
```text
(húzásmentes besorolás és koppintásos párosítás, mellette Drag & Drop, minikvíz)
```

### IMPL-18-1 (RÉSZBEN) — letölthető beadási sablon M1, M2, M3, M4 és M7 v1 számára

- **ID:** IMPL-18-1 (P1, objektív a szűkített részben, RÉSZBEN)
- **Probléma:** az M1 SBI-beadandóhoz, az M2 identitás-jegyzethez, az M3 helyzetleíráshoz, az M4.4 peulabemutató-vázlathoz és a Peula v1-hez nincs deklarált, letölthető (doc) beadási sablon.
- **Bizonyíték:** Program terv :279 „…a tanuló a Moodle-ben közvetlenül szövegként is beírhatja a produktumot, ÉS letölthet egy sablont, amit kitöltve fájlként ad fel”; hozzáférhetőségi sztenderd :46 „adj **letölthető sablont** (doc / sheet; Google-sablont csak szervezeti fiókból, korlátozott megosztással, HUM-PRIV-01)”; M4.4 :759 „* Fájlfeltöltés: 1 oldalas doc / pdf, a letölthető sablon alapján.” (asset nincs); M2 hub :149 „…így az nem ennek a hubnak az assete”.
- **Javítás:** öt új `@asset` blokk, **pontosan** az alábbi tartalommal, az `M5.4-MUNK-01` mintájára (`kind: worksheet`, R2 nélkül, `blockers: []`, így a fordító szerint `spec-ready`). Az öt ID 2026-10-06-án sehol nem szerepelt a repóban. A sablonok tartalma kizárólag a forrás meglévő szövege; minden blokk előtt és után egy üres sor. A beszúrási horgonyok egyediek (mindegyik pontosan 1 találat).
- **Megállási feltétel:** ha a `media_manifest.py build` / `check` hibát ad, vagy a `content_integrity.py --release-report` bármely új `MEDIA-REQUIRED-*` sort, illetve a `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` sor változását mutatja, a lépés nem kész: állj meg, és jelentsd a pontos kimenetet.

**B18-01** — `02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md`, közvetlenül a `### 3.2. Assignment beállítások (javaslat)` címsor után:

```
<!-- @asset
{
  "id": "M1.4-MUNK-01",
  "kind": "worksheet",
  "mode": "generate",
  "title": "Letölthető „SBI-beadandó” kitölthető sablon (doc)",
  "purpose": "Az M1 kapu beadandójának (LMS-M1-05) fájl-alapú leadási útja: aki nem online szövegként ad le, ennek kitöltésével és feltöltésével adja le az SBI-t. A két út egyenértékű (Program terv §5; hozzáférhetőségi sztenderd §4).",
  "spec": "Kitölthető sablon doc formátumban, kizárólag a lecke 2–4. lépésének meglévő elemeivel, szó szerint: a három mező („S – Szituáció: mikor, hol, milyen helyzetben történt?”, „B – Viselkedés: mit csinált a másik konkrétan (megfigyelés, nem címke)?”, „I – Hatás: ez hogyan hatott rád vagy a csapatra?”); a „Formátum – javaslat” mondatváza („Amikor [S – mikor, hol, milyen helyzetben voltunk], és te [B – mit csináltál konkrétan], én / a kvuca [I – mit éreztem / mi lett a hatás].”); két SBI-blokk a 4. lépés szerint (minimum 1 teljes SBI-mondat, maximum 2 különböző SBI); a sablon végén szó szerint a lecke „Extra biztonsági megjegyzés a leírás végére” blokkja. Új mező, minta vagy útmutató szöveg nem kerül bele.",
  "provenance": "human",
  "technical": {
    "note": "Szerkeszthető dokumentum: Google Doc (csak szervezeti fiókban, korlátozott megosztással) és/vagy .docx; A4 nyomtatható elrendezés is; magyar nyelv. Moodle-ben az Assignment „Additional files” mezőjébe kerül."
  },
  "a11y": {
    "note": "Valódi szöveges dokumentum (nem kép), címsorokkal és megjelölt kitöltési helyekkel, hogy képernyőolvasóval is használható és kitölthető legyen; a dokumentum nyelve magyarra állítva."
  },
  "derivatives": [
    "print-pdf"
  ],
  "production_rules": [
    "R5"
  ],
  "blockers": [],
  "notes": "A11Y-18 statikus előfeltétele (IMPL-18-1): a Program terv §5 beadási szabálya és a hozzáférhetőségi sztenderd §4 szerinti letölthető sablon; tartalma kizárólag a lecke meglévő szövegéből áll. Az Assignment online-text mezőjének egyenértékű alternatívája. A sablon letölthetőségét és akadálymentességét a renderen kell igazolni (release-evidence)."
}
-->
```

**B18-02** — `02 Tervezet/Modulok/M2/M2 – Ki vagyok madrihként – Identitás, Somer-értékek és dugma isit.md`, a §6 „Követelmény az M2 „complete”-hez” lista 5. pontja után, közvetlenül a `**Puha kapu küszöbe (az értékelő-fájlból átvéve):**` sor előtt:

```
<!-- @asset
{
  "id": "M2-HUB-MUNK-01",
  "kind": "worksheet",
  "mode": "generate",
  "title": "Letölthető „Madrih identitás-jegyzet” kitölthető sablon (doc)",
  "purpose": "Az M2 identitás-jegyzet (LMS-M2-05) fájl-alapú leadási útja: aki nem online szövegként ad le, ennek kitöltésével és feltöltésével adja le a jegyzetet. A két út egyenértékű (Program terv §5; hozzáférhetőségi sztenderd §4).",
  "spec": "Kitölthető sablon doc formátumban, kizárólag az „M2 – KAPU – értékelő” fájl D. szakaszának („1 oldalas identitás-jegyzet – sablon (a tanulónak)”) szövegével, szó szerint: a bevezető bekezdés a 🔒 „Mit kérünk és mit nem” blokkal együtt, majd a „MADRIH IDENTITÁS-JEGYZET · M2” váz minden blokkja a kitöltési helyekkel. Új mező, minta vagy útmutató szöveg nem kerül bele.",
  "provenance": "human",
  "technical": {
    "note": "Szerkeszthető dokumentum: Google Doc (csak szervezeti fiókban, korlátozott megosztással) és/vagy .docx; A4 nyomtatható elrendezés is; magyar nyelv. Moodle-ben az Assignment „Additional files” mezőjébe kerül."
  },
  "a11y": {
    "note": "Valódi szöveges dokumentum (nem kép), címsorokkal és megjelölt kitöltési helyekkel, hogy képernyőolvasóval is használható és kitölthető legyen; a dokumentum nyelve magyarra állítva."
  },
  "derivatives": [
    "print-pdf"
  ],
  "production_rules": [
    "R5"
  ],
  "blockers": [],
  "notes": "A11Y-18 statikus előfeltétele (IMPL-18-1). A jegyzet-sablon kanonikus szövege az „M2 – KAPU – értékelő” D. szakasza; ez az asset annak letölthető, kitölthető változata, nem új tartalom. A hub deklarálja, mert a kapu-fájl `@asset-free`. A sablon letölthetőségét és akadálymentességét a renderen kell igazolni (release-evidence)."
}
-->
```

**B18-03** — ugyanebben a fájlban, az M2-HUB-DIA-01 `notes` mezőjében:

Régi:
```text
fájlban él, így az nem ennek a hubnak az assete – nincs duplikáció.
```
Új:
```text
fájlban él; a jegyzet-sablon letölthető, kitölthető változata az M2-HUB-MUNK-01 (§6), amely a KAPU D. szakaszát szó szerint veszi át – nincs duplikáció.
```

**B18-04** — `02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md`, közvetlenül az `**Assignment-sablon (Moodle-feladat szövegéhez):**` sor előtt:

```
<!-- @asset
{
  "id": "M3.4-MUNK-01",
  "kind": "worksheet",
  "mode": "generate",
  "title": "Letölthető „Helyzetleírás red flagekkel” kitölthető sablon (doc)",
  "purpose": "Az M3 kapu helyzetleírásának (LMS-M3-05) fájl-alapú leadási útja: aki nem online szövegként ad le, ennek kitöltésével és feltöltésével adja le a helyzetleírást. A két út egyenértékű (Program terv §5; hozzáférhetőségi sztenderd §4).",
  "spec": "Kitölthető sablon doc formátumban, kizárólag a SLIDE 7 „Assignment-sablon (Moodle-feladat szövegéhez)” tanulói szövegével, szó szerint: a bevezető bekezdés (a valódi név és a valós eset tilalmával és a Memunára vonatkozó mondattal együtt), majd az 5 vezetett kérdés az alpontjaival, mindegyik után kitöltési hellyel. A dőlt „Képzői/fejlesztői jegyzet” nem tanulói szöveg, nem kerül bele. Új mező, minta vagy útmutató szöveg nem kerül bele.",
  "provenance": "human",
  "technical": {
    "note": "Szerkeszthető dokumentum: Google Doc (csak szervezeti fiókban, korlátozott megosztással) és/vagy .docx; A4 nyomtatható elrendezés is; magyar nyelv. Moodle-ben az Assignment „Additional files” mezőjébe kerül."
  },
  "a11y": {
    "note": "Valódi szöveges dokumentum (nem kép), címsorokkal és megjelölt kitöltési helyekkel, hogy képernyőolvasóval is használható és kitölthető legyen; a dokumentum nyelve magyarra állítva."
  },
  "derivatives": [
    "print-pdf"
  ],
  "production_rules": [
    "R5"
  ],
  "blockers": [],
  "notes": "A11Y-18 statikus előfeltétele (IMPL-18-1): az M3.4-EGY-07 Moodle-feladatszövegének letölthető, kitölthető változata, a tanulói szöveg szó szerinti átvételével; nem új tartalom. A sablon letölthetőségét és akadálymentességét a renderen kell igazolni (release-evidence)."
}
-->
```

**B18-05** — `02 Tervezet/Modulok/M4/Online leckék/M4.4 – 45 mp-es peulabemutató – vázlat egy konkrét kvucára.md`, közvetlenül a `* Fájlfeltöltés: 1 oldalas doc / pdf, a letölthető sablon alapján.` sor után:

```
<!-- @asset
{
  "id": "M4.4-MUNK-01",
  "kind": "worksheet",
  "mode": "generate",
  "title": "Letölthető „Peulabemutató-vázlat” kitölthető sablon (doc)",
  "purpose": "Az M4.4 peulabemutató-vázlat (LMS-M4-05) fájl-alapú leadási útja: a „Beadás módja” szerinti „1 oldalas doc / pdf, a letölthető sablon alapján”. A két út egyenértékű (Program terv §5; hozzáférhetőségi sztenderd §4).",
  "spec": "1 oldalas kitölthető sablon doc formátumban, kizárólag az Assignment „Leírás (tanulónak)” 5 kérdéses szerkezetével, szó szerint: „1. Kihez beszélsz? (kvuca / korosztály, 1 mondat)”, „2. Miről szól a peula? (1 mondat)”, „3. Miért fontos ez nekik? (1–2 mondat)”, „4. Mit fogtok csinálni? (1 mondat)”, „5. Mit szeretnél, hogy hazavigyenek? (1 mondat)”, mindegyik után kitöltési hellyel; a sablon elején szó szerint a leírás 🔒 „Biztonságos megosztás” bekezdése. Új mező, minta vagy útmutató szöveg nem kerül bele.",
  "provenance": "human",
  "technical": {
    "note": "Szerkeszthető dokumentum: Google Doc (csak szervezeti fiókban, korlátozott megosztással) és/vagy .docx; A4, 1 oldal, nyomtatható; magyar nyelv. Moodle-ben az Assignment „Additional files” mezőjébe kerül."
  },
  "a11y": {
    "note": "Valódi szöveges dokumentum (nem kép), címsorokkal és megjelölt kitöltési helyekkel, hogy képernyőolvasóval is használható és kitölthető legyen; a dokumentum nyelve magyarra állítva."
  },
  "derivatives": [
    "print-pdf"
  ],
  "production_rules": [
    "R5"
  ],
  "blockers": [],
  "notes": "A11Y-18 statikus előfeltétele (IMPL-18-1): az Assignment „Beadás módja” sorában hivatkozott letölthető sablon deklarálása; tartalma kizárólag a leírás meglévő szövegéből áll. A sablon letölthetőségét és akadálymentességét a renderen kell igazolni (release-evidence)."
}
-->
```

**B18-06** — `02 Tervezet/Modulok/M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md`, közvetlenül az `**Értékelés jellege:**` sor előtt:

```
<!-- @asset
{
  "id": "M7.4-MUNK-01",
  "kind": "worksheet",
  "mode": "generate",
  "title": "Letölthető „Peula v1 – első vázlat” kitölthető sablon (doc)",
  "purpose": "A Peula v1 (LMS-M7-05) fájl-alapú leadási útja: aki nem online szövegként ad le, ennek kitöltésével és feltöltésével adja le a v1-et. A két út egyenértékű (Program terv §5; hozzáférhetőségi sztenderd §4).",
  "spec": "Kitölthető sablon doc formátumban, kizárólag az Assignment „Minimum elvárás” 1–4. pontjával, szó szerint: 1. „Kvuca-meta” (a pont adatkímélő mondatával és három alpontjával); 2. „SMART nevelési cél (max. 1–2 mondatban)”; 3. „Legalább 3–4 Peula-terület rövidebb kidolgozása (összesen kb. 10–20 sor)” a két alpontjával; 4. „Zmán Kvucá-operációs mini-táblázat (min. 3–4 sor)” a forrás oszlopfejléceivel („Idő (kb.)”, „Mi történik?”, „Ki felel érte?”) és 4 üres sorral, utána szó szerint a „(A neveknél most elég annyi …)” mondat és az 1:1 helyzetekről szóló dőlt bekezdés; a sablon végén szó szerint a ⚠️ adatkímélő mondat. A forrás táblázatának példasorai nem kerülnek bele. Új mező, minta vagy útmutató szöveg nem kerül bele.",
  "provenance": "human",
  "technical": {
    "note": "Szerkeszthető dokumentum: Google Doc (csak szervezeti fiókban, korlátozott megosztással) és/vagy .docx; A4 nyomtatható elrendezés is; magyar nyelv. Moodle-ben az Assignment „Additional files” mezőjébe kerül."
  },
  "a11y": {
    "note": "Valódi szöveges dokumentum (nem kép) és valódi táblázat-struktúra megjelölt oszlopfejlécekkel és kitölthető cellákkal, hogy képernyőolvasóval is használható és kitölthető legyen; a dokumentum nyelve magyarra állítva."
  },
  "derivatives": [
    "print-pdf"
  ],
  "production_rules": [
    "R5"
  ],
  "blockers": [],
  "notes": "A11Y-18 statikus előfeltétele (IMPL-18-1): a Program terv §5 beadási szabálya szerinti letölthető sablon a Peula v1-hez; tartalma kizárólag a „Minimum elvárás” meglévő szövegéből áll. A Peula v2 sablonja nem ez az asset: annak mezőlistája emberi döntés (IMPL-18-1, M7 v2). A sablon letölthetőségét és akadálymentességét a renderen kell igazolni (release-evidence)."
}
-->
```

### IMPL-18-2 (RÉSZBEN) — a beadási mód ellentmondása az M1-ben és az M3-ban

- **ID:** IMPL-18-2 (P1, objektív a szűkített részben, RÉSZBEN)
- **Probléma:** az ASSIGN-S/ASSIGN-M profil (manifest §1 :19–20) és a Program terv :279 az online text **és** a fájlút egyenértékű megnyitását írja elő; az M1-ben a fájlút csak opcionális, az M3.4-EGY-07 pedig csak szöveges beadást rögzít.
- **Bizonyíték:** M1.4 :518 „* File submissions: opcionálisan engedélyezhető (ha doc-ban írnak).”; M1 KAPU :297 „Online text submission ✅ (File submission opcionális).”; M3.4 :703 „…sablon, szöveges beadás;”. Az M6 és az M7 része ELVETVE: ott a lecke hallgat, a profil irányadó (az M6.B :31 kifejezetten egyenértékű utat ír).
- **Tilos:** próbálkozások, „Require students to click the submit button”, completion, rubrika, BSPEC-07.

**B18-07** — `02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md`

Régi:
```text
  * File submissions: opcionálisan engedélyezhető (ha doc-ban írnak).
```
Új:
```text
  * File submissions: ✅ (a kitöltött M1.4-MUNK-01 sablon feltöltéséhez; a két út egyenértékű, Program terv §5)
```

**B18-08** — `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md`

Régi:
```text
Online text submission ✅ (File submission opcionális).
```
Új:
```text
Online text submission ✅ + File submission ✅ (a két út egyenértékű, Program terv §5).
```

**B18-09** — M3.4 (M3.4-EGY-07 `technical`)

Régi:
```text
Moodle Assignment, magyar feladatleírás + sablon, szöveges beadás;
```
Új:
```text
Moodle Assignment, magyar feladatleírás + sablon; beadás: Online text ON és File submissions ON (a kitöltött M3.4-MUNK-01 sablon feltöltéséhez; a két út egyenértékű, Program terv §5);
```

---

## Nem alkalmazandó — a riportba kerül

### Emberi döntés

- **IMPL-15-3** (P2, emberi-döntés): a Drag & Drop mint második forma maradhat-e az M3.1-ben, az M3.2-ben és az M3.4-ben a fejlesztői megjegyzésben rögzített indoklással, vagy mindháromból kikerül. Bizonyíték: sztenderd :33 „Ha valahol mégis Drag & Drop kell, azt a lecke fejlesztői megjegyzésében indokolni kell” · M0.2 :251 · M3.2 :599 „mellette Drag & Drop” (indoklás nélkül). Indoklást a javító nem írhat (kitalált racionalizálás), a törlés tartalomvesztés. Döntő szerep: az M3 modulgazdája. A döntésig a Drag & Drop második formaként marad.
- **IMPL-18-4** (P2, emberi-döntés): a Z.4-nél a Program terv :279 „online-text ON + letölthető sablon” szabálya teljesül-e a Moodle-on belüli szövegsablonnal és az online texttel, vagy kell letölthető ív is a videós úttal közös fájlhelyen. Bizonyíték: Program terv :279 ↔ Z.4 :336 „File submissions: **ON**, max 1 file … (opcionális videós út)”. A HUM-PRIV-02-t érinti. Döntő szerep: projektgazda / hozzáférhetőségi gazda.
- **IMPL-18-1, M7 v2 része** (emberi-döntés): a Peula v2 sablonjának mezőlistája nem vezethető le egyértelműen (M7 hub :356–357 „Peula v2 sablon … 11 pont” + Zmán Kvucá-checklist ↔ M7 KAPU :252 operációs táblázat, AI-sor, kötelezettségvállalás). Döntő szerep: projektgazda / értékelési felelős.

### Bizonyíték-kapu (nem repo-fix, nem megy /course-fix-be)

- **IMPL-15-4** (P1): renderen igazolandó, hogy a választott típus húzás nélkül, egy koppintással és billentyűzettel teljesíthető (célméret mobil portrait nézetben), a válaszonkénti visszajelzés megjelenik és továbblépés előtt elolvasható, a húzásmentes út egyedül is completiont ad, és a renderelt M3.1/M3.2/M3.4 ugyanazt az alapértelmezett típust mutatja. Runtime acceptance 9., 13., 14. pont; RT-P0-13, RT-P0-14; RELEASE-READINESS G5b, G3b. A sztenderd :128 tétele nyitva marad. Nyitott render-kérdés: hány Multiple Choice elem fér egy diára mobilon; ha a SLIDE 4-et bontani kellene, az a „7 slide” számot érintené, ezt nem statikusan kell eldönteni.
- **IMPL-18-5** (P2): a beadási típusok visszaolvasása, a sablonfájlok tényleges letölthetősége és akadálymentessége (táblázat-fejlécek, címkézett mezők, magyar dokumentumnyelv, mobilon kitölthető), a független pre-flight szerepköri bizonyítéka. RELEASE-READINESS G5b, G3b. A sztenderd :132 tétele nyitva marad.

### Elvetve

- **IMPL-18-3** (javasolt új RT-P0-25 pont és §6-os visszaolvasási lépés): nincs kánoni szabály, amely minden release-evidence tételhez külön RT-pontot írna elő; a bizonyíték hordozója a sztenderd :132 tétele (IMPL-18-5). A verifier szerint a build-verdiktet egyébként sem érintené (`tools/content_integrity.py` :820–821, :848–850).

### Hatókörön kívül (nem validált, nem javítandó ebben a körben)

- Drag & Drop az M0.2, M0.3, M1 hub, M1.2, M4.2, M4.3, M7.2 és M7.3 fájlban is szerepel; az R-13 csak az M3-at érintette.
- A Single Choice Set más leckékben is szerepel; hogy ott is kérdés- vagy válaszszintű visszajelzést várnak-e tőle, nem vizsgáltuk.
- M3.4-EGY-05: a `spec` (:619) Single Choice Set-et, a `technical` (:623) Multiple Choice-t ír.

---

## Zárás (a /course-fix futás végén)

1. A teljes `git diff` visszaolvasása.
2. `python3 tools/media_manifest.py build` kétszer, önállóan (stabil-e), majd `check` és `reconcile`.
3. `python3 tools/content_integrity.py`, `--selftest` és `--release-report`: 0 ERROR; a `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD` sor változatlan; új `MEDIA-REQUIRED-*` sor nincs. Ha bármelyik nem teljesül: megállás a pontos kimenettel.
4. Egyetlen `python3 tools/test_media_manifest.py --pin-visible "A11Y-15 (IMPL-15-1, IMPL-15-2), A11Y-18 (IMPL-18-1, IMPL-18-2): …"`, önállóan.
5. `python3 -m unittest tools.test_media_manifest`, `py_compile`, `git diff --check` (a PR-tartományra is).
6. Célzott újraellenőrzés a diff-hunkokra (implementáció + nyelv).
7. `/release-check`, utolsóként.
