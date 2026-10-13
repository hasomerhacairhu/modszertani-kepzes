# Jóváhagyási csomag – DPO / adatvédelmi és jogi felelős (AP-2026-10-13-01)

> **Audit trail, nem kánon.** Előre kitöltött elfogadási javaslat a 2026-10-13-i futásból. A projektgazda irányait a
> `02 Tervezet/Emberi jóváhagyás szükséges.md` 15. szakasz rögzíti; ahol a döntés vagy a jóváhagyás a címzett szerep hatásköre, az irány **nem helyettesíti** az ő
> döntését. A javasolt szövegek tervezetek: a tananyagba csak az írásos elfogadás után kerülnek, `/course-fix`-szel.
> A tervezeteket read-only szakértői ügynökök készítették, a fő session ellenőrizte; a sorszámok a `8bb4d7d` körüli
> állapotra vonatkoznak, átvezetéskor újra ellenőrizzük őket.

Címzett: a szervezet adatvédelmi felelőse (DPO) / jogi felelős. A megőrzési időt, a jogalapot és az adatkör-besorolást csak a DPO rögzítheti; a tervezetben ezek mezői „DPO tölti ki”.

## Hogyan válaszolj

- Tételenként: **ELFOGADOM** / **MÓDOSÍTOM: …** / **VÉTÓ**, dátummal és szerepnévvel. A repó nyilvános: személynév,
  személyes adat ne kerüljön a válaszba vagy az issue-ba.
- Elfogadásnál a javasolt szöveg (a „DPO tölti ki”, „Memuna dönt” mezők kitöltésével) a következő engedélyezett javítási körben
  kerül be; vétónál a mostani szöveg marad, és az érintett 14. szakaszbeli sor `REOPENED`.
- Az elfogadás nem release-jóváhagyás: a G1–G8 kapuk bizonyítéka és a go/no-go döntés külön lépés (`02 Tervezet/RELEASE-READINESS.md`).
- A válasz helye: a G2 tracker-issue (#2) és a release-jegyzőkönyv (`Program terv.md` §9.3), a 2026-10-12-i P0-kérés D-2 mintája szerint.

## Tételek

| Tétel | Mit kérünk | Kapcsolódó ledger-kulcsok / kapu |
|---|---|---|
| D-11 (vétó/QA) | a projektgazda által elrendelt csoportszűkítés DPO-ellenőrzőlistája (megvalósítva 8bb4d7d; runtime RT-P0-15) | KANON:QA14-BIZT-1, KANON:QA16-IMPL-2, M0:QA14-BIZT-3; BK-07 |
| D-10 | korlátozás, helyesbítés, törlés/megőrzés a feltárást tartalmazó tárolt beadásnál és a Z.4 Feedbacknél (+ Memuna) | M1:QA14-BIZT-5, KANON:QA14-BIZT-4, Z:QA14-BIZT-1, Z:BIZT-G1-2 |
| D-13 (b), (c), (e) | az M4 fókuszmondat-kártya és a Z.A szófelhő-cetli besorolása; az M2 kapubeadvány megőrzési sora | M4:QA14-BIZT-5, Z:QA14-BIZT-3, M2:BIZT-G1-6 |
| D-13 (d) | az M2.A csoportnorma (a Memunával; szöveg a Memuna-csomagban) | M2:QA14-BIZT-7 |
| D-14 | az AI-végpont naplózása, megőrzése, továbbítása; a képző által közvetített AI-út a tanulói tájékoztatóban | KANON:QA14-BIZT-5, KANON:QA14-BIZT-3b |
| ADV-5 | a GDPR 9. cikk szerinti minősítés és kivétel (LMS-M2-07, LMS-M7-10) | M7:BIZT-G1-6; BK-11 |
| ADV-3, ADV-2/ADV-10, ADV-6, LMS-Z-06, ERT-42, ADV-4 | adatkör-aláírás, szereposztás és fiók, fórum, Z.3 megőrzés, adatvédelmi stop, a runtime utáni technika | M4:BIZT-G1-2, M3:BIZT-G2-5, M3:BIZT-G3-8, M3:BIZT-G1-5, M3:BIZT-G2-7, M7:BIZT-G1-1; BK-03, BK-05, BK-06 |
| G2 release-QA | ADV-E1, ADV-E2, ADV-E3 activitynkénti ellenőrzőlista | X-2 |
| Vétó/QA (megvalósítva) | D-12 adatkör; D-13 (a) közös eszköz; D-13 (e) névmező; D-15 (b), (c), (f); D-16 (Z.4) | HUM 15; 8bb4d7d |

## Részletes javaslatok

### P3: DPO / jogi felelős jóváhagyási csomag, tervezet (AP-2026-10-13-01)


**Állítás-osztályok:**
- **PROJEKT-DÖNTÉS (PD):** a HUM 14. szakasz sorai, illetve a HUM-PRIV-01–04.
- **IRÁNY:** a projektgazda 2026-10-13-i irányai (`01 Fejlesztés/04 Audit/2026-10-13 Projektgazdai felhatalmazás és irányok – D-01…D-23, AP-2026-10-13-01.md`). Egy irány nem helyettesíti a szerepköri döntést. A HUM 15. szakasza még nem létezik (Grep: nincs `## 15.`), ezért az irányok kánoni átvezetése a fő session feladata.
- **EJK:** EMBERI JÓVÁHAGYÁS KELL.
- **BK:** bizonyíték-kapu.

**Csomagszintű jóváhagyási szabály (minden tételre):**
- A DPO írásban, dátummal, a szerepe megnevezésével, tételenként „ELFOGADOM / MÓDOSÍTOM: … / VÉTÓ” jelöléssel válaszol.
- A válasz helye: a release-jegyzőkönyv (`Program terv.md` §9.3) és a G2 tracker (#2), a `2026-10-12 P0 jóváhagyási kérés – DPO, PR 30.md` D-2 mintája szerint.
- **Vétónál:** az érintett HUM 14-sor `REOPENED` lesz (HUM:613). A „Most / addig” sor szerinti óvatos állapot marad, és a NEW szöveg nem kerül be.
- **Elfogadásnál:** a NEW szöveg a „DPO tölti ki” mezők kitöltésével kerül be, a hivatkozott bizonyítékkal, a fő session `/course-fix` körében.
- Az elfogadás nem release-jóváhagyás. A G2 csak a 7. tétel ellenőrzőlistájával és a tracker-lezárással zárul.

---

### 1. D-10, DPO-rész (GYV-11, HUM-PRIV-01)

### DPO-1a — Korlátozás, helyesbítés, törlés és megőrzés rendje a tárolt beadásnál
- Fájl: `02 Tervezet/Adatvédelem – tanulói adatok és AI.md:153`
- Alap: GYV-11 (HUM:634, PD), HUM-PRIV-01 (PD), D-10 irány: „incidensnyilvántartás, hozzáférés-korlátozás, dokumentált megőrzés/törlés és feltárásmentes pótlási út”.
- Hatáskör: SZEREP: Memuna + DPO (a, b, f). Jóváhagyási feltétel: mindkettő írásos elfogadása. A pótlásról és a beszámításról (c, d) az értékelési felelős dönt, ez a DPO-csomagon kívül esik.
- OLD: `dokumentálni kell (projektgazdai döntés, 2026-10-12, GYV-11).` (egyedi, :153)
- NEW: `dokumentálni kell (projektgazdai döntés, 2026-10-12, GYV-11). Az eljárás rendje (Memuna + DPO jóváhagyása, <dátum>): (1) a Memuna vagy a helyettese a szükséges tartalmat a gyermekvédelmi incidensnyilvántartásba menti (`Gyermekvédelem – release gate.md` §4.1); (2) a Moodle-példányt <DPO tölti ki: a kijelölt jogosult szerep> korlátozza: elrejti, és elvonja hozzá az értékelői hozzáférést; (3) a végleges törlés kézi, és csak jogi megőrzési felülvizsgálat után történik; a felülvizsgálatot <DPO tölti ki: ki végzi, milyen határidővel>, a döntést <DPO tölti ki: hol dokumentálják>; (4) a Moodle-példány megőrzése a korlátozás alatt: <DPO tölti ki>.`
- Együtt mozgó helyek:
  - `02 Tervezet/Gyermekvédelem – release gate.md:85` (a dokumentálási pont mellé hivatkozás);
  - `02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md:27`;
  - `Z.4 … .md:359` (Assignment-ág, a mondat ma: „Az ilyen beadás kezeléséhez dokumentált, jogosult Memuna-eljárás, szükség szerinti korlátozás vagy helyesbítés, valamint adatvédelmileg jóváhagyott törlési és megőrzési rend kell…”);
  - az M3 KAPU:309 és az M3.4:835 GYV-11-sorai (nem olvastam vissza, G4 nyitott pont).
- Címkék: belső fejlesztői szöveg, nem LÁTHATÓ; nem VÉTÓLISTÁS.
- Indoklás: a G4 (1) opciója. A GDPR 18. cikk (2) szerint korlátozott adattal a tároláson kívül csak szűk célból lehet műveletet végezni. Ezt a G4 **másodlagos forrásból** (gdpr-info.eu) idézte: „such personal data shall, with the exception of storage, only be processed with the data subject's consent or for … legal claims or for the protection of the rights of another natural … person”. Az EUR-Lex 2026-10-13-án nekem sem töltött be, a magyar hivatalos szöveggel össze kell vetni. EJK.
- Vétónál: a :153 változatlan; a GYV-11 sor REOPENED.

### DPO-1b — A „kikerül a Moodle-ből” (HUM-PRIV-01) olvasata
- Fájl: `Adatvédelem – tanulói adatok és AI.md:153`, a DPO-1a mondata után.
- Alap: HUM-PRIV-01 (PD) és GYV-11 (PD): két lezárt mondat, a sorrendjük nincs rögzítve. A G4 szerint az illesztés értelmezés, nem szó szerinti átvezetés.
- Hatáskör: SZEREP: Memuna + DPO.
- OLD: mint a DPO-1a-nál (ugyanabba a bekezdésbe, egy menetben).
- NEW (a DPO-1a NEW-ja után): `A „kikerül a Moodle-ből” (HUM-PRIV-01) itt azt jelenti, hogy az incidensnyilvántartásba mentés után a Moodle-példány korlátozott, kikerül az értékelési és tanulási használatból, és a jogi megőrzési felülvizsgálat után kézi törléssel kerül ki véglegesen; azonnali, felülvizsgálat nélküli törlés nincs (GYV-11).`
- Együtt mozgó helyek:
  - `Adatvédelem…md:75` („Ha feltáráskor mégis megjelenik, kikerül a Moodle-ből…”): marad, a :153 értelmezi;
  - §11:243 (tanulói szöveg: „kikerül a Moodle-ből”): EJK a DPO-nak, lásd lent.
- Címkék: belső szöveg.
- Indoklás: a G4 ajánlása, „(1), amely a felülvizsgálat után a (2)-be fordul”. A (3) (azonnali törlés) ütközik a GYV-11-gyel.
- **DPO-kérdés (EJK):** a korlátozás idején igaz marad-e a tanulói §11:243 „kikerül a Moodle-ből” mondata? Ha nem, a tanulói mondat a HUM-PRIV-01 lezárt szövegét érinti, és a módosításhoz a HUM-PRIV-01 vétó/QA-útja kell, nem ez a csomag.

### DPO-1c — A Z.4 Feedback nyers válaszai (ADV §3:70)
- Fájl: `Adatvédelem – tanulói adatok és AI.md:70`, illetve `02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md:401` és `:370`.
- Alap: HUM-PRIV-03 (PD: 90 nap, utána csak összesítve), GYV-11 (PD, „tárolt beadandó”). Hogy a GYV-11 a Feedbackre is kiterjed-e, nincs eldöntve (D-10 (e)).
- Hatáskör: SZEREP: Memuna + DPO. A visszakeresésnél a jogi felelős is.
- OLD (:70): `| Z visszajelzés nyers válaszai | jogos érdek | 90 nap, utána csak összesítve |` (egyedi)
- NEW, opciónként (a DPO választ, egyet jelöl):
  - **(e-2) adattakarékosabb, és a §3:70 sora változatlan marad.** A Memuna az incidensnyilvántartásba menti a választ, a Moodle-válasz a 90 napos sor szerint megy. Ekkor a Z.4:401 GYV-11-tagmondata (`és ezt a választ jogi megőrzési felülvizsgálat nélkül automatikusan nem töröljük; a korlátozáshoz, … rend kell (projektgazdai döntés, 2026-10-12, GYV-11).`) helyére ez kerül: `; a választ a Memuna az incidensnyilvántartásba menti, a Moodle-beli nyers válasz a 90 napos sor szerint összesítve marad meg (Memuna + DPO jóváhagyása, <dátum>).`
  - **(e-3) adattakarékosabb, a §3:70 változatlan.** Átmentés után kézi törlés a `mod/feedback:deletesubmissions` jogú szereppel (Moodle 4.5 alapértelmezés szerint editingteacher, manager; G4, `mod/feedback/db/access.php`), dokumentáltan. A Z.4:401 NEW-ja: `; a választ a Memuna az incidensnyilvántartásba menti, majd <DPO tölti ki: szerep> dokumentáltan, kézzel törli a Moodle-ből (Memuna + DPO jóváhagyása, <dátum>).`
  - **(e-1)** a feltárást tartalmazó válasz kivétel a 90 napos összesítés alól, korlátozva. Ilyenkor a :70 új sort kap: `| Z visszajelzés gyermekvédelmi feltárást tartalmazó nyers válasza | <DPO tölti ki> | korlátozva; törlés jogi megőrzési felülvizsgálat után, kézzel (GYV-11) |`, és a Z.4:401 marad.
- **Visszakeresés (a jogi felelős is dönt):**
  - (i) tiltott;
  - (ii) csak súlyos veszélynél, a Memuna kérésére, megnevezett adminisztrátor végzi, dokumentáltan.
  - Ha a (ii) mellett döntenek: a Z.4:370 tanulói tájékoztatójába `<DPO tölti ki: tájékoztató mondat>` kell. A HUM-PRIV-03 kanonikus mondata („A válaszok név nélkül jelennek meg a feldolgozásban.”) nem változhat.
- Címkék: a Z.4:370 LÁTHATÓ SZÖVEG (pin kell); az (e-1) a megőrzési mátrixot érinti.
- Indoklás:
  - A G4 a (2)-t vagy a (3)-at ajánlja, mert így a §3:70 változatlan marad. Adattakarékossági szempontból az (e-2) és az (e-3) a jobb.
  - Moodle Feedback FAQ (4.5, a G4 idézete): „the username of the user who took the Feedback is still recorded in the database just as with non-anonymous Feedbacks, but the name is not show to anyone on screen.”
- Vétónál: a Z.4:401 és a §3:70 változatlan.

---

### 2. D-11 (ADV-1, GYV-23, ADV-2, BK-07): DPO-ellenőrzőlista

A kiterjedésről a projektgazda dönt: az IRÁNY szerint mind a négy elemre kiterjed („Separate groups”), megfelelő jogosultságokkal és negatív teszttel, és a csoportmód önmagában nem elegendő. Ezt a fő session a HUM 15-be vezeti át. A DPO itt vétót gyakorol vagy QA-t végez, és nem dönt a kiterjedésről.

### DPO-2 — Ellenőrzőlista (G2 POST-BUILD, RT-P0-15, `LMS – H5P runtime acceptance.md` 15. pont)
A DPO profilonként „rendben / nem rendben / vétó” jelölést tesz, és megadja a staging-bizonyíték hivatkozását (az LMS-gazda tesztje önmagában nem fogadható el: a P0-kérés D-2 pontja).

| # | Ellenőrzendő | Bizonyíték | Elfogadási feltétel |
|---|---|---|---|
| 1 | H5P-C: a „Separate groups” beállítás; a mentor (nem szerkesztő tanár) `moodle/site:accessallgroups` nélkül; a próbálkozás-riport csak a saját csoportot mutatja | role-matrix, két mentor, két csoport | más csoport próbálkozása a közvetlen URL-en sem látható |
| 2 | QUIZ-D/M: csoportmód; a `mod/quiz:viewreports` (RISK_PERSONAL) állapota szerepenként | role-matrix + Responses report képernyő | a mentor csak a saját csoportját látja |
| 3 | **QUIZ-D activity-szintű override (GYV-23):** a nem szerkesztő tanártól elvonják a `mod/quiz:viewreports`-t a belépőkvízen; a csoportszintű korrekcióhoz <DPO tölti ki: melyik szerep> lát összesítést; egyéni utánkövetés csak ideiglenes, dokumentált override-dal | override-napló + runtime-teszt (a statisztika és a Responses report szétválaszthatósága runtime-kérdés, G4) | az egyéni override-ot csak a DPO írásos jóváhagyása nyitja meg, tételenként: pedagógiai cél, érintett tanuló(k), időtartam, ki kapja meg |
| 4 | ASSIGN-S/M: „Separate groups”; a mentor a nem szerkesztő tanári szerepet csak csoportba sorolás után kapja (a TEXT-C BIZT-3 mintája) | RA 15. pont ASSIGN-lépése | **negatív eset:** a csoportba nem sorolt mentorfiók egyik csoport beadását sem látja (G5: a `lib/grouplib.php` szerint ilyenkor az aktív csoport 0, és a kutató a `list_participants()`-ben nem talált extra ellenőrzést, ezért ezt runtime-ban kell eldönteni) |
| 5 | GATE-CP: csoportmód, ugyanaz a negatív eset | role-matrix | mint a 4. sorban |
| 6 | ADV-2: a második vagy fellebbezési értékelő és az F-peula képzőjének hozzáférése | a programvezető írásos szereposztása + hozzáférési napló | a második értékelő csak konkrét eljárásban kap csoporton kívüli hozzáférést, ideiglenesen és dokumentáltan; az F-peula képzője csak összesített vagy minimális hiánylistát lát (ADV §5:148, PD) |
| 7 | Szerkesztő tanár, menedzser, rendszergazda: név szerint kiosztva, auditálható (ADV-1, PD) | kiosztási lista | a lista a privacy felelősnél van; a tanulói szöveg nem tagadja a rendszergazda hozzáférését |
| 8 | A kurzusnapló (`report/log:view`) és a pontkönyv (`moodle/grade:viewall`) mentori láthatósága (ADV:123) | role-matrix | <DPO tölti ki: elfogadható-e a Moodle-alapérték> (EJK) |

- Fájlok, elfogadás után (a fő session szerkeszti):
  - `Adatvédelem…md:104`, `:109`, `:115–117`, `:232`. A `GATE-CP: nincs rögzítve; nyitott: az ADV-1 kiterjedése (BIZT-5)` (egyedi, :117) és a H5P-C/QUIZ cellák „Separate groups” értéket kapnak. Ez a projektgazdai irány átvezetése, a DPO vétó/QA-ja mellett.
  - a MAN ASSIGN-S/M profilsora (:19–20);
  - a QUIZ-D sora (`:116` vége: `a zárt kvíz pontszámát az értékelő látja (§5) |`) kiegészül ezzel: `; a belépőkvízen (QUIZ-D) a nem szerkesztő tanár activity-szintű override miatt nem lát tételszintű egyéni választ; egyéni utánkövetéshez ideiglenes override csak DPO-jóváhagyással (GYV-23; DPO, <dátum>)`.
- BK-07: a teszt után a „csak a kijelölt mentorod” fordulat igazodik a tényleges szerepekhez (M1.4:510, M2.2:499, M2 KAPU:203). Ezek közvetlen következmények, LÁTHATÓ SZÖVEG.
- Vétónál: az ADV-1 sor REOPENED. Az ADV §3 „nincs rögzítve / nyitott” cellái maradnak.

---

### 3. D-12 (GYV-23): adatkör-nyilatkozat

### DPO-3 — A belépőkvíz biztonsági itemjeinek visszajelzése
- Fájl: `02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md:283`
- Alap: GYV-23 (PD), D-12 irány: „név és egyéni eredmény nélküli, csoportszintű visszajelzés”.
- Hatáskör: SZEREP: a döntés a programvezető + Memuna kezében van; a DPO az adatkört nyilatkozza.
- OLD: `első körben csoportszintű, nem megbélyegző korrekció és a két item nyilvános visszajelzése jár.` (a :283 része)
- NEW: `első körben csoportszintű, nem megbélyegző korrekció jár: a két item helyes válaszát és magyarázatát mindenki megkapja, név és egyéni eredmény nélkül (szóban az M0.A-n vagy kurzusüzenetben).`
- **DPO-nyilatkozat (aláírandó szöveg):** „A GYV-23 szerinti csoportszintű visszajelzés során nem kerül közlésre név, egyéni válasz vagy egyéni eredmény; a korrekcióhoz legfeljebb tételszintű összesítés használható, amelyet <DPO tölti ki: szerep> lát. Ha a kvíz review-beállítása is mutatja a két item helyes válaszát (D-12 (2) opció), az nem tesz közzé egyéni adatot. Egyéni mentoros utánkövetés csak a DPO-2 3. sora szerint.”
- Együtt mozgó helyek: a DPO-2 3. sora; (2) esetén a MAN QUIZ-D review-beállítása, runtime-teszttel.
- Címkék: belső, képzői HUB-szöveg; nem VÉTÓLISTÁS (kulcs és küszöb nem változik).
- Indoklás: a G4 (1) opciója, ez adatvédelmileg semleges. A (3) egyéni eredményt tenne közzé.
- Vétónál: a :283 szó szerinti átvezetése marad.

---

### 4. D-13 (b), (c), (e): besorolás és megőrzés

### DPO-4b — Az M4.A és az M4.B fókuszmondat-kártyája (ADV-7)
- Fájlok:
  - `02 Tervezet/Modulok/M4/Peulák/M4.A – Állj oda! – Kiállás & jelenlét a térben.md:381–382`;
  - `…/M4.B – Mit és hogyan kérdezek – Kérdezés & peulabemutató gyakorlása.md:332–333`.
- Alap: ADV-7 (PD). A döntés nem mondja meg, önfeltáró-e a kártya.
- Hatáskör: SZEREP: DPO / jogi felelős, Memuna-QA-val.
- OLD (M4.A): `Ha szeretnéd, tedd a közös ‘M4 – kiállás’ borítékba / falra: ez csak arra lesz, hogy lássuk, milyen fókuszokkal mentek innen tovább.`
- OLD (M4.B): `Ha szeretnéd, itt is hagyhatod névtelenül, vagy el is viheted magaddal emlékeztetőnek.`
- Opciók:
  - **(a) nem önfeltáró** (G4-ajánlás): a szöveg marad, NEW nincs.
  - **(b) önfeltáró:** a boríték-, fali- és bent hagyási opció kikerül. NEW (M4.A): `Ez a tiéd: vidd el magaddal emlékeztetőnek.`; NEW (M4.B): `Ez a tiéd: vidd el magaddal emlékeztetőnek.`; a :382 és a :333 kezelési sora törlendő.
  - **(c)** a kártya a résztvevőnél marad, a képző szóban összesít (az ADV-8 elsődleges útja).
- **Az adattakarékosabb opció: a (b) vagy a (c).** Nem keletkezik begyűjtött papír, és a kis csoportban visszaazonosítható kézírás sem.
- Együtt mozgó helyek: az M4.A @asset blokkja (:304 `purpose`, :336–338 fal-címke). (b)/(c) esetén BUILD-INPUT: az asset kivezetése vagy átírása, utána `media_manifest.py build`.
- Címkék: LÁTHATÓ SZÖVEG (képzői instrukció); (b)/(c) esetén BUILD-INPUT (@asset).
- Vétónál: a szöveg marad (ez a mai állapot).

### DPO-4c — A Z.A szófelhő-cetlije (ADV-7)
- Fájl: `02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md:464–467`
- Hatáskör: SZEREP: DPO / jogi felelős.
- OLD (:467): `* Kérd meg őket, hogy egyenként (vagy egyszerre) vigyék a cetlit a kijelölt felületre (plakát, fal, kör közepe).`
- Opciók:
  - (a) csoportproduktum, fizikai megőrzés (HUM-PRIV-02), az időt a DPO adja;
  - **(b) (G4-ajánlás, és ez az adattakarékosabb)** a NEW a :467 után új alpont: `* A peula végén mindenki elviheti a saját szavát; a bent maradt cetlik kezelése: `Adatvédelem – tanulói adatok és AI.md` §3, „Név nélkül begyűjtött papír munkalap” sor. A felhőről nem készül fotó.`;
  - (c) önfeltáró, a cetli visszakerül a résztvevőhöz.
- **Megjegyzés:** a (b)-ben „A felhőről nem készül fotó” csak akkor maradhat, ha a DPO úgy olvassa, hogy a Z.A:40 HUM-PRIV-02-feltételes fotóútját ez nem zárja ki. Ellenkező esetben a mondat helyére ez kerül: `Fotó csak a Z.A:40 feltételeivel készülhet.` (EJK)
- Címkék: LÁTHATÓ SZÖVEG.
- Nem gyengülhet: „Nevet ne írj rá”, „nincs fotó” alapból, a saját telefon tilalma.

### DPO-4e — Az M2 kapubeadvány (LMS-M2-05) megőrzési sora és a névmező
- Fájlok:
  - `Adatvédelem…md` §3, a :66 után új sor;
  - `02 Tervezet/Modulok/M2/M2 – Kapu – értékelő (item-bank + rubrika).md:214`.
- Alap: D-13 irány: „felesleges névmezők megszüntetése. Megőrzési időt csak DPO-jóváhagyással rögzíts.”
- Hatáskör: SZEREP: DPO / jogi felelős, az LMS-gazdával. **A megőrzési időt csak a DPO rögzítheti.**
- OLD (KAPU:214): `Név (vagy becenév): ______________________   Kvuca / csoport: ______________`
- NEW (KAPU:214), a névmező törlése az irány szerint, az adatminimalizálás miatt (a fiók már azonosít): `Kvuca / csoport: ______________`.
  - A törlés projektgazdai irány, de a sablon tanulói szöveg, ezért a DPO QA-ját kéri.
  - Hogy a „Kvuca / csoport” mező szükséges-e: EJK.
- NEW (ADV §3, új sor): `| Az M2 identitás-jegyzet (LMS-M2-05) | <DPO tölti ki> | <DPO tölti ki: (1) a képzés vége + 90 nap, a „Szabad szöveges reflexió” sor szerint, a Z.4 reflektív beadandó precedense alapján / (2) a képzés vége + 12 hónap, az „Assignment / peulatervek” sor szerint> |`
- Az adattakarékosabb opció: az (1) (rövidebb).
- Együtt mozgó helyek: a §11 „Meddig őrizzük meg?” listája (LÁTHATÓ SZÖVEG, ha az (1)-et választják, mert a tanulói lista ma a beadandókra 12 hónapot mond); a MAN LMS-M2-05 sora.
- Címkék: LÁTHATÓ SZÖVEG.
- Vétónál: a :214 és a §3 változatlan; a sort nem találgatjuk.

---

### 5. D-14 (ADV-12, GYV-10, LMS-8)

Az irány szó szerint: „a nem igazolt AI-adatfolyam maradjon inaktív. A naplózás, megőrzés, adattovábbítás és a képző által közvetített AI-használat dokumentálása szükséges. A no-AI út maradjon egyenértékű.”

### DPO-5a — Az ADV §3 tábla AI-sora
- Fájl: `Adatvédelem…md:73` után (OLD-horgony: `| Gyermekvédelmi incidens |`, egyedi; az új sor a :73 sor után kerül be).
- Alap: ADV-12, GYV-10, LMS-8 (PD), HUM-PRIV-04 (PD), D-14 irány. Az ADV:58 szerint a jogalap és a megőrzés kanonikus helye a §3 tábla.
- Hatáskör: SZEREP: DPO / jogi felelős (QA: programvezető). Jóváhagyási feltétel: a „DPO tölti ki” mezők kitöltése és az ADV-E3 tényellenőrzése (7. tétel).
- NEW (két sor):
  - `| AI-segéd, közvetlen tanulói hozzáférés | — | inaktív: tanulói AI-segéd nincs, amíg a csatornafelmérés (provider, proxy, hibalog, backup, admin) nem igazolja az adatkizárást (projektgazdai döntés, 2026-10-12, GYV-10, ADV-12) |`
  - `| AI-segéd a képző közvetítésével (LMS-8): a képző által küldött prompt és a válasz; személyes adat, hanih-adat, gyermekvédelmi történet nem kerülhet bele (§7) | <DPO tölti ki: jogalap> | a Somer-végpont technikai metaadata: <DPO tölti ki: időtartam>; a tartalom naplózása alapból kikapcsolva (ADV-12); a szolgáltató naplója harmadik félnél: <DPO tölti ki a szolgáltató dokumentációja és a ZDR-állapot alapján> |`
- **A „harmadik fél” mezőhöz idézendő elsődleges forrás:** OpenAI, „Data controls in the OpenAI platform”, https://developers.openai.com/api/docs/guides/your-data (2026-10-13-án magam is megnyitottam):
  - „abuse monitoring logs are generated for all API feature usage and retained for up to 30 days”
  - „Except as noted below, the Responses API has a 30 day Application State retention period by default, or when the `store` parameter is set to `true`”
  - „Currently, these controls are subject to prior approval by OpenAI and acceptance of additional requirements.” (ZDR / Modified Abuse Monitoring)
  - Következmény (TÉNY a forrásból): `store=false` mellett is maradhat tartalom a szolgáltatói visszaélés-naplóban, ha nincs jóváhagyott ZDR. Ez az ADV-12 „store=false önmagában nem bizonyít” mondatát támasztja alá.
- **A verifier B3 szerinti korlátok, és ahogy a tervezet betartja őket:**
  - A sor nem a „Külön review” tanulói listába kerül, hanem a §3 mátrixba.
  - A képző promptját nem minősíti tanulói adatnak: „a képző által küldött prompt”, a jogalapot a DPO adja.
  - Az ADV-12-t nem jelöli nyitottnak: a sor szövege a lezárt szabályt idézi, csak az érték-mezők üresek.
- Címkék: belső szöveg; nem VÉTÓLISTÁS.
- **EJK:** hogy a G5 „jogos érdek + rövid megőrzés + ZDR-kérelem” javaslata elfogadható-e, az a DPO döntése. A tervezet nem írja be.
- Vétónál: a §3 AI-sor nélkül marad, a §7:183 a szabály egyetlen helye. A közvetlen tanulói hozzáférés inaktív (ez a PD alapértelmezése).

### DPO-5b — A tanulói AI-mondat összehangolása (ADV §11:264 és §7:194)
- Fájlok: `Adatvédelem…md:264` (tanulói tájékoztató) és `:194` (kanonikus „Tanulói szöveg”).
- Alap: GYV-10, LMS-8 (PD, 2026-10-12). Az M7 lezárt formulája: `M7.4 …:82`, `M7.2 …:69, :115`: „Az AI-segédet egyelőre a képző kezeli: ha AI-ötletet kérnél, a promptot ő küldi el.” D-14 irány: „a képző által közvetített AI-használat dokumentálása”.
- Hatáskör: SZEREP: programvezető + Moodle-adminisztrátor (LMS-8); vétó/QA: DPO / jogi felelős. A tájékoztató DPO-kapus (ADV:232).
- OLD (:264): `**AI-segéd.** Az AI használata mindig opcionális: minden feladat nélküle is teljesíthető. Saját AI-fiókra nincs szükség: a kurzus AI-segédjét a Somer szervere közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj.` (egyedi a `**AI-segéd.**` miatt)
- NEW (:264): `**AI-segéd.** Az AI használata mindig opcionális: minden feladat nélküle is teljesíthető. Saját AI-fiókra nincs szükség: a kurzus AI-segédjét a Somer szervere közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj. Az AI-segédet egyelőre a képző kezeli: ha AI-ötletet kérnél, a promptot ő küldi el.`
- OLD (:194): `Személyes adatot ide se írj.” Abszolút adatmegőrzési ígéretet` (egyedi)
- NEW (:194): `Személyes adatot ide se írj.” A GYV-10 és az LMS-8 (projektgazdai döntés, 2026-10-12) óta a mondatot ez a mondat követi, az M7.4:82 és az M7.2:69, :115 szövegével azonosan: „Az AI-segédet egyelőre a képző kezeli: ha AI-ötletet kérnél, a promptot ő küldi el.” Abszolút adatmegőrzési ígéretet`
- **A verifier B4 szerinti korlátok, és ahogy a tervezet betartja őket:**
  - A HUM-PRIV-04 mondata szó szerint megmarad, a kiegészítés utána áll. A §7:194 és a §11:264 együtt mozog, így nem tér el egymástól.
  - Az ADV-12 nem jelenik meg nyitottként.
  - A képző promptja nem kap adatminősítést.
- Együtt mozgó helyek:
  - `02 Tervezet/Program terv.md:199` (ugyanez a HUM-PRIV-04 mondat): EJK, igazodjon-e;
  - `Emberi jóváhagyás szükséges.md:189` a lezárt HUM-PRIV-04 döntés szövege, **nem szerkesztendő**.
- Címkék: LÁTHATÓ SZÖVEG (a :264 tanulói, pin kell); nem VO-PACK.
- Vétónál: a :264 és a :194 változatlan. A közvetített út a §7:183-ban és az M7-ben bent marad.

---

### 6. Egyedi DPO-kérdések és nyilatkozatok

### DPO-6.1 — ADV-5 / GDPR 9. cikk (LMS-M2-07, LMS-M7-10; BK-11)
- Fájl: `02 Tervezet/LMS – activity manifest.md:59` (LMS-M2-07: „nyitott: a GDPR 9. cikk szerinti minősítés és kivétel…”), `:95` (LMS-M7-10), `02 Tervezet/RELEASE-READINESS.md:25` (G2, mindkettő már a nyitott DPO-listán).
- Alap: ADV-5 (PD): „GDPR 9. cikk szerinti minősítés és kivétel csak jogi/DPO jóváhagyással.”
- Hatáskör: SZEREP: DPO / jogi felelős; someres vonatkozásban a projektgazda (QA: a helyi ideológiai felelős). Típus: BK (G2, FINAL_RELEASE_QA).
- **Kérdés (szó szerint):** „1) Az LMS-M2-07 záró mondata és az LMS-M7-10 SMART cél R eleme – ha a tanuló saját someres értéket vagy pillér-ágat nevez meg, névhez kötve tárolva – a GDPR 9. cikk (1) szerinti különleges adat-e? 2) Ha igen, melyik 9. cikk (2) szerinti kivétel alkalmazandó: <DPO tölti ki>, vagy a megnevezést tárolt mezőben nem lehet kérni? 3) Elegendő-e az már átvezetett semleges, kitalált vagy kihagyható út (MAN:59, M7.1:526, M7 KAPU:408)?”
- Elfogadás következménye: a MAN:59 és a :95 „nyitott: …” tagmondata a DPO döntésének hivatkozására cserélődik, és a G2 lista két tétele lezárul a trackerben. Ha a DPO szerint nincs alkalmazható kivétel, a két mező tárolt útja külön projektgazdai build-spec döntés (EJK).
- Forrás: a GDPR 9. cikk szövegét nem ellenőriztem (az EUR-Lex nem töltött be), ezért szó szerinti idézetet nem adok.

### DPO-6.2 — ADV-3: az M4 tárolt TEXT-C adatköre (LMS-M4-06, LMS-M4-08; BK-03)
- Fájl: MAN:70, :74; a tanulói ígéret: M4.1:1206, M4.3:650 (a G6 szerint igaz).
- Alap: ADV-3 (PD): „ha … tárolt marad, a tanulói ígéret legyen igaz és a DPO írja alá az adatkört.”
- Hatáskör: SZEREP: DPO / jogi felelős. Típus: BK (G2).
- **Nyilatkozat (aláírandó):** „Az LMS-M4-06 (M4.1, 2 kötelező reflektív válasz) és az LMS-M4-08 (M4.3, kétmondatos reflektív válasz) adatköre: a tanuló saját minivállalása, névhez kötve, TEXT-C profilban. Címzett: a kijelölt mentor a saját csoportjában (ADV §3:118); szerkesztő tanár, menedzser, rendszergazda a §3 szerint. Megőrzés: <DPO tölti ki, alapértelmezett jelölt: a §3 „Szabad szöveges reflexió” sora>. Az adatkört jóváhagyom / nem hagyom jóvá.”
- Elfogadás következménye: a BK-03 lezárul a G2 trackerben, szövegváltozás nincs. A narráció „magadnak” fordulata (M4.1:1199, M4.3:644) VO-PACK (KF-01), ebben a repóban nem változik.
- Vétónál: az ADV-3 REOPENED. Az adatmentes átállás projektgazdai build-spec döntés.

### DPO-6.3 — ADV-2 / ADV-10: F-peula-szereposztás, vészhozzáférés, szervezeti fiók (BK-06)
- Fájl: `Adatvédelem…md:148`; M3.4:67, M3.F:3, :184 (G4 szerint). Az M3.4:801 ADV-10-sora: a sorszámot most nem olvastam vissza.
- Hatáskör: programvezető (szereposztás, fiók), Memuna (a saját szerepe), DPO (ADV-E1, ADV-E2), LMS-gazda (RT-P0-15). Típus: BK (G2, G3b).
- **DPO-kérdés:** „A programvezető által benyújtott F-peula-szereposztást és vészhozzáférési rendet (ki, milyen eseményre, milyen naplózással, mennyi időre kap csoporton kívüli hozzáférést; <programvezető tölti ki>) adatvédelmileg elfogadja-e? A szervezeti Google-fiók adatfeldolgozói és hozzáférési felülvizsgálata (ADV-10) megtörtént-e: <DPO tölti ki: dátum, adatfeldolgozói szerződés helye>?”
- Elfogadás következménye: a BK-06 DPO-része lezárul. Amíg a fiók-felülvizsgálat hiányzik, az opcionális külső Google-eszköz nem engedélyezett (ADV:53, PD).

### DPO-6.4 — ADV-6: a fórum (LMS-M0-05, FORUM-C)
- Fájl: `Adatvédelem…md:79`, OLD-horgony: `addig a szóbeli, nem rögzített bemutatkozás a biztonságos alternatíva;` (egyedi).
- Hatáskör: SZEREP: DPO / jogi felelős; a tájékoztató freeze-kivételéről a projektgazda dönt.
- **Kérdés:** „1) Cél: <DPO tölti ki>. 2) Hozzáférési kör: a kurzus résztvevői (ADV §3:120); kell-e szűkítés? 3) Megőrzési idő: <DPO tölti ki> (a „képzés vége + 90 nap” nem automatikus alapérték, ADV-6). 4) Elfogadja-e a §11-be szánt tanulói tájékoztatót: „a Bemutatkozó fal hozzászólásait <DPO tölti ki> őrizzük meg”?”
- NEW (a :79 vége után, csak elfogadáskor): `a DPO <dátum>-i döntése: cél: <…>; hozzáférési kör: <…>; megőrzés: <…>; tájékoztató: §11;`, és a §3-ba új fórumsor `<DPO tölti ki>`.
- Elfogadás következménye: a fórum megnyitható. A futó kohorsz kezelése a D-15 (f) projektgazdai iránya szerint történik (csak a megnyitás után induló kohorszban feltétel).
- Vétónál: zárva marad, a szóbeli bemutatkozás az alternatíva.

### DPO-6.5 — LMS-Z-06: a Z.3 szöveges válaszai (BS-D6)
- Fájl: `Adatvédelem…md:90` (`a repository nem dönti el; amíg nincs rögzítve`, egyedi), `:239` (a `DPO_RETENTION_TO_CONFIRM` mező), MAN:109.
- Hatáskör: SZEREP: DPO. Típus: G2 nyitott DPO-döntés (RR:25).
- **Kérdés:** „A Z.3 három kötelező szöveges válaszára (köztük a biztonsági lépésre) melyik megőrzési sor vonatkozik: »Szabad szöveges reflexió« (képzés vége + 90 nap) vagy »Assignment / peulatervek« (képzés vége + 12 hónap), esetleg más: <DPO tölti ki>?”
- Az adattakarékosabb opció: a 90 napos sor.
- Elfogadás következménye: a :90 „nincs rögzítve” tagmondata a döntésre cserélődik; a §11 belső mezője kitöltődik („a Z.3 szöveges válaszaidat: <érték>”, LÁTHATÓ SZÖVEG); a MAN:109 igazodik; az activity megnyitható.

### DPO-6.6 — ERT-42: adatvédelmi stop (M7 R8)
- Fájl: `02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md:360` (rubrika); az ADV-ben új eljárás-bekezdés a §5 végén.
- Alap: ERT-42 (PD): „DPO-jóváhagyott korlátozás, incidensértékelés, adateltávolítás és javító leadás. Rubrika és kapuhatás formális döntést igényel.” D-17 irány: „A pedagógiai pontozást és az adatvédelmi stopot külön kezeljük.”
- Hatáskör: értékelési felelős + DPO (QA: DPO + programvezető). A rubrikarész **VÉTÓLISTÁS**, nem a DPO-é.
- **DPO-tervezet (új ADV-bekezdés):** `**Adatvédelmi stop (ERT-42).** Ha egy beadásban harmadik személy (például hanih) azonosítható adata szerepel, a beadás pontszámtól függetlenül nem fogadható el automatikusan. Lépések: (1) korlátozás: <DPO tölti ki: ki, hogyan>; (2) incidensértékelés: hogy a beadott adat személyesadat-incidens-e, a DPO értékeli; (3) az adat eltávolítása: <DPO tölti ki>; (4) javító leadás: a tanuló az adat nélkül újra beadja; hogy ez fogyasztja-e a javító próbálkozást, azt az értékelési felelős dönti el. Gyermekvédelmi feltárásnál a §5 GYV-11-szabálya és a Memuna-út az elsődleges.`
- Elfogadás következménye: az M7 KAPU:360 R8 kettéválasztása (VÉTÓLISTÁS, értékelési felelős) után a rubrika erre a bekezdésre hivatkozik.
- Forrás: GDPR 4. cikk 12. pont, 33. cikk (1). Ezeket sem a G9, sem én nem ellenőriztük élőben, ezért nem idézem.

### DPO-6.7 — ADV-4: tárolásmentes technika (M3 SAFE-1, M3.4 önjelzés)
- Fájl:
  - `…/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md:96` (`„Enable attempt tracking” = Yes`);
  - `…/M3.4 – Do és Don’t madrihként…md:95` (az @asset `notes` mezője: BUILD-INPUT).
- Alap: ADV-4 (PD): a technika a célverziós visszaolvasás után dönthető el.
- Hatáskör: SZEREP: DPO, az M3-nál a Memuna is; a mutatóról a Memuna dönt. **Előfeltétel: BK-05** (az LMS-gazda runtime-visszaolvasása: saved-state, xAPI/LRS, próbálkozás-riport, szerepek).
- **Kérdés (a BK-05 után):** „A visszaolvasott eredmény alapján melyik technika: (a) kikapcsolt próbálkozáskövetés vagy tartalombankos beágyazás; (b) a választó interakció nélküli diára kerül; (c) a követés marad, a riport-capability szűkítésével; (d) <más>? A SAFE-1 csomópontjai nem változnak; az önjelző kérdés nem törölhető, és nem köthető completionhöz.”
- Elfogadás következménye: a M3.3:96 és a M3.4:95 (BUILD-INPUT, `media_manifest.py build`) build-specje igazodik.

---

### 7. G2 release-QA: a DPO írásos ellenőrzőlistája (ADV-E1, ADV-E2, ADV-E3)

Forrás: `RELEASE-READINESS.md:25` (G2: a DPO release-ellenőrzése FINAL_RELEASE_QA), ADV §9 (:209, :211–214, :216, :218), HUM:755–757. Típus: BK. A DPO tölti ki, activitynként.

**A. Activitynként (ADV-E1), minden adatot rögzítő activityre (TEXT-C, ASSIGN-S/M, GATE-CP, QUIZ-D/M, H5P-C, FEEDBACK-N, FORUM-C):**

| Mező | Kitöltendő | Bizonyíték |
|---|---|---|
| build-ID + Moodle `cmid` + kurzusverzió | | staging |
| adatmezők (pontosan mi tárolódik) | | MAN + runtime |
| cél / jogalap / megőrzési sor (ADV §3) | DPO tölti ki | — |
| szerepek: mentor, szerkesztő tanár, menedzser, rendszergazda | | DPO-2 role-matrix |
| export és hozzáférési kérelem | | |
| xAPI/LRS (van-e külső LRS, mi megy ki) | | RT-2 |
| H5P saved-state (tárol-e választ) | | RT-2, RA 15. pont |
| backup (tartalmaz-e felhasználói adatot, ki fér hozzá, meddig) | DPO tölti ki | |
| tartalékút, ha a runtime eltér | | |
| ítélet: elfogadom / vétó (az érintett PD megnevezésével) | | |

Prioritás: az M0/M1 activityk (HUM:755).

**B. Leltár (ADV-E2):**
- a §9:209 többi mezője;
- a nem Moodle-ben vezetett mentori jegyzet;
- a Google-sablonok;
- a papíros munkalapok;
- az adatfeldolgozói és a törlési rend;
- a „Külön review” helyek (ADV:79–91) eredménye.

**C. AI-kapcsolat (ADV-E3, HUM-PRIV-04):** API, közvetítő végpont, szolgáltató, naplózás, retention (a ZDR-állapot írásos igazolása), hozzáférés, adattovábbítás (ország), és a no-AI út egyenértékűségének visszaolvasása (§9:214, POST-BUILD). Amíg ez nincs meg, a közvetlen tanulói hozzáférés inaktív (DPO-5a).

**D. Egyéb sorok:**
- a §11 belső mezői (`PRIVACY_CONTACT_TO_CONFIGURE`, `DPO_RETENTION_TO_CONFIRM`) kitöltve;
- a megőrzési és törlési folyamat tesztelve (§9:213);
- a fotó/videó/hang-folyamat lezárva (§9:216);
- a 6. tétel nyitott DPO-döntései (BS-D6, LMS-M2-07, LMS-M7-10) lezárva.

**Nem fogadható el:** az LMS-gazda tesztje önmagában, generált szöveg vagy AI-összefoglaló. Vétónál a megnevezett PD REOPENED, és a G2 nyitva marad.

---

### (1) Amit nem tudtam ellenőrizni
- A GDPR (17., 18., 9., 25., 33. cikk) hivatalos szövegét: az EUR-Lex HU HTML és ELI oldala 2026-10-13-án sem töltött be. A GDPR-idézetek a G4 másodlagos (gdpr-info.eu) forrásából valók. A 9. cikkhez nem adtam szó szerinti idézetet.
- Az OpenAI-idézeteket magam ellenőriztem (elsődleges forrás). Hogy a szervezetnek van-e ZDR-je: ismeretlen.
- Az M3 KAPU:309 és az M3.4:835 GYV-11-sorát, valamint az M3.4:772/:801 ADV-10-sorát nem olvastam vissza.
- Runtime-tényeket nem ellenőriztem: az Assignment csoport nélküli mentoros viselkedését, a kvízstatisztika és a Responses report szétválaszthatóságát, a H5P saved-state-et.

### (2) Ellentmondás a kánonban
- **ADV §7:194 és §11:264 kontra M7.2:69, :115, M7.4:82 és M7 hub:126:** az M7 tanulói szövegei kimondják a képző által közvetített utat (a hub:126 azt is, hogy „közvetlen tanulói AI-segéd nincs”), az ADV tanulói szövege nem. Az „ide se írj” közvetlen használatot sugall, ami a GYV-10 alatt ki van kapcsolva (DPO-5b). A HUM:189 és a Program terv:199 is a régi formulát hordozza.
- **Z.4:401 (GYV-11-megőrzési kivétel a Feedback-válaszra) kontra ADV §3:70 (90 nap, utána csak összesítve):** ismert, D-10 (e), DPO-1c.
- **ADV §3:** nincs sor a fórumra, az AI-metaadatra és az LMS-M2-05 identitás-jegyzetre. Az utóbbi Assignment, de reflektív; a §11 tanulói lista ma a beadandókra 12 hónapot ígér, ez a DPO-4e (1) opciójánál ütközne.
- **D-11 irány kontra ADV:104, :109, :115–117, :232:** a cellák a „nyitott: az ADV-1 kiterjedése” jelölést viselik, a 2026-10-13-i irány pedig mind a négy profilra kiterjeszti a szűkítést. Az irány még nincs a HUM 15. szakaszában; amíg nincs átvezetve, a cellák maradnak.
- **ADV §11:243 („kikerül a Moodle-ből”) kontra a DPO-1b korlátozás-olvasat:** a tanulói mondat a korlátozás ideje alatt pontatlan lehet. Ez EJK: a HUM-PRIV-01 vétó/QA-útja kell, nem ez a csomag.

Teljesség: mind a hét tétel elkészült, levágott rész nincs.

### Kiegészítő megfigyelések a futásból (nem validált findingok, DPO-kérdésként)

- **M7.F :219, :282 – név nélküli lapgyűjtés:** az M5.F :225 és :302 csak akkor engedi a jegyzetlapok név nélküli begyűjtését,
  ha „ténylegesen senkihez sem köthetők”; az M7.F ugyanezt a feltétel nélkül engedi. Egy kis létszámú F-peulán a kézírás
  azonosíthat. Kérdés: kiterjed-e az ADV §3 „Név nélkül begyűjtött papír munkalap” feltétele az M7.F-re (új alkalmazási eset).
- **M0.A :606 – jelszó-visszaállítás papíros névlistája:** a lista megőrzése és megsemmisítése nincs rögzítve. Kérdés: melyik
  §3-sor vonatkozik rá, és mikor semmisül meg.

## Kiegészítés a célzott QA után (`9788c05`)

A `8bb4d7d` célzott QA-ja (QA17; riport: `2026-10-13 Célzott QA – D-csomagok átvezetése (8bb4d7d), AP-2026-10-13-01.md`) után ehhez a szerephez került tételek. A javasolt szöveg helyett itt a döntési kérdés áll; a javító commit nem implementálta őket.

- **KANON:QA17-BIZT-2b:** a FEEDBACK-N (Z.4) csoportmódja a mentor Z.4-hozzáférésével együtt (Adatvédelem §3, BIZT-6). A kurzus „Separate groups” módja az új activityk alapértéke, ezért a buildnek kifejezett értéket kell adnia; ma a manifest „nyitott”-nak jelöli. Opciók: „No groups” (csak a szerkesztői szerepek látják a név nélküli feldolgozást) / „Separate groups” (a mentor a saját, legfeljebb 8 fős csoportjáét látja – kisebb csoportnál könnyebb a visszaazonosítás).
- **KANON:QA17-BIZT-7 (adatkör):** a mentor pontkönyvi rálátása a saját csoportja egyéni LMS-M0-06-pontszámára (a programvezetővel és a Memunával).
- **Átvezetve, DPO-QA-ra (vétó):** az LMS-M0-06 override a `mod/quiz:grade`-et is elvonja (a Manual grading riport ezzel nyílik); a FORUM-C „Group mode” = „No groups”; a Memuna ADV-2 szerinti, eljáráshoz kötött hozzáférése (KANON:QA17-IMPL-2, -BIZT-2, -BIZT-6).
