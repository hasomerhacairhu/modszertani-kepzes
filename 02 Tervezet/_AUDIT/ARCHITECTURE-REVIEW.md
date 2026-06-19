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
