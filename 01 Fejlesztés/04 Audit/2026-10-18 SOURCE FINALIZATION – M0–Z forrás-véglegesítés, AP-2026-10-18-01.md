# SOURCE FINALIZATION – M0–Z forrás-véglegesítés (AP-2026-10-18-01)

> **Audit trail, nem kánon.** A projektgazda 2026-10-18-i végrehajtási utasítása (`2026-10-18 Projektgazdai végrehajtási
> utasítás – M0–Z forrás-véglegesítés, AP-2026-10-18-01.md`) 13. pontja szerinti záró riport. Nem release-, runtime-, DPO-,
> Memuna-, jogi, hozzáférhetőségi vagy értékelési jóváhagyás. Tételes nyilvántartás: `AUTOPILOT-LEDGER.md`; deduplikált
> regiszter: `2026-10-18 Forrás-hibaregiszter – builder-bizonyíték és célzott QA, AP-2026-10-18-01.md`; nyers bizonyíték:
> `2026-10-18 Builder-bizonyíték – nyers kivonatok, AP-2026-10-18-01.md`.

## A. Vezetői verdikt

| | |
|---|---|
| Kiinduló forrás | `c354f17` (main), rá merge-dzsel a HUM 20. szakasz (`f96ce43`, PR #31 ága); a futás indító commitja `38538ed` |
| Záró forrás | `73a7f4e` (az utolsó `02 Tervezet/` és `tools/` változás); a ledger lezárása `131001d`; ez a riport külön commitban |
| Ág | `next-version/AP-2026-10-18-01`, csak helyi commitok; push, PR, merge nem történt |
| Forrásállapot | A négy forrás-blokkolt activity tanulói forrása elkészült és célzott QA-n átment. A futás minden olyan forráshibáját javítottuk, amelyet a kánonból bizonyítani lehetett (23 tétel `FIXED`). Ahol egy érték nem dönthető el a kánonból, ott javaslat (`PROPOSED`) készült, döntés nem. |
| Verdiktek (`5fa743c`) | `MOODLE-BUILD-VERDICT: NOT_READY` (BSPEC-08, -09, -10, -11 nyitott) · `LEARNER-RELEASE-VERDICT: NO-GO` |
| Ledger | `AUTOPILOT-LEDGER: TERMINAL`, kilépési kód 0; `AUTOPILOT-RESULT: OPEN_ITEMS_REMAIN` (javítva 23, emberi döntésre vár 130, bizonyítékra vár 59) |

**Ami elkészült:**
- A builder-bizonyíték (mk-coursebuild `bd00920`) egyeztetése a forrással, egyetlen deduplikált regiszterben.
- A négy blokkoló pótlása:
  - LMS-M5-01: kulcs, visszajelzés, completion.
  - LMS-M5-05: teljes feladatleírás, R4-cella.
  - LMS-M6-05: feladatleírás.
  - LMS-M7-06: feladatleírás és egységes sablon-specifikáció.
- A HUM 20. szakasz (CB-C-0036) átvezetése: M0.1 = Interactive Book + Feedback, M0.2 = natív Moodle Lecke.
- A GATE-CP kurzusteljesítési hiba (CB-C-0018, P0) javítása.
- Javítva a nyitási logika is: egy újranyitott Assignment-próbálkozás nem zárja vissza a már megnyílt tartalmat (QA-IMPL-1).
- Kvíz-bevezetők, a GATE-CP tanulói leírása, a „Segítség és kapcsolatok” blokk tanulói szövege, a TEXT-C tájékoztató-sablon, a Glosszárium megjelenítési szabálya.
- Három független QA-kör, összesen 132 tétel: a blokkoló-diff célzott QA-ja, a QA2 és a záró regressziós QA (QF).
- A 161 átvett ledger-tétel újraellenőrzése.

**Ami az autonóm forrásmunkán kívül marad:**
- A build-spec számértékei és beállításai (BSPEC-08…11).
- A szerzői, Memuna-, DPO-, programvezetői és értékelési döntések és jóváhagyások.
- Minden runtime-bizonyíték.
- A VO-újrarenderelés.
- A felhasználói átnevezés (TECH-2).
- A release-engedély.

## B. Változások modulonként

| Modul | Előtte → utána (röviden) | Fő fájlok | ID-k | Haszon (tanuló / képző) | Commit |
|---|---|---|---|---|---|
| M0 | M0.1: CP-összefoglaló diás completion → IB + kötelező háromoldalas Feedback (passzválasz a SLIDE 4-en, szerzői jóváhagyásig nem élesíthető); M0.2: CP → natív Lecke, négy kötelező kérdésoldal; a könyv → kérdőív átadás és a záró mondat; Lesson-a11y; belépőkvíz-bevezető | M0.1, M0.2, M0 hub | CB-C-0036 (HUM 20), QF-PED-1, -4, QF-BIZT-1, -3, BSPEC-10, -11 | a tanuló tudja, hol teljesül a lecke; a hibás válasz is teljesít; a nyitott DPO-/Memuna-feltétel minden érintett helyen látszik | `73f30ca`, `17905fd`, `f009c9b` |
| M1 | M1.3 ellentmondó írási instrukció → egy út (szövegmező + saját jegyzet) | M1.3 | A4, QF-NYELV-17 | nem kell kitalálni, hova kell írni | `139bc24`, `f009c9b` |
| M2 | a formatív küszöb „elfogadva” megnevezése → „formatív küszöb teljesül” (számok változatlanok) | M2 KAPU, M2 hub | CB-C-0016 | a puha kapu nem tűnik éles elfogadásnak | `139bc24` |
| M3 | M3.2, M3.3 és M3.4 tanulói szövege (belső kód, törött félkövér, rádiógombos instrukció) | M3.2, M3.3, M3.4 | A3, A12, C | tiszta tanulói felület | `139bc24` |
| M4 | húzásmentes út instrukciója (M4.2, M4.3); M4.3 S1 korrekciós visszajelzés, kategóriánként a harmadik kártya; a célzóna-visszajelzés az oszlopról szól (H5P-szemantika); AI-provenance-jegyzet | M4.2, M4.3 | A1, B, QF-ERT-1, QF-PED-2, QF-IMPL-3 | billentyűzettel is teljesíthető; a visszajelzés nem tanít fordítottat | `139bc24`, `f009c9b` |
| M5 | M5.1 SLIDE 2 kulcs és válaszonkénti visszajelzés, completion-sor; M5.4 4. szakasz: teljes feladatleírás és beállítás; M5 KAPU R4-cellák; kvíz-bevezető | M5.1, M5.4, M5 KAPU, M5 hub | LMS-M5-01, LMS-M5-05, BSPEC-08, QA-ERT/PED/NYELV, QF-NYELV-7…11, -19 | a tanuló látja a feladatot, a minimumot, a leadást és a javítási utat; a kulcs az M5.A-val egyezik | `709423b`, `17905fd`, `f009c9b` |
| M6 | M6 KAPU (E): teljes Játéklap-leírás és beállítás; M6.3 írási helyek; kvíz-bevezető; a javítási ág ütemezése | M6 KAPU, M6 hub, M6.3 | LMS-M6-05, QA-ERT-2, QF-PED-6, QF-NYELV-11, -12, -18 | a blokkoló sorok (biztonság, inkluzivitás) a tanuló felé is ki vannak mondva | `709423b`, `139bc24`, `17905fd`, `f009c9b` |
| M7 | M7 KAPU (D): teljes Peula v2-leírás, egységes sablon (D2, M7-HUB-MUNK-02), beállítás; R8 0. szint értékelői jegyzete GYV-11-gyel; M7.3-MUNK-01; M7.4 S3 választó; felkészültségi kvíz bevezetője; a javítási ág határideje | M7 KAPU, M7 hub, M7.3, M7.4, M7.B | LMS-M7-06, IMPL-18-1, CB-C-0035, QA-BIZT-1…3, QF-PED-6, QF-NYELV-13…15, -20 | v1 ↔ v2 különbség, három nyitási feltétel, R4 0. szint tanulói nyelven | `709423b`, `139bc24`, `17905fd`, `f009c9b`; média `62eb098`, `73a7f4e` |
| Z | Z.1–Z.4 tanulói szöveg (kérdés ↔ vezérlő, írási hely, modullista forrása) | Z.1–Z.4 | A7, A13, CB-C-0012 | egyértelmű feladat | `139bc24` |
| Kánon | manifest: GATE-CP completion, §4 nyitás, LESSON profil, H5P-C kivétel, BSPEC-08…11, Segítség-blokk, Glosszárium-szabály, CB-C-0034; runtime acceptance 8, 9, 19, 31 és RT-P0-31; Adatvédelem §3, §11.1; RELEASE-READINESS G1, G2, G5b; Glosszárium :81 | manifest, RA, Adatvédelem, RELEASE-READINESS, Glosszárium | CB-C-0018, QA-IMPL-1, HUM 20, QF-ERT-3, -4, QF-IMPL-1, -4…7 | a build nem tud bukott kaput teljesítettnek venni; a nyitott feltételek a kapukban is látszanak | `b2c0c6d`, `139bc24`, `17905fd`, `f009c9b` |

Ellenőrzés minden modulnál ugyanaz, a `73a7f4e` végállapotán: `content_integrity` 0 ERROR; 159 teszt OK; média check és reconcile tiszta.

## C. Kereszt-modul javítások

- **Completion.**
  - GATE-CP: „Receive a grade” + „Passing grade” (`completionpassgrade` = 1), Moodle 4.5/5.0 forrással (CB-C-0018).
  - Nyitás: az éles kapu Assignment-leadása nem külön restrict-feltétel (QA-IMPL-1).
  - HUM 20 completion-sorok (M0.1, M0.2) és a LESSON profil.
  - Runtime acceptance:
    - RA 8: cron utáni visszaolvasás.
    - RA 19: az önkéntes újranyitás negatív esete.
    - RA 31: navigáció, záróoldal és teljesítés utáni elérhetőség.
- **Értékelés.**
  - Az M5.1 kulcsa az M5.A szerint; a három új ✅ a vétólistán.
  - Rubrikacellák: az R4 és az R8 értékelői szövege kikerült a cellából, a szint jelentése szó szerint megmaradt.
  - A négy kvíz-bevezető a saját beállításaikból készült; kulcsot nem árul el, küszöböt nem változtat.
  - A záró értékelési QA nem talált indokolatlan kulcs-, küszöb- vagy completion-változást.
- **Előfeltételek.**
  - A Peula v2 három nyitási feltétele.
  - Az M6/M7 „Mi jön utána?” a §4 szerint.
  - A javítási ág határideje és egyéni ütemezése a manifest §7 szerint.
- **Adatvédelem.**
  - Tájékoztató az M5.4, M6 és M7 feladatnál (ADAT §3, §5, §11).
  - TEXT-C sablon (§11.1).
  - Az LMS-M0-07 és az LMS-M0-02 DPO-tétele az Adatvédelem §3-ban és a G2-ben.
  - A marker-mezők neve a tanulói fájlokban nem szerepel.
- **Gyermekvédelem.**
  - A „Segítség és kapcsolatok” blokk: 112 előbb, címzett a Memuna, helyettese a Ros Hinuh, „te vagy valaki más”.
  - R8: értékelői jegyzet, GYV-11-gyel.
  - Az R4 0. szintje tanulói nyelven.
  - Az M0.2 SLIDE 4 megőrzése: a G1-ben.
  - Ugyanazt a gyermekvédelmi mondatot („munkaidőn kívül és közvetlen veszélyben a 112, illetve a Kék Vonal”) a `17905fd` négy helyen egyértelműsítette. Két lencse vitatta, ezért a `f009c9b` a kánoni szöveget visszaállította. Az olvasatról a Memuna dönt (QF-BIZT-4).
- **Terminológia.**
  - A kódkulcs nem része a megjelenő névnek (CB-C-0034).
  - A Glosszárium tanulói oldaláról csak a belső metaadat marad ki (CB-C-0033).
  - „Kijelölt mentorod vagy értékelőd”.
  - A Moodle 4.5 felületi címkéi.
- **Hozzáférhetőség.**
  - Húzásmentes út: M3.4, M4.2, M4.3, M0.2.
  - A Lecke kérdésoldala nem lehet Drag & Drop.
  - G5b: valódi képernyőolvasós teszt az M0.1-hez és az M0.2-höz.
- **Erőforrások és média.**
  - Új assetek: M7.3-MUNK-01, M7-HUB-MUNK-02.
  - A média kétszer újragenerálva, külön commitban (`62eb098`, `73a7f4e`).
  - Egy asset fallbackon: M0.3-FOTO-01.

## D. A négy forrás-blokkolt activity lezárása

| Activity | Ami már nem blokkolt (bizonyíték) | Ami nyitva marad |
|---|---|---|
| **LMS-M5-01** (M5.1) | SLIDE 2 kulcs A Suli ✅, B Somer ✅, C hétköznapok ✅ (M5.1 SLIDE 2; forrás: M5.A ≈:248–250 és :266); válaszonkénti visszajelzés; meta completion-sor (ERT-1, HUM 20 szűkítéssel); SLIDE 4 5. helyzet | M51-D (S4 1. és 4. visszajelzés, PRG-15 b); QA-PED-3; D-18 (M5:PED-G1-3) |
| **LMS-M5-05** (M5.4) | M5.4 4.1 teljes tanulói feladatleírás, 4.2 beállítás; M5 KAPU R4 cellák tisztítva | BSPEC-08 (szintpont, Grade type, Max grade, lockzeropoints, láthatóság: `PROPOSED` 1/2/3, max. 12); BSPEC-09 |
| **LMS-M6-05** (M6 Játéklap) | M6 KAPU (E1) teljes leírás, (E2) beállítás; a rubrika, a 15 pont és a rejtés változatlan | BSPEC-09; a „pontszámot nem” tagmondat az X-16 visszaellenőrzéséig (RT-P0-28) nem élesíthető; D-07 |
| **LMS-M7-06** (Peula v2) | M7 KAPU (D1) teljes leírás, (D2) egységes sablon + M7-HUB-MUNK-02, (D3) beállítás; a mezőlistát a projektgazda 2026-10-18-i utasítása alapján ez a szakasz rögzíti | QA-PED-1 b (sablon a nyitás előtt); BSPEC-09; Memuna írásos átnézése (QA-BIZT-7, X-1); QF-PED-7 (terjedelem) |

## E. Független QA

| Kör | Hatókör | Reviewerek | Tételek | Kimenet |
|---|---|---|---|---|
| Célzott QA | a négy blokkoló diffje (`709423b` előtt) | assessment, Hungarian, safety, implementation (Moodle 4.5 forrással), pedagogy | 55 (ERT 7, NYELV 21, BIZT 9, IMPL 8, PED 10) | objektívek javítva (`709423b`, `b2c0c6d`); 7 emberi döntés / bizonyíték-kapu |
| QA2 | a `17905fd` előtti diff | safety, assessment, Hungarian | 28 (BIZT 10, ERT 6, NYELV 12) | objektívek javítva (`17905fd`, `f009c9b`); 4 emberi döntés / kapu |
| Záró regressziós QA (QF) | a teljes futás diffje, `f96ce43` → `17905fd`, 34 fájl | pedagogy, assessment, safety, implementation, Hungarian | 49 (BIZT 6, PED 9, ERT 5, IMPL 9, NYELV 20) | objektívek javítva (`f009c9b`); 10 emberi döntés / build-spec; 1 nem hiba (QF-PED-9) |
| Ledger-újraellenőrzés | a 161 átvett tétel | general-purpose (read-only) | 161 | 145 nyitva, 14 forráshely-megjegyzés, döntéssel lezárt 0 |

A záró QA több fontos hibát talált a már javított szövegben. Mindegyiket javítottuk:
- az M4.3 célzóna-visszajelzése a kulccsal ellentétes jelentést adott volna;
- az M0.1-ben a könyv olyan választást kért, amely csak a kérdőívben létezik;
- a Lecke „Minimum number of questions” beállítása nem gátolja a kihagyást, ezért ez most BSPEC-10;
- egy gyermekvédelmi mondatot egyértelműsítettünk, de az olvasatot nem a mi dolgunk eldönteni, ezért visszaállítottuk.

Lezárás tételenként: a regiszter D. és G. szakasza.

**Tesztek a záró állapoton (`5fa743c`, a `/release-check` ellenőrzőlistája a fő sessionben, mert a fork üres eredményt adott):**

| Ellenőrzés | Eredmény |
|---|---|
| `content_integrity` selftest | 57/57 |
| `content_integrity` | `Objective integrity errors: 0` |
| `media_manifest.py` | baseline commit megvan; selftest OK; validate OK (417 asset, 906 deliverable, 123 forrásblokk); check naprakész; reconcile unmapped/conflict nélkül; lint 0 HIGH |
| `unittest tools.test_media_manifest` | 159 teszt OK, skip nélkül |
| `py_compile` | OK |
| `git diff --check` és `git diff --check origin/main...HEAD` | tiszta |
| governance | settings JSON, hookok, ledger- és workflow-selftest OK |
| sandbox-próba | „Operation not permitted”, a sandbox aktív |
| `autopilot_ledger.py check` | `TERMINAL`, kilépési kód 0 |

**Nem vizsgált terület** (a záró lencsék saját jelentése szerint), ezek nem „rendben” állapotúak:
- M0.3, M0.4, M1, M2.4 és Z.1–Z.4 a diffen túl;
- az M5.B, M6.B és M7.B teljes peulaszövege;
- az időbecslés újraszámolása (M4.3: 8 → 12 kártya; M0.1: plusz egy Feedback);
- a Lecke záró URL-je és jegyrögzítése Moodle-forrásból;
- a hétköznapi határidők a HUM 11. szakasz pilot-felülírásával szemben;
- WCAG célméret és kontraszt a Lesson- és Feedback-képernyőkön.

**Runtime:** egyetlen viselkedés sincs a célverzión igazolva. A builder zárt fixture-mérései (D-039/D-040, CB-C-0018) mechanizmus-bizonyítékok. `POST-BUILD: RUNTIME-TESTS 43 not RUNTIME_VERIFIED`.

## F. Ami ténylegesen nyitva marad

Tételesen kulcsonként: `AUTOPILOT-LEDGER.md` Findingok és Külső kapuk (X-1…X-19). A 2026-10-18 előtti 145 nyitott tétel a korábbi szerepköri csomagok szerint változatlan (X-1, X-2, X-3, X-5, X-8, X-11); itt csak a futás új vagy érdemben érintett tételei állnak.

**Szakmai döntés**

| Tétel | Fájl | Következmény | Ami kész | Ami hiányzik (kitől) |
|---|---|---|---|---|
| BSPEC-08 | manifest; M5.4 4.2 | build `NOT_READY` | `PROPOSED` 1/2/3, max. 12 | értékelési felelős + LMS-gazda; a végső pont rejtése: projektgazda (vétó: DPO + jogi) |
| BSPEC-09 | manifest; 8 Assignment-sor | build `NOT_READY`; félkész mentés leadottnak számíthat | `PROPOSED` Yes | LMS-gazda + értékelési felelős |
| BSPEC-10 | manifest LMS-M0-02; RA 31 | build `NOT_READY`; az M0.2 kérdésoldalai kihagyhatók maradnak | a builder „config B” mérése | a beállítások átvétele a builderből; LMS-gazda / build-felelős |
| BSPEC-11 | manifest LMS-M0-06; M0 hub | build `NOT_READY`; a bevezető visszajelzés-mondata nem élesíthető | `PROPOSED` az LMS-M5-06 mintájára | LMS-gazda + értékelési felelős |
| CB-C-0017 | manifest §1 ASSIGN-S; HUM:455 | az automatikus újranyitás visszaállítja a leadás-completiont | három opció leírva | projektgazda |
| QF-BIZT-4 | GYV §4.1 :88; Program terv :251; M3 KAPU :13 | a „munkaidőn kívül” út kétértelmű | kánoni szöveg visszaállítva; a Segítség-blokk csak a 112-t mondja | a Memuna és a helyettese |
| QA2-BIZT-3 | manifest, Segítség-blokk | nincs közvetlen Memuna-csatorna | somer.hu/kapcsolat | Memuna + programvezető |
| QF-BIZT-2, QF-ERT-5, M02-P, QF-IMPL-8 | M0.1, M0.2, M0 hub | az M0.1 / M0.2 nem használható valódi tanulóval | a passzválasz-szöveg, a fejlesztői figyelmeztetések | szerző (+ Memuna az M02-P-nél); projektgazda a D-041-ről |
| QF-BIZT-5, QF-BIZT-6, QA-BIZT-4, D-045 | Adatvédelem §11, §11.1; M5.4, M6, M7 tájékoztatók | a tájékoztatók végső szövege | a lezárt értékekből írt szöveg | DPO (+ LMS-gazda; a D-045-nél projektgazda) |
| QA-PED-3, D-18, QA-PED-9, QF-PED-7, OPINION-ALLCORRECT, SPLIT-LESSONS-ERT1, LMS-Z-02-03, M3 QUIZ-M review, LMS-M0-06 B5 | M5.1; M7 KAPU (D1); M3.1, M3.2, M3.4, M7.1, M7.2; M1.2, M1.3; Z; M3 KAPU | pedagógiai, értékelési vagy build-részletek | a regiszter B. és C. szakasza | módszertani lektor / M5 szerző; programvezető + értékelési felelős; értékelési felelős; build-spec gazda; projektgazda |

**Szakmai jóváhagyás (bizonyíték-kapu)**
- **Memuna (G1, X-1):** az M7 (D) gyermekvédelmi szövege; az M0.2 SLIDE 4; a Segítség-blokk; a Glosszárium „Dokumentálás” sora.
- **DPO (G2, X-2):** az LMS-M0-07 és az LMS-M0-02; a tájékoztatók (RT-15).
- **Programvezető (HUM-OPS-02):** a Segítség-blokk.
- **Szerző (PRG-14 a)):** AI-provenance-nyilatkozat a futás AI-val írt szövegéről; a lista a regiszter F. szakaszában.
- **Szakmai lektor:** az M4.3 új elemei.

**Runtime-bizonyíték (X-4)**
- 43 runtime-teszt, köztük:
  - RT-P0-31 (M0.1, M0.2);
  - RA 8 (cron);
  - RA 19 (önkéntes újranyitás);
  - RT-P0-28/29 (X-16).
- Az LMS-M5-07 végleges profilja.

**Nem elérhető külső információ**
- A célverzió és a környezet (G3, X-17).
- A HUM-OPS-02 csatornái és a build napi nevek (‹…›).
- Az adatvédelmi kontakt.
- A Z.3 megőrzése (BS-D6).
- A builder „config B” pontos beállításai: a builder-repóban vannak, a kánonban nincsenek.

**Ebből a repóból biztonságosan nem megoldható technikai tétel**
- **VO-újrarenderelés (X-6):** M1.1 :784, M1.2 :41, M1.4 :434, M7.3 :796. A privát VO-repó ebből a sessionből nem írható.
- **TECH-2 átnevezés (X-7):** a felhasználó futtatja.
- **GitHub tracker #1 és #2 frissítése:** külső írás, nincs rá felhatalmazás.

## G. Kurzus-készenlét

- **SOURCE CONTENT:**
  - A négy blokkoló tanulói forrása kész.
  - Ebben a futásban nem maradt nyitva olyan forráshiba, amelyet a kánonból bizonyítani lehetett.
  - Több tanulói mondat kifejezetten „nem élesíthető”, amíg a döntés meg nem születik: az M0 kvíz visszajelzés-mondata, az M6 „pontszámot nem”, az M0.1 passzválasz, a Segítség-blokk ‹…› mezői.
  - 130 emberi döntés és 59 bizonyíték-kapu nyitott.
  - Ez nem jóváhagyott tartalom.
- **SOURCE BUILD-SPEC:** `MOODLE-BUILD-VERDICT: NOT_READY`, négy nyitott build-spec tétel (BSPEC-08…11).
- **Moodle runtime:** nincs kanonikus runtime-bizonyíték; 43 teszt nem `RUNTIME_VERIFIED`.
- **Kontrollált pilot release-engedélye:** nincs; `LEARNER-RELEASE-VERDICT: NO-GO`. A G1–G8 szerepköri bizonyítéka és a go/no-go hiányzik.

## H. Átadás

- **Ág:** `next-version/AP-2026-10-18-01`, helyi, nincs pusholva.
- **A futás commitjai, sorrendben:**
  - `38538ed` start;
  - `709423b` M5–M7 blokkolók;
  - `73f30ca` M0, HUM 20;
  - `b2c0c6d` kánon;
  - `139bc24` egyéb tanulói szöveg;
  - `62eb098` média;
  - `ac97720` regiszter;
  - `17905fd` kvíz-bevezetők, blokkok;
  - `f009c9b` záró QA javításai;
  - `73a7f4e` média;
  - `5fa743c` audit;
  - `131001d` ledger;
  - utána ennek a riportnak a commitja.
- **Tesztek:** E. szakasz, minden zöld; a két verdikt a fenti.
- **Worktree:** a riport commitja után tiszta.
- **A legkisebb szükséges következő lépés, a repón kívül:**
  1. A BSPEC-08…11 eldöntése az LMS-gazdával és az értékelési felelőssel. A javaslatok készen állnak a manifestben; ez oldaná fel a build-verdiktet.
  2. A Memuna döntése a „munkaidőn kívül…” mondat olvasatáról.
  3. Az ág pusholása és PR-ja. Ez védett művelet, csak a projektgazda kifejezett kérésére történik.
