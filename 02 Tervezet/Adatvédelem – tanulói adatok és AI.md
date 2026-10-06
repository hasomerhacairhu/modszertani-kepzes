# Adatvédelem – tanulói adatok és AI

## 1. Release-szabály

A learner-facing Moodle-kurzust a tényleges adatkezelő szervezet privacy/DPO/jogi felelőse hagyja jóvá. Zárt stagingben csak szintetikus tesztadat használható.

A repository **nem választ jogalapot, megőrzési időt vagy szülői folyamatot a szervezet helyett**. Ezek a döntések az `Emberi jóváhagyás szükséges.md` fájlban, stabil azonosítókkal élnek:

- **HUM-PRIV-01:** Moodle-adatkezelési mátrix;
- **HUM-PRIV-02:** fotó, videó, hang és kézírás;
- **HUM-PRIV-03:** Z.4 visszajelzés anonimitási szintje;
- **HUM-PRIV-04:** külső generatív AI tanulói használata.

Mind a négy tételben **projektgazdai döntés (2026-10-02)** született, a jogalapról és a megőrzési időről is; a tartalmukat a §3, a §4, a §5, a §6, a §7 és a §8 rögzíti. A tételek az `Emberi jóváhagyás szükséges.md`-ben lezártak. A DPO/jogi felelős (a HUM-PRIV-03-nál és a HUM-PRIV-04-nél a programvezető is) későbbi ellenőrzése **utólagos ellenőrzés (vétó/QA)**, nem új döntési kapu. A release-szabály és a §9 átvételi listájának nyitott sorai változatlanul érvényesek.

A tananyag AI-generált médiájának jogi, adatvédelmi és gyermekvédelmi kapuit (a HUM-MEDIA-02 J1, J2, V1 és V3 alkapuját, valamint a HUM-MEDIA-03-at) az `Emberi jóváhagyás szükséges.md` 5. szakasza tartja nyilván. **Projektgazdai döntés (2026-10-02)** – utólagos ellenőrzés (vétó/QA): a release owner és a jogi/adatvédelmi felelős. A jogi és gyermekvédelmi médiakapuk blokkolják az általuk érintett tanulói asset release-ét. A hangjogosultsági bizonyítékok helye a korlátozott hozzáférésű `VOICE-RIGHTS-REGISTER` nyilvántartás (Google Workspace Shared Drive → `Restricted / Rights / Voice`); valódi név nem kerül a Gitbe (részletek: az `Emberi jóváhagyás szükséges.md` HUM-MEDIA-02 tétele és a `Média-assetek/RIGHTS-EVIDENCE.md`).

## 2. Adatminimalizálási alapelv

Minden learner inputnál ebben a sorrendben kérdezzük:

1. szükséges-e egyáltalán begyűjteni;
2. szükséges-e Moodle-ben tárolni;
3. szükséges-e, hogy mentor/képző lássa;
4. elég-e, ha csak a madrih saját jegyzetében marad;
5. elérhető-e ugyanaz a pedagógiai cél kevesebb személyes adattal;
6. kérünk-e érzékeny vagy más személyre vonatkozó adatot valódi indok nélkül.

**Alapértelmezés:** ami csak önreflexióhoz kell, maradjon a madrihnál, hacsak a tanulási cél nem igényel beadandó produktumot. Érzékeny identitás-, családi-, egészségügyi/mentális vagy gyermekvédelmi történet **nem lehet kötelező tanulási artefaktum**. Mindig elfogadható legyen fiktív, általánosított vagy csak a tanulónál maradó alternatíva, ha a személyes adat nem a mérés tárgya.

## 3. Activity-szintű adatleltár

Az `LMS – activity manifest.md` minden tényleges activityhez privacy-osztályt rendel. Az LMS-owner + privacy felelős activitynként ezeket a mezőket tölti ki; a jogalapot és a megőrzést a lenti mátrix adja (HUM-PRIV-01):

| Mező | Kötelező tartalom |
|---|---|
| adatmező | pontosan mi kerül tárolásra |
| cél | miért kell ehhez a pedagógiai/üzemeltetési célhoz |
| jogalap | a lenti jogalap- és megőrzési mátrix szerint |
| kötelező/opcionális | része-e a teljesítésnek |
| címzettek | ki láthatja |
| szerepkör | milyen Moodle-role/capability alapján |
| megőrzés | konkrét idő vagy esemény, a lenti mátrix szerint |
| törlés | automatikus/manuális folyamat + felelős |
| export/hozzáférési kérelem | hogyan teljesíthető |
| harmadik fél | szolgáltató, adatfeldolgozói szerep, ország/adattovábbítás |
| kiskorú-specifikus szabály | ha alkalmazandó |

**Projektgazdai döntés (2026-10-02), HUM-PRIV-01** – utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős. A döntés tartalma:

- a fenti mezőtáblázat, a lenti jogalap- és megőrzési mátrix és az `LMS – activity manifest.md` privacy-osztályai együtt alkotják az **egyetlen activity-szintű adatkezelési mátrixot**; más dokumentum (a `Program terv.md` §4 és §7 tájékoztató-sablonja és a modulok) erre hivatkozik;
- mindenhez a **legszűkebb szükséges hozzáférés** jár; a szerepkörönkénti alapszabályokat, köztük a mentori jegyzetre vonatkozót, a §5 rögzíti;
- Google-sablon csak **szervezeti fiókban**, korlátozott megosztással használható;
- politikai, vallási vagy világnézeti válasz **nem lehet fiókhoz kötött szavazás**: az ilyen kérdés rögzítés nélküli önreflexió (a tanuló magában vagy papíron gondolja végig, a rendszer nem tárolja a választ);
- ha a `Program terv.md` §4 és §7 szabálya ütközik, **a szigorúbb, kisebb hozzáférést engedő szabály** érvényes;
- a jogalapot és a megőrzési időt adattípusonként a lenti mátrix rögzíti.

**Jogalap és megőrzés (projektgazdai döntés, 2026-10-02; HUM-PRIV-01, HUM-PRIV-02)** – utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős. A jogalap és a megőrzés kanonikus helye ez a tábla; az `LMS – activity manifest.md` privacy-megjegyzései erre hivatkoznak.

| Adat | Jogalap / kezelés | Megőrzés |
|---|---|---|
| Moodle-fiók, részvétel, végső completion | jogos érdek, a képzés működtetése | a képzés vége + 24 hónap |
| Nyers kvízpróbálkozások | jogos érdek, értékelés/diagnosztika | a végső megerősítés + 90 nap |
| Végső pontszám / kapueredmény | jogos érdek, a teljesítés igazolása | 24 hónap |
| Szabad szöveges reflexió (a Z.4 beadandó is) | jogos érdek, kizárólag ha szükséges | a képzés vége + 90 nap |
| Assignment / peulatervek | jogos érdek | a képzés vége + 12 hónap |
| Név nélkül begyűjtött papír munkalap | név nélkül, papíron begyűjtve | a peula után összesítés, majd 30 napon belül megsemmisítés |
| Mentori 1:1 meta-napló | jogos érdek, gyermekvédelmi elszámoltathatóság | az utolsó mentorálás + 6 hónap |
| Mentori fejlesztési jegyzet (akkor is, ha nem Moodle-ben készül; a terepi megfigyelési jegyzet is) | a mentori 1:1 meta-napló sora szerint (jogos érdek); csak a fejlődéstámogatáshoz szükséges minimális adat (§5) | az utolsó mentorálás + 6 hónap |
| Z visszajelzés nyers válaszai | jogos érdek | 90 nap, utána csak összesítve |
| Hanih-visszajelzés, Moodle-on kívül | név nélkül, papíron vagy szervezeti űrlapon | 90 nap |
| Fotó/videó/hang (a tanuló saját videója is) | külön, önkéntes hozzájárulás: 18 év alatt a résztvevő és a gondviselő együtt adja, 18 év felett a résztvevő (§4) | a cél teljesüléséig, legfeljebb 90 nap, hacsak nincs külön archiválási hozzájárulás |
| Gyermekvédelmi incidens | külön, korlátozott hozzáférésű rendszer | az érintett 25. születésnapjáig vagy a lezárás + 7 évig (amelyik később jár le); jogi visszatartás esetén tovább |

Politikai, vallási, egészségügyi vagy más különleges adat **normál tanulási activityben nem gyűjthető**. Ha feltáráskor mégis megjelenik, kikerül a Moodle-ből, és az incidensfolyamatba kerül (`Gyermekvédelem – release gate.md` §4.1). Programmutatóként a gyermekvédelmi incidensekről csak összesített darabszám szerepelhet, azonosító nélkül. A mentori 1:1 meta-naplóba csak dátum, résztvevők, időtartam, célkategória és utánkövetés kerül, a beszélgetés tartalma nem (`Gyermekvédelem – release gate.md` §4.2).

Külön review szükséges legalább:

- M0 „Bemutatkozó fal”: kurzuson belül más résztvevőknek látható;
- M1 SBI-beadandó;
- M2 identitás- és értékreflexiók, identitás-jegyzet, az M2.1 identitás-kör kérdése (a válasz nem kerül tárolásra: önellenőrző, nem rögzített elem – H5P-activityként kikapcsolt „Enable attempt tracking” beállítással, vagy tartalombankból oldalba ágyazva; a completion nem erre a válaszra épül), valamint az M2.3 pillér-kérdése (nem lehet fiókhoz kötött szavazás);
- M3 gyermekvédelmi helyzetelemzés: a kapuproduktumba **csak kitalált, életszerű eset** kerülhet, valós eset névtelenítve sem, mert kis közösségben könnyen visszaazonosítható; valós gyermekvédelmi eset soha nem pedagógiai feladat;
- M4 peulabemutató és bármilyen felvételi folyamat;
- M5/M6 produktumok;
- M6 fotó/kézműves dokumentáció, ha egyáltalán szükséges;
- M7 AI-promptok és Peula v1/v2; a Peula v2 valós kvucára is tervezhető, de csak nem azonosító, csoportszintű információval (nevek, egyéni érzékeny történetek, diagnózisok és hasonlók nélkül); saját kvuca hiányában a tanuló kitalált profilt kap;
- a modulhubok és az F-peulák nem Moodle-ben vezetett mentori jegyzete, valamint a Google-sablonok (M5.4, M6);
- Z.2/Z.4 személyes reflexiók és mentor-hozzáférés;
- a Moodle-oldali kötelező szövegmezők (`LMS – activity manifest.md`, TEXT-C profil: nem anonim Moodle Feedback, a válasz a tanuló nevével rögzül, és a tanuló a saját válaszát felülírhatja): activitynként a fenti mezőtáblázat szerint;
- a Z.3 kötelező szöveges válaszai (LMS-Z-06): a megőrzési sor („Szabad szöveges reflexió” vagy „Assignment / peulatervek”) DPO-döntés (BS-D6), a repository nem dönti el; amíg nincs rögzítve, az activity valódi madrihnak nem nyitható meg (Program terv §4);
- Z.4 Moodle Feedback.

A lista M2-, M3- és M7-sorának szabálya **projektgazdai döntés (2026-10-02)**; utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős, az M3-sornál a Memuna is, az M7-sornál a programvezető is.

### Activity-szintű adatleltár – build-rész (PR-01)

A fenti mezőtáblázatból a buildhez szükséges rész: a **címzettek**, a **Moodle-szerepkör/capability** és a **mentor-láthatóság mechanizmusa**, profilonként. Egy activity sorát az `LMS – activity manifest.md` §2 „Profil” oszlopa köti ide; az activitynkénti eltéréseket a manifest adott sora és a fenti „Külön review” lista rögzíti. A többi mező (adatmező, cél, a jogalap- és a megőrzési sor hozzárendelése, törlés, export/hozzáférési kérelem, harmadik fél, kiskorú-specifikus szabály) kitöltése az LMS-gazda és a privacy felelős feladata (§9). A Moodle-alapértelmezések forrása a Moodle 4.5 `db/access.php` fájljai (`MOODLE_405_STABLE`); a célverzión a tényleges szerepkiosztást és capability-állapotot stagingben tesztfiókkal vissza kell olvasni (runtime acceptance 15. pont; §5).

**Szerepkörök a kurzusban:**

| Moodle-szerep | Kinek | `mod/feedback:viewreports` | `moodle/site:accessallgroups` | Mit lát a P2 szövegekből |
|---|---|---|---|---|
| Tanuló (Student) | a madrihok | nincs | nincs | csak a saját válaszát; a TEXT-C-ben a `mod/feedback:viewanalysepage` tiltva (`LMS – activity manifest.md` §1) |
| Nem szerkesztő tanár (Non-editing teacher) | a kijelölt mentor/értékelő | van (alapértelmezés) | nincs (alapértelmezés; nem kaphatja meg) | a TEXT-C-ben csak a saját mentor-csoportja válaszait (lent); az ASSIGN-S/M és a P2-es H5P-C adatait a Moodle-alapértelmezés szerint csoporttól függetlenül (lent, profiltábla; a szűkítés DPO-kérdés: BIZT-5) |
| Szerkesztő tanár (Editing teacher) | a kiosztást a privacy felelős tölti ki | van (alapértelmezés) | van (alapértelmezés) | csoporttól függetlenül minden választ |
| Menedzser (Manager) | a kiosztást a privacy felelős tölti ki | van (alapértelmezés) | van (alapértelmezés) | csoporttól függetlenül minden választ |
| Rendszergazda (site administrator) | a kiosztást a privacy felelős tölti ki | minden capability | minden capability | minden választ |

A szerkesztő tanári, a menedzseri és a rendszergazdai, csoporttól független hozzáférés elfogadhatósága DPO-kérdés (BIZT-2): ez a szakasz nem dönti el.

**Profilonként: ki lát még tanulói adatot** (Moodle 4.5 alapértelmezés):

| Profil (`LMS – activity manifest.md` §1) | A tanuló | Ki lát még (capability) | Csoport szerinti szűkítés | Megjegyzés |
|---|---|---|---|---|
| H5P-C | a saját próbálkozásait | a próbálkozás-riportot (`mod/h5pactivity:reviewattempts`): nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve: DPO-kérdés (BIZT-5) | a tanuló-lokális lépések nem tárolódnak (manifest §2); a riport tényleges tartalmát a runtime acceptance 15. pontja olvassa vissza |
| QUIZ-D, QUIZ-M | a saját próbálkozásait és eredményét | a kvízriportot és az értékelést (`mod/quiz:viewreports`, `mod/quiz:grade`): nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve (BIZT-5) | a zárt kvíz pontszámát az értékelő látja (§5) |
| ASSIGN-S, ASSIGN-M, GATE-CP | a saját beadványát és értékelését | az értékelői nézetet (`mod/assign:grade`, `mod/assign:viewgrades`): nem szerkesztő tanár, szerkesztő tanár, menedzser | nincs rögzítve (BIZT-5) | P2 beadandót csak a kijelölt értékelő/mentor lát, csak ha ténylegesen szükséges (§5) |
| TEXT-C | a saját válaszát (felülírhatja) | a válaszokat (`mod/feedback:viewreports`): a kijelölt mentor a saját csoportjában; a szerkesztő tanár, a menedzser és a rendszergazda csoporttól függetlenül | Separate groups (a mechanizmus lent) | — |
| FEEDBACK-N (Z.4) | — | a válaszokat név nélkül megjelenítve (`mod/feedback:viewreports`; HUM-PRIV-03) | — | a mentor hozzáférése DPO-kérdés (BIZT-6) |
| FORUM-C | a kurzus résztvevőinek posztjait | a kurzus résztvevői | — | a résztvevő előre tudja, hogy a csoport látja (§5) |
| PAGE-C | — | — | — | tanulói adatot nem rögzít |

A kurzusnaplót (`report/log:view`) és a pontkönyvet (`moodle/grade:viewall`) alapértelmezésben a nem szerkesztő tanár, a szerkesztő tanár és a menedzser látja.

**A mentor-láthatóság mechanizmusa (TEXT-C).** Projektgazdai döntés (2026-10-05; `01 Fejlesztés/04 Audit/2026-10-05 Projektgazdai döntések – build-blocker leltár D-a…D-d.md`, 1. szakasz 2. pont). Ez technikai hozzáférés-szűkítés, nem a BS-D1 által elvetett, csoport-alapú kapuállapot. A döntés feltételes: a mechanizmust az RT-P0-15 kiterjesztett stagingtesztjének kell igazolnia; a DPO QA megmarad.

- A TEXT-C activity csoportmódja („Group mode”) „Separate groups”, groupingot nem kap („Grouping”: nincs); a kurzus „Force group mode” beállítása „No” (BIZT-4, BIZT-3). Group- vagy Grouping-alapú hozzáférési feltétel sehol nincs (BS-D1).
- A kurzus csoportjai a mentor-csoportok: minden tanuló a saját mentor-csoportjában van, és a kijelölt mentor ugyanennek a csoportnak a tagja. Más célú csoport a kurzusban nem jön létre; ha mégis kell, a TEXT-C elkülönítése új build-spec kérdés (BIZT-3, grouping-ág).
- A mentor a nem szerkesztő tanári szerepet csak a csoportba sorolása után kapja meg, mert a csoport nélküli, `mod/feedback:viewreports` jogú néző az elemzőoldalon és az Excel-exportban minden választ látna (BIZT-3).
- A mentor nem kap `moodle/site:accessallgroups` jogot; a tanuló nem kap riport-capabilityt.
- „Enable notification of submissions” = „No” (BIZT-11): így a `mod/feedback:receivemail` jogúak nem kapnak a beküldőről nevet és közvetlen linket tartalmazó értesítést.

## 4. Kiskorúak és hozzájárulás

A GDPR 8. cikke csak akkor alkalmazandó a saját korhatárszabályával, ha **az adatkezelés a 6. cikk (1) a) szerinti hozzájáruláson alapul, és információs társadalmi szolgáltatást kínálnak közvetlenül gyermeknek**. A GDPR alapesetben 16 éves korhatárt ír elő, és lehetővé teszi, hogy a tagállam ezt 13 éves korig csökkentse.

Ez **nem** jelenti azt, hogy „minden 18 év alatti Moodle-adatkezeléshez szülői hozzájárulás kell”. A képzés minden adatkezelési céljának jogalapját külön kell meghatározni, és azt is külön kell vizsgálni, hogy a GDPR 8. cikke egyáltalán alkalmazandó-e.

A szülői/gondviselői tájékoztatás vagy engedélyezés helyi folyamata ezért **emberi és jogi döntés (HUM-PRIV-01, HUM-PRIV-02, HUM-SAFE-03)**, nem a tananyag által kitalálható szabály. A jogalapot adattípusonként a §3 mátrixa rögzíti (projektgazdai döntés, 2026-10-02); a gyermekvédelmi helyzetben alkalmazandó gondviselői szabály a `Gyermekvédelem – release gate.md` §4.3-ban áll.

**A hozzájárulás adója kiskorúnál (projektgazdai döntés, 2026-10-02; HUM-PRIV-02)** – utólagos ellenőrzés (vétó/QA): a DPO. Ahol a jogalap külön, önkéntes hozzájárulás (fotó, videó, hang, a tanuló saját videója is; §3, §6), ott **18 év alatt a résztvevő és a gondviselő együtt** adja a hozzájárulást, 18 év felett a résztvevő.

## 5. Mentor- és képzői hozzáférés

A „mentor láthatja, mert hasznos lehet” nem elég indok. Az alábbi alapszabályok a HUM-PRIV-01 **projektgazdai döntését (2026-10-02)** követik; utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős (§3).

- **P0–P1 privacy-osztály** (az `LMS – activity manifest.md` 1. szakasza szerint): csak az a szerepkör lássa, amelynek a completion/értékelés üzemeltetéséhez szüksége van rá; a zárt kvíz pontszámát az értékelő látja.
- **P2 privacy-osztályú beadandó, szabad szöveg, reflexió:** csak a kijelölt értékelő/mentor, csak ha ténylegesen szükséges, és csak a szükséges ideig (a megőrzési idő: §3).
- **kurzusfórum:** a résztvevő előre tudja, hogy a csoport látja.
- **saját önreflexió:** ne legyen mentor-látható, ha nincs rá konkrét pedagógiai szükség.
- **mentori jegyzet** (akkor is, ha nem Moodle-ben készül): csak minimális, a fejlődéstámogatáshoz szükséges adat; „árnyékdosszié” nincs. Megőrzése a §3 mátrixának „Mentori fejlesztési jegyzet” sora szerint; ide tartozik a terepi megfigyelési jegyzet is.
- **mentori 1:1 meta-napló:** csak dátum, résztvevők, időtartam, célkategória és utánkövetés, a beszélgetés tartalma nem (`Gyermekvédelem – release gate.md` §4.2); megőrzése a §3 mátrixa szerint.
- **gyermekvédelmi feltárás:** nem normál tanulási rekord, és nem kezeljük egyszerű „tanulói beadandóként”: a `Gyermekvédelem – release gate.md` §4.1 szerinti ötlépéses jelzési út lép életbe, a dokumentáció pedig nem Moodle-be, hanem külön, hozzáférés-korlátozott gyermekvédelmi incidensnyilvántartásba kerül. A nyilvántartás helye: Google Workspace Shared Drive → `Restricted / Safeguarding / Incidents`; hozzáférés csak a Memunának, a helyettesnek és a szervezeti vezetőnek, nem Moodle, nem GitHub (HUM-SAFE-01). Ha a feltárásban különleges adat jelenik meg, az kikerül a Moodle-ből, és az incidensfolyamatba kerül (§3).

A tényleges Moodle-role/capability beállítást stagingben vissza kell olvasni és tesztfiókokkal ellenőrizni.

## 6. Fotó, videó, hang és kézírás

Felvétel csak előre rögzített cél, jogalap, hozzáférés, tárolási hely, megőrzés és törlés mellett kerülhet a folyamatba.

**Első kérdés:** kell-e egyáltalán felvétel? Ha ugyanaz a pedagógiai cél felvétel nélkül is teljesül, az legyen az alapút.

**Projektgazdai döntés (2026-10-02), HUM-PRIV-02** – utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős. Alapértelmezés: **nincs fotó, videó vagy hangfelvétel**, csak indokolt célból. Minden médiaaktivitásnál rögzíteni kell: cél, jogalap, hozzáférés, megőrzés, törlés. A kézírásos plakátot lehetőleg **fizikailag** őrizzük meg. Ha fotó kell: előbb a nevek és azonosítók eltávolítása, a háttérben ne legyen gyerek, feltöltés ellenőrzött tárhelyre, majd törlés a saját eszközről. Tanulói szelfi vagy videó **opcionális**, kivéve, ha szakmailag ténylegesen nélkülözhetetlen.

Minimum:
- személyes telefon/felhő nem alapértelmezett tároló;
- azonosítható kiskorú, felhasználónév, kézírás vagy más beazonosító tartalom ne kerüljön tovább csak azért, mert „dokumentálni jó”;
- legyen felvétel nélküli alternatíva, ha a felvétel nem nélkülözhetetlen;
- a learner-facing instrukció mondja meg, **mit készítünk, ki látja, és mi történik vele utána**, amikor felvétel valóban része a feladatnak.

A jogalap külön, önkéntes hozzájárulás; a megőrzés a cél teljesüléséig, legfeljebb 90 nap, hacsak nincs külön archiválási hozzájárulás (§3; **HUM-PRIV-02**). A hozzájárulást 18 év alatt a résztvevő és a gondviselő együtt adja, 18 év felett a résztvevő; ez a tanuló saját videójára is vonatkozik (projektgazdai döntés, 2026-10-02; utólagos ellenőrzés (vétó/QA): a DPO; §4). A gondviselői hozzájárulás folyamata is a **HUM-PRIV-02**-höz tartozik.

## 7. Külső generatív AI

A szolgáltatót és a megvalósítást a **HUM-PRIV-04** projektgazdai döntése rögzíti (lent).

**Projektgazdai döntés (2026-10-02), HUM-PRIV-04** – utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős és a programvezető. Az AI használata **mindig opcionális**, a feladat nélküle is teljesíthető. A kurzus kiskorútól **nem kér saját külső AI-fiókot**.

- **Megvalósítás (V1):** `Moodle → a Somer szerveroldali végpontja → OpenAI Responses API`. A madrih **nem** regisztrál szolgáltatói fiókot; a promptot a képző vagy a szervezeti backend küldi. `/v1/responses`, `store=false`, nincs Conversations API, nincs tartós fájlfeltöltés; nincs személyes adat, nincs valódi hanih-eset, nincs gyermekvédelmi történet. Ha a szervezet számára elérhető, a **ZDR (zero data retention)** be van kapcsolva. A szolgáltató jelenlegi dokumentációja szerint az API-adatokat alapból nem használja modelltanításra.
- **AI Act:** a kurzus **alkalmazó (deployer)** szerepben jár el: külső rendszert használ, nem fejleszt és nem hoz forgalomba saját modellt. A kezelők (képzők) AI-jártassági felkészítést kapnak (AI Act 4. cikk).
- **AI-jártassági blokk:** az M7-ben, az M7.2 elején, kb. **15 perc** (az AI már az M7.1 mini AI-blokkjában is megjelenik; az elé kerülő háromsoros „Mielőtt használod” doboz erre a blokkra mutat – projektgazdai döntés, 2026-10-02): mi az AI, mire jó és mire nem; hallucináció; adatvédelem; emberi ellenőrzés; a promptba nem írható adatok (a lenti lista). A no-AI út teljes értékű marad; az AI továbbra is opcionális.

Nem alku tárgya:
- AI használata a madrihnak **opcionális**;
- legyen teljes értékű no-AI út;
- hanih neve, képe, elérhetősége, pontos helye, egészségügyi/mentális állapota, családi háttere, vallási/etnikai vagy más érzékeny identitása és beazonosítható eseménye **nem kerülhet promptba**;
- valós gyermekvédelmi döntést, veszélyértékelést vagy kríziskezelést nem delegálunk AI-nak;
- a szervezet dokumentálja a szolgáltató aktuális korhatárát, guardian-feltételeit, adatkezelési/training beállításait, admin kontrolljait, szerződéses/adatfeldolgozói helyzetét és a jóváhagyás dátumát.

A promptba nem kerülhető adatok fenti felsorolása az **egyetlen kanonikus lista**: más dokumentum (köztük az `Emberi jóváhagyás szükséges.md` HUM-PRIV-04 tétele) csak hivatkozik rá, nem másolja. Ahol tanulói felületen a lista már szó szerint szerepel, ott maradhat, de csak ezzel egyező szöveggel. Az M7.2 elején álló AI-jártassági blokk is csak ezzel egyező szöveggel idézheti.

**Tanulói szöveg** (a korábbi „saját fiók csak akkor, ha a szolgáltató életkori és gondviselői feltételei teljesülnek” fordulat helyett): „Saját AI-fiókra nincs szükség: a kurzus AI-segédjét a Somer szervere közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj.” Abszolút adatmegőrzési ígéretet a tananyag nem tesz; az általános „jóváhagyott AI-eszköz” megfogalmazás maradhat.

## 8. Z.4 visszajelzés

A core Moodle Feedback `Record user names` = `Anonymous` beállítása esetén a válaszok név nélkül jelenhetnek meg, de a Moodle dokumentációja külön figyelmeztet arra, hogy ez **nem azonos a GDPR-értelemben vett teljes anonimitással**. A név ilyenkor nem jelenik meg a felületen, de a felhasználó azonosítója az adatbázisban marad, és a completion követhető (Moodle Docs, Feedback FAQ).

**Projektgazdai döntés (2026-10-02), HUM-PRIV-03** – utólagos ellenőrzés (vétó/QA): a DPO és a programvezető. A Z.4 képzési visszajelzés maradhat **kötelező**, de **nem nevezhető anonimnak**. A nyers válaszok 90 napig maradnak meg, utána csak összesítve (§3). Ezért:
- Learner-facing szövegben a visszajelzést nem nevezzük anonimnak, és nem ígérünk „teljes anonimitást”.
- A kanonikus tanulói mondat: **„A válaszok név nélkül jelennek meg a feldolgozásban.”**
- Valódi anonimitáshoz a visszajelzést le kellene választani a fiókhoz kötött completionről. Ha a szervezet később erősebb technikai anonimitást akar, azt a HUM-PRIV-03 újranyitásával kell eldönteni és runtime-ban bizonyítani.

## 9. Release acceptance

- [x] HUM-PRIV-01–04 lezárva; **projektgazdai döntés: 2026-10-02** – az `Emberi jóváhagyás szükséges.md` mind a négy tételt dátummal, jóváhagyóval és bizonyítékkal zárta; a későbbi ellenőrzés vétó/QA (§1);
- [x] az activity-szintű adatleltár build-része elkészült (§3, „Activity-szintű adatleltár – build-rész”): címzettek, Moodle-szerepkör/capability és a mentor-láthatóság mechanizmusa profilonként, az `LMS – activity manifest.md` §2 „Profil” oszlopával activityre bontva; **repo-spec: 2026-10-05** (PR-01; BIZT-2 objektív része, BIZT-3, BIZT-4, BIZT-11);
- [ ] az activity-szintű adatleltár többi mezője (adatmező, cél, a jogalap- és a megőrzési sor hozzárendelése, törlés, export/hozzáférési kérelem, harmadik fél, kiskorú-specifikus szabály) kitöltve, a nem Moodle-ben vezetett mentori jegyzettel és a Google-sablonokkal együtt (§3: az LMS-gazda és a privacy felelős; vétó: DPO); <!-- gate: release-evidence -->
- [x] learner-facing adatvédelmi tájékoztató rövid, magyar és érthető: a szövege a §11-ben; **repo-spec: 2026-10-05** (PR-02);
- [ ] a tájékoztató belső mezői kitöltve, és az értékük a §11 szerint a tanulói szövegbe került (`PRIVACY_CONTACT_TO_CONFIGURE`: az adatvédelmi kontakt; `DPO_RETENTION_TO_CONFIRM`: az LMS-Z-06 megőrzése, BS-D6); a jelölő sem a tanulói szövegben, sem a renderelt tanulói tartalomban nem jelenik meg; <!-- gate: release-evidence -->
- [ ] mentor/képző hozzáférések tesztfiókkal ellenőrizve; <!-- gate: post-build -->
- [ ] megőrzés/törlés folyamata és felelőse dokumentálva és tesztelve; <!-- gate: release-evidence -->
- [ ] no-AI út ténylegesen végigvihető; <!-- gate: post-build -->
- [x] érzékeny saját történet nem kötelező teljesítési elem; **repo-audit: 2026-09-29** – az érintett reflektív/safety feladatok fiktív vagy általánosított alternatívát engednek;
- [ ] fotó/videó/hang folyamat HUM-PRIV-02 szerint lezárva; <!-- gate: release-evidence -->
- [x] Z.4 nem ígér bizonyítatlan anonimitást; **repo-audit: 2026-09-29** – a learner-facing ígéret „név nélkül jelenik meg”, a dokumentum explicit kizárja a GDPR-értelemben vett teljes anonimitás ígéretét;
- [ ] privacy/DPO/jogi signoff bizonyítéka rögzítve. <!-- gate: human-qa -->

## 10. Elsődleges források

- GDPR, különösen **5., 6., 8., 9., 13–15., 28. és 32. cikk**, EUR-Lex.
- Moodle aktuális privacy/completion/Feedback dokumentáció.
- A választott külső szolgáltatók aktuális hivatalos feltételei és adatvédelmi dokumentációja (V1: az OpenAI API adatkezelési és ZDR-dokumentációja).
- Az EU AI Act, azaz az (EU) 2024/1689 rendelet aktuális, egységes szerkezetű szövege, EUR-Lex – az alkalmazói (deployer) szerephez és a 4. cikk szerinti AI-jártassághoz.

## 11. A kurzus adatvédelmi tájékoztatója (tanulói szöveg)

*Fejlesztői feltétel (nem tanulói szöveg):*
- A tájékoztató a kurzus elején, Moodle-oldalként (PAGE-C) áll (`LMS – activity manifest.md` §2, „Kurzusszintű elemek”).
- Tartalma a §3–§8 lezárt döntéseiből és a `Program terv.md` §7 sablonjából származik (HUM-PRIV-01–04).
- A „Ki látja?” rész a §5 lezárt szabályát közli. Hogy a tényleges beállítás ezzel egyezik-e, azt a runtime acceptance 15. pontja olvassa vissza; a szerkesztő tanári, a menedzseri és a rendszergazdai hozzáférés (BIZT-2) és a nem TEXT-C profilok szűkítése (BIZT-5) DPO-kérdés. A tájékoztató a §1 release-szabálya szerint a DPO jóváhagyása előtt nem élesíthető.

**Belső mezők, a közzététel előtt kitöltendők.** A jelölők csak ebben a táblázatban és a §9 bizonyíték-tételében szerepelhetnek. A tanulói szövegbe és a renderelt tanulói tartalomba soha nem a jelölő kerül, hanem a kitöltött érték.

| Mező | Mi kerül a tanulói szövegbe | Hová | Állapot |
|---|---|---|---|
| `PRIVACY_CONTACT_TO_CONFIGURE` | az adatvédelmi kontakt tényleges elérhetősége, külön sorban | a „Kihez fordulhatsz?” bekezdés alá | nyitott: a HUM-PRIV-01 szerint jóváhagyott kontakt (`Program terv.md` §4) |
| `DPO_RETENTION_TO_CONFIRM` | egy új sor a „Meddig őrizzük meg?” listába: „a Z.3 szöveges válaszaidat:” és utána a DPO által rögzített megőrzés | a „szöveges reflexióidat” sor után | nyitott: BS-D6, LMS-Z-06 (§3) |

> **Adatvédelem a kurzusban – röviden**
>
> **Mit rögzítünk?** A Moodle-fiókodat, a részvételedet és azt, hogy mit teljesítettél; a kvízek és a kapuk eredményét; és azt, amit egy beadandóba vagy egy szöveges mezőbe beírsz vagy feltöltesz. A szöveges mezőkbe írt válaszaid a neveddel együtt rögzülnek, hogy a mentorod szükség esetén neked szóló visszajelzést adhasson. Felesleges személyes adatot nem kérünk, és ahol egy feladat személyes példát kér, írhatsz fiktív vagy általánosított példát is, ha nem maga a személyes adat a feladat tárgya. Érzékeny családi vagy identitással kapcsolatos történetet egyik feladat sem kér kötelezően. Politikai, vallási, egészségügyi vagy más különleges adatot és valós gyermekvédelmi esetet egyik tanulási feladatba se írj be: ilyen adatot normál tanulási feladatban nem gyűjtünk. Ha egy feltárásban mégis megjelenik ilyen adat, kikerül a Moodle-ből, és a külön, hozzáférés-korlátozott gyermekvédelmi incidensfolyamatba kerül. Ha egy valós gyermekvédelmi helyzetet jelezned kell, azt ne egy tanulási feladatban tedd: azonnal vond be a kijelölt Memunát (a Somer gyermekvédelmi felelősét); az elérhetőségét a kurzus „Segítség és kapcsolatok” blokkjában találod.
>
> **Miért?** Hogy lásd a saját haladásodat a teljesítési kapukon, és hogy a kijelölt mentorod vagy értékelőd – ahol ez ténylegesen szükséges – visszajelzést tudjon adni. A program fejlesztéséhez csak összesített, beazonosíthatatlan adatot használunk. Egyedi szöveget más célra csak névtelenítve és a külön, visszavonható hozzájárulásoddal használunk; ha nem járulsz hozzá, az semmiben nem korlátoz a kurzusban.
>
> **Ki látja?** A kvízek és a kapuk eredményét az értékelőd látja. A szöveges válaszaidat és a beadandóidat a kijelölt mentorod vagy értékelőd látja. A beadandóidat és a Z.3 lecke kötelező szöveges válaszait a teljesítésed megerősítéséhez elolvassa; a többi szöveges válaszodat csak akkor nézi meg, ha ténylegesen szükséges. A kurzusfórumra írt hozzászólásodat a kurzus résztvevői látják. A szöveges válaszaidat a többi résztvevő nem látja.
>
> **Meddig őrizzük meg?**
> - a fiókodat, a részvételedet és a végső teljesítésedet: a képzés vége után 24 hónapig;
> - a kvízpróbálkozásaid részleteit: a végső eredményed megerősítése után 90 napig;
> - a végső pontszámodat és a kapueredményedet: 24 hónapig;
> - a szöveges reflexióidat (a záró reflexiót is): a képzés vége után 90 napig;
> - a beadandóidat és a peulaterveidet: a képzés vége után 12 hónapig;
> - a mentorod fejlesztési és terepi megfigyelési jegyzetét (akkor is, ha nem a Moodle-ben készül; csak a fejlődésed támogatásához szükséges minimum kerül bele): az utolsó mentorálás után 6 hónapig;
> - a mentori beszélgetéseitek naplóját (csak a dátum, a résztvevők, az időtartam, a cél kategóriája és az utánkövetés, a beszélgetés tartalma nem): az utolsó mentorálás után 6 hónapig;
> - a peulákon név nélkül, papíron begyűjtött munkalapokat: összesítés után 30 napon belül megsemmisítjük;
> - a „Képzési visszajelzés – név nélkül” kérdőív (Z.4) válaszait: 90 napig, utána csak összesítve.
>
> A megőrzési idő lejárta után az adatot töröljük vagy anonimizáljuk.
>
> **Fotó, videó, hang.** Alapból nem készül felvétel. Saját fotó vagy videó csak akkor kötelező, ha a feladathoz szakmailag elengedhetetlen; egyébként felvétel nélkül is teljesítheted a feladatot. Felvétel csak külön, önkéntes hozzájárulással készül, és a cél teljesüléséig, legfeljebb 90 napig őrizzük meg, hacsak nincs külön hozzájárulás a hosszabb megőrzéshez. Mindkét hozzájárulást 18 év alatt te és a gondviselőd együtt adjátok meg, 18 év felett te magad.
>
> **AI-segéd.** Az AI használata mindig opcionális: minden feladat nélküle is teljesíthető. Saját AI-fiókra nincs szükség: a kurzus AI-segédjét a Somer szervere közvetíti, szervezeti hozzáféréssel. Személyes adatot ide se írj.
>
> **„Képzési visszajelzés – név nélkül” (Z.4).** A válaszok név nélkül jelennek meg a feldolgozásban.
>
> **Kihez fordulhatsz?** Ha kérdésed vagy kérésed van az adataiddal kapcsolatban, az adatvédelmi kapcsolattartónkhoz fordulhatsz; az elérhetősége ez alatt áll.

Ez a dokumentum adatvédelmi követelményrendszer, nem egyedi jogi tanács és nem helyettesíti a tényleges adatkezelő jogi/DPO döntését.
