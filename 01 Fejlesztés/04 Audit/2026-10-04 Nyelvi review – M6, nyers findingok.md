# Nyelvi review – M6, nyers findingok (2026-10-04)

> **Audit trail, nem kánon.** A `/course-review M6 --lens language` hat nyelvi reviewer-csoportjának szó szerinti
> kimenete (repó-relatív útvonallal). **Nem validált nyers lista:** a verdiktek, az eredet-besorolás és a pontosított
> javaslatok a `2026-10-04 Nyelvi review – M6, Anna-baseline összevetés.md`-ben vannak, és azok érvényesek. A G6
> reviewer 2 további P2 findingot a kimeneti korlát miatt levágott; ezek nincsenek meg.

## G1 – modulhub, kapu, M6.F (NYELV-101…115)

**NYELV-101**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:349, 352, 359, 364`. Forrás: `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:479–496`
- **Probléma:** A P1. pool-item pontatlanul veszi át az M6.A 4.3.2/B lépéseit, négy ponton:
  - A visszajelzés feltétel nélküli szabályként tanítja, hogy a Memunát még a peula alatt be kell vonni. Kiesett a „ha valaki erősen érintett” minősítő (2. regressziós minta).
  - A 349. sorban a „láthatóan rosszul lesz” testi rosszullétként is olvasható. A forrás szövege: „rosszul érint”.
  - A mintamondat („csináljunk egy kis levegőt”) és a „nem halasztod utánra” nem magyar.
  - A 359. sorban a „pont ezt kerüli a 4 lépés” egy hibás válasz utáni visszajelzés. A négy lépést azonban csak a helyes válasz visszajelzése sorolja fel, így a „4 lépés” előzmény nélkül marad.
- **Bizonyíték:** KAPU:364 „(4) **még a peula alatt bevonod a Memunát** – nem maradsz egyedül a helyzettel, és nem halasztod utánra.”
  M6.A:496 „**4. Még a peula ALATT vond be a kijelölt Memunát**, ha valaki erősen érintett – ne maradj egyedül a helyzettel, és ne halaszd a peula utánra.”
- **Hatás:**
  - A kvíz más eszkalációs szabályt tanít, mint a peula.
  - Aki a „rosszul lesz” fordulatot testi vészhelyzetként érti (ott a jelzési út 112-es lépése érvényes), annak a ✅-es válasz hibásnak tűnik.
  - Hibás válasz után a tanuló nem tudja, melyik „4 lépésről” van szó.
  - A biztonság-jog lencse ebben a futásban nem fut, ezért a megerősítéshez a Memuna QA-ja kell.
- **Javaslat:** Szó szerinti átvétel az M6.A 4.3.2/B-ből:
  - 349: `az egyik hanihot láthatóan rosszul érinti egy identitást súroló állítás`
  - 352, a zárójeles mintamondat: `„Álljunk meg egy pillanatra, legyen egy kis levegő.”`
  - 364, a (4) pont: `…bevonod a Memunát, ha valaki erősen érintett – nem maradsz egyedül a helyzettel, és nem halasztod a peula utánra`
  - 359: `az M6.A-ban tanult 4 lépés`

  Javítási korlát: a ✅ az A opción marad. Az A opció Memuna-mondata, a kiülés felajánlása és az M3.B-hivatkozás nem törölhető. Új szakpolitikai állítás nem kerülhet be.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-102**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:222–226`
  - `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:35–36, 409`
- **Probléma:** A teljesítési szabály szóhasználata önellentmondó.
  - A hub „mindhárom” feltételt említ, pedig a 3. pont kimondja: „nem feltétel”.
  - A KAPU a „modul” teljesítését egyedül a játéklaphoz köti. A hub szerint (224. sor) a modulhoz az M6.1–M6.4 érdemi teljesítése is kell. A KAPU szakasza a kapu-logikát írja le, a szöveg mégis „modul”-t mond.
- **Bizonyíték:** HUB:222 „Az M6 akkor **teljesített**, ha mindhárom teljesül:” ↔ HUB:226 „…**nem feltétel**.”
  KAPU:409 „→ **modul teljesítve** – ez az **éles, blokkoló** feltétel.”
- **Hatás:** Aki a KAPU-t mérvadónak olvassa, a leckék nélkül is teljesítettnek veheti a modult. A hub olvasója pedig a formatív kvízt feltételnek hiheti.
- **Javaslat:**
  - HUB:222: `ha az alábbi két feltétel (1–2.) teljesül`. A 3. pont megjegyzésként változatlan marad.
  - KAPU:35: `A kapu akkor teljesül, ha:`
  - KAPU:409: `→ a kapu teljesült`

  Küszöb, blokkoló feltétel és completion-logika nem változik.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-103**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:403` (vö. 393, 406, 407)
- **Probléma:** Az R1 „Oké”-ellenőrzőlistája „pontosan 1” célt ír. A rubrikatábla „1 konkrét, kimondott cél”-t mond, a többi sor pedig „legalább 1”-et. A kvantor más szabályt ad: két konkrét céllal a lap a lista szerint nem „Oké”.
- **Bizonyíték:** KAPU:403 „- [ ] **R1** – pontosan **1** kimondott, az eszközhöz illő cél.”
  KAPU:393 „A lapon **1 konkrét, kimondott cél** áll, ami az eszközhöz illik”
- **Hatás:** A társak és a stáb a két szöveg alapján eltérően pontoznak. Az éles kapu „minden sor ≥ 2” feltétele miatt ez a kapueredményt is eldöntheti.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős / projektgazda): az R1 „Oké” szintje pontosan egy vagy legalább egy célt követel? Utána a tábla és a lista ugyanazt a kvantort használja. Szöveget nem javaslok.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-104**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:394, 404`
  - `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:211`
- **Probléma:**
  - Az R2-ben ugyanaz a címkekészlet („Parparim 6–9 / Kivsza 10–12 / Leviatán 13–17”) áll az „Oké” szint kötelező „korosztály”-megadásánál és az „Erős” szint „kvuca-típus”-bónuszánál. A Glosszárium szerint a három kvuca-név maga a korosztály-elnevezés, így a bónusz nem különböztethető meg a minimumtól.
  - A hub az „Erős” szint feltételének írja azt, amit a mérvadó KAPU „ráadás, nem feltétel”-nek nevez.
  - A hub „megnevezi … + … előhívva indokol” szerkezete nem mondat.
  - A KAPU harmadik személyű cellája hirtelen tegezésre vált („ha emlékszel, nevezd meg … tanultad”).
- **Bizonyíték:** KAPU:394 „…nevezd meg a someres kvuca-típust is (Parparim 6–9 / Kivsza 10–12 / Leviatán 13–17) … így a típus-megnevezés ráadás, nem feltétel.”
  HUB:211 „„Erős” szinten megnevezi a someres kvuca-típust (Parparim / Kivsza / Leviatán) + legalább 1, az M3.2-ben tanult korosztály-jellemzőt (…) előhívva indokol”
- **Hatás:** A hub és a KAPU szerint más az „Erős” feltétele, és a bónusz a minimumtól sem választható el. A pontozás nem kalibrálható.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős): mi különbözteti meg az R2 „Oké” korosztály-megadását az „Erős” kvuca-típus-megnevezéstől? A döntés után a hub §6.2 R2-összefoglalója szó szerint a KAPU-t kövesse, a cella pedig végig harmadik személyben álljon. Addig nyelvi átírás ne legyen.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-105**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:155`. Ugyanez a mondat áll itt is: `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:87, 473, 491` (ez másik csoport scope-ja).
- **Probléma:** A szöveg a *dugma isit* fogalmat egy tárgyra, a játékra mondja állítmányként. A Glosszárium szerint a fogalom a madrih élőben látható személyes példamutatása, és a „Dugma Isitnek lenni” forma kerülendő.
- **Bizonyíték:** HUB:155 „„Miben szeretném, hogy a saját játékom **a biztonság és az inkluzivitás szempontjából** *dugma isit* (személyes példamutatás) legyen?””
- **Hatás:** A tanuló a kulcsfogalmat félreértett jelentésben gyakorolja (a játék mint példakép).
- **Javaslat:** A Glosszárium kijelölt formájával: `„Miben szeretnék a saját játékommal a biztonság és az inkluzivitás szempontjából személyes példát (*dugma isit*) mutatni?”`. Az M6.B címe és instrukciója együtt változik vele (7. regressziós minta), vagy egyik sem.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-106**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:218`. Vö. `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:387, 409`
- **Probléma:** A hub mondata az R4-re és az R5-re is vonatkozik, a zárótag mégis csak „biztonsági soron” zárja ki a társak buktatását. A döntéshozót is másként nevezi („a mentor vagy a stáb”), mint a mérvadó KAPU („a képző/mentor”).
- **Bizonyíték:** HUB:218 „**mindig a mentor vagy a stáb hozza meg**; a társak pontszáma önmagában **nem zár le és nem buktat biztonsági soron**.”
  KAPU:387 „…végső pontját **mindig a képző/mentor adja**”
- **Hatás:** Az inkluzivitási (R5) sor társas lezárása a hub szerint nyitva marad, a döntéshozói kör pedig tágabbnak olvasható, mint a KAPU-ban.
- **Javaslat:** HUB:218: `mindig a képző/mentor hozza meg`, illetve `nem buktat blokkoló soron (R4, R5)`. A HUB:217 konzultációs fordulata („mentorral / stábbal egyeztetve”) marad.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-107**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:128, 137, 208, 221/227, 271/274, 291, 293`
- **Probléma:** Több tanulónak megjelenő kvízszöveg hibás szerkezetű, vagy nem a választott opcióra reagál:
  - 227: a D opció hibáját „a részvétel elvétele”-ként nevezi meg, pedig a D opció a kvuca beleszólását veszi el (221).
  - 271: „a kulcs, hogy kimondod, nem művészi verseny” rosszul tagolt; a 274. sor ugyanerre „művészeti verseny”-t mond.
  - 293: „épp a kapcsolódást veszti el” – az alany nem azonosítható.
  - 208: „nem osztunk rá” egy tagadott előzményre mutat.
  - 291: „állapotukat” előzmény nélkül áll.
  - 128: az „energizer „még egy utolsó nagy őrület”” idézet kötőszó nélkül lóg.
  - 137: „Fáradtan elvész a fonal” – a határozó nem az alanyra vonatkozik.
- **Bizonyíték:** KAPU:221 „D) A madrih előre kitalálja az összes állítást, a kvuca ne szólhasson bele, …”
  KAPU:227 „D – Jó szándékú kontroll, DE a részvétel elvétele nem véd: …”
- **Hatás:** A 71. sor szerint a disztraktor-indok hibás válasz után a tanuló visszajelzése. Ha nem a választott hibát nevezi meg, vagy félreolvasható, a diagnosztikai funkció sérül (7. regressziós minta).
- **Javaslat:**
  - 227: `a beleszólás elvétele`
  - 271: `a kulcs az, hogy kimondod: ez nem művészeti verseny, és más eszközt is adsz`
  - 293: `épp a kapcsolódás vész el`
  - 208: `és senkire nem osztunk valódi „kirekesztett” szerepet`
  - 291: `a fáradtak tényleges állapotát`
  - 128: `energizer „még egy utolsó nagy őrület” jelszóval`
  - 137: `Fáradtan könnyen elveszítik a fonalat egy bonyolult, hosszú történetnél.`

  A ✅, az opciósorrend és az elosztók tartalma és hihetősége nem változik.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-108**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:174, 186`. Forrás: `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:878`
- **Probléma:** Az „akadálymentes tér” egy inkluzivitási modulban elsődlegesen hozzáférhetőséget jelent. Itt a botlásveszélytől mentes, szabad teret kell érteni alatta, de az M6.1-es glossza („nincs útban szék, asztal, kábel”) a kvízből kimaradt.
- **Bizonyíték:** KAPU:174 „- A) Akadálymentes tér, közös „stop” jelszó és lassú, sétáló tempó. ✅”
  M6.1:878 „**Tiszta, akadálymentes tér** – nincs útban szék, asztal, kábel, lépcső.”
- **Hatás:** A helyes válasz egy másik fogalomként (akadálymentesítés) is olvasható, így a fizikai biztonsági minimum elmosódik.
- **Javaslat:** A 174. és a 186. sorban együtt: `Akadályoktól mentes, szabad tér` (vagy az M6.1 glosszájával). A ✅ marad.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-109**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:91, 254`
  - `02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md:12, 106, 229` (és a nyomtatandó POSZ-01 és MUNK-01 sorfeliratai: 195, 254)
- **Probléma:** A „Történet, mint tükör” címben a „mint” minőséget jelöl („tükörként”), ezért elé nem kell vessző. A korpusz maga is vessző nélkül írja: HUB:61, 93 és M6.F:26.
- **Bizonyíték:** HUB:91 „### M6.2 – „Történet, mint tükör” (15–20’)”
  HUB:93 „hogyan működik a **történet mint tükör** a kvucának”
- **Hatás:** Ugyanaz a cím két írásmódban él. A cím a `Média-assetek/VOICE-PILOT-SCRIPTS.md`-ben is előfordul; ha narrált, a vessző törlése a hanggyártást is érinti (VO D-10).
- **Javaslat:** `Történet mint tükör` mindenhol, de csak együtt mozgatva: az M6.2 fájlnevével, minden relatív linkkel és a médiaregiszter-útvonalakkal, külön `git mv` commitban. Részleges csere tilos; ha az átnevezés most nem fér bele, maradjon minden.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-110**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:91, 135, 157, 181, 183, 225, 227, 247, 249, 269, 270, 271, 291, 292, 293, 359 („DE”); 81, 147, 306, 372`
  - `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:66, 175, 179, 225`
  - `02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md:331`
- **Probléma:** Tipográfiai és központozási hibák:
  - A tanulónak megjelenő indokokban a nagybetűs „DE” hangsúlyjel 16 helyen áll; a 182. sor ugyanerre kisbetűs „de”-t ír.
  - Hiányzik a vessző: HUB:66 („…érzékenységek) és tud”), KAPU:81 („tanuljanak és oldódjon”), M6.F:331 („percben kérlek, nézz”).
  - KAPU:306: „Téves, a túl erős…” – vessző helyett kettőspont kell.
  - KAPU:372: „főleg ha … kérdésnél” – hiányzik az ige és a vessző.
  - „fogalom-térkép” (HUB:175, 179), az M6.F törzsszövege viszont „fogalomtérkép”.
  - „Leviatán kvuca” (KAPU:147), máshol „Leviatán-kvuca” (157 és az M6.4).
  - HUB:225-ben „= … →” jelek állnak mondat helyett.
- **Bizonyíték:** KAPU:181 „- B – A „mindenki ugyanannyit” méltányos szándék, DE **szervezési** elem”
  KAPU:182 „- C – Kényelmi szempont lehet, de a biztonságot nem a magasság”
- **Hatás:** Következetlen, nem magyar tipográfia a tanulói visszajelzésben és a kapu-specifikációban.
- **Javaslat:**
  - „DE” → `de`; a kiemelést a meglévő félkövér adja.
  - A hiányzó vesszők pótlása.
  - 306: `Téves: a túl erős`
  - 372: `főleg, ha biztonsági vagy inkluzivitási kérdésnél hibáztál`
  - HUB:175, 179: `fogalomtérkép`
  - 147: `Leviatán-kvuca`
  - HUB:225 mondattal: `…rovat esetén a sor 1 pontot kap, és a kapueredmény „Még nem teljesítve”.`

  A ✅ és a küszöbök nem változnak.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-111**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:103, 182, 287, 361, 387, 429; 48, 344, 346`
  - `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:202`
- **Probléma:** Anglicizmusok és hivatali tónus tanulói és képzői szövegben:
  - Tanulói: „tematizálni”, „csoportmechanikák” (103), „irreleváns a kockázatra” (182), „energizálja” (287), „gyermekvédelmi becsatornázást” (361), „emberre adott SBI-ben a B” (429 – az angol betűjel magyarul átláthatatlan; a Glosszárium szerint: Helyzet → Viselkedés → Hatás).
  - Képzői: „item-pool” / „POOL-ITEM” (HUB:202, KAPU:48, 344, 346), „Stáb-záró” (387).
- **Bizonyíték:** KAPU:361 „a „nem szólok senkinek” pedig épp a gyermekvédelmi becsatornázást (a Memuna bevonását) mulasztja el.”
  KAPU:182 „irreleváns a kockázatra”
- **Hatás:** A biztonsági visszajelzés bürokratikus, a tükörfordítások lassítják a megértést.
- **Javaslat:**
  - 103: `szeretnéd felvetni a kirekesztés témáját` (az M6.4 B. szcenárió tanulói céljával egyezően) és `csoportfolyamatok`
  - 182: `a kockázat szempontjából lényegtelen`
  - 287: `felpörgeti` (az elosztó tartalma nem változik)
  - 361: `épp a gyermekvédelmi jelzést, a Memuna bevonását mulasztja el`
  - 429: `az emberre adott SBI-ben a „Viselkedés” (B) elem a megfigyelhető viselkedést írja le` (ugyanez a mondat áll az M6.B:403-ban)
  - „item-pool”: `cserekészlet`; a „P1” azonosító marad
  - 387: `Stábdöntés a blokkoló sorokon`

  A „completion” + magyar rag (HUB:170, KAPU:387, 413, M6.F:54) korpuszszintű minta (26 fájl), ezért itt egyedi cserét nem javaslok.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-112**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md:125, 333, 393, 95; 36, 323, 377–379, 444–445, 387, 420, 431`
- **Probléma:** A képzői instrukció következetlen.
  - Egy bekezdésen belül vált a személy: a 2.3 harmadik személyű, a 4.x tegező, a 95. sor többes szám 2. személyű.
  - Különösen a 125. sorban a kettesben beszélgetés szabálya: „a képző … beszélj vele”.
  - A 333. sorban egy mondaton belül változik az alany: „tarthatják … begyűjtheted”.
  - Ezen felül: nem párhuzamos célfelsorolások (377–379, 444–445), igei elem nélküli pont (323), cselekvő nélküli „a leckék … elindultak” (36), tükörszerkezet („Forduljatok … csoportokba”, 387), vonzathiba („jó Kivszára”, 420), névelőhiány („M6 logikájával”, 431).
- **Bizonyíték:** M6.F:125 „…ahol a képző diszkréten tud beszélni valakivel, … Kettesben csak indokolt esetben és egy másik felelős tudtával beszélj vele.”
- **Hatás:** Felolvasva vagy átfutva nem egyértelmű, kinek szól a gyermekvédelmi szerephatár.
- **Javaslat:**
  - 125: `…beszéljen vele.` (a védelmi feltétel szó szerint marad)
  - 333: `A résztvevők megtarthatják a lapokat, vagy begyűjtheted őket név nélkül…`
  - 393: `vegye el`
  - 36: `a résztvevő legalább részben elkezdte az M6.1–M6.4 leckéket`
  - 323: `– vagy a hiányzó L1–L4 videók / H5P-k pótlása`
  - 377–379 és 444–445: egységesen főnévi igeneves pontok
  - 387: `Alakítsatok 2–3 fős csoportokat.` (ugyanez a sablon az M5.F:289-ben és az M7.F:269-ben; együtt javítandó)
  - 420: `jó a Kivszának`
  - 431: `az M6 logikájával`
- **Típus:** objektív
- **Verdikt:** —

**NYELV-113**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:63`
  - `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:64`
- **Probléma:** A hub „M6.4 (T-ágak)” jelölésnek nincs megfelelője. Az M6.4 csak A–D-ágat, a tanulói felületen pedig „A.–D. szcenárió”-t ismer (M6.4:165–176). A KAPU ugyanarra az ágra „B-ág”-at ír, holott a tanulói visszajelzései (118, 208) „B. szcenárió”-t mondanak.
- **Bizonyíték:** HUB:63 „*(Főleg: M6.2, M6.4 (T-ágak), M6.B, M6.F)*”
  KAPU:64 „| M6.2, M6.4 (B-ág) | 11, 12 |”
- **Hatás:** Törött belső hivatkozás; egy ágra két megnevezés.
- **Javaslat:**
  - HUB:63-ra szöveget nem javaslok. Tisztázni kell, mire utal a „T-ágak”; nem találgatom.
  - KAPU:64: `M6.4 (B. szcenárió)`
- **Típus:** objektív
- **Verdikt:** —

**NYELV-114**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:34, 61, 235`
  - `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:368, 437`
  - `02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md:54, 460`
- **Probléma:** Összefoglaló és keretező mondatok mást mondanak, mint a tartalom, amit összefoglalnak:
  - M6.F:460 – „játék-labor különböző kvucákkal”, holott az M6.A korosztály-szemüvegekkel dolgozik, valódi kvuca nélkül (HUB:133). A „– ez a javító leadásod – úgy, hogy…” tagolás is félreérthető.
  - HUB:235 – „completion arány modulonként” lecke-szintű adatra.
  - HUB:34 – a „tervezési érték” egyszer 3 óra, egyszer 2,5–3 óra (a Program terv:71 szerint „tervezéshez 3 óra”).
  - KAPU:368 – „mindkét kimenetnél megjelenő szöveg”, pedig két külön szövegről van szó.
  - KAPU:437 – „a bizonyíték … dől el”.
  - M6.F:54 – az „(az Assignment az M6.B után nyílik meg)” közvetlenül a javító leadás megnyílása mellett áll.
  - HUB:61 – „Ért egy rövid történetet mint „tükröt”” tükörszerkezet.
- **Bizonyíték:** M6.F:460 „játék-labor különböző kvucákkal, majd játéklap-műhely a saját eszközeitekkel.”
  HUB:235 „M6.1–M6.4 completion arány modulonként,”
- **Hatás:** A képző pontatlan összefoglalót olvas fel, a stáb rossz bontásban keresi az adatot, és ugyanaz a tervezési érték két számmal szerepel.
- **Javaslat:**
  - M6.F:460: `játék-labor három korosztály szemszögéből` és `tedd rendbe a jelzett sorokat úgy, hogy más madrih is tudja használni a lapot, és add le a javított játéklapodat a Moodle-ben – ez a javító leadásod.`
  - HUB:235: `leckénként`
  - HUB:34: a zárójeles „tervezési érték” → `terhelési sáv` (a számok nem változnak)
  - KAPU:368: `(a két kimenet szövege)`
  - KAPU:437: `…a teljesítés érdemi bizonyítéka a játéklap, a blokkoló döntés pedig az R4/R5 blokkoló feltételén dől el`
  - M6.F:54: `(az első leadás az M6.B után nyílik meg)`
  - HUB:61: `Érti, hogyan működik egy rövid történet „tükörként”:`
- **Típus:** objektív
- **Verdikt:** —

**NYELV-115**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:38` (vö. 52, 437)
- **Probléma:** Egy mondaton belül „kötelezően becsatornázódik” és „ajánlott” áll. Nem dönthető el, hogy a mentori egyeztetés kötelező tanulói vagy stábteendő, vagy csak ajánlás. Az 52. és a 437. sor jelzésnek, illetve „a beszélgetés indokának” nevezi.
- **Bizonyíték:** KAPU:38 „A kvíz **diagnózisa** azonban kötelezően becsatornázódik: … **célzott ismétlés + mentori egyeztetés** ajánlott”
- **Hatás:** A képző nem tudja, köteles-e a gyenge biztonsági és inkluzivitási kvízeredmény után egyeztetést kezdeményezni.
- **Javaslat:** EMBERI DÖNTÉS (értékelési felelős): a „kötelezően” a stáb figyelési kötelezettségére vagy a tanulói lépésre vonatkozik? Szöveget nem javaslok, amíg ez nincs eldöntve.
- **Típus:** emberi-döntés
- **Verdikt:** —

A súlyosságot a `.claude/finding-format.md` küszöbe szerint adtam meg (jelentést torzító nyelvi hiba = P1). A `DEEP-AUDIT-RUBRIC.md` D11 sora egy fokkal szigorúbb (jelentés- vagy szabályváltoztató nyelvi hiba = P0, természetellenes magyar = P1). E szerint a NYELV-101–104 P0 lenne; a kalibrálás a verifier dolga.

## G2 – M6.1 (NYELV-201…215)

### NYELV-201
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:1423`
- **Probléma:** A kérdés „durva” élményjátékról beszél, és a 2–3. opcióval együtt azt sugallja, hogy idősebb Leviatánoknál a durva játék rendben van. A lecke többi része és az asset címe (1272) mély vagy erős élményt említ, durvát nem.
- **Bizonyíték:** `> „Mikor **nem jó** nagyon mély, durva élményjátékot hozni?”`
- **Hatás:** A tanuló a köznyelvi „durva” (kemény, bántó) jelentést elfogadható játékjellemzőként tanulja meg. Ez ellentmond a 1442–1443. sori visszajelzésnek („az erős élmény önmagában nem tanít … árthat is”), és torzítja a biztonsági keretezést.
- **Javaslat:** „Mikor **nem jó** nagyon mély, erős élményjátékot hozni?” Az „erős” a lecke saját szava (489, 1442). Nem változik: a ✅ (1427), az opciók és mindkét visszajelzés. Látható szöveg, ezért újra kell pinelni.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-202
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:313`
- **Probléma:** A „kézműveseket” kézműves embereket jelent, a mondat viszont a következő leckék kézműves feladatairól szól. Ez a hiányzó alaptag mintája (1. regressziós minta), és a mellérendelésből a névelő is kimaradt.
- **Bizonyíték:** `mert erre illesztjük a játékokat (és a következő leckékben a történeteket és kézműveseket is).`
- **Hatás:** Szó szerint olvasva a tanuló embereket „illeszt” a korosztály-térképre, és a mondat eltér a modul terminusától.
- **Javaslat:** „…(és a következő leckékben a történeteket és a kézműves feladatokat is).” A „kézműves feladat” a modul uralkodó alakja (M6.3, M6.4, modulhub). A modulhub és az M6.3 címében álló főnévi „kézműves” más csoport scope-ja, itt nem javítandó.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-203
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md`
  - „játék-kategória”: 1, 6, 14, 24, 31, 197, 1405, 1463
  - „játék-szituáció”: 37
  - „kontakt-játék”: 449, 480, 851, szemben a 458. sori „kontaktjáték” alakkal
  - „élmény-alapú”: 453, 458 (spec: 363), szemben a 488. sori „élményjáték” alakkal
  - „megfigyelő-szerepben”: 887
  - „beszélgető kártya”: 1047, 1077, 1106, 1118
- **Probléma:** A kéttagú összetételek kötőjellel vagy különírva állnak, holott egybeírandók. Ugyanaz a kategória a leckén belül két alakban is szerepel.
- **Bizonyíték:** `3. **Bizalom- / kontakt-játékok**` (449) ↔ `3. Bizalom- és kontaktjáték;` (458, alt-szöveg)
- **Hatás:** Helyesírási hiba van a címben és a tanulói szövegben. A kategórianév mást mond a dián, az alt-szövegben és a narrációban, a kapu (186) pedig egy harmadik alakot használ („Bizalom-/kontaktjátéknál”).
- **Javaslat:**
  - Egybeírt alakok: játékkategória, játékszituáció, kontaktjáték (449: „Bizalom- és kontaktjátékok”), élményalapú, megfigyelőszerepben, beszélgetőkártya/beszélgetőkártyás.
  - Az 5. kategória neve kövesse a modulhubot (84): „Mélyebb élményjátékok” (453, 458, 363).
  - A cím (1, 6, 24) csak a fájlnévvel együtt változhat, a `course-content.md` átnevezési szabálya szerint: külön `git mv` commit, minden hivatkozó hely frissül, a generált kimenetek build-del készülnek. Az `asset-migration-map.csv` és a `_legacy/` érintetlen marad. Ha az átnevezés most nem fér bele, a futó szöveg se váljon el a címtől.
  - A 480, 851, 488 és 1077 narrációs sor, ezért a változás a hanggyártást is érinti.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-204
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:1409-1412` (spec: 1249)
- **Probléma:** A négy opció közül csak a helyes szól 2. személyben („átlátod”). A többi 1. személyű vagy személytelen, így a nyelvtan elárulja a kulcsot.
- **Bizonyíték:** `* „Mert így mindig ugyanazt a bevált kedvenc játékot húzhatom elő bármelyik kvucánál.”` / `* „Mert így jobban átlátod, mire való egy játék, és melyik korosztályhoz illik.” ✅`
- **Hatás:** A kvíz a nyelvtani eltérés alapján is megoldható, és a tanuló szájába adott válaszok hangja következetlen.
- **Javaslat:** A ✅ opció legyen: „Mert így jobban átlátom, mire való egy játék, és melyik korosztályhoz illik.” Ugyanez kerüljön a 1249. sori spec »…« idézetébe is (7. minta). Nem változik: a ✅ helye, a többi opció és a 1416–1417. sori visszajelzés (ott a 2. személy helyes).
- **Típus:** objektív
- **Verdikt:** —

### NYELV-205
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:853, 1467`
- **Probléma:** Két helyesírási hiba:
  - A 853. sorban a toldalék az idézőjelen belülre került (a játék neve „Csukott szemű vezetés”).
  - A 1467. sorban az állapothatározói „mint” elé vessző került.
- **Bizonyíték:** `> A ‘Csukott szemű vezetésnél’` / `> A következő leckében (**M6.2 – Történet, mint tükör**)`
- **Hatás:** Helyesírási hiba marad a tanulói szövegben, és a játéknév nem egyezik a kártyán szereplővel (834).
- **Javaslat:**
  - 853: „A ‘Csukott szemű vezetés’-nél” (a toldalék kötőjellel az idézőjel után áll). Ez narrációs forrásszöveg, ezért a hanggyártást érinti, a szüneteket nem.
  - 1467: „Történet mint tükör”. Ez az M6.2 címe és fájlneve (16 előfordulás 8 fájlban: modulhub, LMS activity manifest, média-regiszter). Csak az M6.2 átnevezésével együtt javítható, itt önmagában nem.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-206
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:1428-1429`
- **Probléma:** A 2. és a 3. opcióból hiányzik az állítmány, ezért feltétel helyett általánosító állításként olvasható. A szerkezet nem párhuzamos az 1. opcióval.
- **Bizonyíték:** `* „Amikor fiatalabb Leviatánok (13–15), szeretnek beszélgetni, és kérik a mélyebb témákat.”`
- **Hatás:** Úgy olvasható: „ha Leviatánok, akkor szeretnek beszélgetni”. A disztraktorok nyelvileg sutábbak a kulcsnál, ez is súgás.
- **Javaslat:** Az 1. opció szerkezetét követve:
  - „Amikor fiatalabb (13–15 éves) Leviatán-kvucáról van szó, amelynek tagjai szeretnek beszélgetni, és kérik a mélyebb témákat.”
  - „Amikor idősebb (16–17 éves) Leviatán-kvucáról van szó, amelynek tagjai régóta együtt vannak, és bíznak egymásban.”

  Nem változik: a ✅ (1427) és a visszajelzések.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-207
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:673, 685, 1205, 1211`
- **Probléma:** A Névkör-kérdésből hiányzik, ki és mit kezd. A visszajelzésekben a „kevésbé kínos” alanya a mellérendelés miatt „a szabály”-ra csúszik.
- **Bizonyíték:** `> ha most kezdenek?”` (673) / `egyszerű a szabály, és kevésbé kínos.` (1211)
- **Hatás:** A kulcs (Parparim) azon múlik, hogy a csoport friss, de ezt a kérdés nem mondja ki. A visszajelzés logikája homályos.
- **Javaslat:**
  - 673: „ha friss a kvuca?” (a 648. narrációs sor saját szava).
  - 685, 1205, 1211: az alany legyen kitéve, pl. „…és ez a forma náluk kevésbé kínos.” Az összehasonlítás alapja (idősebbek, vö. 661–662) ne kapjon új indoklást.
  - Nem változik: a ✅ (677, 1198).
- **Típus:** objektív
- **Verdikt:** —

### NYELV-208
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:1219-1220, 1226, 1231, 1234-1235` (spec: 1158)
- **Probléma:** A Szitu 2 feladata és a hozzá tartozó biztonsági keret több nyelvi hibát tartalmaz:
  - Az egyes számú „a kvuca … kap” után többes számú „kell futniuk” áll.
  - A „három falhoz tartozó jelet kap” úgy is érthető, mintha egyetlen jel tartozna mindhárom falhoz.
  - A keretben a „kizáródás” a modulban sehol máshol nem fordul elő; a modul a „kimarad”/„kiesés” szót használja.
  - A címkék nem párhuzamosak: a tempó és a tér szempont, az „ütközés-kerülés” megoldás, a „kizáródás” kockázat.
  - A 1231. sor főnévi szerkezetű („a „teljes erőből futás” fix falakhoz”).
- **Bizonyíték:** `> ahol a kvuca három falhoz tartozó jelet kap,` / `> és jelre **különböző falakhoz kell futniuk** teljes erőből.”`
- **Hatás:** A tanuló nem érti pontosan azt a szabályt, amelynek a kockázatait meg kell neveznie, és a biztonsági keretet nehéz felolvasni.
- **Javaslat:**
  - 1219–1220: „ahol mindhárom falnak saját jele van, / és a gyerekeknek jelre **különböző falakhoz kell futniuk** teljes erőből.”
  - 1226, 1235 és 1158: „kizáródás” helyett „kimaradás”.
  - 1234 címkéje: „ütközés”.
  - 1235: „legyen mód lassabban vagy ülve, jelzéssel is részt venni, a lassabb gyerek se essen ki.”
  - 1231: „…mert ha 10–12 évesek teljes erőből futnak a fix falakhoz, az könnyen…”.
  - A biztonsági tartalom nem változik.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-209
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:1084-1085` (vö. 340, 863, 865, 868); kártyák: 617 ↔ 631, 835/1058 ↔ 1050
- **Probléma:** A narráció végig egyes szám 2. személyben szól, a SLIDE 6-on viszont hirtelen többes 2. személyre vált. A párhuzamos példakártyák felváltva „ti” és „ők” nézőpontból írnak (6. regressziós minta).
- **Bizonyíték:** `> Használjatok fiktív, nem beazonosítható esetet,` / `> és kívülről nézzétek meg a szereplők döntéseit.`
- **Hatás:** Nem egyértelmű, kinek szól az utasítás: a tanulónak, a madrihcsapatnak vagy a kvucának.
- **Javaslat:**
  - 1084: „Használj fiktív, nem beazonosítható esetet,”. Ha a 1085. sor a közös elemzést jelenti, nevezd meg a kvucát (pl. „és a kvucával kívülről nézzétek meg…”). A „fiktív eset, kívülről” védelmi tartalom marad.
  - Kártyák a többségi „ti” alakra: 631 „zenére szabadon mozogtok”, 1050 „körben válaszoltok”.
  - A 1061–1064. sor nem változik.
  - A narráció változása VO-újrarenderelést igényel.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-210
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:327` (spec: 236)
- **Probléma:** A felolvasott alt-szövegben akadémikus „heurisztika” áll, a lecke tanulói szövege ugyanerre a „kiindulópont” szót használja (620, 1212). A beágyazott idézet »…«, nem a normás ‘…’.
- **Bizonyíték:** `Minden sor mellett: »heurisztika, a konkrét kvucához igazítsd«.”**`
- **Hatás:** A képernyőolvasót használó tanuló más, zsargonos szót kap, mint a látó tanuló, így egy fogalomra két megnevezés jut.
- **Javaslat:** A 327. és a 236. sorban egyezően: „Minden sor mellett: ‘kiindulópont, a konkrét kvucához igazítsd’.” Megjegyzés az implementációs lencsének: az alt-szöveg olyan sorfeliratot ír le, amely a 320–322. sor látható szövegében nincs meg. Ezt nyelvi javítás nem dönti el.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-211
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:876, 878, 880, 1233`; `02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md:186`
- **Probléma:** Három szóhasználati gond van a biztonsági minimumban:
  - Az „akadálymentes” a magyarban elsősorban fogyatékossággal élők számára hozzáférhető teret jelent, itt viszont „akadályoktól mentes” értelemben áll.
  - A „Tiszta … tér” és az „állítsd be ezt a négy alapot” tükörfordítás.
  - A „vezető” szót a korpusz a madrihra is használja, itt viszont a párban vezető társat jelenti.
- **Bizonyíték:** `> * **Tiszta, akadálymentes tér** – nincs útban szék, asztal, kábel, lépcső.` / `> * **A vezető végig hangosan jelez** – mondja, merre megy a társa („balra fordulunk”).`
- **Hatás:** Egy biztonsági minimum kulcsszava kétértelmű, és a képző a hangos jelzést a madrih feladatának olvashatja.
- **Javaslat:**
  - 876: „biztosítsd ezt a négy alapfeltételt”.
  - 878: „**Szabad, akadályoktól mentes tér**”.
  - 1233: „tág, akadályoktól mentes terület”.
  - 880: „**A vezető társ végig hangosan jelez**”.
  - A kapu 186. sora ugyanezt a négy elemet idézi, azzal együtt változzon (7. minta).
  - A négy elem tartalma és sorrendje változatlan.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-212
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:887`
- **Probléma:** A kimaradás lehetőségét leíró beleegyezési mondatból hiányzik az ige („lehet nyitott szemmel…”), és a „bekötni” tárgy nélkül áll.
- **Bizonyíték:** `senkinek nem kötelező becsukni a szemét vagy bekötni; aki nem akarja, lehet **nyitott szemmel, lassított verzióban** vagy **megfigyelő-szerepben**.`
- **Hatás:** Felolvasva döccen az egyik beleegyezési instrukció.
- **Javaslat:** „senkinek nem kötelező becsukni vagy bekötni a szemét; aki nem akarja, részt vehet **nyitott szemmel, lassított verzióban**, vagy lehet **megfigyelő**.” A kiemelés szerinti kétféle lehetőség megmarad, a „Ki lehet maradni” védelem nem változik.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-213
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:1452, 1392` (spec: 1301)
- **Probléma:** A „korosztálynak használnád” vonzata tükörfordítás; a lecke máshol „korosztálynál” vonzattal kérdez (672, 1194). A narráció ugyanerre a kérdésre más igét használ („adnád”).
- **Bizonyíték:** `> **Melyik korosztálynak** használnád legszívesebben,` / `> melyik korosztálynak adnád inkább,`
- **Hatás:** A „használ valakinek” jelentése a magyarban ‘hasznára van’ is, és a narráció más kérdést tesz fel, mint a feladat.
- **Javaslat:** 1452: „**Melyik korosztálynál** használnád legszívesebben,”. 1392: „melyik korosztálynál használnád inkább,”. A 1301. sori spec egyezően. A narráció változása a hanggyártást is érinti.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-214
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:928, 1055, 1075` (vö. 453, 488, 1388, 1423)
- **Probléma:** A SLIDE 6 a „Kategória-kártya 3” címet viseli, de a B kártya nem az 5. kategória nevén szerepel, hanem „Összetettebb, érzékenyebb téma” / „mélyebb téma” néven. A példa (fiktív eset kívülről elemzése) nem is élményjáték.
- **Bizonyíték:** `### SLIDE 6 – Kategória-kártya 3: reflexiós vs. mélyebb téma` / `**B – Összetettebb, érzékenyebb téma**`
- **Hatás:** Megszakad a megfeleltetés az öt kategória és a kártyák között. A Check 2. kérdése és a záró narráció „mély élményjátékról” kérdez, ezt a SLIDE 6 nem nevezi meg.
- **Javaslat:** EMBERI DÖNTÉS (projektgazda / a lecke tartalmi gazdája): a B kártya az 5. kategória példája-e, vagy külön forma („érzékeny téma feldolgozása”). Utána a 928., 1055. és 1075. sor megnevezése ehhez igazítható. Bármelyik döntésnél érintetlen marad a 1061–1064. sori biztonsági minimum, és kirekesztést eljátszó vagy szimuláló példa nem kerülhet a fiktív eset helyére (M6-invariáns).
- **Típus:** emberi-döntés
- **Verdikt:** —

### NYELV-215
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md:320, 452`
- **Probléma:** Két rövid leíró sor homályos vagy tükörfordítás:
  - 320: nem derül ki, kinek a figyelméről van szó, és fókuszt vagy odafigyelést jelent-e.
  - 452: névelő nélküli, angolos szerkezet.
- **Bizonyíték:** `az egyéni figyelem és igény ettől eltérhet.` / `– könnyebb út témák felé, megosztás.`
- **Hatás:** A korosztályi figyelmeztetés és a reflexiós kategória célja nem olvasható ki egyértelműen.
- **Javaslat:** 320: „a gyerekek figyelme és igényei egyénenként eltérhetnek.” (vö. M3.2:16 „milyen egy gyerek figyelme”). 452: „– témanyitás könnyű kérdésekkel, megosztás.” (a 485. narrációs sor alapján).
- **Típus:** objektív
- **Verdikt:** —

## G3 – M6.2 (NYELV-301…314)

### NYELV-301
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:778` (SLIDE 6, „Fontos” doboz)
- **Probléma:** A gyermekvédelmi doboz a kanonikus 2. lépést („Hallgasd meg”) „nyugodtan meghallgatod” alakban adja vissza. Ezt megengedésként is lehet érteni („nyugodtan meg is hallgathatod”). A „többek között” kezdetű, saját szavakkal írt négyelemes felsorolás eltér a HUM-SAFE-01 szó szerinti szövegétől.
- **Bizonyíték:** „az **ötlépéses jelzési utat** követed (M3.B lépéstérkép) – többek között nyugodtan meghallgatod, nem faggatod, **nem ígérsz teljes titoktartást**, és **azonnal bevonod a kijelölt Memunát**”
- **Hatás:** A „nyugodtan” egy kötelező lépést választhatónak tüntethet fel. A felsorolásból kimarad az 1. lépés (észleld, vedd komolyan) és az 5. lépés (közvetlen veszélynél 112). A `Gyermekvédelem – release gate.md` §4.1 szerint „Négylépéses, csonka vagy versengő változat nem maradhat a tananyagban”.
- **Javaslat:** A nyelvi javítás minimális: töröld a „nyugodtan” szót („– többek között meghallgatod, nem faggatod, …”). Azt, hogy a „többek között” részfelsorolás megengedett utalás-e, vagy a §4.1 szerint az öt lépés szó szerinti listájára kell cserélni, a biztonság-jog lencse döntse el (ebben a futásban nem futott). Policy-szöveget nem javaslok. Nem eshet ki a titoktartási korlát, az azonnali bevonás és a Memuna első említése a zárójeles meghatározással.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-302
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:1`, `:6`, `:22`, `:544`, `:551` és maga a fájlnév. Ugyanez az alak áll itt is: `02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md:91`, `:254`; M6.1 `:1467`; M6.B `:9`; M6.F `:12`, `:195`, `:229`; `02 Tervezet/Média-assetek/VOICE-PILOT-SCRIPTS.md:135`. Az eltérő alak: `02 Tervezet/LMS – activity manifest.md:72`
- **Probléma:** A „mint” itt szerepet jelöl (a történet tükörként működik), nem hasonlít, ezért elé nem kell vessző. A cím mégis vesszővel áll, és a korpusz ingadozik a két alak között.
- **Bizonyíték:** `# M6.2 – „Történet, mint tükör”` (:1) ↔ `| M6.2 – Történet mint tükör |` (manifest:72); a hubban: „a **történet mint tükör** a kvucának” (hub:93)
- **Hatás:** Ugyanannak a leckének két címalakja van (a manifestben és a Moodle-címben). A vesszős alak hasonlításként is érthető („történet, akár egy tükör”). A korpusz párhuzamos címe vessző nélkül áll („M2.2 – Értékeim mint iránytű”).
- **Javaslat:** Egységesíts „Történet mint tükör” alakra. A fájlnév, a hublink és minden linkcímke együtt változik. Az átnevezés külön `git mv` commitban, tartalmi szerkesztés nélkül történjen (`.claude/rules/course-content.md`). A generált kimenetek `media_manifest.py build`-del frissülnek. Az útvonalat hordozó produkciós hivatkozás is követi a változást (VOICE-PILOT-SCRIPTS.md:135). Az `M6.2` azonosító nem változik.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-303
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:50` (dia címe), `:133` (M6.2-VID-01-VO narráció); a `:57` asset-cím követi
- **Probléma:** A bevezető két kifejezése tükörfordításnak tűnik. A „fagyott csend” nem bevett kifejezés, a narráció maga is „kínos csend”-et mond. A „rosszul lett tőle” magyarul elsősorban testi rosszullétet jelent, nem érzelmi megrendülést.
- **Bizonyíték:** „Meséltél már sztorit, amire fagyott csend lett?” (:50); „valaki láthatóan rosszul lett tőle,” (:133)
- **Hatás:** A diacím és a narráció két különböző képet fest ugyanarról. A „rosszul lett” rosszullétet, orvosi helyzetet idéz fel érzelmi felkavarodás helyett.
- **Javaslat:** :50 → „Meséltél már olyan sztorit, ami után kínos csend lett?” (a :57 asset-cím ezt követi); :133 → „valakit láthatóan felkavart,”. Ez az AI beszélő fejes videó narrációját változtatja meg, ezért a hanggyártást, a videót, a feliratot és a leiratot is érinti.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-304
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:154` (SLIDE 1, 1. opció)
- **Probléma:** Az „ami” a névelő nélküli „kvucának” után áll, ezért nyelvtanilag a kvucára vonatkozik, nem a sztorira.
- **Bizonyíték:** „„Meséltem már sztorit kvucának, ami nem igazán működött.””
- **Hatás:** Az opció úgy is érthető, hogy a kvuca „nem működött”, így az önreflexiós választás félreérthető.
- **Javaslat:** „Meséltem már egy kvucának olyan sztorit, ami nem igazán működött.” Az egységes visszajelzés (:161–164) nem változik.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-305
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:262` (dia-lista), `:269` (az alt-szöveg kulcsfogalma); az IKO-01 spec (`:177`) követi
- **Probléma:** Az „érzéseket elérni” tükörfordítás: nem derül ki, ki éri el kinek az érzéseit.
- **Bizonyíték:** „* segít **érzéseket** elérni, nem csak fejben gondolkodni;” / „szív = **„érzéseket elérni”**”
- **Hatás:** A dia első állítása homályos, és a képernyőolvasó az ikon alt-szövegében ugyanezt a homályos fogalmat olvassa fel.
- **Javaslat:** Vedd át a narráció saját megfogalmazását (:281–282): „* segít, hogy ne csak fejben gondolkodjanak, hanem **érezzenek** is;”. Az alt kulcsfogalma (:269) és a :177 spec ehhez igazodjon, pl. szív = „érezni, nem csak gondolkodni”. A lista és az alt együtt változzon (7. regressziós minta).
- **Típus:** objektív
- **Verdikt:** —

### NYELV-306
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:288` (M6.2-NAR-02-VO)
- **Probléma:** A mondat a „bevonódást” (azaz az elköteleződést) hátrányként említi, pedig a szövegkörnyezet a személyes kitettség csökkenéséről szól. Az „esetleg a szégyen” mellérendelés is döccen.
- **Bizonyíték:** „Kisebb a bevonódás, esetleg a szégyen, így kisebb a tét.”
- **Hatás:** Úgy hangzik, mintha a kitalált szereplő kevésbé vonná be a hanihokat, ami ellentmond a dia állításának.
- **Javaslat:** Igazítsd a dia 3. pontjához (:264: „biztonságosabb, mint rögtön saját sztorikról beszélni”), pl.: „Kevésbé érinti őket személyesen, kisebb a szégyen esélye, így kisebb a tét.” Ha a szerkesztő más szándékot olvas ki az eredetiből, ne írja át, hanem jelezze. Narrációs szöveg, ezért a NAR-02 hanganyagát, feliratát és leiratát is érinti.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-307
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:502–506` (M6.2-NAR-04-VO)
- **Probléma:** Két hiba van benne:
  - **Időrend:** azt, hogy Lili „szinte végig” csendben marad, a peula vége után mondja.
  - **Egyeztetés:** egy mondaton belül vált a számnév utáni egyes számú „odamegy” és a többes számú „mondják” között.
- **Bizonyíték:** „A peula véget ér. / Lili szinte végig csendben marad.”; „A végén két hanih odamegy a madrihhoz, / és azt mondják:”
- **Hatás:** A hallgató egy pillanatra elveszíti az időrendet, és az egyeztetési váltás felolvasva is hallatszik.
- **Javaslat:**
  - Cseréld fel az első két mondatot: „Lili szinte végig csendben marad. / A peula véget ér.”
  - A dia szövegének (:482) mintájára: „A végén két hanih odamegy a madrihhoz:”, az „és azt mondják:” sor nélkül.
  - Az idézett párbeszéd (:507–508) nem változik.
  - Hanggyártási következmény: a NAR-04 a P2 pilotszkript. A `02 Tervezet/Média-assetek/VOICE-PILOT-SCRIPTS.md:37` és `:135–137` sorai a forrás-hasht, a szószámot (71) és a sorszámokat rögzítik, ezek a módosítás után elavulnak.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-308
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:521` (kérdés), `:539` (visszajelzés más válaszra)
- **Probléma:** A „fő helyzet” nem bevett kifejezés, valószínűleg tükörfordítás. A kérdés és a visszajelzések két különböző szót használnak: a :532 már „A lényeg az”.
- **Bizonyíték:** „Mi volt **a fő helyzet** ebben a történetben?”; „Igen. A lényeg az, hogy egy új hanih”
- **Hatás:** A megértést ellenőrző kérdés nehezen értelmezhető: nem világos, hogy helyszínre, szituációra vagy a lényegre kérdez.
- **Javaslat:** :521 → „Mi volt **a lényeg** ebben a történetben?”; :539 → „A lényeg az, hogy …”. Az opciók („Az, hogy …”) és a ✅ helye nem változik.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-309
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:607–608`
- **Probléma:** A két pont szerkezete nem párhuzamos: az egyik többes számú főnév, a másik alany nélküli melléknév. A második pontban a kettőspont után álló „Te voltál ilyen…” a mondatszerkezet miatt a nem szégyenítő kérdés mintájának is olvasható, pedig ellenpélda.
- **Bizonyíték:** „* **nyitott kérdések** → többféle jó válasz lehetséges;” / „* **nem szégyenítő** → nem mutat rá egy emberre: „Te voltál ilyen…””
- **Hatás:** A dián épp a kerülendő megszólítás jelenhet meg mintaként. A narráció (:634–635) és az M6.B (:358) ellenpéldaként kezeli.
- **Javaslat:** „* **nyitott kérdés** → többféle jó válasz lehetséges;” / „* **nem szégyenítő kérdés** → nem mutat rá egy konkrét emberre (nem így: „Te voltál ilyen…”).” A „konkrét” szót a :657 visszajelzés és a kapu is használja.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-310
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:645`
- **Probléma:** Diákra bontott H5P-ben a „fenti történet” nem a történetre mutat: az a 3–4. dián volt, ezen a dián feljebb a kérdésminták listája áll.
- **Bizonyíték:** „Melyik kérdés **nyitott és nem szégyenítő** a fenti történet után?”
- **Hatás:** A tanuló a „fenti” szót a dián feljebb álló mintakérdésekre értheti.
- **Javaslat:** „… a Liliről szóló történet után?” (a :899 megnevezését követve). A ✅ és a visszajelzések nem változnak.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-311
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:667` (dia címe), `:36`, `:769`, `:773`, `:775`; a `:676` (DIA-01 spec) és a `:712` (asset-cím) követi
- **Probléma:** A tanulói szövegben perjeles felsorolás áll mondat helyett. A „nyelv” itt a megfogalmazás módját jelenti, de egy héber szavakkal dolgozó mozgalomban idegen nyelvként is érthető. A :775 pontban a „töltet … kvucának” vonzata sem áll össze.
- **Bizonyíték:** „Nem minden téma / nyelv jó minden korosztálynak” (:667); „* erősen vallási / politikai töltet fiatalabb kvucának;” (:775)
- **Hatás:** A cím kétértelmű, a listapontok nem olvashatók fel mondatként.
- **Javaslat:**
  - :667 → „Nem minden téma és nyelvezet jó minden korosztálynak”
  - :36 → „nem minden téma és nem minden nyelvezet”
  - :769 → „nincs részletezett erőszak vagy trauma”
  - :773 → „túl sötét vagy traumatikus történet”
  - :775 → „erősen vallási vagy politikai töltetű téma fiatalabb kvucánál”

  A DIA-01 ábra feliratai az élő szöveget követik. A narráció :793-as sora („érthető, konkrét nyelv”) nem változik.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-312
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:903` (SLIDE 7, „Biztonságos megosztás”). Ugyanez a mondat áll az M6.4 `:1019` sorában is; az másik reviewercsoporté.
- **Probléma:** A tanulónak szóló adatvédelmi mondat belső governance-nyelven szól („éles kurzus”, „jóváhagyott adatvédelmi beállítás”, „mezőhöz való hozzáférés”), és nem mondja meg, ki látja a válaszát.
- **Bizonyíték:** „A mezőhöz való hozzáférést az éles kurzus jóváhagyott adatvédelmi beállítása szabályozza.”
- **Hatás:** A tanuló nem tudja eldönteni, mennyit írjon. A staging és az éles kurzus megkülönböztetése fejlesztői fogalom (`Emberi jóváhagyás szükséges.md:10`).
- **Javaslat:** Vezesd át tanulói nyelvre a lezárt HUM-PRIV-01 döntést. Forrásai: `02 Tervezet/LMS – activity manifest.md:16`, `:27` és az Adatvédelem-dokumentum §5-e. Eszerint a szabad szöveges H5P-C adat P2-es, és csak a kijelölt mentor vagy értékelő látja, csak ha ténylegesen szükséges. A korpusz meglévő mondata: „A válaszaidat csak a kijelölt mentorod láthatja, és csak akkor, ha ténylegesen szükséges.” (`02 Tervezet/Modulok/M4/Online leckék/M4.2 – Aktív hallgatás & visszatükrözés.md:894`). Ha a verifier szerint a mező nem a P2-sor alá esik, akkor EMBERI DÖNTÉS: a mező láthatóságáról a DPO vagy az adatvédelmi felelős dönt, és addig a mondat tartalmát nem szabad kitalálni. A „ne írj bele konkrét nevet…” védőmondat marad.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-313
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:900` ↔ `:926` (M6.2-NAR-07-VO)
- **Probléma:** A narrációból kimarad a dia pontosító szövege, így hangban a feladat csak a saját kvucára szól (2. regressziós minta; a baseline nem ismert).
- **Bizonyíték:** „**a saját kvucádnak vagy egy elképzelt, de valószerű kvucának** meséled el.” ↔ „a saját kvucádnak meséled el.”
- **Hatás:** Akinek még nincs kvucája, a hang alapján kizárva érezheti magát, pedig a korpusz másutt kifejezetten felkínálja a kitalált kvucát (M4.4:704).
- **Javaslat:** :926 → „a saját kvucádnak – vagy egy elképzeltnek – meséled el.” Narrációs szöveg, ezért a NAR-07 hanganyagát, feliratát és leiratát is érinti. A gondolatjeles beszúrás egyben szünetet is ad (VO D-10).
- **Típus:** objektív
- **Verdikt:** —

### NYELV-314
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md:965` (2. elosztó), `:971–972` (visszajelzés más válaszra)
- **Probléma:** A közös visszajelzés csak az előre megmondott tanulságot cáfolja, a 2. elosztót (a tanulságot a végén mondják el) nem fedi le.
- **Bizonyíték:** „Az, hogy a végén pontosan, félreérthetetlenül elmondjuk a kvucának, mit kell gondolnia róla.”; „nem a dráma, és nem az, hogy előre megmondod a tanulságot.”
- **Hatás:** Aki a 2. opciót választja, olyan visszajelzést kap, amely nem a saját tévedéséről szól (7. regressziós minta).
- **Javaslat:** :972 → „nem a dráma, és nem az, hogy előre vagy a végén megmondod a tanulságot.” Az opciók szövege és a ✅ helye nem változik.
- **Típus:** objektív
- **Verdikt:** —

## G4 – M6.3 (NYELV-401…413)

Mind a 13 finding a fenti fájl 1–1202. soraiból való, a teljes fájlt elolvastam. A P1-esek közül kettő someres tartalmi kérdés (NYELV-401, NYELV-404), ezekhez a projektgazda vagy a someres tartalomgazda döntése kell, mielőtt bárki szöveget írna.

**NYELV-401**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:727` (SLIDE 4, „Cél: mit tanít?”)
- **Probléma:** A *dugma isit* itt annak a része, amit a karkötő a hanihnak tanít: a hanih saját identitásának vállalása. A Glosszárium viszont a madrih élőben látott példamutatásaként határozza meg. A magyarázat ráadásul első személyre vált („értékeim”), pedig a felsorolás a hanihokról szól.
- **Bizonyíték:** 727: „(önkifejezés, *dugma isit*, azaz személyes példamutatás – a vállalt értékeim megélése, képviselete)”. Glosszárium, 24. sor: „személyes példamutatás; a hanihok abból tanulnak, amit a madrihon **élőben** látnak”
- **Hatás:** A tanuló egy központi someres fogalmat a kánoni jelentésétől eltérően tanul meg (mintha a hanihnak lenne „dugma isitje”). Az sem derül ki, kinek az értékeiről szól az „értékeim”.
- **Javaslat:** EMBERI DÖNTÉS: a projektgazda vagy a someres tartalomgazda döntse el, hogy a *dugma isit* ide tartozik-e, és ha igen, kinek a szerepében. A döntésig nyelvi szöveget ne javasoljunk. Az „értékeim” személyét a döntés után kell egyeztetni. A sor egalitásról szóló második fele nem érintett.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-402**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:734` (SLIDE 4, „Inkluzivitás: mire figyelj?”)
- **Probléma:** A szorongó vagy nyelvi nehézséggel küzdő hanih első kiváltó lehetősége értelmezhetetlen. A karkötőt maga a hanih viseli, így nem derül ki, mit mondhat a jelentés elmondása helyett.
- **Bizonyíték:** „az mondhatja csak a viselő nevét, párban súghatja, vagy szó nélkül felmutathatja.”
- **Hatás:** A nem kötelező önfeltárás egyik lehetőségét a madrih nem tudja végrehajtani, vagy félreérti. Ezzel gyengül a kiskorúnak felkínált kilépési lehetőség.
- **Javaslat:** Szövegjavaslat nincs (regressziós minta 8): a tartalomgazda mondja meg, mi az első lehetőség. Javítási korlát: a „**ne legyen kötelező**” kitétel és a másik két lehetőség (párban súgás, szó nélküli felmutatás) szó szerint marad.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-403**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:193`, `:379`, `:550`, `:749`, `:957`, `:1100` (a leirat-sor mind a hat narráció előtt)
- **Probléma:** A sor szerint a leirat „a médiaelem mellől elérhető”. Ez gyengébb a lezárt VO D-19 „mellett látható” követelményénél, mert linkelt vagy rejtett leiratot is megenged. Ráadásul ugyanabban a mondatban kétszer szerepel az „elérhető”.
- **Bizonyíték:** 193: „**Teljes szöveges leirat a dián vagy a médiaelem mellől elérhető szövegként, magyar nyelven – a hangtartalom hang nélkül is elérhető.**” A `PRODUCTION-DECISIONS.md` VO D-19 sora: „a dián vagy a médiaelem mellett látható leirat a szöveges ekvivalens”
- **Hatás:** A build a lezárt döntésnél gyengébb leiratot valósíthat meg (csak elérhetőt, nem láthatót). A lecke a saját asset-jegyzetének is ellentmond (144. sor: „mellett látható leirat”).
- **Javaslat:** A hat sorban a „mellől elérhető szövegként” helyére „mellett látható szövegként” kerüljön (a VO D-19 szó szerinti átvezetése). A sor többi része marad: magyar nyelven, a hangtartalom hang nélkül is elérhető. Ugyanez a sor az M6.1-ben és az M6.2-ben is 8–8 alkalommal szerepel; azokat a saját csoportjuk reviewere jelzi. Ha a sor tanulónak látható, a látható szöveg pinje is változik. Nem narráció, a hanggyártást nem érinti.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-404**
- **Súlyosság:** P1
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:934` és `:938` (SLIDE 5, „Cél: mit tanít?” és „Inkluzivitás: mire figyelj?”)
- **Probléma:** Három gond van ezzel a ponttal:
  - A „Somer saját zászló- és színhagyományára” való hivatkozásnak a korpuszban nincs más forrása (a `02 Tervezet/Modulok` alatt egyetlen további találat sem).
  - A pontot záró meta-mondat („nem váltja ki, hanem kiegészíti”) korábbi szerkesztői betoldás nyomának látszik (regressziós minta 8).
  - Az „ezt” nem dönti el, hogy a mozgalmi jelképekre vonatkozik-e a következő pont (vallási/politikai jelképek) érzékenységi szabálya.
- **Bizonyíték:** 938: „a Somer saját **zászló- és színhagyományához** is kapcsolódik (a mozgalmi identitás vállalt jelképe)”, illetve „Az alábbi érzékenységkezelés ezt **nem váltja ki, hanem kiegészíti**;”
- **Hatás:**
  - A tanuló esetleg nem létező someres hagyományra hivatkozik.
  - Nem tudja, kivétel-e a mozgalmi (politikai) jelkép a „ne legyen senkire nézve bántó” szabály alól.
  - A rövid kulcsszó–utasítás pontokból álló felsorolásban ez az egyetlen többmondatos pont, ezért megtörik a párhuzam.
- **Javaslat:** EMBERI DÖNTÉS: a projektgazda vagy a someres tartalomgazda döntsön, mert ez helyi someres ideológiai kérdés.
  1. Van-e hivatkozható Somer zászló- és színhagyomány? Ettől függ, marad-e a 934. és a 938. sor erre vonatkozó része.
  2. Vonatkozik-e a 939. sor érzékenységi szabálya a mozgalmi jelképekre?

  Nyelvi átírás csak ezután jöhet; addig ne kerüljön a helyére új indoklás. Baseline ismeretlen.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-405**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:529` (SLIDE 3, „Cél: mit tanít?”)
- **Probléma:** A „mi van rajtunk, mi nincs” nem értelmes magyar fordulat (szó szerint: mit viselünk). Nem dönthető el, hogy a plakát tartalmára („mi van rajta”) vagy a csoport jellemzőire gondol.
- **Bizonyíték:** „* közösségi identitás (mi van rajtunk, mi nincs);”
- **Hatás:** A tanuló nem érti, mit tanít a közös plakát a közösségi identitásról.
- **Javaslat:** Szövegjavaslat nincs; a tartalomgazda tisztázza a szándékot (vö. a 932. sor párhuzamos fordulatával: „mi kerül rá, mi nem”). A felsorolás többi pontja változatlan.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-406**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:743` (SLIDE 4, „Fontos:” gyermekvédelmi doboz)
- **Probléma:** A teendőket egyetlen mondat sorolja fel, amelyet kettőspont, gondolatjel, zárójel és a zárójelen belül újabb gondolatjel tagol. Így a lépések sorrendje nehezen követhető.
- **Bizonyíték:** „az **ötlépéses jelzési utat** követed (M3.B lépéstérkép) – többek között nyugodtan meghallgatod (de **NEM faggatod ki a részletekről** – *meghallgatni szabad, kihallgatni nem*), **nem ígérsz teljes titoktartást**,”
- **Hatás:** A helyzetben olvasó madrih könnyen átsiklik egy lépésen, például a Memuna azonnali bevonásán vagy azon, hogy a gyermek saját szavait adja tovább.
- **Javaslat:** Az „Ott már … adod tovább neki.” szakaszt bontsd mondatokra, például: „Ilyenkor az ötlépéses jelzési utat követed (M3.B lépéstérkép). Többek között: …”. Minden elem szó szerint marad:
  - a meghallgatás és a faggatás tilalma, a szállóigével együtt;
  - nincs teljes titoktartás-ígéret;
  - a Memuna azonnali bevonása, a magyarázó zárójellel együtt;
  - továbbadás a gyermek saját szavaival;
  - a dokumentációs korlát;
  - „Madrih vagy, nem terapeuta.”

  Védelmi elemet rövidíteni vagy elhagyni tilos (regressziós minta 2 és 9).
- **Típus:** objektív
- **Verdikt:** —

**NYELV-407**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:1092–1094` (SLIDE 6, Kérdés 3)
- **Probléma:** A nyitott kérdés egyetlen hosszú, beágyazott jelzős szerkezet, és kétszer utal ugyanarra az előző kérdésre („épp az imént”, „(az előző kérdésben)”).
- **Bizonyíték:** „„Írj 1 **variációt**, amivel épp az imént (az előző kérdésben) megnevezett” / „nehézséggel küzdő hanihnak adsz”
- **Hatás:** Mobilon nehezen olvasható, felolvasva követhetetlen. A tanuló elveszítheti a fonalat, melyik hanihra és melyik célra írja a variációt.
- **Javaslat:** Két mondat, változatlan tartalommal: „Gondolj arra a hanihra, aki az előző kérdésben megnevezett nehézséggel küzd. Írj egy **variációt**, amellyel **másik belépési pontot adsz neki ugyanahhoz a célhoz** (amit az 1. kérdésre írtál).” A „másik belépési pont ugyanahhoz a célhoz” fordulat (az R5 rubrikasor nyelve) szó szerint marad, és továbbra is egy variációt kér.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-408**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:1106–1107` (SLIDE 6 narráció, M6.3-NAR-06-VO)
- **Probléma:** A közbeszúrás két tagja nem párhuzamos. A „példák közül” határozó mellé tárgyeset kerül („egy saját ötletet”), így a mondatnak két tárgya lesz.
- **Bizonyíték:** „> Válassz ki egy kézműves feladatot” / „> – akár a példák közül, akár egy saját ötletet –,”
- **Hatás:** Hallva döccen, és a leirat nyelvtanilag hibás. A dián lévő instrukció (1074–1077. sor) ugyanezt helyesen fogalmazza meg, így a kettő eltér.
- **Javaslat:** „– akár a példák közül, akár a saját ötleteid közül –,”. A központozás (gondolatjelek, vessző) nem változik. Ez narrációs szöveg, ezért a hanggyártást is érinti (újrarenderelés), és a látható szöveg pinje is változik.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-409**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:940` (SLIDE 5, „Inkluzivitás: mire figyelj?”)
- **Probléma:** A pont főnévi igenévvel („vigyázni”) tér el a lista tegező felszólító szerkezetétől, és hiányzik a „ne váljon” alanya: nem derül ki, mi ne váljon megalázó poénná (regressziós minta 1).
- **Bizonyíték:** „* humor: vigyázni, hogy ne váljon megalázó poénná valaki rovására („rajta röhögünk a zászlón”);”
- **Hatás:** A tanulónak ki kell találnia, mi ne váljon megalázó poénná. A felsorolás hangneme megbicsaklik.
- **Javaslat:** „* humor: vigyázz, hogy a humor ne váljon megalázó poénná valaki rovására („rajta röhögünk a zászlón”);”. A példaidézet változatlan.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-410**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:1149–1157` és `:1167–1175` (SLIDE 7, Check, Kérdés 1 és 2)
- **Probléma:**
  - A Kérdés 2 opciói közül egyedül a helyesként jelölt szól tegező második személyben. A többi személytelen, vagy harmadik személyben beszél a madrihról.
  - A Kérdés 1 helyes opciója többes szám első személyben áll („átgondoljuk”), a visszajelzés viszont második személyben („átgondolod”).
- **Bizonyíték:** 1169: „„Ha látod, hogy valakinek nehéz a feladat, kínálsz neki másik belépési pontot ugyanahhoz a célhoz.””. 1168: „„Elég, ha a madrih a kör legelején egyszer kimondja, hogy itt senki ne érezze magát kirekesztve.””
- **Hatás:** A nyelvtani eltérés elárulhatja a helyes választ, ami gyengíti az önellenőrzést. A kérdés és a visszajelzés személye is elcsúszik (regressziós minta 7).
- **Javaslat:** EMBERI DÖNTÉS: az értékelési felelős döntse el, egységesíthető-e az opciók személye. Javítási korlát: a helyes válasz jelölése nem mozdul, az opciók tartalma nem változik, disztraktor nem cserélhető. Legfeljebb a személyrag egységesítése jöhet szóba, a hozzá tartozó visszajelzéssel együtt.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-411**
- **Súlyosság:** P2
- **Bizalom:** alacsony
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:1185` (SLIDE 7, Mini-reflexió)
- **Probléma:** A zárójeles szempontlista („cél, kérdések, inkluzivitás”) eltér a leckében végig használt alapkerettől (cél – inkluzivitás – variációk). Nem derül ki, mit jelentenek itt a „kérdések”.
- **Bizonyíték:** 1185: „> Írj 1 mondatot arról, mit változtatnál rajta (cél, kérdések, inkluzivitás).”. 361: „Alapkeret: cél – inkluzivitás – variációk.”
- **Hatás:** A tanuló nem tudja, mit jelent változtatási szempontként a „kérdések”. A záró reflexió így nem a tanult kerethez kapcsol vissza.
- **Javaslat:** Szövegjavaslat nincs. A tartalomgazda döntse el, hogy a „kérdések” elírás-e (ekkor az alapkeret hármasa kerül ide), vagy szándékosan más szempont (ekkor meg kell nevezni, mely kérdésekről van szó).
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-412**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:1200`, `:595`, `:998`
- **Probléma:** Tanulónak szóló teljes mondatokban „+” és „/” áll kötőszó helyett.
- **Bizonyíték:** 1200: „hogy egy adott **kvuca + cél + körülmény** mellett”. 595: „és a végén nehéz hová kitenni / felragasztani a kész plakátot.”
- **Hatás:** Jegyzetszerűen hat, felolvasva nem mondható ki természetesen. A szerkesztői norma szerint: „`+`, `/`, rövidítés-halmozás helyett rendes mondat”.
- **Javaslat:**
  - 1200: „hogy egy adott **kvucához, célhoz és körülményekhez** **játékot, történetet vagy kézművest** választanál”; a mondat folytatása változatlan.
  - 595: „kitenni vagy felragasztani”.
  - 998: „rajzok vagy feliratok”; a helyes válasz jelölése nem mozdul.

  A diák rövid felsoroláspontjaiban (pl. 535., 738. sor) a „/” maradhat.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-413**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md:37` és `:1193`
- **Probléma:** A bevezető „2–3” példát ígér, a zárás „2–3” látott példát állít. A lecke viszont pontosan hármat mutat (SLIDE 3–5), mindegyikhez kötelező kérdéssel.
- **Bizonyíték:** 37: „> 2–3 konkrét példát fogunk megnézni,”. 1193: „* láttál 2–3 konkrét **kézműves példát**,”
- **Hatás:** A visszatekintő összegzés pontatlan; a tanuló azt gondolhatja, kihagyott valamit.
- **Javaslat:** A két tanulói mondatban a „2–3” helyére „három” kerüljön. Ez számváltozás, ezért ez a finding indokolja külön. A modulhub tervezési sávja (`M6 – Eszköztár…md:108`: „2–3 konkrét kézműves ötletet”) fejlesztői specifikáció, nem érintett.
- **Típus:** objektív
- **Verdikt:** —

## G5 – M6.4 (NYELV-501…515)

### NYELV-501
- **Súlyosság:** P1
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:826–828 és :1014
- **Probléma:** Ugyanaz a gyermekvédelmi blokk kétszer szerepel a fájlban, ellentétes kiváltó feltétellel. Az 5D-J oldalon a puszta „kibillenés” a „nemcsak … hanem” miatt kifejezetten nem indítja el a jelzési utat. A záró prompt 3. pontjában a „vagy láthatóan kibillen” miatt viszont önmagában is elindítja.
- **Bizonyíték:** „ha valaki közben nemcsak „kibillen”, / hanem valós, súlyos témát (…) tár fel” (826–827) ↔ „tár fel vagy láthatóan kibillen, az már **nem játék**” (1014)
- **Hatás:** Egyetlen leckén belül két különböző szabályt tanul a madrih arról, mikor kell követnie az ötlépéses jelzési utat és bevonnia a Memunát: az egyik alul-, a másik túleszkalál. Ez a 2. regressziós minta (elveszett vagy megváltozott minősítő). Mellékes eltérés: „meghallgatod” (828) ↔ „nyugodtan meghallgatod” (1014). Összevetésül: az M6.2:778 és az M6.3:743 csak a feltárást vagy felhozást nevezi kiváltónak, az M0.A:129 a kibillenést külön mini-protokollal kezeli.
- **Javaslat:** EMBERI DÖNTÉS: a projektgazda a Memunával döntse el, hogy feltárás nélkül a kibillenés is kiváltja-e az ötlépéses jelzési utat. A döntés után a két blokk szó szerint egyezzen. Nyelvi javítás címén egyik változatot se válaszd ki, és ne írj policy-szöveget. A blokkok egyik eleme sem törölhető (jelzési út, a teljes titoktartás ígéretének tilalma, a Memuna azonnali bevonása, az elérhetőség).
- **Típus:** emberi-döntés
- **Verdikt:** —

### NYELV-502
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:259–262
- **Probléma:** Nem dönthető el, mire vonatkozik a „viselni”. A „mondunk / mutatunk” tárgya nem „viselhető”, ezért nem derül ki, hogy a szabály a saját választott névre vagy mozdulatra, a másra ragasztott becenévre, vagy általában a játékban elhangzottakra vonatkozik.
- **Bizonyíték:** „és jelezd, hogy csak olyat mondunk / mutatunk, / amit **jó érzés viselni**.”
- **Hatás:** A madrih nem tudja egy az egyben továbbadni a szabályt a 10 éveseknek, így az inkluzivitási instrukció nem hajtható végre.
- **Javaslat:** EMBERI DÖNTÉS: a lecke tartalomfelelőse (projektgazda) tisztázza, mit „visel” a gyerek. Addig nincs szövegjavaslat (8. minta). A „gúnyolódó névválasztás / mozdulat” tilalma maradjon.
- **Típus:** emberi-döntés
- **Verdikt:** —

### NYELV-503
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:660–664
- **Probléma:** Az 5C-T oldal „Miért lehet jó döntés?” szakaszának két pontja előzmény nélküli utalásra épül. Nem derül ki, mihez „hasonló” az összegzés, és mire mutat az „ilyen pillanat”.
- **Bizonyíték:** „ami egy hasonló összegzésről szól,” (661) / „„nektek mi volt ma ilyen pillanat?”” (664)
- **Hatás:** A tanuló nem tudja, milyen történetet válasszon napzárásra. A kvucának felolvasott minta-kérdés értelmetlen. Kiesett szövegrész gyanúja (3. és 9. minta); a baseline ismeretlen.
- **Javaslat:** EMBERI DÖNTÉS: a tartalomfelelős adja meg a hiányzó előzményt (milyen történetről, milyen pillanatról van szó). Szövegjavaslat nincs; a két pont szerkezete maradjon.
- **Típus:** emberi-döntés
- **Verdikt:** —

### NYELV-504
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:348–350, :442–447, :535–544, :918–924
- **Probléma:** Az inkluzivitási tippek egy ponton belül váltogatják a személyt: a madrihnak szóló „te”, a többes „ti” és a harmadik személyű „ők” keveredik. Ilyen a „csinálhatjátok → mozoghatnak”, a „ne ossz ki → ne hagyjatok ki”, a „mondjátok ki / dolgozzatok / rakjátok össze → figyelj”, valamint az „osszátok / dolgozhattok / menjetek végig”.
- **Bizonyíték:** „– **ne ossz ki „kirekesztett” vagy „kirekesztő” szerepet** a résztvevőknek, / és ne hagyjatok ki senkit demonstrációként.” (444–445)
- **Hatás:** A „dolgozzatok először kis csoportokban” típusú utasításból nem derül ki, hogy a madrih vagy a kvuca a címzett. Az M6 kirekesztésszimulációs tilalmánál elcsúszik, kinek szól a tilalom (6. minta).
- **Javaslat:** Pontonként egy címzett legyen. A madrihnak szóló utasítás egyes szám 2. személyben álljon, a kvuca cselekvése 3. személyben (pl. „dolgozzanak először kis csoportokban”, „csinálhatják állva … így mozoghatnak is”). A közös cselekvés „közösen” + „ti” alakban maradhat. A 445. sor tiltása tartalmilag nem gyengülhet (pl. „és ne hagyj ki senkit demonstrációként”), és a „harmadik személyben maradás” szabálya is marad.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-505
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:953 (továbbá :949, :972)
- **Probléma:** Három gond van a záró oldal keretszövegében:
  - A „két alapreflex” zárójeles felsorolása nem párhuzamos: egy főnévi szerkezet áll egy mellékmondattal szemben.
  - Ugyanez a fogalom két mondattal később „alapelv” néven tér vissza.
  - A „biztonságot és inkluzivitást nézünk” és a „szempontokat (is) nézni” tükörfordítás. Ide tartozik a vonzathiba is: „egy saját eszközön mutatod meg”.
- **Bizonyíték:** „megvan-e a két alapreflex (előbb a cél és a kvuca, és hogy miért nézünk biztonságot és inkluzivitást)” / „**ez a két alapelv** a biztonságos munkánk minimuma”
- **Hatás:** Nehezen olvasható, és a 2. kérdés „nézni” szava eltér a saját visszajelzésétől, amely „figyelünk”-et mond (983).
- **Javaslat:**
  - „…megvan-e a két alapreflex: előbb a cél és a kvuca; és az, hogy miért figyelünk a biztonságra és az inkluzivitásra.”
  - „ez a két alapelv” → „ez a két alapreflex”
  - „egy saját eszközön” → „egy saját eszközzel”
  - 949: „szempontokat is nézel” → „szempontokra is figyelsz”
  - 972: „szempontokat is nézni” → „szempontokra is figyelni”

  Az opciók, a ✅ és a visszajelzés nem változik (7. minta). A „biztonságos munkánk minimuma” indoklásához nyelvi címen ne nyúlj (8. minta): az, hogy az 1. elv biztonsági elv-e, tartalmi kérdés.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-506
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:978 és :983
- **Probléma:** A 2. kérdés helyes válasza és a visszajelzése is a „kirekesztve … érezze magát” szerkezetet használja. Ez a „feel excluded” tükre; magyarul „kirekesztettnek érzi magát”.
- **Bizonyíték:** „„Mert így kisebb az esély, hogy valaki kirekesztve vagy veszélyben érezze magát.” ✅”
- **Hatás:** A kvíz helyes válaszában természetellenes magyar áll. Ha csak az egyik helyen javítják, az opció és a visszajelzés eltér egymástól (7. minta).
- **Javaslat:** Mindkét helyen „kirekesztve” → „kirekesztettnek”. A ✅ helye, az opció jelentése és a többi opció változatlan.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-507
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:52, :175, :260–261, :411, :469, :573, :602, :753, :782–783, :847, :901, :948, :992, :998, :1011, :1016
- **Probléma:** A tanulói szövegben „+”, „/” és „&” áll kötőszó helyett. Több helyen nem dönthető el, hogy „és” vagy „vagy” értendő.
- **Bizonyíték:** „🎯 **Cél: lezárás & közös reflektálás**” (573) / „amellyel dolgozni fogsz / szeretnél dolgozni.” (998)
- **Hatás:** A szöveg darabos. A „felelősségről / társadalmi kérdésekről” (175, 753) és a „tanuljanak / tapasztaljanak” (1011) jelentése bizonytalan.
- **Javaslat:** Folyó mondatban kötőszó álljon:
  - 573: „lezárás és közös reflektálás”
  - 998: „amellyel dolgozni fogsz vagy szeretnél”
  - 948: „játékot, történetet vagy kézműves feladatot”
  - 1016: „mozogni, rajzolni vagy beszélni”
  - 260–261: „gúnyolódó név vagy mozdulat”, „mondunk vagy mutatunk”
  - 469 és 901: „történet vagy esetleírás”, „plakát vagy térkép”
  - 52: „az adott kvuca, cél és körülmények mellett”

  A 175., a 753. és az 1011. sorban a „/” jelentést hordoz, ezért a kötőszót a szerző válassza meg. Rövid gombfeliratban (411, 602, 782–783, 847, 992) a „+” csak hosszkorlát miatt maradjon.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-508
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:777, :800, :884, :930
- **Probléma:** A „(16–17)” korosztály zárójelben, a toldalékolt főnév után, a folyó mondat közepére ékelve ismétlődik.
- **Bizonyíték:** „**első lépésként** ehhez az idősebb Leviatán-kvucához (16–17)?” (777) / „feltennél egy idősebb Leviatán-kvucának (16–17),” (884)
- **Hatás:** A mondatok nehezen olvashatók. A minden előfordulásnál ismétlődő mechanikus beszúrás korábbi lexikai csere nyomára utal (5. minta; vö. a Glosszárium „Zorea 16+” megjegyzésével). A baseline ismeretlen.
- **Javaslat:** Folyó szövegben jelzőként álljon a kor: „ehhez az idősebb, 16–17 éves Leviatán-kvucához”, „16–17 éves Leviatán-kvucánál” stb. A korosztály minden H5P-oldalon megmarad. A `Leviatán` írásmódja és a 16–17-es tartomány nem változik (HUM-SOMER-02). A címekben (174, 741) maradhat a zárójeles alak.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-509
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:175, :753 (és a 736. sori fejléc), :437, :864
- **Probléma:** Igei tartalom szerepel főnévi szerkezetbe sűrítve. A 175. sorban a „-ről” vonzat a „gondolkodás” helyett az „elindítása” szóhoz tapad. Hasonló a „valódi személyek megnevezésébe csúszik át” és a „nincs egymásra reagálás, önreflexió”.
- **Bizonyíték:** „– Cél: gondolkodás elindítása felelősségről / társadalmi kérdésekről.” (175)
- **Hatás:** A D-szcenárió célja a választógombon és a helyzetleíráson nehezen értelmezhető.
- **Javaslat:**
  - 175 és 753: „Cél: elgondolkodtatni a kvucát a felelősségről […] a társadalmi kérdésekről” (a kötőszót lásd NYELV-507)
  - 437: „ha a beszélgetés átcsúszik oda, hogy valódi személyeket neveznek meg”
  - 864: „és senki nem reagál a másikra, nem gondolja át a saját álláspontját”
- **Típus:** objektív
- **Verdikt:** —

### NYELV-510
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:519, :521, :435, :809, :871, :877–878, :676, :1017, :617–618
- **Probléma:** Hibás vonzat vagy kollokáció:
  - „tanít közös döntést / felelősséget”
  - „az eset hasonlít a kvuca egy valódi tagjára” (az eset nem személy)
  - „nincs elég idő … nem lesz hol megbeszélni” (idő és hely keveredik)
  - „több érv is megfér” (hiányzik az „egymás mellett”)
  - „adhatsz körkérdéseket … elmondja a körnek”
  - „használhatsz jelképet (pl. egy tárgy …)” (az értelmező esete nem egyezik)
  - „hogyan tud mégis kapcsolódni?”
  - „levezetheti az utolsó feszültséget, mielőtt nyugiba mennek”
- **Bizonyíték:** „– tanít közös döntést:” (519) / „– tanít felelősséget:” (521)
- **Hatás:** A felolvasható instrukciók darabosak; a 435. és a 809. sor logikailag is pontatlan.
- **Javaslat:**
  - 519: „megtanít közösen dönteni:”; 521: „felelősségre tanít:”
  - 435: „egy valódi tag helyzetére”
  - 809: „nem lesz alkalom megbeszélni”
  - 871: „több érv is megfér egymás mellett”
  - 877–878: „tehetsz fel körkérdést is … aki szeretné, elmondja a többieknek”; a hosszú mondat két mondatra bontható, de a páros megbeszélés és az önkéntesség megmarad
  - 676: „egy tárgyat”
  - 1017: „bekapcsolódni”
  - 617–618: „a maradék feszültséget, mielőtt lenyugszanak”
- **Típus:** objektív
- **Verdikt:** —

### NYELV-511
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:679–680, :874, :185, :790, :800
- **Probléma:** A kvucának szánt minta-kérdések és néhány cím angol mondatszerkezetet követ: „What was a moment that…”, „one of the first…”, „not always first”, „lived experience”.
- **Bizonyíték:** „„Mi volt ma egy kis pillanat, amit jó volt átélni?”” / „„Mi volt valami, ami nehezebb volt, de tanultál belőle?””
- **Hatás:** A madrih szó szerint így teszi fel a kérdést a 13 éveseknek, ami természetellenesen hangzik; a címek első olvasásra homályosak.
- **Javaslat:**
  - 679: „Melyik volt ma egy olyan kis pillanat, amit jó volt átélni?”
  - 680: „Mi volt ma nehezebb, amiből mégis tanultál?”
  - 874: „Szerintetek melyik szereplő miben felelős?”
  - 185: „10 éves kvuca – az egyik első alkalom”
  - 790: „…erős, de nem mindig ezzel érdemes kezdeni”
  - 800: „erős átélt élményt” → „erős élményt”
- **Típus:** objektív
- **Verdikt:** —

### NYELV-512
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:847, :430, :478
- **Probléma:** Felesleges idegen szavak állnak a tanulói szövegben: „instant ítélet”, „a kirekesztő mechanikát”, „túl direkt”. A „direkt” köznyelvben „szándékosan” jelentésű is.
- **Bizonyíték:** „„Történet / esetleírás – gondolkodás, nem instant ítélet”” (847) / „– a tanulási cél: felismerni a kirekesztő mechanikát,” (430)
- **Hatás:** A „ha túl direkt azt sugallod” „szándékosan”-ként is olvasható; a „mechanika” játéktervezői szakszó.
- **Javaslat:**
  - 847: „azonnali ítélet”
  - 430: „a kirekesztés mechanizmusát”
  - 478: „ha túl nyíltan azt sugallod”

  Az M6 kapu „csoportmechanikák” szót használ (Kapu:103). Ha ez modulszintű terminus, modulszinten döntendő, nem itt egyedül.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-513
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:1019
- **Probléma:** A tanulónak szóló adatvédelmi tájékoztató utolsó mondata hivatali, compliance-regiszterű főnévi szerkezet.
- **Bizonyíték:** „A mezőhöz való hozzáférést az éles kurzus jóváhagyott adatvédelmi beállítása szabályozza.”
- **Hatás:** A tanuló nehezen érti, kire vonatkozik, hogy ki láthatja, amit beír.
- **Javaslat:** „Hogy ki fér hozzá a mezőhöz, azt az éles kurzus jóváhagyott adatvédelmi beállítása határozza meg.” Szerepkört vagy megőrzési szabályt nyelvi címen nem szabad beírni; a „ne írj azonosító adatot” kikötés változatlan. Ugyanez a mondat szerepel az M6.2:903-ban is, ezért vagy mindkettő változik, vagy egyik sem.
- **Típus:** objektív
- **Verdikt:** —

### NYELV-514
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:306–308, :490–495, :678–680, :873–876
- **Probléma:** A „például:” vagy „kérdezz így:” után jövő minta-kérdések ugyanazzal a nagykötőjeles sorkezdéssel, azonos szinten állnak, mint a madrihnak szóló tippek. Így megszűnik a felsorolás párhuzama: felszólító tipp és idézett kérdés kerül egy szintre.
- **Bizonyíték:** „– utána tegyél fel egyszerű kérdéseket, például: / – „Volt-e már olyan, hogy új voltál valahol?””
- **Hatás:** A H5P-oldalon a kvucának szánt kérdés a madrihnak szóló tippel azonos rangú pontnak látszik, és a képernyőolvasó sem jelzi az alárendeltséget.
- **Javaslat:** A minta-kérdések a bevezető tipp alá, alszintre kerüljenek, vagy a tipp mondatába ágyazva álljanak. A kérdések szövege nem változik (a 679–680. sorét lásd NYELV-511).
- **Típus:** objektív
- **Verdikt:** —

### NYELV-515
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md:89
- **Probléma:** A sablonos „Elakadtál?” blokk záró tagmondata tükörszerű, és nem magyaros.
- **Bizonyíték:** „– nem „vizsgázol”, a kérdés is fejlődés.”
- **Hatás:** A mondat minden online lecke elején megjelenik a tanulónak; a „kérdés = fejlődés” azonosítás magyarul döccen.
- **Javaslat:** „…a kérdezés is a fejlődés része.” A szöveg 31 online leckében azonos, ezért csak egységesen javítható. A „tanulási/programkontakt” szerepnév a 2026-10-02-i projektgazdai döntésből ered (HUM 243. sor), ahhoz nem szabad nyúlni.
- **Típus:** objektív
- **Verdikt:** —

## G6 – M6.A, M6.B (NYELV-601…615)

Mindkét fájlt végigolvastam, a kihagyott sortartomány nincs. A régi írásmódok (madrich, chanich, hagshama, dugma ishit, Leviatan) egyik fájlban sem jelennek meg.

Fájlok:
- **A** = `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md`
- **B** = `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md`

**NYELV-601**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:176`
- **Probléma:** A játékválasztási szűrő „Kerüli” pontjában nem dönthető el, mit jelent a „tét nélkül”. Lehet feltétel (csak a tét nélküli kiesős játékot kerüli), és lehet feltétel nélküli tilalom is. A „vesztes-csináló” tükörfordítás.
- **Bizonyíték:** „a kiesés-alapú (vesztes-csináló) játékot tét nélkül” (176). Vö.: „A kieséses / felállásra kényszerítő verzió a rossz minta.” (572)
- **Hatás:** A képző két különböző szabályt olvashat ki ebből a biztonsági szűrőből. A feltételes olvasat beengedi a téttel bíró kiesős játékot, ez pedig ütközik az 572. sorral.
- **Javaslat:** EMBERI DÖNTÉS: a peula tartalomfelelőse mondja meg, melyik szabály érvényes. Addig ne írj helyette szöveget. A döntés után a „vesztes-csináló” is magyarosítandó. A tétel másik két eleméhez nem szabad nyúlni: a kötelező fizikai kontaktushoz és az identitásra, testre vagy családi-anyagi helyzetre építő állításhoz.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-602**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:565` (ugyanez a tétel: a 523. sor, `M6.B-MUNK-06` spec)
- **Probléma:** A „kinek jelzel” a gyermekvédelmi jelzés szókincséből jön, az „elbizonytalanodik” viszont alkotói bizonytalanságot jelent. Nem dönthető el, hogy ez érzelmi megterhelődésre szóló eszkalációs utasítás-e. Ha az, a címzett nincs megnevezve.
- **Bizonyíték:** „Tudod, kit hívsz oda / kinek jelzel, ha valaki nagyon elbizonytalanodik.” (565). Ugyanez a pont az M6.A-ban név szerint megadja a címzettet: „a kijelölt **Memunának** (a Somer gyermekvédelmi felelősének)” (A:180)
- **Hatás:** Ha érzelmi megterhelődésről van szó, a képző ellenőrző listájáról hiányzik a címzett. Ha nem, akkor a „jelzel” egy hétköznapi bizonytalanságot gyermekvédelmi ügynek mutat.
- **Javaslat:** EMBERI DÖNTÉS: a tartalomfelelős döntse el, melyik helyzetre szól a tétel.
  - Ha érzelmi megterhelődésre: az A:180 kánoni mondata szó szerint átvezethető (HUM-SAFE-01).
  - Ha alkotói bizonytalanságra: a „kinek jelzel” kerüljön ki.
  - Policy-szöveget ne írj.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-603**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:87, 473, 491` (a modulhub 155. sora ugyanígy fogalmaz; az a G6-on kívül esik, csak konzisztencia miatt említem)
- **Probléma:** A *dugma isit* a glosszárium szerint a madrih élőben látható személyes példamutatása. Itt egy játékra vagy eszközre vonatkozik („a saját játékom … dugma isit legyen”). Ez a glosszáriumban kerülendőnek jelölt „Dugma Isitnek lenni” szerkezet, tárgyra alkalmazva.
- **Bizonyíték:** „Miben legyen a saját eszközöm dugma isit a biztonság és az inkluzivitás szempontjából?” (473). Glosszárium:27: „A megszemélyesített „Dugma Isitnek lenni” formát **kerüld**”
- **Hatás:** A záró vállalás-kört minden résztvevő hangosan mondja, így egy alapvető someres fogalom téves jelentése rögzül. A modulhub (kánoni 2.) itt ellentmond a glosszáriumnak (kánoni 3.).
- **Javaslat:** EMBERI DÖNTÉS: a projektgazda vagy a Somer-terminológia gazdája döntse el, miről szól a vállalás.
  - Ha a madrih személyes példamutatásáról: glosszárium-konform szerkezet kell („dugma isitként…”, „személyes példát mutatni”).
  - Ha a játéklap példaértékűségéről: a kifejezés nem ide illik.
  - A hub 155. sorát ugyanebben a lépésben kell javítani.
  - Már most javítható: a 87. sor végén pont helyett kérdőjel kell, ahogy a 491. sorban.
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-604**
- **Súlyosság:** P1
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:475, 559`
- **Probléma:** A határozott névelős „a kirekesztés-élmény” azt sugallja, hogy a játék kirekesztést okoz. A 4.3.1 viszont az inkluzív, nem versengő változatot játszatja, a 481. sor pedig felidézett kimaradás-élményről beszél. Az 559. sor „kirekesztett élményű gyerek” szerkezete tükörfordítás.
- **Bizonyíték:** „De ha menet közben láthatóan rosszul érinti a kirekesztés-élmény” (475); „a téma maga is felidézhet korábbi kimaradás-élményt” (481)
- **Hatás:** A képző az azonnali beavatkozás okát szűkebben értheti. A mondat az M6 védelmi elvével is ellentétes irányba mutat (nincs kirekesztés-szimuláció).
- **Javaslat:**
  - 475: „a kirekesztés-élmény” → „egy állítás vagy egy felidézett kimaradás-élmény” (ez a 481. sorban megnevezett két forrás).
  - 559: „kirekesztett élményű gyerek” → „gyerek, akit már kirekesztettek”.
  - A jelek felsorolásához és az „azonnal lépj” utasításhoz nem szabad nyúlni.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-605**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:62–63, 161–180, 707–708`
  - `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:67–77, 105–117, 225, 356, 502–510, 567`
- **Probléma:** A megszólítás keveredik (6. regressziós minta).
  - A meta (A:62–63) a résztvevőt tegezi, a 2.1–2.2 és a 4–5. szakasz a képzőt.
  - A 2.3 mindkét fájlban harmadik személyben beszél a képzőről.
  - A résztvevőkről szóló mondatok többes szám 2. személyben állnak (A:708, B:356, B:567).
  - A felolvasandó instrukciók egy megszólaláson belül váltanak „ti” és „te” között (B:105→107, 225, 502–507).
- **Bizonyíték:** „amit az **M6.B műhelyen** kezdtek el és **Moodle-ben** adtok le.” (A:708); „Gondoljátok át röviden, hogy melyik már ismert eszköztípusból szeretnétek választani” → „Mondj **két dolgot**:” (B:105, 107)
- **Hatás:** Az A:708 „kezdtek el” múlt idejű 3. személyként is olvasható, pedig az M6.B ekkor még nem volt meg. A képzői listán úgy tűnik, mintha a képző adná le a játéklapot. Felolvasáskor a „ti”–„te” váltás döccen.
- **Javaslat:** A képzői szövegben a képző legyen „te”, a résztvevők harmadik személy.
  - A:708 → „amit a résztvevők az M6.B műhelyen kezdenek el, és a Moodle-ben adnak le”.
  - B:356: „játszottatok” → „játszottak”.
  - B:567: „ha csúsztok” → „ha csúszol”.
  - A:62–63: a résztvevő harmadik személyben szerepeljen.
  - A 2.3 szakaszok mindkét fájlban tegezve szóljanak a képzőhöz.
  - A felolvasandó szövegben egy megszólalás végig egy formát használjon.
  - Tartalom, sorrend és idő nem változik.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-606**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:215–216` (összevetve: 49–50, és a 242. sor `M6.B-MUNK-01` spec)
- **Probléma:** A 4.2 1. lépésében a mezőlista két mezőben eltér a 2.1-es listától és a sablon-asset specifikációjától. Az asset megjegyzése (259) szerint pedig ugyanannak a listának kellene lennie (7. regressziós minta).
- **Bizonyíték:** „Inkluzivitás (kire kell külön figyelni; legalább 1 akadály…)” (49) vs. „Inkluzivitás (kire figyelek, hogyan vonok be; legalább 1 akadály…)” (215); „Variációk (könnyített / nehezített / alternatív használat)” (50) vs. „(könnyebb / nehezebb / más célra)” (216)
- **Hatás:** A táblára felírt minimum mást kér, mint a kiosztott sablon.
- **Javaslat:** A 215–216. sor vegye át szó szerint a 49–50. sor szövegét, mert a legyártott sablon ezt tartalmazza. A segédkérdések személyének egységesítése (44/208 „használom”, 48/214 „állsz le”) csak a két listában és a spec-ben együtt történhet.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-607**
- **Súlyosság:** P1 (rubrika D10: terminológiai inkonzisztencia)
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:53, 157, 317`
  - `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:51, 76, 84, 200, 556`
- **Probléma:** Egy fogalom több néven szerepel, illetve egy név két fogalomra:
  - A „közös nyelv” harmadik eleme hol „rizikó” (A:54, 110, 392, 661, 708), hol „kockázat” (A:53, 317).
  - A kijelölt biztonságos hely egyszer „csendesebb sarok” (A:157), máshol „csendes sarok” (490, 696).
  - Ugyanaz a lista „minimum-checklista” / „checklist” (B:51, 84, 200, 556), illetve „ellenőrzőlista” (B:53, 219, kapu: 399).
  - A „biztonsági mondat” egyszer a bizonytalan résztvevő bátorítása (B:76), máskor az R4 blokkoló rubrikasor tárgya (B:223).
- **Bizonyíték:** „**cél – kvuca – kockázat – inkluzivitás / variációk**” (A:53) vs. „„Mi benne a rizikó?”” (A:54); „Előkészít 1–2 **biztonsági mondatot**, ha valaki bizonytalannak érzi magát” (B:76)
- **Hatás:** A 4. cél kifejezetten közös nyelvet ígér, a szöveg viszont váltogatja a szavakat. Az R4 kritériuma összemosódik egy bátorító mondattal.
- **Javaslat:**
  - A:53 és 317: „kockázat” → „rizikó” (így szerepel a POSZ-02 mátrixon és a hubban).
  - A 4. kérdés változatait (A:54/318/662) törléssel tilos egységesíteni: a 318. sor „biztonságosabb” eleme nem eshet ki.
  - A:157: „csendesebb sarok” → „csendes sarok”.
  - B:51, 84, 200, 556: „checklist(a)” → „ellenőrzőlista”. Az `@asset` címe csak a média-manifest folyamattal együtt változhat.
  - B:76: „biztonsági mondatot” → „bátorító mondatot”. A 223. sor és az 562. sor marad.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-608**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:54, 374, 399, 424, 447, 473, 483, 493, 518, 545, 603, 611`
  - `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:573`
- **Probléma:** Tükörfordítás és vonzathiba, főleg a felolvasandó instrukciókban. Az angol „for” „-ra” lett, a „more inclusive” „inkább inkluzívvá”, a „turn into groups” „forduljatok csoportokba”, a „real” „valós”, a „spotlight” „reflektorozd rá”.
- **Bizonyíték:** „Mit kéne változtatni, hogy menjen mondjuk Parparimra (6–9) is?” (A:399); „Forduljatok 2–3 fős kis csoportokba.” (A:603)
- **Hatás:** A képző szó szerint felolvassa ezeket. A hibás vonzat éppen a „közös nyelvben” rögzül (A:54).
- **Javaslat** (a tartalom nem változik):
  - A:54: „korosztályra jó” → „korosztálynak jó” (ahogy a 315. sorban).
  - A:374: „korosztályra … passzol” → „korosztályhoz … illik”.
  - A:399: „Melyik korosztálynál működne a legjobban így? Mit kellene változtatni, hogy mondjuk a Parparimnál (6–9) is működjön? Vagy egy idősebb Leviatán-kvucánál (16–17)?”
  - A:424: „inkább inkluzívvá” → „inkluzívabbá”.
  - A:447: „a kör előtt” → „mindenki előtt”.
  - A:473: „megfoghatod utána” → „utána visszatérhetsz rá”.
  - A:483: „ne tedd középponttá az érintettet” → „ne állítsd az érintettet a figyelem középpontjába”.
  - A:493: „Ne reflektorozd rá az érintettet” → „Ne állítsd reflektorfénybe az érintettet”.
  - A:518: „érzetben” → „érzelmileg”.
  - A:545: „Miért gondolod, hogy inkább ennek a korosztálynak való?”
  - A:603: „Alkossatok 2–3 fős kis csoportokat.”
  - A:611: „amikor játékot választasz egy valódi kvucának?”
  - B:573: „Ne felejtsd el zárásként elmondani:”
  - A címekben álló „3 aktuális kvucára” fix megnevezés, nem változik.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-609**
- **Súlyosság:** P2
- **Bizalom:** közepes (a „kézműves” alpontnál alacsony)
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:21, 67, 71, 359`
- **Probléma:**
  - A „drótváz” (wireframe) fejlesztői szó, a képzői felkészülésben nincs helye.
  - A ragozott „kézműves” főnév mesterembert jelent, nem tevékenységet: „kézművest visz”.
  - A 359. sor „rendben van-e a finommotorika” a gyerek képességére kérdez rá, nem a feladat igényére.
- **Bizonyíték:** „Átolvassa az **M6 modul drótvázát**” (67); „aki **történetet vagy kézművest** visz a játéklapjába” (71)
- **Hatás:** A képző nehezebben érti a felkészülési utasítást. A 359. sorból rossz irányú ellenőrző kérdés lesz.
- **Javaslat:**
  - 67: „drótvázát” → „vázlatát”.
  - 21: „kézműveshez” → „kézműves foglalkozáshoz”; 71: „kézművest” → „kézműves foglalkozást”. A címek és a „játék / történet / kézműves” kategóriacímkék maradnak. A modul többi fájljában is ez a minta él; az egységesítés modulszintű döntés.
  - 359 → „a feladat finommotorikai igénye, az anyag-érzékenység, a költség és a szimbólumok szempontjából rendben van-e”.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-610**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:451, 569`
  - `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:63, 226, 373, 575–577`
- **Probléma:** Öt helyen nem dönthető el a jelentés, ezért szövegjavaslatot nem adok:
  - (a) A:451 „ez is jelzés lehet”: válasz (mint a 438. sor „az is válasz”), vagy figyelmeztető jel? A korpuszban a „jelzés” gyermekvédelmi szakszó.
  - (b) A:569 „identitás-sérüléshez”: nem világos, mit jelent.
  - (c) B:63 és 373 „félplénum”: a percbontás (86) „plénumban”-t ír. Fél csoport vagy az egész?
  - (d) B:226 „(ha van, 2–3 perc)”: hiányzik a főnév. Ha van minta, vagy ha van idő? A 2.3 és az 5.3 kötelezően kéri a mintát.
  - (e) B:575–577 „az élő műhelyen pedig egymásnak is tudnak visszajelzést adni”: melyik műhelyen, és mikor?
- **Bizonyíték:** „ez is jelzés lehet, és rendben van.” (A:451); „2–3 játéklap **félplénumban is megjelenik**” (B:373)
- **Hatás:** A képző nem tudja, mit mondjon vagy hogyan szervezze a feladatot. Az (a) esetben a gyermekvédelmi szókincs félreérthető.
- **Javaslat:** EMBERI DÖNTÉS: a peula tartalomfelelőse tételenként rögzítse, mit akart mondani. Addig ne írj helyettük szöveget (8. regressziós minta).
- **Típus:** emberi-döntés
- **Verdikt:** —

**NYELV-611**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:418`
- **Probléma:** A mondat egy korábbi szerkesztés nyomának tűnik. A „B” nincs feloldva, a „továbbra is” előzmény nélkül áll. Az sem világos, hogy a táblára kell-e írni: a 414–416. sori táblaszöveg után külön idézetblokkban áll.
- **Bizonyíték:** „Az SBI viselkedésre való: amikor ember viselkedésére adsz SBI-t, a **B továbbra is megfigyelhető viselkedés**.”
- **Hatás:** A képző nehezen tudja felolvasni vagy elmagyarázni. Elmosódik az SBI és a produktum-visszajelzés közötti különbség.
- **Javaslat:** „…ha egy ember viselkedésére adsz SBI-visszajelzést, a B (Behavior, viselkedés) megfigyelhető viselkedés legyen.” A modellnév és a „konkrétumról beszélünk, nem címkézünk” rész marad. Ha a `/course-fix` szerint ez egy félbemaradt javítás maradéka, az AFFiNE-forrással kell egyeztetni (a baseline ismeretlen).
- **Típus:** objektív
- **Verdikt:** —

**NYELV-612**
- **Súlyosság:** P2
- **Bizalom:** magas
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:420, 422` (és a 387. sor `M6.B-POSZ-01` spec)
- **Probléma:**
  - (a) Hiányzik a főnév: a példa nem játéklap, hanem egy játéklapra adott visszajelzés.
  - (b) A poszter-spec „kész mintamondata” rövidebb a törzsszöveg példájánál: a „következő madrih” hatása kimarad (7. regressziós minta).
- **Bizonyíték:** „**Kész példa egy játéklapra:**” (420); csak a törzsben: „és egy másik madrih is könnyebben tudná biztonságosan megtartani a játékot.” (422)
- **Hatás:** A képző mintajátéklapot kereshet. A kitett poszteren más mondat áll, mint amit a képző felolvas.
- **Javaslat:**
  - 420 → „Kész példa egy játéklapra adott visszajelzésre:”
  - A POSZ-01 spec mintamondata igazodjon a 422. sorhoz, a média-manifest folyamatán keresztül. A generált kimenetet kézzel ne szerkeszd.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-613**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:** `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:239, 309–321, 481, 498–500`
- **Probléma:**
  - A 4.2.1 címe biztonsági keretet ígér, de a lépés csak a labor magyarázatát tartalmazza. Ez lehet cím és tartalom eltérése, vagy kiesett szöveg (7. vagy 9. minta; a baseline ismeretlen).
  - A 4.3.2/B két „előre” szóló utasítása csak a játék (4.3.2) után következik.
- **Bizonyíték:** „#### 4.2.1. Lépés 1 – Biztonsági keret + Játék-labor magyarázata (kb. 2–3 perc)” (239); „**Keretezd a játékot ELŐRE (a 4.3.1 biztonsági keret után mondd ki ezt is):**” (498)
- **Hatás:** A sorban haladó képző a 4.2.1-ben nem találja a keretet, a 4.3-as előkeretezést pedig csak a játék indítása után olvassa. Ez végrehajthatósági hiba.
- **Javaslat:**
  - 239: a `/course-fix` nézze meg az AFFiNE-forrást. Ha a szöveg kiesett, onnan kell visszaállítani, nem újraírni. Ha soha nem volt meg, a címből törlendő a „Biztonsági keret +”.
  - 498–500: a 4.3.1 végére kerüljön egy utaló sor a 4.3.2/B előkeretező mondatára és a négy lépésre. A 4.3.2/B szövege nem változik.
- **Típus:** objektív
- **Verdikt:** —

**NYELV-614**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:401, 481, 683`
  - `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:200, 338, 346`
- **Probléma:** Egyeztetési és alanyhibák:
  - A:401: a felsorolás és két tagmondat összefolyik.
  - A:481: a „rosszul érint” alany nélkül a madrihra vonatkozik.
  - B:200: „sorait, amire” – számbeli egyeztetési hiba.
  - B:338: a „legyen” alanya a résztvevő, nem a vázlat.
  - B:346: fölösleges vessző.
  - A:683: két mellérendelt azonosító után a főnév többes számban áll.
- **Bizonyíték:** „(pl. kiesés-élmény, aki sokat ront, kinevetik, aki nem ismeri a neveket, szégyenkezik)” (A:401); „Egy kezdő madrih gyakran lefagy, ha valakit menet közben rosszul érint.” (A:481)
- **Hatás:** Félreolvasható mondatok a képzői instrukcióban.
- **Javaslat:**
  - A:401 → „(pl. kiesés-élmény; aki sokat ront, azt kinevetik; aki nem ismeri a neveket, szégyenkezik)”
  - A:481 → „ha a játék valakit menet közben rosszul érint”
  - B:200: „amire” → „amelyekre”
  - B:338 → „A vázlat már a peula végén legyen olyan állapotban, hogy…”
  - B:346 → „egyedül vagy párban”
  - A:683 → „az M6.1 és az M6.4 leckéhez”
- **Típus:** objektív
- **Verdikt:** —

**NYELV-615**
- **Súlyosság:** P2
- **Bizalom:** közepes
- **Lencse:** nyelv
- **Hely:**
  - `02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md:107–113`
  - `02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md:171, 488`
- **Probléma:** Felolvashatósági gondok:
  - B:109–111: a számozott lista kilóg a felolvasandó idézetblokkból.
  - A:488: szögletes zárójeles helyőrző áll a szó szerint felolvasandó mondatban.
  - A:171: a 3. játék leírása egyetlen, zárójelbe ágyazott, kettős kettőspontos mondat.
- **Bizonyíték:** „Itt a [csendes sarok], bármikor visszajöhetsz, amikor jó.” (A:488); „(Ha marad idő, Játék 3: egyszerű „bizalom-labda”: halkabb verzió – **körben állva egy puha labdát adunk körbe” (A:171)
- **Hatás:** A képző nem látja, mi része a felolvasandó szövegnek, és a helyőrzőt is felolvashatja. A 3. játék instrukciója hangosan követhetetlen.
- **Javaslat:**
  - B:109–111 kerüljön az idézetblokkba, szövege nem változik.
  - A:488: „Itt a csendes sarok, …”, a „(mutass rá)” pedig képzői megjegyzésként a mondaton kívülre kerüljön.
  - A:171: két-három mondatra bontva, külön alpontban. A lassú tempó, a „nincs kiesés”, a „nincs gyorsítás” és a passz lehetősége változatlanul marad.
- **Típus:** objektív
- **Verdikt:** —

LEVÁGVA: 2 további finding, súlyosságuk: 2×P2 (a reviewer kimeneti korlátja miatt; nincsenek meg).
