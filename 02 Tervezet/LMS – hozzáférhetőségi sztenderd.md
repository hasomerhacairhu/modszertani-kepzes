# LMS – hozzáférhetőségi sztenderd

> Fejlesztői sztenderd a Moodle/H5P online leckékhez és peulákhoz.
> Mobil-first célközönség (madrihok, telefonon, gyakran tömegközlekedésen, gyenge neten, hang nélkül tanulnak).
> Ez a fájl az audit F-szekciójának (Hozzáférhetőség / LMS) findingjaiból összegzett, kötelező minimum. Ha eltérsz tőle, indokold a lecke fejlesztői megjegyzésében.

---

## 1. Feliratozás és hangzó tartalom

- **Előre rögzített, szinkronizált videóhoz (kép + hang) FELIRAT kell** — a teljes szöveges leirat **nem helyettesíti** (WCAG 2.2 SC 1.2.2, A szint). A leirat emellett **erősen ajánlott** kiegészítés, és a szinkronizált média szöveges alternatívájaként külön szerepet is betölt (SC 1.2.3).
- **Csak hangot tartalmazó** (videó nélküli) előre rögzített tartalomnál elegendő a teljes szöveges leirat (SC 1.2.1).
- **Hangalámondás / audio description (SC 1.2.5, AA):** ott kell megvizsgálni, ahol a képi sáv olyan információt hordoz, ami a hangban nem hangzik el. Ha a videó minden lényegi információja elhangzik a narrációban, külön hangalámondás nem szükséges. A videókat **egyenként** kell besorolni, és a besorolást videónként rögzíteni; nem a teljes videót nevezzük dekoratívnak. A **beszélő fej képi sávja** lehet dekoratív, ha minden információ benne van a hangban és a leiratban. **Jelenetvideónál**, ahol arckifejezés, gesztus vagy képi történés hordoz jelentést, **hangalámondásos képleírás kell (SC 1.2.5, AA)**, mellette **szöveges alternatíva** is (SC 1.2.3).
- **A leirat helye:** a H5P Course Presentation diáinak nincs külön jegyzetmezője (a `h5p-course-presentation` hivatalos `semantics.json`-ja szerint egy dia mezői: `elements`, `keywords`, `slideBackgroundSelector`), ezért a leirat ne „slide-jegyzetbe” kerüljön, hanem a dián látható szövegként, a médiaelem mellől megnyitható szövegként vagy linkelt leirat-oldalként jelenjen meg. Hogy a választott megoldás a célverzión billentyűzettel és képernyőolvasóval elérhető-e, az `LMS – H5P runtime acceptance.md` szerinti teszten kell igazolni.
- A narráció **soha ne hordozzon kizárólag hangban elérhető információt**. Ha a hang önálló infót vagy hangulati keretet közöl, annak olvashatóan is meg kell jelennie a dián vagy a leiratban.
- Ez az **opcionális** narrációra is vonatkozik: ha a narráció bekapcsolható, a tartalma akkor is legyen szövegesen elérhető.
- Az **Interactive Video** minden jelenete legyen feliratozva; az interaktív pontok szövege is legyen elérhető képernyőolvasóval.
- A videó-megnevezésnél írd ki explicit a `felirattal` kitételt (pl. „AI beszélő fej videó, 16:9, **felirattal**”), hogy a feliratozás minden videós leckében konzisztens legyen.
- Mobil-first környezetben a felirat **nem extra, hanem alap** — siket/nagyothalló és néma-lejátszású (tömegközlekedés, mobil) felhasználók miatt.

**Sablon-emlékeztető fejlesztőnek:** *szinkronizált videó = felirat (kötelező) + leirat (ajánlott) + a kulcsüzenet a slide-on is olvasható.*

## 2. Képek és vizuális elemek

- **Alt-szöveg minden beágyazott elemhez**: képernyőkép, ikon, grafika, illusztráció.
- A képernyőképekre épülő leckéknél (pl. kurzus-főoldal képernyőképe) az alt-szöveg vagy egy szöveges megfeleltetés kötelező — különben képernyőolvasóval és gyenge kontrasztnál hozzáférhetőségi rés keletkezik.

## 3. Interakció-típusok (billentyűzet-barátság)

- **Ha egy feladat húzásra épül, legyen mellette egyenértékű út, amely húzás nélkül is teljesíthető**: egyetlen kattintással/koppintással **és** billentyűzettel (WCAG 2.2 SC 2.5.7 – *Dragging Movements*, AA). A követelmény **funkcionális**: „nem kell hozzá húzni” – **nem** egy adott nevű H5P content type. A **Single Choice Set** (kikapcsolt „Auto continue” beállítással) és a **Multiple Choice** egyválaszos („Single Choice (Radio Buttons)”) módban tipikusan ilyen utat ad; a **Drag the Words** viszont **nem az**, mert maga is húzásra épül – ezért soha ne szerepeljen húzásmentes alternatívaként.
- A **Drag & Drop kerülendő** ennél a mobil-first célközönségnél: kis képernyőn és motoros nehézséggel élőknél nehezebben kezelhető. Ahol párosítás kell, **koppintás-/kattintás-alapú** megoldást válassz.
- A párosító/állítás-párosító feladatok alapértelmezésben **koppintás-alapú párosítást** használjanak (ujj-barát) – a projektben ennek a címkéje **Matching / kattintásos párosítás** (projektcímke, nem H5P content type neve). Hogy az adott H5P típus a célverzión ténylegesen húzás nélkül is teljesíthető-e, **acceptance-teszten kell igazolni** (`LMS – H5P runtime acceptance.md`); a típus nevéből ezt nem szabad következtetni. Ha valahol mégis Drag & Drop kell, azt a lecke fejlesztői megjegyzésében indokolni kell, és **kötelező** mellé a húzásmentes út.
- Az interakció-típus legyen **következetes a modulon belül** — ne fordulhasson elő, hogy az egyik slide tudatosan kerüli a Drag & Drop-ot, a másik mégis előírja.

> **Phase-0 univerzális a11y-protokoll (minden H5P-re, nem csak a kapusakra):**
> - **Minden H5P elé heading az aktivitás nevével** — hogy a madrih (és a képernyőolvasó) tudja, melyik feladatba érkezik, mielőtt beletenyerel.
> - **Rövid task description** közvetlenül a heading alatt: 1–2 mondat arról, mi a dolga és mikor „kész” — ne kelljen a feladatból visszafejtenie, mit várunk tőle.
> - **A meglévő AI-videókhoz magyar felirat + leirat kötelező** — visszamenőleg is: ahol már van beágyazott AI beszélő fej / narrált videó, oda magyar feliratot és teljes szöveges leiratot kell pótolni (hang nélkül, tömegközlekedésen is teljesíthető legyen).

## 4. Mobil-first táblázatok és produktumok

- Többoszlopos táblázatot **ne vízszintes görgetésű táblaként** jeleníts meg mobilon (apró cellák, horizontális scroll → ellentmond a „nincs zsúfolt táblázat” elvnek).
- Helyette **kártya / akkordeon nézet**: egy sor = egy blokk, a mezők **egymás alatt** (pl. egy helyzet = egy kártya a 4 mezővel függőlegesen).
- Produktum-beadásnál (Assignment):
  - adj **letölthető sablont** (doc / sheet; Google-sablont csak szervezeti fiókból, korlátozott megosztással, HUM-PRIV-01), hogy a madrihnak ne kelljen mobilon táblázatot építenie a feltöltéshez;
  - **engedélyezd az online-text beadást** is (Online text ON) a fájlfeltöltés mellett.
- Cél: csökkenteni a többlépcsős, súrlódásos beadási folyamatot, ami a leadási arányt (LA-metrika) rontja.

## 5. Eszköz- és adat-méltányosság (equity-fallback)

- A mobil-first premissza nem feltételezheti, hogy **minden madrihnak van saját okostelefonja + elegendő adatforgalma** (a videós leckék adatigényesek). Ahol az eszköz vagy az adatkeret hiányzik — nincs saját készülék, megosztott a családi telefon, korlátos az adatkeret —, ott **alternatív útnak kell lennie**: az eszközhiány **nem zárhat ki a completionből**.
- **Kötelező minimum a videós/adatigényes leckékhez:**
  - adj **alacsony adatigényű, offline letölthető leckeváltozatot** (a narráció szöveges leirata + a kulcsképek; a felirat **és** hozzáférhető szöveges leirat / alternatíva eleve elvárás — lásd 1. szakasz —, így a videó hang és sávozás nélkül, letöltött szövegből is teljesíthető);
  - az **F-peula** (a nem teljesült kapu utáni, offline, képző-kísérte javítási alkalom) egyben **eszközhöz-jutási pont** is: itt – és az F-peula idején belüli Csendes pótlás blokkban, ahol van ilyen – a madrih a ken közös eszközén / a helyszín wifijén végezheti el az online elemeket;
  - ahol a kapus/online elem teljesítése eszközhöz kötött, ott **biztosítani kell egy eszközfüggetlen pótlási utat** (a fenti offline/letölthető változat + a ken közös eszköze); ez a Csendes pótlásra (önálló elmaradás-pótlás) is vonatkozik. Ahol F-peula elérhető (éles kapu sikertelensége után kötelező, puha kapunál ajánlott), az is egyenértékű tér — de a méltányos hozzáférés **nem függhet kizárólag** az F-peula meglététől, mert F-peula csak nem teljesült kapu után jár;
  - a közös eszközön mindenki a saját fiókjával dolgozik, és a munka végén kijelentkezik, hogy a szabad szöveges válaszait más ne lássa (levezetve a HUM-PRIV-01 projektgazdai döntés „legszűkebb szükséges hozzáférés” elvéből).
- Tedd explicitté a lecke fejlesztői megjegyzésében, ha egy elem csak online, élő neten teljesíthető — ez akadálymentesítési kockázat, és kell hozzá offline tartalékút (a letölthető változat, a ken közös eszköze, illetve az F-peula).

## 6. Szabad szöveg és önreflexiók

- **Megnevezés (hivatalos szabály).** A specifikációban ne használj kitalált vagy bizonyítatlan H5P-típusnevet. A H5P jelenlegi kínálatában **létezik Free Text Question** a pontozás nélküli szabad szöveges válaszhoz, mellette **Essay** és kötött válasznál **Fill in the Blanks** is használható. A tananyagban továbbra is a pedagógiai igényt írjuk le magyarul: **„rövid szöveges válasz”**, illetve **„hosszabb szöveges reflexió”**. A konkrét megvalósítást a cél Moodle/H5P telepítés és a befoglaló tényleges támogatása dönti el.
- ⚠️ **Szabad szöveg és Course Presentation — igazolt korlát.** A H5P hivatalos válasza szerint az **Essay NEM adható hozzá Course Presentationhöz**; a megnevezett támogatott alternatíva az **Interactive Book**, amely az Essay-t alcontentként kezeli. Ezért **egyetlen lecke sem tekintheti bizonyítottnak**, hogy egy Course Presentation dián belül szabad szöveges mező jelenik meg.
- **A megvalósítás négy megengedett útja** (a választás a cél Moodle/H5P verzión, acceptance-teszttel dől el — lásd `LMS – H5P runtime acceptance.md`):
  1. **Moodle-oldali szövegmező** a lecke mellett (Assignment online text vagy Quiz esszé-kérdés) — hosszabb, megőrzendő reflexiónál ez az alapértelmezett, könnyebben auditálható út;
  2. **H5P Free Text Question** pontozás nélküli rövid válaszhoz, **csak** ha a célhoston engedélyezett, a szükséges xAPI/LRS-viselkedés rendelkezésre áll, és a választott befoglalóban ténylegesen működik;
  3. **H5P Essay** ott, ahol a befoglaló content type ezt igazoltan támogatja (pl. Interactive Book);
  4. **Fill in the Blanks**, ha a válasz ténylegesen kötött (sablonmondat kiegészítése).
- Önreflexióknál a szöveges mező **completion-alapú** legyen. H5P Essay esetén a kulcsszó-alapú automatikus pontozás nem használható a személyes reflexió értékelésére; Free Text Question esetén pedig a szabad szöveget nem tekintjük automatikusan pontozható teljesítménynek.
- Így nem keletkezik téves pontszám ott, ahol a cél a „megcsinálta / nem csinálta meg” completion, nem az értékelés.

> *(Forrás: H5P 2026-02 frissítés és Release Overview: Free Text Question jelenlegi content type; H5P staff dokumentált korlátja: Essay nem adható Course Presentationhöz. A cél Moodle/H5P verzió és a konkrét befoglaló működése továbbra is futtatási tesztet igényel.)*

### KAPUS H5P „pre-flight” checklist

> Ez a blokk **kizárólag a kapus / értékelt (kapuhoz, completionhöz vagy teljesítési kapuhoz kötött) H5P-elemekre** vonatkozik — ahol a továbblépés a madrih teljesítésén múlik. Itt a hozzáférhetőség nem „jó, ha van”, hanem **élesítési feltétel**: ha bármelyik pont kipipálatlan, az elem **nem mehet élesbe**, mert egy hanih vagy madrih emiatt elakadhat a kapuban.
>
> **„Kész = élesíthető” definíció:** az elem akkor élesíthető, ha **mind a 8 pont** ki van pipálva, a pre-flightot nem az elem szerzője végezte, a független második ellenőrzés megtörtént, ÉS a hozzáférhetőségi felelős aláírta (a szerepeket lásd lent, `HUM-A11Y-01`). Részleges teljesítés nem „majdnem kész” — kapus elemnél a hozzáférhetőségi rés egyenlő azzal, hogy valaki kizáródik a továbbhaladásból.

- [ ] **Célméret (SC 2.5.8, AA)** — a mutatóeszközös célok mérete **legalább 24×24 CSS pixel**, **kivéve** a szabvány kivételeit: elegendő **térköz** (24 CSS px átmérőjű kör nem metsz másik célt), **egyenértékű** másik vezérlő ugyanazon az oldalon, **szövegbe ágyazott (inline)** cél, **user agent** által meghatározott méret, vagy ha az adott megjelenítés **elengedhetetlen**. Gyakorlati elvárásunk: a válaszgomb, hotspot és drop-zóna ujj-barát legyen mobilon.
- [ ] **Billentyűzet-teljesíthetőség** — az elem **végigvihető és befejezhető kizárólag billentyűzettel** (Tab-rend logikus, fókusz látható, egér/érintés nélkül is teljesíthető).
- [ ] **Drag-free egypontos alternatíva (SC 2.5.7, AA)** — ha az elem húzásra épül, van **húzás nélkül, egyetlen kattintással/koppintással is teljesíthető** egyenértékű út, hogy a motoros nehézséggel élő vagy apró kijelzőn dolgozó madrih is átjusson a kapun. A **Single Choice Set** (kikapcsolt „Auto continue” beállítással), az egyválaszos módú **Multiple Choice** és a koppintás-alapú párosítás tipikusan ilyen; a **Drag the Words nem** (maga is húzásra épül). Hogy a választott típus a célverzión valóban húzásmentes-e, **a tényleges renderen kell ellenőrizni**, nem a típus nevéből következtetni.
- [ ] **Időzítés (SC 2.2.1, A)** — az elem nem lép tovább magától, és a visszajelzés nem tűnik el időzítve, mielőtt a madrih elolvashatná; a Single Choice Set „Auto continue” beállítása ki van kapcsolva (a H5P saját leírása szerint képernyőolvasós használathoz ez szükséges).
- [ ] **Alt-szöveg / szöveges ekvivalens** — minden **információt hordozó** képnek, ikonnak, hotspotnak, képernyőképnek van érdemi alt-szövege vagy szöveges megfeleltetése; a **pusztán dekoratív** elem üres/rejtett alt-tal megy, hogy a képernyőolvasó átugorja (2. szakasz). A feladat **nem oldható meg kizárólag vizuális infóból**.
- [ ] **Kontraszt** — **szöveg** (SC 1.4.3, AA): törzsszöveg **≥ 4,5:1**, nagy méretű szöveg **≥ 3:1**. **Nem-szöveges elem** (SC 1.4.11, AA): a UI-komponensek és állapotaik, valamint a jelentést hordozó grafikai elemek szükséges vizuális információja **≥ 3:1** a szomszédos színekhez képest (a szabvány kivételeivel: inaktív komponens, user agent által meghatározott megjelenés, illetve ha az adott grafikai megjelenítés elengedhetetlen).
  - *(Projekt-cél a WCAG-minimum FELETT, nem normatív követelmény: a kapus elemeknél a lényeges UI-kontrasztot is igyekszünk 4,5:1-re hozni, mert a madrihok jellemzően olcsó kijelzőn, gyenge fényben, mozgás közben használják.)*
  - *(D1 vizuális rendszer – HUM-MEDIA-01, projektgazdai döntés, 2026-10-02: a szín soha nem önálló jelentéshordozó, a jelentést mindig felirat, forma vagy betűjel is hordozza (WCAG 2.2 SC 1.4.1). A szín szemantikája modulhatókörű, ezért ugyanaz a szín más modulban más jelentést hordozhat. A kanonikus paletta és a produkciós semleges skála: `Média-assetek/PRODUCTION-DECISIONS.md` D1.)*
- [ ] **Magyar nyelv + iframe-title** — az elem nyelve magyarra állítva, az iframe-nek **beszédes magyar címe** van (képernyőolvasó felolvassa, melyik aktivitásban jár a madrih).
- [ ] **Felirat + leirat a videókhoz** — minden beágyazott (AI beszélő fej / Interactive / narrált) videóhoz **magyar felirat ÉS teljes szöveges leirat** (a dián vagy a médiaelem mellől elérhető szövegként, lásd 1. szakasz), hang nélkül is teljesíthető; a videó egyenként be van sorolva, és ha jelenetvideó, amelyben arckifejezés, gesztus vagy képi történés hordoz jelentést, hangalámondásos képleírás (SC 1.2.5) és mellette szöveges alternatíva (SC 1.2.3) is tartozik hozzá.

**Jóváhagyó szerepkör (`HUM-A11Y-01`):** a hozzáférhetőségi felelős (accessibility reviewer). Projektgazdai döntés (2026-10-02): a felelős (accountable) hozzáférhetőségi gazda a **Ros Hinuh** (jelenleg Lili); a független, élesítés előtti második ellenőrző **Marci**. A szerző nem hagyja jóvá a saját anyagát: a pre-flightot nem az elem szerzője, hanem egy másik, a WCAG- és H5P-követelményeket ismerő személy végzi. Utólagos ellenőrzés (vétó/QA): a programvezető.

## 7. Kognitív és olvasási hozzáférhetőség

> A hozzáférhetőség nem áll meg az érzékelésnél (felirat, alt-szöveg, kontraszt, billentyűzet) — kiterjed a **megértésre** is. Ez a szakasz a leckeszövegek olvashatóságát és a tanulási nehézséggel élő madrih támogatását rögzíti (a WCAG 2.2 érthetőség-elve és a többszörös reprezentáció — UDL — mentén).

- **Plain-language a leckeszövegre:** a tananyagszöveg **rövid mondatokra, egyszerű, tegező nyelvre** törekszik; a szakszót (someres/pedagógiai fogalom) az **első előforduláskor egy mondatban feloldod**, vagy a glosszáriumra linkelsz. (Ez a leckeszövegre vonatkozik — nem keverendő az adatkezelési „just-in-time” dobozok plain-language elvével.)
- **Kulcsfogalom mindig szövegben is:** minden lényeges fogalom és lépés **szövegként** is jelen van, nem csak ábrán/ikonon (ez a 2. szakasz alt-szöveg-elvárásával együtt biztosítja, hogy a lényeges tartalom szövegként és vizuálisan is megjelenjen, ami tanulási nehézségnél kritikus).
- **Tanulási nehézséggel / diszlexiával / SNI-vel élő madrih támogatása:** ahol az olvasás vagy a megértés akadályba ütközik, a madrih a **mentorától** kap segítséget. Ha egy kapu nem teljesült, az **F-peula** egyéni/kiscsoportos támogató tér; ha a madrih csak lemaradt, **Csendes pótlással** pótol (az F-peula idején belüli Csendes pótlás blokkban is, ahol van ilyen) — az online szöveg nem az egyetlen út a tananyaghoz.

---

## Gyors checklist fejlesztőnek

- [ ] Szinkronizált videó → **felirat** (kötelező, SC 1.2.2) + leirat a dián vagy a médiaelem mellől elérhető szövegként (ajánlott); csak hangot tartalmazó anyagnál a teljes leirat elegendő (SC 1.2.1); a hangalámondás igénye (SC 1.2.5) videónként megvizsgálva: a beszélő fej képi sávja lehet dekoratív, a jelentést hordozó jelenetvideóhoz hangalámondásos képleírás (SC 1.2.5) és mellette szöveges alternatíva (SC 1.2.3) kell
- [ ] Narráció nem hordoz kizárólag hangban elérhető infót
- [ ] Interactive Video jelenetei feliratozva
- [ ] Alt-szöveg minden képernyőképhez/ikonhoz/grafikához
- [ ] Húzásra épülő feladat mellett **húzásmentes**, egykattintásos + billentyűzetes egyenértékű út (SC 2.5.7) — a konkrét típus húzásmentességét a renderen igazold
- [ ] Interakció-típus következetes a modulon belül
- [ ] Mobil-táblázat = kártya/akkordeon nézet, nem vízszintes scroll
- [ ] Adatigényes/videós leckéhez offline letölthető, alacsony adatigényű változat + eszközhöz-jutási pont (a ken közös eszköze, illetve az F-peula); eszközhiány nem zár ki a completionből
- [ ] Produktumhoz letölthető sablon + online-text beadás engedélyezve
- [ ] Szabad szöveges önreflexió completion-alapú; Essaynél nincs kulcsszó-alapú automatikus értékelés, Free Text Question csak igazolt host/befoglaló-támogatással
- [ ] Leckeszöveg plain-language: rövid mondatok, szakszó első előforduláskor feloldva; kulcsfogalom szövegben is (nem csak ábrán)

---

## Hivatkozások

- H5P content type ajánlások: https://help.h5p.com/hc/en-us/articles/7505649072797-Content-types-recommendations
- H5P content types: https://h5p.org/content-types-and-applications
- H5P Essay: https://h5p.org/essay
- H5P Interactive Video: https://h5p.org/interactive-video
- Moodle activity completion: https://moodle.com/news/track-learners-progress-using-activity-completion-moodle/
- WCAG 2.2 SC 2.5.7 – Dragging Movements (Understanding): https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements.html
- H5P Drag the Words (a húzás a működés alapja): https://h5p.org/drag-the-words


## Pontosítás: előre rögzített videó és hang

- **WCAG 2.2 SC 1.2.2:** előre rögzített, szinkronizált médiában a hangzó tartalomhoz **felirat szükséges** (a WCAG kivételétől eltekintve, amikor maga a média egy már meglévő szöveg alternatívája és így is van jelölve).
- A teljes szöveges leirat hasznos és erősen ajánlott kiegészítő, de **nem helyettesíti automatikusan a feliratot** szinkronizált videónál.
- Interaktív tartalomnál a billentyűzet, fókuszsorrend, név/szerep/érték, kontraszt és célméret a tényleges Moodle/H5P renderen tesztelendő, nem csak a Markdown-specifikációban.
