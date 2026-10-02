# LMS – activity manifest

> **Kánoni build-szerződés.** Ebből a fájlból a következő implementációs agentnek nem kell pedagógiai prózát újraértelmeznie.
>
> - `build_id`: repository-szintű stabil azonosító.
> - `cmid`: **BUILD_OUTPUT**, a Moodle létrehozás után visszaadott course-module ID. Nem emberi döntés és nem placeholder.
> - Dátumok: kizárólag a **HUM-OPS-01** központi ütemezéséből (§7) származnak. A fájlban nincs kitalált naptári dátum; a projektgazdai szabályból levezetett pontokat a §7 külön jelöli.
> - A táblázat csak **tényleges Moodle-activityket** sorol. Az offline peulák sorrendje külön táblában van.
> - A `completion` és a `mastery` két külön mező. A megnyitás/végigkattintás soha nem helyettesít mastery-feltételt.
> - A fájl a projektgazda 2026-10-02-i döntéseit alkalmazza (`Emberi jóváhagyás szükséges.md`). A HUM-tételek lezártak; a megnevezett szerepek (Memuna, DPO, programvezető stb.) későbbi ellenőrzése utólagos ellenőrzés (vétó/QA), nem új döntési kapu. A táblázatok „HUM-… élesben” jelölése azt mutatja, melyik döntés tartalmának kell az éles kurzusban is megjelennie.

## 1. Megvalósítási profilok

| Profil | Típus | Alapértelmezett completion | Grade / pass | Retry | Mentor-láthatóság | Privacy | A11y / fallback |
|---|---|---|---|---|---|---|---|
| **H5P-C** | H5P activity | automatikus, a forrásban előírt interakció(k) érdemi befejezése; puszta megtekintés nem elég, ha a lecke választ kér | nincs mastery-küszöb | újranyitható | completion + aggregált eredmény; személyes reflexió tartalmát csak a kijelölt mentor/értékelő láthatja, és csak ha ténylegesen szükséges (a forrás ezt kifejezetten indokolja); a Moodle alapbeállításában a tanári szerepkör a próbálkozásokat is látja, ezért a láthatóságot a HUM-PRIV-01 szerint kell beállítani és stagingben tesztfiókkal visszaolvasni | **P1** fiókhoz kötött teljesítési adat; ha az activity szabad szöveget rögzít: **P2**; személyes szabad szöveg lehetőleg ne kerüljön H5P-be | WCAG 2.2 AA pre-flight; húzásmentes út; felirat/leirat; alacsony adatú szöveges út |
| **QUIZ-D** | Moodle Quiz, diagnosztikus | attempt submitted | nincs blokkoló pass | a forrás szerinti, egyébként 2–3 | item-analitika | **P1** teljesítési adat | billentyűzet, mobil, zoom; nincs drag-only item |
| **QUIZ-M** | Moodle Quiz, mastery | attempt submitted **és** az explicit pass-feltétel igazolt; az elfogyott próbálkozásokra is teljesítést adó opció (Moodle-szabály: `completionpassorattemptsexhausted`) kikapcsolva | explicit küszöb | 2 automatikus próbálkozás (1 normál + 1 javító), további próbálkozást a képző nyit kézzel; „Grading method”: „Highest grade”; a completionhöz a legjobb megerősített eredmény számít | eredmény + item-szintű review ott, ahol kritikus item van | **P1** teljesítési adat | mint QUIZ-D |
| **ASSIGN-S** | Moodle Assignment, puha/product completion | érdemi beadvány leadva: az előírt mezőkben tényleges, minimálisan értelmezhető tartalom van; üres vagy kitöltetlen sablon, illetve a puszta fájlfeltöltés nem completion; a tartalmat a kijelölt mentor/értékelő erősíti meg (technikai út: `LMS – H5P runtime acceptance.md` 1. pont) | nincs kizáró küszöb; a forrás minimuma alatt javítás | a puha kapus beadásoknál (LMS-M2-05, LMS-M4-05, LMS-Z-04) 1 normál + 1 javító beadás automatikusan, további beadást a képző nyit kézzel (a §2 sor szerint); a nem kapus Peula v1-nél (LMS-M7-05) újrabeadás engedett; a már megszerzett teljesítést önkéntes újrabeadás egyik esetben sem írja felül (runtime acceptance 19. pont) | a kijelölt mentor/értékelő | **P2** személyes tanulói produktum | online text **és** fájlút, hozzáférhető sablon |
| **ASSIGN-M** | Moodle Assignment, mastery | beadvány leadva **és** megerősített kapueredmény (a kapufájl teljes feltétele, nem a nyers pont; a kétkomponensű M3 kapunál az Assignment-komponens megerősített rubrikája, mert a kapukvíz csak utána nyílik; az M7-nél a kvíz a v2 előtt fut, ezért a v2 csak a kvíz megerősített eredménye után adható le) | explicit kapufeltétel | 1 normál + 1 javító beadás automatikusan, további beadást a képző nyit kézzel; a completionhöz a legjobb megerősített eredmény számít, a már megszerzett teljesítést önkéntes, gyakorló újrabeadás nem írhatja felül (technikai út: runtime acceptance 19. pont) | a kijelölt mentor/értékelő | **P2**, érzékeny tartalom bekérését kerülni | mint ASSIGN-S |
| **FORUM-C** | General Forum | előírt poszt + válasz | nincs grade | szerkeszthető a helyi beállítás szerint | kurzusrésztvevők látják | **P2-PUBLIC-IN-COURSE**; személyes/érzékeny adatot ne kérjen | billentyűzet, reflow; szöveges felület |
| **FEEDBACK-N** | Moodle Feedback | kitöltve | nincs grade | egyszer | eredmény a HUM-PRIV-03 szerint | **P2**; a válaszok név nélkül jelennek meg a feldolgozásban, de a kitöltés nem anonim: a felhasználó azonosítója az adatbázisban marad, és a completion fiókhoz kötött; teljes anonimitást nem ígérünk | mobil + billentyűzet + screen reader |
| **PAGE-C** | Page / Text and media | megtekintés, csak ha valóban információátadás a cél | nincs | n/a | n/a | **P0–P1** | szemantikus címsorok, alt, reflow |

**Privacy osztályok:** `P0` nincs learner input; `P1` fiókhoz kötött teljesítési/értékelési adat; `P2` szabad szöveg vagy tanulói produktum; `P2-PUBLIC-IN-COURSE` a kurzus résztvevőinek látható tartalom; különleges vagy gyermekvédelmi adatot **egyik activity sem kér kötelezően**: politikai, vallási, egészségügyi vagy más különleges adat normál tanulási activityben nem gyűjthető. Ha ilyen mégis megjelenik spontán, HUM-PRIV-01 és HUM-SAFE-01 szerint kell kezelni: nem normál tanulási rekord. Ha feltáráskor jelenik meg, kikerül a Moodle-ből, és az incidensfolyamatba kerül: a `Gyermekvédelem – release gate.md` §4.1 szerinti ötlépéses jelzési út lép életbe, az ügy dokumentációja pedig nem Moodle-ben, hanem külön, hozzáférés-korlátozott incidensnyilvántartásban készül (Google Workspace Shared Drive → `Restricted / Safeguarding / Incidents`; hozzáférés csak a Memunának – a Somer gyermekvédelmi felelősének –, a helyettesnek és a szervezeti vezetőnek; nem Moodle, nem GitHub). Egy activity privacy-osztálya a §2-beli sorának profiljából következik (szabad szöveget rögzítő H5P-C activitynél `P2`); az activitynkénti címzetteket, láthatóságot, jogalapot és megőrzést a HUM-PRIV-01 adatkezelési mátrixa rögzíti (`Adatvédelem – tanulói adatok és AI.md` §3).

**Hozzáférési alapszabály (HUM-PRIV-01):** projektgazdai döntés (2026-10-02); utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős. Mindenhez a legszűkebb szükséges hozzáférés: a zárt kvíz pontszámát (`P1`) az értékelő látja; a szabad szöveget és a reflexiót (`P2`) csak a kijelölt mentor/értékelő, és csak ha ténylegesen szükséges. Politikai, vallási vagy világnézeti válasz nem lehet fiókhoz kötött szavazás. A Program terv §4 és §7 ütközésében a szigorúbb, kisebb hozzáférést engedő szabály érvényes. Az activity-szintű adatkezelési mátrix többi része – a jogalappal és a megőrzési idővel együtt – az `Adatvédelem – tanulói adatok és AI.md` §3-ban van; a manifest privacy-megjegyzései erre hivatkoznak, nem másolják.

## 2. Tényleges Moodle-activityk

A `schedule_key` értékeit a §7 központi ütemezése adja (HUM-OPS-01). `—` = nincs külön határidő.

Ha egy leckében előírt szabad szöveges mező az `LMS – H5P runtime acceptance.md` 6. pontja szerint Moodle-oldali activityként valósul meg, akkor a build előtt saját sort kap ebben a táblázatban (build_id, profil, completion, privacy).

| build_id | cmid | Szakasz | Név | Profil | Kötelező | Forrás | Unlock / előfeltétel | Completion | Mastery / pass | schedule_key | Megjegyzés |
|---|---|---|---|---|---:|---|---|---|---|---|---|
| LMS-M0-01 | BUILD_OUTPUT | M0 | M0.1 – Üdv a képzésben! | H5P-C | igen | M0/Online leckék/M0.1 | kurzushozzáférés | profil | nincs | M0_L1 | |
| LMS-M0-02 | BUILD_OUTPUT | M0 | M0.2 – Madrich, nem terapeuta | H5P-C | igen | M0/Online leckék/M0.2 | LMS-M0-01 | profil | nincs | M0_L2 | HUM-SAFE-01: a lecke szerepet nevez (a Memuna), nevet és telefonszámot nem, a kontakt a kurzusszintű „Segítség és kapcsolatok” blokkban van; HUM-SAFE-03: a „ha téged is érint” blokk a kurzusszintű elemek szerint (a táblázat alatt) |
| LMS-M0-03 | BUILD_OUTPUT | M0 | M0.3 – Moodle, H5P és kapuk | H5P-C | igen | M0/Online leckék/M0.3 | **M0.A után nyílik dátummal**, nem jelenléti találgatással | profil | nincs | M0_L3 | |
| LMS-M0-04 | BUILD_OUTPUT | M0 | M0.4 – Dugma ishit online | H5P-C | igen | M0/Online leckék/M0.4 | LMS-M0-03 | profil | nincs | M0_L4 | |
| LMS-M0-05 | BUILD_OUTPUT | M0 | Bemutatkozó fal | FORUM-C | igen | M0.4 | LMS-M0-04 | **1 új téma + 1 válasz** | nincs | M0_FORUM | module-specific forum completion kézi beállítás; a Moodle a saját témára adott választ is beszámítja, ezért a „másik résztvevő posztjára” feltételt a completion nem ellenőrzi |
| LMS-M0-06 | BUILD_OUTPUT | M0 | M0 belépőkvíz | QUIZ-D | igen | M0 hub §5–6 + M0.1/M0.2/M0.3/M0.4 | LMS-M0-04 | kitöltve: mind a 7 item megválaszolva | **nincs cut-score**; ~60% csak stáb-jelző | M0_QUIZ | 7 item, több próbálkozás; az első próbálkozás diagnosztikus adat, a stáb-jelzést ennek item-statisztikájából kell számolni; az itemek, a kulcs és a visszajelzés megírva (M0 hub §5, 7 item; projektgazdai döntés, 2026-10-02): minden hibás válaszhoz egymondatos visszajelzés tartozik (miért nem jó, és hol találja a helyes szabályt); a 2. (jelzési út) item kulcsa a HUM-SAFE-01 ötlépéses útjához igazodik |
| LMS-M1-01 | BUILD_OUTPUT | M1 | M1.1 – Johari-ablak | H5P-C | igen | M1/Online leckék/M1.1 | **M0 complete** | profil | nincs | M1_L1 | a SLIDE 5 személyes reflexiója opcionális, nem completion-feltétel; lehetőleg learner-local |
| LMS-M1-02 | BUILD_OUTPUT | M1 | M1.2 – Megfigyelés ≠ értelmezés | H5P-C | igen | M1/Online leckék/M1.2 | LMS-M1-01 | profil | nincs | M1_L2 | drag-free egyenértékű út kötelező |
| LMS-M1-03 | BUILD_OUTPUT | M1 | M1.3 – SBI-modell | H5P-C | igen | M1/Online leckék/M1.3 | **M1.A után nyílik** | profil | nincs | M1_L3 | |
| LMS-M1-04 | BUILD_OUTPUT | M1 | M1.4 – Mondd el SBI-ben | H5P-C | igen | M1/Online leckék/M1.4 | LMS-M1-03 | profil | nincs | M1_L4 | a beadandó külön activity |
| LMS-M1-05 | BUILD_OUTPUT | M1 | M1.4 – SBI-beadandó | ASSIGN-M | igen | M1.4 + M1 KAPU | LMS-M1-04 | leadva + megerősített kapueredmény | **minden rubrikasor ≥1 ÉS összesen ≥5/8** | M1_ASSIGN | rubric manual fallback, lásd §5; Grade type: Point, Maximum grade = 8 |
| LMS-M2-01 | BUILD_OUTPUT | M2 | M2.1 – Ki vagyok madrichként? | H5P-C | igen | M2/Online leckék/M2.1 | **M1 complete** | profil | nincs | M2_L1 | személyes reflexió lehetőleg learner-local: az identitástérkép helyben marad, nem beadandó; a nem érzékeny, viselkedésszintű reflexió viszont rögzítve (M2 hub §6) |
| LMS-M2-02 | BUILD_OUTPUT | M2 | M2.2 – Értékeim mint iránytű | H5P-C | igen | M2/Online leckék/M2.2 | LMS-M2-01 | profil | nincs | M2_L2 | |
| LMS-M2-03 | BUILD_OUTPUT | M2 | M2.4 – Reflektív napló és határok | H5P-C | igen | M2/Online leckék/M2.4 | **M2.A után nyílik** | profil | nincs | M2_L4 | **szándékosan M2.3 előtt** |
| LMS-M2-04 | BUILD_OUTPUT | M2 | M2.3 – Somer 3 pillére | H5P-C | igen | M2/Online leckék/M2.3 | LMS-M2-03 | profil | nincs | M2_L3 | HUM-SOMER-01/03 érintett; a nyitó pillér-kérdés rögzítés nélküli önreflexió, nem fiókhoz kötött szavazás (HUM-PRIV-01), és a completion nem kötődik hozzá |
| LMS-M2-05 | BUILD_OUTPUT | M2 | M2 – Identitás-jegyzet | ASSIGN-S | igen | M2 KAPU | **M2.B után** | érdemi, 1 oldalas jegyzet leadva: az előírt mezőkben tényleges, minimálisan értelmezhető tartalommal (üres vagy kitöltetlen sablon, illetve a puszta fájlfeltöltés nem elég); a kijelölt mentor/értékelő erősíti meg | puha kapu, fejlesztő rubrika; hiányosnál javítás | M2_ASSIGN | érzékeny történet nem kötelező; 1 normál + 1 javító beadás automatikusan, további beadást a képző nyit kézzel; a legjobb megerősített eredmény számít (Program terv §5) |
| LMS-M3-01 | BUILD_OUTPUT | M3 | M3.1 – Történetek egy kvucáról | H5P-C | igen | M3/Online leckék/M3.1 | **M2 complete** | profil | nincs | M3_L1 | |
| LMS-M3-02 | BUILD_OUTPUT | M3 | M3.2 – Három kvuca, három világ | H5P-C | igen | M3/Online leckék/M3.2 | LMS-M3-01 | profil | nincs | M3_L2 | HUM-SOMER-02 |
| LMS-M3-03 | BUILD_OUTPUT | M3 | M3.3 – Gyermekvédelem 101 | H5P-C | igen | M3/Online leckék/M3.3 | **M3.A után nyílik**; HUM-SAFE-01/02 **élesben**; stagingben belső QA | profil | nincs | M3_L3 | learner release előtt a Memuna gyermekvédelmi átnézése (`Gyermekvédelem – release gate.md` §2, §6) |
| LMS-M3-04 | BUILD_OUTPUT | M3 | M3.4 – Do / Don’t madrichként | H5P-C | igen | M3/Online leckék/M3.4 | LMS-M3-03 | profil | nincs | M3_L4 | |
| LMS-M3-05 | BUILD_OUTPUT | M3 | M3 – Helyzetelemzés | ASSIGN-M | igen | M3.4 + M3 KAPU | LMS-M3-04; M3.B erősen ajánlott | leadva + megerősített rubrika | minden sor ≥1; **R2 és R4 blokkoló** | M3_ASSIGN | csak kitalált, életszerű eset (valós eset névtelenítve sem); mentor review; R2/R4 blokkoló kimenetnél kétszemes döntés (§4); összetett feltétel manual/runtime fallback; Grade type: Point, Maximum grade = 8; HUM-SAFE-01 élesben |
| LMS-M3-06 | BUILD_OUTPUT | M3 | M3 – Gyermekvédelmi kapukvíz | QUIZ-M | igen | M3 KAPU | LMS-M3-05 | attempt + megerősített eredmény | **≥10/12 ÉS Q2/Q4/Q7/Q9 mind helyes** | M3_QUIZ | összetett feltétel manual/runtime fallback; HUM-SAFE-01 élesben |
| LMS-M4-01 | BUILD_OUTPUT | M4 | M4.1 – Mit üzen a testem? | H5P-C | igen | M4/Online leckék/M4.1 | **M3 complete** | forrás szerinti 2 reflexióval | nincs | M4_L1 | HUM-PED-01 élesben |
| LMS-M4-02 | BUILD_OUTPUT | M4 | M4.2 – Aktív hallgatás | H5P-C | igen | M4/Online leckék/M4.2 | LMS-M4-01 | forrás szerinti 2 reflexióval | nincs | M4_L2 | HUM-PED-01 élesben |
| LMS-M4-03 | BUILD_OUTPUT | M4 | M4.3 – Kérdezési minták | H5P-C | igen | M4/Online leckék/M4.3 | **M4.A után** | mini-kvíz + reflexió | diagnosztikus | M4_L3 | HUM-PED-01 élesben |
| LMS-M4-04 | BUILD_OUTPUT | M4 | M4.4 – 45 mp-es peulabemutató | H5P-C | igen | M4/Online leckék/M4.4 | LMS-M4-03 | H5P befejezve | nincs | M4_L4 | HUM-PED-01 élesben |
| LMS-M4-05 | BUILD_OUTPUT | M4 | M4.4 – Peulabemutató-vázlat | ASSIGN-S | igen | M4.4 + M4 hub §6 | **M4.B után** | érdemi, nem üres vázlat leadva: az előírt mezőkben tényleges, minimálisan értelmezhető tartalommal (üres vagy kitöltetlen sablon, illetve a puszta fájlfeltöltés nem elég); a kijelölt mentor/értékelő erősíti meg | puha kapu, formatív: a mentori „Alapszint / rendben” küszöb (mind az 5 sablonelem azonosítható, M4 hub §6) fejlesztő visszajelzés, nem completion- és nem nyitási feltétel; hiányosnál mentori visszajelzés + javító beadás | M4_ASSIGN | társas visszajelzés a leadás előtt; 1 normál + 1 javító beadás automatikusan, további beadást a képző nyit kézzel; a legjobb megerősített eredmény számít (Program terv §5); HUM-PED-01 élesben |
| LMS-M5-01 | BUILD_OUTPUT | M5 | M5.1 – Mi a nonformális nevelés? | H5P-C | igen | M5/Online leckék/M5.1 | **M4 complete** | profil | nincs | M5_L1 | |
| LMS-M5-02 | BUILD_OUTPUT | M5 | M5.2 – Feladat → cél → kvuca → módszer | H5P-C | igen | M5/Online leckék/M5.2 | LMS-M5-01 | profil | nincs | M5_L2 | |
| LMS-M5-03 | BUILD_OUTPUT | M5 | M5.3 – Hogyan tanulunk tényleg? | H5P-C | igen | M5/Online leckék/M5.3 | **M5.A után** | profil | nincs | M5_L3 | Dialog Cards runtime teszt |
| LMS-M5-04 | BUILD_OUTPUT | M5 | M5.4 – Cél–kvuca–módszer mini-táblázat | H5P-C | igen | M5/Online leckék/M5.4 | LMS-M5-03 | profil | nincs | M5_L4 | |
| LMS-M5-05 | BUILD_OUTPUT | M5 | M5.4 – Modulproduktum | ASSIGN-M | igen | M5.4 + M5 KAPU | **M5.B után** | leadva + megerősített kapueredmény | minden sor ≥ Alapszint; **R4 Hiányos = javítás** | M5_ASSIGN | összetett feltétel manual/runtime fallback |
| LMS-M5-06 | BUILD_OUTPUT | M5 | M5 – Fogalmi önellenőrzés | QUIZ-D | igen | M5 KAPU | LMS-M5-04 | kitöltve | ≥10/12 csak diagnosztikus jelző | M5_QUIZ | 2–3 próbálkozás |
| LMS-M5-07 | BUILD_OUTPUT | M5 | M5.3 – Késleltetett felidézési pont | PAGE-C vagy H5P-C (a forrás szerint Moodle Label vagy rövid H5P) | igen | M5/Online leckék/M5.3 §3.6 | **LMS-M5-03 completion + 72 óra** (tanulónként, relatív időzítés) | a forrás szerinti felidézési interakció elvégzése | nincs | — | nem feltétele az M6 nyitásának, de az online félév teljesítéséhez kell (§4); nem jelenhet meg ugyanabban a tanulási ülésben (M5.3 §3.6); a típus (Label vagy rövid H5P) nyitott, mert a forrás mindkettőt megengedi; eszköz: KUTATÁS KELL, mert a core Moodle-ben nincs teljesítéshez relatív, felhasználónkénti késleltetés; runtime acceptance 4. pont |
| LMS-M6-01 | BUILD_OUTPUT | M6 | M6.1 – Játék-kategóriák 3 aktuális kvucára | H5P-C | igen | M6/Online leckék/M6.1 | **M5 complete** | profil | nincs | M6_L1 | |
| LMS-M6-02 | BUILD_OUTPUT | M6 | M6.2 – Történet mint tükör | H5P-C | igen | M6/Online leckék/M6.2 | LMS-M6-01 | profil | nincs | M6_L2 | |
| LMS-M6-03 | BUILD_OUTPUT | M6 | M6.3 – Kézműves, ami tanít is | H5P-C | igen | M6/Online leckék/M6.3 | **M6.A után** | profil | nincs | M6_L3 | fotó csak HUM-PRIV-02 szerint |
| LMS-M6-04 | BUILD_OUTPUT | M6 | M6.4 – Döntési szcenáriók | H5P-C | igen | M6/Online leckék/M6.4 | LMS-M6-03 | **legalább 3 külön eset tényleges teljesítése** | nincs | M6_L4 | runtime bizonyítandó |
| LMS-M6-05 | BUILD_OUTPUT | M6 | M6 – Játéklap | ASSIGN-M | igen | M6.B + M6 KAPU | **M6.B után** | leadva + mentor által megerősített kapueredmény | minden sor ≥2; **R4 és R5 blokkoló feltétel** | M6_ASSIGN | társas visszajelzés élőben, nem Moodle Workshop |
| LMS-M6-06 | BUILD_OUTPUT | M6 | M6 – Szcenárió-önellenőrzés | QUIZ-D | igen | M6 KAPU | LMS-M6-04 | kitöltve | ≥10/12 csak diagnosztikus jelző | M6_QUIZ | korlátlan újrapróbálás |
| LMS-M7-01 | BUILD_OUTPUT | M7 | M7.1 – SMART nevelési cél | H5P-C | igen | M7/Online leckék/M7.1 | **M6 complete** | profil | nincs | M7_L1 | |
| LMS-M7-02 | BUILD_OUTPUT | M7 | M7.2 – Peula 11 pont + AI | H5P-C | igen | M7/Online leckék/M7.2 | LMS-M7-01 | profil | nincs | M7_L2 | AI opcionális (HUM-PRIV-04), no-AI út kötelező; a lecke elején kb. 15 perces AI-jártassági blokk; saját szolgáltatói fiók nem kell: a kurzus AI-segédje a Somer szerveroldali végpontján át fut (runtime acceptance 20. pont) |
| LMS-M7-03 | BUILD_OUTPUT | M7 | M7.3 – Zmán Kvucá-checklist | H5P-C | igen | M7/Online leckék/M7.3 | **M7.A után nyílik** | profil | nincs | M7_L3 | gyermekvédelmi rész: HUM-SAFE-01 élesben |
| LMS-M7-04 | BUILD_OUTPUT | M7 | M7.4 – Peula v1 + AI | H5P-C | igen | M7/Online leckék/M7.4 | LMS-M7-03 | profil | nincs | M7_L4 | AI opcionális (HUM-PRIV-04), no-AI út kötelező; saját szolgáltatói fiók nem kell: a kurzus AI-segédje a Somer szerveroldali végpontján át fut (runtime acceptance 20. pont) |
| LMS-M7-05 | BUILD_OUTPUT | M7 | Peula v1 – első vázlat | ASSIGN-S | igen | M7.4 | LMS-M7-04 | érdemi v1 leadva: az előírt mezőkben tényleges, minimálisan értelmezhető tartalommal (üres vagy kitöltetlen sablon, illetve a puszta fájlfeltöltés nem elég); a kijelölt mentor/értékelő erősíti meg | formatív, nem buktat | **M7_V1_DUE** | v2-vel nem lehet azonos napon; a kijelölt mentor rubrikára épülő visszajelzést ad a v1-re, a v2 előtt (HUM-OPS-01; a levezetett dátumok: §7) |
| LMS-M7-07 | BUILD_OUTPUT | M7 | M7 – SMART & Zmán Kvucá kvíz (felkészültségi, a v2 előtt) | QUIZ-M | igen | M7 KAPU | az LMS-M7-05 beadása (a v1 leadása, nem a mentor által megerősített completionje; runtime acceptance 1. pont) | attempt + megerősített eredmény | **≥12/14 ÉS Q13 helyes** | M7_QUIZ | felkészültségi kapu: ajánlott még az M7.B előtt teljesíteni, a v2 leadása előtt kötelező; a megerősített eredménye a v2 (LMS-M7-06) leadásának feltétele; a kapu konjunktív marad (kvíz ÉS v2-rubrika); 1 normál + 1 javító próbálkozás, további a képző kézi nyitásával (QUIZ-M); összetett feltétel manual/runtime fallback; HUM-SAFE-01/02 élesben |
| LMS-M7-06 | BUILD_OUTPUT | M7 | Peula v2 + Zmán Kvucá | ASSIGN-M | igen | M7 KAPU | **LMS-M7-05 → M7.B → külön revíziós szakasz**; **LMS-M7-07 megerősített eredménye** | leadva + megerősített rubrika | **≥17/24 ÉS R1/R5/R6 ≥2 ÉS R4 ≥2** | **M7_V2_DUE** | 1 sor AI-használat vagy „nem használtam”; nem pontozott; valós kvucára csak nem azonosító, csoportszintű információval, saját kvuca nélkül kitalált profillal; blokkoló kimenetnél kétszemes döntés (§4); összetett feltétel manual/runtime fallback; Grade type: Point, Maximum grade = 24; HUM-SAFE-01/02 élesben |
| LMS-Z-01 | BUILD_OUTPUT | Z | Z.1 – Visszanéző tükör | H5P-C | igen | Z/Online leckék/Z.1 | **M7 complete** | profil | nincs | Z_L1 | |
| LMS-Z-02 | BUILD_OUTPUT | Z | Z.2 – Saját tanulási pillanataim | H5P-C | igen | Z/Online leckék/Z.2 | LMS-Z-01 | profil | nincs | Z_L2 | személyes részlet nem kötelező |
| LMS-Z-03 | BUILD_OUTPUT | Z | Z.3 – Híd a terepre | H5P-C | igen | Z/Online leckék/Z.3 | LMS-Z-02 | profil | nincs | Z_L3 | |
| LMS-Z-04 | BUILD_OUTPUT | Z | Záró reflexió + következő lépés | ASSIGN-S | igen | Z.4 | **Z.A után, a §7 szerinti dátummal** | érdemi reflexió leadva: az előírt mezőkben tényleges, minimálisan értelmezhető tartalommal (üres vagy kitöltetlen sablon, illetve a puszta fájlfeltöltés nem elég); a kijelölt mentor/értékelő erősíti meg | completion, nem vizsga | Z_REFLECTION | draft/resume runtime test; 1 normál + 1 javító beadás automatikusan, további beadást a képző nyit kézzel; a legjobb megerősített eredmény számít (Program terv §5); videós leadás csak opcionálisan, az alapértelmezés az írásos reflexió (HUM-PRIV-02; a videó jogalapját és megőrzését az `Adatvédelem – tanulói adatok és AI.md` §3 adja) |
| LMS-Z-05 | BUILD_OUTPUT | Z | Képzési visszajelzés – név nélkül | FEEDBACK-N | igen | Z.4 | Z.A után | kitöltve | nincs | Z_FEEDBACK | HUM-PRIV-03: kötelező marad, de nem nevezhető anonimnak; a tanulói szöveg: „A válaszok név nélkül jelennek meg a feldolgozásban.”; a nyers válaszok megőrzését és későbbi összesítését az `Adatvédelem – tanulói adatok és AI.md` §3 adja; kézi létrehozás a Moodle felületén (az MCP nem támogatja) |

**Kurzusszintű elemek** (nem modul-activityk, de a buildben helyük van; tartalmukat a megnevezett döntés adja):

- a „Segítség és kapcsolatok” blokk (HUM-OPS-02) és a gyermekvédelmi kontaktblokk (HUM-SAFE-01);
- a „ha téged is érint” blokk (HUM-SAFE-03; szó szerinti szövege a `Gyermekvédelem – release gate.md`-ben): a kurzus elején (M0.1), az M2.4 és az M3.3 érzékeny része előtt, valamint ott, ahol egy korábbi ad hoc támogató blokk helyére került; az offline M2.A és M3.B a saját peulaszövegében hozza;
- az adatvédelmi tájékoztató (HUM-PRIV-01);
- a kurzus opcionális AI-segédje (HUM-PRIV-04: `Moodle → a Somer szerveroldali végpontja → OpenAI Responses API`, saját szolgáltatói fiók nélkül; runtime acceptance 20. pont).

A Glosszárium Moodle-erőforrásként (PAGE-C) kerül a kurzusba; a leckék tanulói hivatkozásai erre mutassanak, ne a repository-fájlra.

## 3. Offline események és ajánlott útvonal

Az offline esemény **nem Moodle-activity**, ezért nem kap fiktív `cmid`-t. A Moodle-ben a hozzájuk kötött online tartalmat a §7 szerinti dátummal (HUM-OPS-01) vagy, ha később tényleges jelenléti checkpoint készül, annak igazolt completionjével nyitjuk.

| Esemény | Helye az útvonalban |
|---|---|
| **M0.A** | M0.1–M0.2 → **M0.A** → M0.3–M0.4 + fórum + belépőkvíz |
| **M1.A / M1.B** | M1.1–M1.2 → **M1.A** → M1.3–M1.4 + beadandó → **M1.B** |
| **M2.A / M2.B** | M2.1–M2.2 → **M2.A** → M2.4 → M2.3 → **M2.B** → identitás-jegyzet |
| **M3.A / M3.B** | M3.1–M3.2 → **M3.A** → M3.3–M3.4 → **M3.B** → produktum + kapukvíz |
| **M4.A / M4.B** | M4.1–M4.2 → **M4.A** → M4.3–M4.4 → **M4.B** → végleges peulabemutató-beadandó |
| **M5.A / M5.B** | M5.1–M5.2 → **M5.A** → M5.3–M5.4 → **M5.B** → produktum + diagnosztikus kvíz |
| **M6.A / M6.B** | M6.1–M6.2 → **M6.A** → M6.3–M6.4 → **M6.B** → játéklap + diagnosztikus kvíz |
| **M7.A / M7.B** | M7.1–M7.2 → **M7.A** → M7.3–M7.4 → **v1** → **M7.B** → külön revízió → **v2**; a felkészültségi kvíz a v1 leadása után nyílik (nem a v1 mentori megerősítése után), ajánlott még az M7.B előtt teljesíteni, és a megerősített eredménye a v2 leadásának feltétele |
| **Z.A** | Z.1–Z.3 → **Z.A** → Z.4 reflexió + Moodle Feedback |

A kikényszerített feltétel mindig a §2 „Unlock / előfeltétel” oszlopa; ahol az eltér a fenti útvonaltól, a §2 az irányadó. Az LMS-M3-05 leadásának az M3.B nem formális előfeltétele, csak erősen ajánlott (M3 KAPU §0); az LMS-M5-06 és az LMS-M6-06 már az M5.4, illetve az M6.4 után nyílik.

A felzárkóztató peulák (F-peulák, `.F`) a nem teljesült kapu utáni javítási alkalmak; a puszta lemaradás pótlására a Csendes pótlás szolgál (a két fogalmat a Program terv és a Glosszárium definiálja). Projektgazdai döntés (2026-10-02): az éles kapu (M1, M3, M5, M6, M7) sikertelensége után az F-peula kötelező, puha kapunál (M2, M4) ajánlott. Időpontja a kapueredmény megerősítése után, a javító próbálkozás előtt van; a képző jelöli ki a §7 központi naptára szerint. Az F-peulák nem kapuznak, és nem lehetnek az egyetlen tartalék hozzáférési utak.

## 4. Modul-completion és downstream unlock

| Modul | Megerősített modul-completion | Következmény |
|---|---|---|
| M0 | M0.1–M0.4 + Bemutatkozó fal 1 új téma/1 válasz + belépőkvíz kitöltve (mind a 7 item megválaszolva) | M1 nyitható |
| M1 | H5P-k + LMS-M1-05 mastery | M2 nyitható |
| M2 | H5P-k + érdemi identitás-jegyzet | M3 nyitható |
| M3 | H5P-k + LMS-M3-05 mastery + LMS-M3-06 mastery | M4 nyitható |
| M4 | H5P-k + érdemi, nem üres peulabemutató-vázlat (LMS-M4-05; a kijelölt mentor/értékelő erősíti meg, hogy nem üres) | M5 nyitható; az 5 sablonelemre épülő „Alapszint / rendben” küszöb formatív visszajelzés, az M5 nyitásának nem feltétele (a puha kapu nem blokkol, Program terv §5) |
| M5 | H5P-k (az LMS-M5-07 nélkül) + LMS-M5-05 mastery + diagnosztikus kvíz kitöltve | M6 nyitható; az LMS-M5-07 késleltetett felidézés az M6 nyitásának nem feltétele, az online félév teljesítéséhez viszont kell |
| M6 | H5P-k + LMS-M6-05 mastery + diagnosztikus kvíz kitöltve | M7 nyitható |
| M7 | H5P-k + v1 folyamat + LMS-M7-07 mastery (a v2 előtt) + LMS-M7-06 mastery | Z nyitható |
| Z | Z.1–Z.4 + Moodle Feedback | online félév teljesítve (ha az LMS-M5-07 is teljesült); **Program teljesítve = Online félév teljesítve ÉS Terepgyakorlat teljesítve** (a terepgyakorlat külön folytatás) |

**Fontos:** M1, M3, M5, M6 és M7 összetett kapuinál a nyers pontszám önmagában nem nyithat downstream tartalmat. Ha Moodle-ben az összetett feltétel nem kódolható bizonyítottan, egy `GATE_CONFIRMED_<module>` kézi/stáb-checkpointot kell létrehozni és a downstream restrict access ehhez kötni; a választott mechanizmust az `LMS – H5P runtime acceptance.md` 8. pontja szerint verzióval és bizonyítékkal kell rögzíteni. A puha kapuknál (az M2 identitás-jegyzeténél, LMS-M2-05, és az M4 peulabemutató-vázlatánál, LMS-M4-05), valamint minden további ASSIGN-S beadásnál nem completion a puszta leadás, az üres vagy kitöltetlen sablon, illetve a puszta fájlfeltöltés: az előírt mezőkben tényleges, minimálisan értelmezhető tartalom kell, ezt a kijelölt mentor/értékelő erősíti meg, és ha ez nem kódolható bizonyítottan, ugyanez a checkpoint-út érvényes. A puha kapuk rubrika-küszöbe (az M2-nél az M2 KAPU rubrikája, az M4-nél az 5 sablonelemre épülő „Alapszint / rendben” szint, M4 hub §6) formatív visszajelzés: nem completion- és nem nyitási feltétel, mert a puha kapu nem blokkol (Program terv §5). Az M7-ben a felkészültségi kvíz (LMS-M7-07) megerősített eredménye nyitja meg a v2 leadását (LMS-M7-06); ha a kvíz összetett feltétele nem kódolható bizonyítottan, a v2 restrict accessét is kézi stáb-checkpointhoz kell kötni.

**A kapueredmény megerősítésének határideje (HUM-OPS-01):** projektgazdai döntés (2026-10-02); utólagos ellenőrzés (vétó/QA): a programvezető. A kapu eredményét legkésőbb 24 órával a következő fix alkalom előtt meg kell erősíteni. Pénteki A-peula esetén: beadás szerda 18:00-ig, első értékelés csütörtök délután, megerősítés legkésőbb csütörtök 18:00-ig. A függőben lévő (még nem megerősített) eredmény nem bukás. A naptári dátumokat a §7 központi ütemezése adja (HUM-OPS-01).

**Kétszemes döntés (Program terv §5):** az M3 (R2, R4) és az M7 (R1, R4, R5, R6) blokkoló sorainál a „javításra megy / blokkol” kimenet kétszemes: mentor + második képző, az M3-nál a Memuna is. E két kapunál a kapu-szezon előtt az értékelők közösen átbeszélik a rubrikát, és 1–2 referenciamintát együtt pontoznak.

**Újraértékelés (Program terv §5):** M1, M3, M5, M6 és M7 esetén a madrich kérheti, hogy az eredeti értékelőtől eltérő második képző a downstream feloldás előtt átnézze a beadást és a kapudöntést; a megerősített kapueredmény ennek nyomán módosulhat. M3/M7 biztonságkritikus vitánál a Memunát is be kell vonni.

## 5. `moodle-ai-mcp` Core 1.0 képességmátrix

Az implementáció alapja a `neongodio/moodle-ai-mcp` **Core 1.0** állapota, a 2026-09-25-i sign-off után.

| Feladat | Út |
|---|---|
| szakaszok; Page, URL, File, Folder, Text and media, H5P, Quiz, Assignment, general Forum, Choice létrehozása | **MCP** |
| quiz-kérdések létrehozása; H5P telepített típus/séma lekérdezése | **MCP** |
| course completion bekapcsolása, generikus activity completion, passing grade, Assignment maximum, Assignment-dátumok, Quiz időablak | **MCP**, majd visszaolvasás |
| **Assignment advanced grading / rubric létrehozása** | **MANUAL FALLBACK** – a jelenlegi MCP-ben nem tervezett write-surface |
| egyedi értékelési skála létrehozása (pl. a Z.4 pont nélküli skálája; a címkéket a Z.4 adja) | **MANUAL FALLBACK** – nem szerepel a fenti MCP-képességek között |
| **Restrict access / availability prerequisite beállítása** | **MANUAL FALLBACK** – a létrehozó toolok nem konfigurálják |
| **Moodle Feedback activity** | **MANUAL FALLBACK** – nincs a támogatott 10 létrehozható activity-típus között |
| Forum „1 új téma + 1 válasz” modul-specifikus completion | **MANUAL FALLBACK**, majd course inspect |
| H5P, amely saját image/audio/video fájlt ágyaz a content params-ba | **MANUAL FALLBACK / előre elkészített H5P**, mert a programozott H5P file-ingress nem támogatott |
| meglévő H5P tartalom revíziója | **MANUAL / új tartalom + activity újrakötés**, a jelenlegi MCP nem ad biztonságos revision write-ot |
| böngészőszintű vizuális/a11y QA, screen reader, mobil, zoom, billentyűzet | **RUNTIME ACCEPTANCE**, nem MCP |
| learner grade vagy per-user completion írása | **NEM TÁMOGATOTT**, nem kerül workarounddal automatizálásra |

**M6 első kiadás:** nincs Moodle Workshop-függőség. A társas visszajelzés az M6.B élő peulán történik, a játéklap Moodle **Assignment**, a blokkoló feltétel végső értékelője mentor/képző.

## 6. Build és visszaaudit protokoll

1. `moodle_site_inspect`: Moodle build, pluginok, H5P library-verziók rögzítése.
2. Szakaszok és activityk létrehozása **rejtett stagingben**.
3. Minden létrehozás után `build_id ↔ cmid` kötés rögzítése.
4. MCP-vel támogatott completion/grade/dátum beállítás.
5. A §5 szerinti manuális fallbackek elvégzése Moodle UI-ban.
6. `moodle_course_inspect` + `moodle_activity_inspect`: név, típus, sorrend, completion, grade visszaolvasása.
7. Manuális screenshot/tesztjegyzőkönyv a rubrikáról és restrict-access szabályról.
8. Tesztfiókokkal az `LMS – H5P runtime acceptance.md` végrehajtása.
9. Csak sikeres runtime teszt és G1–G8 release-gate után nyitható meg valódi madrichnak. A release-hatókörű jogi és gyermekvédelmi médiakapuknak is zárva kell lenniük, vagy az érintett assetet el kell távolítani, illetve helyettesíteni (`Emberi jóváhagyás szükséges.md` §5: projektgazdai döntés, 2026-10-02; utólagos ellenőrzés (vétó/QA): a release owner és a jogi/adatvédelmi felelős).

## 7. Központi ütemezés (V1, HUM-OPS-01)

Projektgazdai döntés (2026-10-02); utólagos ellenőrzés (vétó/QA): a programvezető. Ez a szakasz a Moodle-dátumok (nyitás, határidő) egyetlen forrása; a §2 `schedule_key` oszlopa erre hivatkozik. Indulás: 2026-11-06 (péntek), zárás: 2027-03-05 (péntek). Modulonként az első péntek az A-peula, a második a B-peula.

| Elem | Péntek(ek) | Kapu-beadás | Megerősítés |
|---|---|---|---|
| M0 | 2026-11-06 | 2026-11-11 18:00 | 2026-11-12 18:00 |
| M1 | 2026-11-13, 2026-11-20 | 2026-11-25 18:00 | 2026-11-26 18:00 |
| M2 | 2026-11-27, 2026-12-04 | 2026-12-09 18:00 | 2026-12-10 18:00 |
| M3 | 2026-12-11, 2026-12-18 | 2027-01-06 18:00 | 2027-01-07 18:00 |
| Téli szünet | 2026-12-25, 2027-01-01 | nincs | nincs |
| M4 | 2027-01-08, 2027-01-15 | 2027-01-20 18:00 | 2027-01-21 18:00 |
| M5 | 2027-01-22, 2027-01-29 | 2027-02-03 18:00 | 2027-02-04 18:00 |
| M6 | 2027-02-05, 2027-02-12 | 2027-02-17 18:00 | 2027-02-18 18:00 |
| M7 | 2027-02-19, 2027-02-26 | 2027-03-03 18:00 | 2027-03-04 18:00 |
| Z | 2027-03-05 | Z completion: 2027-03-10 18:00 | 2027-03-11 |

**Levezetett M7-pontok** (a projektgazda szabályából levezetve, nem külön megadott dátumok):

- a Peula v1 beadása (`M7_V1_DUE`): 2027-02-24 18:00 (szerda az M7.B előtt);
- a kijelölt mentor rubrikás visszajelzése a v1-re: 2027-02-25 18:00-ig;
- az M7 felkészültségi kvíz (`M7_QUIZ`) a v1 beadása után nyílik, ajánlott még az M7.B (2027-02-26) előtt teljesíteni, és a v2 beadása (2027-03-03 18:00) előtt kötelező.

**További ütemezett pontok:**

- az M4.A (2027-01-08) és az M4.B (2027-01-15) előtt 24 órával Moodle-értesítő megy ki (HUM-PED-01);
- az M5.3 késleltetett felidézése (LMS-M5-07) relatív: az M5.3 teljesítése után 72 órával nyílik, naptári dátuma nincs.

**A `schedule_key` értékei.** A „Nyitás” oszlop a dátumhoz kötött nyitást adja; ahol „§2 szerint” áll, ott a nyitás feltétele a §2 „Unlock / előfeltétel” oszlopa. A „—” határidő azt jelenti, hogy nincs külön határidő: az elem a §4 szerinti modul-completion része. A §3 ajánlott útvonala (a leckék az adott peula előtt) ajánlás, nem határidő.

| `schedule_key` | Nyitás | Határidő |
|---|---|---|
| `M0_L1`, `M0_L2` | §2 szerint | — |
| `M0_L3`, `M0_L4` | 2026-11-06, az M0.A után (`M0_L4`: §2 szerint) | — |
| `M0_FORUM`, `M0_QUIZ` | §2 szerint | 2026-11-11 18:00 (az M0 kapu-beadása) |
| `M1_L1`, `M1_L2` | §2 szerint | — |
| `M1_L3`, `M1_L4` | 2026-11-13, az M1.A után (`M1_L4`: §2 szerint) | — |
| `M1_ASSIGN` | §2 szerint | 2026-11-25 18:00 |
| `M2_L1`, `M2_L2` | §2 szerint | — |
| `M2_L4` (M2.4), `M2_L3` (M2.3) | 2026-11-27, az M2.A után (`M2_L3`: §2 szerint) | — |
| `M2_ASSIGN` | 2026-12-04, az M2.B után | 2026-12-09 18:00 |
| `M3_L1`, `M3_L2` | §2 szerint | — |
| `M3_L3`, `M3_L4` | 2026-12-11, az M3.A után (`M3_L4`: §2 szerint) | — |
| `M3_ASSIGN`, `M3_QUIZ` | §2 szerint | 2027-01-06 18:00 (az M3 kapu-beadása; az `M3_QUIZ`-nál levezetett) |
| `M4_L1`, `M4_L2` | §2 szerint | — |
| `M4_L3`, `M4_L4` | 2027-01-08, az M4.A után (`M4_L4`: §2 szerint) | — |
| `M4_ASSIGN` | 2027-01-15, az M4.B után | 2027-01-20 18:00 |
| `M5_L1`, `M5_L2` | §2 szerint | — |
| `M5_L3`, `M5_L4` | 2027-01-22, az M5.A után (`M5_L4`: §2 szerint) | — |
| `M5_ASSIGN` | 2027-01-29, az M5.B után | 2027-02-03 18:00 |
| `M5_QUIZ` | §2 szerint | — |
| `M6_L1`, `M6_L2` | §2 szerint | — |
| `M6_L3`, `M6_L4` | 2027-02-05, az M6.A után (`M6_L4`: §2 szerint) | — |
| `M6_ASSIGN` | 2027-02-12, az M6.B után | 2027-02-17 18:00 |
| `M6_QUIZ` | §2 szerint | — |
| `M7_L1`, `M7_L2` | §2 szerint | — |
| `M7_L3`, `M7_L4` | 2027-02-19, az M7.A után (`M7_L4`: §2 szerint) | — |
| `M7_V1_DUE` | §2 szerint | 2027-02-24 18:00 (levezetett) |
| `M7_QUIZ` | a v1 beadása után (§2) | a v2 beadása előtt kötelező, legkésőbb 2027-03-03 18:00 (levezetett); ajánlott az M7.B (2027-02-26) előtt |
| `M7_V2_DUE` | 2027-02-26, az M7.B után, a §2 további feltételeivel | 2027-03-03 18:00 |
| `Z_L1`, `Z_L2`, `Z_L3` | §2 szerint | — |
| `Z_REFLECTION`, `Z_FEEDBACK` | 2027-03-05, a Z.A után | 2027-03-10 18:00 (Z completion) |
