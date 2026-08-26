# LMS – H5P runtime acceptance

A Markdown specifikációból **nem bizonyítható**, hogy egy H5P/Moodle interakció a tényleges telepítésen működik. Release előtt a célkörnyezetet verzióval rögzíteni és tesztelni kell.

## Environment record

| Komponens | Verzió / build | Dátum | Felelős |
|---|---|---|---|
| Moodle | KITÖLTENDŐ | KITÖLTENDŐ | KITÖLTENDŐ |
| H5P core / plugin | KITÖLTENDŐ | KITÖLTENDŐ | KITÖLTENDŐ |
| Course Presentation | KITÖLTENDŐ | | |
| Branching Scenario | KITÖLTENDŐ | | |
| Dialog Cards | KITÖLTENDŐ | | |
| Column | KITÖLTENDŐ | | |
| Question Set | KITÖLTENDŐ | | |
| Interactive Video | KITÖLTENDŐ | | |
| Browser/device matrix | KITÖLTENDŐ | | |

## P0 runtime tesztek

1. **Completion semantikája:** megnyitás/attempt nem számíthat mastery teljesítésnek; grade/pass feltétel ténylegesen blokkol.
2. **M6.4 Branching Scenario:** legalább három külön ág teljesítése ténylegesen mérhető vagy Moodle-checkpointtal helyettesített.
3. **Z.4 hosszú reflexió:** Moodle Assignment draft mentés, újranyitás, visszatérés és véglegesítés ténylegesen működik. Nem támaszkodunk H5P Documentation Tool session-resume állításra.
4. **M5 Dialog Cards:** a cél verzión a kártyák mobilon, billentyűzettel és nagyított nézetben használhatók; esetleges „repetition” funkciót nem kommunikálunk bizonyított, többnapos spaced-repetition rendszerként külön teszt nélkül.
5. **Moodle 5.x / Branching Scenario:** külön regressziós teszt, mert 2026-ban Moodle 5.1.1 környezetben dokumentált Branching Scenario megjelenítési hiba jelent meg a H5P communityben.
6. **Szabad szöveges mező megvalósítása:** a leckékben „rövid szöveges válasz” / „hosszabb szöveges reflexió” néven leírt mezők **nem** egy adott H5P content type-ot neveznek meg. A cél verzión el kell dönteni és tesztelni, hogy melyik megengedett út valósul meg: Moodle-oldali szövegmező, H5P **Essay** igazoltan támogató befoglalóban (pl. Interactive Book), vagy **Fill in the Blanks** kötött válasznál. **A H5P hivatalos álláspontja szerint az Essay nem adható Course Presentationhöz**, ezért a „Course Presentation dián belüli szabad szöveg” nem feltételezhető.
7. **Resume / state:** minden olyan learner-facing mondat, hogy „később folytathatod”, csak igazolt state persistence után maradhat.
8. **Összetett (konjunkciós) kapuk kikényszerítése:** két kapu feltétele **nem** egyetlen skalár pontszám, és skalár küszöbbel **nem is kódolható**:
   - **M1** – minden rubrikasor ≥1 **ÉS** összpont ≥5/8 (a nyers „Grade to pass = 5” a 0/1/2/2 esetet átengedné);
   - **M3** – összpont ≥10/12 **ÉS** a 2., 4., 7., 9. item mind helyes (súlyozott pontozás nem ekvivalens: két ellentétes eredményű eset ugyanazt a pontszámot adja).
   Tesztelni kell, hogy a cél-környezet a konjunkciót ténylegesen kikényszeríti-e. **Ha nem, az nem a feltétel gyengítését jelenti**, hanem azt, hogy a továbblépést a **megerősített kapu-eredményhez** (kézi/mentori ellenőrzés utáni „megfelelt”) kell kötni, nem a nyers grade/pass állapothoz. A választott mechanizmust verzióval és bizonyítékkal rögzíteni kell.

## Accessibility acceptance

Minden kritikus content type legalább:

- teljes billentyűzetes út;
- látható fókusz és logikus fókuszsorrend;
- screen-reader ellenőrzés;
- 200–400% zoom/reflow;
- mobil portrait;
- feliratos prerecorded videó;
- nem csak színre támaszkodó feedback;
- megfelelő kontraszt és célméret;
- hibás válasz után értelmes, nem csak „rossz” feedback.

## Release evidence

A teszt eredménye legyen issue, táblázat vagy screenshot/log, dátummal és pontos verzióval. „A H5P tudja” nem acceptance evidence.
