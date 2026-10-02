# LMS – H5P runtime acceptance

A Markdown specifikációból **nem bizonyítható**, hogy egy H5P/Moodle interakció a tényleges telepítésen működik. Release előtt a célkörnyezetet verzióval rögzíteni és tesztelni kell.

## Environment record

| Komponens | Verzió / build | Dátum | Felelős |
|---|---|---|---|
| Moodle | `RUNTIME_OUTPUT` | `RUN_DATE` | `TEST_OWNER` |
| H5P core / plugin | `RUNTIME_OUTPUT` | `RUN_DATE` | `TEST_OWNER` |
| Course Presentation | `RUNTIME_OUTPUT` | | |
| Branching Scenario | `RUNTIME_OUTPUT` | | |
| Dialog Cards | `RUNTIME_OUTPUT` | | |
| Column | `RUNTIME_OUTPUT` | | |
| Question Set | `RUNTIME_OUTPUT` | | |
| Free Text Question | `RUNTIME_OUTPUT` | | |
| Interactive Video | `RUNTIME_OUTPUT` | | |
| Single Choice Set | `RUNTIME_OUTPUT` | | |
| Multiple Choice | `RUNTIME_OUTPUT` | | |
| True/False Question | `RUNTIME_OUTPUT` | | |
| Fill in the Blanks | `RUNTIME_OUTPUT` | | |
| Drag and Drop | `RUNTIME_OUTPUT` | | |
| Mark the Words | `RUNTIME_OUTPUT` | | |
| Audio / Video (beágyazott elem) | `RUNTIME_OUTPUT` | | |
| Browser/device matrix | `RUNTIME_OUTPUT` | | |

## P0 runtime tesztek

Minden tétel `IMPLEMENTATION_TEST_REQUIRED` állapotból indul; `RUNTIME_VERIFIED` állapotba csak dátummal és pontos verzióval rögzített, tényleges teszteredmény mozdíthatja (`RELEASE-READINESS.md`, staging-szabály 5. pont).

1. **Teljesítési szemantika:** a megnyitás vagy egy próbálkozás önmagában nem számíthat a teljesítési kapu teljesítésének; a jóváhagyott `grade/pass` feltételnek ténylegesen blokkolnia kell.
   - **Puha kapuk:** ott, ahol a Program terv §5 érdemi tartalmat ír elő – az M2 identitás-jegyzetnél és az M4 peulabemutató-vázlatnál –, a completion üres beküldésre sem állhat be (az M4-nél a „még nem éri el” szintű vázlat sem számít leadottnak, M4 hub §6).
   - **Mastery-kvíz (QUIZ-M):** a completion nem teljesülhet pusztán azzal, hogy a próbálkozások elfogytak (Moodle: „Passing grade or all available attempts completed”).
   - **Beállítások visszaolvasása:** ahol a kapufájl ponthatárt ad (M1, M3 kapukvíz, M7), a beállított Maximum grade és Grade to pass ennek felel meg; a rubrikapontok Moodle-pontszámra vetítését a célverzión kell ellenőrizni.
2. **M6.4 Branching Scenario:** legalább három külön ág teljesítése ténylegesen mérhető vagy Moodle-checkpointtal helyettesített.
3. **Z.4 hosszú reflexió:** Moodle Assignment draft mentés, újranyitás (a „Hiányos” visszajelzés utáni kiegészítéshez is), visszatérés és véglegesítés ténylegesen működik. Nem támaszkodunk H5P Documentation Tool session-resume állításra.
4. **M5 Dialog Cards:** a célverzión a kártyák mobilon, billentyűzettel és nagyított nézetben használhatók; esetleges „repetition” funkciót nem kommunikálunk bizonyított, többnapos spaced-repetition rendszerként külön teszt nélkül. Az M5.3 késleltetett felidézési pontjánál a Moodle-időzítő, a késleltetés, az értesítés és a completion működését külön kell tesztelni (M5.3 fejlesztői jegyzete).
5. **Moodle 5.x / Branching Scenario:** külön regressziós teszt, mert 2026-ban Moodle 5.1.1 környezetben dokumentált Branching Scenario megjelenítési hiba jelent meg a H5P communityben.
6. **Szabad szöveges mező megvalósítása:** a leckékben „rövid szöveges válasz” / „hosszabb szöveges reflexió” néven leírt mezők pedagógiai igényt jelölnek, nem automatikusan egyetlen H5P-típust. A H5P jelenlegi nyílt forrású kínálatában **létezik Free Text Question**, de ez pontozás nélküli, xAPI/LRS-függő interakció, és nem következik a puszta létezéséből, hogy a cél Moodle/H5P telepítésen vagy a kívánt befoglalóban használható. A célverzión külön tesztelendő út: **(a)** Moodle-oldali szövegmező, **(b)** H5P Free Text Question ott, ahol a host és a befoglaló igazoltan támogatja, **(c)** H5P Essay igazoltan támogató befoglalóban, például Interactive Bookban, vagy **(d)** Fill in the Blanks, ha a válasz valóban kötött. Az **Essay Course Presentationbe ágyazását továbbra sem feltételezzük**. Ha egy lecke a Course Presentationbe ágyazott Interactive Video Free Text Question elemére épít, külön tesztelni kell, hogy az erre adott válasz beszámít-e az activity-completionbe.
7. **Resume / state:** minden olyan learner-facing mondat, hogy „később folytathatod”, csak igazolt state persistence után maradhat. Ugyanez vonatkozik arra az ígéretre is, hogy a tanuló egy korábbi mezőbe írt saját szövegét később újra eléri vagy továbbviszi (pl. az M1.3 saját SBI-mondata); erre is külön teszteset kell.
8. **Összetett (konjunkciós) kapuk kikényszerítése:** az alábbi kapufeltételek (Program terv §5 küszöb-táblája, a kapufájlok és a manifest §2 *Mastery / pass* oszlopa) egyike sem egyetlen skalár pontszám, és skalár küszöbbel **nem is kódolható**; mindegyiket a megadott negatív esettel is tesztelni kell, amely mellett a következő tartalom **nem** nyílhat meg:
   - **M1** – minden rubrikasor ≥1 **ÉS** összpont ≥5/8 (a nyers „Grade to pass = 5” a 0/1/2/2 esetet átengedné);
   - **M3, kapukvíz** – összpont ≥10/12 **ÉS** a 2., 4., 7., 9. item mind helyes (súlyozott pontozás nem ekvivalens: két ellentétes eredményű eset ugyanazt a pontszámot adja; negatív eset: 11/12, hibás 7. item);
   - **M3, B komponens (helyzetleírás)** – minden rubrikasor ≥1, az **R2 és az R4 blokkoló** (negatív esetek: 2/0/2/0 = 4/8 és 0/2/2/2 = 6/8; mindkettő pontszáma a kapufájl „átmenő pontsávjának” 4–8 pontos tartományába esik);
   - **M5** – az M5.4 táblázat minden rubrikasora ≥ „Alapszint”, az **R4 kritikus** (negatív eset: R4 „Hiányos”, a többi sor „Erős”);
   - **M6** – minden rubrikasor ≥2, az **R4 és az R5 blokkoló** (negatív eset: R1–R3 = 3, R4 = R5 = 1, összesen 11/15);
   - **M7, Peula v2** – összpont ≥17/24 **ÉS** R1, R5, R6 ≥2 **ÉS** R4 ≥2 (negatív eset: 18/24, R4 = 1);
   - **M7, záró kvíz** – ≥12/14 **ÉS** a Q13 helyes (negatív eset: 13/14, hibás Q13).
   Tesztelni kell, hogy a célkörnyezet a konjunkciót ténylegesen kikényszeríti-e. **Ha nem, az nem a feltétel gyengítését jelenti**, hanem azt, hogy a továbblépést a **megerősített kapu-eredményhez** (kézi/mentori ellenőrzés utáni „megfelelt”, a manifest §4 szerinti `GATE_CONFIRMED_<module>` checkpoint) kell kötni, nem a nyers grade/pass állapothoz. Ilyenkor azt is igazolni kell, hogy a checkpoint a Moodle felületén kézzel beállítható (tanulónkénti grade vagy completion MCP-vel nem írható, manifest §5), és hogy a downstream restrict access ténylegesen ehhez kötődik. A választott mechanizmust verzióval és bizonyítékkal rögzíteni kell. A kvízes kapukat (M3, M7) bekapcsolt kérdés- és opciókeveréssel is tesztelni kell: a kézi ellenőrzésnek a kritikus itemeket a kérdés saját neve vagy címkéje alapján kell megtalálnia, mert keverésnél a próbálkozásban megjelenő sorszám eltérhet a kapufájl szerinti itemsorszámtól.
9. **H5P-C completion:** a manifest H5P-C profilja szerint a completion a forrásban előírt interakció(k) érdemi befejezése. Tesztelni kell, hogy a választott Moodle-beállítással a puszta megnyitás vagy végiglapozás nem teljesít ott, ahol a lecke választ kér.
10. **M2.3 Branching Scenario:** tesztelni kell, hogy az M2 hub §6 szerinti completion (legalább 1 pillér-ág végigjátszva **és** a záró „így mutatok példát” mondat beírva) a választott megvalósításban ténylegesen mérhető-e. Ha a Branching Scenario pontozás nélküli („No scoring”) módban fut, külön igazolni kell, hogy az eredmény egyáltalán eljut-e a Moodle-hoz. A billentyűzetes és képernyőolvasós navigációt a pillér-választóhoz való visszatéréssel együtt kell tesztelni.
11. **M3.3 gyermekvédelmi szcenáriók:** a Course Presentation beágyazható típusai között nincs Branching Scenario (`semantics.json`), ezért a négy szcenárió megépíthető szerkezetét a leckében rögzíteni kell. Tesztelni kell, hogy ebben a szerkezetben a döntésekkel végigvitt út ténylegesen mérhető, és beszámít az M3 hub §6 szerinti completionbe („M3.3 Branching végigvitele döntésekkel”), amely a kapu belépő feltétele.
12. **Kötelező szabad szöveges lépés:** ahol a lecke egy szabad szöveges lépést a továbblépés feltételének ír elő vagy minimális terjedelmet kér (pl. a Z.3 biztonsági lépése), tesztelni kell, hogy a választott megvalósítás ezt ténylegesen kikényszeríti-e, és hogy a lépés beszámít-e a completionbe. Ha nem, a lépés kötelező (nem kihagyható) státusza ettől nem gyengül, csak a technikai kikényszerítésről szóló tanulói állítás pontosítható; a lépés helyéről és completion-kötéséről külön kell dönteni.
13. **Húzásmentes út és párosítás (WCAG 2.2 SC 2.5.7, 2.5.8):** minden húzásra épülő feladatnál (pl. M1.2) a húzásmentes, egyenértékű út egyetlen kattintással vagy koppintással – nem csak billentyűzettel – végigvihető, ugyanazt a visszajelzést és teljesítésjelzést adja, mint a húzásos forma, és aki csak ezt az utat járja, annál is beáll a completion. A koppintásos párosításoknál (a projekt „Matching” címkéje) a ténylegesen választott H5P-típus húzásmentességét a renderen kell igazolni. A célméretet mobil portrait nézetben kell mérni.
14. **Választós elemek visszajelzése és pontozása:** a Single Choice Setben az első alternatíva mindig a helyes válasz, válaszonkénti visszajelző mezője nincs (csak pontsávos összesítő visszajelzés), és alapbeállításban a választás után magától továbblép; ezt a H5P saját leírása szerint képernyőolvasós használathoz ki kell kapcsolni (`semantics.json`). Tesztelni kell, hogy
   - ahol a lecke válaszonkénti vagy kérdésenkénti visszajelzést ír elő (pl. az M0.2 2. helyzetének kiemelt visszajelzése), az a választott típusban ténylegesen megjelenik, képernyőolvasóval is;
   - a visszajelzés elolvasható, mielőtt a feladat továbblép (WCAG 2.2 SC 2.2.1);
   - a helyes válasz nélküli vélemény- és helyzetfelmérő kérdéseknél a választott megoldás egyetlen őszinte választ sem jelöl hibásnak, és nem torzítja a befoglaló elem pontszámát.
15. **Szabad szöveg láthatósága:** tanulói, képzői és mentori tesztfiókkal vissza kell olvasni, hogy az egyes szabad szöveges mezők és beadandók tartalmát ki látja (például a H5P activity próbálkozás-riportjában vagy az Assignment értékelő nézetében). Az eredménynek egyeznie kell a HUM-PRIV-01 szerint jóváhagyott beállítással és azzal, amit a tanulói felület állít (Program terv §4, Adatvédelem §5).
16. **Z.4 Moodle Feedback (LMS-Z-05):** vissza kell olvasni a HUM-PRIV-03 szerinti név nélküli beállítást (Moodle: „Record user names” = „Anonymous”), és képzői tesztfiókkal ellenőrizni, hogy a válaszok név nélkül jelennek meg. Tesztelni kell azt is, hogy a completion a kitöltéssel teljesül, egy fiók egyszer küldhet be (FEEDBACK-N profil: „Allow multiple submissions” = No), a Feedback a Z.A után nyílik, és az űrlap mobilon, billentyűzettel és képernyőolvasóval kitölthető. A teszt teljes anonimitást nem igazol: erősebb technikai anonimitás csak HUM-PRIV-03 döntés és külön runtime-bizonyíték után állítható (Adatvédelem §8).
17. **Learner-facing kontakt megjelenése:** tanulói tesztfiókkal vissza kell olvasni, hogy a `Gyermekvédelem – release gate.md` release-checklistjének kontakt-tétele („a learner-facing kontakt ténylegesen látható a Moodle-ben”) teljesül. A kontakt tartalmát a HUM-SAFE-01 adja; ez a tétel csak a megjelenést igazolja, második igazságforrást nem hoz létre.
18. **M5.2 Branching Scenario:** a 10. pont mintájára tesztelni kell, hogy az M5.2 elágazásai és visszairányításai a választott megvalósításban működnek, és a completion a manifest LMS-M5-02 sora szerint áll be.

## Accessibility acceptance

Minden kritikus content type legalább:

- teljes billentyűzetes út;
- látható fókusz és logikus fókuszsorrend;
- screen-reader ellenőrzés;
- 200–400% zoom/reflow;
- mobil portrait;
- feliratos prerecorded videó;
- a narráció és a videó leirata, valamint a dián gombbal megnyitható szövegelemek billentyűzettel és képernyőolvasóval elérhetők; a videólejátszó nem rejtett a segédtechnológia elől, és leíró azonosítást kap (WCAG 2.2 SC 1.1.1);
- nem csak színre támaszkodó visszajelzés;
- a visszajelzés időkorlát nélkül elolvasható, nincs időzített automatikus továbblépés (WCAG 2.2 SC 2.2.1);
- megfelelő kontraszt és célméret;
- hibás válasz után értelmes, nem csak „rossz” visszajelzés.

## Release evidence

A teszt eredménye legyen issue, táblázat vagy screenshot/log, dátummal és pontos verzióval. „A H5P tudja” nem acceptance evidence.
