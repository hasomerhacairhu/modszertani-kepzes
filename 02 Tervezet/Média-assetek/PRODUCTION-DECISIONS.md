# ⚖️ Média-produkció — nyitott döntések

**Ez a dokumentum kézzel karbantartott.** Nem generált, és nem asset-regiszter: csak
azokat a kérdéseket tartalmazza, amelyekre **ember** válaszol, és amelyek nélkül a
gyártás egy része nem indulhat el. Ha egy döntés megszületik, itt kell kivezetni a
nyitott-érték jelölést, és elvégezni a „Mit kell utána átírni” pontban felsoroltakat.
A lezárt döntések a lap alján, egy táblázatban maradnak — nyomon követhetőségért, nem
kérdésként.

A darabszámok forrása a jelenlegi v2 manifeszt (`MEDIA-PRODUCTION-PLAN.md` 2. és 3.
szakasz). **Egy asset több kapun is ülhet**, ezért az „önmagában felszabadul” szám mindig
kisebb vagy egyenlő, mint az „érintett”.

| | Asset | Deliverable |
|---|---:|---:|
| Összesen | 415 | 903 |
| Ebből központilag előgyártható | 404 | 898 |
| Ebből **most gyártható** | **285** | **526** |
| Élő/runtime tétel (a képző hozza létre a peulán) | 3 | 5 |

---

## D1 — Vizuális rendszer: stílus-token és someres paletta (R5) — LEZÁRVA

> ✅ **Projektgazdai döntés (2026-10-02, `HUM-MEDIA-01`): a D1 lezárva.** D1-a igen: a
> hivatalos Somer-paletta. D1-b igen: a 2022-es arculati kézikönyv és a hivatalos SVG
> színgenerációja a kánon. D1-c: a **B változat** (Source Sans 3 + produkciós semleges
> skála). D1-d igen: a szín szemantikája modulhatókörű, az elsődleges jel a forma és a
> felirat. D1-e: a `#2B2523` csak a logón belül. Az alábbi két lépcső értékei ennek
> alapján kitöltve, és a `produkcios-szabalyok.json` R5 szabályából kikerült a nyitott
> érték. Az asset-szintű R5-blokkolók kivezetése a leckék deklarációiból külön
> manifeszt-művelet; az aktuális állapotot és a darabszámokat a generált terv
> ([`MEDIA-PRODUCTION-PLAN.md`](./MEDIA-PRODUCTION-PLAN.md)) mutatja. Utólagos ellenőrzés
> (vétó/QA): a kreatív/márkafelelős.

**A folyamat eldőlt** (2026-08-27): két lépésben zárjuk — előbb a **stílus-token**, utána
a **hex-paletta**. A 2026-10-02-i döntés mindkét lépcsőt egyszerre zárta le.

**Miért ez volt a legfontosabb:** ez a legnagyobb tétel. Amíg nyitva volt, 258 asset nem
volt gyártható, és ha rosszul indult volna, 258 asseten kellett volna újragyártani.

**A döntés előtti bizonyíték:** a tananyagban (leckék, kánoni szabályok) **nem volt
hex-érték**, és nem volt jóváhagyott design-system fájl, arculati leírás vagy
logó-specifikáció. Ami volt, az szemantikus színhasználat a
leckékben (SBI: kék/zöld/narancs; 3 pillér: kék/piros/zöld; red flag: piros/zöld; M6.4:
kék/sárga/zöld) és 26 olyan tétel, amelynek a saját technikai jegyzete szerint elég a
fekete-fehér nyomtatás. Részletek és a teljes lock-lap:
[`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md). A repository első hex-forrása a
lent hivatkozott [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) javaslata volt;
annak B változatát fogadta el a döntés.

> 🔎 **2026-08-27: a kérdés lényegesen szűkült.** Egy célzott külső kutatás megtalálta a
> mozgalom **saját, nyilvánosan elérhető arculati kézikönyvét** és logócsomagját
> (`somer.hu/arculat/`) — deklarált HEX / RGB / CMYK / Pantone palettával, amelynek mind
> a hat alapszíne **byte-azonosan megerősíthető a hivatalos logó-SVG-ből**. A D1 kérdése
> ezért már nem „mi legyen a paletta”, hanem: **átvesszük-e a meglévőt**, melyik
> színgeneráció a hatályos, és mit teszünk oda, ahol a kézikönyv hallgat (betűméret-skála,
> ikon-stílus, semleges skála). A teljes bizonyíték-lánc, a **kiszámított** WCAG-kontrasztok
> és a két jóváhagyható változat: [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md).
> **Ez bizonyíték volt, nem jóváhagyás; a jóváhagyást a 2026-10-02-i projektgazdai döntés
> adta meg (lásd fent).**

**Mit szabadít fel:** R5 lezárása önmagában **245 központilag előgyártható asset / 484 deliverable**. A teljes R5-hatókör **258 szemantikus asset**: ebből 1 `reuse` hely nem gyárt saját deliverable-t, 1 élő/runtime tétel, 3 további emberi döntésre is vár, 8 pedig R2/R3 blokkolót is visz (közülük az `M1.3-VID-01` emberi döntésre is, D11). Így a ténylegesen csak R5-re váró központi gyártási köteg 245 asset.

**Ki döntött:** a projektgazda (2026-10-02). Utólagos ellenőrzés (vétó/QA): a
kreatív/márkafelelős.

### 1. lépcső — stílus-token

- betűtípus (címsor / törzs): **Source Sans 3** mindkettőre (címsor félkövér, törzs
  normál; SIL OFL 1.1); a betűméret-skála a
  [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 3.4. pontja szerint. A Myriad
  Pro ott marad, ahol a szervezet maga készít anyagot.
- fejléc-, margó- és rácsrend a nyomtatványokhoz: a
  [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 4. szakaszának produkciós
  ajánlása szerint (A4 álló, 190 mm-es szedéstükör, 12 oszlopos rács, címhely kickerrel és
  vastag vonallal)
- ikon-stílus: **körvonalas (outline)**, 24×24-es tervezőrács, **2/24** vonalvastagság,
  kerek vonalvég és -illesztés; a sarok-lekerekítés sugara a vonalvastagsággal egyezik
  ([`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 5. szakasz)
- az AI-provenance címke **vizuális formája és elhelyezése** (a szövege eldőlt — lásd a
  lezárt D9-et a lap alján): mindig **élő LMS-szöveg**, nem képbe égetve; a megjelenése és
  az elhelyezése a [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 7.3. pontja
  szerint
- logóhasználat és biztonsági margó: a **2022-es arculati kézikönyv** szerint — csak a
  hivatalos csomagból, nem újrarajzolva, nem átszínezve, nem nyújtva, nem forgatva,
  színátmenet és effekt nélkül; a `#2B2523` csak a logón belül. Külön biztonsági margót és
  minimális méretet a kézikönyv nem ad meg.

### 2. lépcső — paletta és karakter

- someres alap-hex-paletta: `#D84C15` piros, `#F2BC00` sárga, `#87B027` zöld, `#369D37`
  sötétzöld, `#08A0CA` sötétkék, `#82CDE9` kék (a kézikönyv árnyalatai:
  [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) 1.2.)
- háttér- és szövegszín: szöveg `#1D1D1B`, halvány szöveg `#5C5C5B`, szerkezeti vonal
  `#8E8E8D`, dekoratív vonal `#CDCDCD`, felület `#F1F1F1` (a B változat semleges skálája);
  sötét módot a döntés nem ír elő
- az R6 szín-ütközés feloldása: a szín szemantikája **modulhatókörű**; az elsődleges jel a
  forma és a felirat (betűjel). A szín soha nem önálló jelentéshordozó, ezért ugyanaz a
  szín más modulban újrahasznosítható.
- karakter-stílus és rögzített referencia-seed: **lapos vektoros illusztráció**, nem
  fotorealisztikus 3D; generált képben nincs szöveg. A referencia-karakter és a seed
  rögzítése a karakter-gyártás első lépése
  ([`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md), P-KAR, 1. lépés).

### Mit jelent a kétlépcsős zárás a manifesztben — pontosan

> **2026-10-02:** a két lépcső egyszerre zárult, ezért a 26 fekete-fehér nyomtatvány külön
> kivezetésére már nincs szükség: az R5-blokkoló kivezetése egyetlen, tudatos
> metaadat-művelet az összes érintett asseten. Az alábbi bekezdés a döntés előtti helyzetet
> rögzíti.

**A jelenlegi manifeszt egyetlen R5-blokkolót ismer, nem kettőt.** Az első lépcső
lezárásakor tehát **nem** oldódik fel automatikusan a 26 fekete-fehér nyomtatvány: a terv
`media-production-plan.csv` `Szín-függés` oszlopa megmutatja, melyik az a 26 tétel
(`1A — fekete-fehér is elég`), de a státuszuk addig `produkciós szabályra vár`, amíg az R5
blokkoló rajtuk marad. A gyártás **elindítható** rájuk a stílus-token birtokában — a
manifeszt viszont csak akkor követi ezt, ha a második lépcsőben az R5 egészében lezárul,
vagy ha az érintett 26 asset `blockers` mezőjéből külön, tudatos metaadat-művelettel
kivezetjük az R5-öt. Ez utóbbi önálló feladat; ez a pass nem végezte el, és séma-módosítást
nem igényel.

**Mit kellett utána átírni:** `produkcios-szabalyok.json` R5 (a paletta kitöltve, a
nyitott-érték jelölés kivezetve) és R6 (a modulhatókörű feloldás),
[`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md) értékei és a
[`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) státusza — ezek 2026-10-02-án
átírva. Ezután: az asset-szintű R5-blokkolók kivezetése, majd
`python3 tools/media_manifest.py build`.

---

## D2 — Melyik ElevenLabs egyedi hang legyen a kanonikus narrátor? (R3) — LEZÁRVA

> ✅ **A szolgáltatói kérdés lezárult (felhasználói döntés, 2026-08-28).** A felmondás
> **szintetikus**, a motor az **ElevenLabs**. A „szintetikus vagy emberi” és a „melyik
> szolgáltató” kérdés **többé nem nyitott**, és nem is kerül újra elő.

> **Projektgazdai döntés (2026-10-03, VO 2. fázis; VO D-01, D-02, D-03, D-09, D-12, D-14):**
> mindkét ElevenLabs-hang — a kanonikus narrátorhang és a második hang — létezik; a hanghasználati jog tisztázott, a
> hang tulajdonosai kifejezetten hozzájárultak. Az elsődleges narrátor a **kanonikus narrátorhang**; a
> második hang jogtisztázott, a kalibrálása nem feltétele az első gyártási körnek. A
> gyártási konfiguráció: `eleven_v4`, `stability` 0,35, `similarity_boost` 0,75 (`speed` és
> `style` nincs), `apply_text_normalization: auto`, `pcm_48000`, a kanonikus kiejtési szótár
> (`ulYxuUbd8aSRJ89Pv2Q8` / `VFpQiiOF789b08uzsooM`); részletek: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md)
> 12. szakasz. A meghallgatásos hangválasztás nem fut. A formális jogosultsági bizonyíték
> ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) R2-5) függő. A döntés szó szerinti szövege:
> `01 Fejlesztés/04 Audit/2026-10-03 Projektgazdai döntések – VO 2. fázis.md`.
> *Kiegészítő döntés (2026-10-03, K4): a második hang az első gyártási körben az `M1.3-VID-01` Madrih B szerepét mondja, a kalibrálása után (lásd D11).*

**A kérdés 2026-08-28-án** az volt, hogy a két forrás-beszélő — **VOICE-SRC-01** és
**VOICE-SRC-02** — felvételeiből létrehozandó ElevenLabs egyedi hangok közül melyik legyen a
tananyag **kanonikus narrátora**. A 2026-10-03-i projektgazdai döntés (fent) lezárta: a
kanonikus narrátorhang ki van jelölve.

**A) VOICE-SRC-01**
**B) VOICE-SRC-02**

**Ajánlás: nincs — MEGHALLGATÁS SZÜKSÉGES.** Két hang közül dokumentáció alapján nem lehet
választani: a magyar természetesség, a melegség és a someres szavak kiejtése csak
hallgatással dönthető el. A hatpárosos összehasonlítás kész, végrehajtható terve —
beállításokkal, kiejtési figyelőlistával és pontozólappal —
[`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md). **Mérete 3 208 karakter,
becsült költsége 0,16–0,64 $** — a szolgáltató két árazási felülete eltérő szorzót ad,
de mindkét olvasatban egy dollár alatt marad.

**Egy hang lesz a narrátor.** Az R3 első mondata egyetlen konzisztens narrátor-hangot ír
elő. A másik hang esetleges szerepe (tartalék, dialógus- vagy karakterhang) **külön,
későbbi döntés** — ez a lap nem osztja ki neki. *(2026-10-03: eldőlt — az első gyártási körben az `M1.3-VID-01` Madrih B szerepét mondja, a kalibrálása után; VO D-14, K4, lásd D11.)*

### Ami a szolgáltatói döntés után is nyitva maradt

| Mező | Állapot |
|---|---|
| Felmondó típusa | ✅ **szintetikus** |
| Motor / szolgáltató | ✅ **ElevenLabs** |
| **Kanonikus hang** | ✅ **kijelölve** — a kanonikus narrátorhang (projektgazdai döntés, 2026-10-03, VO D-14); mellette a jogtisztázott második hang |
| Hang-objektumok létrehozása | ✅ **megtörtént** — mindkét hang létezik (VO D-01). A létrehozás módjára vonatkozó szolgáltatói szabály (PVC-t a forrásbeszélő maga hoz létre és hitelesít; a tanítási kimaradásnak a feltöltés előtt élnie kell) változatlanul érvényes; hogy ez a két hangnál hogyan teljesült, azt csak valós bizonyíték rögzítheti ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.0, R2-5). |
| Voice-ID | nem nyilvános: csak a VO QA-repó gyártási konfigurációjában él, a kurzusrepóba (a VOICE-BIBLE-be sem) nem kerül (kiegészítő döntés, 2026-10-03, K3) |
| Hangtípus | fiókbizonyítékból rögzítendő (nem találjuk ki) |
| Modell | ✅ `eleven_v4`, `language_code: "hu"` (VO D-02) |
| Hangbeállítások és seed | ✅ `stability` 0,35, `similarity_boost` 0,75; rögzített seed (VO D-02) |
| Kiejtési szótár | ✅ a kanonikus gyártási kiejtési szótár, `ulYxuUbd8aSRJ89Pv2Q8` / `VFpQiiOF789b08uzsooM` (VO D-03) |
| Hang-jogosultság igazolása | tartalmilag tisztázott (VO D-01); formális bizonyíték: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) R2-5 (függő) |

> ✅ **A hangok léteznek (projektgazdai tényközlés, 2026-10-03, VO D-01).** A létrehozás
> módjára vonatkozó szolgáltatói szabály (PVC: a forrásbeszélő a saját fiókjában hozza létre és
> hitelesíti, majd privát megosztással ad hozzáférést; IVC: külön igazolt használati
> jogosultság) változatlan, de hogy a két hangnál ez hogyan teljesült, azt a repó csak valós
> bizonyítékból rögzítheti. A repóban nincs ElevenLabs hitelesítő adat, és voice-ID-t, hangtípust
> nem találunk ki. Az azonosítás menete: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.4.

**Mi kell még az R3 lezárásához (2026-10-03):** a kanonikus hang, a modell, a beállítások és a
szótár rögzítve, a voice-ID helye kijelölve (K3); nyitott a P-NAR pilot (`M4.2-NAR-03`) fülre
jóváhagyása produkciós környezetben (VO D-13) és a második hang kalibrálása az `M1.3-VID-01`-hez (K4). Az R3 blokkoló ezért a tételeken a helyén marad;
a levétele a manifesztben külön, tömeges módosítás (116 deklaráció).

**Miért fontos (2026-08-28, történeti):** a kutatás egy nem várt eredményt hozott. A szolgáltató **leghosszabb
formára legstabilabbnak jelölt modellje (`eleven_multilingual_v2`) nem támogatja a
magyart** — a dokumentált 29 nyelve közt a `hu` nincs ott. A magyar tehát leszorít a
stabilitási zászlóshajóról, és a választás az `eleven_flash_v2_5` és az `eleven_v3` között
marad. A javaslat a `flash_v2_5`, mert az `eleven_v3`-on **nincs tempó-vezérlés**
(„Speed is not available for the Eleven v3 model”), a tananyag pedig kötött 100–120
szó/perc célsávot ír elő. Részletek: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.1–13.2. A 2026-10-03-i döntés
az `eleven_v4`-et rögzítette, amelyen a fülre hozott kiejtési döntések születtek; tempó-vezérlés
ott sincs, a tempót a szöveg és az időkeret adja ([`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 4., 12.).

**Mit szabadít fel:** R3 lezárása önmagában **0 asset**: mind a 116 R3-tételen az R2 is
ül, mert a felmondás szintetikus, így az R2 a narrációkra is kiterjed
([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1. szakasz). Az R3 + R2 együtt — az R5-öt és
a nyitott emberi döntéseket még nyitva hagyva — **117 asset / 366 deliverable**.

**Ki döntött:** a kanonikus hangról és a gyártási konfigurációról a projektgazda (2026-10-03); a
hang-jogosultság formális bizonyítékáról a jogi jóváhagyó és a hang jogosultja.

**A válasz helye:**
- felmondó típusa: **szintetikus** ✅
- motor: **ElevenLabs** ✅
- kanonikus hang: **kijelölve** ✅ (2026-10-03)
- modell, beállítások, seed, kiejtési szótár verziója: ✅ [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 12. szakasz; voice-ID: nem nyilvános, a VO QA-repó gyártási konfigurációjában ✅ (K3)

**Mit kell utána átírni:** `produkcios-szabalyok.json` R3,
[`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 12. szakasz,
[`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md) eredmény-mezői,
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) hang-sorai, majd build.

---

## D3 — Az R2 jogi bizonyítékai

**A hatály eldőlt** (2026-08-27, A opció): az R2 a beszélőfej-videókra, az AI emberi
karakterjelenetekre és a belőlük kivett állóképekre egyaránt vonatkozik — összesen **28
asset** —, hacsak egy későbbi jogi review kifejezetten nem szűkíti. A hétköznapi
AI-illusztrációk, ikonok és diagramok **nem** tartoznak ide: azokra az R1 (AI-jelölés)
vonatkozik. *(Azóta: 29 vizuális asset — az AI-karakter-B-roll `M1.1-VID-02` is R2 alá
került —, és mivel a felmondás 2026-08-28 óta szintetikus, az R2 „AI-hang” ága mind a 89
hang-assetre is kiterjed: összesen 118 asset.)*

**Ami nyitva maradt: maga a bizonyíték.** Az R2 szövege szerint minden ilyen assethez
dokumentálni kell a generátort, a kereskedelmi/oktatási felhasználást engedő licencet és a
hang-jogosultságot. Ebből ma **egy sincs meg**; a teljes lista soronként:
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1. szakasz.

**Mit szabadít fel:** önmagában **2 asset / 4 deliverable** — a két néma állókép
(`M4.1-FOTO-01/02`), amelyen más kapu nem ül. A 118 R2-tételből 116 R3-ra is vár. R2 + R3 együtt **117 asset /
366 deliverable**.

**Ki dönt:** jogi jóváhagyó.

> 🔎 **2026-08-27: a jelöltek és a feltételeik kutatva.** Megnevezett jelöltek, idézett
> kereskedelmi, kimenet-tulajdonlási, képmás- és provenance-záradékokkal, jelöltenkénti
> bizonyíték-állapottal: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A. szakasz. A
> javasolt gyártási útvonal és a tartalékok:
> [`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) 4–5. szakasz.
>
> **A nyilvános szolgáltatási feltétel nem azonos a produkciós fiók bizonyítékával.**
> Fiókot nem hoztunk létre, próbaidőszakot nem indítottunk, generálást nem futtattunk. Az
> R2 mind a hat bizonyíték-sora **HIÁNYZIK** marad, és a 28 asset blokkolója a helyén.
>
> ⚠️ **Két új emberi kapu, amit a kutatás hozott elő.**
>
> **J1 — jogi.** A javasolt karakter-jelenet szolgáltató feltételei tartalmaznak egy
> záradékot, amely tiltja a generatív szolgáltatás használatát olyan online szolgáltatás
> részeként, amely 18 év alattiakhoz szól vagy hozzájuk valószínűleg eljut. A tananyag
> célközönsége **15+**. Hogy az **offline legyártott, majd Moodle-ben kiszolgált** asset
> ebbe a mondatba esik-e, **jogi olvasat** — és ha igen, az kizárja a javasolt stacket.
> A kérdés a karakter-lock képgenerátorát (`gemini-3-pro-image`) is érinti, mert az is
> ugyanennek a szolgáltatónak a generatív szolgáltatása; a dokumentált tartalék (Runway)
> csak a videót cseréli, a képi lépést nem
> ([`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) 12. szakasz).
>
> **J2 — gyermekvédelmi és szerzői.** A vizsgált szolgáltatók feltételei egybehangzóan
> **felnőtt** megjelenésű avatart és karaktert engednek (kiskorú ábrázolása avatarral
> tiltott, egyedi avatarhoz nagykorúság kell, a személy-generálás EU-ban felnőttre
> korlátozott). A tananyag viszont **madrihot** ábrázol, és a kánoni szabály szerint a
> madrih maga is lehet kiskorú. Ez **nem eszközválasztási kérdés**: a Memunának
> (gyermekvédelmi felelős) és a szerzőnek kell rendeznie. Ez a lap megáll itt.
>
> A J1 és a J2 a `HUM-MEDIA-02` alkapuja (projektgazdai döntés, 2026-10-02); felelős és
> bizonyíték: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.5. Az alkapuk bizonyítéka
> ettől még hiányzik.

> **Projektgazdai döntés (2026-10-02, `HUM-MEDIA-03`):** gyermekvédelmi vagy
> krízis-HOOK-ban nem használunk készlet-AI-beszélőfejet.
> Az `M2.4-VID-01`, az `M3.3-VID-01` és az `M3.4-VID-01` hangalámondás + tipográfia/grafika;
> a szintetikus hang miatt az R2 rajtuk marad. Ha mégis beszélőfej kell, csak egyedi,
> nagykorú avatar jöhet szóba, kifejezett hozzájárulással, jogi/adatvédelmi és
> gyermekvédelmi felülvizsgálattal. A többi HOOK készlet-avatarjának képmás-licencét a
> szolgáltató feltételei szerint dokumentálni kell
> ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) H-3). Utólagos ellenőrzés (vétó/QA): a
> jogi/adatvédelmi felelős, az érintett jogosultak és a Memuna.

**A válasz helye:**
- generátor / szolgáltató neve és verziója: ⟬KITÖLTENDŐ⟭
- kereskedelmi-oktatási felhasználást engedő licenc hivatkozása: ⟬KITÖLTENDŐ⟭
- avatar-/képmás-jogosultság igazolása: ⟬KITÖLTENDŐ⟭
- hang-jogosultság (voice-talent release vagy klónozási engedély): tartalmilag tisztázott — mindkét hang tulajdonosai kifejezetten hozzájárultak (projektgazdai tényközlés, 2026-10-03, VO D-01); a formális, nem személyes hivatkozás (`VOICE-RIGHTS-REGISTER`): ⟬KITÖLTENDŐ⟭

---

## D5 — M3 gyermekvédelmi lépéstérkép poszter (`M3-HUB-POSZ-01`) — LEZÁRVA

**Állapot:** végrehajtva és lezárva: az **A** változat, amely a tananyagban és a manifestben már alkalmazva van. A hub látható gyermekvédelmi mondatának átírása szakpolitikai döntés volt; ezt a 2026-10-02-i projektgazdai döntés (`HUM-SAFE-01`) fedi.

> **Projektgazdai döntés (2026-10-02, `HUM-SAFE-01`):** a kánon az ötlépéses jelzési út;
> minden négylépéses vagy versengő változat ehhez igazodik. Ezzel a D5 lezárult.

A modul-áttekintő és az M3.B **ugyanazt az egyetlen, ötlépéses safeguarding-folyamatot** használja. A hub-poszter nem külön négylépéses anyag, hanem a már meglévő `M3.B-MUNK-01` megjelenése:

- `mode: reuse`
- `reuse_of: M3.B-MUNK-01`

**Kanonikus öt csomópont** *(szinkronpont: az `M3.B` lépéstérképének — 4.3.2. szakasz,
illetve az `M3.B-MUNK-01` `spec` mezője — másolata; a kánoni szöveg ott van, és ha az
változik, ezt is igazítani kell)*:
1. Észreveszem, és komolyan veszem.
2. Meghallgatom, és nem ígérek teljes titoktartást.
3. Nem nyomozok, nem konfrontálok, és nem próbálom egyedül megoldani.
4. Azonnal bevonom a kijelölt Memunát (összeférhetetlenség esetén a név szerint kijelölt helyettesét).
5. Közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés.

Ez megszünteti azt a korábbi hibát, hogy a négylépéses hub-összefoglaló versengő folyamatot adott, és kimaradt belőle a titoktartás határa. Nem keletkezik második safeguarding-poszter vagy párhuzamos folyamat.

**Ki döntött:** a projektgazda (2026-10-02, `HUM-SAFE-01`). A jóváhagyói rend — szintén projektgazdai döntés —: a Memuna (a Somer mindenkori, a `somer.hu/kapcsolat` oldalon publikált gyermekvédelmi felelőse) mint egyetlen felelős jóváhagyó; a programvezető operatív társdöntő. Utólagos ellenőrzés (vétó/QA): a Memuna és a helyettese, a Ros Hinuh (`Gyermekvédelem – release gate.md`, `Emberi jóváhagyás szükséges.md`).

---

## D8 — Az R8 státusza: betartandó szabály vagy önálló jóváhagyási kapu?

**Kérdés:** a két valós felvétel (`M0.3-FOTO-01` Moodle-képernyőkép, `M0.A-FOTO-01`
kvuca-plakát fotók) legyártható-e az R8 **betartásával**, vagy külön adatvédelmi és
gyermekvédelmi **jóváhagyás** kell hozzá?

**Jelenlegi bizonyíték:** az R8 szövegében — az R2/R3/R5-tel ellentétben — **nincs**
kitöltetlen érték: kész, betartható előírás (anonimizálás vagy kikeretezés, kiskorúnál
előzetes, dokumentált hozzájárulás — 18 év alatt a résztvevő és a gondviselő együtt —, képernyőképen nincs valós felhasználónév/arc).
A `README.md` viszont kimondja, hogy ennek a státusza nyitott. Az `M0.A-FOTO-01`
kézírásos plakátokról készül, és a képző hozza létre a peula után — a produkciós tervben
ezért az élő/runtime szakaszban áll, nem gyártási kötegben.

**A) Betartandó szabály.** Az R8 nem kapu: a két tétel a szabály betartásával gyártható,
a bizonyítékot a [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) rögzíti.
**B) Önálló jóváhagyási kapu.** A két tétel csak a gyermekvédelmi és adatvédelmi felelős
írásos jóváhagyása után élesíthető.

**Reviewer-ajánlás: A** — asset-szintű kötelező produkciós szabály, előírt bizonyítékkal
és átalakítással, nem külön általános jóváhagyás. **Ez nem jogi lezárás:** a jelenlegi R8
blokkolók emiatt nem kerültek ki egyik assetről sem.

> **Projektgazdai döntés (2026-10-02, `HUM-PRIV-02`):** alapértelmezésben nincs fotó,
> videó vagy hangfelvétel, csak indokolt célból; minden médiaaktivitásnál rögzíteni kell a
> célt, a jogalapot, a hozzáférést, a megőrzést és a törlést. A kézírásos plakátot
> lehetőleg fizikailag őrizzük meg. Ha fotó kell: előbb a nevek és azonosítók eltávolítása,
> a háttérben ne legyen gyerek, feltöltés ellenőrzött tárhelyre, majd törlés a saját
> eszközről. **Jogalap és megőrzés** (szintén projektgazdai döntés): fotó, videó és hang
> csak külön, önkéntes hozzájárulással, a cél teljesüléséig, legfeljebb 90 napig, hacsak
> nincs külön archiválási hozzájárulás (`Adatvédelem – tanulói adatok és AI.md` 3.
> szakasz). **A hozzájárulás adója** (projektgazdai döntés, 2026-10-02; utólagos
> ellenőrzés (vétó/QA): a DPO): 18 év alatt a résztvevő és a gondviselő együtt, 18 év
> felett a résztvevő (`Adatvédelem – tanulói adatok és AI.md` 4. szakasz). A hozzájárulás
> bizonyítéka ettől még hiányzik ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) R8-2,
> R8-3). Az `M0.A-FOTO-01` adatkezelési kérdéseinek egyetlen helye a kánoni
> `HUM-PRIV-02`; ez a lap nem tart rájuk külön mezőt. Az R8 státuszáról (A vagy B) a döntés
> kifejezetten nem szól. Utólagos ellenőrzés (vétó/QA): a DPO/jogi felelős.

**Mit szabadít fel:** R8 önmagában **0 asset** a központi gyártásból — az egyetlen érintett
tétel (`M0.3-FOTO-01`) az R7-re is vár. Az `M0.A-FOTO-01` élő/runtime tétel.

**Ki dönt:** a Memuna (gyermekvédelmi felelős) + adatvédelmi (DPO) felelős; a felvételek
adatkezeléséről projektgazdai döntés van (`HUM-PRIV-02`, 2026-10-02).

**A válasz helye:** R8 státusza (szabály / kapu): ⟬KITÖLTENDŐ⟭

---

## D10 — A ken alkohol- és dohányzási magatartási kódexe (M3.4) — LEZÁRVA

**Kérdés:** mi a szervezet élesítéskor hatályos, írásban jóváhagyott alkohol- és
dohányzási szabályzata (mit, hol, milyen kortól)?

> **Projektgazdai döntés (2026-10-02, `HUM-SAFE-04`):** kiskorúaknak szóló programon nulla alkohol, dohány, e-cigaretta (vape) és
> nikotintermék; 18 év alatt ezek egyike sem. Felelős felnőtt szolgálat alatt nem fogyaszt
> alkoholt, és nem lehet befolyásolt állapotban. Dohányozni csak szolgálaton kívül, kijelölt
> helyen, a gyerekektől elkülönítve lehet. A törvény minimumként tiltja az alkohol és a
> dohány kiszolgálását 18 év alatt; a szervezet ennél szigorúbb szabályt alkalmaz. A 3C blokk
> tartalma ezt követi. Amíg a leckében álló `decision` mező nem üres, a manifeszt a két
> assetet `emberi döntésre vár` állapotban tartja; a mező kivezetése a lecke és a
> következő build dolga.

**Miért van itt:** ez nem új döntés — a kánoni `Emberi jóváhagyás szükséges.md`
szervezeti tételként tartja nyilván (`HUM-SAFE-04`, 2026-10-02 óta projektgazdai döntéssel
lezárva). A döntés előtt az is látszott, hogy **két média-assetet is gátol**: az
`M3.4-EGY-03` sorting-feladat 6–8. kártyája és az `M3.4-DIA-01` diagram 3C blokkja a kódex
tartalmától függ. A lecke korábban ki is mondta: „Ennek hiányában ez a tartalmi rész nem
élesíthető.” Korábban egyik asset készültségi
állapota sem tükrözte ezt — az `M3.4-EGY-03` emiatt tévesen a „most gyártható” kötegben
állt.

**Mit szabadít fel:** 2 asset / 3 deliverable. Az `M3.4-DIA-01` ezen felül az R5-re is vár.

**Ki döntött:** projektgazdai döntés (2026-10-02, `HUM-SAFE-04`); utólagos ellenőrzés
(vétó/QA): a kánoni `Emberi jóváhagyás szükséges.md` `HUM-SAFE-04` tételében megnevezett
szerepek — köztük a Memuna (gyermekvédelmi felelős), aki a projektgazda által rögzített
jóváhagyói rend szerint gyermekvédelmi ügyben az egyetlen felelős jóváhagyó. Ez a lap nem
nevez meg saját jóváhagyót. A válasz helye is a kánoni `Emberi jóváhagyás szükséges.md`,
nem ez a lap.

**Megjegyzés:** a 3A és 3B témablokk tartalma kész; csak a 3C függ a kódextől.

---

## D11 — Az `M1.3-VID-01` párbeszéde: dialógushangok és gyártási út

**Kérdés:** milyen hangokkal és milyen gyártási úton készüljön az `M1.3-VID-01` két
madrih képernyőn zajló párbeszéde? A
[`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 8. szakasza ehhez **két megkülönböztethető hangot** ír
elő, a stack néma generálása ([`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) 5. szakasz)
viszont erre a jelenetre nem alkalmazható: utólag aláillesztett hangnál nincs szájszinkron.
Nyitott:

- melyik hang(ok) szólaltatják meg a két madrihot — a második hang szerepe a D2 szerint
  külön, későbbi döntés *(2026-10-03: eldőlt — VO D-14, K4, lásd lent)*;
- a dialógushang(ok) jogosultsága (R2, V2);
- a kétszereplős, szájszinkronos gyártási út.

Ugyanez a kérdés érinti az `M4.1-VID-04/05` szereplőjének saját megszólalását is (a 2.
jelenetben „gyorsan beszél”, a 3.-ban egy mondatot mond), ha az hallható hangsávként
készül.

**Miért van itt:** az asset `decision` mezője erre a tételre mutat, ezért a manifeszt
kapuzza: az `M1.3-VID-01` `emberi döntésre vár` állapotú, és a BATCH 6-ban áll, tehát az
R2, R3 és R5 lezárása önmagában nem teszi gyárthatóvá.

> **Projektgazdai döntés (2026-10-02, `HUM-MEDIA-02`):** a D11 a hangjogosultsági
> bizonyítékig blokkolt, és hallgatólagosan nem tekintjük elfogadottnak. A bizonyíték a
> korlátozott hozzáférésű hangjogosultsági nyilvántartásba (`VOICE-RIGHTS-REGISTER`)
> kerül, nem a repositoryba ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md)). Utólagos
> ellenőrzés (vétó/QA): a jogi/adatvédelmi felelős és a hang tulajdonosai.

> **Projektgazdai döntés (2026-10-03, VO D-14, D-15):** az első gyártási körben mindkét madrihot
> a kanonikus narrátorhang szólaltatja meg, beszélőnként külön szegmensben, a feliratban
> beszélőjelöléssel; a második hang kalibrálása után az egyik szerep újrarenderelhető, az azonosítók és
> a felirat változatlanok. Az `M4.1-VID-04/05` szereplője néma, a 3. jelenet mondatát a narrátor
> idézi; karakterhang nem készül. Nyitott marad a kétszereplős, szájszinkronos gyártási út.
>
> **Kiegészítő projektgazdai döntés (2026-10-03, K4; bizonyíték: `01 Fejlesztés/04 Audit/2026-10-03 Projektgazdai döntések – VO 2. fázis, kiegészítés.md`):** az első
> gyártási körben Madrih B szerepét már a második hang mondja, a kalibrálása után (VO QA-repó); Madrih A,
> a képleírás (`M1.3-NAR-08`) és minden más narráció a kanonikus narrátorhanggal szól. Az
> `M1.3-VID-01` hanganyaga a kalibrálásig nem készülhet el; a többi tételt ez nem blokkolja.

**Ki dönt:** a hang-jogosultságról a `HUM-MEDIA-02` jóváhagyói (jogi/privacy felelős + a
hang tulajdonosa); a hangkiosztásról a projektgazda döntött (2026-10-03, VO D-14, K4); a gyártási útról: ⟬KITÖLTENDŐ⟭.

**A válasz helye:**
- dialógushang(ok): **első kör: Madrih A a kanonikus narrátorhang, Madrih B a második hang (a kalibrálása után), beszélőnként szegmentálva** ✅ (VO D-14, K4)
- gyártási út (kétszereplős, szájszinkronos): ⟬KITÖLTENDŐ⟭

**Mit kell utána átírni:** az `M1.3-VID-01` `decision` mezője a leckében (amíg a kérdés
nyitott, ott kell állnia), a [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 8. szakasza, a
[`PRODUCTION-STACK.md`](./PRODUCTION-STACK.md) 5. szakasza, a
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) R2-5 sora (a második dialógushang
jogosultsága), majd build.

---

## Ami NEM döntés, csak függőség

**R7 — véglegesített Moodle-felület.** Egyetlen assetet érint (`M0.3-FOTO-01`), és nem
kérdés, hanem sorrend: a kurzus-főoldal képernyőképe csak az éles felület után
készíthető. Nem indokolja egyetlen más köteg csúszását sem — ez az utolsó tétel. A
vonatkozó runtime-elfogadás az `LMS – H5P runtime acceptance.md` dokumentumban lakik.

**A kurzus release-kapui.** A `RELEASE-READINESS.md`, a gyermekvédelmi és az adatvédelmi
gate NEM ennek a dokumentumnak a hatásköre, és nem is zárható le média-oldalról. A
médiakapuk release-hatásáról viszont projektgazdai döntés van (2026-10-02;
`Emberi jóváhagyás szükséges.md` 5. szakasz; utólagos ellenőrzés (vétó/QA): a release
owner és a jogi/adatvédelmi felelős): a jogi és
a gyermekvédelmi médiakapuk blokkolják az általuk érintett tanulói asset release-ét, és a
teljes release csak akkor `READY`, ha minden release-hatókörű médiakapu zárt, vagy az
érintett assetet eltávolították vagy helyettesítették. A leképezés:
[`RELEASE-MEDIA-STATUS.md`](./RELEASE-MEDIA-STATUS.md) 4. szakasz.

---

## Lezárt döntések (2026-08-27, 2026-10-02, 2026-10-03)

Nyomon követhetőségért; ezek már nem kérdések. A 2026-10-02-án lezárt D1, D5 és D10 a
fenti saját szakaszában maradt, mert ott állnak a kitöltött értékei.

| ID | Döntés | Mi történt a kánoni forrásban |
|---|---|---|
| **D3 (hatály)** | Az R2 a beszélőfej-videókra, az AI karakterjelenetekre és a freeze-frame-ekre is vonatkozik (A opció). | A 28 asset `blockers` mezője változatlanul viszi az R2-t. A bizonyíték-kérdés fent, D3 alatt marad nyitva. |
| **D4** | Az M4 HOOK-formátum marad vegyes: az M4.2–M4.4 statikus illusztrációval nyit, új beszélőfej-videó nem készül (A opció). | Az `M4.2-ILL-01` `decision` mezője kiürült; az asset a szokásos R5 alatt gyártandó. |
| **D6** | Az `M1.3-VID-01` HOOK-dialógjának szövege jóváhagyva (A opció). | A szó szerinti szöveg `@source` blokkba került az M1.3 leckében (`M1.3-VID-01-VO`), az asset `source_ref`-fel hivatkozik rá, a felirat és a leirat onnan generálódik. Az asset továbbra is R2 + R3 + R5 alatt áll. |
| **D7** | Az `M3.2-NAR-02` opcionális narráció **nem készül el** (B opció). | A szemantikus asset és a három deliverable megszűnt; a dia látható tartalma változatlan, csak az „Opcionális narráció (30–40 mp)” sor került ki. A három történeti v1 sor `NO_LONGER_REQUIRED` diszpozícióval, indoklással egyeztetve (`_legacy/legacy-dispositions.json`). |
| **VO D-16** | Az `M5.3-NAR-01` és az `M7.1-NAR-02` opcionális, dia-szöveges narráció **nem készül el** (C opció, a D7 mintája; projektgazdai döntés, 2026-10-03). | A két szemantikus asset és a hat deliverable megszűnt; a dia látható tartalma változatlan, csak az „(Opcionális … narráció …)” sor került ki. A hat történeti v1 sor `NO_LONGER_REQUIRED` diszpozícióval, indoklással egyeztetve (`_legacy/legacy-dispositions.json`). |
| **VO D-18** | Az `M1.3-VID-01` hangalámondásos képleírást kap (a) opció; projektgazdai döntés, 2026-10-03). | Új forrásblokk és asset: `M1.3-NAR-08-VO` / `M1.3-NAR-08` (voiceover, a narrátor hangján, a párbeszéd szüneteiben); átszámozás nincs. A végleges szöveg és időzítés a legyártott videón ellenőrizendő. |
| **VO D-04** | A B4-ben fülre jóváhagyott kiejtések kötelezők: `madrih` „mádrih” [maːdrix], `hanih` [xanix], `Tuckman` „Takmen”, a Tuckman-szakaszok magyaros formái; az írott tananyag nem változik (projektgazdai döntés, 2026-10-03). | `VOICE-BIBLE.md` 6–7., `ELEVENLABS-VOICE-TEST.md` 4., `VOICE-PILOT-SCRIPTS.md` P1–P3 kiejtési táblái. |
| **VO D-05** | A `Leviatán` hangja a fülre jóváhagyott „Leviatan” (B4); az írott alak és a felirat „Leviatán” marad. | `VOICE-BIBLE.md` 6.; a szótár aliasa (Leviatán → Leviatan, Leviatánnál → Leviatannál). |
| **VO D-06** | A `Zmán Kvucá` és a `dugma isit` jóváhagyott kiejtése elfogadva; külön fülpróba nem kell. | `VOICE-BIBLE.md` 6. |
| **VO D-07** | A `112` kimondva „száztizenkettő”; az írott szöveg 112 marad; „egy-egy-kettő” nem. | `VOICE-BIBLE.md` 7. (az `M3.3-NAR-01-VO` hangbemenete); utólagos ellenőrzés (vétó/QA): a Memuna. |
| **VO D-08** | Konzervatív AI-átláthatóság, harmadik fél aláírásának állítása nélkül: a megvalósítási döntést a projektgazda jóváhagyta, a formális szerepköri bizonyíték külön kapu. | `RIGHTS-EVIDENCE.md` („Amit ez a lap NEM állít”); az 50. cikk (4) jogi minősítése és a V1 függő. |
| **VO D-10** | A szünetet elsődlegesen a központozás adja; a sortörés és az üres sor nem szünetvezérlő; szükség esetén utómunkában kb. 0,6–1,0 mp. | `VOICE-BIBLE.md` 5., `VOICE-PILOT-SCRIPTS.md` 5., `PILOT-PRODUCTION-PACK.md` P-NAR. |
| **VO D-11** | Elfogadási feltétel: a jelentést hordozó hangsúly nem sérül (fülre); a félkövér és a CSUPA NAGYBETŰ nem hangsúlyjel. | `VOICE-BIBLE.md` 5., `VOICE-PILOT-SCRIPTS.md` 6., `PILOT-PRODUCTION-PACK.md` P-NAR. |
| **VO D-13** | A kiejtés kanonikus döntési forrása a VO QA-repó B4-regisztere; a P1–P3 és a P-NAR ellenőriz, nem dönt újra; a P-NAR az `M4.2-NAR-03`, várható hossza a mért természetes hossz. | `VOICE-BIBLE.md` 11.2., `PILOT-PRODUCTION-PACK.md` P-NAR, az M4.2 időkerete. |
| **VO D-17** | Valódi túllépésnél a keret a mért természetes hosszra tágul (nem gyorsítás, nem vágás); a `Z.1-NAR-01` kb. 15–20 mp; ahol a keret gondolkodási időt is tartalmaz, a hang hossza és a gondolkodási idő külön szerepel. | A leckék narrációs címkéi és rejtett másolataik (M1–M7, Z); `VOICE-BIBLE.md` 4. |
| **VO D-19** | Csak hangot tartalmazó narrációnál a dián vagy a médiaelem mellett látható leirat a szöveges ekvivalens; a `.vtt` archivált derivatíva; a H5P Audio elemtől feliratsáv nem várható. | `LMS – hozzáférhetőségi sztenderd.md` 1. szakasz, runtime acceptance 22. pont, `VOICE-BIBLE.md` 9., `ASSET-AUTHORING.md` 2.1, a csak hangos narrációk a11y-jegyzete (K2). |
| **VO D-20** | A beszélőfej-videókban egyetlen visszatérő készlet-avatar a kanonikus narrátorhanggal; a J3 formális bizonyítéka függő. | `M1.1-VID-01`, `PRODUCTION-STACK.md` 4., `PILOT-PRODUCTION-PACK.md` P-VID. |
| **VO D-21** | A D9 címke csak hangot tartalmazó narrációnál a leirat első sora és a lecke alján egy sor. | D9 (lent), `Program terv.md` 4., `PRODUCTION-STYLE-TOKEN.md` 7.3., `RIGHTS-EVIDENCE.md` R1-2. |
| **VO D-23** | A további hallgatási tételek az ajánlott alakokkal lezárva (`energizer` „enerdzsájzer”, `13–17` „tizenhárom–tizenhét”, `M2.A` „em kettő pont á”, „az ÉN” → „az én”, `Johari`, `Memunát`); a próbától eltérő hangzás regresszió, nem új döntés. | `VOICE-BIBLE.md` 7., `ELEVENLABS-VOICE-TEST.md` 4. |
| **2026-10-03-A** | A nyilvános kurzusrepóban a hangok csak szerepnéven szerepelnek („kanonikus narrátorhang”, „második hang”); a hangnevek csak a VO QA-repóban. | Minden VO 2. fázisú szöveg; a döntésmásolat szerepnevekkel. |
| **2026-10-03-B** | Nincs automatikus lejátszás: hang és videó soha nem indul el magától (IMPL-34; szigorúbb a WCAG 2.2 SC 1.4.2-nél). | `LMS – hozzáférhetőségi sztenderd.md` 1. szakasz és checklist, runtime acceptance 23. pont, `PILOT-PRODUCTION-PACK.md` P-NAR/P-VID, `PRODUCTION-STACK.md` 9. |
| **K2** | A csak hangot tartalmazó narrációk a11y-jegyzete egységesen a VO D-19 szerint (kiegészítő projektgazdai döntés, 2026-10-03). | 70 narráció a11y-jegyzete; a `captions` archivált .vtt-derivatívaként marad, a deliverable-ek száma nem változik. |
| **K3** | A voice-ID csak a VO QA-repó gyártási konfigurációjában él, a kurzusrepóba nem kerül (kiegészítő projektgazdai döntés, 2026-10-03). | `VOICE-BIBLE.md` 12., D2 (fent), `README.md`, `RIGHTS-EVIDENCE.md` R2-4, `produkcios-szabalyok.json` R3, `HUM-MEDIA-02`. |
| **K4** | A második hang az első gyártási körben az `M1.3-VID-01` Madrih B szerepét mondja, a kalibrálása után; a VO D-14 erre az egy tételre módosul (kiegészítő projektgazdai döntés, 2026-10-03). | `VOICE-BIBLE.md` 8., 11., 12.; D11 (fent); az `M1.3-VID-01` `decision` mezője; `PRODUCTION-STACK.md`, `PILOT-PRODUCTION-PACK.md`, `ELEVENLABS-VOICE-TEST.md`, `produkcios-szabalyok.json` R3. |
| **K5** | A két forrás-beszélő (`VOICE-SRC-01`, `VOICE-SRC-02`) nagykorú — projektgazdai tényközlés (2026-10-03), a VO D-01 mintájára; a formális igazolás (a `VOICE-RIGHTS-REGISTER` nem személyes hivatkozása, jóváhagyói minősítés) bizonyíték-kapu marad (VO D-08); életkor, születési dátum a repóba nem kerül. | `ELEVENLABS-VOICE-TEST.md` 1.0.; `RIGHTS-EVIDENCE.md` R2-5. |
| **D9** | A kanonikus, tanulónak látható AI-provenance címke szövege: **„AI-generált médiaelem · emberi lektorálással.”** | Rögzítve a `produkcios-szabalyok.json` R1 szabályában (`human_label` mező), és kivezetve mind a 21 aktív előfordulásra a tananyagban. A címke **vizuális megjelenése és elhelyezése** a D1 első lépcsőjéből következik (2026-10-02: élő LMS-szöveg, a `PRODUCTION-STYLE-TOKEN.md` 7.3. pontja szerint). Csak hangot tartalmazó narrációnál a címke a leirat első sora és a lecke alján egy sor (VO D-21, 2026-10-03). |
| **F-02** | Az élő/runtime tételek nem számítanak a központi „most gyártható” kötegbe. | `technical.production_phase: trainer-at-runtime` három asseten (`M0.A-EGY-01`, `M0.A-FOTO-01`, `Z.A-KART-04`); a produkciós terv külön szakaszban mutatja őket, a rájuk vonatkozó kapukkal együtt. A követelményük és a deliverable-jük megmarad. |
