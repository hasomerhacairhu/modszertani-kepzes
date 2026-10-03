# 🎧 ElevenLabs hangválasztás — végrehajtható meghallgatási teszt

> **2026-10-03 — a hangválasztás eldőlt, ez a lap történeti.** A projektgazda döntése szerint
> (VO 2. fázis) mindkét ElevenLabs-hang — a kanonikus narrátorhang és a második hang — létezik, a hanghasználati jog
> tisztázott, a hang tulajdonosai kifejezetten hozzájárultak (VO D-01). Az elsődleges
> narrátor a **kanonikus narrátorhang**; a második hang jogtisztázott, és az első gyártási körben csak
> az `M1.3-VID-01` Madrih B szerepét mondja, a kalibrálása után (VO D-14; K4). A hatmintás összehasonlítás ezért nem fut. A hatályos gyártási
> konfiguráció a [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 12. szakaszában áll; az alábbi 2.
> szakasz ehhez igazodik. A P1–P3 szkript a pilotban a fülre hozott (B4) kiejtési döntéseket
> ellenőrzi produkciós környezetben, nem dönt újra (VO D-13).

Egyetlen célja van: eldönteni, hogy a **VOICE-SRC-01** vagy a **VOICE-SRC-02** legyen a
tananyag **kanonikus narrátora**.

| | |
|---|---|
| **Szolgáltató** | **ElevenLabs** — felhasználói döntés, 2026-08-28, lezárva |
| **Jelöltek** | **VOICE-SRC-01** · **VOICE-SRC-02** — forrás-beszélők. A két ElevenLabs-hang (a kanonikus narrátorhang és a második hang) 2026-10-03-án létezik (VO D-01); hogy melyik melyik álnévhez tartozik, a repó nem rögzíti |
| **Eldöntendő** | melyik a kanonikus narrátor |
| **Minta** | **6 db** — 2 hang × 3 meglévő tananyag-szkript |
| **Mért méret** | **3 208 karakter** összesen |
| **Becsült költség** | **0,16 – 0,64 $** (`eleven_flash_v2_5`) — a szolgáltató két árazási felülete eltérő szorzót ad; mindkét olvasatban **egy dollár alatt** |
| **Állapot** | ✅ **nem fut — a kanonikus hang eldőlt** (VO D-14). A P1–P3 szkript a pilotban a kanonikus narrátorhanggal, a produkciós konfigurációval ellenőrző szerepben fut ([`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md); VO D-13) |

Kapcsolódó: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 12–13. szakasz (a kutatás és a
modell-javaslat) · [`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md) (a három szkript
szó szerinti szövege és indoklása) · [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md)
D2.

---

## 1. Amit a teszt előtt tudni KELL — három blokkoló lépés

A hat mintát **nem szabad** legenerálni, amíg ez a három nem történt meg.

**Sorrend a feltöltés körül:** hozzájárulás-bizonyíték és a forrás-beszélő nagykorúsága
(1.0.) → tanítási kimaradás (1.2.) → a hangok létrehozása (1.0.) → azonosítás (1.1.). Az
1.2. tehát a számozása ellenére **a létrehozás előtt** jön (6. szakasz).

### 1.0. A hangok létrehozása — `A HANGOK LÉTEZNEK (2026-10-03)`

**VOICE-SRC-01** és **VOICE-SRC-02** **forrás-beszélők**. A két ElevenLabs-hang (a kanonikus narrátorhang és a második hang)
2026-10-03-án létezik (VO D-01); a voice-ID nem nyilvános, csak a VO QA-repó gyártási konfigurációjában él (K3). Az alábbi pontok a
létrehozás előtti követelményeket rögzítik; hogy ezek a két hangnál hogyan teljesültek, azt csak
valós bizonyíték rögzítheti ([`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) R2-5 — formális
bizonyíték függő).

- **A létrehozás módja nyitott** (Instant Voice Clone / Professional Voice Clone / egyéb):
  a jog- és hozzájárulás-helyzet, valamint a fiók-/csomagkeret dönti el —
  a következményeket típusra bontva a [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) rögzíti.
  Ez a lap **nem dönti el**.
- **Hozzájárulás-bizonyíték (V2) a feltöltés ELŐTT:** valós személy hangfelvétele csak
  dokumentált hozzájárulással tölthető fel. A hozzájárulás maga a korlátozott hozzáférésű
  jogosultsági nyilvántartásba tartozik, nem a repositoryba; a
  [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) csak a létezését és egy nem személyes
  hivatkozást rögzít (projektgazdai döntés, `HUM-MEDIA-02`, 2026-10-02: a nyilvántartás a
  `VOICE-RIGHTS-REGISTER`, a kötelező mezőkkel együtt a
  [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) elején leírva).
- **Kiskorú hangja nem tölthető fel:** a feltöltés előtt ellenőrizni kell, hogy a
  forrás-beszélő nagykorú. A szolgáltató feltételei szerint 18 év alatt a szolgáltatás nem
  használható, és kiskorú hangjának klónozása tiltott ([`VOICE-BIBLE.md`](./VOICE-BIBLE.md)
  13.10., V3; [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) E-8). A nagykorúság
  ellenőrzését a `VOICE-RIGHTS-REGISTER` rögzíti (igen/nem, dátum, az ellenőrző szerepe; életkor,
  születési dátum és igazolvány-adat nélkül — kiegészítő projektgazdai döntés, 2026-10-03, K6); a
  projektgazda tényközlése szerint a két forrás-beszélő nagykorú (K5). A nyilvántartási bejegyzés és a jóváhagyói
  minősítés bizonyíték-kapu (VO D-08); életkor vagy születési dátum a repóba nem kerül. Hogy a
  nagykorúság igazolása a V2 hozzájárulás része-e, nyitott.
- **Összevethetőség:** a tesztnek csak akkor van értelme, ha a két hang **azonos módszerrel**
  és feltételekkel készül el — különben a különbség nem a hangot, hanem a létrehozási
  módot mérné.

### 1.1. A hangok azonosítása — `FIÓKBIZONYÍTÉKBÓL RÖGZÍTENDŐ`

A hangok léteznek (2026-10-03, VO D-01). Ebben a repositoryban **nincs ElevenLabs hitelesítő
adat**; a voice-ID a kurzusrepóba nem kerül (a VO QA-repó gyártási konfigurációjában él, K3), a hangtípust csak fiókbizonyítékból lehet rögzíteni —
**kitalálni nem szabad.**

| Hang | Voice ID | Hangtípus | Magyar nyelvre igazolt? | Modell-kompatibilitás |
|---|---|---|---|---|
| **Kanonikus narrátorhang** | `NEM A REPÓBAN` | `FIÓKBIZONYÍTÉKBÓL RÖGZÍTENDŐ` | `FIÓKBIZONYÍTÉKBÓL RÖGZÍTENDŐ` | a gyártási próbák `eleven_v4`-en futottak (VO 2. fázis) |
| **Második hang** | `NEM A REPÓBAN` | `FIÓKBIZONYÍTÉKBÓL RÖGZÍTENDŐ` | `FIÓKBIZONYÍTÉKBÓL RÖGZÍTENDŐ` | kalibrálandó: az első körben az `M1.3-VID-01` Madrih B szerepét mondja (VO D-14, K4) |

**A kinyerés menete a létrehozás után — a webes út elég:**

1. **My Voices** (`elevenlabs.io/app/voice-lab`).
2. A név melletti **típusikon** adja a hangtípust:
   **sárga pipa** = Professional Voice Clone · **fekete pipa** = Studio Quality PVC ·
   **villám** = Instant Voice Clone · **nincs ikon** = Voice Design.
3. Ugyanabban a sorban látszik, **milyen nyelvre tanították** — ellenőrizd, hogy magyar.
4. Három pont → **Copy voice ID**.
5. PVC-nél: **View**, majd a modellnevek fölé húzva látszik, melyikre van betanítva.

**Vagy hitelesített, csak olvasó API-hívásokkal** (nem generál, nem költ):
`GET /v2/voices?search=…&voice_type=personal` → `GET /v1/voices/{voice_id}` →
`GET /v1/voices/{voice_id}/settings` → `GET /v1/models`.
A rögzítendő mezők listája: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.4.

> **Miért blokkoló:** ha bármelyik hang **PVC**, az `eleven_v3` gyakorlatilag kiesik (a PVC
> a szolgáltató szerint nem arra tanul, és „not fully optimized for Eleven v3”), és a
> modellkérdés magától eldől. A típus ismerete nélkül a teszt rossz modellen futna.

### 1.2. A tanítási kimaradás bekapcsolása

A szolgáltató feltételei szerint a tanítási kimaradás **csak előremutató**: „does not
affect any uses… prior to that date”. Ezért a fiók *Data use* beállításában **már a
forrásfelvételek feltöltése — tehát a hangok létrehozása — előtt** ki kell kapcsolni a
tanítási felhasználást, nem utólag.

A kimaradás fiókhoz kötött: **minden fiókban** be kell kapcsolni, ahová forrásfelvétel
kerül — PVC-nél a forrás-beszélő saját fiókjában is, mert a hangot ott ő hozza létre
(`HUM-MEDIA-02`). A szolgáltató szerint a kimaradás csak **a kérés feldolgozása után** hat
(„once the request has been processed by our team” — EGT-s feltételek 4(i), lekérdezve
2026-10-02), ezért a feltöltés csak ezután jöhet; hogy a feldolgozás a fiókban hogyan
ellenőrizhető, élő fiókból derül ki.

A feltöltött felvételekre adott licencet a szolgáltató „perpetual and irrevocable”
licencként írja le; hogy ebből mit érint a kimaradás, jogi kérdés —
[`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) E-9.

---

## 2. A beállítások — a produkciós konfiguráció (2026-10-03)

| Paraméter | Érték | Miért |
|---|---|---|
| `model_id` | **`eleven_v4`** | projektgazdai döntés, 2026-10-03 (VO D-02); a fülre hozott kiejtési döntések ezen születtek |
| `language_code` | **`"hu"`** | ez kényszeríti a magyar olvasatot; enélkül a someres szavak angol vagy héber fonetikát kaphatnak |
| `voice_settings.stability` | **0,35** | a tesztelt konfiguráció (VO D-02) |
| `voice_settings.similarity_boost` | **0,75** | a tesztelt konfiguráció (VO D-02) |
| `style`, `use_speaker_boost`, `speed` | **nem küldjük** | a v4-en nincs ilyen vezérlés (VO D-02); a tempót a szöveg és az időkeret adja |
| `seed` | **rögzített egész** (a gyártási konfigurációban 260930) | az ingadozás ne keveredjen a valódi különbséggel |
| `pronunciation_dictionary_locators` | **a kanonikus szótár rögzített verziója** (`ulYxuUbd8aSRJ89Pv2Q8` / `VFpQiiOF789b08uzsooM`) | szótár nélküli futás nincs (VO D-03) |
| `output_format` | **`pcm_48000`** → 48 kHz / 16 bit / mono WAV | valódi API-mester, nincs átmintavételezés (VO D-12) |
| `use_pvc_as_ivc` | **explicit `false`**, ha a hang PVC | különben nem tudni, melyik renderelés szólalt meg |
| `apply_text_normalization` | **`auto`**, plusz a hang bemenetének (tts_text) célzott, naplózott cseréi | VO D-09 — mérve: az `off` az „1–2” típusú tartományt elrontja, és nem jobb |

**A két hangnak minden más paramétere azonos legyen.** Amit összehasonlítunk, az a hang —
nem a beállítás.

> ⚠️ **Minden beállítást explicit el kell küldeni a kérésben.** A kérésben megadott
> beállítás felülírja a hangon tároltat, de csak arra a kérésre; ha a tároltra hagyatkozunk,
> a kimenet később csendben megváltozhat, ha valaki a felületen hozzányúl a hanghoz.

### 2.1. A szintézis bemenete — tisztított szöveg

A `@source` blokk szövege, de:

- a **nyitó és záró `„ ”`** idézőjel nélkül (az a forrásblokk határa, nem felmondandó);
- a `**…**` félkövér és a `*…*` dőlt jelölés **eltávolítva** — a v4-en nem hangsúlyjel (VO D-11);
  a sortörésen átnyúló kiemelés sem hagyhat magányos `*`-ot;
- **minden emoji eltávolítva, a közvetlenül utána álló szóközzel együtt** — a P1-ben öt
  `👉 ` áll sorkezdeten, és a szóköz elhagyása nélkül a karakterszám 904 lenne, nem 899;
- a sor eleji listajel (`- `, `* `) eltávolítva; a beszélő- és a verziócímke (`**Madrih A:**`,
  `**1. verzió – …**`) nem hangzik el, a párbeszéd beszélőnként külön szegmens (VO D-14);
- a sortörés és az üres sor **nem** szünetvezérlő: a v4 nem veszi figyelembe őket, a szünetet a
  központozás adja, a bekezdéshatáron szükség szerint az utómunka (VO D-10);
- **szögletes zárójel nem kerülhet a szövegbe**: a v4 a szögletes zárójeles *audio taget*
  előadja (mérve), tehát a zárójeles szöveg elhangzana vagy hangeffektust kapna;
- a kiejtési és normalizálási cserék (szótár-alias, a tts_text célzott cseréi) **csak a hang
  bemenetében** élnek, a feliratban és a leiratban nem (VO D-09). A kanonikus megvalósítás a
  VO QA-repó szövegkinyerője (display_text / tts_text).

**Mind a hat mintához bájtra ugyanaz a tisztított szöveg megy be.**

---

## 3. A hat minta

A három szkript a tananyag meglévő narrációja — nem tesztszöveg. A szó szerinti szöveg,
a forrás-hivatkozás és a kiválasztás indoklása:
[`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md).

| Szkript | Asset | Forrás-hash | Karakter | Szó | Lecke-időkeret | Mit mér |
|---|---|---|---:|---:|---|---|
| **P1** | `M3.1-NAR-02` | `92d86f7be3c403a5` | **899** | 136 | 60–75 mp | hosszú magyarázó ív, hangsúly, angol szakszavak, évszám |
| **P2** | `M6.2-NAR-04` | `f78f0c8b737f2434` | **434** | 71 | 40–50 mp | visszafogott érzelmi sáv, idézet, `madrih`/`hanih`/`peula` |
| **P3** | `M3.1-NAR-05` | `17184b1a6e2cf25c` | **271** | 40 | 15–20 mp (mért: 18,5 mp, kanonikus narrátorhang, 2026-10-03) | mind a három aktuális kvuca-tulajdonnév |
| | | **hangonként** | **1 604** | 247 | ≈ 2 perc | |
| | | **hat minta** | **3 208** | 494 | ≈ 4 perc | |

**A mátrix:**

| | P1 | P2 | P3 |
|---|---|---|---|
| **VOICE-SRC-01** | ☐ | ☐ | ☐ |
| **VOICE-SRC-02** | ☐ | ☐ | ☐ |

**Fájlnév a teszthez** (ideiglenes, nem produkciós asset):

```
teszt__<hang>__<szkript>__<modell>__seed<n>.<kiterjesztés>
pl.  teszt__voice-src-01__P1__flash-v2-5__seed4242.wav
```

Ezek **nem** kerülnek a `masters/` alá és nem asset-deliverable-ök — a hangválasztás
munkaanyagai.

---

## 4. Kiejtési figyelőlista

A P1–P3 a **kanonikus kiejtési szótárral** fut (VO D-03). Ez a lista mondja meg, **mit kell
figyelni**: az elvárt kiejtés a VO QA-repó B4-regiszterének fülre hozott döntése (VO D-04,
D-05, D-06, D-13), az írott alak és a felirat nem változik. Ha egy jóváhagyott szó a
produkcióban hallhatóan eltér a próbától, az regresszió, nem új döntés (VO D-23).

A kánoni írott alakok forrása a `Glosszárium – someres és pedagógiai fogalmak.md`, a hangzásé a
[`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 6–7. szakasza. **Az írásmód eldőlt** (projektgazdai
döntés, 2026-10-02): madrih, hanih, hágsámá, dugma isit, Leviatán; a tanulói korpusz migrált.

| Szó | Elvárt kiejtés | Hol | Kockázat |
|---|---|---|---|
| `kvuca`, `kvucába`, `kvucának` | „kvuca” — a **c** = /ts/ | P1, P2, P3 | angol /k/ vagy /kw/ olvasat |
| `someres` | **s** = /ʃ/ | P1, P3 | angol /s/ |
| `madrih`, `madrihhoz` | „mádrih” [maːdrix] — nem kerekített első magánhangzó, szóvégi [x] (B4) | P2 | a nyers olvasat kerekített [mɔdrix] — fülre elvetve |
| `hanih` | [xanix] — a szótár héber írású aliasa adja (B4) | P2 | a nyers olvasat lágy, kerekített „honih” — fülre elvetve |
| `peula` | „peula” | P2 | ékezet vagy hangsúly elcsúszása |
| `Parparim` | „parparim” | P3 | idegen hangsúly |
| `Kivsza` | „kivsza” | P3 | — |
| `Leviatán` | „Leviatan” [leviotɒn] — rövid a-val (B4); az írott alak és a felirat „Leviatán” | P3 | a szóvégi hosszú á nem produkciós kiejtés |
| `Tuckman` | „Takmen”; `Bruce Tuckman` → „Brúsz Takmen”, `Mary Ann Jensen` → „Méri En Dzsenszen” (B4) | P1 | a nyers angol olvasat — fülre elvetve |
| `1977-ben` | „ezerkilencszázhetvenhét-ben”, nem számjegyenként | P1 | számnormalizálás |
| `forming` / `storming` / `norming` / `performing` / `adjourning`-ot | „fórming, sztórming, nórming, perfórming, edzsörning” (B4), az utolsó magyar toldalékkal | P1 | a nyers brit olvasat és a „forrming” — fülre elvetve |
| `👉` (5×) | **nem hangzik el** | P1 | ha a tisztítás kimaradt, felolvassa |

**A narrációban ténylegesen előforduló, a próbák szerint kockázatos tételek** — a köteg-jóváhagyáskor
és a QA kiejtési regressziós próbájában külön kell ellenőrizni: `dugma isit`, `Zmán Kvucá`, `ken`
(„kenben”), `Johari`, `Memunát`, az `SBI` és az önálló `S`, `red flag`, `checklist`, `SMART`,
`AI`, `Moodle`, `energizer` („enerdzsájzer”), a `13–17` („tizenhárom–tizenhét”), a `112`
(„száztizenkettő”), az `M2.A` („em kettő pont á”), az `az ÉN` („az én”), a modul- és
leckekódok (`M2.4`), a `Peula v1/v2`, valamint a toldalékos számok (`18-tól`).

> **Ha egy szó elromlik:** az eltérés regresszió, nem új döntés (VO D-23). A javítás a kanonikus
> szótár új verziója — elsősorban alias-szabály, minden ténylegesen előforduló toldalékos alakra,
> mert a szóhatár-illesztés alapértelmezetten bekapcsolt: a `Somer` szabály nem illeszkedik a
> `someres`-re. Az IPA-fonémaszabály a v4-en működik, de az alias az elsődleges eszköz.
> Részletek: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.5.

---

## 5. Pontozólap

Mind a hat mintára külön. **1–5** skála, ahol **3 = elfogadható**, **5 = kiváló**.

| # | Szempont | SRC-01 P1 | SRC-01 P2 | SRC-01 P3 | SRC-02 P1 | SRC-02 P2 | SRC-02 P3 |
|---|---|---|---|---|---|---|---|
| 1 | Magyar természetesség | | | | | | |
| 2 | Kiejtés általában | | | | | | |
| 3 | **Someres/héber szavak** | | | | | | |
| 4 | Mondatritmus | | | | | | |
| 5 | Hangsúlyozás | | | | | | |
| 6 | Melegség | | | | | | |
| 7 | Tekintély / hitelesség | | | | | | |
| 8 | Illik-e 15+ közönséghez | | | | | | |
| 9 | **Mentes-e a „reklámhang”-tól** | | | | | | |
| 10 | Hosszútávú fárasztóság (5 = nem fáraszt) | | | | | | |
| 11 | Konzisztencia a három minta között | | | | | | |
| 12 | Érthetőség normál lejátszási sebességen | | | | | | |
| 13 | Felirat-időzítésre alkalmas tagoltság | | | | | | |
| | **Összesen (max 65)** | | | | | | |

**Egy szempont, ami nem hangonként, hanem a párra vonatkozik** — és amit csak most, a hat
minta együtthallgatásakor lehet olcsón rögzíteni:

| # | Szempont | Igen / Nem + megjegyzés |
|---|---|---|
| 14 | **A két hang egymástól hallhatóan megkülönböztethető?** | |

> Miért itt: az `M1.3-VID-01` kétszereplős jelenete a hang-bible 8. szakasza szerint
> **két megkülönböztethető hangot** igényel, „hogy a felirat nélkül is követhető legyen,
> ki beszél”. A tervben pontosan két hang szerepel (a két forrás-beszélőből készülő). Ez az egyetlen tervezett
> alkalom, amikor a kettő egymás mellett szól — **ez a sor nem dönt a második hang
> szerepéről**, csak rögzíti az adatot, amíg ingyen van. A dialógushangok kérdése és a
> jelenet gyártási útja nyitott döntés: [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) D11.

**Súlyozás, ha a két hang közel van:** a 3. (someres szavak), a 9. („nem reklámhang”) és
a 10. (fárasztóság) sor **kétszeres súlyt** kap. Ez a három dönti el, hogy egy hang
kibírja-e 117 tételen — nem az, hogy melyik szebb egyetlen mintán.

### 5.1. Azonnali bukás — bármelyik önmagában kizár egy hangot

- [ ] **B1 — Javíthatatlan kiejtés.** Egy kánoni someres szó rosszul szól, és
      alias-szabállyal sem hozható helyre. *(Például ha egy B4-ben jóváhagyott alak — madrih,
      hanih, Leviatán — a kanonikus szótárral sem a jóváhagyott hangzással szól.)*
- [ ] **B2 — Instabilitás generálások között.** Ugyanaz a szöveg, ugyanaz a seed és
      beállítás **hallhatóan más** hangot ad. Ellenőrzés: a nyertes jelölt P2-jét
      **kétszer** kell legyártani és összevetni.
- [ ] **B3 — A hang-jogosultság nem dokumentálható.** Ha a hang valós személy klónja, és
      a szervezet nem tud érvényes hozzájárulást felmutatni, a hang nem használható —
      **függetlenül attól, milyen jól szól.**

> A B3 nem hangminőségi kérdés, mégis ide tartozik: a legjobb hang is kiesik nélküle.
> A bizonyíték-nyilvántartás helye: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md).

---

## 6. A döntés menete

```
0.  hozzájárulás-bizonyíték (V2)      → RIGHTS-EVIDENCE.md; feltöltés előtt kötelező;
                                        a forrás-beszélő nagykorú (1.0.)
0a. tanítási kimaradás bekapcsolva    → (1.2.) — a feltöltés ELŐTT, minden fiókban,
                                        ahová felvétel kerül (PVC-nél a beszélőében
                                        is), és a kérést a szolgáltató feldolgozta
0b. a két hang létrehozása (1.0.)     → azonos módszerrel; a módszer (IVC/PVC/egyéb)
                                        jog + csomag függvénye — még nyitott
1.  hangok azonosítása (1.1.)         → voice ID + típus rögzítve
2.  ha bármelyik hang PVC             → a modell flash_v2_5, a v3 kiesik
3.  hat minta legyártása              → 0,16–0,64 $
4.  meghallgatás + pontozás           → magyar anyanyelvű, someres szóhasználatot
                                        ismerő jóváhagyóval
5.  a nyertes P2-jének újragyártása   → B2 stabilitási próba
6.  hibás szavak listája              → alias-szabályok, majd újrahallgatás
7.  KANONIKUS HANG kiválasztva        → D2 lezárul
8.  a reprodukciós metaadat rögzítve  → az R3 lezárható
```

**A 7. lépés a felhasználó döntése.** Ez a lap előkészíti, nem helyettesíti.

*(2026-10-03: a 0b–7. lépés tárgytalan — a hangok léteznek, a kanonikus narrátorhang ki van jelölve, a modell
az `eleven_v4` (VO D-01, D-02, D-14). A 8. lépés reprodukciós metaadatát a 6.1. sorolja fel.)*

### 6.1. Mit kell rögzíteni, amikor a döntés megszületik

Ezek nélkül az R3 **nem** zárható le, mert a felvétel nem reprodukálható:

`voice_id` · `voice_display_name` · `voice_type` (`category`) · `model_id` ·
`language_code` · a ténylegesen elküldött `voice_settings` (v4-en: `stability`,
`similarity_boost`) · `seed` · `output_format` · a kiejtési szótár azonosítója **és
`version_id`-je** · `use_pvc_as_ivc` · `apply_text_normalization` · a kérés azonosítója
(`request-id`) és karakterköltsége (`character-cost`) · kérés-összefűzésnél az előző kérések
azonosítói (`previous_request_ids`). A voice-ID a kísérőadatban nem nyilvános formában áll.

> **Őszinte plafon.** A szolgáltató kimondja, hogy a modellek nem determinisztikusak, és
> a seed is csak „best effort”. Egy fél év múlva újragyártott klip **hasonló lesz, nem
> bitre azonos**. Ezért a produkciós szabály: újragyártásnál mindig meghallgatás, és
> inkább a **teljes tétel** újravétele, mint egy javított mondat beillesztése.

## 7. Amit ez a teszt NEM dönt el

- **A második hang szerepét — ez eldőlt.** A második hang jogtisztázott; a kalibrálása
  után már az első körben az `M1.3-VID-01` Madrih B szerepét mondja (VO D-14, K4).
- **A csomagot.** A kimeneti formátum és a hangtípus dönti el, nem a karakterár —
  [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.7. és 13.9.
- **A hang-jogosultságot.** → [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) (R2-5; a V3
  alkapu felelőse és bizonyítéka: 1/A.5.); a V2 és a V3 kérdése:
  [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.10.
- **A kiejtési szótár tartalmát.** A kanonikus szótár a B4-regiszterből épül (VO D-03, D-13): a
  pilot bemenete, nem eredménye.
