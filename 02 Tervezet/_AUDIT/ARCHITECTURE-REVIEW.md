# Architektúra-review — döntést igénylő deep-audit tételek

> Ez a dokumentum a tananyag **architektúra-szintű** (kapu-építhetőség, cél↔item
> illeszkedés, curriculum-ív / kompetencia-lefedettség, akadálymentesség, adatvédelem)
> deep-audit találatait gyűjti, amelyek **emberi DÖNTÉST igényelnek** — nem auto-javíthatók,
> mert pedagógiai ív-, kapu-filozófiai, jogi/korhatár- vagy dizájn-döntést hordoznak.
>
> A tananyag-forrásfájlokat **szándékosan nem módosítjuk** ezekből a tételekből; az alábbiak
> döntés-előkészítésnek készültek, hely- és forrásmegjelöléssel. Az auto-javítható
> (tisztán szerkesztési) találatok máshol kerülnek alkalmazásra.
>
> **Dimenzió-kódok** (lásd `DEEP-AUDIT-RUBRIC.md`):
> - **D3** — kapu-érvényesség (D3.1 cél↔item illeszkedés; D3.8 build-ready küszöb + remediáció)
> - **D4** — curriculum-ív / kompetencia-lefedettség (tanítva vs. mérve)
> - **D5** — akadálymentesség (WCAG / OSCQR)
> - **D8** — adatvédelem / GDPR (D8.1 minimalizálás; D8.2 korhatár/hozzájárulás; D8.3 tájékoztatás; D8.4 megőrzés/törlés)

---

## Deep-audit kör 1

### 1. [D3.8] M0 belépő-quiz mint kapu nem build-ready (küszöb + remediáció)

- **Dimenzió:** D3.8 — kapu-érvényesség: indokolt küszöb + remediáció (kritikus kritérium)
- **Fájl / hely:** `02 Tervezet/MODULOK/M0/M0 – „Kickoff, keret, technika”.md`
  → 5. Kapuk (123–151. sor): „M0 belépő-quiz”; „ajánlott minimum: 60–70%” (138.);
  „eredménytől függetlenül, de cél, hogy a többség 60%+” (144.)
- **Probléma:** Az M0 belépő-quiz mint kapu nincs build-ready:
  - (a) nincs authored item-készlet, csak témalista (6–8 kérdés témái); nincs answer key, nincs rubrika;
  - (b) a cut-score nem kritérium-referenciás indoklású, hanem kerek szám-tartomány
    („60–70%”, „ajánlott”), ráadásul ellentmondásos, mert a completion „eredménytől
    függetlenül” számít — azaz a kapu nem is gate, hanem completion-tracker.

  Ez a D3.8 kritikus kritériumot bukja (indokolt küszöb + remediáció).
  **Pozitívum:** a remediációs / korrektív hurok jól leírt (személyes emlékeztető,
  tech helpdesk, nincs kizárás).
- **Javaslat (DÖNTÉS):** Dönteni kell:
  - ha az M0-quiz tényleg csak **puha completion-jelző**, akkor ne nevezzük „kapunak”
    küszöbbel;
  - ha **kapu**, akkor authored itemek + answer key + kritérium-referenciás
    (Angoff-jellegű) küszöbindoklás kell.

  Ez a quiz tényleges megírását és kapu-filozófiai döntést igényel.
- **Forrás:** —

---

### 2. [D3.1] M0 belépő-quiz: item↔cél illeszkedés nem ellenőrizhető (alulreprezentáció gyanúja)

- **Dimenzió:** D3.1 — cél↔item illeszkedés
- **Fájl / hely:** `02 Tervezet/MODULOK/M0/M0 – „Kickoff, keret, technika”.md`
  → 5. Kapuk, belépő-quiz témák (134–137.); kapcsolódó kompetenciák 2.1–2.5 (24–44.)
- **Probléma:** Item↔cél illeszkedés nem ellenőrizhető, mert nincsenek konkrét itemek,
  csak témák („madrich vs. nem terapeuta”, „jelzési út”, „puha vs. éles kapu”,
  „hol találom a modulokat”). A modul 5 kimeneti kompetenciájából a **„dugma ishit
  online” (kompetencia 5)** és az **„éves ív átlátása” (kompetencia 1)** nincs lefedve
  a quiz-témákban → cél↔item alulreprezentáció gyanúja, de item hiányában nem zárható le.
- **Javaslat (DÖNTÉS):** A quiz authoringakor **cél→item leképező tábla** készítendő, hogy
  minden mastery-kulcscélnak legyen itemje. Az authoring döntés, de a hiánylista
  (kompetencia 1 és 5) már most jelölhető.
- **Forrás:** —

---

### 3. [D8] Reflexiós / napló-elemek adatkezelési nyilatkozat nélkül (minimalizálás / tájékoztatás / megőrzés)

- **Dimenzió:** D8 — adatvédelem (D8.1 minimalizálás, D8.3 tájékoztatás, D8.4 megőrzés/törlés lefedetlen)
- **Fájl / hely:** program (M3 leckék)
  → M3.1 SLIDE 5; M3.2 SLIDE 7A; M3.3 SLIDE 6; M3.4 SLIDE 5 (reflexiós Essay / Short Answer
  mezők) + M3.F Study Lab jegyzetlap
- **Probléma:** D8.1 / D8.3 / D8.4 lefedetlen: a leckék több helyen kérnek érzelmileg
  érzékeny reflexiót (red flag, önsértés, „mikor kérnél segítséget”, saját Do/Don't lista),
  de **SEHOL nincs** adatminimalizálási nyilatkozat, plain-language tájékoztató (milyen adat,
  mire, meddig, kihez fordulhat), megőrzési idő vagy törlési folyamat. A 15+ célcsoportnál
  ez érzékeny személyes adat. M3.4 SLIDE 5 csak annyit ír: „Szervezettől függően dönthető el,
  hogy látja-e a mentor” — ez nem elég.
- **Javaslat (DÖNTÉS):** Minden reflexiós / napló-elemhez beépíteni egy rövid, gyermek-nyelvű
  adatkezelési megjegyzést (mit gyűjtünk, miért, meddig, ki látja, hogyan kérhető törlés),
  és jelezni, hogy a kapu-funkcióhoz **nem szükséges érzékeny tartalmat tárolni**.
  Sablon auto-javasolható; a jogi / korhatár-döntés review.
- **Forrás:** —

---

### 4. [D8] 15+ célcsoport — korhatár / 16 alatti szülői hozzájárulás nem kezelve (GDPR Art.8)

- **Dimenzió:** D8 — adatvédelem (D8.2 korhatár / hozzájárulás lefedetlen)
- **Fájl / hely:** program
  → M3 modul-áttekintő 6. Kapuk + „M3 – KAPU” `0. A kapu adatai` tábla
- **Probléma:** D8.2 lefedetlen: a 15+ célcsoport épp a **GDPR Art.8 / ICO korhatár-vonalán**
  van (16 alatt szülői / gondviselői hozzájárulás a reflexiós / kvíz-adatokra). A modul sehol
  nem jelzi a minimum korhatárt vagy a 16 alatti szülői hozzájárulás kezelését a Moodle / H5P
  naplózott adatokra és a kapu-haladási adatra.
- **Javaslat (DÖNTÉS):** A KAPU `0. adatai` táblába és a modul-áttekintőbe felvenni egy
  adatvédelmi sort: korhatár-kezelés, 16 alatt szülői hozzájárulás a naplózott / mastery-adatokra,
  megőrzési idő. Jogi pontosítás review.
- **Forrás:** —

---

### 5. [D5] M4.1 nonverbális tartalom kizárólag vizuális csatornán — szöveges ekvivalens hiányzik (WCAG 1.1.1 / 1.2.2)

- **Dimenzió:** D5 — akadálymentesség
- **Fájl / hely:** `02 Tervezet/MODULOK/M4/M4_ONLINE_LECKE/M4.1 – Mit üzen a testem_ – Nonverbális kiállás.md`
  → SLIDE 1 AI beszélő fej videó (59. sor); SLIDE 3 Interactive Video (166–256. sor);
  SLIDE 4 képpárok (266–319. sor)
- **Probléma:** A lecke videó- és képalapú (3 mini-jelenet, freeze-frame képpárok, AI beszélő
  fej), és a tanulási cél jelentős részben **vizuális megfigyelésre** épül (nonverbális jelek
  leolvasása). A SLIDE 1-nél szerepel „felirattal”, de a SLIDE 3 Interactive Video jeleneteinél
  és a képpároknál **NINCS** explicit felirat / alt-szöveg követelmény. A vakfolt: aki nem látja
  a testtartást, a feladat magját (vizuális megfigyelés) nem tudja teljesíteni — nincs szöveges
  ekvivalens a kulcs-vizuális tartalomhoz (WCAG 1.1.1 / 1.2.2).
- **Javaslat (DÖNTÉS):** Eszkalálandó dizájn-döntés: a kép / videó-magú nonverbális tartalomhoz
  adj **szöveges ekvivalenst** (a narráció írja le a látott testtartást: „a válla előreesik, a
  tekintete lefelé”), minden Interactive Video jelenethez magyar felirat, minden tartalmi
  képpárhoz alt-szöveg. Dönteni kell, mennyire alapozható a kapus completion kizárólag vizuális
  csatornára.
- **Forrás:**
  - https://www.w3.org/TR/WCAG22/
  - https://oscqr.suny.edu/standard35/

---

### 6. [D4] Életkori / fejlődéslélektani alapismeret nem tanítva, de M6 / M7 méri (unsupported competency)

- **Dimenzió:** D4 — curriculum-ív / kompetencia-lefedettség
- **Fájl / hely:** `02 Tervezet/_AUDIT/CURRICULUM-IV.md` kompetencia-térkép sora
  „Korosztályi / fejlődéslélektani alapismeret (6–10/11–13/14–16/16+)” — Tanítva: üres; Mérve: M6
  → ill. M6 §2.1 / M7 KAPU R2 (224. sor) „Gen Alpha / életkori sajátosság megjelenik a tervben”
- **Probléma:** Az életkori / fejlődéslélektani alapismeret (6–10/11–13/14–16/16+) sehol nincs
  **ÖNÁLLÓAN TANÍTVA**, de az M6 mérőeszköz (eszköz–kvuca illesztés a 4 korosztályra) és az M7
  capstone-rubrika (R2 kvuca-illeszkedés) is **FELTÉTELEZI ill. MÉRI**. Az M3.2 a someres
  kvuca-archetípusokat (Parparim / Kivsza / Leviatan / Zorea) tanítja, ami **NEM** életkori
  fejlődéslélektan — maga az M6 §6 „Feltételez” blokkja is „a 4 kvuca jellemzői csak röviden
  ismételve, nem tanítva”-ként jelöli. A curriculum így nem-tanított tudásra mér
  (unsupported competency).
- **Javaslat (DÖNTÉS):** Vagy az M3 korosztály-mátrix produktumába emelj be expliciten életkori
  sávokat + fejlődési jellemzőket (6–10/11–13/14–16/16+ → someres profilokhoz kötve), vagy tegyél
  az M6 elejére egy rövid korosztály-tanító leckét. A megoldás **curriculum-ív DÖNTÉS**
  (új tanító elem vagy meglévő modul bővítése), ezért nem auto-javítható.
- **Forrás:**
  - `02 Tervezet/MODULOK/M6/M6 – „Toolbox_ játék, történet, kézműves & inkluzivitás”.md` §2.1 + §6 Feltételez
  - `02 Tervezet/MODULOK/M7/M7 – KAPU – értékelő (item-bank + rubrika).md` R2 (224. sor)
  - `02 Tervezet/_AUDIT/CURRICULUM-IV.md` 17–18., 81. sor

---

### 7. [D4] Peula 4-fázisú dramaturgiát M7 méri, de korábban egy modul sem tanítja explicit

- **Dimenzió:** D4 — curriculum-ív / kompetencia-lefedettség
- **Fájl / hely:** `02 Tervezet/MODULOK/M7/M7 – KAPU – értékelő (item-bank + rubrika).md`
  → R3 – Peula 11 pont struktúra rubrikasor (234. sor): „…a 3–4 részletezett pont között ott a
  bevezetés–élmény–feldolgozás–zárás ív”; valamint a CURRICULUM-IV kompetencia-térkép
  „Peula-felépítés (bevezetés–élmény–feldolgozás–zárás, 4 fázis)” sora: Tanítva üres, Mérve M7
- **Probléma:** A peula 4-fázisú dramaturgiáját (bevezetés–élmény–feldolgozás–zárás) az M7
  capstone-rubrika **MÉRI** (R3), de korábban egyetlen modul sem tanítja explicit a
  fázis-szerkezetet: az M4 pitch 5-kérdéses (nem fázis-szerkezet), az M5 tervezési táblázat, az
  M6 egyetlen játéklap. A grep szerint a „4 fázis” kifejezés csak az M7.2 / M7.4 leckékben és az
  M7 KAPU-ban jelenik meg — vagyis az M7 a saját tanítása keretében vezeti be **ÉS** méri,
  korábbi alapozás nélkül. Az M7 KAPU §0 „Feltételez” továbbra is hivatkozik „alap peula-fogalom
  és -felépítés (korábbi programírás-alap)”-ra, ami a curriculumban nem létezik.
- **Javaslat (DÖNTÉS):** Vagy M5 / M6-ba építs be egy minimál peula-dramaturgia (4 fázis) tanító
  elemet, amire az M7 Peula 11 pontja épülhet; vagy explicit mondd ki az M7.2-ben, hogy a 4 fázis
  itt kerül **először** bevezetésre, és töröld a nem létező „korábbi programírás-alap”
  feltételezést. **Ívtervezési DÖNTÉS.**
- **Forrás:**
  - `02 Tervezet/MODULOK/M7/M7 – KAPU – értékelő (item-bank + rubrika).md` R3 (234. sor)
  - `02 Tervezet/_AUDIT/CURRICULUM-IV.md` 21–22., 80. sor
  - grep: „4 fázis / bevezetés–élmény–feldolgozás–zárás” csak M7

---

### 8. [D4] Tuckman-szakaszok árva kompetencia — M3-ban tanítva, sehol nem mérve / újrahasznosítva

- **Dimenzió:** D4 — curriculum-ív / kompetencia-lefedettség (D2.3 lefedetlen: nincs értékelés vagy újrahasznosítás)
- **Fájl / hely:** `02 Tervezet/MODULOK/M3/M3 – „Kvuca, red flag, felelősség” – Csoportdinamika, korosztályok és gyerekvédelem .md`
  → §2 Kimeneti kompetenciák 1. (Tuckman, 24–26. sor) + §6 Kapuk (215–218. sor: szcenárió-kvíz a
  gyerekvédelem / red flag témára)
- **Probléma:** A Tuckman-szakaszok (forming–storming–norming–performing) az M3 explicit tanított
  és kimeneti kompetenciája, de
  - (a) a leírt M3-kapu kvíz a **gyerekvédelem / red flag** konstruktumra fókuszál és a
    Tuckman-felismerést nem méri explicit, és
  - (b) egyetlen későbbi modul sem erősíti / alkalmazza újra a Tuckman-modellt (a 4 kvuca-profil
    részben tovább él M7 / Z-ben, a Tuckman nem).

  Árva kompetencia (D2.3 lefedetlen / nincs értékelés vagy újrahasznosítás).
- **Javaslat (DÖNTÉS):** Vagy az M3-kapuba építsd be a Tuckman-felismerést mérő itemet, vagy az
  M7 kvuca-illeszkedés rubrikasorban kérd, hogy a peula vegye figyelembe a kvuca fejlődési
  szakaszát (Tuckman) — így a Tuckman-tanítás hasznosul. **Kapu / rubrika-bővítési döntést** igényel.
- **Forrás:**
  - `02 Tervezet/MODULOK/M3/…Csoportdinamika….md` §2.1 + §6
  - `02 Tervezet/_AUDIT/CURRICULUM-IV.md` 25–26., 58. sor
