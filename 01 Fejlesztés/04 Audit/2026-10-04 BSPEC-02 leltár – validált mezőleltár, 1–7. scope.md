# BSPEC-02 leltár — validált mezőleltár, 1–7. scope (2026-10-04)

> **Audit trail, nem kánon.** A BSPEC-02 maradék szabadszöveg-leltárának első hét scope-ja: M1.3, M2.2, M2.3, M2.4,
> M7.1, Z.1, Z.2. Bemenet és szempontok: `2026-10-04 BSPEC-02 leltár – projektgazdai utasítás és review-brief.md`.
> Bázis: `ed82dbb`, munkaág `fix/moodle-build-hardening`. Tananyagot ez a kör nem módosított. Rövidítések:
> MAN = `02 Tervezet/LMS – activity manifest.md`, RA = `02 Tervezet/LMS – H5P runtime acceptance.md`,
> ADV = `02 Tervezet/Adatvédelem – tanulói adatok és AI.md`, PT = `02 Tervezet/Program terv.md`,
> HUM = `02 Tervezet/Emberi jóváhagyás szükséges.md`, RR = `02 Tervezet/RELEASE-READINESS.md`.

## 0. Futás és lefedettség

- A hét `/course-review` futást a felhasználó indította (scope-onként egy invocation, a briefben megadott lencsékkel).
- Az orchestrator mind a hét futásnál a lencse-reviewerek elindítása után, a verifier előtt visszatért. A
  lencse-riportok a fő sessionbe érkeztek; a SKILL.md 5–6. lépését (scope-onként **egyetlen** verifier az összes
  findinggal, majd riport) a fő session futtatta, a skill szövege szerint.
- Két lencse a lépéskorlát miatt részleges eredménnyel állt meg (M1.3 implementáció, Z.1 biztonság-jog). Folytatással
  mindkettő teljes riportot adott, így **hiányos lencse nincs**.
- **Nem futott:** a brief 8–20. scope-ja (M0.1–M0.4, M3.3, M3.4, M5.2, M5.4, M6.1–M6.4, M7.4). Ezekre a leltár
  nem teljes.
- Számok: 7 scope, 16 lencse-riport, 7 verifier, 99 finding. Verdikt: MEGERŐSÍTVE 62 (ebből 8 bizonyíték-kapu),
  ELVETVE 18, EMBERI DÖNTÉS 19 (a duplikátumokkal együtt; a findingonkénti verdiktsorokból számolva).

## 1. Mezőleltár (deduplikált, a verifier végső besorolásával)

Privacy: `P0` nincs rögzítés, `P1` fiókhoz kötött választás, `P2` tárolt szabad szöveg (MAN §1).

| # | Lecke:sor | Mező / prompt (röviden) | Köt./opc. | Tárolt | Completion-függés | Privacy | Manifest ma | Besorolás | Teendő | Döntő bizonyíték |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | M1.3:797–805 | 5. dia, vezetett S/B/I: „Kötelező sablon (1 mondat)” | ellentmondásos | nincs eldöntve | ellentmondásos | P2, ha tárolt | nincs (LMS-M1-03 „profil”) | `HUMAN_DECISION_REQUIRED` | D-1 | M1.3:80, :801, :826, :926–928, :1100; M1 hub :116 |
| 2 | M1.3:1100 | 5. dia, „1 opcionális mondat” | opcionális | nem | nem | P0 | nincs | `OPTIONAL_LEARNER_LOCAL` (ha létezik) | a D-1 része | M1.3:928, :1100; ADV:29 |
| 3 | M1.3:887–895 | 6. dia, „Most írj egy saját mini-SBI-t.” (3 mező) | kötelező | igen | igen | P2 | nincs | `REQUIRED_STORED_MANIFEST_ROW_MISSING` | új TEXT-C sor (F-M1.3-1) | M1.3:80, :926; RA:73 (12. pont); MAN:35; HUM:431 |
| 4 | M1.3:888, :1030–1037, :1061 | mentési utasítás, 7. dia önellenőrző pipái | – | nem | nem | P0 | – | `NOT_ACTUALLY_FREE_TEXT` | nincs (RA 7 teszt: bizonyíték-kapu) | M1.3:1037; RA:47 |
| 5 | M2.2:468–495 | SLIDE 5, TOP 3 érték + „legalább egy konkrét helyzet” | kötelező | igen | igen | P2 | nincs | `REQUIRED_STORED_MANIFEST_ROW_MISSING` | új TEXT-C sor (F-M2.2-1) | M2 hub :183, :188; PT:225; MAN:292 |
| 6 | M2.2:499–525 | SLIDE 6, „Írj erről 5–8 mondatot” | kötelező | igen | igen | P2 | nincs | `REQUIRED_STORED_MANIFEST_ROW_MISSING` | ugyanaz a sor | M2.2:507; M2 hub :183, :188; PT:225 |
| 7 | M2.2:181–190, :445–464, :573, :706 | hook-kérdés, értékválasztás, opcionális Kérdés 3, „Tedd el…” | – | H5P-válasz / nem | értékválasztás: igen | P1 / P0 | LMS-M2-02 | `NOT_ACTUALLY_FREE_TEXT` | nincs | M2 hub :183; MAN:53 |
| 8 | M2.2:16, :699 | kapu-utalás: „ez az 1 kiemelt érték kerül be” | kötelező | igen | az M2 modulé | P2 | LMS-M2-05 | `REQUIRED_STORED_ALREADY_COVERED` | nincs | M2 hub :191; MAN:57 |
| 9 | M2.3:896–901 | záró „így mutatok példát” mondat | kötelező | igen, név szerint | igen | P2 | LMS-M2-07 | `REQUIRED_STORED_ALREADY_COVERED` | lecke-szöveg (F-M2.3-1, -2); BIZT-R5 nyilvántartása (F-M2.3-5) | M2 hub :183, :189; MAN:24, :56; HUM:517; a projektgazda A–M listájának B pontja |
| 10 | M2.3:523, :540, :557, :614, :631, :648, :705, :722, :739 | MR1–MR9, „Írj 1 mondatot: …” | opcionális | nem | nem | P0 | nincs | `OPTIONAL_LEARNER_LOCAL` | a tárolást előíró mondatok javítása (F-M2.3-3, -4) | M2 hub :183; ADV:29, :52, :112; PT:227 |
| 11 | M2.3:268–274, :777–814 | hook-önreflexió („nem rögzítjük”), CHECK K1/K2 | – | nem / választás | nem | P0 / P1 | LMS-M2-04 | `NOT_ACTUALLY_FREE_TEXT` | nincs | M2.3:270; MAN:55; RA:71 |
| 12 | M2.4:574–582 | háromoszlopos lista, „privát munkalap: nem adod be” | kötelező tanulási lépés | nem | nem | P0 | nincs (helyesen) | `REQUIRED_BUT_LEARNER_LOCAL` | nincs | M2.4:582; M2 hub :183; PT:225 |
| 13 | M2.4:584–586 | szabálymondat | kötelező | igen | igen | P2 | nincs | `REQUIRED_STORED_MANIFEST_ROW_MISSING` | új TEXT-C sor (F-M2.4-1) | M2 hub :183, :190; PT:225 |
| 14 | M2.4:649–661 | „Írj 4–6 mondatos szakmai választ” (fiktív eset) | kötelező | igen | igen | P2 | nincs | `REQUIRED_STORED_MANIFEST_ROW_MISSING` | ugyanaz a sor | M2 hub :183; PT:225 |
| 15 | M2.4:682–691 | 3 határszabály, „Írj minden ponthoz 1–2 mondatot” | kötelező | igen | igen | P2 | nincs | `REQUIRED_STORED_MANIFEST_ROW_MISSING` | ugyanaz a sor | M2 hub :183, :190; M2.4:671 |
| 16 | M2.4:189–198, :331–342, :762–785 | önjelző pollok (első reflex, emoji, két ön-check) | – | nem rögzítendő | nem | P0 | LMS-M2-03 | `NOT_ACTUALLY_FREE_TEXT` | LMS-M2-03 megjegyzése (F-M2.4-5) | ADV:29, :112 |
| 17 | M2.4:35, :37, :39, :53, :757, :801 | keretszövegek, jegyzetbe-áthordás | – | – | – | – | LMS-M2-05 (:801) | `NOT_ACTUALLY_FREE_TEXT` | nincs | M2 hub :191; M2 KAPU :185 |
| 18 | M7.1:511–541 | SLIDE 7, peula 1 mondatban + SMART cél (max. 2 mondat) | kötelező | igen | igen | P2 | nincs (LMS-M7-01 „profil”) | `REQUIRED_STORED_MANIFEST_ROW_MISSING` | új TEXT-C sor (F-M7.1-1) | M7.1:513, :540; MAN:24, :35; PT:261, :319 |
| 19 | M7.1:412–428 | SLIDE 5 AI-segéd promptja | opcionális | a Moodle-oldal nincs rögzítve | nem | P2, ha tárolódik | LMS-M7-01 megjegyzése | `HUMAN_DECISION_REQUIRED` — **nem BSPEC-02-blokkoló** | N-5 | M7.1:412; ADV:86; HUM:191; RA:90–95 |
| 20 | M7.1:422 | „feljegyezned magadnak, miben segített” | opcionális | nem | nem | P0 | nincs | `OPTIONAL_LEARNER_LOCAL` | nincs | M7.1:422 |
| 21 | M7.1:422 (v2-sor) | AI-használat jelölése a v2 mellett | kötelező a v2-ben | igen | a v2-é | P2 | LMS-M7-06 | `REQUIRED_STORED_ALREADY_COVERED` | nincs | MAN:96 |
| 22 | M7.1:236, :324–358, választós elemek | „Vedd elő…”, SLIDE 4 Fill in the Blanks | – | választás | H5P-C | P1 | LMS-M7-01 | `NOT_ACTUALLY_FREE_TEXT` (a SLIDE 4-nél csak a (B) út lezárásával: F-M7.1-3) | F-M7.1-3 | RA:40 (d); M7.1:333 |
| 23 | Z.1:437–453 | SLIDE 5 fénypont-esszé, „Írj 3–6 mondatot” + „pl. 200 karakter” | a lecke szerint kötelező | nincs eldöntve | nincs eldöntve | P2, ha tárolt | nincs (LMS-Z-01 „profil”) | `HUMAN_DECISION_REQUIRED` | D-2 | Z.1:53, :447–453; RA:73; MAN:35, :147; Z hub :71–72, :196; ADV:29 |
| 24 | Z.1:517–523 | SLIDE 6, „Írj le 1 dolgot, amit semmiképp nem szeretnél elfelejteni” | kötelező tanulási lépés | nem | nem | P0 | LMS-Z-01, megjegyzés nélkül | `REQUIRED_BUT_LEARNER_LOCAL` | F-Z.1-1, -2 | Z hub :72, :196; MAN:147; ADV:29 |
| 25 | Z.1:435 | az M0-mondatok újraírása, ha a mentés elveszett | opcionális | nem | nem | P0 | nincs | `OPTIONAL_LEARNER_LOCAL` | F-Z.1-3 | M0.1:410; Z.4:194 |
| 26 | Z.1:11, :15, :21, :38, :40, :287, :425, :502, :514, :533 | meta-, mikrocél- és narrációs utalások, minta-headline-ok | – | – | – | – | – | `NOT_ACTUALLY_FREE_TEXT` | a :11-re F-Z.1-4 | Z.1:47, :289 |
| 27 | Z.2:274–276 | SLIDE 5, „Írj 5–8 mondatot…” + „pl. 250” | a lecke szerint kötelező | nincs eldöntve | nincs eldöntve | P2, ha tárolt | nincs (LMS-Z-02 „profil”) | `HUMAN_DECISION_REQUIRED` | D-3 | Z.2:39, :59, :280; ADV:88, :93 |
| 28 | Z.2:309–311 | SLIDE 6, „Írj róla 5–8 mondatot” (alternatív kérdéssel, passz-ígérettel) | a lecke szerint kötelező | nincs eldöntve | nincs eldöntve | P2, ha tárolt | nincs | `HUMAN_DECISION_REQUIRED` | D-3 (+ D-3b) | Z.2:305, :307, :311; ADV:88 |
| 29 | Z.2:333–335 | SLIDE 7, 3 szó | kötelező tanulási lépés | nem | nem | P0 | nincs | `REQUIRED_BUT_LEARNER_LOCAL` | F-Z.2-3 | ADV:29, :112; Z.2:17, :321; Z hub :83 |
| 30 | Z.2:122–137, :187–200, :229–244 | választós kérdések | – | választás | H5P-C | P1 | LMS-Z-02 | `NOT_ACTUALLY_FREE_TEXT` | nincs | Z.2:61 |

## 2. Validált objektív findingok a `/course-fix`-hez

A `F-…` azonosító ebben a leltárban egyedi; zárójelben a megtartott reviewer-ID és a beolvasztott duplikátumok. A
„korlát” mező a `/course-fix` javítási korlátja.

### 2.1 Új TEXT-C sorok (a döntésektől független rész)

| build_id (javaslat; szabad) | Lecke | Kérdések („Required” Longer text answer) | Completion |
|---|---|---|---|
| LMS-M1-07 | M1.3 – Saját mini-SBI | 3: S, B, I (6. dia); a D-1 „kötelező” ágán az 5. dia mezői is | beküldve; a minimálisan értelmezhető tartalmat a Moodle nem ellenőrzi (BS-D4) |
| LMS-M2-08 | M2.2 – Szöveges válaszok | 2: SLIDE 5, SLIDE 6 | beküldve; a terjedelmet a Moodle nem ellenőrzi (BS-D4) |
| LMS-M2-09 | M2.4 – Szöveges válaszok | 5: szabálymondat, esetválasz, 3 határszabály | ua. |
| LMS-M7-10 | M7.1 – Saját SMART cél | 2: :528 (peula 1 mondatban), :529 (SMART cél) | ua.; a SMART-minőséget sem |

Mind a négy sornál: P2; megőrzés a TEXT-C alapértelmezése (ADV §3 „Szabad szöveges reflexió”); mentori elfogadási
állapot nincs (a BS-D8 csak a Z.3-ra szól); a just-in-time tájékoztatóba a lecke mező melletti adatvédelmi
megjegyzése szó szerint; felveendő a MAN:35 és az RA 6. pont felsorolásába, a BSPEC-02 sorában lefedettnek jelölendő.
Az unlock a meglévő minta szerint (a TEXT-C a lecke H5P-je után, a következő lépés a TEXT-C után: LMS-M2-06 ←
LMS-M2-01, LMS-M2-02 ← LMS-M2-06); a párhuzamos nyitás tervezői választás, nem kánoni kötelezettség.

### 2.2 Findingok scope-onként

**M1.3**
- **F-M1.3-1** (IMPL-1, P1): az új LMS-M1-07 sor; LMS-M1-03 completion: „profil; a saját mini-SBI: LMS-M1-07”;
  LMS-M1-04 unlock; a lecke :927 nevezze meg az alapértelmezett utat (az M2.3:880 mintájára), a 6. dia mutasson a
  kísérő mezőre, a :80 igazodjon hozzá (látható szöveg, pin). **Korlát:** a :926 feltétele nem gyengülhet; az 5. dia
  státuszához a D-1 előtt nem nyúl; a TEXT-C beállításai és a megőrzés nem változnak.

**M2.2**
- **F-M2.2-1** (IMPL-1 ← BIZT-5, P1): az új LMS-M2-08 sor; LMS-M2-02 completion: „profil (értékválasztás); a nyitott
  mezők: LMS-M2-08”; a lecke :29 az M2.3:44 mintájára; a hub L2 (:72) hivatkozzon az RA 6. pontra. A :488 és a :495
  szó szerint a just-in-time tájékoztatóba. **Korlát:** a SLIDE 5–6 kérdései, terjedelme, a :488/:495 tartalma és a
  narráció (:710–717) nem változik.
- **F-M2.2-2** (IMPL-2, P2): két mező rögzítése (:26 „2×”, :505 „didaktikailag jobb külön”); a :474 és a :505
  zárójeles alternatívája törlendő. **Korlát:** a kérdések szövege nem változik.
- **F-M2.2-3** (IMPL-3 ← BIZT-2, P2): „Completion:” sor az 1. szakaszba a hub :183 M2.2-tagmondatával; a :507
  jelölése ne zárja ki a SLIDE 5-öt. **Korlát:** a SLIDE 5 kötelező státusza nem gyengül.

**M2.3**
- **F-M2.3-1** (ERT-2 ← IMPL-2, BIZT-4, P1): a :114 és a :11 (@asset spec) mondja ki, hogy az „1 teljes ág” a
  Branching Scenario (LMS-M2-04) completionje, a lecke completionjéhez a záró mondat (LMS-M2-07) is kell; utána
  `media_manifest.py build` külön `chore(media)` commitban.
- **F-M2.3-2** (ERT-3 ← IMPL-3, BIZT-5, P1): a ZÁRÓ OLDAL (:896, :901, :922) nevezze meg az „M2.3 – Záró mondat”
  activityt, a :922 ne mondja a BS végét a lecke végének. **Korlát:** a :900 mezőszöveg, a hágsámá-mondat
  (HUM-SOMER-03) és a narráció (:909–918, VO) változatlan; pin kell.
- **F-M2.3-3** (IMPL-1 ← ERT-4, P1): a :44 utolsó mondata helyett: a mini-reflexiók rögzítés nélküli önreflexiók,
  beviteli elem és Moodle-mező nélkül, a completion nem függ tőlük; átvezetés: :11, :15, :116; LMS-M2-04 megjegyzése
  („opcionálisak, nem completion-feltételek”, az LMS-M1-01 mintája); BSPEC-02 sor: „opcionális, sor nélkül”.
  **Korlát:** manifest-sort vagy tárolt mezőt létrehozni tilos.
- **F-M2.3-4** (IMPL-4, P2): a hub :215 mutatója törlendő, a :216 a választások rögzítésére szűkül; helyettesítő
  mutatót kitalálni tilos.
- **F-M2.3-5** (IMPL-6 ← ERT-6, P2): a nyitott BIZT-R5 kérdés nyilvántartása az RR G2 sorában (a BS-D6 mellé) és az
  LMS-M2-07 megjegyzésében; tartalmi döntést nem ír be (lásd N-2).

**M2.4**
- **F-M2.4-1** (IMPL-1 ← BIZT-2, P1): az új LMS-M2-09 sor; LMS-M2-03 completion: „profil; a szöveges válaszok:
  LMS-M2-09”; LMS-M2-04 unlock: LMS-M2-03 → LMS-M2-09; Megjegyzés: a privát lista és a pollok nem ide tartoznak.
  **Korlát:** nincs GATE-CP; a „3”, „4–6”, „1–2” számok változatlanok.
- **F-M2.4-2** (BIZT-1 ← IMPL-2, P1): a :584 szűkítése a SLIDE 4 blokkjára („Ebből a blokkból a Moodle-be csak…”);
  a SLIDE 5 és a SLIDE 6 alá a :590 mintájára Moodle-beadási jelölés az új sorra. **Korlát:** a háromoszlopos lista
  nem lesz tárolt; a :588 nem változik; pin kell.
- **F-M2.4-3** (BIZT-3, P1): a meglévő :588 tiltólista és a :35 „A Moodle-be csak azt írd …” mondata szó szerint a
  SLIDE 5 és a SLIDE 6 mezői mellé. **Korlát:** új tiltólista vagy policy-mondat írása és a :691 példa átírása tilos.
- **F-M2.4-4** (IMPL-3, P2): a :590, :640, :671 nevezze meg az alapértelmezett helyet (LMS-M2-09); az :511 és :549
  asset-megjegyzés javítása után `media_manifest.py build`. A „nincs Completion-sor” részállítás elvetve.
  **Korlát:** a :657–659 biztonsági blokk és a :588, :661 tiltás nem törölhető.
- **F-M2.4-5** (IMPL-5 ← BIZT-5, P2): LMS-M2-03 megjegyzése: az önjelző kérdések (SLIDE 1, 2, 7) rögzítés nélküli
  önreflexiók, a completion nem épül rájuk (ADV §2, §5); RA-teszt az RA 21. pont mintájára.
- **F-M2.4-6** (IMPL-4, P2): a hub :183 „érdemi kitöltés” mellé: a Moodle a beküldést ellenőrzi, az érdemi
  tartalmat – ha szükséges – a kijelölt mentor/értékelő nézi át (BS-D4). **Korlát:** minimum vagy automatikus
  validáció nem kerülhet be.
- **F-M2.4-7** (IMPL-8, P2): a hub :219 stáb-analitikája csak összesített adatra (PT:227). **Korlát:** új mentori
  rögzítési folyamat nem írható (az N-3-tól függ); a „2–3” szám változatlan.

**M7.1**
- **F-M7.1-1** (IMPL-1 ← BIZT-1, ERT-1, ERT-2 :540-része, P1): az új LMS-M7-10 sor; Megjegyzés: a lecke záró
  vázlata, nem a Peula v1 (LMS-M7-05), a kettő nem vonható össze; a :531 szó szerint a just-in-time tájékoztatóba;
  LMS-M7-01 completion: „profil; a saját SMART cél: LMS-M7-10”; LMS-M7-02 unlock: LMS-M7-10; a :540 második
  tagmondata az M4.4:26/:664 mintájára. **Korlát:** rutinszerű mentori átnézés nem írható elő; a „Nincs automatikus
  pontszám, csak completion” és a :541 marad.
- **F-M7.1-2** (IMPL-2 ← BIZT-2, ERT-3, P1): a :8, :45, :518 és a hub :183 eszközleírása: a SLIDE 7 mezői a
  Moodle-oldali kísérő activityben (LMS-M7-10); a dián tanulói mutató („Írd le az „M7.1 – Saját SMART cél”
  szövegmezőbe:”), pin. **Korlát:** a :524–537 feladatszöveg és terjedelme nem változik.
- **F-M7.1-3** (ERT-4 ← IMPL-3, P2): a SLIDE 4 (:333) „pontozás nélküli rövid szöveges válasz” útja csak az RA 6. pont
  (b) útján, igazolt működés után; addig a (d) Fill in the Blanks. **Korlát:** az elfogadási elv, a feladatszövegek
  és a visszajelzések nem változnak (az elfogadott számhalmaz: H-4, hatókörön kívül).

**Z.1** (a SLIDE 5-öt érintő részek a D-2 után)
- **F-Z.1-1** (ERT-3 ← IMPL-4, P2): a SLIDE 6 (:506, :523) tanuló-lokális lépés: „Írd le magadnak (jegyzet,
  képernyőkép). Nem adod be.” A „nem tároljuk” állítás csak az F-Z.1-5 runtime-igazolása után. **Korlát:** a :519
  kérdés és a :531–533 VO-forrás változatlan; a :15 mikrocél és a Z hub :72 nem gyengül.
- **F-Z.1-2** (IMPL-5 ← BIZT-4, P1): „Completion (lecke):” sor (SLIDE 1 SC, SLIDE 3 MC, SLIDE 4 SCS) és az LMS-Z-01
  megjegyzése az LMS-M1-01 mintájára; a SLIDE 5-ről szóló félmondat a D-2 után.
- **F-Z.1-3** (ERT-4 ← IMPL-7, P2): a :435 mondja ki, hogy a két mondat a tanuló saját jegyzetébe kerül, nem a
  fénypont-mezőbe. **Korlát:** új tárolt mező nem nyitható.
- **F-Z.1-4** (IMPL-6 ← ERT-5, P2): a :11 ne „beágyazottként” írja le a szabad szöveget, hanem a :53 szabályára
  utaljon (A11Y §6:63); a hub :71–72 a D-2 után.
- **F-Z.1-5** (BIZT-3, P1): az RA-ba visszaolvasási lépés minden tanuló-lokális H5P-szövegmezőre: aktív-e a
  célverzión a „Save state” (`enablesavestate`, `MOODLE_405_STABLE` alapértéke 1), és keletkezik-e tárolt állapot a
  tesztfiókhoz. Addig „nem tároljuk” típusú tanulói állítás nem kerülhet a leckébe. **Korlát:** a beállítás értékét
  kitalálni tilos.
- **F-Z.1-6** (IMPL-3, P1): a :53 mezőspecifikus legyen (a SLIDE 6 tanuló-lokális, CP-be ágyazott szövegmező nem
  épül); a SLIDE 5 a D-2 szerint. **Korlát:** a :57 tájékoztató-kötelezettsége tárolt mezőnél nem gyengülhet; a 18
  leckében ismétlődő sablont nem kell globálisan cserélni.

**Z.2** (a SLIDE 5–6-ot érintő részek a D-3 után)
- **F-Z.2-1** (ERT-3 ← IMPL-2, P2): a „minimális karakterszám (pl. 250)” helyett: a terjedelem (5–8 mondat)
  útmutatás, az alapértelmezett úton a Moodle nem ellenőrzi (BS-D4; RA 12). **Korlát:** a „pl. 250” nem válik
  küszöbbé, a 6. diára nem kerül szám; az „Írj 5–8 mondatot” marad.
- **F-Z.2-2** (IMPL-4, P2): a „(ESSAY)” és a „Beágyazott kérdés” helyett a pedagógiai megnevezés („hosszabb
  szöveges reflexió”, „rövid szöveges válasz”; A11Y §6:62–63); a mező helye a D-3 után.
- **F-Z.2-3** (IMPL-5 ← BIZT-4, ERT-5, P2): a 7. dia tanuló-lokális, nem completion-feltétel, nem rögzül; LMS-Z-02
  megjegyzése; RA-teszt (F-Z.1-5); a :39 a tárolt mezőkre szűkül. **Korlát:** az „opcionális” szó nem vehető át
  (státuszcsere lenne).
- **F-Z.2-4** (BIZT-2 ← IMPL-3, P1): a :39, :42, :280 láthatósági és gyermekvédelmi mondata a D-3 szerinti
  megvalósításhoz; a :44 kapjon „különben” ágat. **Korlát:** a Memuna- és a 112-utasítás szó szerint marad; a
  tanuló-lokális ágon a gyermekvédelmi tagmondat átfogalmazása a Memuna utólagos ellenőrzése alá esik.
- **F-Z.2-5** (BIZT-5, P2): a :63 hatóköre „minden adatot rögzítő mező” (PT:225); tanuló-lokális mezőnél a szöveg
  mondja ki, hogy nem tároljuk (F-Z.1-5 után). **Korlát:** új megőrzési szabály nem írható.

## 3. Emberi döntések

### 3.1 A BSPEC-02 lezárását blokkolók

- **D-1 — M1.3, 5. dia.** Az 5. dia vezetett S/B/I mezőinek kitöltése az LMS-M1-03 teljesítési feltétele-e? Létezik-e
  a :1100 szerinti „1 opcionális mondat”, és ha igen, mi a szövege? **Gazda:** projektgazda. Kánoni háttér: a :801
  („Kötelező sablon”) és a :1100 („1 kötelező”) a kötelező, a :80 tanulói kész-definíciója (csak a 6. dia), a :826
  nem blokkoló visszajelzése és a :928 („gyakorlás, ezért lehetőleg csak a tanuló látja”) a nem tárolt gyakorlás
  felé mutat; az M1 hub :116 nem dönt. **Ágak:** kötelező → további „Required” kérdések az LMS-M1-07-ben;
  gyakorlás → `OPTIONAL_LEARNER_LOCAL`, a követett LMS-M1-03-ban nem lehet rögzítő mező.
- **D-2 — Z.1, SLIDE 5 fénypont-esszé.** A SLIDE 5 szövegének beküldése a Z.1 (LMS-Z-01) teljesítésének feltétele-e?
  **Gazda:** projektgazda; QA: értékelési felelős. Kánoni háttér: a lecke :53/:453, az RA 12. pont (:73), a MAN:35 és
  a PT:261 a tárolt TEXT-C felé; az ADV:29 alapértelmezése, a Z hub :196 és a MAN:147 (csak a Z.3 szövegét köti), a
  hub :71–72 (nem ismeri a mezőt) és a Z.1:451 a tanuló-lokális út felé; ugyanezt a tartalmat a Z.4 (LMS-Z-04)
  mentori megerősítéssel gyűjti. **Ágak:** (A) tárolt TEXT-C, új sor (LMS-Z-08), az ADV:89 szerinti review, a :449
  módosításánál Memuna-QA; (B) kötelező, de tanuló-lokális lépés, nem completion-feltétel. **D-2b, csak az (A)
  ágon:** maradjon-e a „3–6 mondat” mellett karakterminimum (a Moodle csak a nem üres beküldést ellenőrzi, BS-D4)?
  Gazda: értékelési felelős + projektgazda.
- **D-3 — Z.2, SLIDE 5 és 6.** Feltétele-e a Z.2 teljesítésének, hogy a tanuló a két szöveges választ név szerint
  tárolva beküldje (új TEXT-C sor), vagy a két válasz tanuló-lokális önreflexió? **Gazda:** projektgazda; vétó/QA:
  DPO/jogi felelős (HUM-PRIV-01). Kánoni háttér: a lecke „beadás”-szövege (:39, :280, :305) a tárolt út felé; az
  ADV:88 a „Z.2/Z.4 személyes reflexiók és mentor-hozzáférés” tételt külön review-ként tartja nyilván, és az ADV:93
  projektgazdai döntése csak az M2-, M3- és M7-sorra szól; a Z.3 és a Z.4 felidézésre épít, nem tárolt Z.2-szövegre.
  **D-3b, csak a tárolt ágon:** a 6. dia kötelező mezőjénél a passzjogot csak a :305 alternatív kérdése teljesíti,
  vagy egy passz-jelzés beküldése is? Gazda: projektgazda; vétó: Memuna (HUM-SAFE-03).

### 3.2 Nem blokkolók (learner release, G1/G2)

- **N-1 — M1.3, 6. dia (BIZT-2).** A tárolt mini-SBI mezőbe kerülhet-e valós, névtelenített helyzet (:888), vagy –
  ahogy a lecke az M1.4-re előírja – csak kitalált? Gazda: projektgazda; vétó: DPO. A sor szerkezetét nem érinti.
- **N-2 — M2.3 záró mondat (BIZT-R5, szűkítve).** A brief (a)–(d) pontja: (a) a pedagógiai cél megköveteli (M2.3:875,
  hub :80); (b) a teljesítés is (hub :183, :189); (c) a név szerinti tárolásról a projektgazda A–M listájának B pontja
  („new `LMS-M2-07`: M2.3 required closing response”; „non-anonymous where learner identity/completion must be
  tracked”), a BS-D4 és a TEXT-C profil (MAN:24) dönt; (d) a kevésbé azonosító út (névtelen Feedback) nem teszi
  lehetővé a tanulóhoz kötött javítást és a saját válasz felülírását (MAN:24), a tanuló-lokális út pedig a
  „beírva” állapotot nem igazolja. **A legkisebb nyitott kérdés:** a kötelező, viselkedésszintű, a végigjátszott
  pillér-ághoz kötött mondat az ADV:75 / MAN:27 szerint normál tanulási activityben nem gyűjthető politikai, vallási
  vagy világnézeti adatkérés-e; ha nem, kell-e mező melletti tartalmi korlát, és mi a jóváhagyott szövege. Gazda:
  DPO/jogi felelős; someres vonatkozásban a projektgazda. Ez a HUM-PRIV-01 utólagos ellenőrzése (vétó/QA), amely a
  HUM 10. szakasz build-readiness elve szerint a buildet nem blokkolja; vétó esetén a tétel újranyílik.
  Nyilvántartás: F-M2.3-5.
- **N-3 — M2.4 (BIZT-4, P0).** Az M2.4 beküldött válaszait a kijelölt mentor kötelezően átnézi-e, és milyen
  határidővel? Ha nem, a :37 „a mentorod azonnal bevonja a … Memunát” ígéretet úgy kell-e módosítani, hogy a sürgős
  út kizárólag a „Segítség és kapcsolatok” blokk legyen? Gazda: Memuna (HUM-SAFE-01); vétó/QA: DPO/jogi felelős.
- **N-4 — M2.4 (BIZT-6).** Ha a tanuló passzol a SLIDE 5 kötelező esetválaszánál, mi az egyenértékű alternatíva, és
  hogyan teljesül az LMS-M2-09 completionje? Gazda: Memuna + programvezető (HUM-SAFE-03). A TEXT-C csak a nem üres
  beküldést ellenőrzi, ezért a build-beállítást nem változtatja; a tanulói utasítás szövegét igen.
- **N-5 — M7.1 (BIZT-3).** Ha az AI-segéd Moodle-integrációja a promptot és a választ a tanuló fiókjához kötve tárolja
  (pl. a core AI-alrendszeren át), megengedett-e, és melyik ADV §3 megőrzési sor vonatkozik rá; vagy a build-spec
  nem tároló integrációt ír elő? Gazda: DPO/jogi felelős; programvezető (HUM-PRIV-04). Az AI-prompt opcionális,
  TEXT-C sort egyik kimenetnél sem kap.

## 4. Bizonyíték-kapuk (nem javíthatók; G2/G3b)

Megvalósítási döntés: projektgazda jóváhagyta (HUM-PRIV-01, TEXT-C); a formális szerepköri bizonyíték függő.
- M1.3 (IMPL-4 ← BIZT-4): az RA 7. pont M1.3-tesztesete, az új sor activity-szintű adatleltára (ADV §3), DPO-ellenőrzés.
- M2.2 (IMPL-4 ← BIZT-3): a :495 láthatósági ígéretének RA 15. pont szerinti visszaolvasása.
- M2.3 (BIZT-6): az LMS-M2-07 adatleltár-sora és a DPO szövegmező-review-ja.
- M2.4 (BIZT-8 ← IMPL-6): az új sor DPO-ellenőrzése és az RA 15. pont visszaolvasása.
- Z.1 (IMPL-8): csak a D-2 (A) ágán.

## 5. Elvetett findingok

P1 (egyenként): M1.3/BIZT-1 (a :928 „lehetőleg” megengedi a kijelölt mentort, a TEXT-C profil teljesíti; a valós mag
az F-M1.3-1); M2.2/BIZT-1 (a hub :183/:188 és a PT:225 eldönti a tárolást); M2.3/BIZT-1 és ERT-1 (a BS-D4 és a TEXT-C
profil a tanulónkénti „ha szükséges” ellenőrzést megadja); M2.3/BIZT-3 és ERT-5 (a hub :183, az ADV:29/:52/:112 és a
PT:227 a mini-reflexiók tanuló-lokális útja mellett dönt); M2.4/BIZT-5 (a HUM-PRIV-01-re épülő ADV §5 a saját
önreflexióról is dönt). P2: 11 (M1.3/IMPL-3, M2.2/BIZT-4, M2.3/IMPL-8, M2.4/IMPL-7, M2.4/BIZT-7, M7.1/BIZT-4,
Z.1/BIZT-5, Z.2/IMPL-6, Z.2/BIZT-6, Z.2/ERT-4, Z.2/ERT-5).

## 6. Hatókörön kívüli, validált megfigyelések (nem BSPEC-02)

- **H-1 — M2.3 (IMPL-7).** A :114 „Moodle-checkpoint” tartalékútjának nincs profilja és sora, pedig az LMS-M2-07 az
  LMS-M2-04 completionje után nyílik; ha a Branching Scenario completionje nem érkezik meg, az M2 nem teljesíthető.
  A verifier szerint külön BSPEC-sor kell, nem a BSPEC-02.
- **H-2 — a kijelölt mentor tanulónkénti láthatósága (BIZT-R3).** A szabály lezárt (HUM-PRIV-01), a mechanizmus
  sehol nincs rögzítve; az ADV:33/:42 az activitynkénti „szerepkör (Moodle-role/capability)” mezőt az LMS-owner és a
  privacy felelős feladatának adja, az RR:25 BUILD-tételnek. Minden P2 sort érint, nem csak a TEXT-C-t. Emberi kérdés
  csak akkor: ha nincs core tanulónkénti mechanizmus, elfogadható-e a szerepkör-szintű láthatóság (DPO/jogi felelős).
- **H-3 — M7.1 SLIDE 4.** A (d) úton a „reális szám” elfogadott halmaza nincs rögzítve (modulgazda / értékelési
  felelős).
- **H-4 — a H5P-C completion forrása.** A Z.2 implementációs lencséje szerint a `mod_h5pactivity` megtekintés- vagy
  grade-alapú completiont ismer, interakciónkéntit nem; a verifier BSPEC-02-n kívülinek ítélte (az RA 9. és 14. pont
  teszteli).

## 7. A korábbi kör kilenc „emberi döntés” tételének kánoni ellenőrzése

| # | Tétel | Eredmény | Ami valóban nyitott → gazda | Build-hatás |
|---|---|---|---|---|
| 1 | LMS-Z-06 megőrzése | NYITOTT — a lezárt BS-D6 (HUM:519) tartja nyitva | 90 nap vagy 12 hónap → DPO | learner release; a tájékoztató megőrzési mezője helyőrzővel épül |
| 2 | kijelölt mentor mechanizmusa (BIZT-R3) | RÉSZBEN — a szabály lezárt (HUM:132), a mechanizmus nincs rögzítve | lásd H-2 → DPO/jogi felelős, csak ha nincs core mechanizmus | igen (RR:25 BUILD) |
| 3 | harmadik fél neve a Z.3-ban (BIZT-R10) | RÉSZBEN — a lecke kéri (Z.3:283), a mező csak a személyt igényli (Z.3:287; MAN:102); ADV:29 | valódi név vagy szerep → DPO/jogi felelős | csak szöveg |
| 4 | LMS-Z-07 elfogadási minimuma (BIZT-R2) | KÁNON DÖNTI EL — a gyermekvédelmi jelzés címzettje mindig a Memuna, nem a mentor (Gyermekvédelem :81, HUM-SAFE-01) | csak megfogalmazás (Z.3:306 vs :300) | nincs |
| 5 | felülírás az elfogadás után | RÉSZBEN — automatikus visszarontás nincs (GATE-CP, MAN:25; PT:265; HUM:455) | az LMS-Z-06 zárolása vagy értesítés a mentornak → projektgazda (BS-D8), Memuna-vétó | igen, ha zárolás/értesítés |
| 6 | Memuna-vétó hatóköre (BIZT-R8) | RÉSZBEN — a vétó definíciója döntésszintű (HUM:8; PT:379) | igen/nem megerősítés → projektgazda + Memuna | nincs, ha döntésszintű |
| 7 | LMS-M7-09 megerősítési határideje | NYITOTT (MAN:95 maga jelöli) | határidő vagy a kvíz korábbi zárása → programvezető (HUM-OPS-01) | csak ha az M7_QUIZ zárása mozdul |
| 8 | újraértékelés és F-peula sorrendje | RÉSZBEN — két párhuzamos út (PT:290 „mellett”; HUM:455, :482, :509, :515) | felfüggeszti-e a függő újraértékelés a naptárat → programvezető + értékelési felelős | nincs |
| 9 | „min. 3–5 mondatos” (M4.4:26, LMS-M4-09) | NYITOTT | „≥3” vagy 3–5 sáv → értékelési felelős / M4 lektor (HUM-PED-01) | nincs |

## 8. Állapot

- **BSPEC-02: `BUILD_SPEC_OPEN`.** Okok: (1) a 8–20. scope leltára nem futott; (2) a D-1, D-2, D-3 blokkoló emberi
  döntés.
- A 2.1 négy új sora és a 2.2 döntésfüggetlen findingjai a `/course-fix`-ben most is javíthatók; a D-2/D-3-függő
  részek a döntés után.
- `MOODLE-BUILD-VERDICT: NOT_READY` (a `--release-report` szerint: BSPEC-02, 38 besorolatlan checklist-tétel, 4
  fallback nélküli kötelező média). Ez a leltár a verdiktet nem változtatja.
