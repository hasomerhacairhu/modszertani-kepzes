# Média – release-státusz és staging-prioritás

> **Cél:** különválasztani azt a kérdést, hogy egy médiaelem **kell-e az adott kiadási körhöz**, attól, hogy **legyártható-e már**.
>
> A generált médiaregiszter továbbra is a leckék `@asset` deklarációiból készül. Ez a dokumentum kiadási policy, nem párhuzamos assetleltár.

## 1. Két külön állapot

### 1.1. `release_tier`

| Érték | Jelentés |
|---|---|
| `REQUIRED_FOR_FIRST_RELEASE` | Az első értelmes Moodle-szelet pedagógiai vagy hozzáférhetőségi működéséhez ténylegesen szükséges, és nincs egyenértékű fallback. |
| `REQUIRED_LATER` | A teljes képzés későbbi moduljához vagy jóváhagyott végleges élményéhez kell, de az M0+M1 staginget nem blokkolja. |
| `OPTIONAL` | Javítja az élményt vagy a vizuális egységet, de a tanulási cél teljes értékűen elérhető nélküle. |

### 1.2. `production_state`

| Érték | Jelentés |
|---|---|
| `READY_TO_PRODUCE` | A forrás és specifikáció elég a gyártáshoz, nincs nyitott kapu. |
| `BLOCKED_BY_HUMAN_DECISION` | Tartalmi, szervezeti vagy produkciós döntés kell. |
| `BLOCKED_BY_CONSENT` | Jogosultság, hozzájárulás, képmás-, hang- vagy felhasználási jog bizonyítéka hiányzik. |
| `BLOCKED_BY_TECHNICAL_LIMIT` | A kívánt megoldás a céltechnológián nem megvalósítható biztonságosan, és redesign/fallback kell. |
| `RUNTIME_ONLY` | Csak a tényleges Moodle-felületen vagy az élő foglalkozás során állítható elő/ellenőrizhető. |
| `OBSOLETE` | Aktív tananyaghoz már nem szükséges; történeti nyomként marad. |

A két mezőt **együtt** kell olvasni. Például egy `REQUIRED_LATER + BLOCKED_BY_CONSENT` videó fontos lehet a végleges kurzushoz, de ettől még nem blokkolja az első staging pilotot.

## 2. Determinisztikus leképezés a jelenlegi manifesztből

A jelenlegi média-manifeszt státuszai így fordulnak át:

| Manifeszt / feltétel | `production_state` |
|---|---|
| `technical.production_phase = trainer-at-runtime` | `RUNTIME_ONLY` |
| R7, vagy a végleges Moodle-felületből készülő screenshot | `RUNTIME_ONLY` |
| `mode = human-decision` vagy `decision` mező | `BLOCKED_BY_HUMAN_DECISION` |
| R2 vagy R8 jog-/képmás-/hangjog-bizonyíték | `BLOCKED_BY_CONSENT` |
| R3 vagy R5 nyitott produkciós döntés | `BLOCKED_BY_HUMAN_DECISION` |
| bizonyított technikai korlát, amelyhez nincs egyenértékű fallback | `BLOCKED_BY_TECHNICAL_LIMIT` |
| nincs nyitott kapu és a specifikáció kész | `READY_TO_PRODUCE` |
| aktív forrásból eltávolított, legacy-only tétel | `OBSOLETE` |

A `reuse` mód nem új gyártási feladat: az újrahasznosított hely a forrásasset állapotát örökli.

## 3. Első Moodle-szelet: M0 + M1

Az első pilot célja **nem a végleges látvány**, hanem annak bizonyítása, hogy a tanulói út, completion, Assignment, rubrika, kapu, unlock, mobil és hozzáférhetőség ténylegesen működik.

### 3.1. Mi szükséges?

Az M0+M1 első stagingjéhez központilag előgyártott **AI-videó, narráció, illusztráció, ikoncsomag vagy márkázott poszter nem kötelező**.

A szükséges tartalom:
- a leckék szövege és interakciói;
- az M0.2/M0.3/M0.4 működéséhez szükséges natív Moodle/H5P elemek;
- a Bemutatkozó fal;
- az M0 diagnosztikus kvíz;
- az M1 SBI Assignment és a kézzel konfigurált rubrika;
- minden információt hordozó vizuálhoz azonnal használható **szöveges/HTML fallback**.

Ezek Moodle/H5P build-elemek, nem külön vizuális gyártási kapuk.

### 3.2. M0/M1 médiaelemek staging-besorolása

| Médiaosztály | `release_tier` az első stagingre | Szabály |
|---|---|---|
| AI beszélőfej / karaktervideó | `OPTIONAL` | A látható tananyagszöveg és interakció önmagában hordozza a tanulási célt. |
| narráció | `OPTIONAL` | A teljes szöveges változat az alapút; hang nem lehet completion-előfeltétel. |
| díszítő ikon/illusztráció | `OPTIONAL` | Elhagyható. |
| információhordozó diagram | `OPTIONAL` a stagingben | Helyette strukturált HTML/szöveges lista; végleges UX-nél lehet `REQUIRED_LATER`. |
| nyomtatott peula-segédlet | `OPTIONAL` a technikai stagingben | A tényleges offline pilot előtt szükség szerint `REQUIRED_LATER`. |
| H5P-interakció konfigurációja | `REQUIRED_FOR_FIRST_RELEASE` | Natív build-feladat; azonos tanulási céllal más támogatott típussal helyettesíthető. |
| M0.3 Moodle screenshot | `OPTIONAL + RUNTIME_ONLY` | Stagingben szöveges navigáció; a screenshot csak a célfelület stabilizálása után készül. |
| M0.A plakátfotó | `OPTIONAL + RUNTIME_ONLY` | A Z.A visszakötéshez a képzői jegyzet az adatminimalizált fallback. |

**Következmény:** R2, R3 és R5 nyitottsága **nem blokkolja az M0+M1 belső staging pilotot**.

## 4. Teljes learner release

A teljes képzésnél sem lesz automatikusan minden asset `REQUIRED_LATER`.

Egy médiaelem csak akkor kötelező, ha legalább az egyik igaz:
1. olyan tanulási információt hordoz, amelyet a szöveges/HTML út nem ad vissza egyenértékűen;
2. a hozzáférhetőségi alternatíva része;
3. a jóváhagyott pedagógiai terv kifejezetten az adott modalitást méri;
4. az offline peula lebonyolításához ténylegesen szükséges eszköz.

Ha ezek egyike sem igaz, az elem `OPTIONAL`, még akkor is, ha a produkciós tervben legyártandóként szerepel.

## 5. Specifikáció vs. runtime

A média-hozzáférhetőség állapota háromlépcsős:

- `SPEC_OK`: a forrásban megvan a szükséges alt, felirat-, leirat- vagy fallback-követelmény;
- `IMPLEMENTATION_TEST_REQUIRED`: a Moodle/H5P beépítés elkészült, de a tényleges render nincs igazolva;
- `RUNTIME_VERIFIED`: mobilon, billentyűzettel, zoom/reflow-val és szükség szerint segítő technológiával ellenőrizve.

A Markdownból vagy a manifesztből önmagában **nem** következik `RUNTIME_VERIFIED`.

## 6. Első produkciós kör

Ha az M0+M1 staging már működik, az első média-produkciós kör sorrendje:

1. egy hozzáférhető, információhordozó **diagram/HTML-pár** M0-ból;
2. egy M1-es **SBI-vizuál**;
3. csak ezután narrációs pilot;
4. AI beszélőfej csak a hang-, képmás- és szolgáltatói jogok lezárása után.

A cél nem a 417 asset minél gyorsabb legyártása, hanem annak bizonyítása, hogy a vizuális/hangos réteg hozzáad értéket a már működő tanulási úthoz.

## 7. Kapcsolódó emberi döntések

- `HUM-MEDIA-01`: vizuális rendszer;
- `HUM-MEDIA-02`: hangjogosultság és ElevenLabs-hang;
- `HUM-MEDIA-03`: HeyGen/avatar és média-jogok;
- `HUM-PRIV-02`: fotó, videó, hang és kézírás adatkezelése;
- `HUM-A11Y-01`: hozzáférhetőségi jóváhagyó szerepkör.

Ezek közül egyik sem jogosítja fel az implementációs agentet arra, hogy hiányzó nevet, hozzájárulást, voice ID-t, licencet vagy jóváhagyási dátumot kitaláljon.
