# 🏭 Produkciós stack — döntés-előkészítés

Ez a lap egy helyen írja le, **mivel és hogyan** készülne el a 901 deliverable, ha a
nyitott döntések megszületnek. **Nem lezárás, nem jóváhagyás, és nem indít gyártást.**

| | |
|---|---|
| **Státusz** | NYITOTT — FELHASZNÁLÓI DÖNTÉS SZÜKSÉGES |
| **Mit változtat a manifeszten** | semmit. A 417 asset, a 901 deliverable és a blokkolók ettől a laptól nem változnak: a blokkolókat a leckék deklarációi és a `produkcios-szabalyok.json` viszik. |
| **Mit fizettünk** | semmit. Fizetős API-t nem hívtunk, fiókot nem hoztunk létre, próbaidőszakot nem indítottunk, médiát nem generáltunk. |
| **Kutatás dátuma** | 2026-08-27 (minden külső forrás ekkor lekérdezve) |

Kapcsolódó lapok: [`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md) ·
[`VOICE-BIBLE.md`](./VOICE-BIBLE.md) ·
[`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md) ·
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) ·
[`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md) ·
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md)

---

## 1. A jelenlegi produkciós architektúra

A rendszer, amibe a stack beleilleszkedik, **már megvan**, és nem ez a lap alkotja:

| Réteg | Hol él | Ki tartja karban |
|---|---|---|
| Asset-követelmény | `@asset` blokk a leckefájlban | szerző |
| Felmondandó/alt szöveg | `@source` blokk **ugyanabban a leckében** | szerző |
| Fordítás → manifeszt | `tools/media_manifest.py build` | determinisztikus, offline |
| Produkciós szabályok (R1–R8) | `produkcios-szabalyok.json` | kézzel, döntéskor |
| Köteg-terv | `MEDIA-PRODUCTION-PLAN.md` + `media-production-plan.csv` | generált |
| Nyitott emberi döntések | `PRODUCTION-DECISIONS.md` | kézzel |

**Ebből következik a stack első szabálya:** a gyártó eszköz **soha nem forrás**. A
szöveget a lecke adja, a fájl abból készül, és a `source_hash` mondja meg, melyik
szövegverzióhoz. Ha a lecke változik, a fájl újra készül — nincs „a videóba beleírt”
igazság.

### Jelenlegi darabszámok

| | Asset | Deliverable |
|---|---:|---:|
| Összesen | 417 | 901 |
| Központilag előgyártható | 406 | 896 |
| **Most gyártható (nincs nyitott kapu)** | **36** | **36** |
| Élő/runtime (a képző hozza létre a peulán) | 3 | 5 |

---

## 2. Vizuális rendszer — a D1 lezárva (2026-10-02)

**Részletek és a számított kontrasztok:**
[`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md).

Röviden: a mozgalomnak **van hivatalos arculati kézikönyve**, deklarált HEX / RGB / CMYK
/ Pantone palettával, és a hat alapszín a hivatalos logó-SVG-ből byte-azonosan
megerősíthető. A D1 kérdése ezért nem „mi legyen a paletta”, hanem „átvesszük-e” volt. A
válasz (projektgazdai döntés, 2026-10-02, `HUM-MEDIA-01`): **igen** — a 2022-es kézikönyv és
a hivatalos SVG színgenerációja a kánon, a produkciós rendszer pedig a B változat
([`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D1). Utólagos ellenőrzés
(vétó/QA): a kreatív/márkafelelős.

| Alapszín | HEX | Alapszín | HEX |
|---|---|---|---|
| piros | `#D84C15` | sötét zöld | `#369D37` |
| sárga | `#F2BC00` | sötét kék | `#08A0CA` |
| zöld | `#87B027` | kék | `#82CDE9` |

**A mérés, ami a használatot eldönti:** egyetlen márkaszín sem éri el a 4,5:1-et fehéren,
és a tizenöt színpár közül egy sem a 3:1-et egymáshoz képest. Ezért:

- a márkaszínek **felületszínek**, a szöveg rajtuk `#1D1D1B` (a hivatalos monokróm
  változat feketéje, 16,88:1 fehéren);
- a jelentést mindig **forma vagy betűjel** hordozza, a szín kíséri;
- a szín-szótár **modul-hatókörű**, nem globális.

**Elfogadott változat: B** (projektgazdai döntés, 2026-10-02) — azonos márkaszínek és logóhasználat, de a tananyag-produkcióhoz
nyílt licencű betűtípus (Source Sans 3, SIL OFL 1.1; mérve: mind a **18** magyar ékezetes
glif, valamint `·`, `„`, `”`, `–`, `—`, `✓`, `☐` megvan) és egy `#1D1D1B`-ből származtatott
semleges skála. Indok: az A változat a Myriad Pro **beágyazási licencének** meg nem
válaszolt jogi kérdésétől tenné függővé 245 asset indulását.

---

## 3. Hang — a szolgáltató ELDŐLT

**Felhasználói döntés, 2026-08-28: a felmondás szintetikus, a motor az ElevenLabs.**
Részletek: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 12–13. szakasz. A hangválasztás
végrehajtható terve: [`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md).

| | Állapot |
|---|---|
| **Szolgáltató** | ✅ **ElevenLabs** — lezárva |
| **Hangjelöltek** | ✅ **VOICE-SRC-01** · **VOICE-SRC-02** — forrás-beszélők; a belőlük készülő ElevenLabs hangok **még nem jöttek létre** |
| **Kanonikus hang** | ⛔ **meghallgatásos döntés** — 6 minta, 3 216 karakter, ≈ 0,16–0,64 $ |
| **Modell** | 🔎 javaslat: **`eleven_flash_v2_5`**, `language_code: "hu"` |
| **Tempó** | `speed` paraméter (0,7–1,2) a 100–120 szó/perc célsávra |
| **Kiejtés** | alias-szabályok szótárban — **csak a ténylegesen hibás szavakra**, a teszt után |
| **Voice-ID / hangtípus** | ⛔ **NINCS — a hangok még nem jöttek létre** (V2 bizonyíték → tanítási kimaradás → létrehozás → azonosítás; lásd ELEVENLABS-VOICE-TEST 1.0–1.2) |
| **Költség** | teljes tananyag 3× nyers: **7,50 – 45 $** (a szolgáltató két árazási olvasata szerint, lásd 5/A) |

**A modellválasztás egyetlen meglepetése:** a szolgáltató leghosszabb formára
legstabilabbnak jelölt modellje, az `eleven_multilingual_v2`, **nem támogatja a magyart**
(29 nyelv, a `hu` nincs köztük). A magyar tehát leszorít a stabilitási zászlóshajóról. A
maradék két jelölt közül az `eleven_v3`-on **nincs tempó-vezérlés** — a tananyag viszont
kötött 100–120 szó/perc célsávot ír elő —, ezért a javaslat a `flash_v2_5`.

> **A hang nem választható ki dokumentációból.** A két — még létrehozandó — hang közti választás
> meghallgatásos emberi döntés; a modell-javaslatot is a hangtípus erősíti meg (ha
> bármelyik hang PVC, a `v3` kiesik).

### 3.1. Amit a hang oldalán tudni kell, mielőtt bármi elindul

- **A tanítási kimaradást előre kell bekapcsolni.** A szolgáltató kimaradása
  **csak előremutató** — visszamenőleg nem hat, és csak a kérés feldolgozása után lép
  életbe. Minden fiókban kell, ahová forrásfelvétel kerül (PVC-nél a forrás-beszélőében
  is). **A kimaradás a jogi kérdést nem zárja le:** a feltöltött felvételekre adott
  licencet a szolgáltató „perpetual and irrevocable” licencként írja le; hogy ebből mit
  érint a kimaradás, jogi kérdés (EGT-s feltételek 4(i)/4(d), lekérdezve 2026-10-02;
  [`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md) 1.2.,
  [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) E-4/E-9).
- **Minden kérésben explicit a teljes beállítás-készlet.** A kérésben küldött érték
  felülírja a hangon tároltat, de csak arra a kérésre; a tároltra hagyatkozva a kimenet
  később csendben megváltozhat.
- **A determinizmusnak van plafonja.** A szolgáltató kimondja, hogy modelljei nem
  determinisztikusak, és a `seed` is csak „best effort”. Fél év múlva egy újragyártott
  klip **hasonló lesz, nem bitre azonos** — ezért újragyártásnál mindig meghallgatás, és
  inkább a teljes tétel újravétele, mint mondat-beillesztés.
- **A hang oldalán nincs használható gépi provenance.** A szolgáltató hallhatatlan
  hangvízjelet ágyaz be, de robusztussági leírást nem publikál, a lefedettséget nem
  nyilvánította befejezettnek, és a beszéd-kimeneten **nincs C2PA**. Az R1 gépi ága itt
  **nem értelmezhető**; a kötelezettséget a tanulónak látható címke és a saját
  manifeszt-fegyelem viszi.

---

## 4. Beszélőfej-videó — a szolgáltató ELDŐLT

**Felhasználói döntés, 2026-08-28: a beszélőfej-videók szolgáltatója a HeyGen.**
Hatókör: **21 asset.**

A gyártási architektúra ezzel véglegesen kétlépcsős: **a hangot az ElevenLabs adja, a
képet és a szájszinkront a HeyGen.**

| | Érték |
|---|---|
| **Szolgáltató** | ✅ **HeyGen** — lezárva |
| **Hang-integráció** | **feltöltött ElevenLabs hangmester** — a séma szerint a szöveges szkript-mező és a hang-mező **kölcsönösen kizárja egymást**, tehát a szolgáltató saját TTS-e nem szólalhat meg |
| **Avatar-stratégia** | **egyetlen nyilvános készlet-avatar** a beszélőfej-videókra. A készlet-avatar képmás-licencét a szolgáltató feltételei szerint dokumentálni kell (`HUM-MEDIA-03`, R2-3). Gyermekvédelmi vagy krízis-HOOK-ban nincs készlet-AI-beszélőfej: az `M2.4-VID-01`, az `M3.3-VID-01` és az `M3.4-VID-01` hangalámondás + tipográfia/grafika (projektgazdai döntés, 2026-10-02; utólagos ellenőrzés (vétó/QA): a jogi/adatvédelmi felelős, az érintett jogosultak és a Memuna) |
| **Arány / felbontás** | **16:9** (explicit megadva), 1080p, 25 fps |
| **Felirat** | a lecke `@source` szövegéből, **nem** a szolgáltató SRT-kimenetéből |
| **Költség (21 × 30 mp + 100% újragyártás ≈ 1 260 mp)** | **≈ 21 $** készlet-avatarral |

### 4.1. A hangfeltöltés — ez a lánc kritikus pontja, és ellenőriztük

A szolgáltató gépi API-leírása szó szerint kimondja a kölcsönös kizárást mindkét irányban:
a szöveges szkript-mező „Mutually exclusive with audio_url/audio_asset_id”, a hang-mezők
pedig „Mutually exclusive with script”. Ugyanez a szabály még egyértelműbben, egy másik
séma leírásában: **„exactly one of (script + voice_id), audio_url, or audio_asset_id”** —
tehát a három forrás közül **pontosan egy** adható meg. Ezt **a szolgáltató saját
gépi API-leírásából ellenőriztük**, nem másodkézből.

A mezők a kérésben **egy szinten állnak** (nincs külön „voice” objektum, és nincs
típus-kapcsoló); a kizárást a szolgáltató szerveroldali ellenőrzése tartatja be, nem
formális séma-szerkezet. Gyakorlati következmény nálunk nincs — a szkript-mezőt üresen
hagyjuk —, de a megvalósításnál tudni kell, hogy **hiba esetén a szerver utasítja el a
kérést**, nem a séma-validáció.

Független megerősítés ugyanonnan: a szolgáltató kiejtési szószedet-mezője kifejezetten
azt írja, hogy csak akkor él, ha a hang a szkriptből szintetizálódik, és a hívó által
feltöltött hangot **nem érinti**. A szolgáltató kiejtési rétege tehát a mi hangunkhoz
hozzá sem tud nyúlni.

**A gyártási lánc három lépés**, a szolgáltató jelenlegi API-ján:

| # | Lépés | Végpont | Amit visszaad |
|---|---|---|---|
| 1 | a hangmester feltöltése | `POST /v3/assets` (multipart, `file`) | asset-azonosító |
| 2 | a videó létrehozása | `POST /v3/videos` (`CreateVideoFromAvatar` séma) — az avatar-azonosító + `audio_asset_id`; **a `script` mező üresen marad** | videó-azonosító |
| 3 | állapot lekérdezése | `GET /v3/videos/{id}` | a kész videó ideiglenes letöltési linkje |

A letöltési hivatkozás ideiglenes; a kész fájlt **azonnal archiválni kell**. A szolgáltató
nem archívum.

> ⚠️ **A régi API-útvonal kivezetés alatt áll.** A szolgáltató korábbi, `v1`/`v2`
> generációs videó-végpontját a saját közlése szerint **2026. október 31. után**
> nyugdíjazza, és annak kérés-alakja **más** (beágyazott hang-objektum, dokumentált
> feltöltött-hang mező nélkül). A fenti lánc a **jelenlegi** végpontokra épül. Ez a
> 4.3. szakasz időablak-érvelését is élesíti: a gyártási ablakot a kivezetési dátum
> **elé** vagy tudatosan **utána** kell tenni — de nem a határra.

### 4.2. Négy dolog, amit a dokumentáció NEM mond meg

Ezek nem hiányosságok a kutatásban — a szolgáltató nem publikálja őket. Mind a négy
**egyetlen próbarendereléssel** eldől, és ezért került a pilot elfogadási feltételei közé:

1. **Sértetlen marad-e a feltöltött hangmester**, vagy a kimenet újrakódolja.
2. **Kerül-e gépi provenance-jelölés a kimenetbe.** A szolgáltató egy szabványügyi
   kezdeményezésben való **tagságot** említ, de sehol nem állítja, hogy Content
   Credentials kerülne a fájlba.
3. **Tényleg vízjelmentes-e** a fizetős render — a dokumentáció ezt nem mondja ki
   kifejezetten.
4. **Átengedi-e az automatikus moderáció** ezt a tananyagot: a tiltott kategóriák közt
   szerepel a politikai tartalom, és az érzékeny („conditional”) oktatási anyag a
   szabályzat szerint csak egyedi avatarral készíthető. A gyermekvédelmi és krízis-HOOK-ok
   a projektgazdai döntés szerint nem készülnek beszélőfejjel (`HUM-MEDIA-03`), ezért rájuk ez
   a próba nem vonatkozik.

### 4.3. Reprodukálhatóság — ez a stack leggyengébb pontja

A szolgáltató avatar-leíró rekordjában **nincs verzió-mező** — ezt a gépi API-leírásból
ellenőriztük: a rekord tizenöt mezője közül egyik sem verzió. A szolgáltató emellett
menet közben változtatja a motorok viselkedését, és nem ad megjelenés-stabilitási
garanciát.

**Produkciós következmény:** a 21 beszélőfej-videót **egyetlen szűk időablakban** kell
legyártani, nem hónapokra elosztva, és minden kész fájlt archiválni kell. Egy év múlva
egyetlen klip újragyártására nincs garancia, hogy ugyanaz az arc jön vissza.

---

## 5. AI karakter-jelenet — javaslat

Hatókör: **5 jelenet + 1 B-roll**, és a belőlük kivett **2 freeze-frame**.

A nehézség nem a videó, hanem a **karakter-azonosság**: az `M4.1-FOTO-01` specifikációja
szó szerint „ugyanaz a madrich karba tett kézzel vs. nyitott kézzel” — tehát a három
jelenetben ugyanannak az embernek kell látszania.

| | Javaslat | Tartalék |
|---|---|---|
| **Karakter-rögzítés** | képgenerátor karakter-referenciából (`gemini-3-pro-image`); a dokumentáció **legfeljebb 5 referenciaképet** enged a karakter-konzisztenciához; a referenciakészlet **verziókövetve** | ugyanaz — **ez is Google generatív szolgáltatás**, tehát a J1 kérdése erre a lépésre is kiterjed; a J1-tartalék (12. szakasz) csak a videót cseréli, ezt a lépést nem |
| **Videó** | Veo 3.1 GA (`veo-3.1-generate-001`) fizetős Vertex AI-on | Runway Gen-4.5 |
| **Konzisztencia-mechanizmus** | első képkocka + **legfeljebb 3 `asset` referenciakép**; `enhancePrompt: false` mellett rögzített seed | `referenceImages` (max 3), csak az első képkockára |
| **Hang** | **`generateAudio: false`** — a videó néma készül, a D2 narrációja utómunkában kerül alá. **Nem alkalmazható** az `M1.3-VID-01` kétszereplős, képernyőn zajló párbeszédére, és nem adja ki az `M4.1-VID-04/05` szereplőjének saját megszólalását sem — lásd lent | néma generálás, majd utómunka |
| **Freeze-frame** | képkocka-kivétel a kész jelenetből (`ffmpeg`), nem külön generálás | ugyanaz |
| **Provenance** | SynthID + C2PA | C2PA |
| **Költség** | ≈ 36–144 $ (45–90 generálás, 3–5× selejt-aránnyal számolva; lásd 5/A) | hasonló, viszonteladói áron |

**Miért néma generálás:** egyszerre feleannyiba kerül, kizárja, hogy a modell magyar
helyett kitalált nyelvet mondjon, és **nyitva tartja a D2-t** — a hang bármikor
lecserélhető a videó újragenerálása nélkül.

**Ahol a néma generálás nem elég:** az `M1.3-VID-01` két madrich képernyőn zajló
párbeszéde — utólag aláillesztett hangnál nincs szájszinkron, és a
[`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 8. szakasza két megkülönböztethető hangot ír elő —,
valamint az `M4.1-VID-04/05` szereplőjének saját megszólalása (a 2. jelenetben „gyorsan
beszél”, a 3.-ban egy mondatot mond), ha az hallható hangsávként készül. Ezek gyártási
útja és hangja nyitott döntés: [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D11.

> ⚠️ **Ez a javaslat jogi felülvizsgálat alatt áll.** A Google Cloud feltételei
> tartalmaznak egy 18 év alatti hozzáférésre vonatkozó záradékot, amelynek alkalmazása
> erre a felhasználásra **nem eldöntött** — lásd
> [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.3. J1. Ha a jogi jóváhagyó ezt
> kizárónak minősíti, a tartalék stack lép életbe. A kérdés a karakter-lock
> képgenerátorát (`gemini-3-pro-image`) is érinti; a dokumentált tartalék (12. szakasz)
> csak a videót cseréli, a képi lépésre nem ad választ.

---

## 5/A. Költségmodell — durva, de forrásolt

Nyilvános, jelenlegi listaárakból. **Nem árajánlat, és nem tartalmaz áfát vagy
árfolyamkockázatot.** A bizonytalanság a szolgáltatói árnál ±30%, a selejt-aránynál
lényegesen több — a generatív videónál 3–5 próbálkozásból lesz egy használható felvétel,
és ez a becslés legingatagabb eleme.

### Szolgáltatói díj

| Köteg | Feltételezés | Alsó | Felső |
|---|---|---:|---:|
| **Hangválasztási teszt** — 6 minta, 2 hang × 3 szkript | **3 216 karakter, mérve** | **≈ 0,16 $** | **≈ 0,64 $** |
| **Hang** — ElevenLabs `flash_v2_5`, teljes tananyag 3× nyers | 150 000–225 000 karakter | **7,50 $** | **45,00 $** |
| **Hang** — ElevenLabs `v3` (tartalék modell) | ugyanaz | 15,00 $ | 90,00 $ |
| **Beszélőfej** — HeyGen, **nyilvános készlet-avatar** | 21 × 30 mp + 100% újragyártás ≈ 1 260 mp | **≈ 21 $** | **≈ 21 $** |
| **Beszélőfej** — HeyGen, saját fotó-avatar (ha a moderáció megköveteli — érzékeny tartalomnál csak nagykorú személy egyedi avatarja, kifejezett hozzájárulással, jogi/adatvédelmi és gyermekvédelmi felülvizsgálattal: `HUM-MEDIA-03`, R2-3) | ugyanaz + avatar-létrehozás | ≈ 56 $ | ≈ 64 $ |
| **Karakter-jelenet** — Veo 3.1, néma, 1080p | 15–18 használható 8 mp-es felvétel, 3–5× selejt → **45–90 generálás** | **36 $** | **144 $** |
| **Karakter-lock** — referenciakép-készlet | 20–40 kép | **3 $** | **6 $** |
| **Freeze-frame** | képkocka-kivétel a kész videóból | **0 $** | **0 $** |

> ⚠️ **A hang árában a szolgáltató két árazási felülete nem mond ugyanazt.** Az
> API-árazási oldal karakteralapú dollárárat közöl; a fő árazási oldal kredit-alapon
> számol, és a Flash-re *sávot* ad, nem rögzített szorzót. A fenti alsó becslés az
> elsőből, a felső a másodikból jön. **A nagyságrend így is tíz–ötven dollár** — a
> tényleges elszámolást az első köteg után a fiókban kell ellenőrizni. Részletek:
> [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.9.
>
> ⚠️ **A Veo per-másodperc díja nincs idézve, mert a szolgáltató árlapja nem volt
> lekérdezhető.** A fenti sáv 0,80–1,60 $ / 8 mp-es klip feltételezésen nyugszik (a
> gyorsabb és a teljes minőségű változat között). **Ajánlatkérés vagy az élő árlap
> ellenőrzése nélkül ez a sor tájékoztató.**
>
> ⚠️ **A 15–18 felvételes feltevés alulbecsülhet.** A leckék szerint az `M1.3-VID-01` kb.
> 60–70 mp, az `M4.1-VID-03/04/05` jelenetenként 20–25 mp, az `M1.1-VID-02` pedig
> legfeljebb 40–60 mp-es blokkokban készül. Ha a B-roll egy teljes, kb. 40 mp-es blokk,
> 8 mp-es klipekkel ez legalább kb. 22 használható felvétel, és akkor a karakter-jelenet
> sora **alulbecsül**.

**Összesítés a jelenlegi döntések szerint** (hangválasztási teszt + teljes hang +
beszélőfej készlet-avatarral + karakter-jelenet + karakter-lock):

| Útvonal | Alsó | Felső |
|---|---:|---:|
| **ElevenLabs + HeyGen + Veo** | **≈ 68 $** | **≈ 217 $** |

*(Ha a moderáció miatt saját fotó-avatar kell a beszélőfejhez, a felső becslés ≈ 260 $.)*

A hang ebben már benne van: a szintetikus ág a teljes tananyagra **7,50–45 $** (a
szolgáltató két árazási olvasata szerint). Az
emberi felmondó mint alternatíva **lekerült a napirendről** — a felhasználó a szintetikus
utat választotta.

> **A csomagot ne a karakterár döntse el.** A hang oldalán a Creator-szintű előfizetés
> (havi ≈ 22 $) elég a kereskedelmi használathoz, a 192 kbps MP3-mesterhez és a 3× nyers
> kerethez; **veszteségmentes WAV-mesterhez viszont Pro-szint kell (havi ≈ 99 $)**. Ez
> valódi minőségi döntés: Creator-on minden mester veszteséges, és minden derivatíva
> másodgenerációs tömörítés. A képi oldalon a szolgáltató előre feltöltött egyenlegről
> megy, előfizetés nélkül, néhány dolláros belépővel. PVC-útnál ehhez jön, hogy a hang a
> forrás-beszélő saját fiókjában jön létre (`HUM-MEDIA-02`), a PVC-hez pedig
> Creator-csomag vagy feljebb kell ([`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.4.) — ez a
> fiók a költségmodellben még nem szerepel.

### Emberi munka — ez a nagyobb tétel

A szolgáltatói díj ezen a volumenen **nem a fő költség**. Ami az:

| Tevékenység | Becslés | Megjegyzés |
|---|---|---|
| Pilot-kör családonként (gyártás + 4 review + javítás) | 9 pilot × 2–5 óra | a 13. szakasz jóváhagyási lánca a [`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md)-ben |
| Determinisztikus forrás megírása (SVG / HTML) | a 245 vizuális tétel érdemi része | egyszeri sablon után tételenként rövidül |
| Lektorálás — **kötelező**, nem opció | minden AI-eredetű tételen | az R1-címke szó szerint „emberi lektorálással” |
| Felirat- és leirat-ellenőrzés | 117 beszélt tétel | a szöveg generált, az **időzítés** nem |
| Újravétel szövegváltozás után | a `source_hash` mutatja, mit érint | ez a v2 architektúra fő haszna: pontosan látszik, mit kell újra |

**Nem adunk embernap-becslést**, mert a repositoryban nincs rá adat, és egy kitalált szám
költségvetési kötelezettséget hamisítana.

---

## 6. Fájlformátumok

A leckék technikai jegyzeteiből levezetve; ahol a repository nem rendelkezik, az
**ajánlás** jelölve.

**Jelölés:** ✅ = a leckék technikai jegyzeteiből származó kötelező érték · ▫️ = **produkciós
ajánlás**, a repositoryban nincs rá forrás.

| Család | Mester | Kimenet | Megjegyzés |
|---|---|---|---|
| Narráció | ▫️ WAV **48 kHz** / 16 bit / mono (`wav_48000` — a szolgáltató formátum-listájában létezik, ellenőrizve) | ✅ MP3 (H5P Course Presentation), szükség szerint AAC | „tiszta beszéd, háttérzaj nélkül”; egy asset = egy fájl |
| Videó | ✅ 16:9 · ▫️ MP4 / H.264, 1920 × 1080 | ugyanaz + `.vtt` felirat | égetett felirat nincs |
| Felirat | `.vtt` | — | WCAG 2.2 SC 1.2.2 |
| Leirat | Markdown → a dián látható szövegként, a médiaelem mellől megnyitható szövegként vagy linkelt leirat-oldalként (a Course Presentation diáinak nincs jegyzetmezője) | — | SC 1.2.1; a runtime-elérhetőséget az `LMS – H5P runtime acceptance.md` szerint kell igazolni |
| Ikon | **SVG** | PNG átlátszó háttérrel, ≥ 64 × 64 px | H5P-kompatibilis, retina |
| Diagram | **SVG** | PNG tartalék | mobile-first; **két arány-változat** (lásd 7.4.) |
| Illusztráció | ▫️ SVG mester, benne a generált PNG-alap + vektoros szövegréteg | PNG export | generált szöveg a képben nincs |
| Nyomtatvány, kártya, poszter | ▫️ HTML/CSS forrás | ▫️ PDF (a PDF/A-kompatibilitás javaslat, nem repository-követelmény) | ✅ A4 alap; A5/A6 kártya; A3/A2/A1 poszter |
| Alt-szöveg | a leckében, `@source` blokkban | — | a manifesztből generálódik |

### 6.1. Determinisztikus vektor- és dokumentum-útvonal

A diagram, munkalap, kártya, poszter és ikon családokra **nem generatív**, hanem
determinisztikus útvonalat javasolunk. Ezt nem elvből: **kipróbáltuk**.

| Eszköz | Mire | Eredmény |
|---|---|---|
| HTML/CSS → PDF (WeasyPrint 68.1) | munkalap, kártyaszett, poszter | egyoldalas A4 pontosan 210 × 297 mm; a magyar ékezetek (`ő`, `ű`, `í`) helyesen; **két futtatás bájtra azonos PDF-et adott** (`SOURCE_DATE_EPOCH` rögzítésével); a szövegréteg megmarad, tehát kereshető és felolvasható |
| Kézzel írt SVG → PNG/PDF (rsvg-convert 2.61.3) | diagram, ikon | **két futtatás bájtra azonos PNG-t adott**; a `<title>` és `<desc>` elem viszi az akadálymentesítési szöveget |
| Kétoldalas kártyaív | 4 kártya/A4, szaggatott vágóvonal, **tükrözött oszlopsorrend a hátoldalon** | a hosszú élű duplex illeszkedik; a hátlapon forma-glif (▣ / ◆ / ●) viszi a jelentést szín nélkül is |

**Miért ez a jó irány:** a szöveg a forrásban marad (git-diffelhető), a magyar tipográfia
nem a generátor szeszélyén múlik, egy javítás percek alatt újrafuttatható, és a kimenet
reprodukálható.

> **Ez a pass nem épít renderelő keretrendszert.** A fenti próba ideiglenes munkakönyvtárban
> készült, és nem került a repositoryba. A tényleges építése önálló feladat, a pilotok
> jóváhagyása után.

---

## 7. Elnevezés és verziózás

### 7.1. Javasolt tárolási szerkezet

Ma nincs `media/` könyvtár a repositoryban. Javaslat:

```
media/
  source/       — szerkeszthető forrás: .svg, .html, .css, prompt- és seed-jegyzék
  masters/      — a jóváhagyott mester: .wav, .mp4, .svg, .pdf
  derivatives/  — a mesterből levezetett: .mp3, .vtt, .png, print .pdf
```

**Ez konvenció, nem üres fájlok gyártása.** Egyetlen placeholder sem jön létre előre.

### 7.2. Fájlnév

```
<asset-id>__master.<ext>
<asset-id>__captions.hu.vtt
<asset-id>__transcript.hu.md
<asset-id>__alt.txt
<asset-id>__print.pdf
```

Az `<asset-id>` **pontosan** a manifeszt azonosítója (`M5.1-VID-01`). A deliverable-ek
`::` utótagja fájlnévben `__` alakot kap, mert a `::` több fájlrendszeren problémás.

### 7.2/A. Hang-mester és reprodukciós kísérőadat

A hang-mester **ugyanazt a névkonvenciót követi, mint minden más mester** (7.2.) — a
verziót itt sem a fájlnév viszi, hanem a git és a `source_hash`:

```
<asset-id>__master.wav        — mester
<asset-id>__master.json       — reprodukciós kísérőadat (nem titkos)
<asset-id>__master.mp3        — Moodle/H5P derivatíva
```

**A hangnál viszont a kísérőadat nem opcionális**, mert a szolgáltató modelljei nem
determinisztikusak: a fájl önmagában nem mondja meg, milyen hangból, modellből és
beállításból készült. A jóváhagyási körök alatt itt is használható `__v0` / `__v1`
utótag; az elfogadott változat utótag nélkül kerül a `masters/` alá.

A kísérőadat **pontosan azt tartalmazza, ami nélkül a felvétel nem reprodukálható:**

| Mező | Miért |
|---|---|
| `asset_id`, `source_hash` | melyik szövegverzióhoz készült |
| `provider` (`elevenlabs`), `voice_id`, `voice_display_name`, `voice_type` | **a név nem azonosító** — a megjelenített név megváltoztatható, a voice-ID nem |
| `model_id`, `language_code` | a modell és a nyelvi kényszer |
| `voice_settings` (mind az öt mező), `seed` | a hangzás rögzítése |
| `pronunciation_dictionary_id` **és `version_id`** | a szótár verziója nélkül csendben elcsúszik |
| `use_pvc_as_ivc`, `apply_text_normalization` | PVC-nél két különböző renderelés létezik |
| `output_format`, `generated_at`, `output_sha256` | mit kaptunk és mikor |

**A videó oldalán ugyanez, a képi rétegre:** szolgáltató, avatar-azonosító és
avatar-csoport, motor-típus, felbontás, arány, a **feltöltött hang SHA-256-ja**, a videó
azonosítója, a hossz, a teljes kérés-objektum és a kimenet hash-e.

**Amit soha nem tárolunk a repositoryban:** API-kulcs, fióktoken, privát tanító-felvétel,
és személyes adatot tartalmazó hozzájáruló nyilatkozat. Ezekből csak a *létezés* ténye és
egy nem-személyes hivatkozás kerülhet a bizonyíték-nyilvántartásba.

### 7.3. Verzió

- A mester fájlnév **nem hordoz verziószámot.** A verziót a git és a manifeszt
  `source_hash` mezője adja: az mondja meg, melyik szövegverzióhoz készült.
- A jóváhagyási körökhöz `__v0`, `__v1` utótag használható **a pilot alatt**; az elfogadott
  változat utótag nélkül kerül a `masters/` alá.
- **Beszélt asseteknél a `source_hash` a kötelező kísérőadat.** Ha a lecke szövege
  változik, a hash változik, és a fájlt újra kell venni.

### 7.4. Két arány-változat a diagramoknál

A leckék „mobile-first, vízszintes → függőleges” elrendezést írnak elő. Ezt egyetlen SVG
nem tudja teljesíteni. Javaslat: `<asset-id>__master-wide.svg` és
`<asset-id>__master-tall.svg` ugyanabból a forrásból. **Ez nem növeli a deliverable-ek
számát** — egy deliverable, két arányban exportálva.

---

## 8. Provenance

Két, egymástól független réteg. Ezt a repository már eldöntötte, nem ez a lap.

| Réteg | Hol | Kötelező tartalom |
|---|---|---|
| **Ember-olvasható** | az LMS-ben, a médiaelem alatt, **valódi kijelölhető szövegként** — nem a képbe égetve | szó szerint: **AI-generált médiaelem · emberi lektorálással.** |
| **Gépi** | magában az exportált fájlban (C2PA / Content Credentials / SynthID / vízjel) | ha a generátor ad ilyet, az export **nem távolíthatja el** |

Bizonyíték az első sorra: `M5.1-EGY-01` a11y-jegyzete („Valódi kijelölhető szöveg legyen,
ne képbe égetve.”) és `M6.1-EGY-01` („Olvasható szövegként jelenik meg (nem képbe
égetve).”).

**A gépi réteg a választott stackben gyengébb, mint korábban feltételeztük — ezt ki kell
mondani:**

| Ág | Gépi provenance | Állapot |
|---|---|---|
| **Hang (ElevenLabs)** | hallhatatlan hangvízjel; **C2PA a beszéd-kimeneten nincs**; robusztussági leírás nincs publikálva; a lefedettséget a szolgáltató nem nyilvánította befejezettnek | **nem ellenőrizhető, és nem is csatolható** |
| **Beszélőfej (HeyGen)** | a szolgáltató egy szabványügyi kezdeményezésben való **tagságot** említ, de sehol nem állítja, hogy Content Credentials kerülne a kimenetbe | **egyetlen próbarendereléssel eldönthető** |
| **Karakter-jelenet (Veo)** | SynthID + C2PA | dokumentált |

**Következmény:** az R1 „az export ne távolítsa el” kikötése a **hang** oldalán nem
értelmezhető — nincs mit megőrizni —, a beszélőfejnél pedig egyelőre nem tudjuk, van-e.
**Ez nem gyengíti az R1-et:** a tanulónak látható címke változatlanul kötelező minden
AI-eredetű asseten, és a projektszabály attól él, hogy mi írjuk elő, nem attól, hogy a
szolgáltató technikailag támogatja.

> **Tárgyi tény, nem jogi következtetés:** az EU AI Act 50. cikkének átláthatósági
> rendelkezései főszabály szerint **2026. augusztus 2-tól** alkalmazandók. A
> **2026/1744 rendelettel beiktatott 111. cikk (4)** ugyanakkor a 2026. augusztus 2.
> előtt forgalomba hozott, szintetikus audio-/kép-/videó-/szövegtartalmat generáló
> rendszerek szolgáltatóinak az 50. cikk (2) szerinti megfelelésre **2026. december
> 2-ig** átmeneti időt ad. Hogy az 50. cikkből a szervezetre mint deployerre pontosan
> mi hárul, azt az R1 szövege szerint **jogi review** minősíti — ez a lap nem
> értelmezi tovább.

---

## 9. Akadálymentesítés

Forrás: `LMS – hozzáférhetőségi sztenderd.md`. Ezek **elfogadási feltételek**, nem
utólagos ellenőrzés.

| Követelmény | Mire vonatkozik |
|---|---|
| Felirat kötelező szinkronizált videóhoz (SC 1.2.2); a leirat **nem helyettesíti** | a 27 videó **23 feliratsávja**: az `M4.1-VID-03/04/05` jelenetek felirata az `M4.1-VID-02` konténeré, a néma `M1.1-VID-02` B-rollé pedig az alatta futó narrációé |
| A videó **képi sávját videónként külön** kell besorolni (projektgazdai döntés, 2026-10-02; utólagos ellenőrzés (vétó/QA): a hozzáférhetőségi felelős és a médiafelelős): a beszélő fej képi sávja lehet dekoratív, ha minden információ benne van a hangban és a leiratban; jelenetvideónál, ahol arckifejezés, gesztus vagy képi történés hordoz jelentést, szöveges alternatíva vagy hangalámondásos képleírás kell | minden videó, egyenként |
| Csak hang → teljes szöveges átirat elég (SC 1.2.1) | 90 narráció |
| Alt-szöveg minden beágyazott vizuális elemhez | ikon, diagram, illusztráció, fotó |
| Szövegkontraszt ≥ 4,5:1 (nagy szöveg 3:1); jelentéshordozó grafikai elem ≥ 3:1 | minden vizuál |
| **A szín soha nem egyedüli információhordozó** | minden szemantikus jelölés |
| Nyomtathatóság fekete-fehérben | minden nyomtatvány |
| Eszköz- és adat-méltányosság: alacsony adatigényű, offline letölthető változat | videós/adatigényes leckék |
| A narráció **nem hordozhat kizárólag hangban elérhető információt** | minden narráció |

A mért paletta-kontrasztok miatt (2. szakasz) a „szín nem egyedüli hordozó” szabály ebben
a rendszerben **konstrukciós kényszer**, nem óvintézkedés.

---

## 10. Jogi bizonyíték

Teljes nyilvántartás: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md).

**Az R2 nem zárul le ettől a kutatástól.** A nyilvános szolgáltatási feltétel nem azonos
a produkciós fiók bizonyítékával. Ami a kutatás után is hiányzik:

- a **ténylegesen használt** fiók és csomag licencszövege;
- a magyar szájszinkron és a felirat-export igazolása (csak élő fiókból);
- a **magyar szájszinkron** minősége (a beszélőfej-szolgáltató saját TTS-e nem játszik
  szerepet, mert a hangot feltöltjük — a szájszinkron minősége viszont csak
  próbarendereléssel dönthető el);
- a **hang-jogosultság**: ha a kiválasztott hang valós személy klónja, a szolgáltató
  önbevalláson túl semmilyen bizonyíték-formát nem ír elő — a szervezetnek kell
  eldöntenie, mit tart és milyen formában;
- **két emberi kapu**: a Google 18 év alatti hozzáférési záradékának olvasata (J1), és
  az, hogy a beszélőfej/karakter felnőttnek kell hogy látsszon, miközben a madrich maga
  is lehet kiskorú (J2).

A J2 **nem produkciós kérdés**, és ez a lap nem dönti el. A J1 és a J2 — a hangoldali V1-gyel
és V3-mal együtt — a `HUM-MEDIA-02` alkapuja; felelős és bizonyíték:
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.5.

---

## 11. Nyitott felhasználói döntések

Egyik sem zárul le ezzel a lappal. A teljes kérdésszöveg és hatásszám:
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md). A D1, a D5 és a D10 2026-10-02-án
projektgazdai döntéssel lezárult; a sorukat nyomon követhetőségért hagytuk itt.

| # | Döntés | Mit szabadít fel | Ajánlás |
|---|---|---|---|
| **D1** | vizuális rendszer: átvesszük-e a hivatalos palettát, és A vagy B változat | 245 asset / 484 deliverable | **LEZÁRVA** — projektgazdai döntés (2026-10-02): a hivatalos paletta, **B változat**; utólagos ellenőrzés (vétó/QA): a kreatív/márkafelelős |
| **D2** | **melyik ElevenLabs egyedi hang** a kanonikus narrátor: a VOICE-SRC-01 vagy a VOICE-SRC-02 forrás-beszélőből készülő | önmagában 0 — mind a 117 R3-tételen az R2 is ül | **nincs ajánlás — előbb a két hang létrehozása (V2 bizonyítékkal, bekapcsolt tanítási kimaradással), majd meghallgatás**; a szolgáltató és a modell javaslata megvan |
| **D3** | a videó-stack **jogi bizonyítéka** | önmagában 0; R2 + R3 együtt 109 asset / 344 deliverable | a beszélőfej-szolgáltató **eldőlt (HeyGen)**; karakter-jelenet: Veo 3.1 GA — **jogi review után** |
| **D5** | M3 gyermekvédelmi lépéstérkép poszter | 1 asset | **LEZÁRVA** — projektgazdai döntés (2026-10-02): az ötlépéses jelzési út (`HUM-SAFE-01`) az egyetlen kánon, a hub-poszter az `M3.B-MUNK-01` újrahasznosítása; utólagos ellenőrzés (vétó/QA): a Memuna és a helyettese |
| **D8** | az R8 státusza: szabály vagy önálló kapu | 0 | **NYITVA** — a felvételek adatkezeléséről projektgazdai döntés van (2026-10-02, `HUM-PRIV-02`: alapértelmezésben nincs felvétel; jogalap a külön, önkéntes hozzájárulás; megőrzés legfeljebb 90 nap); az R8 státuszáról (A vagy B) a döntés nem szól |
| **D10** | ken alkohol- és dohányzási kódex | 2 asset | **LEZÁRVA** — projektgazdai döntés (2026-10-02): a `HUM-SAFE-04` szabálya (kiskorúaknak szóló programon nulla alkohol, dohány, vape és nikotin); utólagos ellenőrzés (vétó/QA): a szervezeti vezetés és a Memuna. A két asset állapota a lecke `decision` mezőjét követi |
| **D11** | az `M1.3-VID-01` párbeszéde: dialógushangok és szájszinkronos gyártási út (rokon eset: az `M4.1-VID-04/05` megszólalása) | önmagában 0 — R2, R3 és R5 is ül rajta | **NYITVA** — a néma generálás erre nem alkalmazható (5. szakasz); a projektgazdai döntés (2026-10-02) szerint a hangjogosultsági bizonyítékig (`HUM-MEDIA-02`) blokkolt |
| **J1** | a karakter-jelenet szolgáltatójának 18 év alatti hozzáférési záradéka | a karakter-jelenet stack sorsa | **jogi jóváhagyó** — a `HUM-MEDIA-02` alkapuja; felelős és bizonyíték: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.5. |
| **J2** | a beszélőfej/karakter **felnőtt megjelenése** ↔ a madrich maga is lehet kiskorú | a beszélőfej- és karakter-brief | **Memuna (gyermekvédelmi felelős) + szerző** — a `HUM-MEDIA-02` alkapuja; `RIGHTS-EVIDENCE.md` 1/A.5. |
| **J3** | *(új, 2026-08-28)* a beszélőfej-szolgáltató **visszavonhatatlan, továbbadható tanítási licencet** kér a feltöltött tartalomra — és épp a **klónozott hang** mesterét töltenénk fel | a beszélőfej-lánc élesítése | **jogi jóváhagyó + a hang jogosultja** |
| **V1** | *(átkeretezve)* a választott hang-szolgáltató **nem ír elő** közlési kötelezettséget előre renderelt narrációra. Az R1-címke ettől **projektszabály marad**. Ami nyitva van: kell-e kiskorú tanulóknál külön **szülői** tájékoztatás — ez a tananyag kérdése, nem a szolgáltatóé | a hang-stack élesítése | **Memuna (gyermekvédelmi felelős) + DPO** — a `HUM-MEDIA-02` alkapuja; `RIGHTS-EVIDENCE.md` 1/A.5. |
| **V2** | *(új)* a **hang-jogosultság bizonyítéka**: a szolgáltató önbevalláson túl semmilyen formát nem ír elő | a kanonikus hang használhatósága | **jogi jóváhagyó + a hang jogosultja** |
| **V3** | *(új)* a hang-szolgáltató saját dokumentumai **nem mondanak ugyanazt** a 18 év alattiakról | fiókhasználat | **Memuna (gyermekvédelmi felelős)**; az E-8 jogi kérdésében a **jogi jóváhagyó** — az E-8 jogi felülvizsgálata külön lezárási feltétel; a `HUM-MEDIA-02` alkapuja; `RIGHTS-EVIDENCE.md` 1/A.5. |
| **V4** | *(új, üzemeltetési)* a **tanítási kimaradást előre** kell bekapcsolni — visszamenőleg nem hat | minden feltöltés előtt, minden fiókban, ahová felvétel kerül | **a fiók gazdája** — PVC-nél a forrás-beszélő is, mert a hang az ő fiókjában jön létre (`HUM-MEDIA-02`) |

---

## 12. Tartalék-stratégia

Minden ágnak van kifutása, hogy egyetlen elutasított döntés se állítsa meg a gyártást.

| Ha ez bukik… | …akkor |
|---|---|
| A Myriad Pro beágyazási licence nem igazolható | a **B változat** eleve nyílt licencű betűtípust használ — 2026-10-02 óta ez az elfogadott változat (D1), a kockázat így a tananyagot nem érinti |
| A hivatalos paletta nem hagyható jóvá | *(tárgytalan: a projektgazda 2026-10-02-án elfogadta a hivatalos palettát — D1.)* Korábban: a 26 kizárólag fekete-fehér nyomtatvány a stílus-token birtokában is indulhatott volna |
| Ha a két elkészült hang egyike sem felel meg a meghallgatáson | a szolgáltatón belül marad a megoldás: új egyedi hang készítése vagy — jogi jóváhagyás után — tervezett (szintetikus) hang; **a szolgáltatóváltás nincs napirenden** |
| A javasolt modell kiejtése alias-szabállyal sem javítható | `eleven_v3` — cserébe elveszik a tempó-vezérlés, a similarity- és speaker-boost-rögzítés, és duplázódik a költség |
| A hang-jogosultság nem dokumentálható | a **tervezett (szintetikus) hang** útja — **csak jogi jóváhagyás után**: nincs azonosított természetes személy, akinek a hangját klónoznánk, de a bizonyíték-nyilvántartás ezt `LEGAL_REVIEW_REQUIRED` állapotban tartja, és nem mondja ki, hogy nincs jogi kérdés ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.0.) |
| A beszélőfej magyar szájszinkronja gyenge | a szolgáltató másik avatar-osztálya vagy motorja — **a szolgáltató a felhasználó döntése, és marad** |
| A beszélőfej-moderáció elutasítja a tartalmat | egyedi avatar (a szabályzat az érzékeny oktatási tartalmat ehhez köti) — csak nagykorú személyről, kifejezett hozzájárulással, jogi/adatvédelmi és gyermekvédelmi felülvizsgálattal (`HUM-MEDIA-03`, R2-3, J2) —, vagy a HOOK szövegének szerzői újrakeretezése. Gyermekvédelmi és krízis-HOOK-ban a projektgazdai döntés (2026-10-02, `HUM-MEDIA-03`) szerint eleve hangalámondás + tipográfia/grafika készül, készlet-AI-beszélőfej nem |
| **A feltöltési tanítási licenc nem vállalható (J3)** | a hangot nem töltjük fel: a beszélőfej **a szolgáltató saját hangjával** készül, és a kész videó hangsávját utómunkában cseréljük az ElevenLabs mesterre. **Ára:** a szájszinkron ekkor idegen hangra készül, tehát az illeszkedés romlik — a pilotnak ezt is meg kell mérnie, ha erre az ágra kerül sor |
| A hangmestert a beszélőfej-szolgáltató újrakódolja | ha hallható romlás nincs, elfogadható; ha van, a hangsáv utómunkában cserélhető a mesterre — a kép marad |
| A Google 18 év alatti záradéka kizáró (J1) | **Runway Gen-4.5** — kereskedelmi használat szintkorlát nélkül, C2PA; ára, hogy a szolgáltató a bemeneten és a kimeneten tanít. **Csak a videót cseréli:** a karakter-lock képgenerátora (`gemini-3-pro-image`) is Google-szolgáltatás, a képi lépésre ez a sor nem ad tartalékot — az a J1 jogi jóváhagyójának döntéséig nyitott |
| A karakter-azonosság egyik eszközzel sem tartható | a jelenetek **statikus illusztráció-párrá** egyszerűsíthetők — de ez a lecke tartalmát érinti, tehát **szerzői döntés**, nem produkciós |
| Bármelyik AI-videó ág elbukik | a 21 beszélőfej **narráció + statikus illusztráció** formára váltható — szintén **szerzői döntés**, mert a HOOK-formátumot érinti (vö. a lezárt D4). A gyermekvédelmi és krízis-HOOK-oknál a projektgazdai döntés (`HUM-MEDIA-03`) már ehhez hasonló utat jelöl ki: hangalámondás + tipográfia/grafika |

> Az utolsó két sor szándékosan nem produkciós javaslat: a tananyag formátumát érintik,
> és a lezárt D4 döntés mintája szerint **szerzői hatáskörbe** tartoznak.
