# 🏭 Produkciós stack — döntés-előkészítés

Ez a lap egy helyen írja le, **mivel és hogyan** készülne el a 903 deliverable, ha a
nyitott döntések megszületnek. **Nem lezárás, nem jóváhagyás, és nem indít gyártást.**

| | |
|---|---|
| **Státusz** | NYITOTT — FELHASZNÁLÓI DÖNTÉS SZÜKSÉGES |
| **Mit változtat a manifeszten** | semmit. A 417 asset, a 903 deliverable és minden R2/R3/R5/R7/R8 blokkoló változatlan. |
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
| Összesen | 417 | 903 |
| Központilag előgyártható | 407 | 898 |
| **Most gyártható (nincs nyitott kapu)** | **37** | **37** |
| Élő/runtime (a képző hozza létre a peulán) | 3 | 5 |

---

## 2. Vizuális rendszer — javaslat

**Részletek és a számított kontrasztok:**
[`PRODUCTION-STYLE-TOKEN.md`](./PRODUCTION-STYLE-TOKEN.md).

Röviden: a mozgalomnak **van hivatalos arculati kézikönyve**, deklarált HEX / RGB / CMYK
/ Pantone palettával, és a hat alapszín a hivatalos logó-SVG-ből byte-azonosan
megerősíthető. A D1 kérdése ezért nem „mi legyen a paletta”, hanem „átvesszük-e”.

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

**Javasolt változat: B** — azonos márkaszínek és logóhasználat, de a tananyag-produkcióhoz
nyílt licencű betűtípus (Source Sans 3, SIL OFL 1.1; mérve: mind a **18** magyar ékezetes
glif, valamint `·`, `„`, `”`, `–`, `—`, `✓`, `☐` megvan) és egy `#1D1D1B`-ből származtatott
semleges skála. Indok: az A változat a Myriad Pro **beágyazási licencének** meg nem
válaszolt jogi kérdésétől tenné függővé 247 asset indulását.

---

## 3. Hang — javaslat

**Részletek:** [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13. szakasz. **Tesztanyag:**
[`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md).

A tananyag szempontjából egyetlen kérdés dönt: **kikényszeríthető-e a magyar someres
szavak kiejtése**, vagy csak remélhető.

| | Javaslat | Tartalék |
|---|---|---|
| **Motor** | Azure AI Speech, `hu-HU` **GA** hang | Google Cloud TTS, `hu-HU-Chirp3-HD-*` |
| **Hang** | `hu-HU-TamasNeural` vagy `hu-HU-NoemiNeural` | `hu-HU-Chirp3-HD-Charon` / `-Kore` |
| **Kiejtés-vezérlés** | verziókövetett PLS kiejtési szótár (a szótár karakterei nem számlázottak) | `custom_pronunciations`, de a szolgáltató fonéma-referenciája **nem tartalmaz magyart** |
| **Tempó** | `<prosody rate>` a 100–120 szó/perc célsávra | `speaking_rate` |
| **Reprodukálhatóság** | **12 hónapos leállítási értesítés** GA hangokra | nincs dokumentált dátumozott rögzítés |
| **Költség (3× nyers)** | ≈ 2,25–3,40 $ | 0 $ (az 1M karakter/hó ingyenes kereten belül) |

**Miért az Azure:** ez az egyetlen jelölt, amely **dokumentál magyar IPA fonéma-készletet**,
és abban benne van a `t͡s` (kvuca), a `ʃ` (Somer) és az `x` (madrich, chanich). A többi
jelöltnél a kiejtés próbálgatás vagy „80–90%-os következetesség”.

**Emberi felmondó** továbbra is érvényes alternatíva, más kockázatprofillal: indikatív
nettó sáv ≈ 255 000 – 690 000 Ft, középérték ≈ 420 000 Ft. Egyetlen figyelmeztetés:
**egy projektként kell szerződni, megadott fájlszámmal** — ugyanaz a nyilvános árlista
117 külön „spotra” bontva 51-szeres árat ad.

> **A hang nem választható ki dokumentációból.** A három pilot-szkript
> meghallgatása nélkül minden ajánlás előzetes.

---

## 4. Beszélőfej-videó — javaslat

Hatókör: **21 asset.** A hang **külön döntés (D2)**, ezért a stacknek **fel kell tudnia
tölteni külső hangsávot** — ez zárja ki a „saját hangot kitaláló” videómodelleket.

| | Javaslat | Tartalék |
|---|---|---|
| **Eszköz** | Synthesia, fizetős csomag | HeyGen API (előre feltöltött egyenleg, előfizetés nélkül) |
| **Hang-integráció** | „Voiceover Uploads” — a D2 hangját töltjük fel | „Audio-to-Video” (`audio_url` / `audio_asset_id`, MP3/WAV ≤ 32 MB) |
| **Avatar-stratégia** | **egyetlen készlet-avatar mind a 21 videóra** | ugyanaz |
| **Miért** | ez az egyetlen talált szolgáltató, amely **a megrendelőt kártalanítja** a készlet-avatar képmás- és személyiségi jogi igényeire; kimondja az EU AI Act 50. cikk szerinti jelölést; és az AUP-ja **tiltja** a provenance-jelölés eltávolítását — vagyis a projekt saját R1-szabálya bekerül a szolgáltató feltételei közé | 3–4-szer olcsóbb, a hangfeltöltés dokumentált és nincs csomaghoz kötve |
| **Korlát** | éves ≈ 216 $ alsó küszöb, **nincs nonprofit kedvezmény**; a magyar szájszinkron és a felirat-export **nem ellenőrzött** | nincs kártalanítás a felhasználó felé (fordítva van), a provenance nem ellenőrzött |
| **Költség (21 × 30 mp, 2× újragenerálás)** | ≈ 216 $/év | ≈ 21–84 $ |

**Egyetlen készlet-avatart** használunk saját avatar helyett: így nincs valós személy
képmás-hozzájárulási lánca, és a 21 videó között a persona automatikusan azonos.

---

## 5. AI karakter-jelenet — javaslat

Hatókör: **5 jelenet + 1 B-roll**, és a belőlük kivett **2 freeze-frame**.

A nehézség nem a videó, hanem a **karakter-azonosság**: az `M4.1-FOTO-01` specifikációja
szó szerint „ugyanaz a madrich karba tett kézzel vs. nyitott kézzel” — tehát a három
jelenetben ugyanannak az embernek kell látszania.

| | Javaslat | Tartalék |
|---|---|---|
| **Karakter-rögzítés** | képgenerátor karakter-referenciából (`gemini-3-pro-image`); a dokumentáció **legfeljebb 5 referenciaképet** enged a karakter-konzisztenciához; a referenciakészlet **verziókövetve** | ugyanaz |
| **Videó** | Veo 3.1 GA (`veo-3.1-generate-001`) fizetős Vertex AI-on | Runway Gen-4.5 |
| **Konzisztencia-mechanizmus** | első képkocka + **legfeljebb 3 `asset` referenciakép**; `enhancePrompt: false` mellett rögzített seed | `referenceImages` (max 3), csak az első képkockára |
| **Hang** | **`generateAudio: false`** — a videó néma készül, a D2 narrációja utómunkában kerül alá | néma generálás, majd utómunka |
| **Freeze-frame** | képkocka-kivétel a kész jelenetből (`ffmpeg`), nem külön generálás | ugyanaz |
| **Provenance** | SynthID + C2PA | C2PA |
| **Költség** | ≈ 43–144 $ (90 generálás, 3–5× selejt-aránnyal számolva) | hasonló, viszonteladói áron |

**Miért néma generálás:** egyszerre feleannyiba kerül, kizárja, hogy a modell magyar
helyett kitalált nyelvet mondjon, és **nyitva tartja a D2-t** — a hang bármikor
lecserélhető a videó újragenerálása nélkül.

> ⚠️ **Ez a javaslat jogi felülvizsgálat alatt áll.** A Google Cloud feltételei
> tartalmaznak egy 18 év alatti hozzáférésre vonatkozó záradékot, amelynek alkalmazása
> erre a felhasználásra **nem eldöntött** — lásd
> [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) 1/A.3. J1. Ha a jogi jóváhagyó ezt
> kizárónak minősíti, a tartalék stack lép életbe.

---

## 5/A. Költségmodell — durva, de forrásolt

Nyilvános, jelenlegi listaárakból. **Nem árajánlat, és nem tartalmaz áfát vagy
árfolyamkockázatot.** A bizonytalanság a szolgáltatói árnál ±30%, a selejt-aránynál
lényegesen több — a generatív videónál 3–5 próbálkozásból lesz egy használható felvétel,
és ez a becslés legingatagabb eleme.

### Szolgáltatói díj

| Köteg | Feltételezés | Alsó | Felső |
|---|---|---:|---:|
| **Hang** — Google Chirp3-HD | 150 000–225 000 karakter (3× nyers) | **0 $** | **0 $** (az 1M/hó ingyenes kereten belül) |
| **Hang** — Azure | ugyanaz, 15 $/1M karakter | **2,25 $** | **3,40 $** |
| **Hang** — ElevenLabs v3 | ugyanaz, 0,10 $/1000 karakter | **15 $** | **22,50 $** |
| **Hang** — emberi felmondó | egyetlen projektmegbízás, ~60 perc kész hang | **≈ 255 000 Ft** | **≈ 690 000 Ft** (nettó) |
| **Beszélőfej** — HeyGen API | 21 × 30 mp + 2× újragenerálás = 1260 mp | **21 $** | **84 $** |
| **Beszélőfej** — Synthesia | éves csomag, 120 perc/év | **216 $/év** | **216 $/év** |
| **Karakter-jelenet** — Veo 3.1, néma, 1080p | 15–18 használható 8 mp-es felvétel, 3–5× selejt → **45–90 generálás** | **36 $** | **144 $** |
| **Karakter-lock** — referenciakép-készlet | 20–40 kép | **3 $** | **6 $** |
| **Freeze-frame** | képkocka-kivétel a kész videóból | **0 $** | **0 $** |

> ⚠️ **A Veo per-másodperc díja nincs idézve, mert a szolgáltató árlapja nem volt
> lekérdezhető.** A fenti sáv 0,80–1,60 $ / 8 mp-es klip feltételezésen nyugszik (a
> gyorsabb és a teljes minőségű változat között). **Ajánlatkérés vagy az élő árlap
> ellenőrzése nélkül ez a sor tájékoztató.**

**Két összesítés, a választástól függően:**

| Útvonal | Alsó | Felső |
|---|---:|---:|
| HeyGen + Veo (API-alapú) | **≈ 70 $** | **≈ 235 $** |
| Synthesia + Veo | **≈ 260 $** | **≈ 365 $** |

Ehhez jön a hang: gyakorlatilag 0–25 $ szintetikus ágon, vagy 255 000–690 000 Ft nettó
emberi felmondóval.

> **Az előfizetés vs. kredit szerkezete megfordítja a választ.** A HeyGen API előre
> feltöltött egyenlegről megy, előfizetés nélkül — ezen a volumenen olcsóbb, mint a saját
> havidíjas csomagja. A Synthesia viszont éves perceket ad el, tehát a küszöbe **216 $
> akkor is, ha keveset használunk**, és a szolgáltató kimondja, hogy nonprofit vagy
> oktatási kedvezményt nem ad.

### Emberi munka — ez a nagyobb tétel

A szolgáltatói díj ezen a volumenen **nem a fő költség**. Ami az:

| Tevékenység | Becslés | Megjegyzés |
|---|---|---|
| Pilot-kör családonként (gyártás + 4 review + javítás) | 9 pilot × 2–5 óra | a 13. szakasz jóváhagyási lánca a [`PILOT-PRODUCTION-PACK.md`](./PILOT-PRODUCTION-PACK.md)-ben |
| Determinisztikus forrás megírása (SVG / HTML) | a 247 vizuális tétel érdemi része | egyszeri sablon után tételenként rövidül |
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
| Narráció | ▫️ WAV (48 kHz / 16 bit / mono) | ✅ MP3 (H5P Course Presentation), szükség szerint AAC | „tiszta beszéd, háttérzaj nélkül”; egy asset = egy fájl |
| Videó | ✅ 16:9 · ▫️ MP4 / H.264, 1920 × 1080 | ugyanaz + `.vtt` felirat | égetett felirat nincs |
| Felirat | `.vtt` | — | WCAG 2.2 SC 1.2.2 |
| Leirat | Markdown → a H5P slide-jegyzetbe | — | SC 1.2.1 |
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

A javasolt stackek mindegyike ad gépi jelölést (Synthesia: EU AI Act-jelölés fizetős
szinten; Veo: SynthID + C2PA; Runway: C2PA), és a Synthesia AUP-ja **kifejezetten
tiltja** az eltávolítását.

> **Tárgyi tény, nem jogi következtetés:** az EU AI Act 50. cikkének átláthatósági
> rendelkezései a hivatalos uniós tájékoztatás szerint **2026. augusztus 2-tól**
> alkalmazandók. Hogy ebből a szervezetre mint deployerre pontosan mi hárul, azt az R1
> szövege szerint **jogi review** minősíti — ez a lap nem értelmezi tovább.

---

## 9. Akadálymentesítés

Forrás: `LMS – hozzáférhetőségi sztenderd.md`. Ezek **elfogadási feltételek**, nem
utólagos ellenőrzés.

| Követelmény | Mire vonatkozik |
|---|---|
| Felirat kötelező szinkronizált videóhoz (SC 1.2.2); a leirat **nem helyettesíti** | mind a 27 videó |
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
- a Synthesia/HeyGen magyar nyelvi támogatásának megerősítése;
- az Azure és a Google **kimenet-tulajdonlási** záradéka a hang oldalán;
- **két emberi kapu**: a Google 18 év alatti hozzáférési záradékának olvasata (J1), és
  az, hogy a beszélőfej/karakter felnőttnek kell hogy látsszon, miközben a madrich maga
  is lehet kiskorú (J2).

A J2 **nem produkciós kérdés**, és ez a lap nem dönti el.

---

## 11. Nyitott felhasználói döntések

Egyik sem zárul le ezzel a lappal. A teljes kérdésszöveg és hatásszám:
[`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md).

| # | Döntés | Mit szabadít fel | Ajánlás |
|---|---|---|---|
| **D1** | vizuális rendszer: átvesszük-e a hivatalos palettát, és A vagy B változat | 247 asset / 489 deliverable | átvenni; **B változat** |
| **D2** | narrátor: szintetikus vagy emberi; melyik motor és hang | 90 asset / 267 deliverable | Azure GA `hu-HU` hang, PLS szótárral — **meghallgatás után** |
| **D3** | AI-videó stack és a jogi bizonyíték | önmagában 0; R2 + R3 együtt 111 asset / 351 deliverable | beszélőfej: Synthesia; karakter-jelenet: Veo 3.1 GA — **jogi review után** |
| **D5** | M3 gyermekvédelmi lépés-térkép poszter | 1 asset | **NYITVA — nem ennek a passznak a hatásköre** |
| **D8** | az R8 státusza: szabály vagy önálló kapu | 0 | **NYITVA — nem ennek a passznak a hatásköre** |
| **D10** | ken alkohol- és dohányzási kódex | 2 asset | **NYITVA — nem ennek a passznak a hatásköre** |
| **J1** | a Google 18 év alatti hozzáférési záradékának olvasata | a karakter-jelenet stack sorsa | **jogi jóváhagyó** |
| **J2** | a beszélőfej/karakter felnőtt megjelenése ↔ a madrich lehet kiskorú | a beszélőfej- és karakter-brief | **gyermekvédelmi felelős + szerző** |
| **V1** | a szintetikus hang tényének közlése kiskorúakat érintő felhasználásnál | a hang-stack élesítése | **gyermekvédelmi felelős + DPO** |

---

## 12. Tartalék-stratégia

Minden ágnak van kifutása, hogy egyetlen elutasított döntés se állítsa meg a gyártást.

| Ha ez bukik… | …akkor |
|---|---|
| A Myriad Pro beágyazási licence nem igazolható | a **B változat** eleve nyílt licencű betűtípust használ — ez a tartalék maga |
| A hivatalos paletta nem hagyható jóvá | a 26 kizárólag fekete-fehér nyomtatvány a stílus-token birtokában is indulhat (a manifeszt R5-blokkolója viszont csak a teljes R5-zárással kerül le róluk) |
| Az Azure magyar hangja meghallgatáson megbukik | Google `hu-HU-Chirp3-HD-*` (30 GA hang, ezen a volumenen ingyenes), majd ElevenLabs |
| A szintetikus hang gyermekvédelmi okból nem vállalható (V1) | **emberi felmondó**, egyetlen projektszerződéssel |
| A Synthesia magyar szájszinkronja gyenge, vagy nincs felirat-export | HeyGen API (a hangfeltöltés dokumentált) |
| A Google 18 év alatti záradéka kizáró (J1) | **Runway Gen-4.5** — kereskedelmi használat szintkorlát nélkül, C2PA; ára, hogy a szolgáltató a bemeneten és a kimeneten tanít |
| A karakter-azonosság egyik eszközzel sem tartható | a jelenetek **statikus illusztráció-párrá** egyszerűsíthetők — de ez a lecke tartalmát érinti, tehát **szerzői döntés**, nem produkciós |
| Bármelyik AI-videó ág elbukik | a 21 beszélőfej **narráció + statikus illusztráció** formára váltható — szintén **szerzői döntés**, mert a HOOK-formátumot érinti (vö. a lezárt D4) |

> Az utolsó két sor szándékosan nem produkciós javaslat: a tananyag formátumát érintik,
> és a lezárt D4 döntés mintája szerint **szerzői hatáskörbe** tartoznak.
