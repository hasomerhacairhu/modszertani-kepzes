# Adatvédelem – tanulói adatok és AI

## 1. Release-szabály

A learner-facing Moodle-kurzust a tényleges adatkezelő szervezet privacy/DPO/jogi felelőse hagyja jóvá. Zárt stagingben csak szintetikus tesztadat használható.

A repository **nem választ jogalapot, megőrzési időt vagy szülői folyamatot a szervezet helyett**. Ezek a döntések az `Emberi jóváhagyás szükséges.md` fájlban, stabil azonosítókkal élnek:

- **HUM-PRIV-01:** Moodle-adatkezelési mátrix;
- **HUM-PRIV-02:** fotó, videó, hang és kézírás;
- **HUM-PRIV-03:** Z.4 visszajelzés anonimitási szintje;
- **HUM-PRIV-04:** külső generatív AI tanulói használata.

Mind a négy tételben **projektgazdai döntés (2026-10-02)** született, a jogalapról és a megőrzési időről is; a tartalmukat a §3, a §5, a §6, a §7 és a §8 rögzíti. A tételek az `Emberi jóváhagyás szükséges.md`-ben lezártak. A DPO/jogi felelős (a HUM-PRIV-03-nál és a HUM-PRIV-04-nél a programvezető is) későbbi ellenőrzése **utólagos ellenőrzés (vétó/QA)**, nem új döntési kapu. A release-szabály és a §9 átvételi listájának nyitott sorai változatlanul érvényesek.

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
| Szabad szöveges reflexió | jogos érdek, kizárólag ha szükséges | a képzés vége + 90 nap |
| Assignment / peulatervek | jogos érdek | a képzés vége + 12 hónap |
| Mentori 1:1 meta-napló | jogos érdek, gyermekvédelmi elszámoltathatóság | az utolsó mentorálás + 6 hónap |
| Z visszajelzés nyers válaszai | jogos érdek | 90 nap, utána csak összesítve |
| Fotó/videó/hang | külön, önkéntes hozzájárulás | a cél teljesüléséig, legfeljebb 90 nap, hacsak nincs külön archiválási hozzájárulás |
| Gyermekvédelmi incidens | külön, korlátozott hozzáférésű rendszer | az érintett 25. születésnapjáig vagy a lezárás + 7 évig (amelyik később jár le); jogi visszatartás esetén tovább |

Politikai, vallási, egészségügyi vagy más különleges adat **normál tanulási activityben nem gyűjthető**. Ha feltáráskor mégis megjelenik, kikerül a Moodle-ből, és az incidensfolyamatba kerül (`Gyermekvédelem – release gate.md` §4.1). A mentori 1:1 meta-naplóba csak dátum, résztvevők, időtartam, célkategória és utánkövetés kerül, a beszélgetés tartalma nem (`Gyermekvédelem – release gate.md` §4.2).

Külön review szükséges legalább:

- M0 „Bemutatkozó fal”: kurzuson belül más résztvevőknek látható;
- M1 SBI-beadandó;
- M2 identitás- és értékreflexiók, identitás-jegyzet, valamint az M2.3 pillér-kérdése (nem lehet fiókhoz kötött szavazás);
- M3 gyermekvédelmi helyzetelemzés: a kapuproduktumba **csak kitalált, életszerű eset** kerülhet, valós eset névtelenítve sem, mert kis közösségben könnyen visszaazonosítható; valós gyermekvédelmi eset soha nem pedagógiai feladat;
- M4 peulabemutató és bármilyen felvételi folyamat;
- M5/M6 produktumok;
- M6 fotó/kézműves dokumentáció, ha egyáltalán szükséges;
- M7 AI-promptok és Peula v1/v2; a Peula v2 valós kvucára is tervezhető, de csak nem azonosító, csoportszintű információval (nevek, egyéni érzékeny történetek, diagnózisok és hasonlók nélkül); saját kvuca hiányában a tanuló kitalált profilt kap;
- a modulhubok és az F-peulák nem Moodle-ben vezetett mentori jegyzete, valamint a Google-sablonok (M5.4, M6);
- Z.2/Z.4 személyes reflexiók és mentor-hozzáférés;
- Z.4 Moodle Feedback.

A lista M2-, M3- és M7-sorának szabálya **projektgazdai döntés (2026-10-02)**; utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős, az M3-sornál a Memuna is, az M7-sornál a programvezető is.

## 4. Kiskorúak és hozzájárulás

A GDPR 8. cikke csak akkor alkalmazandó a saját korhatárszabályával, ha **az adatkezelés a 6. cikk (1) a) szerinti hozzájáruláson alapul, és információs társadalmi szolgáltatást kínálnak közvetlenül gyermeknek**. A GDPR alapesetben 16 éves korhatárt ír elő, és lehetővé teszi, hogy a tagállam ezt 13 éves korig csökkentse.

Ez **nem** jelenti azt, hogy „minden 18 év alatti Moodle-adatkezeléshez szülői hozzájárulás kell”. A képzés minden adatkezelési céljának jogalapját külön kell meghatározni, és azt is külön kell vizsgálni, hogy a GDPR 8. cikke egyáltalán alkalmazandó-e.

A szülői/gondviselői tájékoztatás vagy engedélyezés helyi folyamata ezért **emberi és jogi döntés (HUM-PRIV-01, HUM-SAFE-03)**, nem a tananyag által kitalálható szabály. A jogalapot adattípusonként a §3 mátrixa rögzíti (projektgazdai döntés, 2026-10-02); a gyermekvédelmi helyzetben alkalmazandó gondviselői szabály a `Gyermekvédelem – release gate.md` §4.3-ban áll.

## 5. Mentor- és képzői hozzáférés

A „mentor láthatja, mert hasznos lehet” nem elég indok. Az alábbi alapszabályok a HUM-PRIV-01 **projektgazdai döntését (2026-10-02)** követik; utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős (§3).

- **P0–P1 privacy-osztály** (az `LMS – activity manifest.md` 1. szakasza szerint): csak az a szerepkör lássa, amelynek a completion/értékelés üzemeltetéséhez szüksége van rá; a zárt kvíz pontszámát az értékelő látja.
- **P2 privacy-osztályú beadandó, szabad szöveg, reflexió:** csak a kijelölt értékelő/mentor, csak ha ténylegesen szükséges, és csak a szükséges ideig (a megőrzési idő: §3).
- **kurzusfórum:** a résztvevő előre tudja, hogy a csoport látja.
- **saját önreflexió:** ne legyen mentor-látható, ha nincs rá konkrét pedagógiai szükség.
- **mentori jegyzet** (akkor is, ha nem Moodle-ben készül): csak minimális, a fejlődéstámogatáshoz szükséges adat; „árnyékdosszié” nincs.
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

A jogalap külön, önkéntes hozzájárulás; a megőrzés a cél teljesüléséig, legfeljebb 90 nap, hacsak nincs külön archiválási hozzájárulás (§3; **HUM-PRIV-02**). Az esetleges szülői/gondviselői folyamat is a **HUM-PRIV-02**-höz tartozik.

## 7. Külső generatív AI

A szolgáltatót és a megvalósítást a **HUM-PRIV-04** projektgazdai döntése rögzíti (lent).

**Projektgazdai döntés (2026-10-02), HUM-PRIV-04** – utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős és a programvezető. Az AI használata **mindig opcionális**, a feladat nélküle is teljesíthető. A kurzus kiskorútól **nem kér saját külső AI-fiókot**.

- **Megvalósítás (V1):** `Moodle → a Somer szerveroldali végpontja → OpenAI Responses API`. A madrih **nem** regisztrál szolgáltatói fiókot; a promptot a képző vagy a szervezeti backend küldi. `/v1/responses`, `store=false`, nincs Conversations API, nincs tartós fájlfeltöltés; nincs személyes adat, nincs valódi hanih-eset, nincs gyermekvédelmi történet. Ha a szervezet számára elérhető, a **ZDR (zero data retention)** be van kapcsolva. A szolgáltató jelenlegi dokumentációja szerint az API-adatokat alapból nem használja modelltanításra.
- **AI Act:** a kurzus **alkalmazó (deployer)** szerepben jár el: külső rendszert használ, nem fejleszt és nem hoz forgalomba saját modellt. A kezelők (képzők) AI-jártassági felkészítést kapnak (AI Act 4. cikk).
- **AI-jártassági blokk:** az M7-ben, az M7.2 elején (ahol az AI először megjelenik), kb. **15 perc**: mi az AI, mire jó és mire nem; hallucináció; adatvédelem; emberi ellenőrzés; a promptba nem írható adatok (a lenti lista). A no-AI út teljes értékű marad; az AI továbbra is opcionális.

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
- [ ] teljes activity-szintű adatleltár elkészült (§3), a nem Moodle-ben vezetett mentori jegyzettel és a Google-sablonokkal együtt;
- [ ] learner-facing adatvédelmi tájékoztató rövid, magyar és érthető;
- [ ] mentor/képző hozzáférések tesztfiókkal ellenőrizve;
- [ ] megőrzés/törlés folyamata és felelőse dokumentálva és tesztelve;
- [ ] no-AI út ténylegesen végigvihető;
- [x] érzékeny saját történet nem kötelező teljesítési elem; **repo-audit: 2026-09-29** – az érintett reflektív/safety feladatok fiktív vagy általánosított alternatívát engednek;
- [ ] fotó/videó/hang folyamat HUM-PRIV-02 szerint lezárva;
- [x] Z.4 nem ígér bizonyítatlan anonimitást; **repo-audit: 2026-09-29** – a learner-facing ígéret „név nélkül jelenik meg”, a dokumentum explicit kizárja a GDPR-értelemben vett teljes anonimitás ígéretét;
- [ ] privacy/DPO/jogi signoff bizonyítéka rögzítve.

## 10. Elsődleges források

- GDPR, különösen **5., 6., 8., 9., 13–15., 28. és 32. cikk**, EUR-Lex.
- Moodle aktuális privacy/completion/Feedback dokumentáció.
- A választott külső szolgáltatók aktuális hivatalos feltételei és adatvédelmi dokumentációja (V1: az OpenAI API adatkezelési és ZDR-dokumentációja).
- Az EU AI Act, azaz az (EU) 2024/1689 rendelet aktuális, egységes szerkezetű szövege, EUR-Lex – az alkalmazói (deployer) szerephez és a 4. cikk szerinti AI-jártassághoz.

Ez a dokumentum adatvédelmi követelményrendszer, nem egyedi jogi tanács és nem helyettesíti a tényleges adatkezelő jogi/DPO döntését.
