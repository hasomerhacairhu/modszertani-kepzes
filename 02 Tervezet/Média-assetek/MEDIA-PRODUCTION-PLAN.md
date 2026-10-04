# 🎬 Média-produkciós terv

**Generált fájl — kézzel ne szerkeszd.** Előállítja:
`python3 tools/media_manifest.py build`. A forrása kizárólag a jelenlegi
leckékben álló `@asset` deklarációk és a `produkcios-szabalyok.json`.

Ez a dokumentum azt mondja meg, **mi gyártható most**, mi mire vár, és
milyen sorrendben éri meg haladni. A nyitott döntések szövege nem itt van:
azokat [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md) tartja
karban. A soronkénti munkalista: `media-production-plan.csv`.

## 1. Készültségi összesítő

| | |
|---|---:|
| Szemantikus asset | **415** |
| ebből újrahasznosítás (nem gyártandó) | 8 |
| ebből élő/runtime tétel (a képző hozza létre a peulán) | 3 |
| Központilag előgyártható asset | **404** |
| Produkciós deliverable | **903** |

### Státusz szerint

| Státusz | Asset | Deliverable |
|---|---:|---:|
| specifikáció kész | 295 | 529 |
| jogtisztázás alatt | 119 | 370 |
| emberi döntésre vár | 1 | 4 |

### Kapuk szerint

| Kapu | Érintett asset |
|---|---:|
| R2 — AI-avatar / AI-hang jogtisztaság | 118 |
| R3 — narrátor hang-bible (motor / voice-ID) | 116 |
| R5 — vizuális rendszer: stílus-token + hex-paletta | 0 |
| R7 — véglegesített Moodle-felület | 1 |
| R8 — GDPR / képmás valós fotón és képernyőképen | 1 |
| nyitott emberi döntés | 1 |
| nincs jóváhagyott felmondható szkript | 0 |

| Kapu-terheltség (központilag előgyártható tételek) | Asset | Deliverable |
|---|---:|---:|
| nincs nyitott kapu | 285 | 526 |
| pontosan EGY kapu | 2 | 4 |
| TÖBB kapu | 117 | 368 |

A kapu-számok és a 2–3. szakasz a **központilag előgyártható** tételekre
vonatkoznak. Az élő/runtime tételek nem kerülnek gyártási sorba — a saját
szakaszukban állnak, a rájuk vonatkozó kapukkal együtt.

## 2. Döntés-hatás — mit szabadít fel egy kapu lezárása?

Az „érintett” és a „ténylegesen felszabaduló” nem ugyanaz: sok asseten
egyszerre több kapu ül. Az utolsó oszlop mutatja, mi marad zárva akkor is,
ha az adott kaput önmagában lezárjuk.

| Kapu | Érintett asset | Érintett deliverable | Önmagában felszabadul (asset) | …deliverable | Más kapu is ül rajta | A többi kapu |
|---|---:|---:|---:|---:|---:|---|
| R5 — vizuális rendszer: stílus-token + hex-paletta | 0 | 0 | **0** | 0 | 0 | — |
| R3 — narrátor hang-bible (motor / voice-ID) | 116 | 366 | **0** | 0 | 116 | OPEN_DECISION×1, R2×116 |
| R2 — AI-avatar / AI-hang jogtisztaság | 118 | 370 | **2** | 4 | 116 | OPEN_DECISION×1, R3×116 |
| R8 — GDPR / képmás valós fotón és képernyőképen | 1 | 2 | **0** | 0 | 1 | R7×1 |
| R7 — véglegesített Moodle-felület | 1 | 2 | **0** | 0 | 1 | R8×1 |
| nyitott emberi döntés | 1 | 4 | **0** | 0 | 1 | R2×1, R3×1 |
| nincs jóváhagyott felmondható szkript | 0 | 0 | **0** | 0 | 0 | — |

## 3. Javasolt sorrend (mohó, újraszámolt marginális haszon)

Minden lépés után újraszámolva: melyik kapu lezárása szabadítja fel a
legtöbb assetet **abban a pillanatban**. Ez nem határidő, hanem
átbocsátóképesség-sorrend.

| # | Kapu | Ekkor felszabaduló asset | …deliverable | Halmozott gyártható asset |
|---:|---|---:|---:|---:|
| 1 | R2 — AI-avatar / AI-hang jogtisztaság | 2 | 4 | 287 |
| 2 | R3 — narrátor hang-bible (motor / voice-ID) | 115 | 362 | 402 |
| 3 | nyitott emberi döntés | 1 | 4 | 403 |
| 4 | nincs jóváhagyott felmondható szkript | 0 | 0 | 403 |
| 5 | R5 — vizuális rendszer: stílus-token + hex-paletta | 0 | 0 | 403 |
| 6 | R7 — véglegesített Moodle-felület | 0 | 0 | 403 |
| 7 | R8 — GDPR / képmás valós fotón és képernyőképen | 1 | 2 | 404 |

## 4. Kötegek

Egy asset **pontosan egy** kötegbe kerül, és a köteg neve azt mondja meg,
melyik az **utolsó** kapuja — nem azt, hogy csak arra vár. Ha egy tételen
több kapu ül, mindegyiknek le kell zárulnia; a „Kapuk” oszlop ezért mindig
a teljes listát mutatja. Például egy R3 + R5 tétel a hang-zár kötegében áll,
de a vizuális rendszer lezárása nélkül akkor sem gyártható.

Az utolsó szakasz nem köteg: azokat a tételeket gyűjti, amelyeket a képző a
peula alatt hoz létre, tehát előre egyáltalán nem gyárthatók.

| Köteg | Függőség | Asset | Deliverable |
|---|---|---:|---:|
| **BATCH 0 — MOST GYÁRTHATÓ** | nincs nyitott kapu | 285 | 526 |
| **BATCH 1 — VIZUÁLIS RENDSZER ZÁRÁSA UTÁN** | R5 — vizuális rendszer lock | 0 | 0 |
| **BATCH 2 — HANG-ZÁR UTÁN** | R3 — narrátor-hang lock | 0 | 0 |
| **BATCH 3 — AI-AVATAR, KARAKTERVIDEÓ ÉS SZINTETIKUS HANG** | R2 + R3 — avatar- és hang-jogtisztaság, hang-lock | 117 | 366 |
| **BATCH 4 — JOGÉRZÉKENY (valós fotó / képernyőkép)** | R8 — képmás- és adatvédelmi bizonyíték | 0 | 0 |
| **BATCH 5 — RUNTIME-KÉPERNYŐKÉP** | R7 (+ R8) — éles Moodle-felület | 1 | 2 |
| **BATCH 6 — EMBERI DÖNTÉS / SZKRIPT-ZÁR** | szerzői/szakmai döntés vagy jóváhagyott szkript | 1 | 4 |
| **ÉLŐ / RUNTIME DELIVERABLE — A KÉPZŐ HOZZA LÉTRE A PEULÁN** | magára a peulára — előre nem gyártható | 3 | 5 |

### BATCH 0 — MOST GYÁRTHATÓ

**Függőség:** nincs nyitott kapu · **285 asset / 526 deliverable**

A másolat és a specifikáció kész. Két dolgot érdemes tudni: a szabad
szöveges H5P elemek megvalósítási típusát az `LMS – H5P runtime acceptance.md`
6. pontja a célverzión eldöntendőnek nevezi, és a teljes environment record
is kitöltetlen — ez a köteget nem gátolja, de a végleges beépítés előtt
tisztázandó.

| Modul | Típus | Asset | Deliverable |
|---|---|---:|---:|
| M0 | card-set | 2 | 4 |
| M0 | diagram | 4 | 8 |
| M0 | icon-set | 5 | 10 |
| M0 | illustration | 3 | 6 |
| M0 | other | 1 | 1 |
| M0 | poster | 3 | 6 |
| M0 | worksheet | 3 | 6 |
| M1 | card-set | 2 | 4 |
| M1 | diagram | 7 | 14 |
| M1 | icon-set | 6 | 10 |
| M1 | illustration | 5 | 9 |
| M1 | other | 1 | 1 |
| M1 | poster | 5 | 10 |
| M1 | worksheet | 6 | 12 |
| M2 | card-set | 4 | 8 |
| M2 | diagram | 4 | 8 |
| M2 | icon-set | 5 | 9 |
| M2 | illustration | 6 | 12 |
| M2 | other | 3 | 3 |
| M2 | photo | 1 | 2 |
| M2 | poster | 4 | 8 |
| M2 | worksheet | 6 | 13 |
| M3 | card-set | 5 | 10 |
| M3 | diagram | 6 | 12 |
| M3 | icon-set | 8 | 15 |
| M3 | illustration | 8 | 16 |
| M3 | other | 10 | 10 |
| M3 | poster | 3 | 6 |
| M3 | print | 2 | 2 |
| M3 | worksheet | 6 | 12 |
| M4 | card-set | 1 | 2 |
| M4 | diagram | 5 | 10 |
| M4 | icon-set | 4 | 7 |
| M4 | illustration | 5 | 10 |
| M4 | other | 5 | 5 |
| M4 | poster | 4 | 8 |
| M4 | print | 2 | 2 |
| M4 | worksheet | 8 | 16 |
| M5 | card-set | 3 | 6 |
| M5 | diagram | 3 | 6 |
| M5 | icon-set | 3 | 5 |
| M5 | illustration | 4 | 8 |
| M5 | other | 2 | 2 |
| M5 | poster | 3 | 6 |
| M5 | print | 1 | 1 |
| M5 | worksheet | 8 | 16 |
| M6 | diagram | 3 | 6 |
| M6 | icon-set | 4 | 7 |
| M6 | illustration | 7 | 14 |
| M6 | other | 11 | 11 |
| M6 | poster | 6 | 12 |
| M6 | print | 1 | 1 |
| M6 | worksheet | 11 | 23 |
| M7 | card-set | 3 | 6 |
| M7 | diagram | 6 | 12 |
| M7 | icon-set | 3 | 6 |
| M7 | illustration | 6 | 12 |
| M7 | poster | 7 | 14 |
| M7 | worksheet | 11 | 23 |
| Z | card-set | 3 | 6 |
| Z | diagram | 1 | 2 |
| Z | icon-set | 2 | 4 |
| Z | illustration | 2 | 4 |
| Z | poster | 1 | 2 |
| Z | worksheet | 2 | 4 |

A 285 tétel soronként a
`media-production-plan.csv` fájlban van (`Köteg` oszlop = `B0`).

### BATCH 1 — VIZUÁLIS RENDSZER ZÁRÁSA UTÁN

**Függőség:** R5 — vizuális rendszer lock · **0 asset / 0 deliverable**

_Üres._

### BATCH 2 — HANG-ZÁR UTÁN

**Függőség:** R3 — narrátor-hang lock · **0 asset / 0 deliverable**

_Üres._

### BATCH 3 — AI-AVATAR, KARAKTERVIDEÓ ÉS SZINTETIKUS HANG

**Függőség:** R2 + R3 — avatar- és hang-jogtisztaság, hang-lock · **117 asset / 366 deliverable**

| Modul | Típus | Asset | Deliverable |
|---|---|---:|---:|
| M1 | video | 3 | 10 |
| M1 | voiceover | 21 | 62 |
| M2 | video | 6 | 25 |
| M2 | voiceover | 9 | 27 |
| M3 | video | 4 | 18 |
| M3 | voiceover | 11 | 30 |
| M4 | photo | 2 | 4 |
| M4 | video | 5 | 14 |
| M4 | voiceover | 17 | 51 |
| M5 | video | 2 | 8 |
| M5 | voiceover | 1 | 3 |
| M6 | video | 3 | 12 |
| M6 | voiceover | 17 | 51 |
| M7 | video | 3 | 12 |
| M7 | voiceover | 11 | 33 |
| Z | voiceover | 2 | 6 |

A 117 tétel soronként a
`media-production-plan.csv` fájlban van (`Köteg` oszlop = `B3`).

### BATCH 4 — JOGÉRZÉKENY (valós fotó / képernyőkép)

**Függőség:** R8 — képmás- és adatvédelmi bizonyíték · **0 asset / 0 deliverable**

_Üres._

### BATCH 5 — RUNTIME-KÉPERNYŐKÉP

**Függőség:** R7 (+ R8) — éles Moodle-felület · **1 asset / 2 deliverable**

| Asset | Típus | Deliverable | Kapuk | Cím |
|---|---|---:|---|---|
| `M0.3-FOTO-01` | photo | 2 | R7, R8 | Moodle-kurzus főoldal screenshot (modul-lista) |

### BATCH 6 — EMBERI DÖNTÉS / SZKRIPT-ZÁR

**Függőség:** szerzői/szakmai döntés vagy jóváhagyott szkript · **1 asset / 4 deliverable**

| Asset | Típus | Deliverable | Kapuk | Cím |
|---|---|---:|---|---|
| `M1.3-VID-01` | video/interactive | 4 | OPEN_DECISION, R2, R3 | HOOK Interactive Video – ugyanaz a helyzet kétféle visszajelzéssel |

### ÉLŐ / RUNTIME DELIVERABLE — A KÉPZŐ HOZZA LÉTRE A PEULÁN

**Függőség:** magára a peulára — előre nem gyártható · **3 asset / 5 deliverable**

| Asset | Típus | Deliverable | Kapuk | Cím |
|---|---|---:|---|---|
| `M0.A-EGY-01` | other | 1 | — | Zárókör induló-szavainak rögzítése (képzői jegyzet a Z.A-hoz) |
| `M0.A-FOTO-01` | photo | 2 | R8 | Kvuca-plakátok archív fotói (Z.A modulhoz) |
| `Z.A-KART-04` | card-set | 2 | — | M0-tükör név nélküli idézet-kártyák (M0.A kickoff visszakötés) |

## 5. Pilot-tételek

Minden produkciós családban **egy** tétel készül el először, és azt kell
jóváhagyni, mielőtt a testvérei elindulnak. A választás szabálya rögzített:
a legkevesebb nyitott kapuval bíró tételek közül a **medián hosszúságú**
specifikációjú — se a leghiányosabb brief, se a legbonyolultabb darab.

| Család | Pilot | Köteg | Kapuk | Család mérete | Cím |
|---|---|---|---|---:|---|
| Narráció / hang | `M3.4-NAR-02` | B3 | R2, R3 | 89 | Outro narráció (opcionális) – SLIDE 7 |
| AI beszélőfej-videó | `M2.2-VID-01` | B3 | R2, R3 | 18 | Hook-videó: „A kvucád 15 percet késik…” |
| AI karakter- / jelenetvideó | `M4.1-VID-05` | B3 | R2, R3 | 9 | Jelenet 3 karaktervideó – „Nyitott, stabil madrih” |
| Diagram / ábra | `M1.B-DIA-01` | B0 | — | 39 | Szerepcsere-ábra (A→C, C→B, B→A forgás) |
| Ikon-készlet | `M4.3-IKO-01` | B0 | — | 40 | Kérdéstípus szín-ikon készlet (4 db) |
| Illusztráció | `M3.3-ILL-02` | B0 | — | 46 | Jelenet – Branching 2: sértő mém a csoportchatben |
| Munkalap / nyomtatvány | `Z.A-MUNK-01` | B0 | — | 61 | Híd a terepre – kétoszlopos poszter-sablon |
| Poszter és kártyaszett | `M5.B-KART-01` | B0 | — | 59 | Indítósor-kártyaszett (6-8 db kész táblázat-sor) |
| Fotó / képernyőkép | `M2.3-FOTO-01` | B0 | — | 4 | Hook háttér – someres/kvuca-vizuál |
| H5P-interakció / Moodle-elem | `M3.4-EGY-03` | B0 | — | 27 | H5P Drag and Drop (két célzóna) – „OK / Nem OK madrihként” (SLIDE 4) |
| Beszerzendő fizikai eszköz | `M5-HUB-EGY-01` | B0 | — | 6 | Galériaséta reakció-eszközök (post-it / pötty-matrica) |

## 6. Újrahasznosítás — nem gyártandó

Ezek a tételek nem hoznak létre új deliverable-t: a kanonikus asset
legyártásával elkészülnek.

| Asset | Kanonikus forrás | Modul |
|---|---|---|
| `M1-HUB-KART-01` | `M1.A-MUNK-01` | M1 |
| `M1.4-IKO-01` | `M1.3-IKO-01` | M1 |
| `M3-HUB-POSZ-01` | `M3.B-MUNK-01` | M3 |
| `M6-HUB-MUNK-01` | `M6.B-MUNK-01` | M6 |
| `M6.3-FOTO-02` | `M6.3-FOTO-03` | M6 |
| `M6.F-MUNK-02` | `M6.B-MUNK-01` | M6 |
| `M7.4-IKO-01` | `M3.2-IKO-01` | M7 |
| `Z-HUB-POSZ-02` | `Z.A-POSZ-01` | Z |

## 7. Mi NEM ebben a fájlban dől el

- A kapuk szövege és a hiányzó érték: `produkcios-szabalyok.json`.
- A nyitott emberi döntések: [`PRODUCTION-DECISIONS.md`](./PRODUCTION-DECISIONS.md).
- A narrátor-hang követelményei: [`VOICE-BIBLE.md`](./VOICE-BIBLE.md).
- A vizuális rendszer nyitott értékei: [`VISUAL-SYSTEM-DECISION.md`](./VISUAL-SYSTEM-DECISION.md).
- A jogi bizonyíték-nyilvántartás: [`RIGHTS-EVIDENCE.md`](./RIGHTS-EVIDENCE.md).
- A kurzus release-állapota: `02 Tervezet/RELEASE-READINESS.md`.

