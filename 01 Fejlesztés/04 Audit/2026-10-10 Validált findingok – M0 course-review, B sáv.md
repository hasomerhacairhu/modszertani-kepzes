# 2026-10-10 Validált findingok – M0 `/course-review`, B sáv

> **Mentés:** 2026-10-10, a projektgazda jóváhagyásával: „Írd be a teljes M0 és M1 riportot az `01 Fejlesztés/04 Audit/`
> mappába, változtatás nélkül”. A riport és a mellékletek a munkamenet ideiglenes munkaterületéről, tartalmi változtatás
> nélkül kerültek át.
>
> **Státusz:** audit trail — nem kánon, nem tanulói tartalom. Read-only review; a tananyag nem változott.
>
> **Szerkezet:** I. a validált riport (szó szerint); A. melléklet: a verifier-kontextus (szabályok, klaszter-térkép) —
> a riportban `VERIFY-CONTEXT.md`; B. melléklet: a verifier verdiktjei (40/40) — a riportban `VERIFY.md`; C. melléklet: a négy lencse nyers findingjai (40), elvetett hipotézisei és forrásai — a riportban `ALL.md`.
>
> **Gépi normalizálás (tartalmi változás nélkül):** a helyi abszolút útvonal-előtag repó-relatívra rövidítve; a verifier-kimenet két ideiglenes fájlútja a megfelelő melléklet nevére cserélve.
>
> **A mentés után, 2026-10-10:** a projektgazda jóváhagyta az N-M1-04 (M1) P0 adatvédelmi freeze-kivételét; az átvezetés külön `/course-fix` futásban történik. A riport M0-besorolásait ez nem érinti.

---

# M0 – `/course-review` validált riport (2026-10-10)

> Read-only review. Tananyag nem változott. Nyers findingok: `ALL.md` (40), verdiktek: `VERIFY.md` (40/40). Git-history
> nem állt rendelkezésre (baseline ismeretlen). A hipotézisek forrása az Anna-mátrix és a külső specifikáció; egyik sem kánon.

## 1. Scope és futtatott lencsék

- **Scope:** a teljes M0 (6 fájl: hub, M0.1–M0.4, M0.A).
- **Lencsék:** pedagógia, értékelés, implementáció, biztonság-jog (a biztonság-jog kötelező is volt: 49 trigger-találat).
  Nyelvi lencse nem futott (nem kérték). Az implementációs lencse lépéskorlátba futott, folytatással teljes riportot
  adott; RÉSZLEGES pontjai: a Command 5 napló, a fórum JIT-doboza, a QUIZ-D review options, a PT :221 alt-szövegek, a
  6. item Matching-megvalósíthatósága nem lett végignézve.
- **Mérce:** a pilot minőségi küszöbe (2026-10-05, :55–77) és a freeze-kivétel (2026-10-10, :41: csak P0 biztonsági,
  adatvédelmi, hozzáférhetőségi vagy előrehaladást blokkoló hiba). **A pilot 2026-10-10-én elindult**: minden
  PILOT-BLOCKER futó pilot alatti teendő.

## 2. Validált objektív findingok (18, duplikátumok összevonva)

| ID (összevont) | Prio | Hely | Probléma | Javítás és korlát | Pilot |
|---|---|---|---|---|---|
| **ERT-1** (=PED-1, BIZT-4, IMPL-1) | P1 | M0.4:298–333; M0.2:270–279 | M0.4 SLIDE 3: az 1. és 3. helyzet téves (A) opciójához nincs visszajelzés, holott a :300 válaszonkéntit ír elő; a közös helyes-szöveg elárulja a 2–3. helyzetet. M0.2 SLIDE 3: a 2. kérdés előírt kiemelt visszajelzése hiányzik. (A SLIDE 5-rész elvetve.) | `/course-fix`: egymondatos téves visszajelzés a meglévő mondatokból (:325–329, :416–419; hub :240), a helyes-szöveg helyzetenként bontva; M0.2 Q2 saját visszajelzés a :275-ből. ✅, opciók, helyzetek változatlanok; pin; G1 Memuna-hatály. | POST-PILOT (Memuna eltérő minősítése esetén freeze-kivétel) |
| **ERT-2** (=IMPL-4) | P1 | MAN:17, :44, :155; hub:181; RA:71 | Az M0 completion-sorai megválaszolást írnak, a mechanizmus nem kényszeríti ki (QUIZ-D „attempt submitted”; H5P-C összefoglaló dia megválaszolatlanul is küld — forráskódból igazolva). | Negatív esetek az RT 9. pontjába / új QUIZ-D pont; az LMS-M0-06 rögzítse a ténylegesen működő ágat (hub :181). Cut-score-mentesség, BSPEC-06 változatlan. | POST-PILOT; a negatív runtime-teszt most, szerkesztés nélkül elvégezhető |
| **IMPL-2** (=ERT-6) | P1 | M0.3:159, :177; hub:254–260; PT:219; MAN:8, :114–133 | A tanulói szöveg és a lezárt 7. kvízitem kulcsa szerint a peulák a Moodle-kurzusban vannak; a manifest egyetlen peula-elemet sem specifikál (hiány, nem ellentmondás). | MAN „Kurzusszintű elemek”: modulonkénti „Peulák” leíróelem (nem activity, cmid/completion nélkül); a leírás tartalma az N-M4-07-től függ; képzői peulaszöveg nem kerülhet tanulói nézetbe. | POST-PILOT; a programvezető ellenőrizze, hogy a pilot közli-e az M0.A időpontját |
| **IMPL-5** | P1 | MAN:267, :220; hub:176 | A §7 határidőt ír az M0 kvízre, de nem mondja meg, célidő-e vagy zárás; „Close the quiz” esetén a késve érkező nem teljesítheti az M0-t → az M1 zárva marad (ellentmond a puha kapunak). Az M0 sorban felesleges „Megerősítés”. | §7: az M0_QUIZ/M0_FORUM határideje kommunikált célidő (kvízen nincs „Close”, fórumon nincs „Cut-off”); az M0 „Megerősítés” = nincs. | **Feltételes PILOT-BLOCKER**: üzemeltetési ellenőrzéssel most, repóváltozás nélkül elhárítható; a manifest-pontosítás POST-PILOT |
| **ERT-9** (=IMPL-6 b) | P2 | M0.2:195–204 | A SLIDE 2 Multi Choice opciói nincsenek megírva („felsorolásból 3–4 mondat (pl. …)”); egyes számú kérdés többválaszos típussal. | Opciók szó szerint a :187, :190, :192-ből; kérdés és típus összhangban; nem completion-elem marad. | POST-PILOT; **ha a renderelt pilotban helykitöltő látszik: PILOT-BLOCKER** (freeze-kivétel) |
| **ERT-7** (=PED-4) | P2 | hub:229–231; M0.3:253–257 | A 4. kvízitem kulcsa az F-peulára épül, a visszajelzés az M0.3 5. diájára mutat, ahol a fogalom nincs. | M0.3 SLIDE 5: egy mondat a lezárt szabályról (PT:242 / MAN:149), vagy a hivatkozás csak a Glosszáriumra. Item, kulcs változatlan. | POST-PILOT |
| **ERT-8** (=PED-2, IMPL-6 d) | P2 | M0.1:330–351 | Az M0.1 SLIDE 5 cím, instrukció, darabszám és visszajelzés szétcsúszik (CC-04). **A CC-04 döntés nincs átvezetve** az `Emberi jóváhagyás szükséges.md`-be. | Tartalom: CC-04 szerint POST-PILOT. Átvezetés: objektív, a 2026-10-10-i jegyzőkönyvből. | POST-PILOT |
| PED-3 | P2 | M0.1:17–19 | A mikrocél a 9 állomás kódos felsorolását és modulonkénti összefoglalását ígéri; a lecke egyiket sem gyakoroltatja/méri. | A mikrocél igazodjon a hub 1. kompetenciájához és a 6. item szintjéhez; a 6. item és kulcsa változatlan. | POST-PILOT |
| PED-5 | P2 (verifier) | M0.A:152–157, :340–363, :420–451, :643–648 | A lépésenkénti percek nem férnek a blokkidőbe (Blokk 2: 16–21′ a 15′-be; Blokk 3: 13–18′); a 45′-es változat nem ad lépésszintű vágást, és nem védi a „madrih, nem terapeuta” lépést. | Lépésszintű vágási terv a meglévő sávokból (új percszám nélkül); a Blokk 3 3. lépése a megtartandók közé. 45′/60′ keret változatlan. | POST-PILOT |
| PED-6 | P2 | M0.1:414 | A tanulói szöveg kilépés nélkül ígéri, hogy a privát várakozást a zárókörben hangosan kimondja; az M0.A-ban egy szó, passzal. | A mondat igazodjon az M0.A menetéhez és a passzhoz. | POST-PILOT |
| PED-10 | P2 | M0.4:554 | Feltétel nélkül állítja a kickoff-részvételt, holott az M0.3 dátummal nyit, és nincs pótlás. | Feltételes mondat + utalás a „Segítség és kapcsolatok” blokkra. | POST-PILOT |
| BIZT-6 | P2 | M0.4:146–171 | A SLIDE 1 a DM-et/voice chatet a madrih-szerep tereként sorolja, „Oké.”-val nyugtázza; a HUM-SAFE-02 szabály csak a SLIDE 4-en jön. | A :419 kánoni mondata szó szerint a SLIDE 1 visszajelzésébe. | POST-PILOT |
| BIZT-8 | P2 | M0.4:501, :565 | „a csoportnak látszik” pontatlanabb a §11 :245 kánoni mondatánál. | A §11 mondata szó szerint, runtime-visszaolvasáshoz kötve. | POST-PILOT |
| BIZT-10 | P2 | M0.2:467 | A fejlesztői élesítési feltétel csak a Memunát és a mentort kéri, a helyettest és a PILOT-3 négy szerepét nem. | GK :147 / PILOT-3 szerepköre szó szerint; név, elérhetőség nem. | POST-PILOT |
| BIZT-11 | P2 | M0.1:51 | A „Memuna” első előfordulása a kötelező blokkban, a GK :80 formulája nélkül. | A formula a blokk elé (a blokk szövege szó szerint változatlan). | POST-PILOT |
| IMPL-6 (a, c) | P2 | M0.4:11; M0.3:337 | A „Single Choice” típusnév a Single Choice Set felé kétértelmű; az M0.3 SLIDE 7 közbülső skálapontjai címke nélkül. | Valós típusnév (MC egyválaszos mód); a közbülső pontok kimondottan címke nélküli számok. | POST-PILOT |
| IMPL-7 | P2 | MAN:41–44 ↔ M0.4:551/:562, hub:138, M0.3:364, M0.2:508 | Ugyanaz az activity háromféle néven. | Egységesítés a manifest „Név” oszlopához. | POST-PILOT |
| IMPL-8 | P2 | M0.3:162, :183 ↔ hub:260 | „pipa a modul mellett” ↔ a saját kvízkulcs „a leckék/activityk mellett”. | A diaszöveg igazodjon a kulcshoz. | POST-PILOT |

## 3. Emberi döntést igénylő tételek (7) — javasolt szöveg nélkül

| ID | Kérdés | Ki dönt | Pilot |
|---|---|---|---|
| **BIZT-7** | A bemutatkozó fórumposzt/-válasz megőrzési ideje és §3-sora; az M0 „Bemutatkozó fal” külön review-jának eredménye; elfogadható-e a pilotban a megőrzési tájékoztató hiánya. A Program terv :228 szerint rögzített megőrzés nélkül adatgyűjtő activity nem nyitható meg. | DPO / jogi felelős | **PILOT-BLOCKER**; a tájékoztató szövegéhez freeze-kivétel (projektgazda) |
| **BIZT-3** | Kiterjed-e a SAFE-7 (HUM :567, „learner release előtt kötelező lezárni”) az M0.4 SLIDE 3 2. helyzetére (késő esti 1:1 üzenet; a ✅ egy kiskorúnak küldött privát válasz)? | Memuna (HUM-SAFE-02 QA) | **Feltételes PILOT-BLOCKER**; szövegváltozáshoz freeze-kivétel |
| BIZT-5 | A csoportchat-szívatás minden esetben Memuna-jelzés (M0.2), vagy csak súlyosság felett (M0.4, belépőkvíz)? | Memuna | POST-PILOT |
| BIZT-9 | Kötelező-e az M0.A-n két felnőtt jelenléte (felkavart kiskorú mellé felnőtt + a kör folytatása)? | programvezető + Memuna | POST-PILOT; a személyzeti döntés operatívan most meghozható |
| PED-8 | Kapjon-e egyéni, támogató utánkövetést, aki a belépőkvíz 1–2. itemét elsőre tévesen válaszolja; ki láthatja ehhez az egyéni válaszokat? | programvezető + Memuna; DPO (adatkör) | POST-PILOT |
| IMPL-3 | A H5P-C completion jelentése: „az összefoglaló dia elérése” (és a leckék Completion-sorai ehhez igazodnak), vagy a megválaszolás kikényszerítése (szerkezeti átépítés)? | projektgazda; értékelési felelős QA | POST-PILOT |
| ERT-3 | A pontozatlan választók completion-elve (D-d/D-i) általános, vagy csak a felsorolt tételekre szól? (Az M0.1 completionje csak pontozatlan választókból áll.) | projektgazda; értékelési felelős QA | POST-PILOT; **PILOT-BLOCKER, ha az M0.1 completion a pilotban nem áll be** |

## 4. Bizonyíték-kapuk (3) — nem mennek `/course-fix`-be

| ID | Mi hiányzik | Szerep / kapu | Pilot |
|---|---|---|---|
| **BIZT-1** | A Memuna írásos „átnéztem” bejegyzése az M0 gyermekvédelmi elemeire (M0.2 SLIDE 3–4, M0.4 SLIDE 2–4, belépőkvíz 1–2., M0.A mini-protokoll); a GK :17 szerint nélküle nem nyithatók meg valódi madrihoknak. | Memuna · G1 · tracker #1 | **PILOT-BLOCKER** (ha a bejegyzés a repón kívül megvan, elég rá hivatkozni) |
| **IMPL-9** (=BIZT-2) | A „Segítség és kapcsolatok” blokk tényleges kitöltése a pilot-Moodle-ben (négy szerep, a Memuna és a helyettese külön); RT-17 visszaolvasás tanulói fiókkal. | LMS-gazda · G8/G4b · tracker #4 | **PILOT-BLOCKER** (üzemeltetési, freeze-kivétel nem kell) |
| ERT-4 | A belépőkvíz projektgazdai itemszövegének utólagos QA-ja (értékelési felelős; az 1–2. itemnél a Memuna) — megfigyelés a QA-csomagba: az 1., 2. és 5. item kulcsa hossz alapján kitalálható, a 2. item kulcsa a „jóváhagyott” szót tartalmazza. Answer key-módosítást nem javaslunk. | értékelési felelős, Memuna | POST-PILOT |

## 5. Elvetve

- P1: **ERT-5** — az M0.1-része a PED-3 duplikátuma; a hub 2.2/2.5 mérés nélkülisége a lezárt D-4 tanuló-lokális döntésből és a puha kapuból következik.
- P2: 3 (PED-7 ízlésbeli; PED-9 pedagógiai preferencia; ERT-10 item-írási preferencia).

## 6. Következő lépés

**A futó pilothoz most (repóváltozás nélkül):**
1. Memuna: G1 „átnéztem” az M0 gyermekvédelmi elemeire (BIZT-1), és döntés a BIZT-3-ról.
2. LMS-gazda, pilot-Moodle: a „Segítség és kapcsolatok” blokk visszaolvasása (IMPL-9); az M0 kvíz határideje ne „Close the quiz” legyen (IMPL-5); az M0.1 completion beáll-e (ERT-3); az M0.2 SLIDE 2 renderelt opciói (ERT-9); az ERT-2 negatív tesztjei.
3. DPO: a fórum megőrzési sora és a tájékoztató (BIZT-7).

**Freeze-kivételhez kötött tananyag-módosítás** (projektgazdai döntés): BIZT-7 tájékoztatója; BIZT-1/BIZT-3, ha a Memuna szövegváltozást kér; ERT-9, ha a renderben helykitöltő látszik.

**POST-PILOT `/course-fix`** (a pilot-visszajelzéssel együtt): ERT-1, ERT-7, ERT-9, PED-3, PED-5, PED-6, PED-10, BIZT-6, BIZT-8, BIZT-10, BIZT-11, IMPL-6, IMPL-7, IMPL-8; manifest: IMPL-2, IMPL-5, ERT-2. **Átvezetés** (objektív): a CC-04 döntés a HUM-fájlba (ERT-8).

---

# A. melléklet – verifier-kontextus

# M0 verifier — kontextus és klaszter-térkép (fő munkamenet, 2026-10-10)

A findinglista: `ALL.md` (ugyanebben a mappában), 40 finding: PED-1…10, BIZT-1…11, IMPL-1…9, ERT-1…10.

## Szabályok, amelyekhez mérni kell

- Lezárt döntés és bizonyíték-kapu: `.claude/rules/safety-and-human-gates.md` „Lezárt döntések”.
- **Git-history nem áll rendelkezésre.** A „restauráció vagy baseline” kérdésre a válasz „baseline ismeretlen”; a súlyosság emiatt nem emelkedik.
- **Pilot minőségi küszöb** (2026-10-05): `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntés – pilot-ütemezés és M0+M1 freeze.md` :55–77 — „Pilot előtt nem halasztható” lista és „Pilot utánra halasztható” lista.
- **Freeze-kivétel** (2026-10-10): `01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntések – Anna-megfeleltetés indítása, M0.1 POST-PILOT, Moodle-összevetés.md` :41 — „Freeze-kivételt csak tényleges P0 biztonsági, adatvédelmi, hozzáférhetőségi vagy a tanulói előrehaladást blokkoló hiba indokolhat.” Ugyanott: M0.1 SLIDE 5 (CC-04) = POST-PILOT; a Moodle-összevetés külön build/runtime feladat.
- A pilot 2026-10-10-én elindult: egy mai PILOT-BLOCKER futó pilot alatti javítást jelent, freeze-kivétellel. Ahol egy PILOT-BLOCKER csak a tágabb 2026-10-05-i küszöbre támaszkodik (nem P0 a 2026-10-10-i értelemben), a freeze-kivétel projektgazdai döntés — ezt jelöld.
- Repón kívüli állapotot (Moodle-konfiguráció, Memuna-bejegyzés a repón kívül) a reviewerek nem láthattak: ahol a finding a repón kívüli bizonyíték hiányára épül, a helyes típus `bizonyíték-kapu`, nem objektív tananyaghiba.

## Klaszterek (egy tényállás, több lencse) — egyszer ellenőrizd, de minden ID kapjon verdiktet; jelöld a megtartandót

| Klaszter | Findingok | Tárgy |
|---|---|---|
| K1 | PED-1, BIZT-4, IMPL-1, ERT-1 | M0.4 SLIDE 3: az 1. és 3. helyzet A opciójának nincs téves visszajelzése; összevont helyes-visszajelzés (N-M0-14). ERT-1 a SLIDE 5-öt és az M0.2 2. kérdését is említi. |
| K2 | IMPL-2, ERT-6 | A peulák helye a Moodle-kurzusban (M0.3:159/:177, kvíz 7. item ↔ manifest). |
| K3 | BIZT-2, IMPL-9 (+BIZT-10) | „Segítség és kapcsolatok” blokk: runtime-bizonyíték hiánya (PILOT-3); BIZT-10 az M0.2:467 feltétel szövege. |
| K4 | IMPL-3, IMPL-4, ERT-2, ERT-3 | Completion-mechanizmus: H5P-C összefoglaló dia; kvíz „mind a 7 item”; pontozatlan választók. |
| K5 | PED-2, ERT-8 (+IMPL-6 d) | M0.1 SLIDE 5 (CC-04, POST-PILOT). |
| K6 | PED-4, ERT-7 | A 4. kvízitem F-peula-hivatkozása ↔ M0.3 SLIDE 5. |
| K7 | ERT-9, IMPL-6 (b) | M0.2 SLIDE 2 opciói nincsenek megírva. |
| K8 | PED-3, ERT-5 | M0.1 mikrocél ↔ gyakorlás/mérés. |

Egyedi findingok: BIZT-1, BIZT-3, BIZT-5, BIZT-6, BIZT-7, BIZT-8, BIZT-9, BIZT-11, PED-5, PED-6, PED-7, PED-8, PED-9, PED-10, IMPL-5, IMPL-6 (a, c), IMPL-7, IMPL-8, ERT-4, ERT-10.

## Mit kérünk minden findingnál (a verifier saját utasításain felül)

- verdikt (MEGERŐSÍTVE / ELVETVE / EMBERI DÖNTÉS) és típus;
- a **Pilot-besorolás** helyes-e (PILOT-BLOCKER / POST-PILOT), a fenti két szabály szerint; ha PILOT-BLOCKER, kell-e hozzá tananyag-módosítás (→ freeze-kivétel, projektgazdai döntés) vagy csak runtime/üzemeltetési lépés;
- duplikátumnál: melyik a megtartandó ID.

---

# B. melléklet – verifier-verdiktek (40/40)

M0 adverzális ellenőrzés kész: mind a 40 finding verdiktet kapott, egyik sem maradt ki. Minden hivatkozott helyet visszaolvastam a repóban. A H5P `summary-slide.js` állítást (IMPL-3, ERT-2) a forráskódban ellenőriztem: a `triggerXAPICompleted` hívás feltétele csak a `!isSolutionMode && !ignoreResize`, a megválaszolást nem vizsgálja. A MoodleDocs-idézeteket (IMPL-4, IMPL-5, IMPL-8) nem nyitottam meg külön. Git-history nincs, ezért a baseline mindenhol ismeretlen, és a súlyosság ettől nem emelkedett.

**Findingonként** (`ID · verdikt · típus · Pilot-besorolás · indok · duplikátum`)

- PED-1 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.4:323–333-ban az 1. és a 3. helyzet A opciójához nincs téves visszajelzés, a közös helyes-szöveg pedig a 2. és a 3. helyzetre is utal. · (duplikátum: ERT-1)
- PED-2 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes (CC-04) · Az M0.1:330–351-ben a cím, az instrukció („1–2 modul”, kíváncsiság vagy félelem), a „max. 2–3” jegyzet és a csak kíváncsiságra reagáló visszajelzés szó szerint szétcsúszik. · (duplikátum: ERT-8)
- PED-3 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.1:17–18 mikrocélja a 9 állomás kódos felsorolását ígéri; a :205 tiszta input, a SLIDE 5 csak felismertet, a 6. item 3 témát párosít. · (K8 megtartandó)
- PED-4 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.3:257-ben nincs F-peula. A Bizonyíték idézete csonka: a hub :231 a Glosszárium F-peula-szócikkére is mutat, ezt ERT-7 pontosan idézi. · (duplikátum: ERT-7)
- PED-5 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.A-ban a Blokk 2 lépései 16–21’, a Blokk 3-éi 13–18’ a 15’-es (45’-nél 10’-es) sávban; a :643–648 nem védi a Blokk 3 3. lépését. A súlyosság inkább P2. A javítás csak a meglévő lépéssávokból dolgozhat, új percszámot nem találhat ki.
- PED-6 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.1:414 szerint a zárókörben hangosan kimondod a leírt várakozásodat, az M0.A zárókörében viszont induló-szó van, passz-lehetőséggel (:497, :501).
- PED-7 · ELVETVE · — · — · Ízlésbeli kérdés. A SLIDE 7 szándékosan sűrít (a cél a :388-ban), az „1–2 mondat” és az „1 mondat” nem zárja ki egymást, a példák kárát semmi nem bizonyítja; a 2026-10-10-i döntés 5. pontja a szükségtelen módosítást kerülteti.
- PED-8 · EMBERI DÖNTÉS · emberi-döntés · POST-PILOT, helyes · Új gyermekvédelmi és adathozzáférési kérdés (egyéni utánkövetés az 1–2. item első téves próbálkozása után), lezárt döntés nem válaszolja meg (HUB:148, :174).
- PED-9 · ELVETVE · — · — · Pedagógiai preferencia. Az M0.4 SLIDE 4 1. szabálya az M0.2:430 megerősítő ismétlése, nem hiba; hogy a lecke „újként vezeti be”, az értelmezés.
- PED-10 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.4:554 feltétel nélkül állítja a kickoff-részvételt, holott az LMS-M0-03 dátummal nyílik (MAN:41), és pótló peula nincs (M0.A:610).
- BIZT-1 · MEGERŐSÍTVE · bizonyíték-kapu (G1, Memuna „átnéztem”) · PILOT-BLOCKER, helyes; tananyag-módosítás nem kell, ha a Memuna szövegváltozást kér, ahhoz freeze-kivétel kell · A GK :17 és az RR :40 alapján az M0 bántalmazásról, önsértésről és a 112-ről tanító elemei (pl. M0.4:422, M0.2 SLIDE 3–4) a Memuna írásos átnézése nélkül nem nyithatók meg; a repóban a G1 nyitott.
- BIZT-2 · MEGERŐSÍTVE · bizonyíték-kapu (G8/G4b, PILOT-3) · PILOT-BLOCKER, helyes; runtime-/üzemeltetési lépés, freeze-kivétel nem kell · HUM :550 és GK :147 szerint a kontaktok kitöltése a pilot feltétele, a repóban erre nincs bizonyíték. · (duplikátum: IMPL-9)
- BIZT-3 · EMBERI DÖNTÉS · emberi-döntés · A PILOT-BLOCKER csak feltételes: a Memuna QA-ja dönti el, hogy a SAFE-7 (HUM :567, „learner release előtt kötelező lezárni”) kiterjed-e erre; szövegváltozáshoz freeze-kivétel kell (projektgazdai döntés) · Az M0.4:311–314 ugyanaz a késő esti, bejövő 1:1 minta, mint a nyitott SAFE-7; ez egy lezárt döntés új alkalmazási esete. A SLIDE 2 (:223) véleménykérdés, kulcsa nincs, ezért irreleváns.
- BIZT-4 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes; ha a Memuna P0-nak minősíti, freeze-kivétel (projektgazdai döntés) · Ugyanaz a tényállás, mint PED-1-nél (:300, :306, :331). · (duplikátum: ERT-1)
- BIZT-5 · EMBERI DÖNTÉS · emberi-döntés · POST-PILOT, helyes · Az M0.2:265 ✅-ja tartalmazza a Memuna-jelzést, az M0.4:307 hallgat róla, a hub :241 „szükség esetén”-t mond. Hogy minden chat-szívatás jelzendő-e, az gyermekvédelmi szabálykérdés, ezért a kétség emberi döntést kér.
- BIZT-6 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.4:163–164 az insta-DM-et és a voice chatet a madrih-szerep tereként sorolja, a :170 „Oké.” korrekció nélkül nyugtázza, a GK :94 szabálya csak a SLIDE 4-en jön. A :419 kánoni mondatának szó szerinti átvezetése objektív javítás.
- BIZT-7 · EMBERI DÖNTÉS · emberi-döntés (DPO) · PILOT-BLOCKER, helyes (adatvédelem; a Program terv :228 kifejezetten tiltja a megnyitást); a tájékoztató szövegéhez freeze-kivétel kell (projektgazdai döntés) · Az Adatvédelem §3 táblájában (:60–73) és a §11 listájában (:247–256) nincs fórumsor, a :79 „külön review” eredménye sincs meg. Ha a Moodle-ben már van megőrzési tájékoztató, az repón kívüli bizonyíték.
- BIZT-8 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.4:501 és :565 „a csoportnak látszik” megfogalmazása pontatlanabb, mint a §11 :245 kánoni mondata, és a Program terv :230 a tényleges Moodle-beállítás szerinti közlést írja elő. Gyengítő körülmény: az Adatvédelem :149 maga is „a csoport látja” formát használ.
- BIZT-9 · EMBERI DÖNTÉS · emberi-döntés · POST-PILOT, helyes (a személyzeti döntés operatívan azonnal meghozható) · Az M0.A:132–133 egyszerre kér felnőttet a felkavart kiskorú mellé és a kör folytatását; hogy kötelező-e a második felnőtt, az gyermekvédelmi szabálykérdés.
- BIZT-10 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.2:467 fejlesztői feltétele csak a Memunát és a mentort kéri, a GK :147 a helyettest, a PILOT-3 négy szerepet; nem duplikátuma a K3-nak.
- BIZT-11 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.1-ben a „Memuna” egyetlen előfordulása a szó szerint kötelező HUM-SAFE-03 blokk (:51), a GK :80 első-előfordulási formulája hiányzik. A blokk szövege nem változhat (GK :102).
- IMPL-1 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Ugyanaz a tényállás, mint PED-1-nél. · (duplikátum: ERT-1)
- IMPL-2 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes; hogy a pilot más csatornán közli-e az M0.A-t, azt a programvezető ellenőrzi · Az M0.3:159, a Program terv :219 és a 7. item kulcsa (hub :260) peulát ígér a Moodle-ben; a manifest kurzusszintű elemei (:114–129) és a §3 (:133) nem adnak hozzá elemet. · (K2 megtartandó)
- IMPL-3 · EMBERI DÖNTÉS · emberi-döntés · POST-PILOT, helyes · A forráskód igazolja: a `summary-slide.js` megválaszolás-ellenőrzés nélkül küldi a completiont, így a leckék „megválaszolás” completion-sorai és a BSPEC-06 mechanizmusa között új jelentésdöntés kell. · (K4: ERT-2 mellett megtartandó a döntési ága miatt)
- IMPL-4 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · A MAN:44 és :155 „mind a 7 item megválaszolva” feltétele ellentmond a QUIZ-D „attempt submitted” profiljának (:17); a hub :181 maga stagingbe utalja. A javaslat a runtime-eredmény előtt ágat választ, ezért ERT-2 eljárása a jobb. · (duplikátum: ERT-2)
- IMPL-5 · MEGERŐSÍTVE · objektív · Feltételes PILOT-BLOCKER, helyes; üzemeltetési ellenőrzéssel (Close the quiz nincs beállítva) repóváltozás nélkül elhárítható, a manifest pontosítása POST-PILOT vagy freeze-kivétel · A MAN:267 határidőt ír, nem mondja meg, hogy célidő vagy zárás; a :220 M0-sorában olyan „Megerősítés” dátum áll, amelyhez az M0-ban nincs lépés.
- IMPL-6 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · (a) A „Single Choice” típusnév (M0.4:11) kétértelmű a Single Choice Set felé (RT :80 is jelzi). (c) Az M0.3:337 közbülső skálapontjainak nincs címkéje. · (a (b) rész ERT-9, a (d) rész ERT-8 duplikátuma)
- IMPL-7 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · A MAN:41–44 nevei eltérnek az M0.4:551/:562, a hub :138, az M0.3:364 és az M0.2:508 neveitől.
- IMPL-8 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Az M0.3:162 és :183 „a modul mellett” pipát ígér, a saját 7. item kulcsa (hub :260) viszont „a leckék/activityk mellett”-et mond: repón belüli ellentmondás.
- IMPL-9 · MEGERŐSÍTVE · bizonyíték-kapu (G8/G4b, RT-17, PILOT-3) · PILOT-BLOCKER, helyes; üzemeltetési és bizonyítéki tétel, freeze-kivétel nem kell · HUM :550 és RR :34 szerint a valódi kontakt RELEASE-EVIDENCE, a repóban nincs igazolva. · (K3 megtartandó)
- ERT-1 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Lefedi a K1-et, és bizonyított többletet ad: az M0.2:279 a 2. kérdés kiemelt visszajelzését írja elő, a :272–273 viszont közös szöveget ad. Az M0.4 SLIDE 5-re vonatkozó rész (véleménykérdés visszajelzés nélkül) nem bizonyított hiba, azt el kell hagyni. · (K1 megtartandó)
- ERT-2 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes; a negatív runtime-teszt freeze-kivétel nélkül elvégezhető · A H5P-C mechanizmusa forrásból igazolt, a QUIZ-D ága a hub :181 szerint staging-kérdés; a javaslat (negatív esetek az RT-be, a működő ág rögzítése) a runtime-elvet követi. · (K4 megtartandó)
- ERT-3 · EMBERI DÖNTÉS · emberi-döntés · POST-PILOT, helyes; PILOT-BLOCKER csak akkor, ha az M0.1 completion nem áll be · A MAN:16 általánosan fogalmaz, a HUM :561 (D-i) tételesen; az M0.1:13 completionje csak pontozatlan választókból áll. Az elv kiterjesztése egy lezárt döntés új alkalmazási esete; nem duplikátum.
- ERT-4 · MEGERŐSÍTVE · bizonyíték-kapu (értékelési felelős; az 1–2. itemnél a Memuna QA-ja) · POST-PILOT, helyes · A hub :180 utólagos QA-jának nincs bizonyítéka; az item-szöveg projektgazdai, ezért a hosszjel-megfigyelés csak a QA-csomagba mehet, a kulcshoz nem nyúlhat. Az 1–2. item Memuna-része átfed BIZT-1-gyel.
- ERT-5 · ELVETVE · — · — · Az M0.1-rész PED-3 duplikátuma. A hub 2.2 és 2.5 elemeinek mérés nélkülisége a lezárt D-4 tanuló-lokális döntésből és a nem vizsga jellegű puha kapuból következik; a kvízterv nem állítja, hogy minden alelem mérve van.
- ERT-6 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Ugyanaz a manifest-hiány, mint IMPL-2-nél. · (duplikátum: IMPL-2)
- ERT-7 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes · Pontos idézet (hub :231 a Glosszárium-hivatkozással); az M0.3 SLIDE 5 nem tanítja az F-peulát, holott a hub :281 ott pótolná. · (K6 megtartandó)
- ERT-8 · MEGERŐSÍTVE · objektív (átvezetés) · POST-PILOT, helyes (CC-04) · A tartalmi hiba valós, és a CC-04 döntés (04 Audit, 2026-10-10, :41) nincs átvezetve az `Emberi jóváhagyás szükséges.md`-be: „CC-04”-re 0 találat. Átvezetendő a döntési jegyzőkönyvből. · (K5 megtartandó)
- ERT-9 · MEGERŐSÍTVE · objektív · POST-PILOT, helyes; ha a rendereléskor helykitöltő látszik, PILOT-BLOCKER, freeze-kivétellel · Az M0.2:199-ben az opciók nincsenek megírva, a :197 egyes számú kérdése mellett a típus Multi Choice. · (K7 megtartandó)
- ERT-10 · ELVETVE · — · — · Az M0.3:193 egy formatív, nem kapus igaz/hamis állítás, amelynek visszajelzése (:200–201) tanít; az „abszolút kulcsszó” kritika item-írási preferencia, nem bizonyított hiba.

**Összesítés**
- MEGERŐSÍTVE: 29, ebből bizonyíték-kapu 4 (BIZT-1, BIZT-2, IMPL-9, ERT-4)
- ELVETVE: 4 (PED-7, PED-9, ERT-5, ERT-10)
- EMBERI DÖNTÉS: 7 (PED-8, BIZT-3, BIZT-5, BIZT-7, BIZT-9, IMPL-3, ERT-3)
- PILOT-BLOCKER a verdiktek után:
  - feltétel nélkül: BIZT-1, BIZT-2/IMPL-9, BIZT-7;
  - feltételesen: BIZT-3 (a Memuna QA-ja dönt), IMPL-5, ERT-2, ERT-3, ERT-9.
  - Tananyag-módosítást BIZT-7 igényel, BIZT-1 és BIZT-3 pedig akkor, ha a Memuna szövegváltozást kér; ezekhez freeze-kivétel kell, amiről a projektgazda dönt. A többi bizonyítéki, runtime- vagy üzemeltetési lépés.

**Duplikátum-csoportok** (megtartandó → duplikátumok)
- K1: ERT-1 → PED-1, BIZT-4, IMPL-1 (ERT-1-ből az M0.4 SLIDE 5-rész elhagyandó)
- K2: IMPL-2 → ERT-6
- K3: IMPL-9 → BIZT-2; BIZT-10 külön finding
- K4: ERT-2 → IMPL-4; IMPL-3 külön megtartandó a döntési ága miatt; ERT-3 nem duplikátum
- K5: ERT-8 → PED-2, IMPL-6 (d)
- K6: ERT-7 → PED-4
- K7: ERT-9 → IMPL-6 (b)
- K8: PED-3 → ERT-5 M0.1-része (ERT-5 egyébként ELVETVE)
- Részleges átfedés: ERT-4 Memuna-része (1–2. item) és BIZT-1

Fájlok:
- C. melléklet (a riportban `ALL.md`)
- A. melléklet (a riportban `VERIFY-CONTEXT.md`)

---

# C. melléklet – nyers lencse-findingok (pedagógia, biztonság-jog, implementáció, értékelés)

# M0 /course-review — nyers findingok (4 lencse), 2026-10-10


---
# LENCSE: PED

## PED – pedagógiai lencse, M0 (6 fájl), read-only

Az M0-ban 10 pedagógiai findingot találtam: 3 P1 és 7 P2. P0 nincs, és a pilot-küszöb szerint egyik sem PILOT-BLOCKER, ezért freeze-kivételt egyikhez sem kell kérni. A kért N-M0-hipotéziseket a mai fájlokon ellenőriztem. Egy állítás nem igaz: a Z-modul visszakéri az M0-mondatokat (lásd a 3. vizsgálati pontot).

**Fájlok (a Hely mezőben rövid névvel, a sor a fájlon belüli sorszám):**
- HUB = `02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md`
- M0.1 = `02 Tervezet/Modulok/M0/Online leckék/M0.1 – Üdv a képzésben! – Éves útiterv & mi köze hozzám.md`
- M0.2 = `02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrih, nem terapeuta – szerepek és elvárások.md`
- M0.3 = `02 Tervezet/Modulok/M0/Online leckék/M0.3 – Hogyan működik a Moodle, H5P és a kapu.md`
- M0.4 = `02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md`
- M0.A = `02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md`
- Z.4 = `02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md`
- MAN = `02 Tervezet/LMS – activity manifest.md`

---

**PED-1**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** pedagógia
- **Hely:** M0.4:323–333 (SLIDE 3, helyzetenkénti visszajelzések)
- **Probléma:** Az 1. helyzet A opciójához (a bántás bagatellizálása) és a 3. helyzet A opciójához (kiskorúról készült kínos kép lájkolása) nincs téves-válasz visszajelzés. A helyzetek szabálytartalma csak a helyes válaszok közös blokkjában áll: a fotószabály, és hogy a Memuna bevonása nem múlik a hanih beleegyezésén. Ez a blokk mindhárom helyes opcióhoz ugyanaz, ezért az 1. helyzet helyes megválaszolása előre elárulja a 2. és a 3. helyzet indoklását.
- **Bizonyíték:** M0.4:331 „**Visszajelzés téves válasznál a 2. helyzetben (A):**” (más téves ág nincs); M0.4:329 „A 3. helyzetben pedig: hanihról csak indokolt célból készülhet fotó, és az is ellenőrzött tárhelyre kerül…”
- **Hatás:**
  - Aki „csak poén”-t vagy „lájkolja”-t választ, csak a H5P helytelen-jelölését kapja, indoklást nem.
  - A fotószabály az M0-ban csak a jól válaszolókhoz jut el.
  - A 2. és a 3. helyzet gyakorló értéke csökken, mert az indoklás előre látszik.
  - Részben enyhíti: az M0.2:276–277 („ne nézz félre”, csoportchat-szívatás), és a belépőkvíz 5. itemének B és D visszajelzése (HUB:240, :243). Ezek is csak ahhoz jutnak el, aki ott is tévesen választ.
- **Javaslat:**
  - Az 1. és a 3. helyzet A opciójához egy-egy mondatos téves visszajelzés, kizárólag meglévő mondatokból: M0.4:325–326, :329, :416–419; HUB:240.
  - A közös helyes-visszajelzést helyzetenként kell bontani: 1B → :325–326, 2B → :327–328, 3B → :329.
  - Javítási korlát:
    - a ✅, az opciók, a :300 fejlesztői feltétel és a 2. helyzet téves visszajelzése nem változik;
    - új szabály nem kerülhet be (például új jelzési küszöb a chat-szívatásra);
    - látható szöveg változik, ezért pin kell.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A küszöb egyik sora sem teljesül szó szerint:
  - valódi learnert nem veszélyeztet: a kockázat közvetett, a hanihokra irányul, és az M0.2 meg a belépőkvíz 5. iteme részben fedi;
  - a kulcs, a completion és az unlock ép, gate nem blokkol.
  - Ha a safety-lencse a fotószabály egyetlen M0-beli előfordulását gyermekvédelmi P0-nak minősíti, az a küszöb 1. sora alá eshet. Erről a projektgazda dönt.
- **Verdikt:** —

**PED-2**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** pedagógia
- **Hely:** M0.1:320–351 (SLIDE 5)
- **Probléma:** Ugyanazon a dián öt elem mást kér:
  - a cím azt, hogy mi érdekel;
  - a kérdés azt, hogy mire vagy a legkíváncsibb;
  - az instrukció a kíváncsiságot VAGY a félelmet, 1–2 modulra;
  - a fejlesztői jegyzet max. 2–3 választ;
  - a visszajelzés a kíváncsiságról és az izgalomról szól.

  Egy pipa nem választja szét a kíváncsiságot a félelemtől, és a félelmet jelölő tanulóhoz szóló visszajelzés nem róla szól.
- **Bizonyíték:** M0.1:332 „jelölj ki **1–2 modult**, amire most nagyon kíváncsi vagy, vagy amitől kicsit félsz”; M0.1:336 „Opciók (pipa-típus, max. 2–3 válasz javasolt):”
- **Hatás:** A tanuló számára értelmezhetetlen, mit jelölt meg, és a félelmet jelölőt a visszajelzés nem éri el. A completiont nem érinti: bármely jelölés teljesít.
- **Javaslat:**
  - Az instrukció, a darabszám és a visszajelzés egy konstruktumhoz és egy számhoz igazodjon, a címmel összhangban, a CC-04 szerint a pilot-visszajelzéssel együtt.
  - A félelem-dimenzió máshol már megvan: M0.A:353 („Mitől félek?” plakát), M0.4:484 (fórumkérdés).
  - Azt, hogy csak a kíváncsiság marad-e, vagy két külön kérdés lesz, a CC-04 a pilot-visszajelzéshez köti, most nem dől el.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Lezárt projektgazdai döntés (CC-04, 2026-10-10). P0-bizonyíték nincs: nincs biztonsági, adatvédelmi, hozzáférhetőségi vagy előrehaladást blokkoló hatás.
- **Verdikt:** —

**PED-3**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** pedagógia
- **Hely:** M0.1:17–19 (Mikrocél), összevetve a :205 és a :386–403 sorral
- **Probléma:** A tanulói mikrocél kétfélét ígér: a 9 állomás kódos felsorolását és modulonként egymondatos összefoglalását. A lecke egyiket sem gyakoroltatja: a SLIDE 2 tiszta input, a SLIDE 5 a látható listából választat. Nem is ellenőrzi: a Check a várakozás-mondat. A modulszintű mérés (belépőkvíz 6. item) csak 3 téma felismerő párosítása.
- **Bizonyíték:** M0.1:17–18 „**fel tudod majd sorolni a képzés 9 állomását a kódjukkal (M0–M7 + Z)**, **egy-egy mondatban megnevezni, miről szólnak az egyes modulok**”; M0.1:205 „*(Ezen a slide-on nincs interakció – tiszta Input.)*”
- **Hatás:** A mikrocél többet ígér, mint a hub 1. kompetenciája (HUB:31) és a mérés. A 6. item felidézési próba nélkül jön, így a gyenge eredménye az elmaradt gyakorlást mutatja.
- **Javaslat:** A mikrocél első két félmondata igazodjon a hub 1. kompetenciájához és a 6. item szintjéhez. Példa: „el tudod mondani, hány modulból áll az év, és melyikben lesz szó a visszajelzésről, a gyermekvédelemről és a peulatervezésről”. Korlát: a 6. item és a kulcsa nem változik.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Copy-finomítás, completiont és unlockot nem érint.
- **Verdikt:** —

**PED-4**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** pedagógia
- **Hely:** HUB:229–231 (belépőkvíz 4. item), összevetve az M0.3:253–257 sorral (SLIDE 5)
- **Probléma:** A 4. item kulcsa és a D-visszajelzés a „kötelező F-peulát” a helyes következmény részeként kezeli. Ezt a fogalmat az M0.1–M0.4 egyike sem tanítja, és a visszajelzés által megjelölt M0.3 5. dián sincs benne.
- **Bizonyíték:** HUB:231 „a kötelező F-peulán (a javítási úton) kell dolgozni; lásd: M0.3, 5. dia (puha és éles kapu)”; M0.3:257 „…kapsz visszajelzést, javítási lehetőséget.” (F-peula nélkül)
- **Hatás:**
  - A tanuló olyan diára kap utalást, ahol a fogalom nincs.
  - A §6 elemzés (HUB:281) a 4. item gyengeségét „M0.3 újramondással” pótolná, de az M0.3 nem tartalmazza a fogalmat.
  - A kulcs a „javítási úton” szinonimával felismerhető, tehát a mérés nem törött.
- **Javaslat:** A két megoldás közül az egyik:
  - az M0.3 SLIDE 5 éles-kapu pontjába egy félmondat a Glosszárium F-peula-szócikkéből (Glosszárium:193);
  - vagy a D-visszajelzés hivatkozása szűküljön a Glosszáriumra.

  Az item szövege és a kulcs projektgazdai (HUB:180), nem változik. A visszajelzés szerkesztői kiegészítés, amelyet az értékelési felelős ellenőriz.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A kulcs ép, a kvíz eredménytől független completion-jelző (HUB:170), gate nem blokkol.
- **Verdikt:** —

**PED-5**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** pedagógia
- **Hely:** M0.A:152–157 (45’ percbontás); :340–363; :420–451; :643–648
- **Probléma:** A lépésenként megadott percek nem férnek a blokkidőbe:

  | Blokk | Lépések összege | Sáv 60’-nél | Sáv 45’-nél |
  |---|---|---|---|
  | Blokk 2 (plakát) | 16–21’ | 15’ | 10’ |
  | Blokk 3 (közös keret) | 13–18’ | 15’ | 10’ |

  - A teljes 60’-es peula így 58–72’.
  - A 45’-es változatban a Blokk 2 a 4. és az 5. lépés teljes elhagyásával is 11–14’.
  - A 45’-es változat nem ad lépésszintű vágást.
  - A vágási prioritás nem védi a „madrih, nem terapeuta” lépést (Blokk 3, 3. lépés), pedig az M0.2 ezt élőben megígéri a tanulónak.
- **Bizonyíték:** M0.A:155 „**17–27’** – 2. fő tevékenység – „Közös keret” (gyorsabb közös ötletelés, rövidebb plenáris)”; M0.A:646–647 „– rövidebb nagykör, – de **tartsd meg a zárókört + „kihez fordulhatok” részt**.”
- **Hatás:** A képző improvizálva vág, és a nagykörös Blokk 3 3. lépése (M0.A:441–446) a „rövidebb nagykör” alá eshet. Pedig az M0.2:504 ígéri, hogy „a kickoff-peulán élőben is kimondjuk”, és a hub szerint az M0.A a 2. kompetencia támogató eleme (HUB:37).
- **Javaslat:**
  - Lépésszintű percbontás a 45’-es változathoz: melyik lépés marad, melyik rövidül vagy marad el.
  - A :643–648 priorizálásba kerüljön be a Blokk 3 3. lépésének megtartása (az M0.2:504 átvezetése).
  - Korlát: a 45’/60’ időtartam, a zárókör és a „Kihez fordulhatok?” prioritása, a biztonsági keret és a 2.4 protokoll nem változik.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A tanulói útvonalat nem blokkolja: az M0.A nem completion-feltétel, az LMS-M0-03 dátummal nyit.
- **Verdikt:** —

**PED-6**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** pedagógia
- **Hely:** M0.1:414 (SLIDE 7, kapcsolat a kickoff-peulához)
- **Probléma:** A tanulói szöveg kijelentő módban, kilépési lehetőség nélkül azt ígéri, hogy a tanuló a magának leírt várakozását a plakáton és a zárókörben hangosan is megfogalmazza. Ez ellentmond a SLIDE 6 „A reflexió nálad marad” keretének (:373), és annak is, amit az M0.A ténylegesen csinál:
  - csoportos plakát, „amennyit szeretnétek” (:342);
  - a zárókörben egy indulószó, passz-lehetőséggel (:497, :501).
- **Bizonyíték:** M0.1:414 „és a zárókörben hangosan is megfogalmazod, amit itt magadnak leírtál”; M0.A:501 „Ha valaki passzol, az is oké.”
- **Hatás:** A 15+ tanuló nyilvánosnak várhatja a privát reflexiót, és ehhez igazítva öncenzúrázhat. A két dokumentum mást mond ugyanarról az alkalomról.
- **Javaslat:** Az M0.1:414 igazodjon az M0.A tényleges menetéhez és a passz-lehetőséghez („ha szeretnéd…”; egy szó vagy rövid mondat). Korlát: az M0.A menete és a SLIDE 6 privát kerete nem változik.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Learnert nem veszélyeztet, mert az élő alkalom ténylegesen önkéntes.
- **Verdikt:** —

**PED-7**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** pedagógia
- **Hely:** M0.1:355–403 (SLIDE 6–7); M0.2:449–454 és :483–492 (SLIDE 6–7)
- **Probléma:**
  - Az M0.1 SLIDE 6 (2–4 mondat: mit remélsz) és SLIDE 7 (1 mondat: mit vársz) ugyanarra kérdez.
  - A SLIDE 7 három kész példamondata a SLIDE 6 három szempontját mondja vissza, így a sűrítő lépés megkerülhető.
  - Az M0.2 SLIDE 7 példái a lecke kulcsüzeneteit ismétlik.
  - Az M0.2 SLIDE 6 1. pontjának példái alapkötelességek.
  - Mindkét záró mondatot a Z.4 „SAJÁT” mondatként kéri vissza.
- **Bizonyíték:** M0.1:398–399 „Írhatsz ilyesmit: – „Azt várom, hogy bátrabban álljak ki a kvucám elé.””; Z.4:190 „vedd elő a SAJÁT két mondatodat, amit M0-ban magadnak elmentettél”
- **Hatás:** Ha a mondat átvett példa, gyengül az év eleji és az év végi összevetés (Z.4:190–198). A kért mondatszám is szétcsúszik: M0.1:19 és :44 „1–2 mondat”, :369 „2–4 mondatot”, :394 „1 mondatot”.
- **Javaslat:** Minimális változtatás:
  - az M0.1 SLIDE 7 a SLIDE 6 saját szövegének egy mondatba sűrítését kérje; a kész mondatok helyett elég a meglévő mondatkezdet (M0.1:407);
  - az M0.2 SLIDE 7-ben ugyanígy (az M0.2:485 mondatkezdet elég);
  - az M0.2 SLIDE 6 1. pontjának zárójele elhagyható, a 2. pont gyermekvédelmi példája (:454) marad;
  - a mondatszámok egyeztetve.

  Korlát: a tanuló-lokális státusz (D-4), a Z-hivatkozás és a SLIDE 6 biztonsági és adatvédelmi blokkjai nem változnak.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. Apró copy-finomítás.
- **Verdikt:** —

**PED-8**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** pedagógia
- **Hely:** HUB:148; HUB:279–281 (§6, 4. pont)
- **Probléma:** A gyermekvédelmi reflexet mérő 1–2. item első próbálkozásos tévedése (pl. „Vár másnapig”, „Saját maga utánajár”) csak automatikus visszajelzést és újrapróbát vált ki. A stáb-reakció csak kohorsz- és témakörszintű; egyéni utánkövetés csak a hiányzó kitöltésre van előírva.
- **Bizonyíték:** HUB:148 „A §6 stáb-jelzés (átlag és témakörszintű arány) az **első próbálkozás** item-statisztikájából számol”; HUB:174 „Ha valakinek **hiányzik a bemutatkozó poszt** vagy a kvíz → személyes, támogató emlékeztető”
- **Hatás:** Az a madrih, akinek az első próbán téves a jelzési reflexe, az M3 éles kapujáig egyéni megerősítés nélkül marad. Ha közben kvucával dolgozik, a tévképzet a terepen jelenhet meg.
- **Javaslat:** EMBERI DÖNTÉS:
  - Kapjon-e egyéni, támogató, nem szankcionáló utánkövetést (például egy rövid mentori beszélgetést) az, aki az 1–2. itemet az első próbálkozáson tévesen válaszolja?
  - Ki láthatja ehhez az egyéni válaszokat (a HUM-PRIV-01 keretén belül)?
  - Gazda: programvezető és Memuna; adatkör-vétó: DPO.
  - A ponthatár nélküli, nem blokkoló kvíz lezárt döntése nem nyílik újra.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT. Nem blokkol, és learnert nem veszélyeztet. Ha a döntés megszületik, tananyag-módosítás nélkül, operatívan a pilot alatt is alkalmazható.
- **Verdikt:** —

**PED-9**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** pedagógia
- **Hely:** M0.4:144–154 (SLIDE 1) és :414–428 (SLIDE 4), összevetve az M0.2:417–431 sorral
- **Probléma:** Az M0.4 a dugma isitet és az online szabályokat újként vezeti be. A SLIDE 1 nem idézi fel az M0.2-es definíciót (M0.2:420). A SLIDE 4 1. szabálya szinte szó szerint az M0.2 SLIDE 5 online példáit ismétli, felidéző kérdés nélkül.
- **Bizonyíték:** M0.2:430 „nem csinálok olyat privátban, amit szégyellenék nagykörben is felolvasva,” ↔ M0.4:416 „„Amit nem olvasnék fel nagykörben, azt nem írom le privátban.””
- **Hatás:** Az M0.2 → M0.A → M0.4 közti napok térközös felidézésre adnának alkalmat; ehelyett ismételt input jön. Aki az M0.2-t régen végezte, annak definíció nélkül indul a lecke.
- **Javaslat:** Egymondatos felidézés az M0.4 SLIDE 1-be az M0.2:420 definíciójával, szó szerint. A SLIDE 4 jelezze, hogy az 1. szabály az M0.2-ből ismerős. Korlát: a három szabály és a safety-tartalom nem változik, új tartalom nem kerül be.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT.
- **Verdikt:** —

**PED-10**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** pedagógia
- **Hely:** M0.4:554 (SLIDE 7, kapcsolat a kickoff-peulához)
- **Probléma:** Az M0.3 dátummal nyílik, nem jelenléttel, ezért az M0.A-ról hiányzó tanuló is eljut az M0.4-ig, ahol a szöveg feltételezi, hogy ott volt. Az M0.A céljainak (közös keret, névvel kitöltött „Kihez fordulhatok?” térkép) nincs leírt pótlási útja; az M0.A:610 kimondja, hogy F-peula nincs.
- **Bizonyíték:** M0.4:554 „a kvucáddal **élőben a kickoff-peulán találkoztál először** … **A kickoffon 1 szóval megfogalmaztad**”; MAN:41 „**M0.A után nyílik dátummal**, nem jelenléti találgatással”
- **Hatás:** A hiányzó a nevesített támaszrendszert csak a kurzusblokkból tudhatja meg, és a szöveg nem irányítja oda. A „Bemutatkozó fal” felvezetése rá nem igaz.
- **Javaslat:** Az M0.4:554 legyen feltételes, és kapjon egy félmondatot a hiányzónak a „Segítség és kapcsolatok” blokkról (ez meglévő út, M0.4:52). Hogy jár-e a hiányzónak rövid egyéni pótlás, az emberi döntés (programvezető), nem része a javításnak.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A completiont és az unlockot nem érinti.
- **Verdikt:** —

---

## Vizsgálati pontok
1. **N-M0-14** → PED-1. P1-re emeltem, mert pont a két gyermekvédelmi tévképzet marad magyarázat nélkül. A küszöb sorai szerint POST-PILOT, az indoklás a findingban.
2. **N-M0-01** → PED-2. Valós: öt elem mást kér ugyanazon a dián, és a visszajelzés elhagyja a félelmet. A CC-04 szerint POST-PILOT. P0-bizonyíték nincs: bármely jelölés teljesít, és nincs biztonsági, adatvédelmi vagy hozzáférhetőségi hatás.
3. **Példák és saját válaszok:**
   - N-M0-02 és N-M0-06 → PED-7.
   - N-M0-05 csak részben: az 1. pont példái igen, a 2. pont gyermekvédelmi példája maradjon (PED-7).
   - Az „1–2 modul” ↔ „max. 2–3 válasz” széttartás → PED-2.
   - N-M0-13 → PED-9.
   - A Z-kapcsolat hiánya nem finding: a Z.4:190–194 és a `…/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md`:206 mindkét M0-mondatot visszakéri, és hiány esetén emlékezetből pótoltatja (Z.4:194).

**Lencsén kívüli tétel.** A szabály szerint objektív finding, de nem pedagógiai, ezért nem számoztam: a CC-04 döntés nincs átvezetve az `Emberi jóváhagyás szükséges.md`-be (a „CC-04”-re 0 találat). Forrása a `01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntések – Anna-megfeleltetés indítása, M0.1 POST-PILOT, Moodle-összevetés.md` :41. Az átvezetés governance-teendő; a mátrix :334 is jelzi.

## Mi maradt ki
- Nem olvastam:
  - a Program terv §5-öt;
  - a Glosszárium F-peula-szócikkének tartalmát (csak a :193 fejlécet);
  - az `Adatvédelem – tanulói adatok és AI.md` §3-at és a HUM-PRIV-01-et, ami a PED-8 hozzáférési részéhez kellene;
  - az `LMS – H5P runtime acceptance.md`-t (egyetlen grep-találatot néztem: :83, a helyes válasz nélküli véleménykérdések kezelése; erre építve nem nyitottam findingot);
  - az M3.B-t.
- Git-history nem állt rendelkezésre.
- D9: az M0-ban nem találtam neuromítoszt vagy túláltalánosított kutatási állítást.

---
# LENCSE: BIZT

## BIZT-findingok: M0 (biztonság-jog lencse)

Read-only futás volt: egyetlen fájlt sem módosítottam. 11 finding van, a 12-es plafon alatt, ezért nincs levágás.

---

**BIZT-1**
- **Súlyosság:** P0 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M0.2 SLIDE 3–4 (:255–277, :339–352); M0.4 SLIDE 2–4 (:222–244, :302–333, :414–428); M0 hub belépőkvíz 1–2. item (:185–207); M0.A mini-protokoll (:129–140). Kánon: `Gyermekvédelem – release gate.md` :17, `RELEASE-READINESS.md` :40
- **Probléma:** Az M0 gyermekvédelmi tartalmai a GK §2 témaalapú hatókörébe esnek (bántalmazás, önsértés, 112). Ezekről a repóban nincs a Memunától írásos „átnéztem” bejegyzés, miközben a pilot 2026-10-10-én valódi madrihokkal elindult.
- **Bizonyíték:** GK :17 „…amely bántalmazásról, önsértésről, … vagy külső jelzésről tanít, **nem nyitható meg valódi madrihoknak a Memuna írásos átnézése nélkül**”. RR :40 „A G1 nyitott marad, amíg ez az átnézés meg nem történt.” M0.4 :422 „(bántalmazás, önsértés, „nem akarok élni”)”. A repóban az „átnéztem” csak szabályként és nyitott tételként szerepel (Build-blocker leltár :87, SG-01 `SIGNOFF_REQUIRED`).
- **Hatás:** Ha a bejegyzés tényleg hiányzik, a pilot a kánon szerint átnézetlen gyermekvédelmi tartalmat nyitott meg akár kiskorú tanulóknak.
- **Javaslat:** A repóban nem javítható. A release-jegyzőkönyvben (Program terv §9.3) a Memuna „átnéztem” bejegyzése kell a felsorolt M0-elemekre, vagy hivatkozás rá, ha a repón kívül már megvan. A tananyaghoz ne nyúljunk. Megvalósítási döntés: a projektgazda jóváhagyta; a formális szerepköri bizonyíték függő.
- **Típus:** bizonyíték-kapu · **Osztály:** PROJEKT-DÖNTÉS (a QA-kapu, RR :40) + hiányzó szerepköri bizonyíték
- **Pilot-besorolás:** PILOT-BLOCKER. A küszöb „safety/privacy probléma, amely valódi learnert veszélyeztet” sora és a GK §2 alapján. Maga a bizonyíték nem igényel szövegmódosítást. Ha a Memuna átnézése szövegváltozást kér: freeze-kivétel szükséges (projektgazdai döntés).
- **Verdikt:** —

**BIZT-2**
- **Súlyosság:** P0 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M0.1 :51; M0.2 :465; M0 hub :204 (2. item, B visszajelzés); M0.A :139. Kánon: `Emberi jóváhagyás szükséges.md` :550 (PILOT-3), GK :147, RR :34
- **Probléma:** Az M0 tanulói szövegei a Memuna elérhetőségét a „Segítség és kapcsolatok” blokkra bízzák. A repóban nincs bizonyíték arra, hogy a blokk a renderelt Moodle-ben ki van töltve: négy szerep, a Memuna és a helyettese a többi kontakttól külön.
- **Bizonyíték:** HUM :550 „…a learner-facing pilot release-t viszont blokkolja, amíg a tényleges csatornák nincsenek kitöltve.” GK :147 `[ ]` „…ténylegesen látható a Moodle-ben; <!-- gate: post-build -->”
- **Hatás:** Ha a blokk üres vagy jelölő maradt benne, egy veszélyben lévő, akár kiskorú tanuló a leckéből nem jut el a Memunához.
- **Javaslat:** A repóban nem javítható. A G8/G4b staging-visszaaudit és a GK §6 :147 renderelt bizonyítéka kell. Kontaktadatot nem írunk be.
- **Típus:** bizonyíték-kapu · **Osztály:** PROJEKT-DÖNTÉS (PILOT-3) + hiányzó runtime-bizonyíték
- **Pilot-besorolás:** PILOT-BLOCKER, a küszöb „learner-facing placeholder / hibás kontakt” sora szerint. Ez Moodle-konfiguráció, tartalmi freeze-kivétel nem kell hozzá.
- **Verdikt:** —

**BIZT-3**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M0.4 SLIDE 3, 2. helyzet (:309–314); SLIDE 2, 2. helyzet (:223). Kánon: GK :94, :97; HUM :567 (SAFE-7)
- **Probléma:** Ugyanaz a mintázat, amelyet az M3.3-ban a SAFE-7 nyitott Memuna-QA-ként tart: késő esti, egy az egyben (1:1) bejövő üzenet egy hanihtól. A ✅ B maga egy kiskorúnak küldött privát válasz, és a csatorna (szervezeti vagy személyes) nincs megadva.
- **Bizonyíték:** M0.4 :311 „Késő este ír egy hanih: „Nagyon sz\*rul vagyok, senki nem ért meg.”” GK :97 „kiskorúnak küldött személyes privát üzenet soha nem „helyes” válasz. … de gyermekvédelmi helyzet megoldásaként nem.” HUM :567 (SAFE-7): „learner release előtt kötelező lezárni”.
- **Hatás:** Ha a Memuna a SAFE-7-ben nem találja megfelelőnek ezt a mintát, akkor az M0.4 már most valódi, akár kiskorú madrihokat tanít egy, a HUM-SAFE-02-vel ütköző válaszmintára.
- **Javaslat:** EMBERI DÖNTÉS: a Memuna (HUM-SAFE-02 vétó/QA) döntse el, hogy a SAFE-7 kérdése kiterjed-e az M0.4 SLIDE 3 2. helyzetére és a SLIDE 2 2. helyzetére, és hogy a ✅ B megfelel-e a GK §4.2-nek. Bizonyíték hozzá: a két idézett szöveg és a GK :94/:97. A döntésig a ✅-hoz és a szöveghez a `/course-fix` ne nyúljon (answer key-invariáns).
- **Típus:** emberi-döntés · **Osztály:** EMBERI JÓVÁHAGYÁS KELL (egy lezárt döntés új alkalmazási esete)
- **Pilot-besorolás:** PILOT-BLOCKER a „safety probléma, amely valódi learnert veszélyeztet” sor szerint. A besorolás a SAFE-7 „learner release előtt” státuszával vont analógián alapul; hogy az analógia áll-e, azt a Memuna mondja ki. Ha a QA szövegváltozást kér: freeze-kivétel szükséges (projektgazdai döntés).
- **Verdikt:** —

**BIZT-4** (N-M0-14)
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** M0.4 SLIDE 3: :300, :302–307 (1. helyzet), :316–321 (3. helyzet), :323–333
- **Probléma:** Az 1. és a 3. helyzet téves (A) opciójához nincs válaszonkénti visszajelzés, pedig a :300 válaszonkénti `chosenFeedback`-et ír elő. Így pont a bántás bagatellizálása és a kiskorúról készült kínos kép lájkolása marad magyarázat nélkül.
- **Bizonyíték:** M0.4 :306 „A) „Nyugi, gyerekek, ez csak poén, ne sírjon senki, túl komolyan veszitek.”” A :331 az egyetlen téves visszajelzés („…téves válasznál a 2. helyzetben (A)”). H5P MultiChoice `semantics.json` (h5p/h5p-multi-choice, elsődleges forrás): a chosenFeedback leírása „Message will appear below the answer on "check" if this answer is selected.”, az enableSolutionsButton alapértéke „Enable "Show Solution" button" (default: true).
- **Hatás:** A H5P a téves választást hibásnak jelöli, de magyarázatot nem ad. A helyes megoldást csak külön „Show solution” kattintásra mutatja, és hogy ez a gomb be van-e kapcsolva, azt a build-spec nem rögzíti (grep: nincs találat).
- **A pilot-minősítés bizonyítéka:** A korrekció máshol részben megvan, de nem jut el mindenkihez.
  - (a) A kombinált helyes-visszajelzés (:325–329) mindkét elvet tartalmazza, de csak annak jelenik meg, aki legalább egy helyzetben jól választ.
  - (b) Az M0.2 SLIDE 3 4. kérdése kötelező completion-elem, és a chat-szívatásra a beavatkozást tanítja (:265, :277), de az M0.4 előtt, nem utána.
  - (c) A belépőkvíz 5. itemére mindenkinek válaszolnia kell, de a „csak poén” nem disztraktor. A B (kínos poszt) és a D (hallgatás) visszajelzése (hub :240, :243) csak ahhoz jut el, aki azt választja.
  - A lecke nem tanít téves szabályt, a helyes viselkedés ✅-val jelölt.
- **Javaslat:** `/course-fix`: az 1. és a 3. helyzet A opciója kapjon egymondatos téves visszajelzést, kizárólag a meglévő kánoni mondatokból (M0.4 :325, :329; hub :240, :243), új szabály nélkül. A ✅ és a disztraktorok nem változnak. Hogy az 1. helyzetnél szerepeljen-e Memuna-jelzés, az a BIZT-5 döntésétől függ.
- **Típus:** objektív · **Osztály:** TÉNY (a hiány) / PROJEKT-DÖNTÉS (a :300 előírás)
- **Pilot-besorolás:** POST-PILOT. A „safety/privacy probléma, amely valódi learnert veszélyeztet” sor a repó alapján nem bizonyítható: nincs téves szabály, és a helyes viselkedés jelölt. Marad egy kockázat: aki mindhárom helyzetben téved, és nem kéri a megoldást, korrekció nélkül halad tovább. Hogy ez veszélyeztető-e, azt a Memuna mérlegelje. Ha igen, freeze-kivétel szükséges (projektgazdai döntés).
- **Verdikt:** —

**BIZT-5**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M0.2 :264–265; M0.4 :304–307; M0 hub :241 (5. item, C). Kánon: GK :80
- **Probléma:** Ugyanarra a helyzetre (csoportchat-szívatás) az M0 két különböző „helyes” mintát tanít. Az M0.2-ben a Memuna-jelzés kötelező; az M0.4-ben nincs jelzés, a belépőkvízben pedig csak „szükség esetén”.
- **Bizonyíték:** M0.2 :265 „A) A csoportchatben leállítom a szívatást, figyelek az érintettre, és **jelzek** a Memunának ✅”. M0.4 :307 „B) „Srácok, ez már nem vicces, álljunk meg. …” ✅”. Hub :241 „…szükség esetén hivatalos segítségi utat használni. ✅”
- **Hatás:** A madrih nem tudja, kell-e minden chat-szívatást jeleznie. A BIZT-4 1. helyzetre szóló visszajelzése sem írható meg enélkül.
- **Javaslat:** EMBERI DÖNTÉS: a Memuna döntse el, hogy a kvuca-csoportchatben zajló szívatás minden esetben Memuna-jelzés-e (M0.2), vagy csak egy meghatározott súlyosság felett (M0.4, belépőkvíz). Bizonyíték: a három idézett hely és a GK :80 („sértéssel, bántalmazással, zaklatással kapcsolatos ügyekben”). Utána az eltérő hely átvezetése objektív javítás. A belépőkvíz itemszövegét a projektgazda adta meg (hub :180), azt csak ő módosíthatja.
- **Típus:** emberi-döntés · **Osztály:** EMBERI JÓVÁHAGYÁS KELL
- **Pilot-besorolás:** POST-PILOT. Mindkét minta beavatkozást tanít, önmagában egyik sem veszélyeztet (a küszöb „safety…” sora nem teljesül).
- **Verdikt:** —

**BIZT-6**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M0.4 SLIDE 1 (:146–151, :158–171). Kánon: GK :94; M0.4 :419, :430
- **Probléma:** A SLIDE 1 a privát üzenetet, az insta-DM-et és az online játékot / voice chatet a madrih-szerep természetes online tereként sorolja fel, és a visszajelzés („Oké.”) korrekció nélkül nyugtázza. A HUM-SAFE-02 szabálya csak a SLIDE 4-en jön, és ott nincs completion-elem (:430: „tiszta Input”), vagyis a dia átugorható.
- **Bizonyíték:** M0.4 :163–164 „* Insta (DM / sztorira reagálás)” / „* Online játék / voice chat”, :170 „„Oké. Akár már sok, akár kevés online helyzeted volt,”. GK :94 „Kiskorúval **személyes közösségimédia-fiókról** nem kommunikálunk; **szervezeti csatorna** használható.”
- **Hatás:** A lecke a személyes csatornát normalizálja, mielőtt a szabályt kimondaná.
- **Javaslat:** `/course-fix`: a SLIDE 1 visszajelzésébe kerüljön át szó szerint a :419 kánoni mondata (HUM-SAFE-02). A kérdés és az opciók nem változnak, új szabályt ne írjunk.
- **Típus:** objektív · **Osztály:** PROJEKT-DÖNTÉS (HUM-SAFE-02)
- **Pilot-besorolás:** POST-PILOT. Ugyanabban a leckében szerepel a szabály, téves szabályt nem tanít.
- **Verdikt:** —

**BIZT-7**
- **Súlyosság:** P0 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M0 hub :164; M0.4 §4 (:558–570). Kánon: `Program terv.md` :228; `Adatvédelem – tanulói adatok és AI.md` §3 (:60–73), :79, §11 (:247–256)
- **Probléma:** A bemutatkozó fórumposzt és -válasz megőrzési ideje nem szerepel sem a §3 mátrixban, sem a §11 „Meddig őrizzük meg?” listájában. Ezért a kötelező just-in-time tájékoztató „meddig” része nem írható meg, a Program terv szerint pedig ilyen activity nem nyitható meg valódi madrihnak. Az Adatvédelem :79 szerinti „külön review” eredménye sincs a repóban.
- **Bizonyíték:** Program terv :228 „Ha egy adatot gyűjtő aktivitásra ez nincs rögzítve, az nem nyitható meg valódi madrihnak.” Adatvédelem :79 „M0 „Bemutatkozó fal”: kurzuson belül más résztvevőknek látható;” (a „Külön review szükséges legalább” listában). A §3/§11 megőrzési listákban nincs fórumsor.
- **Hatás:** Akár kiskorú tanulók posztolnak (bemutatkozás, félelmek) úgy, hogy nem tudják, meddig őrizzük meg. A GDPR 13. cikk (2) a) pontját az EUR-Lexről csak töredékesen tudtam lekérni („a személyes adatok tárolásának időtartamára vonatkozó információ, vagy ahol ez”), ezért a jogi minősítést óvatosan fogalmazom: ez a DPO dolga.
- **Javaslat:** EMBERI DÖNTÉS: a DPO/jogi felelős (a HUM-PRIV-01 utólagos ellenőrzője) döntsön három kérdésben. (1) Mi a fórumposzt és -válasz megőrzési ideje, és melyik §3-sorba kerül? (2) Mi az M0 „Bemutatkozó fal” külön review-jának eredménye? (3) Elfogadható-e a pilotban a megőrzési tájékoztató hiánya? Megőrzési értéket a repó nem talál ki.
- **Típus:** emberi-döntés · **Osztály:** PROJEKT-DÖNTÉS (Program terv :228, HUM-PRIV-01) + EMBERI JÓVÁHAGYÁS KELL (a megőrzési érték)
- **Pilot-besorolás:** PILOT-BLOCKER a küszöb „safety/privacy probléma” sora és a Program terv :228 kifejezett nyitási tilalma alapján. A tájékoztató szövegének beépítéséhez freeze-kivétel szükséges (projektgazdai döntés). A bizalom azért közepes, mert a Moodle-buildben esetleg már van tájékoztató; ezt nem tudtam ellenőrizni.
- **Verdikt:** —

**BIZT-8**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M0.4 :501, :565. Kánon: Program terv :230; Adatvédelem :245; `LMS – activity manifest.md` :21
- **Probléma:** A tanulói szöveg szerint a poszt „a csoportnak látszik”. A kánon ezzel szemben a tényleges Moodle-beállítás szerinti közlést írja elő (FORUM-C: „kurzusrésztvevők látják”), és kifejezetten tiltja az „automatikusan az egész kvuca számára látható tér” leírást. A „csoport” a Moodle-ben a mentor-csoportot is jelentheti.
- **Bizonyíték:** M0.4 :565 „ez a poszt a csoportnak látszik (nem privát)”. Adatvédelem :245 „A kurzusfórumra írt hozzászólásodat a kurzus résztvevői látják.”
- **Hatás:** A tanuló szűkebb közönséget feltételezhet (például csak a saját kvucáját), mint aki a posztot ténylegesen látja (más csoportok, stáb).
- **Javaslat:** `/course-fix`: a két helyen a §11 kánoni mondata kerüljön át szó szerint, a runtime (RT) visszaolvasásához kötve. Az „annyit ossz meg…” védőmondat maradjon.
- **Típus:** objektív · **Osztály:** PROJEKT-DÖNTÉS (HUM-PRIV-01)
- **Pilot-besorolás:** POST-PILOT. A láthatóság szándékolt, és a poszt nem érzékeny adat-osztályú. Ha a runtime-visszaolvasás szélesebb kört mutat, mint amire a tanuló számít, a „hibás hozzáférés vagy érzékeny adat láthatósága” sor alá kerülhet.
- **Verdikt:** —

**BIZT-9**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M0.A :47, :132–134, :632–633. Kánon: GK :64
- **Probléma:** A mini-protokoll egyszerre írja elő, hogy a felkavart kiskorú mellett „egy felnőtt legyen” a biztonságos helyen, és hogy a képző folytassa a kört. A peula ugyanakkor nem rögzíti, hogy a képzőn kívül egy második felnőttnek is jelen kell lennie. A szöveg csak utal rá: „mi, képzők” (:595), „képző(k)” (hub :124).
- **Bizonyíték:** M0.A :132 „Felkavart kiskorú résztvevőt ne küldj ki egyedül: a kijelölt biztonságos helyen egy felnőtt legyen vele.” M0.A :133 „Tereld vissza a kört egy kész mondattal, és menj tovább…”
- **Hatás:** Egyetlen felnőtt mellett a GK :64 szabálya és a csoport felügyelete egyszerre nem teljesíthető.
- **Javaslat:** EMBERI DÖNTÉS: a programvezető és a Memuna (HUM-SAFE-03 vétó/QA) döntse el, kötelező-e az M0.A-n (és a képzési peulákon) legalább két felnőtt jelenléte, vagy egy megnevezett, azonnal elérhető második felnőtt. A szabályt a repó nem találja ki.
- **Típus:** emberi-döntés · **Osztály:** EMBERI JÓVÁHAGYÁS KELL
- **Pilot-besorolás:** POST-PILOT a tartalmi javításra. A :633 ellenőrzőlista-kérdés részben fedi a kockázatot. Ha a pilot M0.A-ja egyetlen felnőttel fut, a személyzeti döntés operatív, és tartalmi freeze-kivétel nélkül is meghozható.
- **Verdikt:** —

**BIZT-10**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** biztonság-jog
- **Hely:** M0.2 :467. Kánon: GK :147; HUM :550
- **Probléma:** A fejlesztői élesítési feltétel csak „a Memuna és a mentor” adatait kéri. Kimarad belőle a helyettes, amelyet a GK §6 külön kontaktként ír elő, és a PILOT-3 négy szerepe is.
- **Bizonyíték:** M0.2 :467 „amíg a „Segítség és kapcsolatok” blokkban a Memuna és a mentor neve és elérhetősége nincs láthatóan kint”. GK :147 „a Memuna és összeférhetetlenség esetére a név szerint kijelölt helyettese”.
- **Hatás:** Aki az M0.2-ből épít, a helyettes nélkül is teljesítettnek láthatja a feltételt.
- **Javaslat:** `/course-fix`: a feltétel a GK :147 / PILOT-3 szerepkörét vegye át szó szerint. Nevet és elérhetőséget ne írjunk be.
- **Típus:** objektív · **Osztály:** PROJEKT-DÖNTÉS (HUM-SAFE-01, PILOT-3)
- **Pilot-besorolás:** POST-PILOT. Nem tanulói szöveg, a kapu (GK :147, RR :34) önállóan érvényes.
- **Verdikt:** —

**BIZT-11**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** biztonság-jog
- **Hely:** M0.1 :51. Kánon: GK :80, :102
- **Probléma:** A kurzus első leckéjében a „Memuna” először a szó szerint kötelező HUM-SAFE-03 blokkban fordul elő, és ott nincs megmagyarázva. A GK :80 szerint első előfordulásnál a „kijelölt Memuna (a Somer gyermekvédelmi felelőse)” formula kell.
- **Bizonyíték:** M0.1 :51 „…a Memuna más biztonságos felnőttet vagy hivatalos segítséget von be.” GK :80 „Tanulói fájlban az első előforduláskor: „a kijelölt **Memuna** (a Somer gyermekvédelmi felelőse)”, utána „a Memuna”.”
- **Hatás:** Egy új, akár kiskorú tanuló a biztonsági blokkban nem tudja, ki az, aki segítséget von be.
- **Javaslat:** `/course-fix`: a GK :80 formulája kerüljön át a blokk elé, a 🛟 dobozba vagy a bevezetőbe. A HUM-SAFE-03 blokk szövege szó szerint változatlan marad (GK :102).
- **Típus:** objektív · **Osztály:** PROJEKT-DÖNTÉS (HUM-SAFE-01/03)
- **Pilot-besorolás:** POST-PILOT. A blokk a „Somer gyermekvédelmi kontaktja” kifejezéssel részben azonosítja a szerepet; ez apró copy-finomítás.
- **Verdikt:** —

---

### Vizsgálati pontok
1. **N-M0-14:** BIZT-4, POST-PILOT, a fenti bizonyíték-sorral. A maradék kockázat (aki mindhárom helyzetben téved és nem kér megoldást) pilot-minősítése a Memunáé. Kapcsolódik a BIZT-5-höz: az 1. helyzet visszajelzésének tartalma a jelzési szabálytól függ.
2. **Az M0.4 biztonsági visszajelzéseinek teljessége:** BIZT-4 (1. és 3. helyzet), BIZT-3 (a 2. helyzet ✅ csatornája, SAFE-7-analógia) és BIZT-6 (SLIDE 1). Nem finding a hatósági szerep kérdése: egyik visszajelzés sem ad a madrihnak önálló hatósági vagy jogi döntést. Az M0.4 :328 és :333 a Memuna bevonását írja elő, a SLIDE 4 2. szabálya (:421–424) a GK §4.1 4–5. lépésével egyezik, az M0.4 :42 pedig a kánoni első-előfordulási formulát használja.

### Ami kimaradt vagy bizonytalan
- Git-history nem állt rendelkezésre, és a Moodle runtime-ot (renderelt kontaktblokk, H5P „Show solution”-beállítás, tájékoztató doboz) nem ellenőriztem.
- A BIZT-1, -2 és -7 abból indul ki, hogy a bizonyíték a repón kívül sincs meg. A release-jegyzőkönyv lehet archívumban, ezért ezeknél közepes a bizalom.
- Az M0.3-at csak grep szinten néztem át; biztonsági tartalmat nem találtam benne.
- A GDPR 13. cikkét az EUR-Lex csak töredékesen adta vissza (lásd BIZT-7).
- A belépőkvíz 1–2. itemének szövege lezárt projektgazdai döntés (hub :180); ezeket nem nyitottam újra.

### Érintett fájlok
- 02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md
- 02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrih, nem terapeuta – szerepek és elvárások.md
- 02 Tervezet/Modulok/M0/Online leckék/M0.1 – Üdv a képzésben! – Éves útiterv & mi köze hozzám.md
- 02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md
- 02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md
- 02 Tervezet/Gyermekvédelem – release gate.md
- 02 Tervezet/Adatvédelem – tanulói adatok és AI.md
- 02 Tervezet/Program terv.md
- 02 Tervezet/RELEASE-READINESS.md
- 02 Tervezet/Emberi jóváhagyás szükséges.md

Források:
- [h5p-multi-choice semantics.json (H5P, elsődleges)](https://raw.githubusercontent.com/h5p/h5p-multi-choice/master/semantics.json)
- [GDPR (EU) 2016/679, EUR-Lex HU (töredékesen lekérve)](https://eur-lex.europa.eu/legal-content/HU/TXT/HTML/?uri=CELEX:32016R0679)
---
# LENCSE: IMPL

## IMPL-lencse – M0 (6 fájl), finding-lista

A lépéskorlát miatt a vizsgálat egy része elmaradt; a hiányzó részeket a „Vizsgálati pontok” blokk végén, a RÉSZLEGES pontban sorolom fel.

---

**IMPL-1**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** implementáció
- **Hely:** `02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md:298–333` (SLIDE 3)
- **Probléma:** A specifikáció válaszonkénti visszajelzést ír elő (`chosenFeedback`), de a hat opcióból kettőhöz (1. helyzet A, 3. helyzet A) nincs szöveg. A helyes opciókhoz egyetlen összevont szöveg tartozik, amely mindhárom helyzetről szól, ezért az építő ugyanazt a bekezdést tenné be háromszor.
- **Bizonyíték:** :300 „Az alábbi visszajelzések válaszonként (`chosenFeedback`) jelennek meg.” · :327 „Figyeld meg a 2. helyzetet: a madrih **nem engedélyt kér**, hanem **nyíltan megmondja**, kit von be és miért.” A téves szöveg csak a :331-ben van („Visszajelzés téves válasznál a 2. helyzetben (A)”).
- **Hatás:**
  - Az 1. és a 3. helyzet A opciójára (bántás bagatellizálása; kínos kép lájkolása egy kiskorúról) a tanuló csak piros jelölést kap, indoklást nem.
  - A hanihról készülő fotó szabálya (:329) kizárólag a helyes úton jelenik meg.
  - Az 1. helyzet helyes válasza után kiírt összevont szöveg előre elárulja a 2. és a 3. helyzet kulcsát, mert a három MC elem ugyanazon a dián van.
  - A belépőkvíz 5. itemének B-visszajelzése (hub :240) éppen erre a diára utal vissza.
- **Javaslat:**
  - A :325–329 összevont szövegét helyzetenként szét kell bontani, és mindegyik rész csak a saját helyes opciójához kerüljön.
  - Az 1. és a 3. helyzet A opciójához egymondatos téves visszajelzés kell, kizárólag a :325–329 meglévő elveiből (N-M0-14).
  - Javítási korlát: új szabályt nem vezet be; a ✅-jelölések és a 2. helyzet szövege változatlan marad.
- **Típus:** objektív · **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A küszöb egyik nem halasztható sorába sem esik: nem veszélyeztet tanulót, a completion nem függ a helyességtől (H5P-C), a kulcs ép, és nincs placeholder. A 2026-10-10-i döntés szerint freeze-kivételt csak P0 hiba indokolhat.

---

**IMPL-2**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** implementáció
- **Hely:**
  - M0.3 :19, :38, :156–160, :177
  - hub `M0 – Kickoff, keret, technika.md` :85, :254, :259
  - M0.2 :507
  - `Program terv.md` :219
  - `LMS – activity manifest.md` :8, :133, :114–129
- **Probléma:** A tanulói szöveg és a lezárt kvízitem azt ígéri, hogy a peulák a Moodle-kurzus modulstruktúrájában megtalálhatók („`M[szám].A, B` → offline peulák leírásai”, „`Kapu`”). A Program terv modulonként „Peulák”, „Modul-kapu” és „Extra / F-peula” blokkot ír elő. A kánoni build-szerződés (a manifest) viszont egyiket sem definiálja: nincs rá sor, sem kurzus- vagy szakaszszintű elem.
- **Bizonyíték:**
  - M0.3 :159 „– `M[szám].A, B` → **offline peulák** leírásai”
  - MAN :133 „Az offline esemény **nem Moodle-activity**, ezért nem kap fiktív `cmid`-t.”
  - PT :219 „minden modulon belül: „Online mikroleckék”, „Peulák”, „Modul-kapu”, „Extra / F-peula””
  - Az M0.A :610 szerint az M0-ban nincs F-peula; a MAN :248 szerint „a manifestben nincs külön F-peula-activity”.
- **Hatás:**
  - Ha a manifest szerint építenek, az M0 szakaszban nincs M0.A-bejegyzés. A tanuló hiába keresi a peulát, pedig az M0.2 :507 szerint „A következő lépésed: M0.A”.
  - A 7. item kulcsa (C) a kínált opciók közül továbbra is a legjobb, de a „peulákat … a Moodle-kurzusban találod” visszajelzés (:259) nem igaz.
  - Ha az építő a „peula leírása” kifejezést szó szerint veszi, a képzői peulafájl tanulói nézetbe kerülhet. Ez a fájl a 2.4-es red-flag protokollt és a képzői ellenőrző listát is tartalmazza.
- **Javaslat:**
  - A lezárt kvízitem (projektgazdai döntés, 2026-10-02) és a PT :219 szerint a manifestet ki kell egészíteni egy szakaszszintű elemmel: modulonként egy „Peulák” felirat vagy Text and media elem, benne a peula kódja, a kánoni címe és a §7 szerinti dátum.
  - Az elemnek nincs completionje. Amíg a dátum `SCHEDULE_TO_RESYNC`, tanulónak nem látható (PILOT-2).
  - Rögzíteni kell, hogy az M0-ban nincs „Extra / F-peula” elem (M0.A :610), és mi felel meg a „Kapu”/„Modul-kapu” névnek (LMS-M0-05/06).
  - Javítási korlát: a peulafájl képzői szövege nem kerülhet tanulói nézetbe. A peula tanulói leírásának tartalma (mire készüljön a tanuló) nem e finding része, hanem az N-M4-07 kérdése.
- **Típus:** objektív · **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A kvíz diagnosztikus, és a kulcs nem törik el. Az M0.A időpontját a pilot más csatornán is közölheti. A repóból nem állítható, hogy közli-e: ha egyetlen csatornán sem kapja meg a tanuló, a hiány a küszöb „learner nem tudja végigvinni a szükséges M0/M1 útvonalat” sorába esik. Ezt a programvezető ellenőrzi.

---

**IMPL-3**
- **Súlyosság:** P1 · **Bizalom:** magas a mechanizmusra; közepes arra, hogy a döntés ezt nem tudatosan fogadta-e el
- **Lencse:** implementáció
- **Hely:**
  - `LMS – activity manifest.md` :16 (H5P-C profil)
  - M0.1 :13 · M0.2 :13, :15 · M0.3 :14 · M0.4 :14
  - `LMS – H5P runtime acceptance.md` :71 (9. pont)
- **Probléma:** A leckék a completiont az interakciók megválaszolásához kötik („a SLIDE 3 négy Multiple Choice kérdésének megválaszolása”). A rögzített mechanizmus ezzel szemben a „Receive a grade” a Course Presentation összefoglaló diájáról. Ezt az összefoglaló dia megválaszolatlan kérdésekkel is elküldi, tehát egy dián átnavigálás is teljesítést ad.
- **Bizonyíték:**
  - M0.2 :13 „**Completion (lecke):** a SLIDE 3 négy Multiple Choice kérdésének megválaszolása”
  - h5p-course-presentation `src/scripts/summary-slide.js`, `outputScoreStats`: „`if (!this.cp.isSolutionMode && !this.cp.ignoreResize) { this.cp.triggerXAPICompleted(totalScore, totalMaxScore); }`” A kód nem vizsgálja, hogy a kérdések meg vannak-e válaszolva.
  - Az RT 9. pontja csak az összefoglaló dia nélküli esetet teszteli („végiglapozás az összefoglaló dia nélkül nem teljesít”).
- **Hatás:**
  - A tanuló az M0.2 SLIDE 3-at (a titoktartási reflexet) megválaszolás nélkül is teljesítettnek kapja. Az M0 complete állapot így M1-et nyit.
  - A hub §6 completion-analitikája („fejezték be”) erősebb jelzést mutat, mint ami a valóságban teljesült.
  - Ez a minta minden Course Presentation-alapú H5P-C sort érint, nem csak az M0-t.
- **Javaslat:** EMBERI DÖNTÉS (projektgazda; értékelési felelős QA). Két út van:
  - (a) A H5P-C completion jelentése „az összefoglaló dia elérése”. Ekkor a leckék Completion-sorai és a profil szövege ehhez igazodik.
  - (b) A megválaszolást ténylegesen ki kell kényszeríteni. Core Course Presentationben erre nincs beállítás, ezért szerkezeti átépítés kellene.

  Bármelyik út mellett objektív kiegészítés: az RT 9. pontja kapjon negatív esetet („összefoglaló dia megválaszolatlan interakciókkal”).
- **Típus:** emberi-döntés · **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. Az eltérés megengedő irányú: senkit nem blokkol tévesen, és nem tesz ki érzékeny adatot. A freeze-kivétel feltételeinek (P0 biztonsági, adatvédelmi, hozzáférhetőségi vagy előrehaladást blokkoló hiba) nem felel meg.

---

**IMPL-4**
- **Súlyosság:** P1 · **Bizalom:** magas · **Lencse:** implementáció
- **Hely:**
  - `LMS – activity manifest.md` :44 (LMS-M0-06), :155 (§4, M0 sor), :17 (QUIZ-D)
  - hub :170, :181
  - M0.4 :552
- **Probléma:** Az LMS-M0-06 completionje és az M0 complete feltétele „mind a 7 item megválaszolva”. Ilyen completion-feltétel a core Moodle Quizben nincs. A QUIZ-D profil maga is „attempt submitted”-et ír, és a hub csak elhalasztja a kérdést a stagingre.
- **Bizonyíték:**
  - MAN :44 „kitöltve: mind a 7 item megválaszolva”
  - hub :181 „Hogy a Moodle-beállítás kikényszeríti-e mind a 7 item megválaszolását, vagy ezt a stábnak kell ellenőriznie, a stagingben kell igazolni.”
  - MoodleDocs 4.5, Activity completion settings: „Quizzes may be automatically marked complete when one or more attempts have been submitted.” A felsorolt feltételek: grade, passing grade, submitted attempts; olyan nincs, amely minden kérdés megválaszolását követeli.
- **Hatás:** Az LMS-M1-01 („M0 complete”) feloldását ténylegesen a beküldés hajtja. A spec szerinti feltétel nem kódolható, így a build és a dokumentáció szétválik.
  - Mellékmegfigyelés: a QUIZ-D profil a review options beállítást (Specific feedback megjelenítése) sem rögzíti. A hub :183 szerint minden hibás válaszhoz visszajelzés jár, és az M0.3 SLIDE 6 1. kérdésének kulcsa („átnézed, mit rontottál”) is erre épít. Ezt nem ellenőriztem.
- **Javaslat:**
  - A manifest LMS-M0-06 Completion cellája és a §4 M0 sora rögzítse a core-ban beállítható feltételt („Require attempts”/beküldés, QUIZ-D profil).
  - A hub :181 második ága szerint a 7 item megválaszolását a stáb ellenőrzi az első próbálkozás item-statisztikájából. Ez nem unlock-feltétel.
  - Rögzíteni kell a review options beállítást (Specific feedback a próbálkozás után).
  - Javítási korlát: a tanulói M0.4 :552 mondat marad, a kvíz diagnosztikus jellege és a kulcs nem változik.
- **Típus:** objektív · **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. A feltétel megengedő irányban tér el (nem blokkol tévesen), és a tanulói mondat önmagában igaz.

---

**IMPL-5**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** implementáció
- **Hely:**
  - `LMS – activity manifest.md` :267 (`M0_FORUM`, `M0_QUIZ`), :220 (M0 sor), :45 (LMS-M1-01)
  - hub :174–176
- **Probléma:** A §7 határidőt ír elő az M0 kvízre („az M0 kapu-beadása”). A spec nem mondja meg, hogy ez kommunikált célidő-e vagy kemény zárás. Moodle Quizben határidőként csak a „Close the quiz” állítható, ami után nem indítható új próbálkozás. Így a késve érkező madrih nem tudja teljesíteni az M0-t, és az M1 („M0 complete”) zárva marad. Ez ellentmond a puha kapu szabályának („Nincs kizárás”).
- **Bizonyíték:**
  - MAN :267 „`M0_FORUM`, `M0_QUIZ` | §2 szerint | `SCHEDULE_TO_RESYNC` 18:00 (az M0 kapu-beadása)”
  - hub :176 „Nincs kizárás, csak **jelzés és támogatás**.”
  - MoodleDocs 4.5, Quiz settings: „After the closing time, the students will not be able to start new attempts.” Külön, puha „due date” beállítás a kvíznél nincs. A fórumnál a „Due date” puha határidő, ott a kockázat csak a „Cut-off date” beállításnál áll fenn.
  - A :220 M0-sora „Megerősítés” dátumot is ír, pedig az M0-nak nincs megerősítési lépése (QUIZ-D, nincs GATE-CP).
- **Hatás:** A PILOT-2 szerint most konfigurálják a dátumokat. Ha az építő a határidőt zárásként állítja be, a késve érkező tanulót a puha kapu tévesen blokkolja M1 felé.
- **Javaslat:**
  - A manifest §7 rögzítse, hogy az M0_QUIZ és az M0_FORUM határideje tanulónak kommunikált célidő. Kvíznél nincs „Close the quiz”; ha mégis van, a képző felhasználói felülbírálással nyit. Fórumnál nincs „Cut-off date”.
  - Az M0 sor „Megerősítés” cellája „nincs” legyen.
  - Javítási korlát: a HUM-OPS-01 naptárszabályai és az éles kapuk határidő-logikája nem változik.
- **Típus:** objektív · **Verdikt:** —
- **Pilot-besorolás:** PILOT-BLOCKER (feltételes) a küszöb „törött prerequisite/completion/unlock” és „olyan gate, amely tévesen blokkol” sora szerint, de csak akkor, ha az M0_QUIZ határidejét zárásként konfigurálják. A futó pilotban üzemeltetési utasítással, repóváltozás nélkül is elhárítható. A manifest pontosításához freeze-kivétel szükséges (projektgazdai döntés).

---

**IMPL-6**
- **Súlyosság:** P1 · **Bizalom:** közepes · **Lencse:** implementáció
- **Hely:**
  - M0.4 :11, :230–244, :446–454, :527–544
  - M0.1 :11, :268–280, :303–316, :332–336
  - M0.2 :195–199
  - M0.3 :337
  - hub :88
- **Probléma:** A választós elemek build-specifikációja több ponton nem építhető meg egyértelműen:
  - (a) „Single Choice” néven nincs H5P content type. Az egyetlen ilyen nevű típus a Single Choice Set: abban az első alternatíva mindig helyes, válaszonkénti visszajelzés nincs, és alapból magától továbblép. Ezzel szemben a vélemény-itemeknek nincs helyes válaszuk, az M0.4 SLIDE 7 pedig opciónként eltérő visszajelzést ír elő („Teljesen / Félig / Bizonytalan”).
  - (b) Az M0.2 SLIDE 2 opciói nincsenek megadva („felsorolásból 3–4 mondat (pl. …)”). A kérdés egyes számú („Melyik MONDAT … a legjobban”), a típus mégis Multi Choice.
  - (c) Az M0.3 SLIDE 7 „1, 2, 3, 4, 5 (címkékkel)” skálájához csak az 1 és az 5 címkéje van meg.
  - (d) Az M0.1 SLIDE 5 instrukciója „1–2 modul”, a jegyzet „max. 2–3 válasz”. H5P-ben a választások száma nem korlátozható.
- **Bizonyíték:**
  - M0.4 :11 „Beágyazott kérdéstípusok: Single Choice, Multi Choice, Multiple Choice egyválaszos (rádiógombos) módban”
  - h5p-single-choice-set `semantics.json`: „Alternatives - first alternative is the correct one.” és „Automatically go to next question when alternative is selected. This needs to be turned off to make the content fully accessible when using a screen reader.”
  - h5p-multi-choice `semantics.json`: „Single Choice (Radio Buttons)” kérdéstípus és `chosenFeedback`: „Message will appear below the answer on 'check' if this answer is selected.”
- **Hatás:**
  - Ha az építő a „Single Choice” nevet Single Choice Setként értelmezi, az őszinte véleményválaszok hibásnak jelölődnek, és az M0.4 SLIDE 7 opciónkénti visszajelzése nem építhető meg.
  - A (b)–(c) esetben az MCP-építőnek magának kellene opciót és címkét kitalálnia.
  - Az RT 14. pontja (:80–83) csak utólag teszteli az eredményt, építési utasítást nem ad.
- **Javaslat:**
  - Az M0-leckékben a „Single Choice” helyére a valós típus kerüljön: „H5P Multiple Choice egyválaszos (rádiógombos) módban”. Ahol nincs helyes válasz, ott minden opció helyesnek jelölve és opciónkénti `chosenFeedback`-kel, az RT 14. pontja harmadik alpontja szerint.
  - Az M0.2 SLIDE 2 opciói a SLIDE 2 meglévő listamondataiból, szó szerint.
  - Az M0.3 SLIDE 7 közbülső pontjai címke nélküli számok, ezt ki kell mondani.
  - Az M0.1 SLIDE 5-ben egyetlen szám szerepeljen (azt a pedagógiai lencse vagy a CC-04 dönti el).
  - Javítási korlát: a D-i miatt az M0.3 SLIDE 7 nem completion-elem; ezen nem változtat.
- **Típus:** objektív · **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT. Senkit nem blokkol, és a completiont nem érinti. Az „Auto continue” kikapcsolását a hozzáférhetőségi sztenderd :83 human-qa tétele már előírja.

---

**IMPL-7**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** implementáció
- **Hely:**
  - `LMS – activity manifest.md` :41–44
  - M0.2 :508 · M0.3 :364 · M0.4 :551, :562
  - hub :138
- **Probléma:** Ugyanannak az activitynek háromféle neve van: a manifest „Név” oszlopa (ez lesz a Moodle-név és az A11Y-07 szerinti iframe-cím), a tanulói navigációs szöveg, és az M0.4 §4 építési utasítása. Az M0.4 §4 a manifesttől eltérő nevet ad az építőnek.
- **Bizonyíték:**
  - MAN :42 „M0.4 – Dugma isit online”, a tanulói szövegben viszont M0.3 :364 „Moodle → M0.4 – „Dugma isit az online térben + bemutatkozó fórum””
  - MAN :43 „Bemutatkozó fal”, ezzel szemben M0.4 :562 „**Név:** `Bemutatkozó fal – M0`”
  - MAN :44 „M0 belépőkvíz”, ezzel szemben M0.4 :551 „„M0 belépőkvíz: keret, szerepek, technika””
  - Hasonlóan: MAN :41 „M0.3 – Moodle, H5P és kapuk” és M0.2 :508 „„Hogyan működik a Moodle / H5P / kapu?””
- **Hatás:** A tanuló a navigációs szövegben más nevet keres, mint amit a kurzusban lát; a kódelőtag miatt ez csak zavaró, nem blokkoló. Az iframe-cím nem egyezik a lecke saját címsorával. Az építő két ellentmondó utasítást kap.
- **Javaslat:** A manifest a kánoni build-szerződés, ezért az M0.4 :562 építési neve igazodjon a manifest „Név” oszlopához. A tanulói navigációs szövegek a kódelőtag mellett a manifest-nevet használják, vagy a manifest-név vegye át a lecke címét. Arról, hogy melyik irányba egységesítünk, a javítás dönt; tartalmi változás nincs.
- **Típus:** objektív · **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT (a küszöb halasztható „apró copy finomítás” sora; a használhatóságot nem akadályozza).

---

**IMPL-8**
- **Súlyosság:** P2 · **Bizalom:** közepes (a célkörnyezet témája és kurzusformátuma ismeretlen, G3)
- **Lencse:** implementáció
- **Hely:** M0.3 :145, :162, :183 · hub :260
- **Probléma:** A tanulói szöveg és az alt-szöveg azt állítja, hogy a modulok (a szakaszok) mellett pipa jelzi a teljesítést. A core Moodle a teljesítést activity-szinten jelzi. A belépőkvíz kulcsa is ezt mondja („a leckék/activityk mellett”).
- **Bizonyíték:**
  - M0.3 :162 „A modulok mellett a kis **pipák** mutatják, mit fejeztél már be.”
  - M0.3 :183 „Ettől lesz „pipa” a modul mellett.”
  - MoodleDocs 4.5, Using Activity completion: „Completion indicators in the Course index on the left show which activities have to be completed and which still must be done.” A szakaszszintű jelzést a dokumentáció nem említi.
- **Hatás:** A „hol a pipa” tájékozódási cél félrevezető lehet. A 7. item visszajelzése (:257) mást mond, mint a lecke.
- **Javaslat:** A diaszöveg és az alt-szöveg „modul mellett” fordulata igazodjon a 7. item kulcsához: a pipa a leckék és feladatok mellett látszik. Ha a célkörnyezet kurzusformátuma szakaszszintű előrehaladást is mutat, azt a runtime-ban kell igazolni (G3b), nem a szövegben feltételezni.
- **Típus:** objektív · **Verdikt:** —
- **Pilot-besorolás:** POST-PILOT („apró copy finomítás”).

---

**IMPL-9**
- **Súlyosság:** P1 · **Bizalom:** magas (arra, hogy a bizonyíték hiányzik a repóból; a kurzus állapotáról nem állítok semmit)
- **Lencse:** implementáció
- **Hely:**
  - `Emberi jóváhagyás szükséges.md` :550 (PILOT-3)
  - M0.2 :467 · hub :204
  - M0.1 :48–51, M0.2 :53–54, M0.3 :50–51, M0.4 :52–53
  - `LMS – H5P runtime acceptance.md` :86, :145
  - `RELEASE-READINESS.md` :34 (G8)
- **Probléma:** Az M0 tanulói útvonala a technikai segítséget, a mentor elérhetőségét és a Memuna elérhetőségét kizárólag a „Segítség és kapcsolatok” blokkra bízza. A projektgazdai döntés szerint a tanulói pilot csak kitöltött csatornákkal indulhat. Ennek bizonyítéka nincs a repóban: az RT-P0-17 állapota `IMPLEMENTATION_TEST_REQUIRED`, és a G8 „valódi kontaktok” sora RELEASE-EVIDENCE.
- **Bizonyíték:**
  - HUM :550 „a learner-facing pilot release-t viszont blokkolja, amíg a tényleges csatornák nincsenek kitöltve.”
  - M0.2 :467 „amíg a „Segítség és kapcsolatok” blokkban a Memuna és a mentor neve és elérhetősége nincs láthatóan kint, a kurzus nem élesíthető.”
  - A repó-oldal rendben van: az M0-fájlokban nincs `KITÖLTENDŐ`, `SCHEDULE_TO_RESYNC`, kitalált név, telefonszám vagy URL (grep).
- **Hatás:** Ha a blokk üres, a kvíz 2. itemének B-visszajelzése és az összes „ha elakadsz” doboz valódi tanulót üres kontaktra küld. Ez gyermekvédelmi úton is érinti a tanulót.
- **Javaslat:** Megvalósítási döntés: a projektgazda jóváhagyta (PILOT-3); a formális bizonyíték függő. A pilotkurzusban tanulói tesztfiókkal kell visszaolvasni a négy szerep szerinti kontaktot (RT 17. pont), és a G8/G4b bizonyítékként rögzíteni (tracker #4). A repóba nem írunk kontaktot.
- **Típus:** bizonyíték-kapu · **Verdikt:** —
- **Pilot-besorolás:** PILOT-BLOCKER a küszöb „learner-facing placeholder / hibás kontakt” sora és a PILOT-3 szerint. Freeze-kivétel nem szükséges, mert nem tananyag-módosításról van szó, hanem üzemeltetési és bizonyítéki tételről.

---

### Vizsgálati pontok
1. **N-M0-14:** → IMPL-1. A pilotküszöb szerint POST-PILOT. Az építési oldalon a két üres `chosenFeedback` mellett az összevont helyes-szöveg is hiba: előre elárulja a 2. és a 3. helyzet kulcsát.
2. **Az M0.4 visszajelzéseinek teljessége:**
   - A SLIDE 3 → IMPL-1. A SLIDE 7 opciónkénti visszajelzése „Single Choice”-on → IMPL-6.
   - A SLIDE 1, 2 és 5 visszajelzése megvan, vagy véleménykérdésről van szó: ezek nem findingok.
   - A típus és a mező létezik: a H5P Multiple Choice egyválaszos módja és a `chosenFeedback` (semantics.json).
3. **A peulák helye és az unlock-lánc:**
   - A peulák Moodle-beli helye → IMPL-2.
   - Az LMS-M0-01 → 02 → (03 dátum az M0.A után) → 04 → 05/06 lánc egyezik a tanulói szöveggel (M0.2 :507–508, M0.3 :361–365, M0.4 :548–552, M0.A :23–24). Ez nem finding.
   - Az M0 → M1 kapcsolatban két spec-hiba van → IMPL-4 (a „mind a 7 item” feltétel nem kódolható) és IMPL-5 (a kvízzárás tévesen blokkolhat).
   - Ide tartozik a H5P-C completion szemantikája is → IMPL-3.
4. **Placeholder, kontakt, PILOT-4:**
   - Az M0-fájlokban nincs placeholder és nincs kitalált kontakt. A PILOT-3 → IMPL-9.
   - PILOT-4: minden információhordozó vizuálnak van diaszöveges megfelelője (M0.1 SLIDE 2 listája, M0.2 SLIDE 2/4, M0.3-FOTO-01 fallback, M0.4 SLIDE 2–4). Ez nem finding.

**RÉSZLEGES**, a lépéskorlát miatt kimaradt:
- (a) Nem néztem végig a 2026-10-05-i Command 5 naplóját, csak a :23–24, :50 és :72 sort. Nem tudom, hogy a döntés tudatosan elfogadta-e az összefoglaló dia megválaszolatlan elküldését; ezért közepes az IMPL-3 bizalma.
- (b) Nem elemeztem a fórum és a kvíz just-in-time adatkezelési dobozának építési szövegét (hub :164), sem a fórumposztok megőrzési sorát (Adatvédelem :79, :97). Ez a safety-lencse, illetve a DPO területe.
- (c) A QUIZ-D review options beállítását nem vetettem össze a Moodle alapértelmezéseivel; csak megjegyzésként szerepel az IMPL-4-ben.
- (d) Nem hasonlítottam össze teljesen a Program terv :221 alt-szövegeit a leckék alt-szövegeivel (például M0.3 :145 és PT :221).
- (e) Nem ellenőriztem a Moodle dokumentációjában, hogy a 6. item 9 kódos legördülő listája (hub :182) megépíthető-e Matching típussal.

Források:
- [h5p-course-presentation summary-slide.js](https://raw.githubusercontent.com/h5p/h5p-course-presentation/master/src/scripts/summary-slide.js)
- [h5p-multi-choice semantics.json](https://raw.githubusercontent.com/h5p/h5p-multi-choice/master/semantics.json)
- [h5p-single-choice-set semantics.json](https://raw.githubusercontent.com/h5p/h5p-single-choice-set/master/semantics.json)
- [MoodleDocs 4.5 – Activity completion settings](https://docs.moodle.org/405/en/Activity_completion_settings)
- [MoodleDocs 4.5 – Quiz settings](https://docs.moodle.org/405/en/Quiz_settings)
- [MoodleDocs 4.5 – Using Activity completion](https://docs.moodle.org/405/en/Using_Activity_completion)
---
# LENCSE: ERT

## ERT – értékelési lencse, M0 (6 fájl), read-only

**Rövidítések (abszolút útvonalak):**
- [HUB] = 02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md
- [M0.1] = 02 Tervezet/Modulok/M0/Online leckék/M0.1 – Üdv a képzésben! – Éves útiterv & mi köze hozzám.md
- [M0.2] = 02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrih, nem terapeuta – szerepek és elvárások.md
- [M0.3] = 02 Tervezet/Modulok/M0/Online leckék/M0.3 – Hogyan működik a Moodle, H5P és a kapu.md
- [M0.4] = 02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md
- [M0.A] = 02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md
- [MAN] = 02 Tervezet/LMS – activity manifest.md
- [RTA] = 02 Tervezet/LMS – H5P runtime acceptance.md
- [PT] = 02 Tervezet/Program terv.md
- [HUM] = 02 Tervezet/Emberi jóváhagyás szükséges.md
- [PILOT] = 01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntés – pilot-ütemezés és M0+M1 freeze.md (:55–77)
- [CC04] = 01 Fejlesztés/04 Audit/2026-10-10 Projektgazdai döntések – Anna-megfeleltetés indítása, M0.1 POST-PILOT, Moodle-összevetés.md (:41)

A pilot-besorolás alapja a [PILOT] küszöb két listája és a [CC04]:41 feltétele: freeze-kivételt csak P0 biztonsági, adatvédelmi vagy hozzáférhetőségi hiba, illetve a tanulói előrehaladást blokkoló hiba indokolhat. **Egyik finding sem P0**, és a tíz közül egyik sem PILOT-BLOCKER a forrásszöveg alapján. Kettőnél (ERT-2 és ERT-9) runtime- vagy renderellenőrzés mutathat PILOT-BLOCKER állapotot; ezt az adott findingnál jelzem.

---

### ERT-1
- **Súlyosság:** P1 (D3 sárga: „feedback/elosztó finomítandó”). A mátrix P2-jét nem vettem át.
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** [M0.4]:298–333 (SLIDE 3). Ugyanez a minta: [M0.4]:446–454 (SLIDE 5) és [M0.2]:270–279 (SLIDE 3, 2. kérdés).
- **Probléma:**
  - A SLIDE 3 fejlesztői feltétele válaszonkénti visszajelzést ír elő. Az 1. helyzet „csak poén” opciójához és a 3. helyzet „lájkolja a kínos képet” opciójához (A) mégsincs visszajelzés.
  - A három helyes opció egyetlen közös szöveget kap, amely a 2. és a 3. helyzetre is utal. Ha ez az 1. helyzet helyes opciójánál jelenik meg, elárulja a 2. és a 3. helyzet megoldását.
  - A SLIDE 5 Single Choice-hoz egyáltalán nincs visszajelzés megadva.
  - Az M0.2 :279 előírja, hogy a 2. kérdés helyes válaszának visszajelzése legyen a leghangsúlyosabb, a 2. kérdés mégis ugyanazt a szöveget kapja, mint a 3. és a 4. kérdés (:272–273).
- **Bizonyíték:** [M0.4]:300 „Az alábbi visszajelzések válaszonként (`chosenFeedback`) jelennek meg.” / [M0.4]:331 „**Visszajelzés téves válasznál a 2. helyzetben (A):**” (ez az egyetlen téves válaszra írt szöveg).
- **Hatás:**
  - Pont a két gyermekvédelmi szempontból téves reakció (a bántás bagatellizálása; egy hanih kínos képének lájkolása) marad magyarázat nélkül. A fotószabály (:329) csak a helyesen válaszolóhoz jut el.
  - Az [RTA]:81 tesztje ezekre az opciókra nem teljesülhet, mert nincs megjelenítendő szöveg.
- **Javaslat:** /course-fix, POST-PILOT.
  - Az 1. és a 3. helyzet A opciója kapjon egymondatos `chosenFeedback`-et, kizárólag ugyanennek a diának a meglévő állításaiból (:325–329) és a SLIDE 4 1. szabályából. Új szabály nem írható.
  - A közös helyes-válasz szöveget helyzetenként kell szétbontani (1. helyzet: :325; 2. helyzet: :327–328; 3. helyzet: :329), hogy egyik se utaljon másik helyzetre.
  - SLIDE 5: semleges, egymondatos visszajelzés a SLIDE 1–2 mintájára.
  - M0.2 2. kérdés: a helyes válasz saját visszajelzést kapjon, a „ne ígérj teljes titoktartást” mondat szó szerint a :275-ből.
  - Korlát: a ✅ jelölés, az opciók és a helyzetszövegek változatlanok. Mivel látható szöveg változik, utána pin kell, és a szöveg a G1 Memuna-átnézés hatálya alá tartozik.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT.
  - A „nem halasztható” sorok egyike sem teljesül: a kulcs nem törött (✅ :307, :314, :321 helyes), a feladat nem kapu és nem blokkol, adat nem válik láthatóvá. P1, nem P0 ([CC04]:41).
  - Ha a G1 Memuna-átnézés vagy a biztonság-jog lencse a H3-A javítatlan hagyását P0 adatvédelmi vagy gyermekvédelmi hibának minősíti, a freeze-kivételről a projektgazda dönt.
- **Verdikt:** —

### ERT-2
- **Súlyosság:** P1
- **Bizalom:** közepes. A repóbeli hiány biztos; a Moodle- és H5P-viselkedést a célverzión nem igazoltam, elsődleges forrást nem néztem.
- **Lencse:** értékelés
- **Hely:** [HUB]:170, :181; [MAN]:17 (QUIZ-D), :44, :155; [RTA]:71 (9. pont); [M0.1]:13, [M0.2]:13, [M0.4]:14, :552
- **Probléma:** Az M0 completion-feltételei megválaszolást írnak elő: a kvíznél mind a 7 itemet, a leckéknél az előírt interakciókat. A rögzített mechanizmus ezt nem kényszeríti ki: a QUIZ-D completionje „attempt submitted”, a H5P-C-é „Receive a grade” a CP összefoglaló diáján. Egyik negatív esetet sem teszteli a runtime acceptance:
  - üres itemekkel beadott kvíz;
  - összefoglaló dia elérése megválaszolatlan interakciókkal.
- **Bizonyíték:** [HUB]:181 „Hogy a Moodle-beállítás kikényszeríti-e mind a 7 item megválaszolását, vagy ezt a stábnak kell ellenőriznie, a stagingben kell igazolni.” / [MAN]:17 „| **QUIZ-D** | Moodle Quiz, diagnosztikus | attempt submitted |”
- **Hatás:**
  - Az M0 complete, és vele az M1 nyitása (pilot-hatókör) üres kvízbeadással és megválaszolatlan CP-interakciókkal is beállhat, az M0.2 SLIDE 3 jelzési helyzeteit is beleértve.
  - Az üres válaszok lefelé torzítják az első próbálkozás item-statisztikáját, így a §6 „kb. 60%” és „< 50% témakör” jelzése hamis riasztást adhat.
  - Az M0.4 :552 tanulói ígérete („mind a 7 kérdésre válaszolj”) ellenőrizetlen marad.
- **Javaslat:** objektív, spec-szinten.
  1. A két negatív eset kerüljön be az [RTA] 9. pontjába, illetve egy új QUIZ-D pontba, rögzített eredménnyel.
  2. Az LMS-M0-06 sor rögzítse, hogy a [HUB]:181 két ága közül melyik működik ténylegesen. Ha a Moodle nem kényszeríti ki: a stáb a válaszriportban nézi az üres itemeket, és a [HUB]:174 szerinti emlékeztetőt küldi; az üres beadások ne kerüljenek az item-statisztikába.
  - Korlát: a „kitöltés, eredménytől függetlenül”, a cut-score hiánya és a BSPEC-06 mechanizmusa nem változik.
  - Ha a teszt szerint a lecke-completion megválaszolás nélkül is beáll: EMBERI DÖNTÉS (projektgazda és értékelési felelős) a lecke completion-sorainak pontosításáról vagy a mechanizmus módosításáról.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT a forrásban.
  - Az eltérés engedékeny irányú, nem blokkol; a puha kapu a [HUM]:456 lezárt döntése szerint nem blokkol, és van támogató útja ([HUB]:174).
  - A negatív runtime-teszt a PILOT-1 M0+M1 evidence listhez freeze-kivétel nélkül elvégezhető, mert nem szerkeszt tananyagot.
  - Ha a pilotban az M0 complete kvízbeadás nélkül áll be, az „törött completion”, vagyis PILOT-BLOCKER (freeze-kivétel szükséges – projektgazdai döntés).
- **Verdikt:** —

### ERT-3
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** értékelés
- **Hely:** [MAN]:16 (H5P-C profil); [HUM]:561 (D-i); [M0.1]:13; [M0.3]:14 a :77–90-nel együtt; [M0.4]:14
- **Probléma:** A manifest általános szabályként mondja ki, hogy a pontozatlan választók nem önálló completion-elemek. A D-i viszont csak az M0.3 SLIDE 7-re és az M2.2-re terjeszti ki a D-d elvét. Közben a leckék mást írnak:
  - az M0.1 completionje kizárólag pontozatlan véleménykérdésekből áll (SLIDE 3, 4, 5);
  - az M0.3 a SLIDE 1 otthonosság-skáláját completion-elemnek veszi, a SLIDE 7 skáláját nem;
  - az M0.4 négy véleményválasztót számít be (SLIDE 1, 2, 5, 7).
- **Bizonyíték:** [MAN]:16 „A pontozatlan választók nem önálló completion-elemek (M7.4 SLIDE 4: D-d; M0.3 SLIDE 7 és M2.2 értékválasztás: D-i).” / [M0.1]:13 „a SLIDE 3 és a SLIDE 4 Single Choice, valamint a SLIDE 5 Multi Choice megválaszolása”
- **Hatás:**
  - A két kánoni helyből ellentétes completion-konfiguráció vezethető le.
  - Az általános szabály szerint az M0.1-nek, az M0 unlock-lánc első elemének (az LMS-M0-02 előfeltételének) nem maradna completion-eleme.
  - Pontozott véleménykérdés őszinte választ jelölhet hibásnak ([RTA]:83).
- **Javaslat:** EMBERI DÖNTÉS (projektgazda; QA: értékelési felelős): a D-d/D-i elve általános, vagy csak a felsorolt tételekre vonatkozik?
  - Ha általános: az M0.1, az M0.3 SLIDE 1 és az M0.4 completion-sorait újra kell definiálni.
  - Ha tételes: a [MAN]:16 mondatát a D-d/D-i tételeire kell szűkíteni.
  - Korlát: a D-d, a D-i és a BSPEC-06 nem nyitható újra.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT, ha a pilot runtime szerint az M0.1 completion beáll ([RTA]:71 (b)). Ha nem áll be, az „törött prerequisite/completion/unlock”, vagyis PILOT-BLOCKER (freeze-kivétel szükséges – projektgazdai döntés).
- **Verdikt:** —

### ERT-4
- **Súlyosság:** P1 (D3: elosztó finomítandó)
- **Bizalom:** közepes. A szövegre vonatkozó tények biztosak; azt, hogy a QA-bizonyíték hiányzik, a 04 Audit és a RELEASE-READINESS átnézése alapján állítom.
- **Lencse:** értékelés
- **Hely:** [HUB]:180, :187–243 (1., 2., 5. item), :205; [HUM]:473
- **Probléma:**
  - A projektgazdai itemszöveg 1., 2. és 5. itemjében a kulcs az egyetlen többtagú, messze leghosszabb opció (hossz alapján kitalálható).
  - A 2. item kulcsa tartalmazza a „jóváhagyott” szót, amelyet ugyanez a döntési sor az M3-ban árulkodóként kizárt.
  - A 2. item kulcsa a HUM-SAFE-01 4. lépését (azonnal bevonni a Memunát) csak „jóváhagyott gyermekvédelmi út”-ként nevezi meg.
  - A [HUB]:180 szerinti utólagos QA írásos bizonyítéka (értékelési felelős, az 1–2. itemnél a Memuna is) nem található.
- **Bizonyíték:** [HUB]:205 „C) Komolyan veszi, nem ígér teljes titoktartást, nem nyomoz, és a jóváhagyott gyermekvédelmi utat követi; közvetlen veszélyben 112. ✅” / [HUM]:473 „M3: a helyes választ eláruló „jóváhagyott” szó nélkül”
- **Hatás:**
  - A 2. és az 5. item tesztbölcsességgel, tudás nélkül is megoldható. Ez felfelé torzítja a §6 „kihez jelzek?” jelzését, éppen az M2/M3-ráerősítésről szóló döntésnél.
  - A helyesen válaszoló a 2. itemnél nem kap visszajelzést, így a „Memuna azonnal” lépés a kulcsszövegből sem jut el hozzá.
- **Javaslat:** /course-fix-szel nem javítható, mert a szöveg és a kulcs projektgazdai (2026-10-02).
  - Megvalósítási döntés: a projektgazda jóváhagyta; a formális szerepköri bizonyíték (értékelési felelős; az 1–2. itemnél a Memuna) függő.
  - Ez a megfigyelés kerüljön a QA-csomagba. Vétó esetén a tétel REOPENED, és a projektgazdához megy. Answer key-módosítást nem javaslok.
- **Típus:** bizonyíték-kapu
- **Pilot-besorolás:** POST-PILOT. A kulcs nem törött (a jelölt válasz helyes), a kvíz nem kapuz, és nem P0 ([CC04]:41).
- **Verdikt:** —

### ERT-5
- **Súlyosság:** P1 (D1: részleges illeszkedés)
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** [M0.1]:17–19; [HUB]:35, :49, :149–161 (kvízterv); [M0.4]:440–464; [M0.A]:441–446
- **Probléma:** Több kimondott cél- vagy kompetencia-elemhez nincs sem mérés, sem megfigyelés:
  - Az M0.1 mikrocélja azt ígéri, hogy a tanuló felsorolja a 9 állomást kóddal, egy-egy mondatos tartalommal. A leckében csak véleménykérdések vannak, a kvíz 6. iteme 3 témát párosít.
  - A hub 2.5 „legalább 1 saját online határszabály” eleme csak tanuló-lokális, be nem adott jegyzet.
  - A hub 2.2 „2–3 mondat a képzés és a ken elvárásairól” eleme csak az M0.A szóbeli körében hangzik el, rögzítés nélkül.
- **Bizonyíték:** [M0.1]:17 „A lecke végére **fel tudod majd sorolni a képzés 9 állomását a kódjukkal (M0–M7 + Z)**,” / [M0.4]:464 „Írd le magadnak, jegyzetbe vagy papírra; nem adod be.”
- **Hatás:** A kvízterv azt sugallja, hogy a modulcélok mérve vannak; a stáb ezekről a célokról semmilyen jelzést nem kap.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős és modulgazda): a nem mért cél-elemek önellenőrzésként jelölése a kvíztervben, vagy a mikrocél szűkítése a ténylegesen gyakorolt szintre.
  - Korlát: a tanuló-lokális besorolás (BSPEC-02 leltár, D-4) nem fordítható vissza, új adatgyűjtés nem javasolható, a projektgazdai kvízitemek nem bővíthetők.
- **Típus:** emberi-döntés
- **Pilot-besorolás:** POST-PILOT. A használhatóságot nem akadályozza, és egyik „nem halasztható” sor sem teljesül.
- **Verdikt:** —

### ERT-6
- **Súlyosság:** P2
- **Bizalom:** közepes. Hogy a pilot-kurzus ténylegesen mit tartalmaz, nem ellenőriztem.
- **Lencse:** értékelés
- **Hely:** [M0.3]:159, :177; [HUB]:86, :254–262 (7. item); [PT]:219; [MAN]:8, :114–129, :133
- **Probléma:** A tanulói szöveg (M0.3) és a projektgazdai 7. item kulcsa szerint a peulák (leírásai) a Moodle-kurzus modulstruktúrájában vannak, a Program terv modulonként „Peulák” szakaszt ír elő. A build-szerződés (manifest) viszont egyetlen peula-elemet sem specifikál. Ez hiány, nem ellentmondás: a lezárt 7. item a manifest fölött áll.
- **Bizonyíték:** [M0.3]:159 „– `M[szám].A, B` → **offline peulák** leírásai” / [PT]:219 „minden modulon belül: „Online mikroleckék”, „Peulák”, „Modul-kapu”, „Extra / F-peula”.”
- **Hatás:** A [CC04]:43 szerint a Moodle MCP a GitHub-forrásból épít. Ha a manifest szerint épül, az M0.A, M1.A és M1.B tanulói helye hiányzik: az M0.3 állítása és a 7. item kulcsa, valamint a B-opció visszajelzése (:259) a pilot-tanulónak ellenőrizhetetlen, az item mást mér, mint amit állít.
- **Javaslat:** objektív. A [MAN] „Kurzusszintű elemek” része (vagy a §3) egészüljön ki modulonkénti „Peulák” szakasszal és peulánkénti leíráselemmel: nem activity, cmid és completion nélkül, a [PT]:219 és a lezárt 7. item szerint. Az M0-ban F-peula nincs ([M0.A]:610).
  - A leírás tartalma („mire készülj”) nem található ki (N-M4-07 kérdése).
  - Korlát: a 7. item és az M0.3 tanulói szövege nem változik.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT. A peula offline és completion nélküli, a kvíz diagnosztikus, a tanuló végig tudja vinni az útvonalat.
- **Verdikt:** —

### ERT-7
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** [HUB]:229–231 (4. item); [M0.3]:253–257 (SLIDE 5)
- **Probléma:** A 4. item kulcsa és a D-disztraktor az „F-peula” fogalomra épül, a D-visszajelzés pedig az M0.3 5. diájára mutat. Egyik M0-lecke sem tanítja az F-peulát: az M0.3 SLIDE 5 csak visszajelzést és javítási lehetőséget említ.
- **Bizonyíték:** [HUB]:231 „…a kötelező F-peulán (a javítási úton) kell dolgozni; lásd: M0.3, 5. dia (puha és éles kapu) és a Glosszárium F-peula szócikke.” / [M0.3]:257 „– ha nem sikerül → **nem bukás**, hanem jelzés: beszélünk róla, kapsz visszajelzést, javítási lehetőséget.”
- **Hatás:** A tanuló a hivatkozott dián nem találja a szabályt. Az item egy részét nem tanított fogalom hordozza; a „/ javítási úton” glossza miatt az item megoldható, ezért csak P2.
- **Javaslat:** objektív, POST-PILOT. Két lehetőség:
  - Az M0.3 SLIDE 5 éles kapu blokkjába egy mondat, a lezárt döntés szó szerinti átvezetésével ([PT]:242 / [MAN]:149: éles kapunál a javító próbálkozás előtt kötelező F-peula).
  - Vagy a szerkesztői D-visszajelzés hivatkozása mutasson csak a Glosszáriumra.
  - Korlát: a 4. item szövege, a kulcs és a BS-D5 szerinti D-disztraktor nem változik.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT (apró copy-finomítás).
- **Verdikt:** —

### ERT-8
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** [M0.1]:330–351 (SLIDE 5)
- **Probléma:** Az utasítás egyetlen választásba vonja a kíváncsiságot és a félelmet („1–2 modult”). A fejlesztői sor „max. 2–3” választ javasol, a visszajelzés pedig csak a kíváncsiságra és az izgalomra reagál.
- **Bizonyíték:** [M0.1]:332 „…jelölj ki **1–2 modult**, amire most nagyon kíváncsi vagy, vagy amitől kicsit félsz…” / [M0.1]:336 „Opciók (pipa-típus, max. 2–3 válasz javasolt):”
- **Hatás:** A válasz nem értelmezhető (kíváncsiság vagy félelem?), és aki félelmet jelöl, nem kap reflektáló visszajelzést. Pontozatlan item, nem blokkol.
- **Javaslat:** A tartalmi finomítás a lezárt CC-04 döntés szerint POST-PILOT, a pilot-visszajelzéssel együtt; addig nincs módosítás.
  - Most is elvégezhető, objektív lépés: a CC-04 döntés átvezetése a [HUM] új, datált 2026-10-10-i szakaszába (forrás: [CC04]:41). Ma ott nincs 2026-10-10-i döntés-szakasz.
- **Típus:** objektív (átvezetés)
- **Pilot-besorolás:** POST-PILOT ([CC04]:41, lezárt döntés). P0-elem nincs.
- **Verdikt:** —

### ERT-9
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** [M0.2]:195–204 (SLIDE 2)
- **Probléma:** A Multi Choice opciói nincsenek megírva, csak minta szerint vannak megadva. A kérdés egyes számú („Melyik MONDAT”), a típus viszont többválaszos.
- **Bizonyíték:** [M0.2]:199 „Opciók: felsorolásból 3–4 mondat (pl. terápia, éjjel-nappali ügyelet, red flag jelzése stb.)” / [M0.2]:197 „„Melyik MONDAT lep meg a legjobban a fenti listából?””
- **Hatás:** A GitHub-forrásból építő build ([CC04]:43) vagy improvizálja az opciókat, vagy helykitöltő kerül a tanulói felületre. Az utasítás és a típus ellentmond egymásnak.
- **Javaslat:** objektív. Opciók: a „pl.”-ben megnevezett három mondat szó szerint ([M0.2]:187, :190, :192); a negyedik nem található ki. A kérdés és a típus legyen összhangban. Korlát: a SLIDE 2 nem completion-elem ([M0.2]:13), és az is marad.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT a forrásban. A pilot-kurzus renderelt M0.2 SLIDE 2-jét ellenőrizni kell (G4b): ha ott helykitöltő vagy a „felsorolásból…” szöveg látszik, az a küszöb szerint „learner-facing placeholder”, vagyis PILOT-BLOCKER (freeze-kivétel szükséges – projektgazdai döntés).
- **Verdikt:** —

### ERT-10
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** értékelés
- **Hely:** [M0.3]:193 (SLIDE 3, igaz/hamis 2.)
- **Probléma:** Az állítás abszolút kulcsszavai („mindig”, „mindent tökéletesen”) tudás nélkül is elárulják a „Hamis” választ.
- **Bizonyíték:** [M0.3]:193 „2. „A pipa mindig azt jelenti, hogy mindent tökéletesen értek.””
- **Hatás:** Az item nem méri a „pipa = megértés” tévképzetet; aki ezt hordozza, a szöveg formájából is ráérez a helyes válaszra.
- **Javaslat:** objektív, POST-PILOT: az állítás a tévképzet hihető, nem abszolút alakjában. Korlát: a kulcs (Hamis ✅) és a :200–201 visszajelzései változatlanok.
- **Típus:** objektív
- **Pilot-besorolás:** POST-PILOT (apró copy-finomítás).
- **Verdikt:** —

---

### Vizsgálati pontok
1. **N-M0-14 (M0.4 SLIDE 3):** ERT-1. P1 a rubrika D3 sárga sora szerint, POST-PILOT, a G1 Memuna-átnézéshez kötött eszkalációs feltétellel.
2. **N-M0-01 (M0.1 SLIDE 5):** ERT-8. POST-PILOT (CC-04), P0-elem nincs. Mellékteendő a döntés átvezetése a HUM-fájlba.
3. **M0.4 visszajelzések teljessége:** ERT-1. Hiányos a SLIDE 3 (az 1. és 3. helyzet A opciója, a közös helyes-válasz szöveg) és a SLIDE 5 (nincs visszajelzés). Nem finding a SLIDE 1, 2 és 7: a SLIDE 7 válaszonkénti, az 1–2 általános visszajelzést kap, véleménykérdésnél ez elfogadható, a jelölést az [RTA]:83 teszteli.
4. **Belépőkvíz:**
   - Nem finding: mind a 7 kulcs jelölt és a leckeszöveg szerint helyes (a 6. item az [M0.1]:183–199 szerint).
   - Nem finding: a BS-D5 megvalósult. A D) ([HUB]:230) a Q-REL-2 mellett egyértelműen téves, mert éles kapunál az F-peula kötelező ([MAN]:149).
   - Nem finding: minden hibás opcióhoz van egymondatos visszajelzés ([HUB]:190–262).
   - A 2. item kulcsa csak megközelítően igazodik a HUM-SAFE-01-hez, és árulkodó: ERT-4.
   - A „completion = kitöltés” szövegszinten következetes (hub :170/:181, M0.4 :552, M0.3 :282–287, MAN :44/:155, PT :132, HUM :430). A kikényszerítés viszont hiányzik: ERT-2.
   - Az F-peula-hivatkozás: ERT-7.
5. **Peulák Moodle-beli helye:** ERT-6. Nem finding az M0.A ↔ M0.3 sorrend: az [M0.A]:23 megfelel a [MAN]:41 és :137 sorának.

### Korlátok
- Moodle- vagy H5P-runtime-ot nem futtattam. Az ERT-2 és az ERT-3 H5P CP összefoglaló dián és Moodle Quiz beadáson alapuló viselkedését elsődleges forrásból nem ellenőriztem; ezért közepes a bizalom.
- A Glosszárium F-peula szócikkének tartalmát és az M1 F-peula-helyét nem vizsgáltam, mert a scope-on kívül esik.
- A lépéskorlát nem állt meg semmit; a fenti tíz a teljes lista, nem levágott.
