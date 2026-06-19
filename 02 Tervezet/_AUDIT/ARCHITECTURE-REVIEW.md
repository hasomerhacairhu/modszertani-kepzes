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

---

## Deep-audit kör 2

> Második deep-audit kör (kelt: 2026-06-19). Az alábbi tételek szintén **emberi
> DÖNTÉST igényelnek** — tananyag-forrás nem módosul, csak ez a döksi.
> Hozzáadott dimenzió-kódok ehhez a körhöz:
> - **D3.1** — item↔cél illeszkedés (konstruktum-lefedettség, nem-túlreprezentáció)
> - **D3.2** — egy védhető helyes válasz / kulcs egyértelműsége
> - **D3.8** — build-ready küszöb + remediáció + determinisztikus kapu-logika

### 1. [D3.1] M0 belépő-quiz: itemek ténylegesen nincsenek megírva — a kapu nem build-ready, item↔cél nem ellenőrizhető

- **Dimenzió:** D3.1 — item↔cél illeszkedés (kihat D3.2-re és D3.8-ra is)
- **Fájl / hely:** `02 Tervezet/MODULOK/M0/M0 – „Kickoff, keret, technika”.md`
  → 5. Kapuk → „Moodle Quiz – M0 belépő-quiz” (132–138. sor). A kvízt az
  **M0.3 SLIDE 6** és az **M0 overview** is hivatkozza mint éles, kapus mérőeszközt.
- **Probléma:** Az M0 belépő-quiz (a modul completion **egyik feltétele**) sehol nincs
  ténylegesen kidolgozva: csak témamegjelölés van („madrich vs. terapeuta”, „jelzési
  út”, „puha vs. éles kapu”, „hol találom a modulokat”) és „6–8 egyszerű kérdés
  (true/false + feleletválasztás)”. **Nincsenek megírt itemek**, nincs dokumentált
  helyes-válasz kulcs, nincs cél→item leképezés. Így a **D3.1** (item↔cél illeszkedés),
  a **D3.2** (egy védhető helyes válasz) és a **D3.8** (explicit cut-score indoklás)
  sem ellenőrizhető. A „ajánlott minimum 60–70%” küszöb **kerek szám**,
  kritérium-referenciás indoklás nélkül. Az éles kapus mérőeszköz **nem build-ready**.
- **Javaslat (DÖNTÉS):** A belépő-quiz itemeit ténylegesen meg kell írni (lead-in,
  opciók, kulcs, distraktor-logika), **minden mastery-kulcscélhoz legalább 1 item**,
  NBME-flaw-mentesen, dokumentált helyes-válasz kulccsal és kritérium-referenciás
  cut-score-indoklással. Ez tananyag-szerzői / architekturális munka, **nem
  biztonságos auto-edit**.
- **Forrás:**
  - assessment-validity (construct validity, Angoff cut-score)

> **Megj.:** Ez a tétel részben átfed a kör 1 / 1–2. tételeivel (M0-quiz nem
> build-ready, item↔cél nem ellenőrizhető), de **élesíti** azt: itt a kifejezett
> elvárás az itemek tényleges megírása answer-key-vel, cél→item leképezéssel és
> kritérium-referenciás cut-score-ral. A két kör együtt olvasandó.

---

### 2. [D4] CURRICULUM-IV.md (és párhuzamosan a GAP-MAP.md) érdemben ELAVULT — aktívan félrevezet a hatókör-feltérképezésben

- **Dimenzió:** D4 — curriculum-ív / kompetencia-lefedettség (audit-riport karbantartás)
- **Fájl / hely:** `02 Tervezet/_AUDIT/CURRICULUM-IV.md` — teljes fájl; kiemelten:
  - fejléc „Koherencia-találatok: 🔴 3 · 🟡 7”;
  - 17–18. sor (🔴 unsupported korosztály), 21–22. sor (🟡 unsupported 4-fázis),
    23–24. sor (🔴 orphan M2-identitás), 31–34. sor (🔴 capstone-gap + 🟡 horgonyzás);
  - Kompetencia-térkép 80–82. sor (Tanítva-oszlop üres: peula-4-fázis, korosztály, Gen Alpha)
- **Probléma:** A program-szintű koherencia-audit (`CURRICULUM-IV.md`) **érdemben
  elavult** a tényleges modulfájlokhoz képest, és ezért **aktívan félrevezet**. A git
  history igazolja: az audit-riportot az `e61cee4 docs(audit)` commit hozta létre, majd
  a **későbbi** `6f3c82b fix(curriculum): koherencia-szakadások — korosztály-tanítás,
  portfólió-átkötések, capstone` commit a benne diagnosztizált hibákat a tényleges
  modulokban javította, **de a riportot senki nem frissítette**. A riportban még
  🔴/🟡-ként szereplő alábbi hibák a valós fájlokban **MÁR MEG VANNAK OLDVA:**
  - (a) a korosztályi / fejlődéslélektani alapismeret most **explicit TANÍTVA** —
    **M3.2 SLIDE 5B** „Korosztály → fejlődés → madrich-implikáció” referencia-táblázat a
    6–10 / 11–13 / 14–16 / 16+ sávokat fejlődési jellemzőkhöz köti és előrekapcsol M6-ra;
  - (b) a peula 4-fázisú dramaturgiát az **M7.2** lecke már explicit tanítja, mielőtt az
    M7 KAPU mérné;
  - (c) a „Gen Alpha” rubrikasor az **M7 KAPU**-ból eltűnt, helyette „az M3-ban tanult
    kvuca-profil mentén” életkori sajátosság;
  - (d) a portfólió-átkötések (M1/M2/M3/M5/M6 → M7 Peula v2) megvannak az **M7
    áttekintő §PORTFÓLIÓ-BEMENET** és az **M7 KAPU §CAPSTONE** tábláiban, és egyeznek;
  - (e) a capstone-leadás **horgonyzva van** („NEM csúszik a modulon kívülre, a Z nem
    helyettesíti”) — miközben a `CURRICULUM-IV` 33. és 137. sora **MÉG** a „modulon
    KÍVÜLi, későbbi végleges verzió Workshop”-ot írja le.

  Egy stábtag, aki ezt az audit-anyagot olvassa a hatókör feltérképezéséhez, **hamis
  hibalistát és hamis kompetencia-térképet kap**.
- **Javaslat (DÖNTÉS):** Futtasd újra a program-szintű koherencia-auditot a **jelenlegi**
  modulfájlokon; **vagy** láss el a `CURRICULUM-IV.md` (és a párhuzamosan elavult
  `GAP-MAP.md`) tetejére egy explicit **verzió- / dátum- / commit-bélyeget +
  figyelmeztetést**, hogy a `6f3c82b` előtti állapotot tükrözi. Minimum a már lezárt
  🔴/🟡 tételeket (korosztály-tanítás, 4-fázis, Gen Alpha, M2-orphan, capstone-átkötés,
  horgonyzás) jelöld **RESOLVED**-ként, hogy ne kerüljenek újra javítási sorba. **Nem
  egyszerű szövegcsere:** a kompetencia-térkép Tanítva / Erősítve / Mérve oszlopait újra
  kell vezetni.
- **Forrás:**
  - git log: `e61cee4 docs(audit)` → `6f3c82b fix(curriculum)`
  - M3.2 SLIDE 5B referencia-táblázat (235–254. sor)
  - M7.2 lecke 4-fázis (288 / 315. sor)
  - M7 KAPU CAPSTONE-tábla (323–335. sor)

> **Megj.:** Ez a tétel **felülírja** a kör 1 / 6. és 7. tételének súlyozását: az ott
> „unsupported competency”-ként jelölt korosztály- és 4-fázis-hiányok a **mai
> modulfájlokban már tanítva vannak** (M3.2 SLIDE 5B, ill. M7.2). A kör 1 / 6–7.
> találat a `CURRICULUM-IV.md` elavult állapotán alapult; a tényleges javítási feladat
> elsősorban az **audit-riport szinkronizálása**, nem új tanító elem beépítése.

---

### 3. [D3.8] M3 gate — a „kötelező kritikus item (2,4,7,9)” szabály nincs determinisztikusan implementálva

- **Dimenzió:** D3.8 — build-ready küszöb + determinisztikus kapu-logika (biztonságkritikus)
- **Fájl / hely:** `02 Tervezet/MODULOK/M3/M3 – KAPU – értékelő (item-bank + rubrika).md`
  → 1.2 Pontozás és küszöb, 57. sor
- **Probléma:** A **biztonságkritikus** M3 gate „kötelező kritikus item (2,4,7,9)”
  szabálya nincs determinisztikusan implementálva. A fájl maga elismeri, hogy a Moodle
  natívan **nem tud item-szintű pass-feltételt**, és három, **nem ekvivalens**
  alternatívát kínál (kritikus itemek súlyozása 2 pontra + arányos küszöbemelés VAGY
  mentori utóellenőrzés), a döntést a stábra hagyva. A súlyozott megoldás
  **matematikailag nem zárja ki**, hogy valaki egy kritikus itemet elvétve mégis elérje
  a küszöböt (a hiányzó kritikus pont **kompenzálható** nem-kritikus itemekkel), tehát a
  „tévesztése akkor is bukás” ígéret **nem garantált**. Gyerekvédelmi kapunál a
  kritikus-item-szabály érvényesítése **nem maradhat** „a stáb döntése, dokumentáld”
  szinten.
- **Javaslat (DÖNTÉS):** Determinisztikus implementáció kell: vagy a 4 kritikus itemet
  külön **„all-or-nothing” Quiz-szekcióba** szervezni (kötelező 4/4 + külön ≥80% a
  többire), vagy a Moodle gradebook „conditional” / locked-feltételével, vagy **explicit
  kötelező mentori review-checklisttel minden átmenőnél**, amíg a tényleges
  LMS-konfiguráció nem garantálja. Az architektúrát a **gyerekvédelmi felelőssel együtt**
  kell véglegesíteni.
- **Forrás:**
  - https://learning.nspcc.org.uk/child-abuse-and-neglect/recognising-and-responding-to-abuse

---

### 4. [D3.2] M3 gate — ITEM 2 (kritikus) és ITEM 8 ugyanazt a titoktartás-konstruktumot duplikálja

- **Dimenzió:** D3.2 — egy védhető helyes válasz / konstruktum-lefedettség (kihat D3.1-re)
- **Fájl / hely:** `02 Tervezet/MODULOK/M3/M3 – KAPU – értékelő (item-bank + rubrika).md`
  → ITEM 2 (~79–93. sor) és ITEM 8 (~187–201. sor); lefedettség-tábla 1.1 (mindkettő a
  „titoktartás” célhoz kötve)
- **Probléma:** Az **ITEM 2 (KRITIKUS)** és az **ITEM 8** lényegében ugyanazt a
  konstruktumot méri ugyanazzal a helyes-válasz mintával („nem ígérek titkot + elmondom
  kinek-miért + nem hagylak egyedül”), sőt a tanulói feedbackjük is csaknem azonos. Az
  **1.1 tábla** is mindkettőt a „Nincs 100% titoktartás” sorhoz rendeli. Ez
  **konstruktum-túlreprezentáció (D3.1)** és gyengíti a 12-itemes lefedettség valódi
  szélességét: két item egy fogalmat duplikál, miközben a kötelező kritikus itemek
  (2/4/7/9) súlya így a titoktartásra billen. **Nem** két egyformán védhető OPCIÓ egy
  itemen belül, **hanem két item redundanciája** — de a kapu validitását érinti.
- **Javaslat (DÖNTÉS):** Az item-bank felülvizsgálata: vagy **ITEM 8-at élesítsd egy
  MÁS, jelenleg alulreprezentált célra** (pl. adatkezelés / megosztás-korlát „csak a
  felelősnek, nem mindenkinek” önállóan), vagy **vond össze és helyettesítsd egy új
  construct-tal**, hogy a 12 item ne duplikálja a titoktartás-konstruktumot. Mivel a
  kapu-szerkezetet és a kritikus-item készletet érinti, **strukturális review**.
- **Forrás:** —

---

### 5. [D3.8] M3 gate — a kritikus-item kapuzás súlyozásos fallback-je nem garantálja a „minden kritikus item helyes” feltételt

- **Dimenzió:** D3.8 — cut-score / megkülönböztető-szint validitása (biztonságkritikus)
- **Fájl / hely:** `02 Tervezet/MODULOK/M3/M3 – KAPU – értékelő (item-bank + rubrika).md`
  → 1.2 pontozás (~57. sor) — „ha a Moodle nem tud item-szintű feltételt, a kritikus
  itemek súlyozhatók 2 pontra és a küszöb arányosan emelhető – a stáb döntése”;
  0. tábla „Kötelező kritikus itemek”
- **Probléma:** A kapu **legbiztonságkritikusabb** logikája — a 4 kötelező kritikus item
  (2,4,7,9) tévesztése akkor is bukás, ha az összpont ≥80% — **nincs garantáltan
  implementálva**: a fájl maga ismeri el, hogy ha a Moodle nem tud item-szintű
  feltételt, akkor a súlyozás „a stáb döntése”. A javasolt fallback (kritikus item 2
  pontra súlyozása) **nem ekvivalens** a „minden kritikus item helyes” feltétellel: egy
  2-pontos kritikus item elbukása az **emelt küszöbnél is kompenzálható** lehet más
  itemekkel, így egy kritikus biztonsági állítás tévesztése **átcsúszhat**. Egy
  biztonságkritikus mastery-kapunál ez a **cut-score / megkülönböztető-szint validitását
  (D3.8)** érinti.
- **Javaslat (DÖNTÉS):** Rögzítsd egyértelműen, melyik LMS-mechanizmus biztosítja az
  item-szintű kötelező feltételt (pl. külön H5P / Moodle feltételes elérés, vagy mentori
  utóellenőrzés **mint kötelező lépés, nem opció**), és **töröld vagy korlátozd a
  súlyozásos fallback-et**, mert nem garantálja a kritikus-item kapuzást. **Strukturális
  / assessment-architektúra döntés.**
- **Forrás:** —

> **Megj.:** A 3. és az 5. tétel ugyanarra a sorra (1.2 pontozás, ~57. sor) mutat, de
> **eltérő dimenzióból**: a 3. a *determinisztikus implementáció* hiányát (D3.8 —
> kapu-logika), az 5. a *súlyozásos fallback érvénytelenségét* (D3.8 — cut-score
> validitás) emeli ki. Együtt kezelendők egyetlen LMS-architektúra döntésben.

---

### Kör 2 — kiegészítő tételbatch (kelt: 2026-06-19)

> Az alábbi 10 tétel a kör 2 folytatása (6–15. sorszám), a már lezárt 1–5. tételek
> mellé. Mind **emberi DÖNTÉST igényel** (kapu-filozófia, cél↔item átfogalmazás,
> curriculum-ív, produktumlánc-horgonyzás); **tananyag-forrást nem módosítunk**.
> Ehhez a batch-hez érintett dimenzió-kódok:
> - **D2** — constructive alignment (cél↔tanítás↔értékelés; tanítva vs. mérve)
> - **D3** (D3.1 item↔cél lefedettség/alulreprezentáció; D3.6 szcenárió-/SJT-item;
>   D3.7 kétképzős kalibráció; D3.8 indokolt cut-score + determinisztikus kapu-logika)
> - **D4** — produktumlánc / árva kompetencia

### 6. [D3] M0 belépő-quiz — a kimondott „60–70%” küszöb funkció nélküli (completion ≠ cut-score, belső ellentmondás)

- **Dimenzió:** D3 — kapu-érvényesség (D3.8: indokolt cut-score; belső konzisztencia)
- **Fájl / hely:** `02 Tervezet/MODULOK/M0/M0 – „Kickoff, keret, technika”.md`
  → 5. Kapuk (124–151. sor), különösen 138. sor („ajánlott minimum: 60–70%”) és
  143–144. sor (a complete-követelmény: quiz „kitöltve, eredménytől függetlenül”)
- **Probléma:** A mastery-kapu cut-score-ja nincs kritérium-referenciásan indokolva
  (D3.8). A belépő-quiznél „ajánlott minimum: 60–70%” (138.) szerepel mint **kerek
  tartomány, indoklás nélkül**, ráadásul a complete-követelmény szerint a quiz
  „kitöltve (eredménytől függetlenül)” elég (143–144.) — vagyis a kimondott küszöb
  **funkció nélküli**: nincs valódi, a tanuló számára a lecke elején kimondott,
  indokolt cut-score. **Belső ellentmondás:** vagy van küszöb (akkor indokolni ÉS
  érvényesíteni kell), vagy nincs (akkor ne nevezzünk meg számot). Soft gate
  belépő-modulnál ez védhető döntés lehet, de jelenleg indoklás nélküli.
- **Javaslat (DÖNTÉS):** Architektúra/értékelés-review döntse el, hogy az M0-quiz
  **tisztán diagnosztikus** (nincs cut-score, csak completion) vagy **valódi
  küszöbös**. Ha diagnosztikus: töröljék a „60–70%” számot, vagy jelöljék explicit
  **nem-kapuzónak**. Ha küszöb: adjanak kritérium-referenciás indoklást és
  remediációt. Ez a kapu-filozófia döntése.
- **Forrás:** —

> **Megj.:** Ez a tétel a kör 2 / 1. és a kör 1 / 1. M0-quiz tételekkel **átfed, de
> más metszetet** emel ki: itt nem az itemek hiánya, hanem a **completion ↔ kimondott
> küszöb belső ellentmondása** a döntési mag. Egy M0-kapu-filozófiai döntésben
> kezelendők együtt.

---

### 7. [D3] M6 KAPU — a modul-hub mennyiségi mastery-céljai (3 inkluzivitási szempont, 3–4 nyitott kérdés) alulreprezentáltak a kapuban

- **Dimenzió:** D3 — item↔cél lefedettség / mérési hiány (D3.1)
- **Fájl / hely:** `02 Tervezet/MODULOK/M6/M6 – KAPU – értékelő (item-bank + rubrika).md`
  → összevetés: modul-hub kompetencia 2 (sor 30) és 3 (sor 34) vs. KAPU R5 (sor 343),
  Oké-checklist (sor 353) és item-lefedettség tábla (sor 35–40)
- **Probléma:** A modul-hub kimeneti kompetenciái konkrét **mennyiségi célokat**
  ígérnek: »Legalább 3 inkluzivitási szempontot meg tud nevezni« (kompetencia 2,
  hub sor 30) és »Képes 3–4 nyitott kérdéssel feldolgozni egy történetet«
  (kompetencia 3, sor 34). A kapu ezeket **alulreprezentálja**:
  - az **R5 Inkluzivitás** rubrika-sor »Oké« szintje csak »1 nevezett akadály +
    1 konkrét alternatív belépési pont«-ot kér (KAPU sor 343/353) — a »3
    inkluzivitási szempont« **sosem mérődik**;
  - a »3–4 nyitott kérdés« kompetenciának a kapuban (sem kvíz, sem rubrika) **NINCS
    önálló itemje vagy rubrika-sora**: a 12 itemből a trigger / kérdés-érzékenységet
    csak 2 item (11, 12) érinti, a »3–4 kérdés generálása« **produktum-szintű mérése
    hiányzik**.

  Így a kapu **nem méri a kimondott mastery-célok egy részét**.
- **Javaslat (DÖNTÉS):** Vagy **igazítsd a kimeneti kompetencia-megfogalmazásokat** a
  ténylegesen mért szinthez (»legalább 1«), vagy **emeld a rubrika/kvíz mérési
  szintjét** a célhoz: R5 »Oké« = 2 akadály + variáció; külön rubrika-sor vagy item a
  3–4 nyitott kérdés generálására. A cut-score / szint-átfogalmazás **emberi review-t**
  érdemel.
- **Forrás:**
  - assessment-validity (construct coverage)
  - id-alignment (mastery)

---

### 8. [D3] M7 KAPU — a BLOKKOLÓ gyerekvédelmi konstruktumra (R4) nulla kvíz-item esik (construct-validitási rés)

- **Dimenzió:** D3 — konstruktum-validitás / item↔cél lefedettség (D3.1; D3.6)
- **Fájl / hely:** `02 Tervezet/MODULOK/M7/M7 – KAPU – értékelő (item-bank + rubrika).md`
  → (A) ITEM-BANK Q1–Q12 (Blokk 4 etikus AI: Q10–Q12) szemben a (B) rubrika **R4
  blokkoló** + R7 sorral és a 35. sori lefedettség-állítással
- **Probléma:** A kvíz (12 item) lefedettsége: SMART, 11 pont, Zmán Kvucá-checklist,
  etikus AI — **de a kapu BLOKKOLÓ gyerekvédelmi konstruktumára (R4) NULLA item esik:**
  nincs item a red-flag-eljárásra, eszkalációs láncra vagy disclosure-elvekre. Így a
  „fogalmi belépő” **épp azt a tudásalapot nem igazolja**, amit a produktum-rubrika
  blokkolóként kapuz. Ráadásul a 33. sor elvárása („minden mastery-kulcscélnak van
  legalább egy itemje”, D3.1) **sérül**: az R4-kulcscél item nélkül marad.
- **Javaslat (DÖNTÉS):** Legalább **1–2 szcenárió-alapú (SJT, D3.6) item** felvétele a
  gyerekvédelmi alaplépésre (red flag → mit teszel / mit NEM teszel / kit vonsz be),
  best-response kulccsal, és **cél→item tábla kitöltése**, hogy R4 ne maradjon
  alul-reprezentálva. (A safeguarding tartalmi megalapozása maga **D7-döntés**.)
- **Forrás:** —

---

### 9. [D2] Korosztályi / fejlődéslélektani alapismeret árva-alátámasztatlan — M6 és M7 R2 méri/kapuzza, a curriculum sehol nem tanítja explicit

- **Dimenzió:** D2 — constructive alignment (tanítva vs. mérve)
- **Fájl / hely:** `02 Tervezet/MODULOK/M6/M6 – „Toolbox_ játék, történet, kézműves & inkluzivitás”.md`
  → M6 §2 (1. kimeneti kompetencia, „6–10 / 11–13 / 14–16 / 16+”) és **M6 KAPU R2**;
  továbbá `02 Tervezet/MODULOK/M7/M7 – KAPU – értékelő (item-bank + rubrika).md` **R2
  level-3** („életkori / korosztályi sajátosság”), M7 áttekintő §6 rubrika 2. sor;
  `CURRICULUM-IV` unsupported #17
- **Probléma:** A korosztályi / fejlődéslélektani alapismeret (6–10, 11–13, 14–16,
  16+ életkori sajátosságok) **ÁRVA-ALÁTÁMASZTATLAN**: az M6 mérőeszköze (eszköz↔
  korosztály illesztés, R2 sor) és az M7 Peula v2 rubrika (R2 korosztály-illeszkedés,
  level-3) **MÉRI / KAPUZZA**, de a curriculum **SEHOL nem TANÍTJA** explicit. Az M3 a
  someres kvuca-PROFILOKAT (Parparim / Kivsza / Leviatan / Zorea) tanítja, ami someres
  **archetípus, NEM életkori fejlődéslélektan** — maga az M6 áttekintő is „csak
  röviden ismételve, nem tanítva”-ként jelöli (M6 §Feltételez). Az M7 R2 level-3
  ráadásul **össze is mossa** a kettőt: „az M3-ban tanult kvuca-profil mentén” életkori
  sajátosságot kér számon, amit az M3 nem ad meg. Constructive alignment sérül: a
  tanuló **olyan tudásra van kapuzva, amihez nem kap tanítást**.
- **Javaslat (DÖNTÉS):** Vagy az **M3-ba** (korosztály-mátrix produktum köré) emelj be
  egy explicit életkori / fejlődéslélektani tanító elemet, amely a 6–10 / 11–13 /
  14–16 / 16+ sávokat a someres profilokhoz köti, VAGY az **M6 elejére** tegyél egy
  rövid korosztály-tanító leckét. Ennek hiányában az M6 R2 és az M7 R2 **nem-tanított
  konstruktumot mér**. (Curriculum-ív strukturális kérdés.)
- **Forrás:** —

> **Megj.:** Ütközik a kör 2 / 2. tétellel: a `CURRICULUM-IV` szinkron-tétel szerint a
> korosztály-tanítás a **mai modulfájlokban már részben tanítva van** (M3.2 SLIDE 5B).
> A 9. tétel az M6/M7 R2 **mérési oldaláról** vetít — döntéskor a kettőt
> össze kell olvasni (tényleg tanítva van-e az M6/M7 R2 által mért konstruktum, vagy
> az M3.2 5B csak a hub-szintet fedi).

---

### 10. [D3] M7 KAPU — a peula-dramaturgia (4 fázis) FELTÉTELEZETT és MÉRT, de a curriculumban korábban nem tanított

- **Dimenzió:** D3 — konstruktum-validitás (feltételezett előtudás ↔ mért konstruktum)
- **Fájl / hely:** `02 Tervezet/MODULOK/M7/M7 – KAPU – értékelő (item-bank + rubrika).md`
  → M7 KAPU **R3** (level-2/3: „bevezetés–élmény–feldolgozás–zárás ív”), kvíz **Q4**
  (11 pont 3 fázisa); M7 áttekintő §2.2 („Azonosítja a Peula 11 pontjának fázisait”);
  `CURRICULUM-IV` unsupported #21
- **Probléma:** A peula-dramaturgia (4 fázis: bevezetés–élmény–feldolgozás–zárás)
  **FELTÉTELEZETT és MÉRT, de nem TANÍTOTT**. Az M7 áttekintő §Feltételez expliciten
  „Alap peula-fogalom és -felépítés (korábbi programírás-alap)”-ra hivatkozik, ami a
  curriculumban **NEM létezik**: az M4 pitch 5 kérdéses (nem fázis-szerkezet), az M5
  tervezési táblázat, az M6 egyetlen játéklap — **egyik sem tanítja** a teljes peula
  4-fázisú dramaturgiáját. Az M7 R3 rubrikasor és a kvíz mégis a **fázis-ív
  felismerését** kéri. Konstruktum-validitás: a kapu a saját tanítása **ELŐTT**
  feltételezi és méri a fázisszerkezetet.
- **Javaslat (DÖNTÉS):** Vagy az **M5 / M6-ba** építs be egy minimál
  peula-dramaturgia (4 fázis) tanító elemet, amire az M7 Peula 11 pont épülhet, VAGY az
  **M7-be** tegyél explicit fázis-tanító micro-blokkot a Peula 11 pont előtt. Az M7
  §Feltételez **ne hivatkozzon** nem létező „korábbi programírás-alap”-ra.
- **Forrás:** —

> **Megj.:** Átfed a kör 1 / 7. és a kör 2 / 2. tétellel. A `CURRICULUM-IV`
> szinkron-tétel szerint a 4-fázist az **M7.2 lecke már tanítja** a KAPU előtt — ha ez
> a mai forrásban igaz, a 10. tétel megoldása részben az **M7 §Feltételez
> átfogalmazása** (ne hivatkozzon „korábbi programírás-alap”-ra), nem új tanító elem.

---

### 11. [D4] M2 identitás-térképezés árva kompetencia — egyetlen későbbi modul sem erősíti/alkalmazza újra mint kompetenciát

- **Dimenzió:** D4 — produktumlánc / árva kompetencia
- **Fájl / hely:** `02 Tervezet/MODULOK/M2/M2 – „Ki vagyok madrichként_” – Identitás, Somer-értékek és dugma ishit.md`
  → M2 §2 (identitás-körök, érték→viselkedés) + §6 portfólió-átkötés; kompetencia-térkép
  (`CURRICULUM-IV`): „Identitás-körök – Tanítva: M2, Erősítve: —”; M7 KAPU CAPSTONE-tábla
- **Probléma:** **ÁRVA KOMPETENCIA:** az M2 identitás-térképezés (identitás-körök +
  érték→viselkedés) tanítva és produktumba öntve (1 oldalas identitás-jegyzet), de a
  produktumlánc szempontjából **zsákutca** — egyetlen későbbi modul SEM erősíti /
  alkalmazza újra az identitás-térképezést **mint kompetenciát** (Erősítve: —).
  **Részben enyhítve:** az M2 §6 és az M7 KAPU CAPSTONE-tábla már beköti a választott
  someres **ÉRTÉKET** a SMART cél R-eleméhez (R1 „someres értékhez kötött”). **DE:**
  (a) ez csak az **érték-mondatot** horgonyozza, magát az **identitás-térkép
  kompetenciát** nem; (b) a Z reflexió **nem méri** az M2-höz viszonyított
  identitás-elmozdulást. A blended-ív így a madrich-identitásnál **cél-szakadást** mutat.
- **Javaslat (DÖNTÉS):** Erősítsd a horgonyt: vagy az **M4 kiállás/pitch** kösse vissza
  a madrich saját értékéhez / dugma ishitjéhez, vagy a **Z záró-reflexió** kérje számon
  az M2-höz mért identitás-elmozdulást (M0→Z szemléletváltás analógiájára). Így az
  identitás-térkép **nem csak az M2 érték-mondatként, hanem kompetenciaként is
  továbbél**.
- **Forrás:** —

---

### 12. [D2] M0 belépő-quiz — gyerekvédelmi viselkedés-cél Bloom-szintje > a quiz mérési szintje (felidéző item < alkalmazási cél)

- **Dimenzió:** D2 — cél↔értékelés illeszkedési rés (D2.5 + D3.1; Bloom-szint eltérés D2.4)
- **Fájl / hely:** `02 Tervezet/MODULOK/M0/M0 – „Kickoff, keret, technika”.md`
  → 2. Kimeneti kompetenciák (20–44. sor) vs. 5. Kapuk M0 belépő-quiz (132–138. sor)
- **Probléma:** **Cél↔értékelés illeszkedési rés** (D2.5 + D3.1). A modul 2.
  kompetenciája explicit **gyerekvédelmi viselkedés-célt** fogalmaz meg („meg tudja
  különböztetni, mi NEM az ő feladata… nem egyedül visz gyerekvédelmi ügyet”, 30. sor),
  és a quiz-témák között szerepel a „jelzési út gyerekvédelmi ügyben” (137. sor).
  Viszont a quiz csak „6–8 egyszerű kérdés (true/false + feleletválasztás)” szintű, ami
  **felidéző / megértő Bloom-szint** — a gyerekvédelmi cél **viselkedés / alkalmazás
  szinten** kimondott, de az értékelés **nem alkalmazási / elemzési** (D2.4: item
  Bloom-szint < cél Bloom-szint). A 4. kompetencia (puha / éles kapu különbség) jól
  mért M0.3-ban, de a **gyerekvédelmi cél mérése aluldimenzionált** a célhoz képest.
- **Javaslat (DÖNTÉS):** Az M0 belépő-quizbe (vagy az M0.2 aktivitásába) kerüljön
  **legalább egy szcenárió-alapú, döntést kérő item** a gyerekvédelmi jelzési útról
  (van ilyen az M0.2 SLIDE 3-ban, de az **nem kapuzott**) — a kompetencia-cél
  Bloom-szintjének megfelelő mérés. **Tevékenység-redesign, emberi tervezést igényel.**
- **Forrás:** —

---

### 13. [D3] M1 KAPU — a sor-szintű ≥1 (különösen az I/hatás) kapu-garancia a Moodle-ban nem automatizálható; kétképzős kalibráció nélkül kompenzálható

- **Dimenzió:** D3 — mastery-kapu construct-validitás (D3.1) + cut-score védhetőség (D3.8) + kalibráció (D3.7)
- **Fájl / hely:** `02 Tervezet/MODULOK/M1/M1 – KAPU – értékelő (item-bank + rubrika).md`
  → 0. szakasz fejléc (17. sor) és 5. Moodle-gyorslista (279. sor): „A Moodle natívan
  az összpontot kapuzza; a »minden sorban ≥1« szabályt a képző a pontozáskor
  érvényesíti”. Ugyanez **M1.4-ben** (238. sor).
- **Probléma:** A kapu **kulcsbiztosítéka** („egyik SBI-elem, különösen az I/hatás, sem
  hiányozhat teljesen”) kizárólag a **sor-szintű ≥1** feltételen áll, ám a fájl maga
  elismeri, hogy ezt a Moodle **automatikusan NEM tudja kapuzni** — csak az 5/8
  összpontot. Így a tényleges automatizált kapu **átengedhet** olyan beadványt, ahol pl.
  az **I (hatás) sor 0**, ha a többi sor kompenzál (pl. 2+2+0+2=6 ≥5). A validitási
  garancia teljes egészében a **képző kézi, kalibrálatlan-kockázatú ellenőrzésére**
  hárul, dokumentált **kétképzős kalibráció (D3.7 cél) nélkül**. Ez a mastery-kapu
  **construct-validitását (D3.1)** és a **cut-score védhetőségét (D3.8)** gyengíti.
- **Javaslat (DÖNTÉS):** Architektúra-döntés: vagy állítsd be a sorszintű minimumot
  **technikailag** (pl. Moodle conditional / külön „I-sor ≥1” feltétel workflow-val,
  vagy a hatás-sort **önálló pass/fail kérdésként**), vagy tedd **kötelezővé a
  kétképzős kalibrációt** minden határeset-beadványra, dokumentált eljárással. A
  jelenlegi „a képző majd figyel rá” **nem reprodukálható kapu**.
- **Forrás:** —

---

### 14. [D3] M2 KAPU — a hub 3-értékes kimeneti kompetenciája vs. a rubrika 1 kiemelt értéke (cél↔item alulreprezentáció)

- **Dimenzió:** D3 — konstruktum-/illeszkedési ellentmondás (D3.1)
- **Fájl / hely:** `02 Tervezet/MODULOK/M2/M2 – KAPU – értékelő (item-bank + rubrika).md`
  → C. szakasz rubrika **R2 sor** (173. sor) vs. modul-hub **2. kompetencia** (M2-hub
  28–31. sor: „Kiválaszt 3 személyes értéket”) és **M2.2 lecke** (3 vezető érték)
- **Probléma:** **Konstruktum-/illeszkedési ellentmondás** a mastery-produktum és a
  kimondott kompetencia között (D3.1): a hub 2. kompetenciája **3 érték + mindegyikhez
  viselkedés** megfogalmazását követeli, az M2.1–M2.2 leckék is 3 értéket tanítanak /
  gyakoroltatnak, a kapu-rubrika **R2 viszont csak 1 kiemelt értéket** horgonyoz le. A
  hub maga jelzi („a másik kettő a feltáró munkát gazdagítja”), de ez azt jelenti, hogy
  a **3-értékes kimeneti kompetencia 2/3-a** se a rubrikában, se máshol **nincs mérve**
  — lefedetlen cél / alul-reprezentáció a kapuban.
- **Javaslat (DÖNTÉS):** Döntés: vagy a kimeneti kompetenciát **igazítják 1 kiemelt
  értékre** (a 3 érték explicit „feltáró, nem mért” státuszba kerül a 2. kompetenciánál
  is), vagy a **rubrika / self-check kiterjed a 3 érték→viselkedés** leképezésre. A
  jelenlegi **szövegszintű mentegetés nem old fel** egy cél↔item alul-reprezentációt.
- **Forrás:**
  - assessment-validity
  - id-alignment

---

### 15. [batch összegzés] Visszatérő architektúra-minta: a kapuk a hub-szintű mennyiségi/blokkoló célok egy részét nem (vagy nem determinisztikusan) mérik

- **Dimenzió:** D3.1 / D3.8 / D2 (kereszt-modul minta)
- **Fájl / hely:** M0 / M1 / M2 / M6 / M7 KAPU + hub-fájlok (lásd 6–14. tételek hivatkozásai)
- **Probléma (összegző, nem önálló új találat):** A 6–14. tételekből kirajzolódik egy
  **ismétlődő minta**: több modulban a **hub-szintű kimeneti kompetencia** (mennyiségi
  cél — 3 érték, 3 inkluzivitási szempont, 3–4 nyitott kérdés — vagy blokkoló
  konstruktum — R4 gyerekvédelem, I/hatás-sor) **ígéretesebb / szigorúbb**, mint amit a
  hozzá tartozó **kapu ténylegesen, determinisztikusan mér**. A rés vagy
  **alulreprezentáció** (M2 R2, M6 R5, M7 R4), vagy **nem-automatizálható garancia**
  (M1 sor-szintű ≥1), vagy **completion ↔ küszöb ellentmondás** (M0).
- **Javaslat (DÖNTÉS):** Egy **egységes kapu-filozófiai döntés** ajánlott a stáb/
  architektúra-review szintjén: rögzítsék, hogy a hub-kompetenciák **(a) mind
  kapuzandók** (akkor a rubrika/kvíz emelendő a célhoz), vagy **(b) explicit
  szétválasztják** a „mért mastery-magot” a „feltáró/gazdagító” céloktól (akkor a hub
  szövegét kell e státuszhoz igazítani). A modulonkénti megoldás (6–14.) legyen e
  közös elv leképezése, ne ad-hoc.
- **Forrás:** —
