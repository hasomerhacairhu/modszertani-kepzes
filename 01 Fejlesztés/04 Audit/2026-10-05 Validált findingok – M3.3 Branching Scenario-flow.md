# Validált findingok — M3.3 Branching Scenario-flow (2026-10-05)

> **Audit trail, nem kánon.** `/course-review M3.3 --lens implementation`, egy verifier-körrel (SKILL §5; git-history
> nélkül, „baseline ismeretlen”). Döntési háttér: D-g (a) — `2026-10-05 Projektgazdai döntések – MAN completion és
> mentor-láthatóság D-e…D-j.md` 1. és 4. szakasz. Kapcsolódó: `2026-10-05 Validált findingok – MAN completion és
> mentor-láthatóság.md` IMPL-3 (az M3.3 linearitását ez a kör ellenőrizte). Javítás nem történt, commit nincs.
> Munkaág: `fix/moodle-build-hardening` @ `9ef2b25`.

## 1. Scope és lencse

- Scope: `02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md`
  (950 sor, teljesen olvasva; mind a négy szcenárió minden ágával: S1 :460–510, S2 :514–543, S3 :632–657, S4
  :661–705). H5P-forrás: `h5p-branching-scenario` és `h5p-branching-question` `semantics.json` (WebFetch; a verifier
  szúrópróbával megerősítette). A Moodle `mod_h5pactivity` grade-viselkedése nem lekérve (G3b runtime-kérdés).
- **Kötelező biztonság-jog lencse kimaradt** az explicit `--lens implementation` miatt (M3, gyermekvédelmi lecke).
  A reviewer a gyermekvédelmi tartalmat nem értékelte.
- Verifier: mind a 8 finding verdiktet kapott (a verdiktsorokból számolva): 7 MEGERŐSÍTVE (ebből 1 bizonyíték-kapu),
  1 EMBERI DÖNTÉS, 0 ELVETVE. A verifier összesítő mondata („6 MEGERŐSÍTVE”) elszámolás; a sorok az irányadók.
  Valódi duplikátum nincs; az M33-IMPL-1 a gerinc (az -2, -3, -7 egyes elemei benne vannak).
- Cap (egy fájl: 15): `LEVÁGVA: 0`.

## 2. Válaszok a fókuszkérdésekre

1. **Minden út a végképernyőn ér véget?** A forrásból nem bizonyítható: egyetlen alternatívának sincs célcsomópontja,
   végképernyő nincs definiálva; a H5P BranchingQuestion `nextContentId` alapértéke `-1` (végképernyő).
2. **A végképernyő egybeesik a completion-feltétellel?** Nincs rögzítve; pontozott BS-nél a grade a végképernyőn megy
   át, és a végképernyő a SLIDE 6–7 után állhat csak (M33-IMPL-2).
3. **Pontozott BS + „Receive a grade” determinisztikusan kifejezi?** Ma nem: a pontozási mód nincs rögzítve (a BS
   alapértéke `"scoringOption" … "default": "no-score"` — az IMPL-3 bizonyítéka), és a csomóponttérkép hiányzik.

## 3. Validált findingok (objektív)

| ID | Súly | Hely | Probléma | Javítási korlát |
|---|---|---|---|---|
| M33-IMPL-1 | P1 | M3.3 :470–543, :639–698, :512, :545, :659, :707; RA :72 | nincs célcsomópont, szcenárió-átmenet és végképernyő; a korai végképernyő (hamis completion, a kapu belépőfeltétele is) nincs kizárva | a §3 elején fix sorrendű csomóponttérkép (SLIDE 1–3 CP → S1–2 instrukció → S1-K1 → S1-K2 → biztonsági csomópont(ok) → S2-K1 → S2-K2 → S3–4 instrukció → S3-K1 → biztonsági csomópont → S4-K1 → S4-K2 → biztonsági csomópont → SLIDE 6 → SLIDE 7 → egyetlen végképernyő); minden alternatíva: a meglévő visszajelzés a Feedback-mezőben, Next Content ID = következő csomópont; negatív ID S1–S4-ben tilos; szövegek, ✅, visszajelzések változatlanok; tartalékút tilos (D-g). Levezetés: :458, :629 |
| M33-IMPL-2 | P1 | M3.3 :17–18, :28, :815; MAN :63 | a completion technikai triggere nincs rögzítve; a SLIDE 6–7 kezelése nyitott | :17–18 és MAN :63: completion az egyetlen végképernyő elérésével; a végképernyő a SLIDE 7 után, csak S1–S4 döntési pontjain át; SLIDE 6–7-en át kell haladni, kitölteni nem; „Required to watch” (`forceContentFinished`) = ki. A :18 tartsa meg a hub :254 „Branching végigvitele döntésekkel” kritériumát, csak a mechanizmust tegye hozzá; a hub :254 általános „kérdések megválaszolva” mondata nem olvasható úgy, hogy a SLIDE 7 válaszai kellenek |
| M33-IMPL-3 | P1 | M3.3 :499–506, :508, :651–657, :700–705 | a négy tanulói biztonsági doboz helye a BS-ben nincs megadva; egy alternatíva visszajelzésébe téve a többi ágon nem látszik | minden doboz saját Advanced Text csomópont a közös úton, a kérdés után; szöveg változatlan; :510 nem tanulói szöveg; a :506 forrásmegjelölés nem törölhető, csak a státusza mondható ki; gyermekvédelmi tartalom nem módosul |
| M33-IMPL-4 | P1 | RA :72 (11. pont) | a D-g által megkövetelt negatív runtime tesztek hiányoznak | RA 11 kiegészítése: (a) kilépés S1/S2/S3 után és S4 után a végképernyő előtt → nincs grade/completion; (b) minden alternatíva a következő csomópontra, a csupa ❌-es út is; az egyetlen végképernyőn grade és completion (0 ponttal is); (c) CP-kérdések a végképernyő előtt nem adnak grade-et; (d) „Required to watch” és „Randomize Branching Questions” visszaolvasása |
| M33-IMPL-7 | P2 | M3.3 :51–52, :452–453 | a §3 bevezetője CP-navigációt ír és mind a 7 slide-ot BS-tartalomcsomópontnak nevezi; a BS viselkedési beállításai és a CP-felosztás nincs rögzítve | SLIDE 1–3, 6, 7 CP-csomópont(ok) rögzített felosztással; SLIDE 4–5 instrukció + Branching Question; „Randomize Branching Questions” = ki; „Navigate back” értéke rögzítendő (a „be” csak a CP-korszakbeli „Prev” szóból következik, gyenge); haladásjelző csak CP-n belül (a BS-szintű haladásjelző hiánya nem ellenőrzött) |
| M33-IMPL-8 | P2 | M3 hub :103–105; M3.3 :17 | a hub „3–4 szituációt” és két párhuzamos eszközt ír; a lecke és a hub :116–119 négy szcenáriót, egy BS-befoglalót | a hub :103–105 igazodjon a lecke :17-hez; a szcenáriók tartalma nem változik |

## 4. Emberi döntést igénylő tétel

| ID | Súly | Kérdés | Gazda |
|---|---|---|---|
| M33-IMPL-6 | P2 | Az S1-K2 csomópont (az ágak összefutási pontja) azzal nyit, hogy a beszélgetés folytatódott (:485), ami az S1-K1 C) ága (:474, elhárítás) után nem igaz. Kell-e — és milyen — narratív átvezetés; új tanulói mondat egy önsértést feltáró gyermekvédelmi szcenárióban nem vezethető le a forrásból | projektgazda (pedagógia); Memuna-QA |

Az M33-IMPL-1 a C-ágat is az S1-K2-re vezeti; ettől a build determinisztikus, a narratív koherencia kérdése az
M33-IMPL-6.

**Eldöntve (2026-10-05):** „ne kerüljön új learner-facing bridging mondat a C ág után; a meglévő safeguarding szöveg
maradjon változatlan, csak a flow-node kapcsolat változhat” — `2026-10-05 Projektgazdai döntések – MAN completion és
mentor-láthatóság D-e…D-j.md`, 6. szakasz.

## 5. Bizonyíték-kapu

- **M33-IMPL-5** (G3b, #3): RT-P0-11 és RT-P0-05 a célkörnyezetben, az M33-IMPL-4 negatív eseteivel; környezeti
  rekord. Megvalósítási döntés: projektgazda jóváhagyta (D-g a); a runtime-bizonyíték függő, és a hiánya a D-g 4.
  szakasza szerint nem tartja nyitva a BSPEC-05 sorát.

## 6. Az LMS-M3-03 lezárhatósága a D-g (a) szerint (verifier, Q2)

Akkor zárható `BUILD_SPEC_RESOLVED`-ra, ha rögzítve van: M33-IMPL-1, -2, -3, -7; a korábbi IMPL-3 sorszintű része
(pontozott BS, „Receive a grade” passing grade nélkül, indokolt „nincs tartalékút”); a D-g visszanyitási feltétele a
sor szövegében. Egy paraméter nem vezethető le közvetlenül a forrásból: a BS `scoringOption` (statikus vagy
dinamikus) és az ebből adódó maximális pontszám. Technikai választás, feltétellel: a csupa ❌-es út is nem üres
grade-et adjon; ha a választás tanulónak látható pontszám-jelentést hozna, a `/course-fix` álljon meg. A Moodle-oldali
attempt- és grade-módszer nem ellenőrzött (bizalom: közepes).

## 7. Következő lépés

A 3. pont findingjai a BSPEC-05 LMS-M3-03 sorának tartalma → a BSPEC-05/06/07 `/course-fix` csomagjába. Előtte
ajánlott a kimaradt biztonsági lencse (`/course-review M3.3 --lens safety`), mert az M33-IMPL-1 és -3 a
gyermekvédelmi szcenárió szerkezetét és a biztonsági dobozok helyét érinti. → Lefutott: 8. pont.

## 8. Biztonság-jog lencse (`/course-review M3.3 --lens safety`, 2026-10-05)

Fókusz: az M33-IMPL-1, -2, -3 gyermekvédelmi hatása és az M33-IMPL-6 (a projektgazdai döntés a 4. pont szerint).
Olvasva: M3.3 :1–55, :324–368, :448–707, :795–815 és a kánoni helyek; nem részleges. Egy verifier-kör: 8 finding,
a verdiktsorokból számolva 5 MEGERŐSÍTVE (ebből 1 bizonyíték-kapu), 3 EMBERI DÖNTÉS, 0 ELVETVE. A verifier nem
ellenőrizte: M3 hub :254, RA :47/:72, RT-P0-07, M3.B :330, RR :24 (bizalom: közepes).

### 8.1. Validált findingok (objektív)

| ID | Súly | Hely | Probléma | Javítási korlát |
|---|---|---|---|---|
| SAFE-2 | P2 (P1-ről) | M3.3 :329, :348; 3. pont M33-IMPL-2, -7 | nincs rögzítve, hogy a SLIDE 3 HUM-SAFE-03 blokkja az activityn belül az S1 előtt megjelenik (a Moodle intro címkéjében, :41, a H5P előtt már áll) | a build-specben (az M33-IMPL-7 csomópont-felosztásában) a SLIDE 3 saját, egydiás CP-csomópont a lineáris úton, az S1–2 instrukció előtt; a SLIDE 1–3 közös CP-jén bekapcsolt „Required to watch”-felülírás kerülendő (a CP „finished” állapota nem igazolt, a kérdések kötelezővé válhatnak); szöveg, hely és completion nem változik |
| SAFE-3 | P1 | M3.3 :506; 3. pont M33-IMPL-3 | a :506 státusza nyitott; tanulói csomópontba téve a „Képzőnek … egyeztesd a Memunával” az akut utat feltételesnek mutathatja | a 🛠 jel és a „Képzőnek” megszólítás alapján (a repóban a 🛠 következetesen képzői/fejlesztői jegyzet) a :506 nem tanulói szöveg, mint a :510; a fájlban szó szerint marad; a tanulói csomópontba a :499–505 kerül; az „egyeztesd” mondat szükségessége a Memuna G1-átnézésére tartozik |
| SAFE-5 | P2 | 3. pont M33-IMPL-4; RA :72 | az RA 11 tesztjei nem nézik a biztonsági csomópontok megjelenését és sorrendjét | RA 11 pozitív esete: a csupa ❌-es és a csupa ✅-es úton a SLIDE 3 blokk és a négy biztonsági csomópont megjelenése és sorrendje; a D-g visszanyitási feltétel erre is vonatkozik; szöveg és completion nem változik |
| SAFE-6 | P2 | HUM :494; D-e…D-j :5 | a 2026-10-05-i D-g és az M33-IMPL-6 döntés csak a 04 Audit jegyzőkönyvben | új datált HUM-szakasz szó szerint (a D-a…D-j és az M33-IMPL-6 döntéssel együtt, lásd IMPL-8 a MAN-review-ban), a jegyzőkönyvre hivatkozva; utólagos ellenőrző csak ha a jegyzőkönyv megnevez, egyébként „—” |

### 8.2. Emberi döntést igénylő tételek

| ID | Súly | Kérdés | Gazda |
|---|---|---|---|
| SAFE-1 | P1 | Hogyan érvényesül a HUM-SAFE-03 indoklás nélküli passza és szünete egy kötelező, tartalékút nélküli online BS-ben (az S1 önsértés-feltárás és az S3 kihagyhatatlan; aki passzol, completion nélkül marad, és az M3.4 és az M3-kapu belépőfeltétele elakad); van-e egyenértékű alternatíva, és az a D-g kerülőút-tilalma alá esik-e; mi lesz a félbehagyott M3.3-mal; a második személyű, segítő szerepű BS belefér-e a GK §2 „harmadik személyű esetelemzés” alapértelmezésébe. Új alkalmazási eset (HUM-SAFE-03 + D-g). | projektgazda (D-g); Memuna és programvezető (HUM-SAFE-03 vétó/QA) |
| SAFE-4 | P2 | Az S1-K1 C) ága új mondat nélkül melyik csomópontra vezessen: a következőre (S1-K2; a feltárás folytatódik az elhárítás után) vagy vissza az S1-K1-re (szöveg nélkül; módosítja az M33-IMPL-1 „következő csomópont” és az M33-IMPL-4(b) „csupa ❌-es út” korlátját). A 6. szakasz döntésének betűjén belüli új alkalmazási eset, nem újranyitás. Ha marad a következő csomópont: maradék kockázat a Memuna G1-átnézésében. | projektgazda (flow); Memuna (QA) |
| SAFE-7 | P1 (bizalom: alacsony) | Az S1 23:15-ös 1:1 privát üzenetben zajlik, a csatorna (személyes vagy szervezeti) és a másik felelős tudta nincs megadva; ütközik-e a ✅ B a HUM-SAFE-02 kvízkulcsával és a (b) kivétellel. Új alkalmazási eset, nem a HUM-SAFE-02 újranyitása; a ✅ és a szöveg a döntésig nem változik. | Memuna (HUM-SAFE-02 vétó/QA) |

**Döntések (2026-10-05):** SAFE-1 eldöntve (passz-út minden érzékeny scenario előtt; completion: S1…S4 mindegyike
„completed OR passed” → post-scenario tartalom → FINAL; szünet/félbehagyás; a második személyű framing fikciós
„helper-role case analysis”); SAFE-4 eldöntve (Option 1: C → meglévő feedback → S1-K2, új mondat és visszavezetés
nélkül); SAFE-7 nyitva (Memuna-QA, learner-release előtt kötelező; a staging buildet nem blokkolja; a ✅ változatlan).
Az LMS-M3-03 BSPEC-05-része újranyitottnak tekintendő a passz-csomóponttérkép rögzítéséig. Forrás: `2026-10-05
Projektgazdai döntések – MAN completion és mentor-láthatóság D-e…D-j.md`, 7. szakasz.

### 8.3. Bizonyíték-kapu

- **SAFE-8** (G1, #1): a Memuna írásos „átnéztem” bejegyzése (M3.3 :9 szerint nincs rögzítve); a tárgya a stagingben
  felépített BS legyen; a SAFE-1, -3, -4, -7 maradék kockázata ide tartozik. A tanulói release-t blokkolja, a buildet
  nem.

### 8.4. Verifier-válaszok

- **Q1 — a SAFE-1 és az LMS-M3-03 lezárása:** a D-g név szerint jóváhagyta az LMS-M3-03-ra a „nincs független
  tartalékút” megoldást; a sor a D-g (a) szerint spec-szinten `BUILD_SPEC_RESOLVED` lehet a 6. pontban felsoroltakkal,
  így a SAFE-1 a build-verdiktet nem tartja nyitva, a tanulói release-t viszont blokkolja (HUM-SAFE-03, G1). Feltétel:
  ha a SAFE-1 döntése BS-en belüli alternatív csomópontot vagy szerkezetváltozást hoz, a sort újra kell nyitni vagy
  módosítani; ajánlott a SAFE-1-et függő kapcsolatként a sor szövegébe írni a D-g visszanyitási feltétele mellé. A
  döntés nem hozhat be a D-g által tiltott kerülő utat. Bizalom: közepes; hogy a lezárást szervezetileg kivárják-e,
  projektgazdai mérlegelés.
- **Q2 — a SAFE-2/-5 és az M33-IMPL-2/-4 összeférése:** a SAFE-2 a H5P szintjén összefér (globális „Required to
  watch” = ki; a SLIDE 3 saját egydiás CP-csomópontja a lineáris úton mindenképp megjelenik; a SLIDE 6–7 kezelése
  érintetlen). A SAFE-5 teljesen összefér.
