# 🎧 ElevenLabs hangválasztás — végrehajtható meghallgatási teszt

Egyetlen célja van: eldönteni, hogy a **Dombi Miksa** vagy a **Budai Enn** legyen a
tananyag **kanonikus narrátora**.

| | |
|---|---|
| **Szolgáltató** | **ElevenLabs** — felhasználói döntés, 2026-08-28, lezárva |
| **Jelöltek** | **Dombi Miksa** · **Budai Enn** — **forrás-beszélők**: az ő felvételeikből készül majd a két ElevenLabs egyedi hang, amelyek **még nem jöttek létre** |
| **Eldöntendő** | melyik a kanonikus narrátor |
| **Minta** | **6 db** — 2 hang × 3 meglévő tananyag-szkript |
| **Mért méret** | **3 066 karakter** összesen |
| **Becsült költség** | **0,15 – 0,61 $** (`eleven_flash_v2_5`) — a szolgáltató két árazási felülete eltérő szorzót ad; mindkét olvasatban **egy dollár alatt** |
| **Állapot** | ⛔ **nem futtatható — a két ElevenLabs hang még nincs létrehozva** (előbb: hozzájárulás-bizonyíték → hang-létrehozás → azonosítás) |

Kapcsolódó: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 12–13. szakasz (a kutatás és a
modell-javaslat) · [`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md) (a három szkript
szó szerinti szövege és indoklása) · [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md)
D2.

---

## 1. Amit a teszt előtt tudni KELL — három blokkoló lépés

A hat mintát **nem szabad** legenerálni, amíg ez a három nem történt meg.

### 1.0. A hangok létrehozása — `A HANGOK MÉG NEM LÉTEZNEK`

**Dombi Miksa** és **Budai Enn** jelenleg **forrás-beszélők**: tőlük származnak (illetve
készülnek) azok a felvételek, amelyekből a két ElevenLabs egyedi hangot létre kell hozni.
A hang-objektumok **még nem léteznek**, ezért voice-ID sincs.

- **A létrehozás módja nyitott** (Instant Voice Clone / Professional Voice Clone / egyéb):
  a jog- és hozzájárulás-helyzet, valamint a fiók-/csomagkeret dönti el —
  a következményeket típusra bontva a [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md) rögzíti.
  Ez a lap **nem dönti el**.
- **Hozzájárulás-bizonyíték (V2) a feltöltés ELŐTT:** valós személy hangfelvétele csak
  dokumentált hozzájárulással tölthető fel; a bizonyíték-nyilvántartás helye a
  [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md).
- **Összevethetőség:** a tesztnek csak akkor van értelme, ha a két hang **azonos módszerrel**
  és feltételekkel készül el — különben a különbség nem a hangot, hanem a létrehozási
  módot mérné.

### 1.1. A hangok azonosítása a létrehozás UTÁN — `LÉTREHOZÁS UTÁN RÖGZÍTENDŐ`

Ebben a környezetben **nincs ElevenLabs hitelesítő adat**, és a hangok még nem is léteznek,
ezért voice-ID-t és hangtípust rögzíteni még nem lehet. **Nem is találtuk ki őket.**
Amint a két hang elkészült, ezt a táblát kell kitölteni:

| Hang | Voice ID | Hangtípus | Magyar nyelvre igazolt? | Modell-kompatibilitás |
|---|---|---|---|---|
| **Dombi Miksa** (a forrás-beszélőből készülő hang) | `MÉG NEM LÉTEZIK — LÉTREHOZÁS UTÁN RÖGZÍTENDŐ` | `MÉG NEM LÉTEZIK` | `LÉTREHOZÁS UTÁN` | `LÉTREHOZÁS UTÁN` |
| **Budai Enn** (a forrás-beszélőből készülő hang) | `MÉG NEM LÉTEZIK — LÉTREHOZÁS UTÁN RÖGZÍTENDŐ` | `MÉG NEM LÉTEZIK` | `LÉTREHOZÁS UTÁN` | `LÉTREHOZÁS UTÁN` |

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

> **Miért blokkoló:** ha bármelyik hang **PVC**, a `eleven_v3` gyakorlatilag kiesik (a PVC
> a szolgáltató szerint nem arra tanul, és „not fully optimized for Eleven v3”), és a
> modellkérdés magától eldől. A típus ismerete nélkül a teszt rossz modellen futna.

### 1.2. A tanítási kimaradás bekapcsolása

A szolgáltató feltételei szerint a tanítási kimaradás **csak előremutató**: „does not
affect any uses… prior to that date”. Ezért a fiók *Data use* beállításában **már a
forrásfelvételek feltöltése — tehát a hangok létrehozása — előtt** ki kell kapcsolni a
tanítási felhasználást, nem utólag.

---

## 2. A teszt beállításai

| Paraméter | Érték | Miért |
|---|---|---|
| `model_id` | **`eleven_flash_v2_5`** | a magyar támogatott, van tempó-vezérlés, a beállítások rögzíthetők — [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.2. |
| `language_code` | **`"hu"`** | ez kényszeríti a magyar olvasatot; enélkül a someres szavak angol vagy héber fonetikát kaphatnak |
| `voice_settings.stability` | **0,70** | a 3. szakasz szűk érzelmi sávjához; alacsonyabb érték szélesebb, hullámzóbb előadást ad |
| `voice_settings.similarity_boost` | **0,75** | alapérték; a hang karakterét tartja |
| `voice_settings.style` | **0,0** | a szolgáltató kifejezett ajánlása; emelve romlik a stabilitás |
| `voice_settings.use_speaker_boost` | **`true`** | alapérték |
| `voice_settings.speed` | **1,0** kiindulásként | a mért tempóhoz igazítandó, tartomány 0,7–1,2 |
| `seed` | **egyetlen rögzített egész**, mind a hat mintára ugyanaz | különben a hangok különbsége és a véletlen ingadozás összekeveredik |
| `pronunciation_dictionary_locators` | **nincs — szándékosan üres** | a teszt egyik célja épp az, hogy kiderüljön, mire kell szótár |
| `output_format` | **a legjobb, amit a csomag ad** (`wav_44100` Pro-n, egyébként `mp3_44100_192`) | a meghallgatást ne a tömörítés döntse el |
| `use_pvc_as_ivc` | **explicit `false`**, ha a hang PVC | különben nem tudni, melyik renderelés szólalt meg |
| `apply_text_normalization` | **explicit, rögzített érték** — mind a hat mintára ugyanaz | a 4. szakasz figyelőlistája kifejezetten teszteli a számnormalizálást (`1977-ben`); ha ez a paraméter nincs rögzítve, az eredmény nem köthető ismert beállításhoz. Ha a választott modell nem támogatja, azt is **rögzíteni kell** |

**A két hangnak minden más paramétere azonos legyen.** Amit összehasonlítunk, az a hang —
nem a beállítás.

> ⚠️ **Minden beállítást explicit el kell küldeni a kérésben.** A kérésben megadott
> beállítás felülírja a hangon tároltat, de csak arra a kérésre; ha a tároltra hagyatkozunk,
> a kimenet később csendben megváltozhat, ha valaki a felületen hozzányúl a hanghoz.

### 2.1. A szintézis bemenete — tisztított szöveg

A `@source` blokk szövege, de:

- a **nyitó és záró `„ ”`** idézőjel nélkül (az a forrásblokk határa, nem felmondandó);
- a `**…**` félkövér-jelölés **eltávolítva** (a hangsúly forrása, de maga nem hangzik el);
- **minden emoji eltávolítva, a közvetlenül utána álló szóközzel együtt** — a P1-ben öt
  `👉 ` áll sorkezdeten, és a szóköz elhagyása nélkül a karakterszám 832 lenne, nem 827;
- a sortörések és az üres sorok **megmaradnak** (rövid levegő, illetve bekezdés-szünet);
- **szögletes zárójel nem kerülhet a szövegbe.** Ez **saját produkciós óvatosság, nem
  idézett szolgáltatói előírás**: a szögletes zárójel a szolgáltatónál az *audio tag*
  szintaxisa, amit a választott modell nem értelmez — a tananyag szövegében amúgy sem
  fordul elő, tehát a szabály költségmentes.

**Mind a hat mintához bájtra ugyanaz a tisztított szöveg megy be.**

---

## 3. A hat minta

A három szkript a tananyag meglévő narrációja — nem tesztszöveg. A szó szerinti szöveg,
a forrás-hivatkozás és a kiválasztás indoklása:
[`VOICE-PILOT-SCRIPTS.md`](./VOICE-PILOT-SCRIPTS.md).

| Szkript | Asset | Forrás-hash | Karakter | Szó | Lecke-időkeret | Mit mér |
|---|---|---|---:|---:|---|---|
| **P1** | `M3.1-NAR-02` | `0ec386081b2a7fab` | **827** | 125 | 60–75 mp | hosszú magyarázó ív, hangsúly, angol szakszavak, évszám |
| **P2** | `M6.2-NAR-04` | `72d4bb4dbb80803a` | **438** | 71 | 40–50 mp | visszafogott érzelmi sáv, idézet, `madrich`/`chanich`/`peula` |
| **P3** | `M3.1-NAR-05` | `22f975437c89e97f` | **268** | 40 | 15–20 mp | mind a négy kvuca-tulajdonnév |
| | | **hangonként** | **1 533** | 236 | ≈ 2 perc | |
| | | **hat minta** | **3 066** | 472 | ≈ 4 perc | |

**A mátrix:**

| | P1 | P2 | P3 |
|---|---|---|---|
| **Dombi Miksa** | ☐ | ☐ | ☐ |
| **Budai Enn** | ☐ | ☐ | ☐ |

**Fájlnév a teszthez** (ideiglenes, nem produkciós asset):

```
teszt__<hang>__<szkript>__<modell>__seed<n>.<kiterjesztés>
pl.  teszt__dombi-miksa__P1__flash-v2-5__seed4242.wav
```

Ezek **nem** kerülnek a `masters/` alá és nem asset-deliverable-ök — a hangválasztás
munkaanyagai.

---

## 4. Kiejtési figyelőlista

A teszt **szótár nélkül** fut. Ez a lista mondja meg, **mit kell figyelni**, és ebből lesz
utána a szükséges alias-szabályok listája — csak azokra a szavakra, amelyek ténylegesen
elromlanak.

A kánoni alakok forrása a `Glosszárium – someres és pedagógiai fogalmak.md` és a
[`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 6. szakasza. **A jelenlegi írásmódot teszteljük** — a
`madrich`/`madrih` és `chanich`/`hánih` house-style kérdés nyitva van, és ez a lap nem
nyúl hozzá.

| Szó | Elvárt kiejtés | Hol | Kockázat |
|---|---|---|---|
| `kvuca`, `kvucába`, `kvucának` | „kvuca” — a **c** = /ts/ | P1, P2, P3 | angol /k/ vagy /kw/ olvasat |
| `someres` | **s** = /ʃ/ | P1, P3 | angol /s/ |
| `madrich`, `madrichhoz` | szóvégi **ch** torokhang, nem /cs/, nem /k/ | P2 | **magas** — a `ch` digráf nem magyar elem |
| `chanich` | a **ch** ugyanaz, **szó elején is** | P2 | **magas** |
| `peula` | „peula” | P2 | ékezet vagy hangsúly elcsúszása |
| `Parparim` | „parparim” | P3 | idegen hangsúly |
| `Kivsza` | „kivsza” | P3 | — |
| `Leviatan` | „leviatan” — **ékezet nélkül** | P3 | **magas** — a „Leviatán” alak tiltott, a modell hajlamos megnyújtani |
| `Zorea` | „zorea” | P3 | — |
| `Tuckman` | a pilot rögzíti; utána következetesen | P1 | nincs kánoni előírás |
| `1977-ben` | „ezerkilencszázhetvenhét-ben”, nem számjegyenként | P1 | számnormalizálás |
| `forming` / `storming` / `norming` / `performing` / `adjourning`-ot | angol olvasat magyar mondatban, az utolsó magyar toldalékkal | P1 | kódváltás |
| `👉` (5×) | **nem hangzik el** | P1 | ha a tisztítás kimaradt, felolvassa |

**Amit a három szkript nem fed le**, és a köteg-jóváhagyáskor külön kell ellenőrizni:
`ken`, `Zmán Kvucá`, `dugma ishit`, `hagshama`, `bogrim`, `mazkirut`, `Hasomer Hacair`,
`Johari`, az `SBI` betűzés, a korosztály-tartományok és az időtartamok.

> **Ha egy szó elromlik:** a `flash_v2_5` **alias**-szabályt fogad el (fonéma-szabályt
> kihagy). A magyar toldalékolás miatt **minden ténylegesen előforduló alakot** fel kell
> venni, mert a szóhatár-illesztés alapértelmezetten bekapcsolt: a `Somer` szabály nem
> illeszkedik a `someres`-re. Részletek: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.5.

---

## 5. Pontozólap

Mind a hat mintára külön. **1–5** skála, ahol **3 = elfogadható**, **5 = kiváló**.

| # | Szempont | Dombi P1 | Dombi P2 | Dombi P3 | Enn P1 | Enn P2 | Enn P3 |
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
> szerepéről**, csak rögzíti az adatot, amíg ingyen van.

**Súlyozás, ha a két hang közel van:** a 3. (someres szavak), a 9. („nem reklámhang”) és
a 10. (fárasztóság) sor **kétszeres súlyt** kap. Ez a három dönti el, hogy egy hang
kibírja-e 117 tételen — nem az, hogy melyik szebb egyetlen mintán.

### 5.1. Azonnali bukás — bármelyik önmagában kizár egy hangot

- [ ] **B1 — Javíthatatlan kiejtés.** Egy kánoni someres szó rosszul szól, és
      alias-szabállyal sem hozható helyre. *(A `Leviatan` → „Leviatán” önmagában ilyen: a
      glosszárium kifejezetten tiltja.)*
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
0.  hozzájárulás-bizonyíték (V2)      → RIGHTS-EVIDENCE.md; feltöltés előtt kötelező
0b. a két hang létrehozása (1.0.)     → azonos módszerrel; a módszer (IVC/PVC/egyéb)
                                        jog + csomag függvénye — még nyitott
1.  hangok azonosítása (1.1.)         → voice ID + típus rögzítve
2.  tanítási kimaradás bekapcsolva    → (1.2.) — a feltöltés ELŐTT
3.  ha bármelyik hang PVC             → a modell flash_v2_5, a v3 kiesik
4.  hat minta legyártása              → 0,15–0,61 $
5.  meghallgatás + pontozás           → magyar anyanyelvű, someres szóhasználatot
                                        ismerő jóváhagyóval
6.  a nyertes P2-jének újragyártása   → B2 stabilitási próba
7.  hibás szavak listája              → alias-szabályok, majd újrahallgatás
8.  KANONIKUS HANG kiválasztva        → D2 lezárul
9.  a reprodukciós metaadat rögzítve  → az R3 lezárható
```

**A 8. lépés a felhasználó döntése.** Ez a lap előkészíti, nem helyettesíti.

### 6.1. Mit kell rögzíteni, amikor a döntés megszületik

Ezek nélkül az R3 **nem** zárható le, mert a felvétel nem reprodukálható:

`voice_id` · `voice_display_name` · `voice_type` (`category`) · `model_id` ·
`language_code` · a teljes `voice_settings` objektum (mind az öt mező) · `seed` ·
`output_format` · a kiejtési szótár azonosítója **és `version_id`-je** ·
`use_pvc_as_ivc` · `apply_text_normalization`.

> **Őszinte plafon.** A szolgáltató kimondja, hogy a modellek nem determinisztikusak, és
> a seed is csak „best effort”. Egy fél év múlva újragyártott klip **hasonló lesz, nem
> bitre azonos**. Ezért a produkciós szabály: újragyártásnál mindig meghallgatás, és
> inkább a **teljes tétel** újravétele, mint egy javított mondat beillesztése.

## 7. Amit ez a teszt NEM dönt el

- **A második hang szerepét.** Egy hang lesz a kanonikus narrátor; a másik esetleges
  szerepe (tartalék, dialógus- vagy karakterhang) **külön, későbbi döntés**.
- **A csomagot.** A kimeneti formátum és a hangtípus dönti el, nem a karakterár —
  [`VOICE-BIBLE.md`](./VOICE-BIBLE.md) 13.7. és 13.9.
- **A hang-jogosultságot.** → [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md), V2/V3 kapuk.
- **A kiejtési szótár végleges tartalmát.** Az a teszt *eredménye*, nem a bemenete.
