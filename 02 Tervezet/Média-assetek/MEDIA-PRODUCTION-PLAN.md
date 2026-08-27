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
| Szemantikus asset | **418** |
| ebből újrahasznosítás (nem gyártandó) | 7 |
| Produkciós deliverable | **906** |

### Státusz szerint

| Státusz | Asset | Deliverable |
|---|---:|---:|
| produkciós szabályra vár | 339 | 760 |
| specifikáció kész | 46 | 39 |
| jogtisztázás alatt | 29 | 98 |
| blokkolt | 2 | 6 |
| emberi döntésre vár | 2 | 3 |

### Kapuk szerint

| Kapu | Érintett asset |
|---|---:|
| R2 — AI-avatar / AI-hang jogtisztaság | 28 |
| R3 — narrátor hang-bible (motor / voice-ID) | 118 |
| R5 — vizuális rendszer: stílus-token + hex-paletta | 258 |
| R7 — véglegesített Moodle-felület | 1 |
| R8 — GDPR / képmás valós fotón és képernyőképen | 2 |
| nyitott emberi döntés | 4 |
| nincs jóváhagyott felmondható szkript | 2 |

| Kapu-terheltség | Asset | Deliverable |
|---|---:|---:|
| nincs nyitott kapu | 39 | 39 |
| pontosan EGY kapu | 339 | 760 |
| TÖBB kapu | 33 | 107 |

## 2. Döntés-hatás — mit szabadít fel egy kapu lezárása?

Az „érintett” és a „ténylegesen felszabaduló” nem ugyanaz: sok asseten
egyszerre több kapu ül. Az utolsó oszlop mutatja, mi marad zárva akkor is,
ha az adott kaput önmagában lezárjuk.

| Kapu | Érintett asset | Érintett deliverable | Önmagában felszabadul (asset) | …deliverable | Más kapu is ül rajta | A többi kapu |
|---|---:|---:|---:|---:|---:|---|
| R5 — vizuális rendszer: stílus-token + hex-paletta | 258 | 509 | **248** | 491 | 10 | MISSING_SPOKEN_SOURCE×1, OPEN_DECISION×3, R2×7, R3×6 |
| R3 — narrátor hang-bible (motor / voice-ID) | 118 | 365 | **90** | 267 | 28 | MISSING_SPOKEN_SOURCE×2, OPEN_DECISION×2, R2×26, R5×6 |
| R2 — AI-avatar / AI-hang jogtisztaság | 28 | 97 | **0** | 0 | 28 | MISSING_SPOKEN_SOURCE×1, OPEN_DECISION×1, R3×26, R5×7 |
| R8 — GDPR / képmás valós fotón és képernyőképen | 2 | 4 | **1** | 2 | 1 | R7×1 |
| R7 — véglegesített Moodle-felület | 1 | 2 | **0** | 0 | 1 | R8×1 |
| nyitott emberi döntés | 4 | 9 | **0** | 0 | 4 | MISSING_SPOKEN_SOURCE×2, R2×1, R3×2, R5×3 |
| nincs jóváhagyott felmondható szkript | 2 | 6 | **0** | 0 | 2 | OPEN_DECISION×2, R2×1, R3×2, R5×1 |

## 3. Javasolt sorrend (mohó, újraszámolt marginális haszon)

Minden lépés után újraszámolva: melyik kapu lezárása szabadítja fel a
legtöbb assetet **abban a pillanatban**. Ez nem határidő, hanem
átbocsátóképesség-sorrend.

| # | Kapu | Ekkor felszabaduló asset | …deliverable | Halmozott gyártható asset |
|---:|---|---:|---:|---:|
| 1 | R5 — vizuális rendszer: stílus-token + hex-paletta | 248 | 491 | 287 |
| 2 | R3 — narrátor hang-bible (motor / voice-ID) | 91 | 269 | 378 |
| 3 | R2 — AI-avatar / AI-hang jogtisztaság | 27 | 94 | 405 |
| 4 | nyitott emberi döntés | 2 | 3 | 407 |
| 5 | nincs jóváhagyott felmondható szkript | 2 | 6 | 409 |
| 6 | R8 — GDPR / képmás valós fotón és képernyőképen | 1 | 2 | 410 |
| 7 | R7 — véglegesített Moodle-felület | 1 | 2 | 411 |

## 4. Kötegek

Egy asset **pontosan egy** kötegbe kerül, és a köteg neve azt mondja meg,
melyik az **utolsó** kapuja — nem azt, hogy csak arra vár. Ha egy tételen
több kapu ül, mindegyiknek le kell zárulnia; a „Kapuk” oszlop ezért mindig
a teljes listát mutatja. Például egy R3 + R5 tétel a hang-zár kötegében áll,
de a vizuális rendszer lezárása nélkül akkor sem gyártható.

| Köteg | Függőség | Asset | Deliverable |
|---|---|---:|---:|
| **BATCH 0 — MOST GYÁRTHATÓ** | nincs nyitott kapu | 39 | 39 |
| **BATCH 1 — VIZUÁLIS RENDSZER ZÁRÁSA UTÁN** | R5 — vizuális rendszer lock | 248 | 491 |
| **BATCH 2 — HANG-ZÁR UTÁN** | R3 — narrátor-hang lock | 91 | 269 |
| **BATCH 3 — AI-AVATAR ÉS KARAKTERVIDEÓ** | R2 + R3 — avatar-jogtisztaság és hang-lock | 27 | 94 |
| **BATCH 4 — JOGÉRZÉKENY (valós fotó / képernyőkép)** | R8 — képmás- és adatvédelmi bizonyíték | 1 | 2 |
| **BATCH 5 — RUNTIME-KÉPERNYŐKÉP** | R7 (+ R8) — éles Moodle-felület | 1 | 2 |
| **BATCH 6 — EMBERI DÖNTÉS / SZKRIPT-ZÁR** | szerzői/szakmai döntés vagy jóváhagyott szkript | 4 | 9 |

### BATCH 0 — MOST GYÁRTHATÓ

**Függőség:** nincs nyitott kapu · **39 asset / 39 deliverable**

| Asset | Típus | Deliverable | Kapuk | Cím |
|---|---|---:|---|---|
| `M0.2-EGY-01` | other/h5p-interaction | 1 | — | Akadálymentes iframe-cím és fókusz-spec a SLIDE 3 interakcióhoz |
| `M0.A-EGY-01` | other | 1 | — | Zárókör induló-szavainak rögzítése (képzői jegyzet a Z.A-hoz) |
| `M2.3-EGY-01` | other/h5p-interaction | 1 | — | Hook Single Choice poll – "Melyik pillérhez érzed a legerősebb kapcsolatot?" |
| `M2.3-EGY-02` | other/h5p-interaction | 1 | — | H5P Branching Scenario – 3 pillér döntés-fa (a lecke magja) |
| `M2.3-EGY-03` | other/h5p-interaction | 1 | — | SLIDE CHECK mini-kvíz – 2× Single Choice (fogalmi rögzítés) |
| `M3.2-EGY-01` | other/h5p-interaction | 1 | — | Matching jelenet-feladat (H5P Matching/Drag&Drop, 7 jelenet + 4 kvuca-címke) |
| `M3.2-EGY-02` | other/h5p-interaction | 1 | — | Húzás-mentes Matching alternatíva (Single Choice Set / legördülős) |
| `M3.4-EGY-01` | other/h5p-interaction | 1 | — | Single Choice interakció – „Mennyire érzed fontosnak…” (SLIDE 1) |
| `M3.4-EGY-02` | other/h5p-interaction | 1 | — | Mini True/False interakció – szigorúbb határok (SLIDE 2) |
| `M3.4-EGY-03` | other/h5p-interaction | 1 | — | H5P Sorting / Drag & Drop – „OK / Nem OK madrichként” (SLIDE 4) |
| `M3.4-EGY-04` | other/h5p-interaction | 1 | — | Húzás-mentes a11y-alternatíva – Single Choice/Matching (SLIDE 4) |
| `M3.4-EGY-05` | other/h5p-interaction | 1 | — | H5P Question Set – mini-kvíz 3 kérdés (SLIDE 6) |
| `M3.4-EGY-06` | other/h5p-interaction | 1 | — | Szabad szöveges reflexiós mező – „Saját Do/Don’t listám” (SLIDE 5) |
| `M3.4-EGY-07` | other/moodle-activity | 1 | — | Moodle Assignment-sablon – „Helyzetleírás red flag-ekkel” (SLIDE 7 / modulproduktum) |
| `M3.4-EGY-08` | other | 1 | — | Moodle intro Label/oldal – „0. lépés” a lecke előtt (lecke-keret) |
| `M3.F-EGY-01` | print/consumable | 1 | — | Check-in matrica / post-it készlet |
| `M3.F-EGY-02` | print/consumable | 1 | — | Filcek a fogalom-térkép-táblához |
| `M4.2-EGY-01` | other/h5p-interaction | 1 | — | H5P Single Choice – „Mi lenne az első reakciód?” (helyzetfelmérés) |
| `M4.2-EGY-02` | other/h5p-interaction | 1 | — | H5P Dialog Cards készlet – „Melyik segít jobban?” |
| `M4.2-EGY-03` | other/h5p-interaction | 1 | — | H5P Drag&Drop / Sorting – „Lezáró vagy támogató?” |
| `M4.2-EGY-04` | other/h5p-interaction | 1 | — | H5P mini-quiz – 2 Single Choice kérdés (Check) |
| `M4.2-EGY-05` | other/h5p-interaction | 1 | — | 2× szabad szöveges mező – reflektív kérdések (visszatükröző mondat + elhagyandó mondat) |
| `M4.F-EGY-01` | print/consumable | 1 | — | Check-in matricák / post-it készlet (1 db/fő) |
| `M4.F-EGY-02` | print/consumable | 1 | — | Filc-/marker-készlet a fogalom-térkép táblához |
| `M5-HUB-EGY-01` | print/consumable | 1 | — | Gallery walk reakció-eszközök (post-it / pötty-matrica) |
| `M5.1-EGY-01` | other/ui-text | 1 | — | Provenance-címke – AI-generált avatar / AI-elemek jelölés |
| `M5.3-EGY-01` | other/h5p-interaction | 1 | — | Dialog Cards Leitner-pakli (Repetition mód) – akadálymentes interaktív elem |
| `M6.1-EGY-01` | other/ui-text | 1 | — | AI-provenance ember-olvasható sor (lecke alján/dián) |
| `M6.1-EGY-02` | other/h5p-interaction | 1 | — | Single Choice – önreflexió: „mi alapján döntesz?” |
| `M6.1-EGY-03` | other/h5p-interaction | 1 | — | Single Choice – „Névkör labdával” korosztály |
| `M6.1-EGY-04` | other/h5p-interaction | 1 | — | Single Choice – 11–13 bizalomjáték forma |
| `M6.1-EGY-05` | other/h5p-interaction | 1 | — | Szabad szöveges kérdés – kockázat bizalomjátékban |
| `M6.1-EGY-06` | other/h5p-interaction | 1 | — | Single Choice – 6–10 reflexiós vs. mély |
| `M6.1-EGY-07` | other/h5p-interaction | 1 | — | Single Choice – Szitu 1 korosztály-választás |
| `M6.1-EGY-08` | other/h5p-interaction | 1 | — | Szabad szöveges kérdés – Szitu 2 futkosós energizer kockázata + safety-keret |
| `M6.1-EGY-09` | other/h5p-interaction | 1 | — | Single Choice – miért hasznos kategóriákban gondolkodni |
| `M6.1-EGY-10` | other/h5p-interaction | 1 | — | Single Choice – mikor ne hozz mély élményjátékot |
| `M6.1-EGY-11` | other/h5p-interaction | 1 | — | Szabad szöveges mező – záró mini-reflexió (kedvenc játék + kockázat) |
| `M6.F-EGY-01` | print/consumable | 1 | — | Check-in matricák / post-it készlet (beszerzendő irodaszer) |

### BATCH 1 — VIZUÁLIS RENDSZER ZÁRÁSA UTÁN

**Függőség:** R5 — vizuális rendszer lock · **248 asset / 491 deliverable**

Az R5 két külön dolgot tart nyitva: a **stílus-tokent** (tipográfia,
elrendezés, margók, jelölés) és a **hex-palettát**. Amelyik tétel a saját
technikai jegyzete szerint fekete-fehérben is nyomtatható és nem nevez meg
színt, az csak a stílus-tokenre vár — az a paletta-vita előtt is indulhat.

| Alköteg | Asset | Deliverable |
|---|---:|---:|
| 1A — fekete-fehér is elég | 26 | 54 |
| 1B — nincs kimondva | 205 | 404 |
| 1C — színfüggő | 17 | 33 |

| Modul | Típus | Asset | Deliverable |
|---|---|---:|---:|
| M0 | card-set | 2 | 4 |
| M0 | diagram | 4 | 8 |
| M0 | icon-set | 5 | 10 |
| M0 | illustration | 3 | 6 |
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
| M2 | photo | 1 | 2 |
| M2 | poster | 4 | 8 |
| M2 | worksheet | 6 | 13 |
| M3 | card-set | 5 | 10 |
| M3 | diagram | 6 | 12 |
| M3 | icon-set | 8 | 16 |
| M3 | illustration | 8 | 16 |
| M3 | poster | 4 | 8 |
| M3 | worksheet | 6 | 12 |
| M4 | card-set | 1 | 2 |
| M4 | diagram | 5 | 10 |
| M4 | icon-set | 4 | 7 |
| M4 | illustration | 4 | 8 |
| M4 | poster | 4 | 8 |
| M4 | worksheet | 8 | 16 |
| M5 | card-set | 3 | 6 |
| M5 | diagram | 3 | 6 |
| M5 | icon-set | 3 | 5 |
| M5 | illustration | 4 | 8 |
| M5 | poster | 3 | 6 |
| M5 | worksheet | 8 | 16 |
| M6 | diagram | 3 | 6 |
| M6 | icon-set | 4 | 7 |
| M6 | illustration | 7 | 14 |
| M6 | poster | 6 | 12 |
| M6 | worksheet | 11 | 23 |
| M7 | card-set | 3 | 6 |
| M7 | diagram | 6 | 12 |
| M7 | icon-set | 3 | 6 |
| M7 | illustration | 6 | 12 |
| M7 | poster | 7 | 14 |
| M7 | worksheet | 11 | 23 |
| Z | card-set | 4 | 8 |
| Z | diagram | 1 | 2 |
| Z | icon-set | 2 | 4 |
| Z | illustration | 2 | 4 |
| Z | poster | 1 | 2 |
| Z | worksheet | 2 | 4 |

A 248 tétel soronként a
`media-production-plan.csv` fájlban van (`Köteg` oszlop = `B1`).

### BATCH 2 — HANG-ZÁR UTÁN

**Függőség:** R3 — narrátor-hang lock · **91 asset / 269 deliverable**

| Modul | Típus | Asset | Deliverable |
|---|---|---:|---:|
| M1 | video | 1 | 2 |
| M1 | voiceover | 20 | 60 |
| M2 | voiceover | 9 | 27 |
| M3 | voiceover | 11 | 30 |
| M4 | voiceover | 17 | 51 |
| M5 | voiceover | 2 | 6 |
| M6 | voiceover | 17 | 51 |
| M7 | voiceover | 12 | 36 |
| Z | voiceover | 2 | 6 |

A 91 tétel soronként a
`media-production-plan.csv` fájlban van (`Köteg` oszlop = `B2`).

### BATCH 3 — AI-AVATAR ÉS KARAKTERVIDEÓ

**Függőség:** R2 + R3 — avatar-jogtisztaság és hang-lock · **27 asset / 94 deliverable**

| Asset | Típus | Deliverable | Kapuk | Cím |
|---|---|---:|---|---|
| `M1.1-VID-01` | video/ai-talking-head | 4 | R2, R3 | HOOK AI beszélő fej – „Mondtak már rólad mást?” |
| `M1.2-VID-01` | video/ai-talking-head | 4 | R2, R3 | HOOK beszélő fej – "Bunkó voltál" vs. "Háromszor közbevágott" |
| `M2.1-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook beszélő fej – „Te mitől vagy someres?” |
| `M2.2-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook-videó: „A kvucád 15 percet késik…” |
| `M2.2-VID-02` | video/ai-talking-head | 4 | R2, R3 | Outro – beszélő fej / köszönőkártya (Slide 8) |
| `M2.3-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook AI beszélő-fej videó – 3 pillér felvezetés |
| `M2.3-VID-02` | video/ai-talking-head | 4 | R2, R3 | Outro AI beszélő-fej videó (opcionális, INFERÁLT forma) – záró keret + híd M2.4-re |
| `M2.4-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook – késő esti krízis-üzenet beszélő fej |
| `M3.1-VID-01` | video/ai-talking-head | 4 | R2, R3 | HOOK beszélő fej – három kvuca-sztori |
| `M3.2-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook beszélő fej – 4 kvuca, 4 hangulat |
| `M3.3-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook beszélő fej – „Mit ígérhetek egy chanichnak?” |
| `M3.4-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook beszélő fej – „Meddig mehetek el madrichként?” |
| `M4.1-FOTO-01` | photo | 2 | R2, R5 | Képpár 1 freeze-frame – karba tett kéz vs. nyitott kéz |
| `M4.1-FOTO-02` | photo | 2 | R2, R5 | Képpár 2 freeze-frame – földre nézés vs. körre nézés |
| `M4.1-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook beszélő-fej videó – „Mit gondolnak rólad az első 5 másodpercben?” |
| `M4.1-VID-02` | video/interactive | 3 | R2, R3, R5 | Interactive Video – 3 madrich-kiállás mini-jelenettel + beágyazott kérdések |
| `M4.1-VID-03` | video/explainer | 1 | R2, R3, R5 | Jelenet 1 karaktervideó – „Jegyzetbe bújó madrich” |
| `M4.1-VID-04` | video/explainer | 1 | R2, R3, R5 | Jelenet 2 karaktervideó – „Ideges topogó madrich” |
| `M4.1-VID-05` | video/explainer | 1 | R2, R3, R5 | Jelenet 3 karaktervideó – „Nyitott, stabil madrich” |
| `M5.1-VID-01` | video/ai-talking-head | 4 | R2, R3 | HOOK beszélő fej – suli / somer / random |
| `M5.1-VID-02` | video/ai-talking-head | 4 | R2, R3 | OUTRO beszélő fej thumbnail (opcionális) |
| `M6.1-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook beszélőfej-videó – „Volt már olyan, hogy nem ült a játék?” |
| `M6.2-VID-01` | video/ai-talking-head | 4 | R2, R3 | Hook – AI beszélő fej: „fagyott csend lett a sztoritól?” |
| `M6.2-VID-02` | video/ai-talking-head | 4 | R2, R3 | Opcionális beszélő fej / narrációs videó – „Az új lány a körben” (1. rész) |
| `M7.2-VID-01` | video/ai-talking-head | 4 | R2, R3 | HOOK – AI beszélő fej: „Csak játék maradt a peula?” |
| `M7.3-VID-01` | video/ai-talking-head | 4 | R2, R3 | HOOK beszélő-fej: „Zmán Kvucá = csak programidő…?” |
| `M7.4-VID-01` | video/ai-talking-head | 4 | R2, R3 | HOOK – AI beszélő fej: papíron szép vs. vállalható peula |

### BATCH 4 — JOGÉRZÉKENY (valós fotó / képernyőkép)

**Függőség:** R8 — képmás- és adatvédelmi bizonyíték · **1 asset / 2 deliverable**

| Asset | Típus | Deliverable | Kapuk | Cím |
|---|---|---:|---|---|
| `M0.A-FOTO-01` | photo | 2 | R8 | Kvuca-plakátok archív fotói (Z.A modulhoz) |

### BATCH 5 — RUNTIME-KÉPERNYŐKÉP

**Függőség:** R7 (+ R8) — éles Moodle-felület · **1 asset / 2 deliverable**

| Asset | Típus | Deliverable | Kapuk | Cím |
|---|---|---:|---|---|
| `M0.3-FOTO-01` | photo | 2 | R7, R8 | Moodle kurzus főoldal screenshot (modul-lista) |

### BATCH 6 — EMBERI DÖNTÉS / SZKRIPT-ZÁR

**Függőség:** szerzői/szakmai döntés vagy jóváhagyott szkript · **4 asset / 9 deliverable**

| Asset | Típus | Deliverable | Kapuk | Cím |
|---|---|---:|---|---|
| `M1.3-VID-01` | video/interactive | 3 | MISSING_SPOKEN_SOURCE, OPEN_DECISION, R2, R3, R5 | HOOK Interactive Video – ugyanaz a helyzet kétféle visszajelzéssel |
| `M3-HUB-POSZ-01` | poster | 1 | OPEN_DECISION, R5 | Gyermekvédelmi lépés-térkép poszter (észreveszem → jelzek → nem maradok egyedül → bevonás) |
| `M3.2-NAR-02` | voiceover/narration | 3 | MISSING_SPOKEN_SOURCE, OPEN_DECISION, R3 | Input 1 opcionális narráció |
| `M4.2-ILL-01` | illustration | 2 | OPEN_DECISION, R5 | Hook chat-buborék: ideges peula-mondat |

## 5. Pilot-tételek

Minden produkciós családban **egy** tétel készül el először, és azt kell
jóváhagyni, mielőtt a testvérei elindulnak. A választás szabálya rögzített:
a legkevesebb nyitott kapuval bíró tételek közül a **medián hosszúságú**
specifikációjú — se a leghiányosabb brief, se a legbonyolultabb darab.

| Család | Pilot | Köteg | Kapuk | Család mérete | Cím |
|---|---|---|---|---:|---|
| Narráció / hang | `M4.2-NAR-03` | B2 | R3 | 91 | Slide 3 narráció – Dialog Cards felvezetés |
| AI beszélőfej-videó | `M5.1-VID-01` | B3 | R2, R3 | 21 | HOOK beszélő fej – suli / somer / random |
| AI karakter- / jelenetvideó | `M1.1-VID-02` | B2 | R3, R5 | 6 | Mini storyboard / B-roll – kvuca-szituk a példákhoz |
| Diagram / ábra | `M5.2-DIA-02` | B1 | R5 | 39 | Döntési fa térkép – 4 ág + közös visszacsatlakozás |
| Ikon-készlet | `M0.2-IKO-02` | B1 | R5 | 40 | SLIDE 5 dugma ishit ikonok: kör / chat / kulissza |
| Illusztráció | `M4.2-ILL-03` | B1 | R5 | 46 | Outro összegző checklist vizuál |
| Munkalap / nyomtatvány | `M6.A-MUNK-02` | B1 | R5 | 61 | Képzői checklist – „Játék-labor 4 kvucára” (1 oldalas cheat-sheet) |
| Poszter és kártyaszett | `M7.B-POSZ-01` | B1 | R5 | 62 | Flipchart-poszter: "Zmán Kvucá = …" definíció + "AI-határok" |
| Fotó / képernyőkép | `M2.3-FOTO-01` | B1 | R5 | 5 | Hook háttér – someres/kvuca-vizuál |
| H5P-interakció / Moodle-elem | `M4.2-EGY-02` | B0 | — | 29 | H5P Dialog Cards készlet – „Melyik segít jobban?” |
| Beszerzendő fizikai eszköz | `M3.F-EGY-01` | B0 | — | 6 | Check-in matrica / post-it készlet |

## 6. Újrahasznosítás — nem gyártandó

Ezek a tételek nem hoznak létre új deliverable-t: a kanonikus asset
legyártásával elkészülnek.

| Asset | Kanonikus forrás | Modul |
|---|---|---|
| `M1-HUB-KART-01` | `M1.A-MUNK-01` | M1 |
| `M1.4-IKO-01` | `M1.3-IKO-01` | M1 |
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

