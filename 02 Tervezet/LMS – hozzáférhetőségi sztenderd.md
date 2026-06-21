# LMS – hozzáférhetőségi sztenderd

> Fejlesztői sztenderd a Moodle/H5P online leckékhez és peulákhoz.
> Mobil-first célközönség (madrichok, telefonon, gyakran tömegközlekedésen, gyenge neten, hang nélkül tanulnak).
> Ez a fájl az audit F-szekciójának (Hozzáférhetőség / LMS) findingjaiból összegzett, kötelező minimum. Ha eltérsz tőle, indokold a lecke fejlesztői megjegyzésében.

---

## 1. Feliratozás és hangzó tartalom

- **Minden narrált videóhoz és hangsávhoz** tartozzon felirat, VAGY a slide-on / slide-jegyzetben elérhető **teljes szöveges átirat**. (A H5P Course Presentation támogat slide-jegyzetet — használd erre.)
- A narráció **soha ne hordozzon kizárólag hangban elérhető információt**. Ha a hang önálló infót vagy hangulati keretet közöl, annak olvashatóan is meg kell jelennie a dián vagy a jegyzetben.
- Ez az **opcionális** narrációra is vonatkozik: ha a narráció bekapcsolható, a tartalma akkor is legyen szövegesen elérhető.
- Az **Interactive Video** minden jelenete legyen feliratozva.
- A videó-megnevezésnél írd ki explicit a `felirattal` kitételt (pl. „AI beszélő fej videó, 16:9, **felirattal**"), hogy a feliratozás minden videós leckében konzisztens legyen.
- Mobil-first környezetben a felirat **nem extra, hanem alap** — siket/nagyothalló és néma-lejátszású (tömegközlekedés, mobil) felhasználók miatt.

**Sablon-emlékeztető fejlesztőnek:** *minden narráció = felirat + a kulcsüzenet a slide-on is olvasható.*

## 2. Képek és vizuális elemek

- **Alt-szöveg minden beágyazott elemhez**: screenshot, ikon, grafika, illusztráció.
- A screenshotokra épülő leckéknél (pl. kurzus-főoldal képernyőképe) az alt-szöveg vagy egy szöveges megfeleltetés kötelező — különben képernyőolvasóval és gyenge kontrasztnál hozzáférhetőségi rés keletkezik.

## 3. Interakció-típusok (billentyűzet-barátság)

- **Drag & Drop helyett (vagy mellett) adj billentyűzet-barát alternatívát**: H5P **Matching**, **Drag the Words** vagy **Single Choice**.
- A **Drag & Drop kerülendő** ennél a mobil-first célközönségnél: kis képernyőn és motoros nehézséggel élőknél nehezebben kezelhető, mint a Matching.
- A párosító/állítás-párosító feladatok alapértelmezésben **Matching** típusúak legyenek (ujj-barát). Ha valahol mégis Drag & Drop kell, azt a lecke fejlesztői megjegyzésében indokolni kell.
- Az interakció-típus legyen **következetes a modulon belül** — ne fordulhasson elő, hogy az egyik slide tudatosan kerüli a Drag & Drop-ot, a másik mégis előírja.

> **Phase-0 univerzális a11y-protokoll (minden H5P-re, nem csak a kapusakra):**
> - **Minden H5P elé heading az aktivitás nevével** — hogy a madrich (és a képernyőolvasó) tudja, melyik feladatba érkezik, mielőtt beletenyerel.
> - **Rövid task description** közvetlenül a heading alatt: 1–2 mondat arról, mi a dolga és mikor „kész" — ne kelljen a feladatból visszafejtenie, mit várunk tőle.
> - **A meglévő AI-videókhoz magyar felirat + leirat kötelező** — visszamenőleg is: ahol már van beágyazott AI beszélő fej / narrált videó, oda magyar feliratot és teljes szöveges leiratot kell pótolni (hang nélkül, tömegközlekedésen is teljesíthető legyen).

## 4. Mobil-first táblázatok és produktumok

- Több oszlopos táblázatot **ne vízszintes görgetésű táblaként** jeleníts meg mobilon (apró cellák, horizontális scroll → ellentmond a „nincs zsúfolt táblázat" elvnek).
- Helyette **kártya / akkordeon nézet**: egy sor = egy blokk, a mezők **egymás alatt** (pl. egy helyzet = egy kártya a 4 mezővel függőlegesen).
- Produktum-beadásnál (Assignment):
  - adj **letölthető sablont** (doc / sheet), hogy a madrichnak ne kelljen mobilon táblázatot építenie a feltöltéshez;
  - **engedélyezd az online-text beadást** is (Online text ON) a fájlfeltöltés mellett.
- Cél: csökkenteni a több lépcsős, súrlódásos beadási folyamatot, ami a leadási arányt (LA-metrika) rontja.

## 5. H5P Essay és önreflexiók

- Önreflexióknál a H5P **Essay** content type (vagy Moodle szöveges mező) **completion-alapú** beállítással kerüljön be: **kulcsszó-pontozás kikapcsolva**.
- Így nem keletkezik téves pontszám ott, ahol a cél a „megcsinálta / nem csinálta meg" completion, nem az értékelés.
- Megnevezésnél ne használd a „Short Answer" megfogalmazást önálló H5P típusként — a hivatalos content type neve **Essay**. (A félreérthető „Essay / Short Answer" megnevezés helyett írd egyértelműen, melyik kerül be.)

### KAPUS H5P „pre-flight" checklist

> Ez a blokk **kizárólag a kapus / értékelt (gate-höz, completionhöz vagy mastery-kapuhoz kötött) H5P-elemekre** vonatkozik — ahol a továbblépés a madrich teljesítésén múlik. Itt a hozzáférhetőség nem „jó, ha van", hanem **élesítési feltétel**: ha bármelyik pont kipipálatlan, az elem **nem mehet élesbe**, mert egy chanich vagy madrich emiatt elakadhat a kapuban.
>
> **„Kész = élesíthető" definíció:** az elem akkor élesíthető, ha **mind a 7 pont** ki van pipálva ÉS az a11y-lektor jóváhagyta. Részleges teljesítés nem „majdnem kész" — kapus elemnél a hozzáférhetőségi rés egyenlő azzal, hogy valaki kizáródik a továbbhaladásból.

- [ ] **Target size ≥ 24px** — minden kattintható/koppintható elem (válaszgomb, hotspot, drop-zóna) elég nagy ujj-barát célfelület mobilon.
- [ ] **Billentyűzet-teljesíthetőség** — az elem **végigvihető és befejezhető kizárólag billentyűzettel** (Tab-rend logikus, fókusz látható, egér/érintés nélkül is teljesíthető).
- [ ] **Drag-free egypontos alternatíva** — ha az elem húzásra épül, van **drag nélkül is teljesíthető** út (Matching / Single Choice / koppintásos párosítás), hogy a motoros nehézséggel élő vagy apró kijelzőn dolgozó madrich is átjusson a kapun.
- [ ] **Alt-szöveg / szöveges ekvivalens** — minden képnek, ikonnak, hotspotnak, screenshotnak van alt-szövege vagy szöveges megfeleltetése; a feladat **nem oldható meg kizárólag vizuális infóból**.
- [ ] **Kontraszt ≥ 4,5:1** — szöveg és lényeges UI-elem kontrasztja eléri a 4,5:1 küszöböt (apró szövegnél is), gyenge fényben / olcsó kijelzőn is olvasható.
- [ ] **Magyar nyelv + iframe-title** — az elem nyelve magyarra állítva, az iframe-nek **beszédes magyar címe** van (képernyőolvasó felolvassa, melyik aktivitásban jár a madrich).
- [ ] **Felirat + leirat a videókhoz** — minden beágyazott (AI beszélő fej / Interactive / narrált) videóhoz **magyar felirat ÉS teljes szöveges leirat** (slide-jegyzetben vagy a dián), hang nélkül is teljesíthető.

⟬KITÖLTENDŐ: a11y-lektor — ki a felelős a kapus elemek pre-flight jóváhagyásáért (név / szerep)⟭

---

## Gyors checklist fejlesztőnek

- [ ] Minden narrált videó/hangsáv → felirat VAGY teljes szöveges átirat a slide-on/jegyzetben
- [ ] Narráció nem hordoz kizárólag hangban elérhető infót
- [ ] Interactive Video jelenetei feliratozva
- [ ] Alt-szöveg minden screenshothoz/ikonhoz/grafikához
- [ ] Drag & Drop helyett/mellett billentyűzet-barát alternatíva (Matching / Single Choice)
- [ ] Interakció-típus következetes a modulon belül
- [ ] Mobil-táblázat = kártya/akkordeon nézet, nem vízszintes scroll
- [ ] Produktumhoz letölthető sablon + online-text beadás engedélyezve
- [ ] H5P Essay completion-alapú, kulcsszó-pontozás kikapcsolva

---

## Hivatkozások

- H5P content type ajánlások: https://help.h5p.com/hc/en-us/articles/7505649072797-Content-types-recommendations
- H5P content types: https://h5p.org/content-types-and-applications
- H5P Essay: https://h5p.org/essay
- H5P Interactive Video: https://h5p.org/interactive-video
- Moodle activity completion: https://moodle.com/news/track-learners-progress-using-activity-completion-moodle/
