# Deep-Audit záró riport

> Iteratív deep-audit a `02 Tervezet` tananyagforráson, a
> [`DEEP-AUDIT-RUBRIC.md`](DEEP-AUDIT-RUBRIC.md) dimenziói mentén.
> Mód: **live** (éles javítás + commit) · Futás: **2 kör** · Konvergencia: **nem érte el**.
> Készült: 2026-06-19.

---

## 1. Vezetői összefoglaló

| Mutató | Érték |
| --- | --- |
| Mód | `live` (éles javítás, stagenként önálló commit) |
| Lefuttatott körök | 2 |
| Konvergált? | **Nem** — a 2. kör után is maradtak nyitott, megerősített eltérések, ezért a futás nem konvergáltként zárult |
| Megerősített találatok | 27 |
| Alkalmazott javítások (commit) | 15 |
| Review-be route-olt döntések | 83 |

A két kör során a kiértékelés → verifikálás → javítás ciklus **15 forrás-szintű javítást**
commitolt (auto-javítható, alacsony kockázatú szerkesztői eltérések). A maradék, emberi
döntést igénylő tételek **három külön review-dokumentumba** lettek route-olva, nem a
tananyagforrásba:

- **safeguarding-review → 46 tétel** ([`SAFEGUARDING-REVIEW.md`](SAFEGUARDING-REVIEW.md)) —
  gyerekvédelmi felelős / vezetőség (egy ponton mentálhigiénés szakember) hatásköre.
- **ideology-gate-review → 23 tétel** ([`IDEOLOGY-GATE-REVIEW.md`](IDEOLOGY-GATE-REVIEW.md)) —
  mozgalmi / Judaica szakértő + a magyarországi Somer vezetésének és a képzés-stábnak a döntése.
- **architecture-review → 14 tétel** ([`ARCHITECTURE-REVIEW.md`](ARCHITECTURE-REVIEW.md)) —
  kapu-építhetőség, cél↔item illeszkedés, curriculum-ív, akadálymentesség, adatvédelem.

**Miért nem konvergált?** A 27 megerősített találat zöme nem egyedi elírás, hanem
**rendszerszintű, több fájlon átívelő mintázat** — elsősorban két tengelyen:

1. **D2.1 (mérhető, ige-alapú tanulási célok):** modul-hubok kimeneti kompetenciái és a
   leckecélok következetesen „megérti / tudatosul / érzi / jobban látja” típusú belső
   állapot-megfogalmazásokat használnak, amit a rubrika kifejezetten tilt. Ez M0, M1, M2,
   M3, M4 modulokban ismétlődik — célblokk-szintű átírást igényel, nem pontjavítást.
2. **D5.1 / D5.2 / D5.5 (akadálymentesség):** a tartalmi ábrákhoz (Tuckman-görbe,
   Johari/identitás-körök, kvuca-jelenetek, timeline, screenshotok) nincs előírt
   alt-szöveg, a videó-narrációkhoz csak részleges / tömörített felirat-flag van, és a
   drag&drop / kártya-interakciókhoz hiányzik a billentyűzet-operálhatóság és célméret-előírás.
   Az M1.4 és M2.1 pozitív mintát ad — a többi lecke ehhez képest egyenetlen.

Ezek a mintázatok **szerkesztői konvenció-döntést** kívánnak (egységes cél-sablon és
akadálymentességi checklist minden leckére), ezért a 2. kör után is nyitva maradtak —
innen a „nem konvergált” státusz.

---

## 2. Megerősített találatok dimenziónként

Súlyosság: 🔴 = blokkoló (kritikus rubrika-kritérium sérül) · 🟡 = figyelmeztető.
Összesen **27** megerősített találat.

### D1 — Tartalmi minőség, provenance, forrás-épség

**🟡 D1.2 — Hiányzó emberi lektorálási nyom a biztonságkritikus fájlokon**
`M3/M3_ONLINE_LECKE/M3.3 – „Gyerekvédelem 101”` (és M3.4)
A két legmagasabb tétű, biztonságkritikus tananyagfájl (M3.3 „Gyerekvédelem 101”, M3.4
határok / red flag) NEM hordoz lektor-nevet / dátumot / verziónyomot vagy „gyerekvédelmi
felelős review szükséges” jelölést — holott a KAPU-fájlon (≈5. sor) ez explicit megvan.
A krízis-protokoll (112 / 116-123, disclosure-elvek) tényszerűen helytálló, de a jóváhagyási
nyom hiányzik. D1.2 kritikus: érzékeny tartalomnál legyen review-jelölés.

**🟡 D1.5 — Forrás-épség + AI-provenance (ChatGPT tracking-paraméter)**
`M3/M3_ONLINE_LECKE/M3.4 – „Do / Don’t madrichként”` (SLIDE 2 / 81. sor, SLIDE 5 / 234. sor; M3.3 SLIDE 4 / 235. sor)
Két hivatkozás `?utm_source=chatgpt.com` query-paraméterrel szerepel (nya.org.uk PDF és
centerforadolescentstudies.com). Ez egyrészt AI-provenance jelzés D1.3-jelölés nélkül,
másrészt a tracking-paraméter beégetése nem build-ready linkszöveg. Gyerekvédelmi / határ-
tartalmat alátámasztó forrásnál a hivatkozás épsége és emberi ellenőrzése elvárt.

### D2 — Tanulási célok (mérhetőség, Bloom-illeszkedés)

**🔴 D2 — Nem mérhető kimeneti kompetenciák és leckecélok (M1)**
`M1/M1 – „Vakfolt, tükör, feedback”` (2. szakasz, 20–38. sor; 3. szakasz leckecélok: M1.1 ~47, M1.2 ~63, M1.4 ~95)
A modul kimeneti kompetenciái és a leckecélok jelentős része nem mérhető, ige-alapú ILO,
hanem belső állapot („Érti, hogy…”, „Reálisabb, kevésbé fenyegető képe van a
visszajelzésről”, „Ráérezni, hogy nem látok mindent magamból”). Néhány tanulói mikrocél jó
(„megnevezed a 4 mezőt és saját példával illusztrálod” — mérhető), de a fő kompetencia-blokk
**BLOKKOLT-szintű D2.1 sértés**, és emiatt a 4. kompetencia („visszajelzéshez való viszony”)
mérés nélkül marad (D2.3).

**🔴 D2 — Nem mérhető célblokkok (M4)**
`M4/M4_ONLINE_LECKE/M4.1 – Mit üzen a testem_` (mikrocél 10–13; M4.2 mikrocél 12–14; Kimeneti kompetenciák 24–45)
Több cél belső állapot / megértés: „jobban látod, mit mond rólad…”, „Érti, hogy a kvuca a
testéből olvas”, „Felismeri alapvető nonverbális mintáit”. Van mérhető produktum (2 fókusz
megnevezése, 1 visszatükröző mondat), de a célblokk nem ige+megfigyelhető-cselekvés páros,
így a cél↔item Bloom-illeszkedés (D2.4) sem ellenőrizhető tisztán. Átível M4.1, M4.2 és a
KAPU §2 kompetencialistán.

**🟡 D2 — Nem ige-alapú modul- és peula-célok (M2)**
`M2/M2 – „Ki vagyok madrichként_”` (modulcél 16. sor „tudatosítja”; §2 38. sor „Érti, hogy”; M2.F 23. sor „Tisztábban látja”; M2.3 mikrocél 12. sor „jobban átlátod”)
A rubrika tiltja a „tudatosul / megérti / érzi” megfogalmazást, de a modulcél, több
kompetencia-fejléc és az M2.F / M2.3 célok pont ilyenek. Megfigyelhető produktum (1 oldalas
jegyzet, 3 mondat) létezik, de a cél nem ILO-ként jelenik meg a tartalom előtt.

**🟡 D2 — Alulfogalmazott mikrocélok az online leckékben (M2)**
`M2/M2_ONLINE_LECKE/M2.1 – identitás-körök` (M2.1 §1 10–14; M2.2 §1 10–15; M2.3 §1 10–16; M2.4 §1 10–14)
A tanulói mikrocélok „átlátod / jobban látod / el tudod kezdeni átgondolni” típusúak, miközben
a leckék TEVÉKENYSÉGEI magasabb szintet aktiválnak (megfogalmaz, viselkedésre lefordít,
megír). A cél **alulfogalmazza** a tényleges Bloom-szintet — alignment-rés a célblokk és a
feladatok között.

**🟡 D2.1 — Nem mérhető lecke-/modulcélok (M3)**
`M3/M3_ONLINE_LECKE/M3.1 – Tuckman-szakaszok` (Cél ~54; M3.2 mikrocél; modul-hub §2 kimeneti kompetenciák) és `M3.2 – 4 kvuca, 4 világ`
„megismeri / fejben tartja / megérti / érti”, „lesz egy gyors fejprofilod” — revideált Bloom
szerint nem megfigyelhető. A mérhető célok jó része megvan („be tudja azonosítani”, „felismer”,
„meg tud nevezni”), de a fenti megfogalmazások következetlenné teszik a célblokkot (M3.1, M3.2,
modul-hub). Constructive alignment-rés: a kvízek valójában magasabb (felismer / besorol /
alkalmaz) szintet aktiválnak.

**🟡 D2.1 — Belső-állapot mikrocélok (M0 online leckék)**
`M0/M0_ONLINE_LECKE/M0.1 – „Üdv a képzésben!”` (mikrocél 13–17; M0.2:13–18, M0.3:13–18, M0.4:14–19)
„egyben látod az éves ívet”, „jobban értem, mit jelent madrichnak lenni” (M0.2),
„biztonságosabban mozgok a Moodle-ben” (M0.3), „jobban értem… online is dugma ishitként”
(M0.4). „ért / lát / mozog” — D2.1 kritikus. Van mérhető elem („leírsz 1–2 mondatot”), de a
célblokk dominánsan nem viselkedés-szintű. Mind a 4 online leckére összevont megállapítás.

### D3 — Kapu- és item-validitás

**🔴 D3 — Inkonzisztens kapu-logika hub ↔ KAPU között (M6)**
`M6/M6 – „Toolbox_ játék, történet, kézműves & inkluzivitás”` (hub 6.2 vs. KAPU (B) rubrika R4/R5)
A hub 6.2 egyetlen összevont „Biztonság & inkluzivitás” hard-gate sort ír le, a KAPU viszont
KÉT külön hard-gate sort definiál (R4 Biztonság ÉS R5 Inkluzivitás). Ráadásul a hub
játéklap-rubrikájában „Somer-érték kapcsolódása” önálló sor, ami a KAPU-ban R1 részeként
szerepel. A mastery-kapu küszöbe eltér → kalibrálatlan értékelés (D3.8 explicit cut-score +
megkülönböztető szintek), mert nem egyértelmű, a peer/staff melyik rubrikát használja.

**🔴 D3 — Kereszt-fájl ellentmondás a kapu-konstrukcióban (M7)**
`M7/M7 – „Peula a papírtól a valóságig”` (§6 Kapuk 213. sor „kiegészítő kapu, rövid” vs. M7 – KAPU §0 10. sor „éles, kétrészes mastery-kapu — mindkét részt teljesíteni kell”)
A KAPU-fájl szerint a kvíz (≥80%, ≥10/12) KÖTELEZŐ második rész; a modul-áttekintő
„kiegészítő kapu”-ként írja le (azaz nem blokkol). Egy LMS-építő ellentétes Moodle-konfigot
vezetne le (gating BE vs. KI). A kapu-validitás (mastery-küszöb egyértelműsége) ellen hat.

**🟡 D3 — Single Choice item két védhetően jó opcióval (M1.1)**
`M1/M1_ONLINE_LECKE/M1.1 – Johari-ablak` (329–342. sor, Slide 6, Kérdés 2)
A szerzői megjegyzés maga kimondja: „Opciók (2 jó, 2 rossz – de itt csak 1-et kell választani…)”
(333. sor). Egyetlen-helyes-válasz formátumban két jó opció sérti a D3.2-t (pontosan egy
védhető helyes válasz); a tanuló jogosan választhat „rosszat”, ami felett címkézve. A
distraktorok ráadásul túl nyilvánvalóan abszurdak („soha többé ne hibázz”) — D3.5 plauzibilitás
is gyenge.

**🟡 D3 — Length-cue / testwise-cueing a formatív item-bankban (M2 KAPU)**
`M2/M2 – KAPU – értékelő (item-bank + rubrika)` (Item 4 83–92, Item 10 149–158 C-opciók; Item 5 94–103 B-opció)
Több „legjobb válasz” opció feltűnően hosszabb és részletesebb (több, vesszővel tagolt
megfigyelhető viselkedés), míg a distraktorok rövidek és sablonosak — klasszikus length-cue
(D3.4), amivel a tartalom ismerete nélkül is kitalálható a kulcs. Bár a szakasz deklaráltan
formatív (nem a kapu), az item-minőségi kritérium erre is vonatkozik, és rontja a self-check
diagnosztikai értékét.

### D4 — Curriculum-ív, belépő-folytonosság, blended-kötés

**🟡 D4 — Cél-szakadás a modul ívén: 3 érték kidolgozva, 1 mérve (M2)**
`M2/M2 – „Ki vagyok madrichként_”` (§2 kompetencia 2, 28–31; M2.2 mikrocél 12–14 „3 érték” vs. M2 – KAPU §0 15. sor „1 someres érték”, self-check 31, rubrika R2)
A kimeneti kompetencia és M2.2 három érték kiválasztását + három viselkedésre fordítását kéri,
a kapu viszont csak 1 someres értéket mér. A másik kettő „árva” kimenet, lefedetlen az
értékelésben (D4.5 / D2.3). Az M2.2 outro és M2.4 (374. sor) már egyes számra („a kiemelt
ÉRTÉKED”) vált, de a §2 és M2.2 fő szövege végig 3-at mond.

**🟡 D4 — Hiányzó belépő szakasz a kapu-aktivitás előtt (M0.4)**
`M0/M0_ONLINE_LECKE/M0.4 – „Dugma Ishit az online térben”` (teljes fájl)
M0.4-ből hiányzik a „2. Moodle-intro (H5P előtt)” belépő szakasz, ami M0.1–M0.3 mindegyikében
megvan, és hiányzik a „kezdd itt” getting-started utasítás (D4.1). M0.3 példamutatóan átvezet
(„A következő lépésed → M0.4”, 296–298), de M0.4 nem hivatkozik vissza a belépési pontra, csak
előre a fórumra — törés a blended ív belépő-folytonosságában (D4.1 / D4.2) épp a modul
kapu-aktivitása (fórum) előtt.

**🟡 D4 — Egyirányú online↔offline kötés, hiányzó belépő pozícionálás (M1)**
`M1/M1_ONLINE_LECKE/M1.1 – Johari-ablak` (a lecke ELEJÉN nincs „hol tartok az íven / melyik a peula-párom”; M1.2, M1.3 hasonló)
Az online mikroleckék (M1.1–M1.4) nem mondják meg a lecke elején, hol tartanak az íven és melyik
peula a párjuk; a folytonosság csak a lecke VÉGI „következő leckében…” hídban jelenik meg, és
csak online→online irányban. A peulák (M1.A 9–13, M1.B 9–13, M1.F 7) explicit listázzák a
kapcsolódó leckéket, de a leckék NEM hivatkoznak vissza (D4.3) — a blended pár célrendszere a
tanuló szemszögéből nem zár teljes ívvé.

### D5 — Akadálymentesség (WCAG)

**🔴 D5.2 — Tartalmi ábrákhoz nincs alt-szöveg / szöveges ekvivalens (M3)**
`M3/M3_ONLINE_LECKE/M3.1 – Tuckman-szakaszok` (SLIDE 2 animált görbe, SLIDE 3 4-jelenet storyboard, minden HOOK „AI beszélő fej videó”; ugyanígy M3.2 SLIDE 2 + 5B táblázat, M3.3 SLIDE 3 red flag lista, M3.4 ikonok)
Több információt hordozó vizuális elem (Tuckman-görbe, érzés-jelenet storyboard, kvuca-profil
ikonok) mellett a fájlok következetesen csak a VIDEÓKHOZ adnak felirat-flaget („Videók
feliratozva”), a KÉPEKHEZ / ÁBRÁKHOZ nincs alt-szöveg-előírás vagy szöveges ekvivalens. D5.2
kritikus: minden tartalmi ábrának ekvivalens alt-szöveget kell kapnia, a dekoratívat jelölni
kell. Tömeges, ismétlődő hiány mind a 4 online leckében.

**🔴 D5 — Egyenetlen akadálymentesítés a modulon belül (M4)**
`M4/M4_ONLINE_LECKE/M4.1 – Mit üzen a testem_` (SLIDE 1 AI-videó 61–111, SLIDE 3 Interactive Video 172–268, SLIDE 4 képpárok 272–331; M4.3 Sorting, M4.4 mini-check)
Csak az M4.2 tartalmaz részletes akadálymentesítési jegyzetet (célméret, billentyűzet, fókusz,
mobil-alternatíva). Az M4.1 (Interactive Video + képpárok + AI-videó), M4.3 (Sorting drag&drop
+ Single Choice Set) és M4.4 (mini-check) hasonló elemei NEM kapnak felirat- / alt-szöveg- és
billentyűzet- / célméret-jegyzetet. A freeze-frame képpároknak és ikonoknak nincs alt-szövege;
az Interactive Video narrációjának nincs kimondott feliratkövetelménye (D5.1, D5.2, D5.5).

**🔴 D5 — Timeline-grafika és narráció alt/felirat nélkül (Z modul)**
`Z/Z_ONLINE_LECKE/Z.1 – „Visszanéző tükör” – M0–M7 timeline` (Slide 1 sorozat-plakát ikon 61, Slide 2 idővonal 97–99 + opc. narráció 123–128, 285–289; Z.2 56–57, Z.3 58–60)
A leckék információt hordozó vizuális elemet (M0–M7 idővonal-grafika, modul-ikonok, sorozat-
plakát) és opcionális hangos narrációt írnak elő, de SEHOL nincs alt-szöveg (D5.2) és felirat /
szöveges-ekvivalens flag (D5.1). A timeline a tananyag kulcsüzenetét (az ív koherenciáját)
vizuálisan közli; ha kulcsszöveg képbe ég és nincs alt, a cél kizárólag vizuálisan / hangosan
érhető el. A narrációhoz nincs előírva, hogy a leckeszöveg szó szerint lefedi-e.

**🟡 D5.2 — Tartalmi screenshot/ikon/timeline alt-szöveg nélkül (M0)**
`M0/M0_ONLINE_LECKE/M0.3 – „Hogyan működik a Moodle / H5P / gate?”` (SLIDE 2 88–107 Moodle-screenshot; M0.1 SLIDE 2 timeline-ikon, SLIDE 3 ikonok)
A Moodle-screenshot kifejezetten tartalmi (megmutatja, hol vannak a modulok / kapuk), de nincs
szöveges ekvivalense, és fennáll a kulcsszöveg-képbe-égetés kockázata. A videó- / A-V-flag (D5.1)
sehol nincs kezelve, bár a H5P Course Presentation interaktív médiát feltételez. Mind a 4 leckére
összevont D5 megállapítás (alt-szöveg + felirat-flag hiány).

**🟡 D5 — Részleges/tömörített felirat + hiányzó diagram-alt (M1)**
`M1/M1_ONLINE_LECKE/M1.1 – Johari-ablak` (71. sor „feliratként is, tömörebben”; 142–178 Johari-animáció alt nélkül; analóg M1.2 53–101, M1.3 41–119)
A leckék kimondják, hogy a videók feliratozottak, de a HOOK-narrációknál gyakran „ugyanez mehet
feliratként is, tömörebben” (M1.1 71) — a felirat tömörített, nem szó szerinti, így a hangban
közvetített tartalom egy része kizárólag audión érhető el (D5.1). Diagram- / animáció-alt
(Johari 2×2, SBI folyamat) sehol nincs explicit megadva (D5.2). Mintázat M1.2–M1.4-en is végigfut
— modul-szintű, ismétlődő hiány.

**🟡 D5.5 — Kapus feladat billentyűzet-operálhatósága + célméret nem biztosított (M1.4)**
`M1/M1_ONLINE_LECKE/M1.4 – Miniszituációk_ „Mondd el SBI-ben”` (35–54 kártya-interakció, 90–147; M1.2 213–305 drag&drop)
Az M1.4 H5P mini-kvíz „nagy tappolható kártya” / „klikkelj egy kártyára” interakcióra épül, a
leckék „nagy tappolási felület” mobil-tippet adnak, de SEHOL nincs kimondva a billentyűzet-only
végigvihetőség és a látható fókusz követelménye — pedig ez a kapus út (a beadvány előfeltétele).
D5.5 a kapus feladatnál kritikus; hiánya kizárhat billentyűzet-használó tanulót.

**🟡 D5.5 — Drag&drop / Mark the Words billentyűzet-alternatíva nélkül (M1.1–M1.3)**
`M1/M1_ONLINE_LECKE/M1.2 – Megfigyelés ≠ értelmezés` (SLIDE 4 Mark the Words 213–251, SLIDE 5 Drag & Drop 255–304; M1.3 Fill in the Blanks 283–387, Interactive Video 41–119; M1.1 Course Presentation)
A D5.5 (célméret ≥24px + teljes billentyűzet-operálhatóság + látható fókusz + drag&drop
billentyűzet-alternatíva) követelményt csak az M1.4 teljesíti explicit előírással. Az M1.1–M1.3
egér- / húzásfüggő interakciói nem kapnak ilyet. Mivel az activity completion a modul
minimumkövetelménye (modulkeret §6, 183. sor: „H5P-k végigjátszva”), a drag&drop billentyűzet-
akadálya kizárhat egy completion-kötelezett tanulót.

**🟡 D5 — Felirat- és alt-szöveg-flag hiánya (M2 online leckék)**
`M2/M2_ONLINE_LECKE/M2.1 – identitás-körök` (SLIDE 1 „AI beszélő fej videó (16:9, felirattal)” 57–58; M2.2 57, M2.3 67, M2.4 55; koncentrikus-kör/diagram ábrák alt nélkül)
A leckék „AI beszélő fej videó, felirattal” elemekre épülnek, de sehol nincs jelölve, hogy a
narráció szövege szó szerint elérhető-e szöveges ekvivalensként (a narráció-szöveg a fejlesztői
doksiban van, nem garantáltan a tanulói felületen) — WCAG 1.2.2 kockázat. Az érdemi diagramoknál
(identitás-körök, 3-pillér ikon-ábra) nincs alt-szöveg-előírás. Tömeges, ismétlődő hiány.

**🟡 D5 — Akadálymentességi inkonzisztencia leckék között (M2.2 vs. M2.1)**
`M2/M2_ONLINE_LECKE/M2.2 – Értékeim mint iránytű` (SLIDE 1 57 AI-videó; SLIDE 3 szófelhő 127–162; M2.3 64–66; M2.4 54–56 — vö. M2.1 57 és 108, ahol EXPLICIT)
M2.1 mintaszerűen előírja a bekapcsolható feliratot + szó szerinti narráció-szöveget és a
koncentrikus-körök ábrához kötelező alt-szöveget. M2.2 / M2.3 / M2.4 AI-videókat és tartalmi
ábrákat (érték-szófelhő, 3-pillér ikonok, 3-oszlopos vizuál) tartalmaz ugyanezen követelmény
kimondása nélkül (D5.1, D5.2). A „szófelhő” ráadásul kontraszt / olvashatóság szempontból is
kockázatos (D5.4 / D5.7).

### D9 — Érzékeny megosztás / pszichológiai biztonság

**🟡 D9 — Privát vázlat → nyilvános poszt váltás kockázata (M0.4)**
`M0/M0_ONLINE_LECKE/M0.4 – „Dugma Ishit az online térben + bemutatkozó fórum”` (SLIDE 6 vázlat 199–231; 3. Forum-leírás 285–296)
A bemutatkozó fórum nyilvános posztot kér 15+ résztvevőtől, érzékeny tartalommal („mitől félsz a
madrich-szerepben”). A fórum-leírás (292) helyesen jelzi, hogy „ez a poszt a csoportnak látszik
(nem privát)” és felajánl négyszemközti alternatívát (jó D9.5). DE a korábbi vázlat-pontnál
(SLIDE 6) a tanuló még csak azt látja, hogy „a vázlatot csak a képzők látják” (230) — ami azt
sugallhatja, hogy a fórumposzt is privát. A váltás kockázata, hogy a tanuló érzékenyebbet ír be,
mint amit nyilvánosan vállalna.

### D10 / D5.11 — Fogalom-feloldás, pre-training

**🟡 D5.11 / D10.1 — Mozgalmi szakkifejezések feloldatlanok az első előfordulásnál (M0.4)**
`M0/M0_ONLINE_LECKE/M0.4 – „Dugma Ishit az online térben”` (SLIDE 1 35–46 „dugma ishit”, „chanich”, „kvuca”; M0.A „peula”, „ken”, „Zmán Kvucá”; M0.3 „H5P”, „activity completion”)
A héber / mozgalmi szakkifejezések és rövidítések nincsenek az ELSŐ előfordulásukkor feloldva
(D10.1 + D5.11 pre-training). M0.4 a „dugma ishit” fogalmat használat előtt nem definiálja
(feltételezi M0.2-t, de a lecke önállóan is elérhető); a „chanich” sehol nincs feloldva; a „kvuca”
definiálatlan. Nincs glosszárium / fogalomkártya. A mozgalmi szókincs feloldatlansága a 15+ belépő
modulnál akadály. Összevont megállapítás a modulra.

---

## 3. Review-be route-olt döntések

A megerősített, de **emberi döntést igénylő** (nem auto-javítható) tételek három
döntés-előkészítő dokumentumba kerültek. A tananyagforrást ezekből **szándékosan nem
módosítottuk** — a döntés a megfelelő szerepkör hatásköre.

### safeguarding-review — 46 tétel → [`SAFEGUARDING-REVIEW.md`](SAFEGUARDING-REVIEW.md)
**Hatáskör:** Hasomer Hacair gyerekvédelmi felelőse / vezetősége (egy ponton mentálhigiénés
szakember bevonásával).
A deep-auditból ide route-olt, szervezeti döntést igénylő gyerekvédelmi tételek. Tartalmi
kapcsolódás a megerősített találatokhoz: a krízis- / disclosure-protokoll emberi jóváhagyási
nyoma (D1.2, M3.3 / M3.4), a nyilvános fórum-megosztás pszichológiai biztonsága (D9, M0.4), és a
gyerekvédelmi forrás-épség / provenance (D1.5, M3.4). A best-practice szintű finomításokat a
tananyagba beépítettük; ezek a tételek viszont szervezeti policy-döntést hordoznak.

### ideology-gate-review — 23 tétel → [`IDEOLOGY-GATE-REVIEW.md`](IDEOLOGY-GATE-REVIEW.md)
**Hatáskör:** mozgalmi / Judaica szakértő + a magyarországi Somer vezetése és a képzés-stáb.
A SOMERES-FIDELITY audit 🧑‍🏫 (mozgalmi / Judaica szakértőt igénylő) és kapu-architektúra
(elv-vs-gyakorlat) tételei. Kapcsolódik a megerősített kapu-validitási találatokhoz (D3, M6 / M7):
hogy egy mastery-kapu küszöbe és filozófiája mozgalmi-pedagógiai döntés, nem auto-kalibrálható;
valamint a mozgalmi szókincs (dugma ishit, kvuca, Zmán Kvucá) tananyagbeli kezeléséhez (D5.11 /
D10.1, M0.4).

### architecture-review — 14 tétel → [`ARCHITECTURE-REVIEW.md`](ARCHITECTURE-REVIEW.md)
**Hatáskör:** képzés-stáb pedagógiai + LMS-építési döntés.
Architektúra-szintű (kapu-építhetőség, cél↔item illeszkedés, curriculum-ív / kompetencia-
lefedettség, akadálymentesség, adatvédelem) tételek, amelyek pedagógiai ív-, kapu-filozófiai,
jogi / korhatár- vagy dizájn-döntést hordoznak. Ide tartoznak a megerősített D3-as kapu-
ellentmondások (M6 hub↔KAPU, M7 „kiegészítő” vs. „kötelező”), a D4-es cél-szakadás (M2: 3 érték
kidolgozva / 1 mérve) és belépő-folytonossági törések (M0.4, M1), valamint a rendszerszintű D5
akadálymentességi konvenció-döntés (egységes alt-szöveg + felirat + billentyűzet-checklist).

---

## 4. Következő lépések

**A. Forrásba auto-javítható / következő körben javasolt szerkesztői munka**

1. **Egységes cél-sablon bevezetése (D2.1 — legmagasabb prioritás).** Minden modul-hub kimeneti
   kompetenciáját és minden lecke mikrocélját át kell írni „ige + tartalom” ILO-ra
   (felidéz / felismer / besorol / alkalmaz / megfogalmaz / megír / lefordít viselkedésre). A tiltott
   „megérti / tudatosul / érzi / jobban látja / megismeri / fejben tartja” fordulatok cseréje
   M0, M1, M2, M3, M4 modulokban. Az M1.4 és a már jó mérhető célok (M2 „1 oldalas jegyzet”,
   M3 „be tudja azonosítani”) referenciaként szolgálnak. **Ez a tétel okozta elsősorban a
   nem-konvergenciát.**
2. **Akadálymentességi checklist minden leckére (D5.1 / D5.2 / D5.5).** Az M1.4 és M2.1 mintát
   ki kell terjeszteni: (a) minden tartalmi ábrához kötelező alt-szöveg + dekoratív jelölés;
   (b) videó-narrációhoz szó szerinti szöveges ekvivalens a tanulói felületen (nem tömörített
   felirat); (c) minden drag&drop / kártya- / Mark the Words-interakcióhoz billentyűzet-
   alternatíva + látható fókusz + célméret ≥24px — kiemelten a kapus utakon. Érintett: M0, M1
   (1–3), M2 (2–4), M3 (mind a 4), M4 (1, 3, 4), Z (1–3).
3. **Kapu-ellentmondások feloldása a forrásban (D3, M6 / M7).** Hub és KAPU-fájl mastery-küszöbének
   és rubrika-sorainak összehangolása, hogy egyetlen, build-ready Moodle-konfiguráció vezethető
   le legyen (M6: R4/R5 vs. összevont sor; M7: „kiegészítő” vs. „kötelező második rész”).
4. **Item-javítások (D3, M1.1 + M2 KAPU).** M1.1 Slide 6 Kérdés 2: vagy Multiple Choice-ra váltani,
   vagy egyetlen védhető helyes opcióra szűkíteni + plauzibilisebb distraktorok. M2 item-bank:
   length-cue megszüntetése (a kulcs ne legyen feltűnően hosszabb).
5. **Belépő-folytonosság (D4, M0.4 + M1).** M0.4-be Moodle-intro + „kezdd itt” + visszahivatkozás
   M0.3-ra; az M1 online leckék elejére „hol tartok az íven / melyik a peula-párom” pozícionálás
   (kétirányú online↔offline kötés).
6. **Cél-szakadás (D4, M2): 3 érték vs. 1 mérve** — döntés után a §2 kompetencia / M2.2 szöveg
   és a kapu-rubrika R2 összehangolása (vagy mindhárom értéket mérni, vagy végig 1-re egységesíteni).
7. **Forrás-épség (D1.5, M3.4):** a `?utm_source=chatgpt.com` paraméterek eltávolítása a linkekből
   + a forrás emberi visszaellenőrzése + AI-provenance jelölés (D1.3).
8. **Lektor-nyom (D1.2, M3.3 / M3.4):** a KAPU-fájlon meglévő review-jelölés átvezetése a két
   biztonságkritikus leckefájlra is.

**B. Emberi döntésre váró tételek** — a három review-dokumentum feldolgozása a megfelelő
szerepkörökkel (safeguarding 46, ideology-gate 23, architecture 14). Ezek lezárása nélkül a
következő audit-kör sem fog konvergálni, mert a kapu- és cél-architektúra részben ezeken a
döntéseken áll.

**C. Konvergencia-kapu a következő körhöz:** a fenti A1 (cél-sablon) és A2 (akadálymentességi
checklist) rendszerszintű átvezetése után érdemes 3. kört indítani — ezek megszüntetése után a
maradék találatok várhatóan egyedi, pont-szintű eltérésekké redukálódnak, és a futás konvergálhat.

---

*Generálta: deep-audit (live mód, 2 kör). A rubrika: [`DEEP-AUDIT-RUBRIC.md`](DEEP-AUDIT-RUBRIC.md).*
