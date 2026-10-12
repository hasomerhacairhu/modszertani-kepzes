# M0–Z módszertani képzés — 125 szakmai döntés kutatással alátámasztott javaslata

**Dátum:** 2026. október 12.\
**Forrásverzió:** `next-version/AP-2026-10-11-01`, `e67cce5` · [Draft PR #30](https://github.com/hasomerhacairhu/modszertani-kepzes/pull/30)\
**Elsődleges kérdéslista:** [2026-10-12 Projektgazdai döntési csomag](https://github.com/hasomerhacairhu/modszertani-kepzes/blob/e67cce5/01%20Fejleszt%C3%A9s/04%20Audit/2026-10-12%20Projektgazdai%20d%C3%B6nt%C3%A9si%20csomag%20%E2%80%93%20next-version,%20AP-2026-10-11-01.md) — 141 bejegyzés, ebből 125 tényleges döntés és 16 bizonyíték/jóváhagyás.\
**A dokumentum jellege:** független szakmai javaslat; **nem jóváhagyási jegyzőkönyv, nem DPO-vélemény, nem Memuna-signoff, nem módosítja a repót.**

## Vezetői összefoglaló

A döntési csomag **mind a 125 tényleges kérdésére** szerepel alább konkrét ajánlott irány, nem csupán újabb eldöntendő kérdés. A kutatás és kánonösszevetés alapján **53 javaslat közvetlenül támogatható irányként** (`A`) és **72 feltételes, pontosított irányként** (`F`) került megfogalmazásra. Az `F` **nem azt jelenti, hogy nincs válasz**: azt jelenti, hogy a választott irány implementálásához az adatkezelési, gyermekvédelmi, implementációs, szerzői vagy más tényleges jogosultság/teszt tisztázandó.

Ez **nem a 125 döntés formális meghozatala**. A projektgazda saját hatáskörébe eső javaslatokat elfogadhatja; a Memuna, DPO, értékelési felelős, jogász, Moodle-gazda, szakmai lektor és más jogosultak hatáskörébe tartozó döntéseket csak ők hagyhatják jóvá. A 16 fennmaradó bejegyzés eleve bizonyíték vagy formális signoff, így kutatással sem jelölhető `DONE`-nak.

**Döntési státuszok**

- **A — konkrét alapjavaslat.** A kánonra/lezárt döntésre vagy jó általános szakmai indokra vezethető vissza. A jogosult jóváhagyó szerepe továbbra is érvényes.
- **F — konkrét, feltételes javaslat.** Válasz és preferált irány adott, de objektív hiányzó adat, implementációs teszt, helyi szerzői szándék vagy szakértői jogkör nélkül nem fogadható el automatikusan.

**Nem változott:** a pilot `main@213a4c5` forrását és PR #30 Draft állapotát tiszteletben kell tartani. A két release-verdict:

```text
MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD
LEARNER-RELEASE-VERDICT: NO-GO
```

Ezek a PR-forrásban rögzített gépi verdiktek, nem Moodle-runtime bizonyítékok. A staging buildet a 125 döntés hiánya önmagában nem tiltja, de a tanulói release-t a szerepköri és technikai kapuk igen.

### A javaslatcsomag hét vezérelve

1. **Ne ígérjünk nem létező monitoringot vagy azonnali beavatkozást.** Az LMS-feladat nem helyettesíti a külön gyermekvédelmi jelzési csatornát.
2. **Önreflexió és érzékeny válasz alapból ne legyen tárolt, pontozott vagy completion-feltétel.** Csak indokolt, jóváhagyott kivételek lehetnek.
3. **Az értékelés és a completion két külön réteg.** Moodle activity-completion nem lehet azonos a képzés komplex, személyes megerősítési kapujával.
4. **Kritikus gyermekvédelmi hibát ne kompenzáljon magas összpontszám.** A konjunkciós kapuknál a kritikus feltétel külön, valósan érvényesül.
5. **Személyes önfeltárás helyett fiktív, egyenértékű demonstrációt kérjünk.** A passzjog nem lehet burkolt büntetés.
6. **A meglévő kanonikus tanulási célokat tartsuk meg; ne hozzunk létre felesleges új activityket és adatfolyamokat.** Ahol ellentmondás van, előbb a meglévő feladathoz igazítsuk az ígéretet.
7. **Kiadás előtt valódi adatfolyam-, jogosultság-, runtime- és szakértői bizonyíték kell.** A build zöld státusza ezt nem helyettesíti.

### Sürgős P0 prioritás (7 bejegyzés)

| ID | Javasolt első lépés | Formális kapu |
|---|---|---|
| **GYV-1** | Az indokolatlan „mentor azonnal bevonja” ígéretet szüntessük meg, vagy bizonyítsunk SLA-val működő felügyeletet; külön akut jelzési út | Memuna + DPO |
| **GYV-2** | Valódi passz és egyenértékű fiktív tudásdemonstráció a kötelező krízisgyakorlatban | Memuna + programvezető + assessment |
| **GYV-24** | A Memuna SHA-hoz kötött, tényleges G1-visszaolvasása | Nem automatizálható signoff |
| **ADV-6** | A bemutatkozó fórum pilotbeli megnyitását függesszük a DPO megőrzési/háttérhozzáférési döntésétől | DPO |
| **ADV-E1** | Activityszintű DPO G2-visszaolvasás, szerepek, xAPI/LRS, backups vizsgálata | Nem automatizálható signoff |
| **ERT-12** | A tárolt mini-SBI kizárólag fiktív helyzetet fogadjon | Projektgazda, DPO-vétó |
| **RT-2** | Valós Moodle/H5P célverziós M0/M1 negatív tesztek + N-M1-04 beviteli elem nélküli út | Moodle build-felelős |

## 125 döntés — tételesen

**Olvasási szabály:** minden sor a forráscsomag **azonos ID-jére** utal. A státusz javaslatom bizonyosságát/engedélyezhetőségét jelöli, **nem a forrás ledger-státuszát**. Ha a forrás opciói közül nem egyet választok betűvel, az ajánlás kifejezetten kombinált vagy konzervatív megoldás, és ennek tételeit a döntéskor ellenőrizni kell.

## 1. Gyermekvédelem — GYV-1–23

Kánoni biztonsági protokoll + passzjog; szakmai vétó a Memunáé. A gyakorlati ajánlások nem helyettesítik a helyi gyermekvédelmi operatív rendet.

| ID | Ajánlás típusa | Javasolt konkrét döntés / indok |
|---|---|---|
| **GYV-1** | **F** · feltételes | Az LMS-M2-09 szabad reflexiót ne kezeljük folyamatosan figyelt gyermekvédelmi bejelentőcsatornaként, és töröljük a garantálhatatlan „mentorod azonnal bevonja” ígéretet. Az LMS-M2-05 kapubeadványon csak akkor maradjon határidős átnézés, ha tényleges szolgálati rend, értesítés, helyettesítés és SLA bizonyított; egyébként ott is világos, külön akut jelzési út legyen. Memuna + DPO ellenőrzése kell. |
| **GYV-2** | **F** · feltételes | Érzékeny krízis-/önfeltárási gyakorlatnál biztosítsunk valódi passzt és nem személyes, fiktív alternatívát; a teljesítés nem függhet önfeltárástól. Ha a feladat biztonsági kompetenciát mér, a passzhoz ekvivalens tudásdemonstráció járjon, ne automatikus kapuátengedés. M2.4 kötelező mezője így biztosan módosítandó; M3/M4-es kör Memuna- és completion-QA. |
| **GYV-3** | **F** · feltételes | Terjesszük ki a SAFE-7 helyenkénti felülvizsgálatát valamennyi 1:1-es kockázati helyzetre, a kritikus itemek kulcsának érintetlenül hagyásával. A 7 helyre külön Memuna-verdict szükséges; addig az egyéni privát kapcsolattartást ne tanítsuk automatikus helyes eljárásként. |
| **GYV-4** | **F** · feltételes | Egységes, szerepnév-alapú krízisút legyen a veszélyt bemutató dobozokban: kijelölt Memuna/helyettes, tényleges elérhetőség; közvetlen veszélyben 112, érzelmi támogatásra 116 111. FONTOS: a 116 000 elsődlegesen az eltűnt gyermekek forróvonala, nem általános segélyhívó; a tananyagban szolgáltatás és címzett szerint pontosítani kell, és a Memuna kiadáskor ellenőrizze a számokat és az órákat. |
| **GYV-5** | **F** · feltételes | Érzékeny, potenciálisan felkavaró peulán előzetesen legyen legalább két rendelkezésre álló, felkészített 18+ felelős, vagy azonnal elérhető helyettes és kötelező megállítási protokoll. Egyszemélyes működés csak dokumentált alacsony kockázatú helyzetben; felkavart kiskorú nem maradhat egyedül. Végleges létszámnorma a Memuna és programvezető hatásköre. |
| **GYV-6** | **A** · alapjavaslat | A meglévő GK §4:63–64 védelmi minimum szerepeljen röviden minden releváns peula képzői instrukciójában; a Z.A-nál előbb nyugodt meghallgatás és biztonság, gyermekvédelmi jelzés esetén azonnal Memuna. A szereplési szorongás nem automatikusan gyermekvédelmi krízis, de legyen szabad megállni és passzolni; a Memuna hagyja jóvá a küszöböt. |
| **GYV-7** | **F** · feltételes | Kétlépcsős küszöb: zaklatás, feltárás, önsértés vagy más veszélyeztetettség gyanújánál azonnali Memuna-jelzés; pusztán nem veszélyeztető nehéz érzelemnél támogató mentorálás, választási lehetőséggel. A csoportchatbántalmazás M0-specifikus küszöbét a Memuna külön ellenőrizze; a kvízkulcs nem módosul vélelmezésből. |
| **GYV-8** | **F** · feltételes | Terepi veszélynél a helyszíni 18+ felelős cselekszik azonnal, és a szervezeti Memuna-jelzés külön megtörténik; ez nem két alternatív, egymást helyettesítő címzett. Pusztán hiányzó felnőtt felügyelet operatív ügyét a képző/programvezető rendezi, akut kockázatnál Memuna is. Jóváhagyás: Memuna + programvezető. |
| **GYV-9** | **F** · feltételes | Az M7 blokkoló R4-rubrika minimumába és a mintatáblába kerüljön a felelős 18+ felnőtt megnevezése, de csak a rubrikahorgony és a már tanított Q9/(C) szabály összehangolt, formális jóváhagyásával; a hallgató nem bukhat előzetesen nem közölt követelményen. |
| **GYV-10** | **F** · feltételes | Tanulók, különösen kiskorúak számára ne nyissunk szabad beszélgetéses AI-segédet addig, amíg nincs igazolt adatkezelési és kríziskezelési út. Ideiglenes alap: AI-segéd kikapcsolva, no-AI út teljes értékű. Később előre meghatározott krízisválasz, külön jelzési csatorna és kontrollált, szükséges metaadat lehet; automatikus veszélyszűrés nem helyettesíti az embert. |
| **GYV-11** | **F** · feltételes | Tárolt beadandóba kerülő gyermekvédelmi feltárásnál ne legyen az LMS az incidens elsődleges nyilvántartása. Dokumentált, jogosult Memuna-eljárás, szükség szerinti korlátozás/helyesbítés és adatvédelmileg jóváhagyott törlés/megőrzés kell; a tanuló kapjon biztonságos, feltárásmentes pótlási utat, a kapueredmény ne függjön a feltárástól. Ne töröljünk bizonyítékot automatikusan jogi megőrzési felülvizsgálat nélkül. |
| **GYV-12** | **A** · alapjavaslat | M1-ben a szabad szöveghez az ADV §11 már elfogadott, adattakarékos mondata kerüljön az önfeltárást sugalló egyedi felszólítás helyére; M2-ben a meglévő biztonsági blokk legyen közvetlenül elérhető az érintett mezőnél. Ne hozzunk létre új, önkéntelen disclosure-ra ösztönző képeslap-szöveget; Memuna QA. |
| **GYV-13** | **A** · alapjavaslat | Az érzékeny, valódi helyzeteknél a meglévő rövid „azonnal vond be a Memunát” formula egységesen szerepeljen; a személyes reflexiós feladatoknál ne sugalljunk kötelező jelentést a puszta érzelmi megosztás miatt. A Memuna erősítse meg a konkrét helyeket és a poszterek rövid változatát. |
| **GYV-14** | **F** · feltételes | Kiadás előtt a Kék Vonal és az NMHH aktuális szolgáltatásleírása alapján javítsuk a hívószámok célcsoportját: 116 111 gyermek- és ifjúsági lelkisegély, 116 000 eltűnt gyermekek vonala; 112 közvetlen veszély. Ha a kánon félrevezető, a Memuna formálisan nyissa újra a konkrét tájékoztató sort; ne változtassunk telefonszámot igazolás nélkül. |
| **GYV-15** | **F** · feltételes | A semleges „a Memuna és – ahol indokolt – a hivatalos szervek feladata” megfogalmazást ajánlom az önsértési eseteknél; a tanuló nem nyomoz, nem konfrontál. Hogy mely szerveknek, mikor kell külső jelzés, azt a jogász/JOG-1 és a Memuna határozza meg. |
| **GYV-16** | **F** · feltételes | Kirekesztést nem demonstrálunk valódi kirekesztett/kirekesztő szerep kiosztásával; fiktív harmadik személyű esetelemzés és választásos feldolgozás legyen az alap. Az M3.A csoportszobor csak önkéntes, nem megbélyegző, passzolható formában maradjon, explicit debrief-fel. Memuna szakmai döntés. |
| **GYV-17** | **A** · alapjavaslat | Az M6.A tiltott zónái legyenek rövid, kötelezően kimondott biztonsági keretek a gyakorlat előtt; a kiskorúakra, identitásra, kirekesztésre és önfeltárásra is térjen ki. Ne kerüljenek olyan állítások a kapukvízbe, amelyeket az élő peulán opcionálisan hall a résztvevő. |
| **GYV-18** | **F** · feltételes | A 12. item „friss seb” provokatív keretezése helyett fiktív, szereplőközpontú kérdés és biztonságos válasz legyen; a „nálatok” önfeltáró kérdés opcionális és passzolható. A megváltozott disztraktor/✅ szöveg értékelési felelős + Memuna jóváhagyását igényli. |
| **GYV-19** | **A** · alapjavaslat | Mind az M2.A, mind az M4.3 gyakorlat-instrukciója kapjon egy rövid, kánoni határmondatot: aggasztó feltárásnál meghallgatni lehet, részleteket kikérdezni/nyomozni nem; a képzőnek és a Memunának a kijelölt úton jelezni kell. |
| **GYV-20** | **F** · feltételes | A zsidósághoz, családi viszonyhoz és személyes különbözőséghez kötődő identitás-vonal ne követeljen nyilvános kiállást. Privát, papíros vagy fejben végzett út, passz és nem érzékeny közös reflexió legyen a default; Memuna/DPO review után lehet az önkéntes nyilvános változatot mérlegelni. |
| **GYV-21** | **A** · alapjavaslat | A „név nélkül” nem egyenlő anonim jelleggel egy kis kvucában. Gyermekvédelmi és érzékeny példából csak fiktív, illetve ténylegesen nem visszaazonosítható, általánosított változatot kérjünk szóban is. Valós esetet sem szóban, sem beadandóban nem tehetünk alapkövetelménnyé. |
| **GYV-22** | **A** · alapjavaslat | Az M1.1 önfeltárásához kerüljön az M1.A mintájára világos határmondat: a személyes történet megosztása nem elvárás és nem feltétele a jó madrihságnak; lehet általános/fiktív példát választani. Memuna és lektor ellenőrizze. |
| **GYV-23** | **F** · feltételes | Első körben csoportszintű, nem megbélyegző korrekciót és a biztonsági 1–2. item nyilvános visszajelzését ajánlom. Egyéni mentoros utánkövetés csak indokolt pedagógiai cél, célhoz kötött válaszhozzáférés és DPO-jóváhagyás mellett; a kvíz diagnosztikus marad. |

## 2. Adatvédelem — ADV-1–15

Adatminimalizálás, szükségesség, jogosultsági visszaolvasás, különleges adatok; jogalapot, megőrzési időt és GDPR kivételt a DPO/jogász nem vélelmezhet.

| ID | Ajánlás típusa | Javasolt konkrét döntés / indok |
|---|---|---|
| **ADV-1** | **F** · feltételes | Vegyes (c) hozzáférési modell: mentor csak saját csoportjának lássa a beadást; admin/editor jogosultság szűk, név szerint kiosztott, auditálható, de technikai admin teljes hozzáférését ne tagadja a tájékoztató. A „csak mentorod látja” ígéretet a tényleges RBAC-hoz kell igazítani a staging role-matrix után. |
| **ADV-2** | **F** · feltételes | Alapértelmezés: kijelölt értékelő olvas, második/fellebbezési értékelő csak konkrét eljárásnál, Memuna szükség esetén, F-peula képzője csak aggregált vagy minimális hiánylistát lát. Az F-peula szereposztást és a vészhozzáférést dokumentálni kell; csoport-hozzáférés ténylegesen tesztelendő. |
| **ADV-3** | **F** · feltételes | Alapértelmezés az N-M1-04 mintája: opcionális reflexió saját jegyzetben, beviteli elem és completion nélkül. Az M4 már tárolt TEXT-C-ként deklarált helyein csak formális completion-/build-spec döntéssel lehet adatmentesre átállni; ha pedagógiai bizonyíték nélkül tárolt marad, a tanulói ígéret legyen igaz és a DPO írja alá az adatkört. |
| **ADV-4** | **F** · feltételes | Érzelmi önjelzést, passzt és véleményt ne pontozzunk, és lehetőleg ne rögzítsük a követett H5P próbálkozásban. M1.1-ben a szöveg + Tovább út az alap; M3 SAFE-1 ágnál a konkrét H5P verzió, próbálkozás-riport, xAPI/LRS, mentett állapot és szerepkörök visszaolvasása után dönthető el a tárolásmentes technika. |
| **ADV-5** | **F** · feltételes | Különleges vagy érzékeny világnézeti információként kezeljük azt a névhez köthető válaszmintát, amely vallási/ideológiai meggyőződésre következtetni enged. Ne legyen kötelező azonosítható vallási önbesorolás; engedjünk semleges, fiktív vagy válasz nélküli egyenértékű utat pontlevonás nélkül. GDPR 9. cikk szerinti minősítés és kivétel csak jogi/DPO jóváhagyással. |
| **ADV-6** | **F** · feltételes | A FORUM-C bemutatkozó fórum maradjon valódi tanulóknak zárva, amíg nincs dokumentált cél, hozzáférési kör, DPO által elfogadott megőrzési idő és életkornak megfelelő tájékoztató. A „képzés vége + 90 nap” nem automatikus jogszerű alapérték. Addig szóbeli/nem rögzített bemutatkozás a biztonságos alternatíva. |
| **ADV-7** | **A** · alapjavaslat | Közös papírszabály: személyes önfeltáró cetli a résztvevőnél marad vagy hozzá visszakerül; névvel nem függesztjük ki és nem gyűjtjük, fotózás alapból nincs. Szükséges csoportproduktum fotója csak előre rögzített céllal, hozzáféréssel, tájékoztatással és HUM-PRIV-02 szerinti engedéllyel; saját telefon ne legyen kötelező. |
| **ADV-8** | **F** · feltételes | Visszaazonosítható kis csoportos produktumot ne minősítsünk anonimnak. Elsődlegesen visszaadás, szóbeli összegzés vagy ténylegesen deidentifikált csoportos aggregálás; ha a mentor személyhez kapcsolja a feljegyzést, azt személyes adatként a megfelelő mentori adatkörhöz kell sorolni. Ne találjunk ki univerzális „anonim X fő fölött” küszöböt. |
| **ADV-9** | **A** · alapjavaslat | A Peula v2 minimális csoportszintű kvuca-adatszabályát alkalmazzuk az M4/M5/M6 produktumokra is: korosztály, hozzávetőleges létszám, általános energia/hangulat igen; név, diagnózis, konkrét azonosítható eset nem. Kis csoportban az egyedi élethelyzet is visszaazonosítható lehet, ezért DPO QA. |
| **ADV-10** | **F** · feltételes | Moodle és papír legyen az alap. Külső Google-sablon csak szervezeti fiókkal, adatfeldolgozói és hozzáférési felülvizsgálattal; nyílt digitális fal vagy QR-eszköz nélkül is teljesíthető egyenértékű feladat. A szolgáltató, adatkör, megőrzés és harmadik fél tényleges ismeretéig ne engedjük az opcionális külső eszközt. |
| **ADV-11** | **F** · feltételes | Egységes közös eszköz-protokoll: jelszómentés és személyes munkapéldány tilos; kijelentkezés, munkamenet-ellenőrzés, letöltési törlés és adatmentes papír/saját eszköz alternatíva. Kivételt csak LMS-biztonsági és DPO teszt után, szükséges esetben engedjünk. |
| **ADV-12** | **F** · feltételes | Az AI-végponton a tartalom naplózása legyen kikapcsolva alapból; csak feltétlenül szükséges technikai metaadat, rövid, dokumentált megőrzéssel. Előbb mérjük fel a provider-, proxy-, hibalog-, backup- és admincsatornákat; ha nem garantálható az adatkizárás, a közvetlen tanulói AI-hozzáférés maradjon inaktív. „store=false” önmagában nem bizonyít teljes naplózásmentességet. |
| **ADV-13** | **A** · alapjavaslat | Az LMS-M2-09 szabad szövegeit ne olvassuk újra pusztán programanalitika miatt. A tanulási folyamatból jogszerűen rendelkezésre álló aggregált mutató használható, különben a „2–3 konkrét szabály” KPI kerüljön ki vagy helyettesítse completion/önértékelési mutató; nem keletkezik új monitoringcél. |
| **ADV-14** | **F** · feltételes | A Z.4 videóopció legyen alapból kikapcsolva, amíg nincs hozzájárulás- és jogosultsági folyamat, visszavonási/törlési út és feltöltés előtti ellenőrzés. A fő szöveges/beadandós út teljesen egyenértékű. Ha később bevezetjük a videót, a fotóra vonatkozó szigorúbb szabályokat is alkalmazzuk rá; a kiskorú jogalapját jogász/DPO ellenőrzi. |
| **ADV-15** | **A** · alapjavaslat | Z.4 Feedback: „Show analysis page” = No, „Enable notification of submissions” = No. A résztvevő ne lássa a kis kohorsz válaszmintáját, automatikus e-mailben ne terjesszünk válaszokat. Külön vizsgáljuk az anonim mód és az adminisztratív back-end hozzáférés tényleges működését. |

## 3. Jogi értelmezés — JOG-1

A Btk. 209/A § és a Gyvt. 17. § alkalmazását szerepkörönként jogi szakértő vizsgálja. A veszélyhelyzeti operatív út nem várhat jogi formai kérdésre.

| ID | Ajánlás típusa | Javasolt konkrét döntés / indok |
|---|---|---|
| **JOG-1** | **F** · feltételes | Ideiglenes szervezeti rend: madrih azonnal a kijelölt Memunának/helyettesnek jelez; a szervezet nevében a jogi tanács alapján kijelölt felnőtt dönt a külső jelzésről, anélkül hogy az akut védelem késne. A Gyvt. 17. § konkrét címzettjeit/időhatárait jogász ellenőrizze; a Btk. 209/A. § nem valamennyi jelzéskésés általános büntetőszabálya, hanem a Gyvt. 17. § (4a)–(4c) szerinti speciális kötelezettségekhez kötődik. Ne állítsunk általános három munkanapos büntetőjogi határidőt jogi vélemény nélkül. |

## 4. Mozgalmi nyelv és terminológia — TERM-1–8

Az ideológiai tartalmat a helyi kánon, a pedagógiai terminológiát a célmérce és a meglévő glosszárium vezeti.

| ID | Ajánlás típusa | Javasolt konkrét döntés / indok |
|---|---|---|
| **TERM-1** | **F** · feltételes | A „dugma isit” fogalom példamutató magatartást jelölő alakja legyen következetes („dugma isitként viselkedik / példát mutat”), ne antropomorf címke („dugma isit vagy”). Az átnevezés a csatolt fájlokra és jóváhagyott kvíztörzsekre is kihat, ezért a helyi mozgalmi terminológiagazda megerősítése kell. |
| **TERM-2** | **A** · alapjavaslat | Az SBI S elemének kánoni magyar neve „helyzet”, az első előfordulásnál elfogadható a „szituáció” szinonima. A rubrikacím is ehhez igazodjon úgy, hogy az értékelt kompetencia és a pontozás ne változzon. |
| **TERM-3** | **A** · alapjavaslat | Az M2.4 két gyermekvédelmi szabálymondatában „transzparens” helyett „átlátható” legyen a szó, a GK szóhasználatával egyezően; tartalmi szabályt nem módosít. |
| **TERM-4** | **F** · feltételes | Az M3.4 tanulói címe legyen természetes magyar („Mit tegyél, mit ne tegyél madrihként?”), míg a belső LMS-azonosító stabil marad; a fájlnév-átnevezés, manifest és hivatkozások együtt, ellenőrzött diffben mozogjanak. A tényleges szerzői cím az M3 modulgazdájának döntése. |
| **TERM-5** | **A** · alapjavaslat | Az LMS-M3-05 tanulói elnevezése legyen következetesen „M3 – Helyzetleírás” (ha indokolt: „red flag és első lépések” alcímmel); ez illeszkedik a gyermekvédelmi kánon helyzetleírás fogalmához, a kód marad változatlan. |
| **TERM-6** | **F** · feltételes | Ha a 3. kártya a tizenéves kvuca állapotáról szól, „Leviatán – év eleji kvuca” legyen, ne „stáb”; a „stáb” a képzői csapatot jelöli. Csak akkor maradjon a stáb, ha a modulgazda konkrét mozgalmi értelemben igazolja a szándékát. |
| **TERM-7** | **F** · feltételes | M2-ben a személyes ideológiai viszonyulás legyen nem pontozott reflektív cél, ne névhez kötött véleménymérés. Az M5-ben a tanulási elvek saját szavas magyarázatát rövid, formatív demonstrációval lehet ellenőrizni; ha nincs erre idő/hely, a hub célmegfogalmazását szűkítsük. Modulgazdai/értékelői jóváhagyás. |
| **TERM-8** | **F** · feltételes | A „someres érték” értékelését a helyi Ideológiai Kézikönyvhez kössük, de ne követeljünk személyes világnézeti vallomást. A rubrika nyitott, leírt kritérium alapján fogadja el az érték és hangulat közti különbséget; a top 3-ban hiányzó someres értékre előre rögzített támogatás legyen, ne utólagos, önkényes bukás. Helyi ideológiai és értékelési QA. |

## 5. Értékelés, kompetencia és completion — ERT-1–50

A rubrika mérje azt, amit tanítottunk; a Moodle-grade, activity-completion és GATE_CONFIRMED következetesen eltérő jelentésű marad.

| ID | Ajánlás típusa | Javasolt konkrét döntés / indok |
|---|---|---|
| **ERT-1** | **A** · alapjavaslat | A H5P Course Presentation completionje a kánoni BSPEC-06 szerint az összefoglaló dia elérését jelentse, ne minden beágyazott kérdés kötelező kitöltését. Csak olyan CP kapjon erre épülő completiont, amelynek valóban van összefoglaló diája; az üres/kihagyott interakciós negatív teszt kötelező. |
| **ERT-2** | **A** · alapjavaslat | A pontozatlan vélemény- és önjelző választó általánosan ne legyen önálló completion-elem, és ne legyen hamis „hibás” visszajelzése. A leckéket a megtekintés/összefoglaló vagy más legitim aktivitás teljesítse; M0.1-nél ezt kifejezetten rögzítsük, nehogy a completion feltétel nélkül megszűnjön. |
| **ERT-3** | **F** · feltételes | Diagnosztikus M5 QUIZ-D: a beküldés ténye elegendő completionhez, tartalmi bukás nélkül. Kötelező Z.4 Feedback: legalább egy nem érzékeny, értelmezhető Required válasz, a személyes kérdéseknél passz és egyenértékű alternatíva. A „kiürítés” valós működését stagingben tesztelni kell. |
| **ERT-4** | **F** · feltételes | Csak a tananyagban ténylegesen megígért formatív kvíz legyen külön Moodle-activity és manifest-sor; szerzői itempoolhoz ne hozzunk létre új tárolt aktivitást pusztán azért, mert a kánon „itembank”-nak nevezi. Az M1 nyitott szöveges itemjei maradjanak szerzői pool, az M2 zárt formatív gyakorló csak akkor activity, ha a tanulói út követeli és DPO által elfogadott. |
| **ERT-5** | **A** · alapjavaslat | Éles kapun első próbálkozás után pontszám és a hibázott kompetencia/kritikus követelmény látszódjon, de ne jelenjen meg a helyes kulcs és a teljes opció-visszajelzés a javító lezárása előtt. Az M3/M7 kritikus itemekhez a mentor szabályosan adjon javítási útmutatást; az eltérő Moodle Review options-t célverzión vissza kell olvasni. |
| **ERT-6** | **A** · alapjavaslat | Diagnosztikus jelzéshez az első, visszajelzés előtti próbálkozás a mérvadó; a későbbi próbálkozások gyakorlásra szolgálnak, nem írják felül a korai szükségletet. M5-ben 3 próbálkozást javaslok (2 helyett is elérhető gyakorlás), M6-ban maradjon a jelenlegi korlátlan formatív út. A gradebook és az analitika e két szerepét el kell választani. |
| **ERT-7** | **A** · alapjavaslat | A valódi tévképzetre épülő, kulcsot nem eláruló disztraktor-követelményt a M5/M6 kánonban már előírt item-bankokra és a gyermekvédelmi leckeitemekre terjesszük ki; minden alacsony tétű ellenőrző kötelező újraírását nem indokolja bizonyíték. |
| **ERT-8** | **A** · alapjavaslat | Puha kapunál a gyenge, de értelmezhető munka formatív F-peula-javaslatot váltson ki, ne „nem teljesült” bukást. A „Még nem teljesítve” státusz az üres/értelmezhetetlen beadásé marad; a rubrika szerinti fejlődési cél külön, nem kapuzó jelzés. Az értékelés helyét és hozzáférését dokumentálni kell. |
| **ERT-9** | **A** · alapjavaslat | ASSIGN-M saját completion = SUBMITTED (beküldte); a tényleges szakmai CONFIRMED állapot külön GATE-CP-n álljon be. Egy „Receive a passing grade” kipipálása az Assignmenten nem helyettesíti a kritikus rubrikasorok és a mentor-konfirmáció összetett feltételeit. A korábbi pontküszöb nem változik. |
| **ERT-10** | **F** · feltételes | Az M3 kritikus itemsor módosításához egyszerre kell írásos projektgazdai kapudöntés és Memuna-jóváhagyás; az értékelési felelős kalibrál. Az ITEM 10-et addig ne emeljük kritikusnak, amíg nincs küszöbhatás-vizsgálat és Memuna szakmai állásfoglalás; megmaradhat fontos, de nem automatikusan blokkoló lefedettségi tételként. |
| **ERT-11** | **A** · alapjavaslat | A belépőkvíz nyilvánvaló nyelvi hibái („completion-állapot”, alanyegyeztetés) javíthatók a kérdések helyességének és a ✅ elhelyezésének változtatása nélkül; értékelési QA a SIG-1 körében. |
| **ERT-12** | **A** · alapjavaslat | Tárolt, névhez kötött M1.3 mini-SBI-ben kizárólag fiktív helyzet legyen. Az M1.4-es precedens, a HUM:462 és az adatminimalizálás ezt támogatja; a leckeszöveg, HUB, MAN és érintett NAR-spec egy fix packban igazodik. DPO-vétó és szükséges hanggyártás külön. |
| **ERT-13** | **A** · alapjavaslat | SBI rövid válaszának kánoni hossza 2–3 mondat legyen a Program terv és a rubrika jelenlegi, többségi mintája alapján. A mondatszám csak instrukció, ne váljon pontozott küszöbbé. |
| **ERT-14** | **A** · alapjavaslat | Az M1 KAPU tartalmazzon kimondott értékelői szabályt a mintaválasz szó szerinti visszaadására: az adaptációt és helyzetre szabást értékeljük, a bemásolás önmagában nem kompetencia. A kapuval azonos példát cseréljük független, nem kulcsolt mintára, de a rubrikát az értékelési felelősnek kell jóváhagynia. |
| **ERT-15** | **F** · feltételes | Ugyanazért az enyhe minősítő szóért csak egyszer járjon levonás. A viselkedést objektíven leíró B-sor hordozza az adott tartalmi hibát, a hangnem külön csak önállóan igazolt kommunikációs hibánál módosulhat. A két horgony értékelői példáit egységesíteni és kalibrálni kell. |
| **ERT-16** | **F** · feltételes | Az S („helyzet”) jó teljesítésének egyértelmű olvasata: idő VAGY hely (mindkettő lehet) ÉS a helyzet releváns szakasza. Kerüljön zárójelezett, pontozói példákkal megadott szabály a rubrikába; a bizonyítottan eltérő konstruktumválasztást csak az értékelési felelős hagyhatja jóvá. |
| **ERT-17** | **A** · alapjavaslat | A „megtartható kapcsolatban” zárójel magyarázó cél legyen, ne új, előre nem tanított külön pontozási dimenzió. Az értékelő a viselkedésre, nem a személy minősítésére adott visszajelzést méri, a kapcsolat megőrzése ennek pedagógiai oka. |
| **ERT-18** | **F** · feltételes | Az M2.4 pontozatlan önbevalló polljai maradjanak követésmentesek; ne generáljanak fantom „grade”-et. A továbblépést külön igazolt, nem érzékeny completion-jelhez vagy a megtekintéshez kell kötni. A (2a) egyszerű út az első választás, ha a manifest lánca megőrzi a tanulási célt; cél-Moodle runtime próba nélkül ez nem kész. |
| **ERT-19** | **F** · feltételes | Az M2 identitáskör-módszertanában az „ÉN” a középpont, a „legalább 3 kör” ezért három további rétegként értelmezendő; viszont ez a jelenlegi rubrika szigorítását okozhatja. A módosított követelményt előre kommunikálni és a modulgazda/értékelési felelős által aláíratni kell, meglévő beadást visszamenőleg nem büntetünk. |
| **ERT-20** | **F** · feltételes | Ha a DPO nem engedélyezi a szabad szöveg rendszeres olvasását, a M2:244 mutató szűnjön meg; ne erőltessük a „2 vagy 3” számot adatkezelési kényszerrel. Ha marad, a programvezető válasszon előre rögzített, legalább 2-es formatív célértéket, és csak jogszerű aggregátumból számoljon. |
| **ERT-21** | **F** · feltételes | Az M3 R1 fogadjon el a kánoni értelemben releváns biztonsági/határhelyzetet, ne csak erőszakos krízist; R2-t az olyan helyzetekben, ahol nincs feltárás vagy titoktartási ígéret, ne büntető mechanikával alkalmazzuk. A rubrika ne buktassa meg a saját sablonját követő résztvevőt; kalibráció Memuna + értékelési felelős. |
| **ERT-22** | **A** · alapjavaslat | Az M3 blokkoló R4 sorban csak gyermekvédelmi eljárási kritérium (nem nyomoz, nem konfrontál, megfelelő jelzés) legyen. Az életszerűség kerüljön egy nem blokkoló minőségi sorba, mert az irreális, de biztonságos válasz nem azonos veszélyes eljárással. |
| **ERT-23** | **F** · feltételes | Többértelmű kvuca-jelenetnél dokumentáltan több helyes párosítás legyen elfogadható; egyetlen kulcs csak akkor maradjon, ha a megfigyelhető jelek azt egyértelműen alátámasztják. A módosítást a M3 modulgazda és az értékelési felelős itemenként validálja. |
| **ERT-24** | **F** · feltételes | M4 Kapu 1 alacsony teljesítményét ne állítsuk be önkényes P/F küszöbként. Addig személyre nem szabott, összesített téma-visszajelzés legyen; ha a programvezető egyéni felzárkóztatási jelzést kíván, előbb rögzített feladatszerkezet, validált értékhatár, hozzáférés és Moodle runtime teszt kell. |
| **ERT-25** | **F** · feltételes | Az M4.3 K3 kérdésszárát és a kulcsolt opciókat egy szakmai értelmezés körül tegyük egyértelművé; elsőként a kérdésszár pontosítása és a meglévő helyes válasz megtartása preferált. Ha szakmailag másik válasz helyes, a ✅ változása külön explicit lektori és projektgazdai döntés legyen. |
| **ERT-26** | **A** · alapjavaslat | Az M5 kapu elsődleges pontozási egysége a rubrikakritérium a teljes táblázat alapján, nem minden táblázatcellára külön kötelező mikropont; a PT és HUB ugyanezt írja. Soronként legyen látható módszertani indok, de egy tanulástani eszköz nem feltétlenül kell minden sorba. Értékelési kalibráció. |
| **ERT-27** | **A** · alapjavaslat | Az M5 R4 gyakorlásfogalma maradjon a Glosszárium tágabb, meglévő definícióján; a felidézés és az elosztott gyakorlás fontos példák, de önkényesen ne szűkítsük erre a rubrikát. |
| **ERT-28** | **F** · feltételes | Az M5.2 SLIDE 8 helyes opciója a „feladat–kvuca–módszer–cél” logikát kövesse úgy, hogy a kiválasztás valóban a tanított döntési utat méri. A ✅ pozíció csak akkor maradhat, ha a szemantika ténylegesen helyes; ellenkező esetben explicit új itemdöntés, nem kozmetikai szövegezés. |
| **ERT-29** | **A** · alapjavaslat | Az M5.4 SLIDE 6 „Igaz rám / Még nem” önbevallás ne legyen pontozott helyes–hibás kérdés. Mindkét válasz legitim önellenőrzési állapot, a completion a lecke megtekintésén vagy más semleges eseményen alapuljon. |
| **ERT-30** | **F** · feltételes | Az M5 KAPU Q12 opciói ugyanabból az ágensnézőpontból szóljanak; a ✅ C jelentése változatlan legyen. Elsőként csak a C mondatot igazítanám az egyes szám első személyű kontextushoz, a szakmai szerző/értékelő jóváhagyásával. |
| **ERT-31** | **A** · alapjavaslat | Az M6 diagnosztikus szcenárió-kvíz beküldése legyen kötelező completion, de az eredmény ne blokkolja az elsődleges éles játéklapkaput. Az önellenőrzés hibáira lehessen újrapróbálni, az „ajánlott 80%” ne váljon át rejtett bukási szabállyá. |
| **ERT-32** | **F** · feltételes | A biztonságkritikus R4 „Oké” horgonya az adott eszköztípus tanított kötelező minimumait kérje (kontaktjátéknál akadálymentes tér, stop-jelzés, tempó, kísérés; szenzitív helyzetnél passz és felnőtt). Ez rubrikaváltozás, ezért ne implementáljuk értékelési/Memuna kalibráció nélkül. |
| **ERT-33** | **A** · alapjavaslat | Az M6.B társas visszajelzése maradjon formatív, pontozás nélküli („ma nem pontozunk”); a végső rubrikával a képző értékel, a stáb egymás között kalibrál. A HUB/PT „társas pontozás” kifejezéseit a tényleges folyamatra pontosítsuk a projektgazda engedélyével. |
| **ERT-34** | **F** · feltételes | A 2. item tartalmi duplikációja helyére készítsünk azonos nehézségű Kivsza-korú, korosztályi illesztést mérő új itemet, és előzetesen validáljuk; addig a meglévő kvízt ne hirdessük teljes korosztályi lefedettségűnek. Az itemszám és küszöb csak jóváhagyással változhat. |
| **ERT-35** | **A** · alapjavaslat | A M6 4. diagnosztikus kvízitem egyedüli helyes elvének legalább minimális változata kerüljön az összes tanuló által garantáltan látott kötelező forrásba. Az opcionális Branching Scenario ág nem lehet az értékelt ismeret egyetlen tanítási helye. |
| **ERT-36** | **F** · feltételes | Az M6 11–12. tétel azonos gondolkodási elvet más, fiktív helyzeten kérjen számon, ne szó szerinti leckememóriát. A 12. item érzékeny, önfeltárást hívó megfogalmazása csak GYV-18 döntése után javítható; biztonsági veto megtartandó. |
| **ERT-37** | **A** · alapjavaslat | Az M6.B közös páros munka lehet formatív vázlat, de az éles LMS-M6-05 kapun minden résztvevő önállóan véglegesít és nyújt be egyéni játéklapot. A társproduktum önmagában nem bizonyít egyéni kompetenciát. |
| **ERT-38** | **A** · alapjavaslat | Z.4 „Teljesítve”: a tartalom legyen minimálisan értelmezhető, tényleges beadás, de a három részes ideális reflektív szerkezet legyen formatív útmutató, ne új, rejtett bukási küszöb. Az adatvédelmi szempontból szenzitív részek passzolhatók, a tanulói követelmény előre ismert. |
| **ERT-39** | **A** · alapjavaslat | Z.A záró peula legyen ajánlott, értékes közösségi esemény, ne a Moodle program completion kötelező feltétele; ezt a PT és MAN jelenlegi kritériumai alátámasztják. Hiányzó jelenlét ne akadályozzon minden egyéb kaput teljesítő tanulót. |
| **ERT-40** | **F** · feltételes | M7 Q11/Q14 Multi-Select: a kapuküszöb darabszám-alapú (legalább 12 teljesen helyes item / 14), ne átszámított részpontszázalék. Ha van validált minden-vagy-semmit Moodle kérdéstípus, használjuk; egyébként manual GATE-CP megerősítés, negatív teszttel 11 teljes + 2 részleges esetére. Ne engedjen át „Grade to pass 12” önmagában. |
| **ERT-41** | **A** · alapjavaslat | A hiányzó M7 kipróbálási vállalás/AI-megjegyzés esetén kérjünk kitöltési pótlást és értelmezhető, nem értékelői visszajelzést, de ne buktassuk a kaput és ne tiltsuk a szakmai v2 értékelését. Így összeegyeztethető a „figyelembe vesszük” és a „nem blokkol” kánon. |
| **ERT-42** | **F** · feltételes | Az M7 R8-ban különítsük el az AI-másolat pedagógiai problémáját és a harmadik személy azonosítható adatának biztonsági/adatvédelmi kockázatát. Az utóbbinál a beadás ne legyen automatikusan elfogadott magas összpont mellett sem; legyen DPO-jóváhagyott korlátozás, incidensértékelés, adateltávolítás és javító leadás. Rubrika és kapuhatás formális döntést igényel. |
| **ERT-43** | **F** · feltételes | SMART R1 2-es szinten legyen valóban ellenőrizhető jel/kimenet, ne csupán határidő: különben a mérhetőség tanított elemét nem értékeljük. A követelmény értékelési szigorítás, ezért csak előzetes egyértelmű tanulói tájékoztatóval és projektgazdai jóváhagyással léphet hatályba. |
| **ERT-44** | **F** · feltételes | Az M7 R3 egyetlen konstruktuma a peula koherens belső íve legyen; a három fázis a strukturáltság megfigyelhető bizonyítéka, ne külön még egyszer pontozott dimenzió. Ha a szerző két kompetenciát akar mérni, az már külön rubrikafejlesztés és kalibráció. |
| **ERT-45** | **A** · alapjavaslat | Az M7 Peula v2-re ne találjunk ki univerzális 45 percet: a valódi célcsoport és helyzet szerint tervezett időkeret betarthatóságát pontozzuk; a 45 perc csak példa lehet. A PT-ben szereplő 60–90 perces programkeretekkel így nincs ellentmondás. |
| **ERT-46** | **F** · feltételes | M7.1 Fill in the Blanks numerikus helyein csak akkor pontozzunk, ha cél- és kontextusfüggően meghatározható, előre publikált elfogadott válaszhalmaz vagy tartomány. Ha a „reális” szabad mérlegelést jelent, legyen pontozatlan, formatív visszajelzéses feladat; semmilyen numerikus varázsküszöböt ne gyártsunk. |
| **ERT-47** | **A** · alapjavaslat | Az M7 (C) „átláthatóság” kifejezést bontsuk két ellenőrizhető alpontra: ki tud a felügyeletről/kockázatról, és hogyan közlik a helyszín, sötétedés és hazajutás feltételeit a résztvevőkkel/szükséges felelőssel. Csak a már tanított követelmény legyen pontozott; Memuna ellenőrzés. |
| **ERT-48** | **A** · alapjavaslat | Az M7 AI-jártassági gyakorló kérdése legyen Page-be vagy CP-be ágyazott, lehetőleg nem követett, nem külön pontozott H5P; a kötelező tanulási tartalom megtekintését a befogadó activity completionje jelölje. No-AI azonos teljesítési út; külön H5P gradebook-nyom ne keletkezzen csak a szemléltető gyakorlatért. |
| **ERT-49** | **A** · alapjavaslat | Az M7 (C) kritériumából vegyük ki az „eltérő létszám” olyan elvárását, amely nincs megtanítva, és az M7.3/SLIDE5 itemekben sincs következetesen szerepeltetve. Alternatíva csak új kötelező tanulói tartalommal és jóváhagyott assessment-módosítással; a legkisebb helyes változás a rubrika szűkítése. |
| **ERT-50** | **A** · alapjavaslat | Az M7 v1 operációs táblájának minimális terjedelme 3 értelmes sor legyen; 4 sor ajánlott, de nem kötelező. A kétértelmű „min. 3–4” helyett egyetlen világos szám szerepeljen az M7.4-ben és a KAPU-ban. |

## 6. Tantervi architektúra — PRG-1–17

Kevesebb gépezet; a meglévő modul, peula és példák visszafogott, konzisztens fejlesztése. Új tartalom csak valódi szükségletre.

| ID | Ajánlás típusa | Javasolt konkrét döntés / indok |
|---|---|---|
| **PRG-1** | **A** · alapjavaslat | Az ütemezett 45 perces peulablokkok és a központi naptár maradjanak; a modulgazdák tételes vágási tervvel csökkentsék a túlcsorduló lépéseket, a védett biztonsági/reflexiós és kötelező feldolgozó lépések rövidítése nélkül. M5.1-nél a 15–20 perc és a 9–13 percre összegződő részidők tényleges újrabecslése vagy a metaszám visszaigazítása kell, nem kitalált „átmeneti” percek. |
| **PRG-2** | **A** · alapjavaslat | Kimeneti kompetenciának csak a ténylegesen gyakoroltatott/mérhető teljesítményt nevezzük; ahol nincs ilyen, inkább szűkítsük a hub-ígéretet (C opció, alap A), mint hogy minden hiányra új activityt építsünk. Új tartalom csak tételesen bizonyított nevelési szükség és PRG-4 szerzői jóváhagyás esetén. |
| **PRG-3** | **A** · alapjavaslat | A tényleges peulafájlban végrehajtható, időbe férő lépés legyen a részletes igazságforrás; a hub/meta/kártya-spec azzal egyezzen. Ha egy fontos, korábban ígért tanulási cél elveszne, azt a modulgazda kifejezetten PRG-4 fejlesztésre jelölheti, nem automatikus bővítésre. |
| **PRG-4** | **F** · feltételes | Egy összefogott, célzott /course-develop csomag készüljön a kötelező, hiányzó feedback- és akadálymentesítési tartalomra, majd szakaszos szakmai QA. Nem kell egyszerre minden opcionális új játékot megírni. Új biztonsági/értékelési item csak Memuna/értékelési gazda által jóváhagyott tervből; az RA 125 visszajelzési minimumát ne gyengítsük. |
| **PRG-5** | **F** · feltételes | Minden kötelező F-peulához legyen 1–5 főre előre leírt, azonos kompetenciát fejlesztő változat. Hiányzásnál dokumentált pótidőpont vagy jóváhagyott, rövid egyéni mentoros út legyen, mindig a javító próbálkozás előtt; 1:1 kiskorúval csak a meglévő HUM-SAFE-02 kivétel szerint. A programvezető rögzítse a kapacitást és a pótlási felelőst. |
| **PRG-6** | **F** · feltételes | Az M0 diagnosztikus belépőkvíz ne kapjon kitalált formális megerősítési kaput. M7-nél a függőben lévő kvízeredmény ne szorítsa ki a v2 határidejét: indokolt egyéni hosszabbítás és meglévő F-peula utáni 1+1 javítás. Z-nél a mentor jelölje ki a javító időpontját, a teljesítés várja be az eredményt; a Z.3 v1-út azoknak is működjön, akiknek az M7 v2-je még nincs kész. Konkrét dátumot csak a tényleges naptárból írjunk. |
| **PRG-7** | **A** · alapjavaslat | Az M5/M6 diagnosztikus eredményből a mentor kapjon támogató, nem kötelező beavatkozási ajánlást; a hallgatót ne büntesse alacsony diagnosztikus pont. A programvezető a meglévő tananyagból ismétlést vagy beszélgetést rendelhet, új tanulási modult ne építsünk automatikusan. |
| **PRG-8** | **A** · alapjavaslat | A peulák szerepeljenek a Moodle-kurzusban tanulói felkészítő leíróelemként, de a képzői forgatókönyv ne legyen résztvevői anyag; az F-peulák külön látható, releváns szakaszt és szükség esetén kézi, megalapozott részvételi jelölést kapjanak. A manifest ennek megfelelően bővüljön az új verzióhoz, nem a pilotba visszamenőleg. |
| **PRG-9** | **F** · feltételes | M1.2 SLIDE 5 Drag & Drop: nem szükséges, legyen csak húzásmentes, rádió-/kattintásos út. M2.1 identitáskör: maradjon a CP-ben integrált, nem követett reflexió, tényleges tárolás-ellenőrzéssel. M3.3 négy illusztrációja csak akkor épüljön be az elágazás UTÁN, ha bizonyított pedagógiai szerepe van, különben maradjon ki (SAFE-1 és passzjog előtt vizuális kitettség sem lehet). |
| **PRG-10** | **A** · alapjavaslat | M4.B feedbackben az SBI forma legyen opcionális, de Megfigyelés → Hatás → Következő lépés szerkezet kötelező. M5 produktumnál a valós kvuca-adat nem kötelező: fiktív profil egyenértékű. Zárókörben mindenki kapjon lehetőséget megszólalni, de a passz ugyanúgy teljes értékű részvétel. |
| **PRG-11** | **A** · alapjavaslat | Egységes skálázási szabály: 8–20 főnél alapból 3–5 fős csoportokat képezzünk, a csoportszámot és kártyakészletet a létszámhoz igazítva. Minden peula-specbe kerüljön az adott célhoz ténylegesen szükséges eset-/kártyadarabszám és az egyenlő részvétel ellenőrzése. Ez működési alapjavaslat, nem új kánoni létszámkorlát. |
| **PRG-12** | **F** · feltételes | Az M3.B 4. esetkártyáját használjuk előre megírt fiktív példaanyagként, és a felnőtt-gyanúsítottas eset kulcskülönbségét a képző akkor is mondja el, ha egy időhiányos lépés kimarad. Ne rögtönözzünk valós gyermekvédelmi történetet. Memuna review szükséges a konkrét forgatókönyvre. |
| **PRG-13** | **A** · alapjavaslat | Az M5.A és M6.A sarokjátékokhoz legyen mozgás nélküli, helyben jelzős/kártyás egyenértékű részvétel, a passzjoggal. A cél a vélemény és megértés kifejezése, nem a fizikai sarokba állás; a modulokban már van ehhez mintaszöveg. |
| **PRG-14** | **F** · feltételes | Generatív AI eredetet csak szerzői/provenance bizonyíték alapján jelöljünk, soha ne tippeljünk. Az M7.1 no-AI alternatíva legyen ugyanabban az online leckében letölthető/nyomtatható promptkártya, azonos fejlesztési céllal és completionnel. A tényleges médiaeredetet a szerző vagy médiafelelős igazolja. |
| **PRG-15** | **F** · feltételes | M2.B 3. helyzetének lezárását meglévő kánoni példából és önkéntes reflektáló kérdéssel készítsük el; M5.1 SLIDE4 1./4. kulcsát csak a formális–nonformális–informális definícióval egybevetett szakmai lektor döntése után módosítsuk; M7.B A/B sarokjátéka maradhat nem pontozott, tanári összegzéssel, amíg nincs validált, egyértelmű helyes kulcs. |
| **PRG-16** | **F** · feltételes | A kilenc szerzői jelentéskérdésre a legkisebb értelmező javítás: M1 SBI-S határozói sablon; M1.A-n új cetli csak önkéntesen; M2 „megtartás” = támogató figyelem, nem titoktartási ígéret; M3.A a képző választ 3 kártyát; M4.4 „puha” = nem blokkoló fejlesztő visszajelzés; M6 nem valódi veszélyhelyzet eljátszása, hanem fiktív eset; M7.4 v1-ben a megfelelő meglévő szakaszba emelés; M7.B „átjárás” egyértelmű részvételi/álláspontváltási instrukció; Z.3 „túl kicsi” csak akkor hibapélda, ha konkrétan megmagyarázott. A szerző szándékát megerősítő rövid QA kell, nem új teljes review. |
| **PRG-17** | **F** · feltételes | Az M0.1 SLIDE 5 kíváncsiság/félelem, illetve „1–2/2–3 modul” kérdését most ne döntsük el puszta ízlésből. CC-04 szerint tényleges pilot-visszajelzéssel együtt kell választani; addig a változat izolált, nem módosítjuk a futó pilot tananyagát. |

## 7. Moodle, H5P és hozzáférhetőség — LMS-1–8

Core, ellenőrizhető és adatminimalizáló utak az alapok. Egy plugin vagy H5P-beállítás létezését sem szabad célverziós teszt nélkül készpénznek venni.

| ID | Ajánlás típusa | Javasolt konkrét döntés / indok |
|---|---|---|
| **LMS-1** | **F** · feltételes | Az egyenértékű online szöveges és fájlfeltöltéses út maradjon. Elfogadott fájltípusok a tényleges akadálymentes sablonhoz igazítva (például .docx, .odt, .pdf), alapból legfeljebb 1 fájl; képfeltöltés/screenshot ne legyen szükséges vagy ösztönzött. A Z.4 videó csak külön, DPO által engedélyezett profilon szerepelhet. Cél-Moodle beállítás- és a11y-ellenőrzés kell. |
| **LMS-2** | **A** · alapjavaslat | Az M3.2/M3.4 Drag & Drop mellékutakat hagyjuk el, ha a húzásmentes kártyás/rádiógombos út ugyanazt a tanulási célt és visszajelzést adja. A WCAG 2.2 AA 2.5.7 szerint húzásnál egyetlen mutatóval, húzás nélküli alternatíva kell; a felesleges kétféle implementáció csak növeli az eltérés kockázatát. |
| **LMS-3** | **F** · feltételes | M5.3 késleltetett felidézéshez rövid, adatminimalista CP/PAGE út javasolt: a személyes felidézés a tanuló saját jegyzetében történik, külön pontozott önellenőrző itemekkel csak akkor egészítjük ki, ha erre van jóváhagyott tartalom. Üres CP-t ne állítsunk be hamis „Receive grade” completionnek; a valós H5P és az LMS-M5-07 manifest tesztje dönti el, kell-e más profil. |
| **LMS-4** | **F** · feltételes | Az M6 játéklap kapu megállapítását a rubrikasorok szemantikai értékelése és a GATE-CP hordozza, ne puszta Moodle-normalizált összpont. Ha megőrizzük az 1/2/3 pontokat, a Grade type / Maximum grade / rubrikaminimum és a 10 pontos „csupa Oké” negatív/pozitív teszt legyen dokumentálva. A rubrikapontértéket értékelői döntés nélkül nem vetítjük át 0/1/2-re. |
| **LMS-5** | **F** · feltételes | Az M7.3 Zmán Kvucá-checklistet inkább Moodle core Page/CP + letölthető munkalap formában, tanuló-lokálisan építsük, külön tárolt komment és plugin nélkül; a completiont a befogadó tanulási szakasz viszi. Ha a checklist maga kötelező és minden pipát strukturáltan kell ellenőrizni, új manifest/activity/DPObizonyíték kell, de a „szabad pipa nélkül hagyni” szabályt nem sértheti. |
| **LMS-6** | **A** · alapjavaslat | A M7.4 3–4 terület kijelölése legyen pontozatlan, saját jegyzetes lista, nem minden választ „helyessé” programozó H5P Multiple Choice. Nincs pedagógiai helyes válasz; a Completiont az oldal vagy összefoglaló dia biztosítja, ne a véleménykiválasztás. |
| **LMS-7** | **F** · feltételes | Elsőként a Program terv kánoni M7.2-DIA-01 alt-szövegét használjuk, de csak akkor, ha a diagram lényegi információját ténylegesen közvetíti. Az akadálymentességi felelős ellenőrizze, hogy a rövid alt és a látható kísérőszöveg együttesen teljes értékű-e; nem az alt hossza, hanem a funkciója a döntő. |
| **LMS-8** | **F** · feltételes | Az AI-segédet kezdetben képző által közvetített, opcionális, személyes adat nélküli útban engedném (C). Közvetlen tanulói chatbot/plugin csak krízis-, adatkezelési, jogosultsági és no-AI parity review után. A H5P/Moodle course completion ne függjön az AI használatától. |

## 8. Narráció és média — VO-1

A hanggal és leirattal való egyezés a mérce; a valóban kimondott szöveg változása hanggyártási függőség.

| ID | Ajánlás típusa | Javasolt konkrét döntés / indok |
|---|---|---|
| **VO-1** | **F** · feltételes | Egyetlen VO-fix pack legyen; a valóban kimondott szöveget módosító 6 blokkot újra kell renderelni és meghallgatni. A további 9 írásmódi/typográfiai blokkot csak dokumentált kiejtési azonosság, source hash és VO-gazda ellenőrzés után lehet régi hanggal tartani; kétség esetén újrarender. A két videó feliratát és leiratát külön hang–szöveg egyezésre ellenőrizzük. |

## 9. Technikai kivételek — TECH-1–2

Kerüljük a biztonsági őr szükségtelen kivételeit és a nem ellenőrzött, átfogó Git-módosításokat.

| ID | Ajánlás típusa | Javasolt konkrét döntés / indok |
|---|---|---|
| **TECH-1** | **A** · alapjavaslat | A jelenlegi gyermekvédelmi „minijelenet” tiltóőrét nem lazítanám globálisan. A legkisebb biztonságos megoldás elsőre az (A): a már működő „mini-jelenet” formát hagyjuk, a P2 helyesírási hibát dokumentált kivételként. Ha szerkesztői egység miatt mégis javítanánk, inkább „rövid jelenet” (D) három fájlban, mint széles fájl-szintű security-exemption; kizárólag tételes regression-test után. |
| **TECH-2** | **F** · feltételes | Az M6.1/M6.2 két címbeli/fájlnévi javítását elvégezném külön, review-olható change setként, az összes hivatkozás, két gépi útvonalkulcs, baseline-rename mapping, pin és generált média együttmozgásával. A git mv-t a tulajdonos futtassa a saját termináljában, a hookot nem kerülve meg; utána célzott selftest, invariáns és külön media commit. |

## A 16 bizonyíték- és jóváhagyási bejegyzés — nem döntések

Ezek **nem válaszolhatók meg kutatással úgy, mintha a jóváhagyás vagy teszt megtörtént volna**. Alább megadom a bizonyító minimumot és a tényleges jogosult felelőst.

| ID | Beszerzendő bizonyíték / elfogadási feltétel | Jogosult igazoló |
|---|---|---|
| **GYV-24** | Egyazon végleges SHA-ra szóló, datált „átnéztem” G1; SAFE-7 és valamennyi 1:1-kulcs explicit verdikt; akut út/segélyvonal friss ellenőrzése; tracker #1 lezárása linkkel | Memuna |
| **ADV-E1** | Activitynkénti DPO G2 QA: pontos adatmezők, hozzáférési szerepek (mentor/editor/manager/admin), megőrzés, export, xAPI/LRS, saved-state, backup, esetenkénti tartalékút. M0/M1-re prioritás | DPO/jogi felelős |
| **ADV-E2** | Teljes activity-szintű adatleltár, külső Google/papír/mentori jegyzet folyamatokkal, adatfeldolgozói és törlési renddel, „külön review” helyek rögzítése | DPO/jogi és programvezető |
| **ADV-E3** | HUM-PRIV-04 AI-kapcsolat tényellenőrzése: API, közvetítő, provider, naplózás, retention, hozzáférés, továbbítás, no-AI egyenértékű út; formális QA | DPO/jogi |
| **SIG-1** | M0 hét belépőkvíz-itemjének független értékelési QA-ja; az 1–2. itemnél gyermekvédelmi kontroll, dátummal és SHA-val | Értékelési felelős, 1–2.: Memuna |
| **SIG-2** | M3 ≥10/12 és kritikus Q2/Q4/Q7/Q9, M7 Q13 szakértői item- és küszöbmegállapítás (korábbi Q-PED-6 Angoff-elv átvezetése); 1–2 közös referenciaminta; kétszemes blokkoló döntési rend | Szakmai lektor, assessment, Memuna a gyermekvédelmi résznél |
| **SIG-3** | M3.4 kritikus követelmény megnevezése kulcsfelfedés nélkül; szöveg és valós tanulói review-options QA | Értékelési felelős + Memuna |
| **SIG-4** | M4 kvíz/rubrika/sablon és M5 kapu független lektori QA-ja az összes függő döntés alkalmazása után | Kijelölt szakmai lektor; M5 assessment QA |
| **SIG-5** | M5 AI-generált media assetenkénti emberi szakmai és eredetjelölési ellenőrzés; release-record referencia | Szakmai lektor |
| **SIG-6** | M6 média jogosultságok: J3, H-11, AI Act minősítés, J2, V1, V3/E-8, R2/R3 és minden releváns RIGHTS-EVIDENCE kontroll; az érintett asset addig fallbacken | Jogi jogosult, Memuna, DPO, szerző |
| **RT-1** | Valódi technikai/program/mentor/Memuna kontakt, ügyfél- és tanulói nézetben helyesen megjelenik; nyitvatartás, szerepcímke, elérhetőség | LMS-gazda + programvezető |
| **RT-2** | M0/M1 completion/unlock/attempt/GATE_CP, védett és hibás negatív esetek; N-M1-04 saját jegyzetes/no-input alapút; H5P saved-state, xAPI/LRS és jogosultsági visszaolvasás a célverzión | Moodle/LMS-gazda, a11y szerep, DPO a saját részén |
| **RT-3** | M4 kész kapu/completion/a11y és notification teszt; tényleges M4_ASSIGN dátum és az elkülönített learner-scope | LMS-gazda + programvezető + a11y |
| **RT-4** | M6.4 Branching Scenario A → B → opcionális C → D → 6D → ZÁRÓ valós bejárása; kizárólag végponti completion, passz és érintés/húzásmentes működés | LMS-gazda + a11y |
| **RT-5** | M7 AI „store=false” és esetleges proxy/provider naplózások auditja, API és ZDR jogcím; no-AI út feladat-, grade- és completion-paritása | LMS-gazda + DPO |
| **RT-6** | M7.2/M7.3 minden párosítás billentyűzettel és egyérintéses kattintás/koppintás útján egyenértékű, azonos visszajelzéssel; mobil portrait teszt | LMS-gazda + független hozzáférhetőségi QA |

## Független kutatás — döntést befolyásoló megállapítások

Ez a rész **külső elsődleges forrásokból** származik. A fenti konkrét ID-k és kánoni kötöttségek a repository döntési csomagjából; az általános jogi/szakmai/technikai követelmények az itt felsorolt forrásokból kerültek kontrollálásra. Az idegen forrásokat **nem helyettesítem automatikusan** a helyi szabályzattal.

### Adatvédelem és gyermekek

- Az EDPB GDPR 25. cikkhez kapcsolódó útmutatója szerint az adatvédelem már tervezéskor és az alapbeállításoknál érvényesítendő. Ez alátámasztja a nem kötelező önfeltárási adatok ki nem gyűjtését és az alapértelmezett legkisebb hozzáférést; **nem ad automatikus GDPR 9. cikk szerinti jogalapot** különleges adatokhoz.\
  [EDPB — Guidelines 4/2019, Article 25](https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en)
- A vallási, világnézeti, identitás- és kis csoportban visszaazonosítható információk esetén a „névtelen” és a „nem tartalmaz teljes nevet” nem ugyanaz. Ezért az ADV-5/8/9 irányadó alapelve a kockázatos szöveg el nem kérése és azonosítási kockázat tényleges felmérése.\
  [GDPR (EU 2016/679), Articles 5, 9, 25](https://eur-lex.europa.eu/eli/reg/2016/679/oj)

### Moodle, H5P és pontozás

- A Moodle **Activity completion**, a **Grade to pass**, az **Assignment submission** és a képzés pedagógiai **GATE_CONFIRMED** szabálya eltérő állapotok. Az ilyen szabályok összevonása hibás felszabadítást vagy megtévesztő bukást okozhat.\
  [MoodleDocs — Activity completion settings](https://docs.moodle.org/en/Activity_completion_settings)
- A H5P próbálkozás és az xAPI/LRS eseményrendszer ténylegesen tárolhat/forwardolhat tanulónkénti válaszjeleket, de a konkrét helyi Moodle plugin / H5P verzió konfigurációjában kell ellenőrizni. Az, hogy nincs értékelés vagy látható szövegmező, **önmagában nem adatmentességi bizonyíték**.\
  [MoodleDocs — H5P activity](https://docs.moodle.org/en/H5P_activity) · [H5P — xAPI](https://h5p.org/x-api)
- A Feedback activity „analysis page” és a beküldési értesítés külön megjelenítési/adatkezelési döntés. Kis kohorsznál a statisztikus összesítés is visszaazonosíthatóságot okozhat, ezért ADV-15 alapértelmezésként mindkettőt kikapcsolja.\
  [MoodleDocs — Feedback activity settings](https://docs.moodle.org/502/en/Adding/editing_a_feedback_form)

### Gyermekvédelem, jog és segélyvonalak

- A `116 111` gyermek/fiatal lelkisegélyhez kapcsolódó szám, a `116 000` **elsődlegesen az eltűnt gyermekek** ügyében fenntartott európai hotline (a Kék Vonal a szülők segítségkérési lehetőségeként is megnevezi). A `112` az általános sürgősségi szám. A tananyagban sem a szolgáltatás funkcióját, sem a tényleges elérhetőségi adatot ne találjuk ki; a Memuna a kiadás napján ellenőrizze a helyi működést.\
  [NMHH — 116-os harmonizált közérdekű szolgáltatások](https://nmhh.hu/cikk/115/A_116_kezdoszamu_harmonizalt_kozerdeku_szolgaltatasok_szamainak_hasznalata_es_kijelolese) · [Kék Vonal](https://kek-vonal.hu/)
- A magyar **Btk. 209/A. §** nem egyszerűen azt mondja, hogy „minden gyermekvédelmi jelzés legfeljebb három munkanapon belül kötelező, különben bűncselekmény”. A rendelkezés a **Gyvt. 17. § (4a)–(4c)** szerinti speciális, kiemelt veszélyeztető okkal kapcsolatos kötelezettségekhez kötődik. A szervezet jogállása és szerepei a jogász vizsgálatát igénylik.\
  [Nemzeti Jogszabálytár — 2012. évi C. törvény](https://njt.hu/jogszabaly/2012-100-00-00) · [1997. évi XXXI. törvény](https://njt.hu/jogszabaly/1997-31-00-00)

### Pedagógia és hozzáférhetőség

- A **WCAG 2.2 AA 2.5.7** megköveteli, hogy a húzásos művelethez legyen húzás nélküli, egyetlen pointerrel használható alternatíva, ha az interakció nem lényegénél fogva húzás. A billentyűzetes út önmagában nem garantálja a teljes 2.5.7 megfelelést.\
  [W3C WAI — Dragging movements](https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements)
- A **CAST UDL** többféle részvételi és kifejezési útját figyelembe véve a passz és a fiktív példa a személyes kitárulkozási kényszer alternatívája lehet; de a megmért biztonsági kompetenciának az alternatív úton is értékelhetőnek kell maradnia.\
  [CAST — UDL Guidelines](https://udlguidelines.cast.org/)
- A **SAMHSA trauma-informed** megközelítésében a biztonság, bizalom és választási szabadság támogatja, hogy a személyes krízis megosztása ne legyen értékelési kényszer.\
  [SAMHSA — Trauma-informed approach](https://www.samhsa.gov/)

## Lényeges eltérések a korábbi döntési csomag ajánlásaitól

1. **TECH-1:** a döntési csomag fájl-szintű automatikus kivételt javasol a „minijelenet” tiltóőrben. Én **nem engednék új technikai biztonsági kivételt egy P2 helyesírási kérdésért**; előbb (A) státus quo, szükség esetén a világos „rövid jelenet” szókapcsolat (D), külön diff- és gyermekvédelmi QA-val. Ez egy tudatosan konzervatív eltérés.
2. **LMS-6:** a nem pontozott, személyes fókuszválasztó alapvetően **nem jól modellezhető értékelési Multiple Choice-ként**. Inkább a tanuló-lokális, beviteli elem nélküli lista/jegyzet a default, amíg a célverziós teszt nem bizonyít egyenértékű, tárolásmentes választót.
3. **GYV-4/GYV-14:** a segélyvonalak funkcióját külső elsődleges forrás alapján pontosítanám; a 116 000 nem általános krízisvonal.
4. **ERT-40:** a ≥12/14 **teljesen helyes item** nem ugyanaz, mint 12 pont részpontozásból; az éles kapunak csak a ténylegesen jóváhagyott itemszintű küszöb adhat megbízható eredményt.
5. **ADV-11:** közös eszközön inkább adatmentes működés az alap, ne abban bízzunk, hogy a kézzel megígért törlés mindig hiánytalan.

## Javasolt végrehajtási sorrend

1. **Pilotkockázat jelenlegi állapota:** az M0/M1 tényleges Moodle activityk nyitottságát és adatfolyamait ellenőrizni kell. Ez nem helyettesíthető a Git diff-fel.
2. **Projektgazda által igazolható javaslatok:** az itt `A` jelölt javaslatokat és az `F`-ek konkretizált preferált irányát összefogott csomagban lehet véleményezni, ID-szinten naplózva. Ez a dokumentum önmagában nem jelenti az elfogadást.
3. **Memuna/DPO/jogász/assessment review:** az érzékeny és kifejezett jóváhagyási körök szerepkörönként, a már előkészített javaslattal és alternatívával kerüljenek ki, ne 125 külön rutinkérdésként.
4. **PR #30 maradjon draft; a main pilot-freeze megőrzendő.** A jóváhagyott, objektív javítások egy külön, auditálható PR-körben vagy a meglévő next-version ág külön commitjaiban alkalmazhatók, de csak a projektgazda erre adott felhatalmazásával.
5. **Staging és runtime QA:** a teljes Moodle-build kapacitásait ellenőrizni kell; 38 runtime és 19 környezeti mező hiánya nem tüntethető el dokumentációs szöveggel. Staging tesztelés technikailag párhuzamosan haladhat a döntésekkel, de release nem.
6. **Zárás:** a formálisan meghozott döntések pontos átvezetése, új célzott QA, média-VO-fix pack, szerepköri G1–G8, valódi go/no-go, majd a pilot időzítését tiszteletben tartó PR-merge.

### Mi nincs megalapozva pusztán forrásból?

- Valóban működő Memuna/helyettes ügyeleti rend és reakcióidő.
- A cél-Moodle/H5P pontos verziója, pluginjai, jogosultságmátrixa, xAPI/LRS, mentett állapot, backup és naplózás.
- A gyermekvédelmi/szervezeti jogalany aktuális jogállása és a hatósági jelzési szerepek.
- A pontos ágazati vagy helyi ideológiai szerzői szándék ott, ahol a szövegek ütköznek.
- A tényleges tanulói pilotforgalom, beküldött adatok és már megnyitott aktivitások.
- A formális jóváhagyók személye, jogköre és a meglévő aláírt release-bizonyíték.

**Minden további ilyen pontnál az itt adott irány a javaslat, nem az ellenőrzött valóság.**
