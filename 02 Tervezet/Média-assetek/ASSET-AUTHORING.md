# Asset-deklarációk — szerzői útmutató

Ez a gyakorlati kézikönyv ahhoz, hogyan írj asset-igényt egy leckébe. A rendszer
áttekintése: [`README.md`](./README.md).

**Az egyetlen szabály, amit érdemes fejben tartani:** a szöveget egy helyen
tartod — a leckében. A regiszter, a felirat, a leirat és a hang mind onnan
származik.

> Az itteni példák **kitalált `M9` modulra** hivatkoznak, hogy másolás után
> biztosan ne írj felül egy valódi assetet. Élő példákért nézd meg a
> [`Média-asset regiszter.md`](./Média-asset%20regiszter.md) megfelelő fájlszakaszát.

---

## 1. A két blokk

### `@asset` — mit kell legyártani

```markdown
<!-- @asset
{
  "id": "M9.1-VID-01",
  "kind": "video",
  "subtype": "ai-talking-head",
  "title": "HOOK beszélő fej – suli / somer / random",
  "source_ref": "M9.1-VID-01-VO",
  "a11y": {"audio": "spoken", "visual": "decorative"},
  "derivatives": ["voiceover", "captions", "transcript"],
  "provenance": "ai",
  "production_rules": ["R1", "R2", "R3"]
}
-->
```

Szigorú JSON: dupla idézőjel, nincs záró vessző, nincs komment. A záró `-->`
kerülhet a nyitó sorra is, ha rövid a tartalom.

### `@source` — a szó szerinti szöveg

```markdown
<!-- @source {"id": "M9.1-VID-01-VO", "kind": "narration"} -->

> „Szia!
> Gondolj vissza az elmúlt hetekre.

> És azt is, hogy **a Somer hol van ebben a képben**.”

<!-- @endsource -->
```

A fordító csak a `>` jelölést veszi le. A szavak, az idézőjelek, a kiemelések és
a bekezdéshatárok érintetlenül maradnak — **nem szerkesztő, hanem másoló**.

**Mikor kell forrásblokk?** Ha van olyan szöveg, amit szó szerint kell
legyártani: felmondandó narráció, alt-szöveg, kártyára/poszterre nyomtatandó
mondatok. **Mikor nem?** Ha a leckében csak leírás van arról, mit ábrázoljon egy
kép — az a `spec` mezőbe való, nem forrásblokkba.

---

## 2. Másolható példák

### 2.1 Csak narráció (nincs videó)

```markdown
<!-- @asset
{
  "id": "M9.1-NAR-03",
  "kind": "voiceover",
  "subtype": "narration",
  "title": "SLIDE 3 narráció – a négy mező",
  "source_ref": "M9.1-NAR-03-VO",
  "derivatives": ["captions", "transcript"],
  "provenance": "mixed",
  "technical": {"note": "kb. 40–60 mp, tegező, rövid mondatok"}
}
-->
```

### 2.2 AI beszélő fej videó

Lásd az 1. pont példáját. A `voiceover` derivatíva a felvett hang, a `captions`
és a `transcript` ugyanabból a `@source` blokkból készül.

### 2.3 Néma videó (képernyőfelvétel, B-roll)

```json
{"id": "M9.3-VID-02", "kind": "video", "subtype": "screen-recording",
 "title": "Moodle-navigáció képernyőfelvétel",
 "a11y": {"audio": "silent", "visual": "decorative",
          "alt_note": "a lépéseket a dia szövege is leírja"},
 "spec": "Kurzus-főoldal → modul → H5P megnyitása, kurzorkiemeléssel."}
```

A `"audio": "silent"` **explicit állítás**: nincs benne beszéd, ezért nem kell
felirat. Ha bizonytalan vagy, `"spoken"` a helyes választás.

### 2.4 Tartalmi illusztráció alt-szöveggel

```markdown
<!-- @asset
{
  "id": "M9.1-DIA-01",
  "kind": "diagram",
  "title": "Johari-ablak 2×2 diagram",
  "a11y": {"visual": "informative", "alt_source_ref": "M9.1-DIA-01-ALT#1"},
  "derivatives": ["alt-text"],
  "provenance": "ai",
  "production_rules": ["R1", "R5"]
}
-->
```

és a leckében, ahol az alt-szöveg áll:

```markdown
<!-- @source {"id": "M9.1-DIA-01-ALT", "kind": "alt-text"} -->

* **Alt-szöveg / szöveges ekvivalens (kötelező):** „A Johari-ablak 2×2-es
  diagramja. Oszlopok: én ismerem / én nem ismerem…”

<!-- @endsource -->
```

A `#1` a blokkban álló `„…”` idézetet választja ki — a blokk szövegéből csak az
alt-ot, a körülötte lévő előírás-mondat nélkül.

**A szabály:** minden forráshoz kötött alt kapja meg a **saját `@source`
blokkját**, és abban **pontosan egy** `„…”` idézet legyen; a hivatkozás mindig
`#1`. Ha a blokkba egy második idézet is belekerül, a fordító **hibát jelez** —
nem választ helyetted. Ez szándékos: egy pozíciós szelektor némán átcsúszna egy
másik idézetre, ha valaki később beszúr egyet elé, és a CI ettől még zöld
maradna.

**Ha nem fér bele:** ne told a jelölőt egy bekezdés közepébe. Ha az alt pontos
körbezárása megváltoztatná a renderelt Markdown szerkezetét — például egy
idézetblokkon belül két alt áll egy bekezdésben, és a közéjük tett jelölő
kettévágná azt a bekezdést —, akkor hagyd forrás nélkül: `a11y.alt_note`-tal
tartsd meg az alt-követelményt, és írd le a mezőben, hogy a szöveg a leckében
van megírva, de erre az egy altra nem terjed ki az élő ellenőrzés.

### 2.5 Dekoratív kép

```json
{"id": "M9.1-IKO-01", "kind": "icon-set", "title": "Hook-ikon: útiterv",
 "a11y": {"visual": "decorative",
          "alt_note": "a jelentést a cím és a bullet-szöveg hordozza"},
 "provenance": "ai"}
```

A dekoratív jelölés **döntés, nem hiány**: azt állítod, hogy az elem nem hordoz
olyan információt, ami máshol ne lenne meg szövegként.

### 2.6 Stock vagy külső fotó

```json
{"id": "M9.3-FOTO-01", "kind": "photo", "mode": "external",
 "title": "Kvuca közös plakáton dolgozik",
 "external": {"source": "stock-kép beszerzés",
              "licence": "nyitott: licenc, attribúció és jogcím igazolása (R8)"},
 "a11y": {"visual": "informative", "alt_source_ref": "M9.3-FOTO-01-ALT#1"},
 "derivatives": ["alt-text"], "provenance": "stock", "blockers": ["R8"]}
```

### 2.7 Nyomtatható munkalap

```json
{"id": "M9.A-MUNK-01", "kind": "worksheet",
 "title": "Megfigyelés vagy címkézés? – képzői segédlet",
 "spec": "8 példamondat, mindegyik mellett megfigyelés / címke jelöléssel.",
 "derivatives": ["print-pdf"], "provenance": "human",
 "technical": {"note": "A4, 1 oldal, fekete-fehér nyomtatásra is olvasható"}}
```

### 2.8 Kártyaszett

```json
{"id": "M9.A-KART-02", "kind": "card-set", "title": "Kvuca-sztori kártyák",
 "spec": "8 nyomtatható kártya, kvucánként egy rövid sztorival.",
 "derivatives": ["print-pdf"], "provenance": "human"}
```

### 2.9 Letölthető sablon / dokumentum

```json
{"id": "M9.4-MUNK-01", "kind": "template", "subtype": "spreadsheet",
 "title": "Feladat–kvuca–módszer kitölthető tábla",
 "spec": "4 oszlopos sablon, kitöltött mintasorral.",
 "derivatives": ["print-pdf"], "provenance": "human"}
```

### 2.10 Beszerzendő eszköz (nem gyártjuk)

```json
{"id": "M9.F-EGY-01", "kind": "print", "subtype": "consumable", "mode": "external",
 "title": "Check-in matrica / post-it készlet",
 "external": {"source": "beszerzendő irodaszer", "owner": "képzés-logisztika"}}
```

### 2.11 Zene vagy SFX

```json
{"id": "M9.A-HANG-01", "kind": "audio", "subtype": "music",
 "title": "Aláfestő zene a gallery walkhoz",
 "derivatives": ["transcript"],
 "provenance": "third-party",
 "external": {"source": "licencelt zenei könyvtár"}, "blockers": ["R8"]}
```

A `transcript` hangnál is kötelező: hangzó tartalom szöveges ekvivalens nélkül
nem mehet ki (WCAG 2.2 SC 1.2.1). Zenénél ez rövid leírás is lehet.

### 2.12 Explicit újrahasznosítás

```json
{"id": "M9.4-IKO-01", "kind": "icon-set", "mode": "reuse",
 "reuse_of": "M9.2-IKO-01",
 "title": "Négy kvuca-ikon (az M9.2-ből)",
 "notes": "Ugyanaz a négy piktogram, csak más elrendezésben."}
```

**Csak akkor újrahasznosítás**, ha *ugyanaz a legyártott fájl* kerül be mindkét
helyre. „Hasonló”, „ugyanaz a stílus”, „ugyanarról szól” — ezek **nem**
újrahasznosítások. Az újrahasznosított asset nem kap derivatívákat.

### 2.13 Emberi döntésre váró tétel

```json
{"id": "M9.B-KART-03", "kind": "card-set", "mode": "human-decision",
 "title": "Képzői safety-gyorskártya",
 "decision": "Kell-e ez a segédanyag, és ha igen, milyen tartalommal — a képzés gyermekvédelmi felelősével."}
```

A `decision` **kötelező**: eldöntetlen tétel nem tűnhet el csendben a leltárból.

### 2.14 Média nélküli fájl

```markdown
<!-- @asset-free
{
  "reason": "Kapu-fájl: item-bank és rubrika. A benne szereplő plakát- és kártyaemlítések kvíz-szituációk, nem legyártandó anyagok."
}
-->
```

Egy fájlban egy ilyen blokk lehet, és akkor nem lehet benne `@asset`.

---

## 3. Mezőtár

| Mező | Kötelező | Mit jelent |
|---|---|---|
| `id` | ✅ | `<egység>-<TÍPUS>-<nn>`; az egységet a fájl útvonala adja |
| `kind` | ✅ | `video`, `voiceover`, `audio`, `animation`, `image`, `illustration`, `diagram`, `icon-set`, `screenshot`, `photo`, `document`, `template`, `download`, `print`, `worksheet`, `card-set`, `poster`, `other` |
| `title` | ✅ | rövid, ember-olvasható megnevezés |
| `subtype` | | `video`: `ai-talking-head`, `explainer`, `interactive`, `screen-recording`, `live-action`; `audio`: `narration`, `music`, `sfx`, `ambience`; `document`: `pdf`, `docx`, `spreadsheet`, `checklist`, `handout`, `template` |
| `mode` | | `generate` (alapértelmezett), `reuse`, `external`, `provided`, `human-decision` |
| `purpose` | | miért van rá szükség (pedagógiai cél) |
| `spec` | | mit kell legyártani |
| `source_ref` | | a felmondandó szöveg forrásblokkja |
| `a11y` | | `visual`, `audio`, `alt_source_ref`, `alt_note`, `note` |
| `derivatives` | | `voiceover`, `captions`, `transcript`, `alt-text`, `thumbnail`, `audio-only`, `low-bandwidth`, `print-pdf` |
| `provenance` | | `human`, `ai`, `stock`, `third-party`, `mixed`, `unknown`, `pending` |
| `technical` | | szabad kulcs-érték (arány, hossz, méret, formátum) |
| `external` | | `source`, `url`, `path`, `owner`, `licence`, `evidence`, `replace` |
| `production_rules` | | R1–R8 hivatkozás |
| `blockers` | | nyitott kapuk (R2, R3, R5, R8) — ezek adják a státuszt |
| `decision` | `human-decision`-nél ✅ | mit kell eldönteni és kinek. **Bármelyik módnál megadható**, és amíg nem üres, a státusz `emberi döntésre vár` — a produkciós szabályok előtt |
| `reuse_of` | `reuse`-nál ✅ | a kanonikus asset ID-je |
| `notes`, `review` | | megjegyzés, illetve migrációs/szerkesztői észrevétel |
| `legacy` | | a v1 sorok leképezése (`{"asset": [...], "captions": [...]}`) |

---

## 4. Amit a fordító kikényszerít

* beszélt videóhoz **felirat és leirat** derivatíva (WCAG 2.2 SC 1.2.2);
* csak hangzó assethez **leirat** (SC 1.2.1);
* tartalmi vizuálishoz **alt-text** derivatíva és alt-forrás (vagy `alt_note`);
* vizuális assetnél az `a11y.visual` **explicit** — a dekoratív is döntés;
* egyedi asset- és forrás-ID, létező hivatkozások;
* újrahasznosításnál: létező cél, nem önmaga, nincs kör, kompatibilis típus;
* `external`/`provided` assetnél forráshivatkozás;
* `human-decision`-nél `decision`.

A fordító a **manifeszt szerkezetét** ellenőrzi. Azt, hogy a kész Moodle/H5P
oldal tényleg akadálymentes-e, továbbra is a release-elfogadás dönti el.

---

## 5. Munkamenet

```bash
# 1. szerkeszted a leckét (deklaráció és/vagy forrásszöveg)
# 2. újraépíted a regisztert
python3 tools/media_manifest.py build
# 3. commitolod a leckét ÉS a generált kimeneteket együtt
git add "02 Tervezet"
# 4. commit előtt ellenőrzés
python3 tools/media_manifest.py check
```

Ha kihagynád a 2. lépést, a CI `check` lépése pirosra vált, és megmondja, melyik
generált fájl csúszott el.
