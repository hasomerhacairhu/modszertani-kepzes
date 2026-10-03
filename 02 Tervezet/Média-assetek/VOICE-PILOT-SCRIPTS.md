# 🎧 Hang-pilot szkriptek — a kanonikus hang pilotszkriptjei (P1–P3)

Ez a lap **három meglévő narrációt** jelöl ki a tananyagból, amelyeken a kanonikus narrátorhang a
fülre hozott kiejtési döntéseket produkciós környezetben ellenőrzi (P1–P3; VO D-13). A szövegek **másolatok, nem kánon**: a kánoni forrás továbbra is a
leckében álló `@source` blokk, és a felvétel mindig onnan készül.

> ⚠️ **Ez a lap nem hoz létre új narrációt, és nem írja felül a meglévőt.** Ha egy
> forrásszöveg megváltozik a leckében, ez a lap **elavul** — a `Forrás-hash` oszlop
> ezért van itt. Ellenőrzés kézzel: a `Forrás-hash` egyezzen a `_build/media-manifest.v2.json`
> megfelelő `sources[].hash` értékének első 16 karakterével — a `python3 tools/media_manifest.py check`
> ezt **nem** nézi, csak a generált kimenetek frissességét.

**Miért kell pilot:** a [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 11.2. szakasza szerint a pilot a
hangszínt, a szünetkezelést és a mért hosszt hagyja jóvá produkciós környezetben; a someres
szavak kiejtését a B4-regiszter fülre hozott döntései szerint **ellenőrzi**, nem dönti el újra
(VO D-13). A hang 89 hang-assetre és 27 videó hangsávjára hat; egy hiba 116 tételen kerül
vissza.

**Mit NEM dönt el ez a lap:** magát a hangot — az eldőlt: a narrációt a kanonikus narrátorhang mondja (projektgazdai
döntés, 2026-10-03, VO D-14). A beállítások a [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 12.
szakaszában, a kiejtési figyelőlista az
[`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md) 4. szakaszában, az elfogadási feltétel e lap 6. szakaszában áll; a tesztlap
pontozólapja a kéthangos választás idejéből való, történeti.

> ✅ **2026-08-28: a szolgáltatói kérdés lezárult.** A felmondás **szintetikus**, a motor
> az **ElevenLabs**. **2026-10-03:** mindkét hang (a kanonikus narrátorhang és a második hang) létezik, a narrációt a kanonikus
> narrátorhang mondja (VO D-01, D-14). Az itt kijelölt három szkript ezért nem hangválasztási anyag, hanem a
> kanonikus hang **produkciós ellenőrzésének** anyaga (VO D-13).

---

## 1. A három szkript és amit mérnek

| # | Asset | Forrásblokk | Szó | Lecke-időkeret | Mit tesztel elsősorban |
|---|---|---|---:|---|---|
| **P1** | `M3.1-NAR-02` | `M3.1-NAR-02-VO` | 136 | 60–75 mp | hosszú magyarázó ív, hangsúlykezelés, angol szakszavak magyar mondatban |
| **P2** | `M6.2-NAR-04` | `M6.2-NAR-04-VO` | 71 | 40–50 mp | visszafogott érzelmi sáv, párbeszéd-idézet, mozgalmi köznevek |
| **P3** | `M3.1-NAR-05` | `M3.1-NAR-05-VO` | 40 | 15–20 mp | kiejtés — mind a három aktuális kvuca-tulajdonnév egyetlen mondatban |

Együtt kb. **247 szó ≈ 2 perc** kész hang. Ennyi elég a döntéshez, és nem terheli meg a
próba-keretet.

### Mit fed le a három szkript a hang-bible 6. szakaszának kiejtési táblájából

| Lefedett | Hol |
|---|---|
| `kvuca` / `kvucá-` (c = /ts/) | P1, P2, P3 |
| `Somer` / `someres` (s = /ʃ/) | P1, P3 |
| `madrih`, `madrihhoz` („mádrih” [maːdrix], B4) | P2 |
| `hanih` ([xanix], B4) | P2 |
| `peula` | P2 |
| `Parparim`, `Kivsza`, `Leviatán` (hangja „Leviatan”, B4) | P3 |
| `Tuckman` („Takmen”, B4) | P1 |
| évszám felmondása (`1977`) | P1 |

**A narrációban ténylegesen előforduló, a próbák szerint kockázatos tételek, amelyeket a három
szkript nem fed le** — ezeket a köteg-jóváhagyáskor és a QA kiejtési regressziós próbájában kell
ellenőrizni, nem a piloton: `dugma isit`, `Zmán Kvucá`, `ken` („kenben”), `Johari`, `Memunát`,
az `SBI` és az önálló `S`, `red flag`, `checklist`, `SMART`, `AI`, `Moodle`, `energizer`, a
`13–17`, a `112`, az `M2.A`, az `az ÉN`, a modul- és leckekódok, a `Peula v1/v2` és a
toldalékos számok (`18-tól`).

---

## 2. P1 — Nyugodt magyarázó narráció

- **Asset:** `M3.1-NAR-02` — *INPUT 1 narráció – Tuckman 4+1 szakasz*
- **Forrás:** `02 Tervezet/Modulok/M3/Online leckék/M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md`, `@source` blokk `M3.1-NAR-02-VO` (deklaráció: 254. sor, törzs: 255–275. sor)
- **Forrás-hash:** `92d86f7be3c403a5`
- **Lecke-időkeret:** kb. 60–75 mp · **136 szó** → 109–136 szó/perc
- **Becslés a kanonikus narrátorhang mért tempójával (2026-10-03):** kb. 64 mp — a keretben marad, gyorsítás nélkül.

### Miért ez a reprezentatív magyarázó szkript

- A korpusz **leghosszabb egybefüggő INPUT-narrációja**. Ha egy hang egy percen át
  megtartja a figyelmet monotónia nélkül, a 20–40 mp-es többségen is meg fogja.
- **Kilenc félkövér kiemelés** van benne. A v4-en a félkövér nem hangsúlyjel (hang-bible 5.): a
  szkript azt méri, hogy a jelentést hordozó hangsúly a mondatszerkezetből ép marad-e — fülre
  (VO D-11). Ez a legsűrűbb ilyen hely a tananyagban.
- **Öt `👉` emoji** áll sorkezdeten. A hang-bible szerint az emoji **hangulatjelölő, nem
  felmondandó** — ez egyben csővezeték-teszt: a szintézis bemenetéből az emojit ki kell
  szűrni, különben a motor felolvassa vagy megbotlik rajta.
- Öt **angol szakszó** (`forming`, `storming`, `norming`, `performing`, `adjourning`)
  áll magyar mondatban, az egyik magyar toldalékkal (`adjourning`-ot). Ez a magyar TTS
  tipikus töréspontja.
- Egy **évszám** (`1977`) és két **szerzőnév** (Bruce Tuckman, Mary Ann Jensen).


### A szó szerinti szöveg — **másolat, nem kánon**

> „Bruce Tuckman egy csoportkutató volt, aki azt mondta:
>
> **a legtöbb csoport négy fő szakaszon megy át**, mielőtt igazán jól működne (plusz van egy ötödik, a lezárás).
>
> 👉 Az első a **forming**, vagyis az alakulás.
> Ilyenkor mindenki kicsit bizonytalan, udvarias, figyeli a többieket.
>
> 👉 A második a **storming**, amikor jönnek a viták, beszólások, klikkek.
> Ez fárasztó lehet, de **nem hiba**, hanem a fejlődés része.
> Figyelj: a storming kölcsönös vita – a célzott bántás már nem storming.
>
> 👉 A harmadik a **norming**, amikor megszületnek a közös szabályok.
> Már jobban figyelnek egymásra, és elkezd kialakulni a bizalom.
>
> 👉 A negyedik a **performing**.
> Itt a kvuca már tényleg **együtt dolgozik**, saját ötleteket hoz, és felelősséget vállal.
>
> 👉 Tuckman 1977-ben, Mary Ann Jensennel közösen tett hozzá egy ötödiket, az **adjourning**-ot, vagyis a **lezárást**.
> Ez a kvuca búcsúja: amikor egy someres ciklus véget ér, és szépen elköszöntök egymástól.”

*A kánoni példány a leckében áll; ez a másolat a `92d86f7be3c403a5` hash-hez tartozik. Ha a lecke szövege változik, a hash változik, és ezt a másolatot frissíteni kell — a felvétel akkor is a leckéből készül.*

### Kiejtés-érzékeny elemek

| Elem | Elvárás | Forrás |
|---|---|---|
| `kvuca` (2×) | „kvuca”, c = /ts/ | glosszárium, hang-bible 6. |
| `someres` | „someres”, s = /ʃ/ | glosszárium, hang-bible 6. |
| `Tuckman` (2×) | „Takmen”; a teljes név „Brúsz Takmen” (B4, fülre jóváhagyva; VO D-04) | hang-bible 7. |
| `Mary Ann Jensen` | „Méri En Dzsenszen” (B4) | hang-bible 7. |
| `1977-ben` | „ezerkilencszázhetvenhét-ben”, nem számjegyenként | hang-bible 7. |
| `forming` / `storming` / `norming` / `performing` / `adjourning` | „fórming, sztórming, nórming, perfórming, edzsörning” (B4; VO D-04); az `adjourning`-ot toldalékkal | hang-bible 7. |

### Tempó és hangvétel

Nyugodt, tagolt, magyarázó. A kulcsszó kap hangsúlyt, nem az egész mondat. A négy
`👉`-cel kezdődő blokk **azonos ritmusú** legyen — ez a szakaszok listaszerűségét adja
vissza. Nincs lelkesedés, nincs tanári számonkérés.

---

## 3. P2 — Érzelmileg telítettebb, reflektív narráció

- **Asset:** `M6.2-NAR-04` — *Narráció – SLIDE 4 történet 2. rész*
- **Forrás:** `02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md`, `@source` blokk `M6.2-NAR-04-VO` (deklaráció: 492. sor, törzs: 493–512. sor)
- **Forrás-hash:** `f78f0c8b737f2434`
- **Lecke-időkeret:** kb. 40–50 mp · **71 szó** → 85–106 szó/perc
- **Becslés a kanonikus narrátorhang mért tempójával (2026-10-03):** kb. 30 mp — a keret alatt, tehát **van hely a szüneteknek**; szöveget nem töltünk fel a keretig (VO D-17). Ez itt szándékos.

### Miért ez a reprezentatív érzelmi szkript

- Ez a tananyag **legérzelmesebb narratív szakasza**, és pontosan az a hely, ahol a
  hang-bible 3. szakasza a **túljátszást hibának** nevezi: „a szöveg önmagában hordozza
  a feszültséget — a felmondás ne tegyen rá”. Egy reklámhangú vagy drámai TTS ezen a
  szövegen azonnal megbukik; egy generikus marketingmondaton nem bukna meg.
- **Ez az egyetlen szkript, amelyben párbeszéd-idézet van**
  (`‘Figyi, szerintünk ez nem volt oké. / Lehetett volna valamit csinálni?’`), ráadásul
  két sorra tördelve. A hangnak jeleznie kell, hogy idézet — de a 8. szakasz szerint
  **nem külön karakterhanggal**: ez narrátori idézés, nem dialógus-asset.
- Hordozza a három leggyakoribb mozgalmi köznevet (`madrih`, `hanih`, `peula`) és a
  toldalékolt `madrihhoz` / `kvucának` alakot.
- Egyetlen félkövér kiemelés zárja (`a történet tükröt tarthat a kvucának`) — a
  hangsúly a lezáró mondaton ül, nem szórva.


### A szó szerinti szöveg — **másolat, nem kánon**

> „A beszólás után Lili elhallgat.
> Lehajtja a fejét, hátradől.
>
> A madrih hallja, mi történt.
> Látszik rajta, hogy gondolkodik,
> de végül csak megköszöni Lilinek a megosztást,
> és megy tovább a kör.
>
> A peula véget ér.
> Lili szinte végig csendben marad.
>
> A végén két hanih odamegy a madrihhoz,
> és azt mondják:
> ‘Figyi, szerintünk ez nem volt oké.
> Lehetett volna valamit csinálni?’
>
> Most jön az a rész,
> ahol **a történet tükröt tarthat a kvucának**.”

*A kánoni példány a leckében áll; ez a másolat a `f78f0c8b737f2434` hash-hez tartozik. Ha a lecke szövege változik, a hash változik, és ezt a másolatot frissíteni kell — a felvétel akkor is a leckéből készül.*

### Kiejtés-érzékeny elemek

| Elem | Elvárás | Forrás |
|---|---|---|
| `madrih`, `madrihhoz` | „mádrih” [maːdrix] — a toldalékolt alakban is (B4; VO D-04) | hang-bible 6. |
| `hanih` | [xanix] — a szótár aliasa adja (B4; VO D-04) | hang-bible 6. |
| `peula` | „peula”, kisbetűs köznév | glosszárium |
| `kvucának` | hosszú á a toldalékolt tőben | glosszárium |
| `Lili`, `Lilinek` | magyar keresztnév | — |

### Tempó és hangvétel

Visszafogott, tényszerű, meleg — **nem szomorkás és nem drámai**. A „Lili szinte végig
csendben marad.” után valódi szünet kell: a v4 az üres sort nem veszi szünetnek, ezért ha a
központozás kevés, az utómunka kb. 0,6–1,0 mp-et illeszt be (VO D-10). Az idézetnél a
regiszter enyhén vált, a hangszín nem.

---

## 4. P3 — Kiejtés-sűrű narráció

- **Asset:** `M3.1-NAR-05` — *Outro narráció – átvezetés M3.2-re*
- **Forrás:** `02 Tervezet/Modulok/M3/Online leckék/M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md`, `@source` blokk `M3.1-NAR-05-VO` (deklaráció: 811. sor, törzs: 812–818. sor)
- **Forrás-hash:** `17184b1a6e2cf25c`
- **Lecke-időkeret:** 15–20 mp · **40 szó** → 120–160 szó/perc

> ✅ **Mért hossz (kanonikus narrátorhang, 2026-10-03): 18,5 mp** — a lecke 15–20 mp-es keretén belül, gyorsítás
> nélkül. A korábbi, 110 szó/perces céltempóra számolt kb. 22 mp-es becslés elavult (hang-bible
> 4.). A szabály változatlan: ha egy felvétel nem fér a keretbe, **a keretet kell tágítani**, nem
> a hangot gyorsítani — a keretről a szerző dönt, nem a hang (VO D-17).

### Miért ez a reprezentatív kiejtési szkript

- A tananyag **legsűrűbb someres kiejtési tesztje**: 40 szóban több kiejtés-érzékeny elem, köztük **mind a három aktuális kvuca-tulajdonnév egyetlen felsorolásban**.
- A `Leviatán`: az írott alak a kánon (projektgazdai döntés, 2026-10-02, HUM-SOMER-02), a hangja
  a fülre jóváhagyott „Leviatan” (B4; projektgazdai döntés, 2026-10-03, VO D-05) — a szótár
  aliasa adja, a felirat „Leviatán”. Ha a hang ezt elrontja, az minden előfordulásnál hallatszik.
- Rövid: egy jelölt kiejtési profilja 20 másodperc alatt eldönthető, mielőtt a hosszabb
  szkriptekre költenél.


### A szó szerinti szöveg — **másolat, nem kánon**

> „Köszi, hogy végigmentél ezen a leckén.
> Most már van egy térképed arról, hogyan fejlődik egy kvuca.
> A következő részben belenagyítunk a három aktuális someres kvucába:
> Parparim, Kivsza és Leviatán –
> hogy lásd, milyen világban élnek, és te miben tudsz hozzájuk kapcsolódni.”

*A kánoni példány a leckében áll; ez a másolat az `17184b1a6e2cf25c` hash-hez tartozik. Ha a lecke szövege változik, a hash változik, és ezt a másolatot frissíteni kell — a felvétel akkor is a leckéből készül.*

### Kiejtés-érzékeny elemek

| Elem | Elvárás | Forrás |
|---|---|---|
| `Parparim` | „parparim” | glosszárium |
| `Kivsza` | „kivsza” | glosszárium |
| `Leviatán` | „Leviatan” [leviotɒn] — rövid a-val (B4); a felirat „Leviatán” | projektgazdai döntés (2026-10-03, VO D-05); hang-bible 6. |
| `kvuca`, `kvucába` | c = /ts/; a toldalékolt tőben hosszú á | glosszárium |
| `someres` | s = /ʃ/ | glosszárium |
| `és` a felsorolás végén, `–` gondolatjel | a gondolatjel szünet, nem felmondandó | hang-bible 5. |

### Tempó és hangvétel

Lezáró, barátságos, kicsit lassuló. A négy tulajdonnév **külön-külön hallható** legyen —
ez a szkript egyetlen valódi feladata. A gondolatjel után rövid levegő.

---

## 5. Hogyan kell a pilotot futtatni

1. **A három szkript a kanonikus narrátorhanggal fut**, a produkciós konfigurációval
   ([`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 12.); hangválasztás nincs (VO D-14). P1 a hosszú
   magyarázó ívet, P2 az érzelmi sávot, P3 a kiejtést méri.
2. **A szintézis bemenete a tisztított szöveg**, nem a nyers Markdown. A pontos szabályokat
   az [`ELEVENLABS-VOICE-TEST.md`](./ELEVENLABS-VOICE-TEST.md) 2.1. szakasza rögzíti —
   röviden: a `**…**` jelölés **eltávolítandó** (nem fordítandó hangsúly-jelölésre), az emoji a
   mögötte álló szóközzel együtt törlendő, a nyitó/záró `„ ”` a forrásblokk határa; a sortörés
   és az üres sor nem szünetvezérlő (VO D-10).
3. **A kiejtési táblát (hang-bible 6–7.) végig kell hallgatni** — a futás a **kanonikus
   szótárral** megy (VO D-03). A jóváhagyott hangzás a B4-regiszteré; ha egy szó a próbától
   hallhatóan eltér, az regresszió, nem új döntés (VO D-13, D-23).
4. **A jóváhagyó magyar anyanyelvű, someres szóhasználatot ismerő ember.** A
   `Leviatán` / `kvuca` / `hanih` alak helyességét nem lehet leírt átiratból eldönteni.

## 6. Elfogadási feltétel a hang-pilotra

- [ ] mind a három szkript elkészült a kanonikus narrátorhanggal;
- [ ] P1 gyorsítás és időnyújtás nélkül a lecke 60–75 mp-es keretén belül marad, és a jelentést
      hordozó hangsúly nem sérül (fülre) (VO D-11, D-17);
- [ ] P1-ben egyetlen emoji sem hangzik el;
- [ ] P2 nem játssza túl az érzelmi tartalmat, és az idézet nem külön karakterhang;
- [ ] P3-ban mind a három aktuális kvuca-név helyes, és a `Leviatán` „Leviatan”-ként, rövid
      a-val szól (B4; VO D-05);
- [ ] a `madrih` „mádrih” [maːdrix], a `hanih` [xanix] hangzású (B4; VO D-04) — nem a fülre
      elvetett kerekített olvasat;
- [ ] a `kvuca` c-je /ts/, a `Somer` s-e /ʃ/;
- [ ] a hang tegező, egyenrangú, nem gyerekhang és nem hivatalos;
- [ ] a felvétel szó szerint fedi a forrásszöveget (a felirat ebből generálódik);
- [ ] tiszta beszéd, háttérzaj nélkül; a mester 48 kHz / 16 bit / mono WAV (VO D-12); a
      hangerő-normalizálás célértéke ekkor rögzíthető.

> **Írásmód — projektgazdai döntés (2026-10-02):** a magyar Somer first-party alakjai a
> kánon (madrih, hanih, hágsámá, dugma isit, Leviatán), és a tanulói korpusz egyszeri gépi
> migrációt kapott (2026-10-02). Ezzel a P2 és a P3 forrásszövege is változott: a fenti
> másolatok és a hash-ek a migrált szöveget követik, a karakterszám az
> `ELEVENLABS-VOICE-TEST.md`-ben frissítve, a szószám nem változott. A P2 és P3 hangmintáját a migrált szöveggel, **a terminológiai
> ellenőrzővel együtt** érdemes meghallgatni (utólagos ellenőrzés (vétó/QA): a ken-vezető /
> mozgalmi felelős).
>
> **Korosztály-architektúra frissítve 2026-09-28:** a tananyag a 2025/26-os oktatási tervre
> hivatkozó három csoportot használja: **Parparim 6–9, Kivsza 10–12, Leviatán 13–17** (HUM-SOMER-02; projektgazdai döntés, 2026-10-02).
> A P3 ezért már csak ezt a három tulajdonnevet teszteli.
