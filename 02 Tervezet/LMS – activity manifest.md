# LMS – activity manifest

> **Kánoni build-szerződés.** Ebből a fájlból a következő implementációs agentnek nem kell pedagógiai prózát újraértelmeznie.
>
> - `build_id`: repository-szintű stabil azonosító.
> - `cmid`: **BUILD_OUTPUT**, a Moodle létrehozás után visszaadott course-module ID. Nem emberi döntés és nem placeholder.
> - Dátumok: kizárólag a **HUM-OPS-01** központi ütemezésből származnak. A fájlban nincs kitalált naptári dátum.
> - A táblázat csak **tényleges Moodle-activityket** sorol. Az offline peulák sorrendje külön táblában van.
> - A `completion` és a `mastery` két külön mező. A megnyitás/végigkattintás soha nem helyettesít mastery-feltételt.

## 1. Megvalósítási profilok

| Profil | Típus | Alapértelmezett completion | Grade / pass | Retry | Mentor-láthatóság | Privacy | A11y / fallback |
|---|---|---|---|---|---|---|---|
| **H5P-C** | H5P activity | automatikus, a forrásban előírt interakció(k) érdemi befejezése; puszta megtekintés nem elég, ha a lecke választ kér | nincs mastery-küszöb | újranyitható | completion + aggregált eredmény, személyes reflexió tartalma csak ha a forrás ezt kifejezetten indokolja | **P1** fiókhoz kötött teljesítési adat; személyes szabad szöveg lehetőleg ne kerüljön H5P-be | WCAG 2.2 AA pre-flight; húzásmentes út; felirat/leirat; alacsony adatú szöveges út |
| **QUIZ-D** | Moodle Quiz, diagnosztikus | attempt submitted | nincs blokkoló pass | a forrás szerinti, egyébként 2–3 | item-analitika | **P1** teljesítési adat | billentyűzet, mobil, zoom; nincs drag-only item |
| **QUIZ-M** | Moodle Quiz, mastery | attempt submitted **és** az explicit pass-feltétel igazolt | explicit küszöb | a kapufájl szerint | eredmény + item-szintű review ott, ahol kritikus item van | **P1** teljesítési adat | mint QUIZ-D |
| **ASSIGN-S** | Moodle Assignment, puha/product completion | érdemi beadvány leadva | nincs kizáró küszöb; a forrás minimuma alatt javítás | újrabeadás engedett | mentor/képző | **P2** személyes tanulói produktum | online text **és** fájlút, hozzáférhető sablon |
| **ASSIGN-M** | Moodle Assignment, mastery | beadvány leadva **és** rubrika/mastery igazolt | explicit kapufeltétel | mastery-javítás | mentor/képző | **P2**, érzékeny tartalom bekérését kerülni | mint ASSIGN-S |
| **FORUM-C** | General Forum | előírt poszt + válasz | nincs grade | szerkeszthető a helyi beállítás szerint | kurzusrésztvevők látják | **P2-PUBLIC-IN-COURSE**; személyes/érzékeny adatot ne kérjen | billentyűzet, reflow; szöveges felület |
| **FEEDBACK-N** | Moodle Feedback | kitöltve | nincs grade | egyszer | eredmény a HUM-PRIV-03 szerint | **P2**, válaszok név nélkül jelenjenek meg; teljes anonimitást nem ígérünk | mobil + billentyűzet + screen reader |
| **PAGE-C** | Page / Text and media | megtekintés, csak ha valóban információátadás a cél | nincs | n/a | n/a | **P0–P1** | szemantikus címsorok, alt, reflow |

**Privacy osztályok:** `P0` nincs learner input; `P1` fiókhoz kötött teljesítési/értékelési adat; `P2` szabad szöveg vagy tanulói produktum; `P2-PUBLIC-IN-COURSE` a kurzus résztvevőinek látható tartalom; különleges vagy gyermekvédelmi adatot **egyik activity sem kér kötelezően**. Ha ilyen mégis megjelenik spontán, HUM-PRIV-01 és HUM-SAFE-01 szerint kell kezelni.

## 2. Tényleges Moodle-activityk

A `schedule_key` értékeit a HUM-OPS-01 zárása után a központi ütemezés tölti ki. `—` = nincs külön határidő.

| build_id | cmid | Szakasz | Név | Profil | Kötelező | Forrás | Unlock / előfeltétel | Completion | Mastery / pass | schedule_key | Megjegyzés |
|---|---|---|---|---|---:|---|---|---|---|---|---|
| LMS-M0-01 | BUILD_OUTPUT | M0 | M0.1 – Üdv a képzésben! | H5P-C | igen | M0/Online leckék/M0.1 | kurzushozzáférés | profil | nincs | M0_L1 | |
| LMS-M0-02 | BUILD_OUTPUT | M0 | M0.2 – Madrich, nem terapeuta | H5P-C | igen | M0/Online leckék/M0.2 | LMS-M0-01 | profil | nincs | M0_L2 | HUM-SAFE-03 kontaktblokk csak élesítéskor |
| LMS-M0-03 | BUILD_OUTPUT | M0 | M0.3 – Moodle, H5P és kapuk | H5P-C | igen | M0/Online leckék/M0.3 | **M0.A után nyílik dátummal**, nem jelenléti találgatással | profil | nincs | M0_L3 | |
| LMS-M0-04 | BUILD_OUTPUT | M0 | M0.4 – Dugma ishit online | H5P-C | igen | M0/Online leckék/M0.4 | LMS-M0-03 | profil | nincs | M0_L4 | |
| LMS-M0-05 | BUILD_OUTPUT | M0 | Bemutatkozó fal | FORUM-C | igen | M0.4 | LMS-M0-04 | **1 poszt + 1 válasz** | nincs | M0_FORUM | module-specific forum completion kézi beállítás |
| LMS-M0-06 | BUILD_OUTPUT | M0 | M0 belépő-kvíz | QUIZ-D | igen | M0 hub §5–6 + M0.3/M0.4 | LMS-M0-04 | kitöltve | **nincs cut-score**; ~60% csak stáb-jelző | M0_QUIZ | 6–8 item, kulcs a kánoni forrásból |
| LMS-M1-01 | BUILD_OUTPUT | M1 | M1.1 – Johari-ablak | H5P-C | igen | M1/Online leckék/M1.1 | **M0 complete** | profil | nincs | M1_L1 | |
| LMS-M1-02 | BUILD_OUTPUT | M1 | M1.2 – Megfigyelés ≠ értelmezés | H5P-C | igen | M1/Online leckék/M1.2 | LMS-M1-01 | profil | nincs | M1_L2 | drag-free egyenértékű út kötelező |
| LMS-M1-03 | BUILD_OUTPUT | M1 | M1.3 – SBI-modell | H5P-C | igen | M1/Online leckék/M1.3 | **M1.A után nyílik** | profil | nincs | M1_L3 | |
| LMS-M1-04 | BUILD_OUTPUT | M1 | M1.4 – Mondd el SBI-ben | H5P-C | igen | M1/Online leckék/M1.4 | LMS-M1-03 | profil | nincs | M1_L4 | a beadó külön activity |
| LMS-M1-05 | BUILD_OUTPUT | M1 | M1.4 – SBI-beadandó | ASSIGN-M | igen | M1.4 + M1 KAPU | LMS-M1-04 | leadva + megerősített kapueredmény | **minden rubrikasor ≥1 ÉS összesen ≥5/8** | M1_ASSIGN | rubric manual fallback, lásd §5 |
| LMS-M2-01 | BUILD_OUTPUT | M2 | M2.1 – Ki vagyok madrichként? | H5P-C | igen | M2/Online leckék/M2.1 | **M1 complete** | profil | nincs | M2_L1 | személyes reflexió lehetőleg learner-local |
| LMS-M2-02 | BUILD_OUTPUT | M2 | M2.2 – Értékeim mint iránytű | H5P-C | igen | M2/Online leckék/M2.2 | LMS-M2-01 | profil | nincs | M2_L2 | |
| LMS-M2-03 | BUILD_OUTPUT | M2 | M2.4 – Reflektív napló és határok | H5P-C | igen | M2/Online leckék/M2.4 | **M2.A után nyílik** | profil | nincs | M2_L4 | **szándékosan M2.3 előtt** |
| LMS-M2-04 | BUILD_OUTPUT | M2 | M2.3 – Somer 3 pillére | H5P-C | igen | M2/Online leckék/M2.3 | LMS-M2-03 | profil | nincs | M2_L3 | HUM-SOMER-01/03 érintett |
| LMS-M2-05 | BUILD_OUTPUT | M2 | M2 – Identitás-jegyzet | ASSIGN-S | igen | M2 KAPU | **M2.B után** | érdemi, 1 oldalas jegyzet leadva | puha kapu, fejlesztő rubrika; hiányosnál javítás | M2_ASSIGN | érzékeny történet nem kötelező |
| LMS-M3-01 | BUILD_OUTPUT | M3 | M3.1 – Történetek egy kvucáról | H5P-C | igen | M3/Online leckék/M3.1 | **M2 complete** | profil | nincs | M3_L1 | |
| LMS-M3-02 | BUILD_OUTPUT | M3 | M3.2 – Négy kvuca, négy világ | H5P-C | igen | M3/Online leckék/M3.2 | LMS-M3-01 | profil | nincs | M3_L2 | HUM-SOMER-02 |
| LMS-M3-03 | BUILD_OUTPUT | M3 | M3.3 – Gyermekvédelem 101 | H5P-C | igen | M3/Online leckék/M3.3 | HUM-SAFE-01/02 **élesben**; stagingben belső QA | profil | nincs | M3_L3 | szakértői signoff learner release előtt |
| LMS-M3-04 | BUILD_OUTPUT | M3 | M3.4 – Do / Don’t madrichként | H5P-C | igen | M3/Online leckék/M3.4 | LMS-M3-03 | profil | nincs | M3_L4 | |
| LMS-M3-05 | BUILD_OUTPUT | M3 | M3 – Helyzetelemzés | ASSIGN-M | igen | M3.4 + M3 KAPU | LMS-M3-04; M3.B erősen ajánlott | leadva + rubrika | minden sor ≥1; **R2 és R4 blokkoló** | M3_ASSIGN | mentor review |
| LMS-M3-06 | BUILD_OUTPUT | M3 | M3 – Gyermekvédelmi kapukvíz | QUIZ-M | igen | M3 KAPU | LMS-M3-05 | attempt + megerősített eredmény | **≥10/12 ÉS Q2/Q4/Q7/Q9 mind helyes** | M3_QUIZ | összetett feltétel manual/runtime fallback |
| LMS-M4-01 | BUILD_OUTPUT | M4 | M4.1 – Mit üzen a testem? | H5P-C | igen | M4/Online leckék/M4.1 | **M3 complete** | forrás szerinti 2 reflexióval | nincs | M4_L1 | |
| LMS-M4-02 | BUILD_OUTPUT | M4 | M4.2 – Aktív hallgatás | H5P-C | igen | M4/Online leckék/M4.2 | LMS-M4-01 | forrás szerinti saját mondattal | nincs | M4_L2 | |
| LMS-M4-03 | BUILD_OUTPUT | M4 | M4.3 – Kérdezési minták | H5P-C | igen | M4/Online leckék/M4.3 | **M4.A után** | mini-kvíz + reflexió | diagnosztikus | M4_L3 | |
| LMS-M4-04 | BUILD_OUTPUT | M4 | M4.4 – 45 mp-es peula-pitch | H5P-C | igen | M4/Online leckék/M4.4 | LMS-M4-03 | H5P befejezve | nincs | M4_L4 | |
| LMS-M4-05 | BUILD_OUTPUT | M4 | M4.4 – Peula-pitch váz | ASSIGN-S | igen | M4.4 + M4 hub §6 | **M4.B után** | 5 sablonelem azonosítható | puha kapu; hiányosnál mentor + újrabeadás | M4_ASSIGN | társas visszajelzés a leadás előtt |
| LMS-M5-01 | BUILD_OUTPUT | M5 | M5.1 – Mi a nonformális nevelés? | H5P-C | igen | M5/Online leckék/M5.1 | **M4 complete** | profil | nincs | M5_L1 | |
| LMS-M5-02 | BUILD_OUTPUT | M5 | M5.2 – Feladat → cél → kvuca → módszer | H5P-C | igen | M5/Online leckék/M5.2 | LMS-M5-01 | profil | nincs | M5_L2 | |
| LMS-M5-03 | BUILD_OUTPUT | M5 | M5.3 – Hogyan tanulunk tényleg? | H5P-C | igen | M5/Online leckék/M5.3 | **M5.A után** | profil | nincs | M5_L3 | Dialog Cards runtime teszt |
| LMS-M5-04 | BUILD_OUTPUT | M5 | M5.4 – Cél–kvuca–módszer mini-táblázat | H5P-C | igen | M5/Online leckék/M5.4 | LMS-M5-03 | profil | nincs | M5_L4 | |
| LMS-M5-05 | BUILD_OUTPUT | M5 | M5.4 – Modulproduktum | ASSIGN-M | igen | M5.4 + M5 KAPU | **M5.B után** | leadva + rubrika | minden sor ≥ Alapszint; **R4 Hiányos = javítás** | M5_ASSIGN | |
| LMS-M5-06 | BUILD_OUTPUT | M5 | M5 – Fogalmi önellenőrzés | QUIZ-D | igen | M5 KAPU | LMS-M5-04 | kitöltve | ≥10/12 csak diagnosztikus jelző | M5_QUIZ | 2–3 próbálkozás |
| LMS-M6-01 | BUILD_OUTPUT | M6 | M6.1 – Játék-kategóriák 4 kvucára | H5P-C | igen | M6/Online leckék/M6.1 | **M5 complete** | profil | nincs | M6_L1 | |
| LMS-M6-02 | BUILD_OUTPUT | M6 | M6.2 – Történet mint tükör | H5P-C | igen | M6/Online leckék/M6.2 | LMS-M6-01 | profil | nincs | M6_L2 | |
| LMS-M6-03 | BUILD_OUTPUT | M6 | M6.3 – Kézműves, ami tanít is | H5P-C | igen | M6/Online leckék/M6.3 | **M6.A után** | profil | nincs | M6_L3 | fotó csak HUM-PRIV-02 szerint |
| LMS-M6-04 | BUILD_OUTPUT | M6 | M6.4 – Döntési szcenáriók | H5P-C | igen | M6/Online leckék/M6.4 | LMS-M6-03 | **legalább 3 külön eset tényleges teljesítése** | nincs | M6_L4 | runtime bizonyítandó |
| LMS-M6-05 | BUILD_OUTPUT | M6 | M6 – Játéklap | ASSIGN-M | igen | M6.B + M6 KAPU | **M6.B után** | leadva + mentor által megerősített rubrika | minden sor ≥2; **R4 és R5 blokkoló feltétel** | M6_ASSIGN | társas visszajelzés élőben, nem Moodle Workshop |
| LMS-M6-06 | BUILD_OUTPUT | M6 | M6 – Szcenárió-önellenőrzés | QUIZ-D | igen | M6 KAPU | LMS-M6-04 | kitöltve | ≥10/12 csak diagnosztikus jelző | M6_QUIZ | korlátlan újrapróbálás |
| LMS-M7-01 | BUILD_OUTPUT | M7 | M7.1 – SMART nevelési cél | H5P-C | igen | M7/Online leckék/M7.1 | **M6 complete** | profil | nincs | M7_L1 | |
| LMS-M7-02 | BUILD_OUTPUT | M7 | M7.2 – Peula 11 pont + AI | H5P-C | igen | M7/Online leckék/M7.2 | LMS-M7-01 | profil | nincs | M7_L2 | AI opcionális, no-AI út kötelező |
| LMS-M7-03 | BUILD_OUTPUT | M7 | M7.3 – Zmán Kvucá-checklist | H5P-C | igen | M7/Online leckék/M7.3 | LMS-M7-02 | profil | nincs | M7_L3 | |
| LMS-M7-04 | BUILD_OUTPUT | M7 | M7.4 – Peula v1 + AI | H5P-C | igen | M7/Online leckék/M7.4 | **M7.A után** | profil | nincs | M7_L4 | |
| LMS-M7-05 | BUILD_OUTPUT | M7 | Peula v1 – első vázlat | ASSIGN-S | igen | M7.4 | LMS-M7-04 | érdemi v1 leadva | formatív, nem buktat | **M7_V1_DUE** | v2-vel nem lehet azonos napon |
| LMS-M7-06 | BUILD_OUTPUT | M7 | Peula v2 + Zmán Kvucá | ASSIGN-M | igen | M7 KAPU | **LMS-M7-05 → M7.B → külön revíziós szakasz** | leadva + megerősített rubrika | **≥17/24 ÉS R1/R5/R6 ≥2 ÉS R4 ≥2** | **M7_V2_DUE** | 1 sor AI-használat vagy „nem használtam”; nem pontozott |
| LMS-M7-07 | BUILD_OUTPUT | M7 | M7 – Záró mastery-kvíz | QUIZ-M | igen | M7 KAPU | LMS-M7-06 | attempt + megerősített eredmény | **≥12/14 ÉS Q13 helyes** | M7_QUIZ | 2–3 próbálkozás |
| LMS-Z-01 | BUILD_OUTPUT | Z | Z.1 – Visszanéző tükör | H5P-C | igen | Z/Online leckék/Z.1 | **M7 complete** | profil | nincs | Z_L1 | |
| LMS-Z-02 | BUILD_OUTPUT | Z | Z.2 – Saját tanulási pillanataim | H5P-C | igen | Z/Online leckék/Z.2 | LMS-Z-01 | profil | nincs | Z_L2 | személyes részlet nem kötelező |
| LMS-Z-03 | BUILD_OUTPUT | Z | Z.3 – Híd a terepre | H5P-C | igen | Z/Online leckék/Z.3 | LMS-Z-02 | profil | nincs | Z_L3 | |
| LMS-Z-04 | BUILD_OUTPUT | Z | Z.4 – Záró reflexió | ASSIGN-S | igen | Z.4 | **Z.A után, schedule restrictionnel** | érdemi reflexió leadva | completion, nem vizsga | Z_REFLECTION | draft/resume runtime test |
| LMS-Z-05 | BUILD_OUTPUT | Z | Képzés-visszajelzés | FEEDBACK-N | igen | Z.4 | Z.A után | kitöltve | nincs | Z_FEEDBACK | HUM-PRIV-03; MCP-ben manuális létrehozás |

## 3. Offline események és kötelező sorrend

Az offline esemény **nem Moodle-activity**, ezért nem kap fiktív `cmid`-t. A Moodle-ban a hozzájuk kötött online tartalmat a HUM-OPS-01 szerinti dátummal vagy, ha később tényleges jelenléti checkpoint készül, annak igazolt completionjével nyitjuk.

| Esemény | Helye az útvonalban |
|---|---|
| **M0.A** | M0.1–M0.2 → **M0.A** → M0.3–M0.4 + fórum + belépő-kvíz |
| **M1.A / M1.B** | M1.1–M1.2 → **M1.A** → M1.3–M1.4 + beadó → **M1.B** |
| **M2.A / M2.B** | M2.1–M2.2 → **M2.A** → M2.4 → M2.3 → **M2.B** → identitás-jegyzet |
| **M3.A / M3.B** | M3.1–M3.2 → **M3.A** → M3.3–M3.4 → **M3.B** → produktum + kapukvíz |
| **M4.A / M4.B** | M4.1–M4.2 → **M4.A** → M4.3–M4.4 → **M4.B** → végleges pitch-beadó |
| **M5.A / M5.B** | M5.1–M5.2 → **M5.A** → M5.3–M5.4 → **M5.B** → produktum + diagnosztikus kvíz |
| **M6.A / M6.B** | M6.1–M6.2 → **M6.A** → M6.3–M6.4 → **M6.B** → játéklap + diagnosztikus kvíz |
| **M7.A / M7.B** | M7.1–M7.4 → **M7.A** → **v1** → **M7.B** → külön revízió → **v2** → mastery-kvíz |
| **Z.A** | Z.1–Z.3 → **Z.A** → Z.4 reflexió + Feedback |

A `.F` Study Labek támogatási utak. Nem kapuznak és nem lehetnek az egyetlen hozzáférési fallbackek.

## 4. Modul-completion és downstream unlock

| Modul | Megerősített modul-completion | Következmény |
|---|---|---|
| M0 | M0.1–M0.4 + Bemutatkozó fal 1 poszt/1 válasz + belépő-kvíz kitöltve | M1 nyitható |
| M1 | H5P-k + LMS-M1-05 mastery | M2 nyitható |
| M2 | H5P-k + érdemi identitás-jegyzet | M3 nyitható |
| M3 | H5P-k + LMS-M3-05 mastery + LMS-M3-06 mastery | M4 nyitható |
| M4 | H5P-k + érdemi pitch | M5 nyitható |
| M5 | H5P-k + LMS-M5-05 mastery + diagnosztikus kvíz kitöltve | M6 nyitható |
| M6 | H5P-k + LMS-M6-05 mastery + diagnosztikus kvíz kitöltve | M7 nyitható |
| M7 | H5P-k + v1 folyamat + LMS-M7-06 mastery + LMS-M7-07 mastery | Z nyitható |
| Z | Z.1–Z.4 + Feedback | online félév complete; terepgyakorlat külön folytatás |

**Fontos:** M1, M3, M6 és M7 összetett kapuinál a nyers pontszám önmagában nem nyithat downstream tartalmat. Ha Moodle-ban az összetett feltétel nem kódolható bizonyítottan, egy `GATE_CONFIRMED_<module>` kézi/stáb-checkpointot kell létrehozni és a downstream restrict access ehhez kötni.

## 5. `moodle-ai-mcp` Core 1.0 képességmátrix

Az implementáció alapja a `neongodio/moodle-ai-mcp` **Core 1.0** állapota, a 2026-09-25-i sign-off után.

| Feladat | Út |
|---|---|
| szakaszok; Page, URL, File, Folder, Text and media, H5P, Quiz, Assignment, general Forum, Choice létrehozása | **MCP** |
| quiz-kérdések létrehozása; H5P telepített típus/séma lekérdezése | **MCP** |
| course completion bekapcsolása, generikus activity completion, passing grade, Assignment maximum, Assignment-dátumok, Quiz időablak | **MCP**, majd visszaolvasás |
| **Assignment advanced grading / rubric létrehozása** | **MANUAL FALLBACK** – a jelenlegi MCP-ben nem tervezett write-surface |
| **Restrict access / availability prerequisite beállítása** | **MANUAL FALLBACK** – a létrehozó toolok nem konfigurálják |
| **Moodle Feedback activity** | **MANUAL FALLBACK** – nincs a támogatott 10 létrehozható activity-típus között |
| Forum „1 poszt + 1 válasz” modul-specifikus completion | **MANUAL FALLBACK**, majd course inspect |
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
8. Tesztfiókokkal a `LMS – H5P runtime acceptance.md` végrehajtása.
9. Csak sikeres runtime teszt és G1–G8 release-gate után nyitható meg valódi madrichnak.
