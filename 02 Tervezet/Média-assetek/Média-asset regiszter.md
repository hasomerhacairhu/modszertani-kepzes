# 🎬 Média-asset regiszter — Hasomer Hacair madrichképzés

> **Ez a fájl generált.** Forrás: a `02 Tervezet/` alatti leckefájlok rejtett
> `@asset` deklarációi és `@source` blokkjai. Ne szerkeszd kézzel —
> `python3 tools/media_manifest.py build` állítja elő.
>
> **Mi ez?** A teljes produkciós leltár: szemantikus assetek (amit a szerző
> megfogalmaz) és az ezekből származó konkrét deliverable-ek (amit a produkció
> legyárt) — narráció, videó, animáció, illusztráció, ikon, fotó, hang,
> felirat, leirat, alt-szöveg, valamint a nyomtatható és letölthető anyagok.
>
> A **felmondandó és az alt-szöveg minden buildnél élőben** a leckefájlból
> származik, nem kifagyasztott pillanatképből.

## 📊 Összesítő

| Mutató | Érték |
|---|--:|
| Feldolgozott forrásfájl | **84** |
| Assetet tartalmazó fájl | 65 |
| Ellenőrzötten asset nélküli fájl | 19 |
| Forrásblokk (`@source`) | 121 |
| Szemantikus asset | **418** |
| Produkciós deliverable | **913** |

**Produkciós mód szerint**

| Mód | Db |
|---|--:|
| legyártandó | 403 |
| újrahasznosítás | 7 |
| külső forrás | 6 |
| emberi döntés kell | 2 |

**Asset-típus szerint**

| Típus | Db |
|---|--:|
| voiceover | 91 |
| worksheet | 63 |
| illustration | 47 |
| icon-set | 42 |
| diagram | 39 |
| poster | 39 |
| other | 34 |
| video | 27 |
| card-set | 25 |
| print | 6 |
| photo | 5 |

**Deliverable-szerep szerint**

| Szerep | Db |
|---|--:|
| elsődleges | 411 |
| alt-szöveg | 123 |
| nyomtatható PDF | 122 |
| leirat | 118 |
| felirat | 115 |
| felmondott hang | 21 |
| szerkeszthető, kitölthető változat | 3 |

**Modul szerint**

| Modul | Db |
|---|--:|
| M0 | 24 |
| M1 | 58 |
| M2 | 48 |
| M3 | 66 |
| M4 | 58 |
| M5 | 31 |
| M6 | 66 |
| M7 | 52 |
| Z | 15 |

**Státusz szerint**

| Státusz | Db |
|---|--:|
| produkciós szabályra vár | 343 |
| specifikáció kész | 41 |
| jogtisztázás alatt | 32 |
| emberi döntésre vár | 2 |

**Nyitott produkciós blokkolók (hivatkozások szerint)**

| Blokkoló | Érintett asset |
|---|--:|
| R5 | 248 |
| R3 | 118 |
| R2 | 21 |
| R8 | 11 |
| R7 | 1 |

## ⛔ Nyitott produkciós kapuk

Ezek **szervezeti és jogi döntések**. Amíg nyitva vannak, a jelölt
assetek kötegelt gyártása nem indulhat. A jelölés gépileg is
detektálható, ezért a `content_integrity.py --release-report` számolja.

| Szabály | Mi hiányzik | Érintett asset |
|---|---|--:|
| **R2** — AI-avatar / AI-hang IP-megfelelőség | A konkrét licenc-igazolás ⟬KITÖLTENDŐ⟭ (szervezeti/jogi) | 21 |
| **R3** — Narrátor hang-bible | a konkrét TTS-motor / voice-ID ⟬KITÖLTENDŐ⟭ | 118 |
| **R5** — Ikon- és karakter-batch + lock | A konkrét someres hex-paletta ⟬KITÖLTENDŐ⟭ | 248 |

## 🗂 Assetek fájlonként

### 02 Tervezet/Modulok/M0/Online leckék/M0.1 – Üdv a képzésben! – Éves útiterv & mi köze hozzám.md

*Egység:* `M0.1` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M0.1-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Éves útiterv timeline (M0→M7→Z) | — | alt-szöveg | AI-generált |
| `M0.1-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Hook-ikon: útiterv / térkép / lépcső | — | alt-szöveg | AI-generált |
| `M0.1-IKO-02` | icon-set | legyártandó | produkciós szabályra vár | 3 ígéret-ikon (kézfogás, létra, pajzs) | — | alt-szöveg | AI-generált |

### 02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrich, nem terapeuta – szerepek és elvárások.md

*Egység:* `M0.2` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M0.2-DIA-01` | diagram | legyártandó | produkciós szabályra vár | SLIDE 4 jelzési folyamatábra: észreveszem → nem maradok egyedül → jelzek → támogatást kapunk | — | alt-szöveg | AI-generált |
| `M0.2-DIA-02` | diagram | legyártandó | produkciós szabályra vár | SLIDE 2 kétoszlopos összevetés: „Madrichként csinálom" vs. „Nem (csak) az én feladatom" | — | alt-szöveg | AI-generált |
| `M0.2-EGY-01` | other/h5p-interaction | legyártandó | specifikáció kész | Akadálymentes iframe-cím és fókusz-spec a SLIDE 3 interakcióhoz | — | — | emberi |
| `M0.2-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | SLIDE 1 hook-ikonok: barát / tanár / szuperhős | — | alt-szöveg | AI-generált |
| `M0.2-IKO-02` | icon-set | legyártandó | produkciós szabályra vár | SLIDE 5 dugma ishit ikonok: kör / chat / kulissza | — | alt-szöveg | AI-generált |

### 02 Tervezet/Modulok/M0/Online leckék/M0.3 – Hogyan működik a Moodle, H5P és a gate.md

*Egység:* `M0.3` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M0.3-FOTO-01` | photo | legyártandó | jogtisztázás alatt | Moodle kurzus főoldal screenshot (modul-lista) | — | alt-szöveg | emberi |

### 02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma ishit az online térben + bemutatkozó fórum.md

*Egység:* `M0.4` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M0.4-DIA-01` | diagram | legyártandó | produkciós szabályra vár | 3 egyszerű online szabály – kártyás összegző diagram | — | alt-szöveg | AI-generált |
| `M0.4-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Online-felület ikonkészlet (chat / insta / messenger / Moodle-komment) | — | alt-szöveg | AI-generált |
| `M0.4-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Hook-vizuál: a kvuca online terei a telefonon | — | alt-szöveg | AI-generált |
| `M0.4-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Online szituációk – 4 problémahelyzet jelenetképe | — | alt-szöveg | AI-generált |
| `M0.4-ILL-03` | illustration | legyártandó | produkciós szabályra vár | „Dugma ishit vagy sem?” – 3 döntéshelyzet vizuál | — | alt-szöveg | AI-generált |
| `M0.4-POSZ-01` | poster | legyártandó | produkciós szabályra vár | „3 egyszerű szabály online” – nyomtatható poszter/kártya | — | nyomtatható PDF | AI-generált |

### 02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md

*Egység:* `M0.A` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M0.A-EGY-01` | other | legyártandó | specifikáció kész | Zárókör induló-szavainak rögzítése (képzői jegyzet a Z.A-hoz) | — | — | emberi |
| `M0.A-FOTO-01` | photo | legyártandó | jogtisztázás alatt | Kvuca-plakátok archív fotói (Z.A modulhoz) | — | alt-szöveg | emberi |
| `M0.A-KART-01` | card-set | legyártandó | produkciós szabályra vár | Red-flag mini-protokoll kártya a képzőnek | — | nyomtatható PDF | vegyes |
| `M0.A-KART-02` | card-set | legyártandó | produkciós szabályra vár | Képzői safety-mondatok kártya | — | nyomtatható PDF | vegyes |
| `M0.A-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Kvuca-plakát 3 rubrikás sablon (Mit várok / Mitől félek / Mit hozok) | — | nyomtatható PDF | vegyes |
| `M0.A-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Exit ticket cetli – 2 kérdéses sablon | — | nyomtatható PDF | vegyes |
| `M0.A-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Moodle-belépési segédlet (papír helpdesk-kézirat) | — | nyomtatható PDF | vegyes |
| `M0.A-POSZ-01` | poster | legyártandó | produkciós szabályra vár | „KÖZÖS KERET" 2 oszlopos flipchart-sablon | — | nyomtatható PDF | vegyes |
| `M0.A-POSZ-02` | poster | legyártandó | produkciós szabályra vár | „Kihez fordulhatok?" támasz-térkép sablon (buborékábra) | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, feedback – Önismeret & visszajelzés – Johari + SBI.md

*Egység:* `M1-HUB` · *típus:* hub

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M1-HUB-KART-01` | card-set | újrahasznosítás | specifikáció kész | M1.A 'Megfigyelés vagy címkézés?' kártyaszett | — | — | vegyes |
| `M1-HUB-POSZ-02` | poster | legyártandó | produkciós szabályra vár | M1.F Közös fogalom-térkép sablon | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M1/Online leckék/M1.1 – Johari-ablak – vakfoltjaim felismerése.md

*Egység:* `M1.1` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M1.1-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Animált Johari-ablak diagram (4 mező felvillan) | — | alt-szöveg | AI-generált |
| `M1.1-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | 4 mező-ikon a példa-gridhez (dekoratív) | — | — | AI-generált |
| `M1.1-IKO-02` | icon-set | legyártandó | produkciós szabályra vár | Önreflexió-ikon (gondolkodó figura / napló) | — | alt-szöveg | AI-generált |
| `M1.1-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Üres 4 ablakos Johari-váz grafika (címke nélkül) | — | alt-szöveg | AI-generált |
| `M1.1-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Példa-grid (4 mező) ikonokkal – 4 hétköznapi példa | — | — | AI-generált |
| `M1.1-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – Safety / érzelmi check-in | `M1.1-NAR-02-VO` | felirat, leirat | AI-generált |
| `M1.1-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – „Mi az a Johari-ablak?” (4 mező) | `M1.1-NAR-03-VO` | felirat, leirat | AI-generált |
| `M1.1-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – Példák a 4 mezőre | `M1.1-NAR-04-VO` | felirat, leirat | AI-generált |
| `M1.1-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – Önreflexió bevezető (opcionális) | `M1.1-NAR-05-VO` | felirat, leirat | AI-generált |
| `M1.1-NAR-06` | voiceover/narration | legyártandó | produkciós szabályra vár | Záró narráció – outro + átvezetés M1.2-re | `M1.1-NAR-06-VO` | felirat, leirat | AI-generált |
| `M1.1-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | HOOK AI beszélő fej – „Mondtak már rólad mást?” | `M1.1-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |
| `M1.1-VID-02` | video/explainer | legyártandó | produkciós szabályra vár | Mini storyboard / B-roll – kvuca-szituk a példákhoz | — | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M1/Online leckék/M1.2 – Megfigyelés ≠ értelmezés.md

*Egység:* `M1.2` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M1.2-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Megfigyelés vs. értelmezés – kétoszlopos animált grafika | — | alt-szöveg | AI-generált |
| `M1.2-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Ikonok a megfigyelés/értelmezés példákhoz | — | alt-szöveg | AI-generált |
| `M1.2-IKO-02` | icon-set | legyártandó | produkciós szabályra vár | Helyzet-piktogramok – iskola / ken / család | — | alt-szöveg | AI-generált |
| `M1.2-IKO-03` | icon-set | legyártandó | produkciós szabályra vár | Drop-zóna ikonok – szem (megfigyelés) / maszk (értelmezés) | — | — | AI-generált |
| `M1.2-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Két chat-buborék – "Bunkó voltál" / "Háromszor közbevágott" | — | alt-szöveg | AI-generált |
| `M1.2-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Storyboard – 3 kontextus kártya (iskola / ken / család) | — | alt-szöveg | AI-generált |
| `M1.2-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | INPUT narráció – definíciók (kamera-teszt) | `M1.2-NAR-02-VO` | felirat, leirat | AI-generált |
| `M1.2-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | INPUT 2 narráció – hétköznapi példák (suli/ken/otthon) | `M1.2-NAR-03-VO` | felirat, leirat | AI-generált |
| `M1.2-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Mark the Words instrukció-narráció (opcionális) | `M1.2-NAR-04-VO` | felirat, leirat | AI-generált |
| `M1.2-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Drag & Drop instrukció-narráció (opcionális) | `M1.2-NAR-05-VO` | felirat, leirat | AI-generált |
| `M1.2-NAR-06` | voiceover/narration | legyártandó | produkciós szabályra vár | OUTRO záró narráció – híd az SBI-hez | `M1.2-NAR-06-VO` | felirat, leirat | AI-generált |
| `M1.2-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | HOOK beszélő fej – "Bunkó voltál" vs. "Háromszor közbevágott" | `M1.2-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M1/Online leckék/M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md

*Egység:* `M1.3` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M1.3-DIA-01` | diagram | legyártandó | produkciós szabályra vár | S = Situation magyarázó grafika | — | alt-szöveg | AI-generált |
| `M1.3-DIA-02` | diagram | legyártandó | produkciós szabályra vár | B = Behavior magyarázó grafika | — | alt-szöveg | AI-generált |
| `M1.3-DIA-03` | diagram | legyártandó | produkciós szabályra vár | I = Impact magyarázó grafika (+ pozitív SBI keret) | — | alt-szöveg | AI-generált |
| `M1.3-EGY-01` | other | legyártandó | specifikáció kész | Videó-belső verziócímkék overlay (1. verzió / 2. verzió) | — | — | AI-generált |
| `M1.3-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | SBI vizuális kód ikon-készlet (S/B/I) | — | alt-szöveg | AI-generált |
| `M1.3-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | S = Situation narráció (20–30 mp) | `M1.3-NAR-01-VO` | felirat, leirat | AI-generált |
| `M1.3-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | B = Behavior narráció (20–30 mp) | `M1.3-NAR-02-VO` | felirat, leirat | AI-generált |
| `M1.3-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | I = Impact narráció (20–30 mp) | `M1.3-NAR-03-VO` | felirat, leirat | AI-generált |
| `M1.3-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Activity 1 (vezetett SBI) narráció (15–20 mp) | `M1.3-NAR-04-VO` | felirat, leirat | AI-generált |
| `M1.3-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Activity 2 (saját mini-SBI) narráció (20–30 mp) | `M1.3-NAR-05-VO` | felirat, leirat | AI-generált |
| `M1.3-NAR-06` | voiceover/narration | legyártandó | produkciós szabályra vár | Self-check narráció (10–15 mp) | `M1.3-NAR-06-VO` | felirat, leirat | AI-generált |
| `M1.3-NAR-07` | voiceover/narration | legyártandó | produkciós szabályra vár | Zárószöveg narráció (10–15 mp) | `M1.3-NAR-07-VO` | felirat, leirat | AI-generált |
| `M1.3-VID-01` | video/interactive | legyártandó | produkciós szabályra vár | HOOK Interactive Video – ugyanaz a helyzet kétféle visszajelzéssel | — | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M1/Online leckék/M1.4 – Miniszituációk – Mondd el SBI-ben.md

*Egység:* `M1.4` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M1.4-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Slide 2 – S/B/I emlékeztető diagram ikonokkal | — | alt-szöveg | AI-generált |
| `M1.4-IKO-01` | icon-set | újrahasznosítás | specifikáció kész | S/B/I ikonok (óra+helyszín, szem/fül, szív/hullám) | — | — | AI-generált |
| `M1.4-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Slide 1 – 3 szituáció-kártya vizuál | — | alt-szöveg | AI-generált |
| `M1.4-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 1 Hook-narráció – 3 helyzet bemutatása | `M1.4-NAR-01-VO` | felirat, leirat | AI-generált |
| `M1.4-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 2 narráció – SBI emlékeztető | `M1.4-NAR-02-VO` | felirat, leirat | AI-generált |
| `M1.4-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 6 átvezető narráció – beadandóra hívás | `M1.4-NAR-03-VO` | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M1/Peulák/M1.A – Önismeret & Johari + megfigyelés vs. címkézés (45’).md

*Egység:* `M1.A` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M1.A-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Képzői segédlet: „Megfigyelés vagy címkézés?” – 8 példamondat + várt besorolás | — | nyomtatható PDF | vegyes |
| `M1.A-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Képzői segédlet: „Magunkat is címkézzük?” – saját-cetli példák + megfigyeléssé átírás | — | nyomtatható PDF | vegyes |
| `M1.A-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Johari-ablak nagy tábla-/flipchart-sablon | — | nyomtatható PDF | vegyes |
| `M1.A-POSZ-02` | poster | legyártandó | produkciós szabályra vár | „MEGFIGYELÉS” sarok-poszter (👁️) | — | nyomtatható PDF | vegyes |
| `M1.A-POSZ-03` | poster | legyártandó | produkciós szabályra vár | „CÍMKE / ÉRTELMEZÉS” sarok-poszter (🎭) | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M1/Peulák/M1.B – SBI-lab – Smiley-tól a használható visszajelzésig (45’).md

*Egység:* `M1.B` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M1.B-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Szerepcsere-ábra (A→C, C→B, B→A forgás) | — | alt-szöveg | AI-generált |
| `M1.B-KART-01` | card-set | legyártandó | produkciós szabályra vár | Helyzetkártya-szett (SBI szerepjáték) | — | nyomtatható PDF | emberi |
| `M1.B-KART-02` | card-set | legyártandó | produkciós szabályra vár | Smiley-kártyák (😃 / 😐 / 😬) | — | nyomtatható PDF | emberi |
| `M1.B-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Trió-checklist lap a megfigyelőnek (C) | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M1/Peulák/M1.F – Felzárkóztató peula – Johari, megfigyelés és SBI egyben (45’).md

*Egység:* `M1.F` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M1.F-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Offline B-terv – 1 oldalas M1.1–M1.4 összefoglaló kártya | — | nyomtatható PDF | AI-generált |
| `M1.F-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Jegyzetlap – „1 mondat + 1 kérdés” | — | nyomtatható PDF | AI-generált |
| `M1.F-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist – „Peula előtt / közben / után” (1 A4) | — | nyomtatható PDF | AI-generált |
| `M1.F-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Flipchart-sablon – „Melyik leckénél tartasz?” 5 soros állapot-tábla | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M2/M2 – Ki vagyok madrichként – Identitás, Somer-értékek és dugma ishit.md

*Egység:* `M2-HUB` · *típus:* hub

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M2-HUB-DIA-01` | diagram | legyártandó | produkciós szabályra vár | M2 modul fogalom-térkép (identitás–értékek–pillérek–határok & személyes példamutatás) | — | alt-szöveg | AI-generált |

### 02 Tervezet/Modulok/M2/Online leckék/M2.1 – Ki vagyok én madrichként – identitás-körök.md

*Egység:* `M2.1` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M2.1-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Identitás-körök koncentrikus diagram (animált) | — | alt-szöveg | AI-generált |
| `M2.1-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Outro ikon – kvuca-kör + next nyíl | — | alt-szöveg | AI-generált |
| `M2.1-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Három jelenet – helyzetek illusztráció (SLIDE 3) | — | alt-szöveg | AI-generált |
| `M2.1-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – identitás-körök bevezetés (SLIDE 2) | `M2.1-NAR-02-VO` | felirat, leirat | AI-generált |
| `M2.1-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – helyzetek és körök (SLIDE 3) | `M2.1-NAR-03-VO` | felirat, leirat | AI-generált |
| `M2.1-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Outro narráció – lezárás + híd M2.2-re | `M2.1-NAR-04-VO` | felirat, leirat | AI-generált |
| `M2.1-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook beszélő fej – „Te mitől vagy someres?” | `M2.1-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M2/Online leckék/M2.2 – Értékeim mint iránytű.md

*Egység:* `M2.2` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M2.2-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Ikon-készlet – „Mi az, hogy érték?” bulletpontokhoz | — | — | AI-generált |
| `M2.2-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Statikus illusztráció (videó-alternatíva) – késő, szétesett kvuca | — | alt-szöveg | AI-generált |
| `M2.2-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Érték-szófelhő (14 értékkel) | — | alt-szöveg | AI-generált |
| `M2.2-ILL-03` | illustration | legyártandó | produkciós szabályra vár | Köszönőkártya (outro, videó-alternatíva) | — | alt-szöveg | AI-generált |
| `M2.2-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – „Mi az, hogy érték?” (Slide 2) | `M2.2-NAR-02-VO` | felirat, leirat | AI-generált |
| `M2.2-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – szófelhő (Slide 3) | `M2.2-NAR-03-VO` | felirat, leirat | AI-generált |
| `M2.2-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook-videó: „A kvucád 15 percet késik…” | `M2.2-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |
| `M2.2-VID-02` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Outro – beszélő fej / köszönőkártya (Slide 8) | `M2.2-VID-02-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M2/Online leckék/M2.3 – Somer 3 pillére – mini-kapszula.md

*Egység:* `M2.3` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M2.3-EGY-01` | other/h5p-interaction | legyártandó | specifikáció kész | Hook Single Choice poll – "Melyik pillérhez érzed a legerősebb kapcsolatot?" | — | — | vegyes |
| `M2.3-EGY-02` | other/h5p-interaction | legyártandó | specifikáció kész | H5P Branching Scenario – 3 pillér döntés-fa (a lecke magja) | — | — | vegyes |
| `M2.3-EGY-03` | other/h5p-interaction | legyártandó | specifikáció kész | SLIDE CHECK mini-kvíz – 2× Single Choice (fogalmi rögzítés) | — | — | vegyes |
| `M2.3-FOTO-01` | photo | legyártandó | jogtisztázás alatt | Hook háttér – someres/kvuca-vizuál | — | alt-szöveg | AI-generált |
| `M2.3-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | 3 pillér ikon-készlet (cionizmus / szocializmus / humanista zsidóság) | — | alt-szöveg | AI-generált |
| `M2.3-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | KERET narráció – "Ez a három pillér sokkal több, mint három szó" | `M2.3-NAR-02-VO` | felirat, leirat | AI-generált |
| `M2.3-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook AI beszélő-fej videó – 3 pillér felvezetés | `M2.3-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |
| `M2.3-VID-02` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Outro AI beszélő-fej videó (opcionális, INFERÁLT forma) – záró keret + híd M2.4-re | `M2.3-VID-02-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma ishit nem terapeuta.md

*Egység:* `M2.4` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M2.4-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Privát – Személyes – Szakmai 3 oszlopos vizuál | — | alt-szöveg | AI-generált |
| `M2.4-DIA-02` | diagram | legyártandó | produkciós szabályra vár | 3 oszlopos „kinek mit mondok el” tábla-vizuál | — | alt-szöveg | AI-generált |
| `M2.4-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Madrich + felnőtt/szervezet támogató ikon | — | alt-szöveg | AI-generált |
| `M2.4-IKO-02` | icon-set | legyártandó | produkciós szabályra vár | Napló ikon (Activity 1) | — | alt-szöveg | AI-generált |
| `M2.4-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Chat-buborékok háttér (hook) | — | alt-szöveg | AI-generált |
| `M2.4-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Chat-buborék illusztráció (Activity 3 – vissza az üzenethez) | — | alt-szöveg | AI-generált |
| `M2.4-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Safety & keret narráció (opcionális) | `M2.4-NAR-02-VO` | felirat, leirat | AI-generált |
| `M2.4-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Privát–személyes–szakmai narráció | `M2.4-NAR-03-VO` | felirat, leirat | AI-generált |
| `M2.4-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Záró narráció (Check & Outro) | `M2.4-NAR-04-VO` | felirat, leirat | AI-generált |
| `M2.4-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook – késő esti krízis-üzenet beszélő fej | `M2.4-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M2/Peulák/M2.A – Identitás-körök élőben – mit mutatok magamból (45’).md

*Egység:* `M2.A` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M2.A-KART-01` | card-set | legyártandó | produkciós szabályra vár | Identitás-vonal állítás-kártyák (8 db szett) | — | nyomtatható PDF | emberi |
| `M2.A-KART-03` | card-set | legyártandó | produkciós szabályra vár | Kiscsoportos feldolgozás – beszélgetőkérdés-kártya / facilitátor-segédlet (4 kérdés) | — | nyomtatható PDF | emberi |
| `M2.A-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Identitás-térkép munkalap (ÉN + körök) | — | nyomtatható PDF, szerkeszthető, kitölthető változat | emberi |
| `M2.A-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Megosztási szabályok flipchart-sablon (kettős funkció: közös minták gyűjtéséhez is) | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M2/Peulák/M2.B – Somer-értékek a gyakorlatban – döntések, amelyek tanítanak.md

*Egység:* `M2.B` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M2.B-KART-01` | card-set | legyártandó | produkciós szabályra vár | Érték-sziget kártyaszett (4 db A3) | — | nyomtatható PDF | vegyes |
| `M2.B-KART-02` | card-set | legyártandó | produkciós szabályra vár | Storyboard-feladat instrukciós kártya | — | nyomtatható PDF | vegyes |
| `M2.B-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | A/B kép storyboard nagylap-sablon (flipchart) | — | nyomtatható PDF | vegyes |
| `M2.B-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist – 1 A4 sablon | — | nyomtatható PDF | vegyes |
| `M2.B-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Egyéni reflexió + commit munkalap (A5) | — | nyomtatható PDF | vegyes |
| `M2.B-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Somer-pillér poszterszett (3 db A3) | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M2/Peulák/M2.F – Felzárkóztató peula – Identitás, értékek, pillérek, személyes példamutatás (Study Lab).md

*Egység:* `M2.F` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M2.F-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Study Lab jegyzetlap – „1 gondolat / 1 kérdés leckénként” | — | nyomtatható PDF | emberi |
| `M2.F-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist – Felzárkóztató peula (1 A4) | — | nyomtatható PDF | emberi |
| `M2.F-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Állapotfelmérő tábla / flipchart-sablon – „Melyik leckénél tartasz?” | — | nyomtatható PDF | emberi |
| `M2.F-POSZ-02` | poster | legyártandó | produkciós szabályra vár | Fogalom-térkép flipchart-sablon – 4 buborék (identitás–értékek–pillérek–határok) | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md

*Egység:* `M3-HUB` · *típus:* hub

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M3-HUB-POSZ-01` | poster | emberi döntés kell | emberi döntésre vár | Gyermekvédelmi lépés-térkép poszter (észreveszem → jelzek → nem maradok egyedül → bevonás) | — | — | vegyes |
| `M3-HUB-POSZ-02` | poster | legyártandó | produkciós szabályra vár | A/B sarok jelölőtáblák („Red flag” / „Nem red flag”) | — | nyomtatható PDF | AI-generált |

### 02 Tervezet/Modulok/M3/Online leckék/M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md

*Egység:* `M3.1` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M3.1-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Tuckman-görbe animált diagram (5 szakasz) | — | alt-szöveg | AI-generált |
| `M3.1-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Reflexiós ikon – kvuca-kör / beszélgető figurák (dekoratív) | — | alt-szöveg | AI-generált |
| `M3.1-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Kvuca-jelenet – Forming (alakulás) | — | alt-szöveg | AI-generált |
| `M3.1-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Kvuca-jelenet – Storming (balhék) | — | alt-szöveg | AI-generált |
| `M3.1-ILL-03` | illustration | legyártandó | produkciós szabályra vár | Kvuca-jelenet – Norming (szabályok) | — | alt-szöveg | AI-generált |
| `M3.1-ILL-04` | illustration | legyártandó | produkciós szabályra vár | Kvuca-jelenet – Performing (működés) | — | alt-szöveg | AI-generált |
| `M3.1-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | INPUT 1 narráció – Tuckman 4+1 szakasz | `M3.1-NAR-02-VO` | felirat, leirat | AI-generált |
| `M3.1-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | INPUT 2 narráció – „Milyen érzés benne lenni?” | `M3.1-NAR-03-VO` | felirat, leirat | AI-generált |
| `M3.1-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Reflexió narráció (opcionális) | `M3.1-NAR-04-VO` | felirat, leirat | AI-generált |
| `M3.1-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Outro narráció – átvezetés M3.2-re | `M3.1-NAR-05-VO` | felirat, leirat | AI-generált |
| `M3.1-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | HOOK beszélő fej – három kvuca-sztori | `M3.1-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan, Zorea – 4 kvuca, 4 világ.md

*Egység:* `M3.2` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M3.2-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Parparim & Kivsza – kétoszlopos profilkártya | — | alt-szöveg | AI-generált |
| `M3.2-DIA-02` | diagram | legyártandó | produkciós szabályra vár | Leviatan & Zorea – kétoszlopos profilkártya | — | alt-szöveg | AI-generált |
| `M3.2-DIA-03` | diagram | legyártandó | produkciós szabályra vár | 4 kulcsszó-kártya (2×2 rács) | — | alt-szöveg | AI-generált |
| `M3.2-DIA-04` | diagram | legyártandó | produkciós szabályra vár | Korosztály-térkép mini-táblázat (4 sor) | — | alt-szöveg | AI-generált |
| `M3.2-EGY-01` | other/h5p-interaction | legyártandó | specifikáció kész | Matching jelenet-feladat (H5P Matching/Drag&Drop, 7 jelenet + 4 kvuca-címke) | — | — | AI-generált |
| `M3.2-EGY-02` | other/h5p-interaction | legyártandó | specifikáció kész | Húzás-mentes Matching alternatíva (Single Choice Set / legördülős) | — | — | AI-generált |
| `M3.2-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | 4 kvuca ikon-készlet (🦋 🐑 🐋 🌱) | — | alt-szöveg | AI-generált |
| `M3.2-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Input 1 opcionális narráció | — | felirat, leirat | AI-generált |
| `M3.2-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Parparim & Kivsza opcionális narráció | `M3.2-NAR-03-VO` | felirat, leirat | AI-generált |
| `M3.2-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Leviatan & Zorea opcionális narráció | `M3.2-NAR-04-VO` | felirat, leirat | AI-generált |
| `M3.2-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Outro narráció hangsáv | `M3.2-NAR-05-VO` | felirat, leirat | AI-generált |
| `M3.2-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook beszélő fej – 4 kvuca, 4 hangulat | `M3.2-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M3/Online leckék/M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md

*Egység:* `M3.3` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M3.3-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Ikon-készlet – Gyermekvédelem 4 pontja | — | alt-szöveg | AI-generált |
| `M3.3-IKO-02` | icon-set | legyártandó | produkciós szabályra vár | Piktogramok – Red flag példák | — | alt-szöveg | AI-generált |
| `M3.3-IKO-03` | icon-set | legyártandó | produkciós szabályra vár | Védelem ikon – pajzs/szív (reflexió) | — | alt-szöveg | AI-generált |
| `M3.3-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Jelenet – Branching 1: késő esti privát üzenet | — | alt-szöveg | AI-generált |
| `M3.3-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Jelenet – Branching 2: sértő mém a csoportchatben | — | alt-szöveg | AI-generált |
| `M3.3-ILL-03` | illustration | legyártandó | produkciós szabályra vár | Jelenet – Branching 3: vágásnyomok táborban | — | alt-szöveg | AI-generált |
| `M3.3-ILL-04` | illustration | legyártandó | produkciós szabályra vár | Jelenet – Branching 4: madrich–chanich kapcsolat gyanú | — | alt-szöveg | AI-generált |
| `M3.3-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – „Mi az a gyermekvédelem?” (4 pont) | `M3.3-NAR-01-VO` | leirat | AI-generált |
| `M3.3-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – Reflexió bevezető (opcionális) | `M3.3-NAR-02-VO` | leirat | AI-generált |
| `M3.3-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – Outro / lecke lezárás | `M3.3-NAR-03-VO` | leirat | AI-generált |
| `M3.3-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook beszélő fej – „Mit ígérhetek egy chanichnak?” | `M3.3-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrichként – határok, red flag-ek és modulproduktum.md

*Egység:* `M3.4` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M3.4-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Do/Don’t három témablokk – minibox-pár diagram (SLIDE 3) | — | alt-szöveg | AI-generált |
| `M3.4-EGY-01` | other/h5p-interaction | legyártandó | specifikáció kész | Single Choice interakció – „Mennyire érzed fontosnak…” (SLIDE 1) | — | — | AI-generált |
| `M3.4-EGY-02` | other/h5p-interaction | legyártandó | specifikáció kész | Mini True/False interakció – szigorúbb határok (SLIDE 2) | — | — | AI-generált |
| `M3.4-EGY-03` | other/h5p-interaction | legyártandó | specifikáció kész | H5P Sorting / Drag & Drop – „OK / Nem OK madrichként” (SLIDE 4) | — | — | AI-generált |
| `M3.4-EGY-04` | other/h5p-interaction | legyártandó | specifikáció kész | Húzás-mentes a11y-alternatíva – Single Choice/Matching (SLIDE 4) | — | — | AI-generált |
| `M3.4-EGY-05` | other/h5p-interaction | legyártandó | specifikáció kész | H5P Question Set – mini-kvíz 3 kérdés (SLIDE 6) | — | — | AI-generált |
| `M3.4-EGY-06` | other/h5p-interaction | legyártandó | specifikáció kész | Szabad szöveges reflexiós mező – „Saját Do/Don’t listám” (SLIDE 5) | — | — | AI-generált |
| `M3.4-EGY-07` | other/moodle-activity | legyártandó | specifikáció kész | Moodle Assignment-sablon – „Helyzetleírás red flag-ekkel” (SLIDE 7 / modulproduktum) | — | — | AI-generált |
| `M3.4-EGY-08` | other | legyártandó | specifikáció kész | Moodle intro Label/oldal – „0. lépés” a lecke előtt (lecke-keret) | — | — | AI-generált |
| `M3.4-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Ikon: madrich + kvuca stilizált „határvonallal” (SLIDE 2) | — | alt-szöveg | AI-generált |
| `M3.4-IKO-02` | icon-set | legyártandó | produkciós szabályra vár | Lista-ikon – Saját Do/Don’t lista reflexió (SLIDE 5) | — | alt-szöveg | AI-generált |
| `M3.4-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Outro narráció (opcionális) – SLIDE 7 | `M3.4-NAR-02-VO` | felirat, leirat | AI-generált |
| `M3.4-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook beszélő fej – „Meddig mehetek el madrichként?” | `M3.4-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M3/Peulák/M3.A – Találd ki, hol tart a kvuca! – Történetek Tuckman szemüvegén át.md

*Egység:* `M3.A` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M3.A-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Tuckman-szakasz ikonok (4 db) | — | alt-szöveg | AI-generált |
| `M3.A-KART-01` | card-set | legyártandó | produkciós szabályra vár | Tuckman-szakasz kártyaszett (4 db) | — | nyomtatható PDF | vegyes |
| `M3.A-KART-02` | card-set | legyártandó | produkciós szabályra vár | Kvuca-sztori kártyaszett – fix 8 db nyomtatható szett | — | nyomtatható PDF | vegyes |
| `M3.A-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Megoldókulcs a képzőnek (kártya-hátlapok) | — | nyomtatható PDF | vegyes |
| `M3.A-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Tuckman-idővonal flipchart-sablon ikonokkal | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépés-térkép.md

*Egység:* `M3.B` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M3.B-KART-01` | card-set | legyártandó | produkciós szabályra vár | Szituáció-kártyák (4 db red flag eset) | — | nyomtatható PDF | emberi |
| `M3.B-KART-02` | card-set | legyártandó | produkciós szabályra vár | Krízis- / segélyvonal referenciakártya (képzőnek) | — | nyomtatható PDF | emberi |
| `M3.B-KART-03` | card-set | emberi döntés kell | emberi döntésre vár | Képzői safety-gyorskártya | — | nyomtatható PDF | emberi |
| `M3.B-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Lépés-térkép flipchart-sablon (5 lépéses folyamatábra) | — | nyomtatható PDF | emberi |
| `M3.B-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Helyi gyermekvédelmi útvonal lap (szerep + név + elérhetőség) | — | nyomtatható PDF | emberi |
| `M3.B-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Képzői megoldó-jegyzet kártyánként (4 soros referenciatáblázat) | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M3/Peulák/M3.F – Felzárkóztató peula – Kvucadinamika & gyermekvédelem (Study Lab).md

*Egység:* `M3.F` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M3.F-EGY-01` | print/consumable | külső forrás | jogtisztázás alatt | Check-in matrica / post-it készlet | — | — | stock |
| `M3.F-EGY-02` | print/consumable | külső forrás | jogtisztázás alatt | Filcek a fogalom-térkép-táblához | — | — | stock |
| `M3.F-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Jegyzetlap – „1 gondolat / 1 kérdés leckénként” | — | nyomtatható PDF | AI-generált |
| `M3.F-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist – M3.F peula (1 A4) | — | nyomtatható PDF | AI-generált |
| `M3.F-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Check-in állapotfelmérő tábla – M3 leckesorok | — | nyomtatható PDF | AI-generált |
| `M3.F-POSZ-02` | poster | legyártandó | produkciós szabályra vár | Fogalom-térkép alaplap – 4–5 üres buborék | — | nyomtatható PDF | AI-generált |

### 02 Tervezet/Modulok/M4/Online leckék/M4.1 – Mit üzen a testem – Nonverbális kiállás.md

*Egység:* `M4.1` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M4.1-DIA-01` | diagram | legyártandó | produkciós szabályra vár | 3-ikonos „belevillanó” keret-grafika – Testtartás / Tekintet / Térfoglalás | — | alt-szöveg | AI-generált |
| `M4.1-FOTO-01` | photo | legyártandó | jogtisztázás alatt | Képpár 1 freeze-frame – karba tett kéz vs. nyitott kéz | — | alt-szöveg | AI-generált |
| `M4.1-FOTO-02` | photo | legyártandó | jogtisztázás alatt | Képpár 2 freeze-frame – földre nézés vs. körre nézés | — | alt-szöveg | AI-generált |
| `M4.1-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | AI-eredet címke ikon/badge a Hook videóhoz | — | alt-szöveg | AI-generált |
| `M4.1-IKO-02` | icon-set | legyártandó | produkciós szabályra vár | 3 fókusz-ikon: Testtartás, Tekintet, Térfoglalás | — | alt-szöveg | AI-generált |
| `M4.1-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 2 narráció – „3 dolog, ami azonnal látszik rajtad” | `M4.1-NAR-02-VO` | felirat, leirat | AI-generált |
| `M4.1-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Jelenet 1 narráció – „Jegyzetbe bújó madrich” | `M4.1-NAR-03-VO` | felirat, leirat | AI-generált |
| `M4.1-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Jelenet 2 narráció – „Ideges topogó madrich” | `M4.1-NAR-04-VO` | felirat, leirat | AI-generált |
| `M4.1-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Jelenet 3 narráció – „Nyitott, stabil madrich” | `M4.1-NAR-05-VO` | felirat, leirat | AI-generált |
| `M4.1-NAR-06` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 4 közös bevezető narráció – „Mi a különbség?” | `M4.1-NAR-06-VO` | felirat, leirat | AI-generált |
| `M4.1-NAR-07` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 6 outro narráció – „Mire figyelek legközelebb?” | `M4.1-NAR-07-VO` | felirat, leirat | AI-generált |
| `M4.1-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook beszélő-fej videó – „Mit gondolnak rólad az első 5 másodpercben?” | `M4.1-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |
| `M4.1-VID-02` | video/interactive | legyártandó | produkciós szabályra vár | Interactive Video – 3 madrich-kiállás mini-jelenettel + beágyazott kérdések | — | felirat, leirat | AI-generált |
| `M4.1-VID-03` | video/explainer | legyártandó | produkciós szabályra vár | Jelenet 1 karaktervideó – „Jegyzetbe bújó madrich” | — | felirat, leirat | AI-generált |
| `M4.1-VID-04` | video/explainer | legyártandó | produkciós szabályra vár | Jelenet 2 karaktervideó – „Ideges topogó madrich” | — | felirat, leirat | AI-generált |
| `M4.1-VID-05` | video/explainer | legyártandó | produkciós szabályra vár | Jelenet 3 karaktervideó – „Nyitott, stabil madrich” | — | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M4/Online leckék/M4.2 – Aktív hallgatás & visszatükrözés.md

*Egység:* `M4.2` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M4.2-EGY-01` | other/h5p-interaction | legyártandó | specifikáció kész | H5P Single Choice – „Mi lenne az első reakciód?” (helyzetfelmérés) | — | — | vegyes |
| `M4.2-EGY-02` | other/h5p-interaction | legyártandó | specifikáció kész | H5P Dialog Cards készlet – „Melyik segít jobban?” | — | — | vegyes |
| `M4.2-EGY-03` | other/h5p-interaction | legyártandó | specifikáció kész | H5P Drag&Drop / Sorting – „Lezáró vagy támogató?” | — | — | vegyes |
| `M4.2-EGY-04` | other/h5p-interaction | legyártandó | specifikáció kész | H5P mini-quiz – 2 Single Choice kérdés (Check) | — | — | vegyes |
| `M4.2-EGY-05` | other/h5p-interaction | legyártandó | specifikáció kész | 2× szabad szöveges mező – reflektív kérdések (visszatükröző mondat + elhagyandó mondat) | — | — | vegyes |
| `M4.2-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Fogalom-ikonok: fejhallgató (aktív hallgatás) & körkörös nyíl (visszatükrözés) | — | — | AI-generált |
| `M4.2-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Hook chat-buborék: ideges peula-mondat | — | alt-szöveg | AI-generált |
| `M4.2-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Két fogalom-doboz: Aktív hallgatás & Visszatükrözés | — | alt-szöveg | AI-generált |
| `M4.2-ILL-03` | illustration | legyártandó | produkciós szabályra vár | Outro összegző checklist vizuál | — | alt-szöveg | AI-generált |
| `M4.2-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 1 narráció – „Mit mondanál elsőre?” | `M4.2-NAR-01-VO` | felirat, leirat | AI-generált |
| `M4.2-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 2 narráció – aktív hallgatás és visszatükrözés definíciója | `M4.2-NAR-02-VO` | felirat, leirat | AI-generált |
| `M4.2-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 3 narráció – Dialog Cards felvezetés | `M4.2-NAR-03-VO` | felirat, leirat | AI-generált |
| `M4.2-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 6 narráció – Outro „Mit mondok legközelebb?” | `M4.2-NAR-04-VO` | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M4/Online leckék/M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md

*Egység:* `M4.3` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M4.3-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Négy kérdéstípus – színkódolt doboz-diagram | — | alt-szöveg | vegyes |
| `M4.3-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Kérdéstípus szín-ikon készlet (4 db) | — | alt-szöveg | AI-generált |
| `M4.3-ILL-01` | illustration | legyártandó | produkciós szabályra vár | „Na, értitek?” – síri csend storyboard | — | alt-szöveg | AI-generált |
| `M4.3-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 1 narráció – Hook | `M4.3-NAR-01-VO` | felirat, leirat | AI-generált |
| `M4.3-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 2 narráció – Négy kérdéstípus | `M4.3-NAR-02-VO` | felirat, leirat | AI-generált |
| `M4.3-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 6 narráció – Outro/reflexió | `M4.3-NAR-03-VO` | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M4/Online leckék/M4.4 – 45 mp-es peula-pitch – vázlat egy konkrét kvucára.md

*Egység:* `M4.4` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M4.4-DIA-02` | diagram | legyártandó | produkciós szabályra vár | Slide 2 definíciós bullet-vizuál: „Peula-pitch =" | — | alt-szöveg | AI-generált |
| `M4.4-DIA-03` | diagram | legyártandó | produkciós szabályra vár | Slide 3 sablon-vizuál: 5 kérdéses pitch-sablon | — | alt-szöveg | AI-generált |
| `M4.4-DIA-05` | diagram | legyártandó | produkciós szabályra vár | Slide 5 sablon-vizuál + összefoglaló | — | alt-szöveg | AI-generált |
| `M4.4-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Hook-jelenet: madrich a kvuca előtt, 45 mp nyomás | — | alt-szöveg | AI-generált |
| `M4.4-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 1 narráció – „45 mp-ed van… Mit mondasz?" | `M4.4-NAR-01-VO` | felirat, leirat | AI-generált |
| `M4.4-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 2 narráció – „Mi az a peula-pitch?" | `M4.4-NAR-02-VO` | felirat, leirat | AI-generált |
| `M4.4-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 3 narráció – Az 5 kérdéses pitch-sablon | `M4.4-NAR-03-VO` | felirat, leirat | AI-generált |
| `M4.4-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Slide 5 narráció – „Írd meg a saját 45 mp-es pitch-vázad" | `M4.4-NAR-05-VO` | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M4/Peulák/M4.A – Állj oda! – Kiállás & jelenlét a térben.md

*Egység:* `M4.A` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M4.A-KART-01` | card-set | legyártandó | produkciós szabályra vár | Kiállás-szobrok szerepcímke-szett | — | nyomtatható PDF | vegyes |
| `M4.A-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Exit-mondat post-it / fókuszmondat cédula | — | nyomtatható PDF | vegyes |
| `M4.A-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist – „Állj oda!” (1 A4) | — | nyomtatható PDF | vegyes |
| `M4.A-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Flipchart-előkészítő sablon – kulcsmondatok & megfigyelés-kulcsszavak (opcionális) | — | nyomtatható PDF | vegyes |
| `M4.A-POSZ-01` | poster | legyártandó | produkciós szabályra vár | „M4 – kiállás” gyűjtő-boríték / fal-címke | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M4/Peulák/M4.B – Mit és hogyan kérdezek – Kérdezés & pitch gyakorlása.md

*Egység:* `M4.B` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M4.B-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Exit-ticket kártya / post-it sablon (2 kérdés) | — | nyomtatható PDF | emberi |
| `M4.B-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Gyors pitch-váz mini-sablon (B-terv munkalap) | — | nyomtatható PDF | emberi |
| `M4.B-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist (1 A4) | — | nyomtatható PDF | emberi |
| `M4.B-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Kérdéstípusok flipchart-/poszter-sablon (4 típus) | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M4/Peulák/M4.F – Felzárkóztató peula – Test, hang, kérdések & pitch (Study Lab).md

*Egység:* `M4.F` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M4.F-EGY-01` | print/consumable | külső forrás | jogtisztázás alatt | Check-in matricák / post-it készlet (1 db/fő) | — | — | stock |
| `M4.F-EGY-02` | print/consumable | külső forrás | jogtisztázás alatt | Filc-/marker-készlet a fogalom-térkép táblához | — | — | stock |
| `M4.F-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Jegyzetlap – 1 gondolat / 1 kérdés leckénként (L1–L4) | — | nyomtatható PDF | vegyes |
| `M4.F-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | 45 mp-es peula-pitch váz-sablon (eszközmentes pótló feladat) | — | nyomtatható PDF | vegyes |
| `M4.F-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Állapotfelmérő tábla-sablon – „Melyik leckénél tartasz?” (M4.1–M4.4 sorok) | — | nyomtatható PDF | vegyes |
| `M4.F-POSZ-02` | poster | legyártandó | produkciós szabályra vár | Fogalom-térkép sablon – Test / Hang / Kérdések / Pitch (4 buborék) | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M5/M5 – Ez most játék vagy tanulás – Nonformális nevelés, módszerválasztás & tanulástan.md

*Egység:* `M5-HUB` · *típus:* hub

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M5-HUB-EGY-01` | print/consumable | külső forrás | jogtisztázás alatt | Gallery walk reakció-eszközök (post-it / pötty-matrica) | — | — | stock |

### 02 Tervezet/Modulok/M5/Online leckék/M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md

*Egység:* `M5.1` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M5.1-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Háromoszlopos formális/nonformális/informális grafika | — | alt-szöveg | AI-generált |
| `M5.1-EGY-01` | other/ui-text | legyártandó | specifikáció kész | Provenance-címke – AI-generált avatar / AI-elemek jelölés | — | — | emberi |
| `M5.1-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Három tanulástípus ikon-grafika | — | — | AI-generált |
| `M5.1-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | INPUT 2 narráció – három fogalom definíciója | `M5.1-NAR-02-VO` | felirat, leirat | vegyes |
| `M5.1-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | HOOK beszélő fej – suli / somer / random | `M5.1-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |
| `M5.1-VID-02` | video/ai-talking-head | legyártandó | jogtisztázás alatt | OUTRO beszélő fej thumbnail (opcionális) | `M5.1-VID-02-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M5/Online leckék/M5.2 – Feladat → módszer döntési fa – Mit választok először.md

*Egység:* `M5.2` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M5.2-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Központi sorrend-folyamatábra: feladat → cél → kvuca → módszer | — | alt-szöveg | AI-generált |
| `M5.2-DIA-02` | diagram | legyártandó | produkciós szabályra vár | Döntési fa térkép – 4 ág + közös visszacsatlakozás | — | alt-szöveg | AI-generált |
| `M5.2-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Ág-azonosító ikonkészlet (4 ikon) | — | alt-szöveg | AI-generált |
| `M5.2-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Bevezető jelenet-illusztráció: madrich a péntek esti felkérés előtt | — | alt-szöveg | AI-generált |
| `M5.2-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Feladat–cél–kvuca–módszer mondatbefejező munkalap | — | nyomtatható PDF | AI-generált |

### 02 Tervezet/Modulok/M5/Online leckék/M5.3 – Hogyan tanulunk tényleg – Gyakorlás, visszahívás, spacing.md

*Egység:* `M5.3` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M5.3-EGY-01` | other/h5p-interaction | legyártandó | specifikáció kész | Dialog Cards Leitner-pakli (Repetition mód) – akadálymentes interaktív elem | — | — | emberi |
| `M5.3-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Három kulcsfogalom ikon-trió (gyakorlás, visszahívás, spacing) | — | alt-szöveg | AI-generált |
| `M5.3-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Két tanulási történet – A vs. B szembeállítás (Hook) | — | alt-szöveg | AI-generált |
| `M5.3-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Somer-példák a három fogalomra – három mini-jelenet | — | alt-szöveg | AI-generált |
| `M5.3-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | Opcionális narráció – három kulcsfogalom (20-30 mp) | — | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M5/Online leckék/M5.4 – Cél–kvuca–módszer mini-táblázat – saját adatbázisod madrichként.md

*Egység:* `M5.4` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M5.4-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Minta-táblázat kártya-nézet (mobilbarát) – 3 helyzet blokk | — | alt-szöveg | AI-generált |
| `M5.4-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Letölthető „Feladat–kvuca–módszer + tanulástan” kitölthető sablon (doc / sheet) | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M5/Peulák/M5.A – Suli, Somer vagy random – Hol tanulunk és hogyan.md

*Egység:* `M5.A` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M5.A-KART-01` | card-set | legyártandó | produkciós szabályra vár | 12 helyzetkártya – kétoldalas szett (front: sztori, hátlap: címke) | — | nyomtatható PDF | vegyes |
| `M5.A-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Poszter-sablon: 4 mezős „átöltöztetés” mini-táblázat | — | nyomtatható PDF | vegyes |
| `M5.A-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Flipchart-sablon: „Feladat / Cél → Kvuca → Módszer” lánc | — | nyomtatható PDF | vegyes |
| `M5.A-POSZ-01` | poster | legyártandó | produkciós szabályra vár | 3 sarok-felirat: SULI / SOMER / RANDOM élet | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M5/Peulák/M5.B – Tervezek egy nonformális peula-részletet – hogy tényleg tanuljunk is.md

*Egység:* `M5.B` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M5.B-KART-01` | card-set | legyártandó | produkciós szabályra vár | Seed-sor kártyaszett (6-8 db kész táblázat-sor) | — | nyomtatható PDF | emberi |
| `M5.B-KART-02` | card-set | legyártandó | produkciós szabályra vár | Élő kvíz – képzői állítás-kártyák (5 db igaz/hamis + súgó) | — | nyomtatható PDF | emberi |
| `M5.B-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | A3 / flipchart üres vázlatlap (3-4 blokkos peula-részlet) | — | nyomtatható PDF | emberi |
| `M5.B-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Mintatáblázat – „Cél–kvuca–módszer" (2-3 db tartalék) | — | nyomtatható PDF | emberi |
| `M5.B-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Tábla/flipchart sablonlap – kulcsszó-panel + javasolt tervezési struktúra | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M5/Peulák/M5.F – Felzárkóztató peula – Suli, Somer & tanulástan (Study Lab).md

*Egység:* `M5.F` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M5.F-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Jegyzetlap – „1 gondolat / 1 kérdés leckénként” (L1–L4) | — | nyomtatható PDF | emberi |
| `M5.F-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Hőmérő-flipchart – „Melyik M5-leckéig jutottam?” | — | nyomtatható PDF | emberi |
| `M5.F-POSZ-02` | poster | legyártandó | produkciós szabályra vár | Fogalom-térkép flipchart-sablon – 3 nagy rész + nyilak | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M6/M6 – Toolbox – játék, történet, kézműves & inkluzivitás.md

*Egység:* `M6-HUB` · *típus:* hub

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M6-HUB-MUNK-01` | worksheet | újrahasznosítás | specifikáció kész | Játéklap-sablon (üres, kitölthető) – M6 modul-produktum | — | — | vegyes |

### 02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 4 kvucára.md

*Egység:* `M6.1` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M6.1-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Korosztály-táblázat – 4 kvuca-korosztály (tartalmi ábra) | — | alt-szöveg | AI-generált |
| `M6.1-EGY-01` | other/ui-text | legyártandó | specifikáció kész | AI-provenance ember-olvasható sor (lecke alján/dián) | — | — | emberi |
| `M6.1-EGY-02` | other/h5p-interaction | legyártandó | specifikáció kész | Single Choice – önreflexió: „mi alapján döntesz?” | — | — | emberi |
| `M6.1-EGY-03` | other/h5p-interaction | legyártandó | specifikáció kész | Single Choice – „Névkör labdával” korosztály | — | — | emberi |
| `M6.1-EGY-04` | other/h5p-interaction | legyártandó | specifikáció kész | Single Choice – 11–13 bizalomjáték forma | — | — | emberi |
| `M6.1-EGY-05` | other/h5p-interaction | legyártandó | specifikáció kész | Szabad szöveges kérdés – kockázat bizalomjátékban | — | — | emberi |
| `M6.1-EGY-06` | other/h5p-interaction | legyártandó | specifikáció kész | Single Choice – 6–10 reflexiós vs. mély | — | — | emberi |
| `M6.1-EGY-07` | other/h5p-interaction | legyártandó | specifikáció kész | Single Choice – Szitu 1 korosztály-választás | — | — | emberi |
| `M6.1-EGY-08` | other/h5p-interaction | legyártandó | specifikáció kész | Szabad szöveges kérdés – Szitu 2 futkosós energizer kockázata + safety-keret | — | — | emberi |
| `M6.1-EGY-09` | other/h5p-interaction | legyártandó | specifikáció kész | Single Choice – miért hasznos kategóriákban gondolkodni | — | — | emberi |
| `M6.1-EGY-10` | other/h5p-interaction | legyártandó | specifikáció kész | Single Choice – mikor ne hozz mély élményjátékot | — | — | emberi |
| `M6.1-EGY-11` | other/h5p-interaction | legyártandó | specifikáció kész | Szabad szöveges mező – záró mini-reflexió (kedvenc játék + kockázat) | — | — | emberi |
| `M6.1-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Játék-kategória ikonok – 5 kategória | — | alt-szöveg | AI-generált |
| `M6.1-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Kategória-kártyák 1 – ismerkedős + energizer (2 kártya) | — | alt-szöveg | AI-generált |
| `M6.1-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Kategória-kártya 2 – bizalomjáték „Csukott szemű vezetés” | — | alt-szöveg | AI-generált |
| `M6.1-ILL-03` | illustration | legyártandó | produkciós szabályra vár | Kategória-kártya 3 – reflexiós vs. mély élmény (2 minisztori) | — | alt-szöveg | AI-generált |
| `M6.1-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 2: 4 korosztály bemutatása | `M6.1-NAR-02-VO` | felirat, leirat | AI-generált |
| `M6.1-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 3: 5 játék-kategória | `M6.1-NAR-03-VO` | felirat, leirat | AI-generált |
| `M6.1-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 4: ismerkedős + energizer | `M6.1-NAR-04-VO` | felirat, leirat | AI-generált |
| `M6.1-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 5: bizalom-/kontakt-játék + kockázat | `M6.1-NAR-05-VO` | felirat, leirat | AI-generált |
| `M6.1-NAR-06` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 6: reflexiós vs. mély élmény | `M6.1-NAR-06-VO` | felirat, leirat | AI-generált |
| `M6.1-NAR-07` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 8 outro (opcionális rövid videóhoz) | `M6.1-NAR-07-VO` | felirat, leirat | AI-generált |
| `M6.1-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook beszélőfej-videó – „Volt már olyan, hogy nem ült a játék?” | `M6.1-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M6/Online leckék/M6.2 – Történet, mint tükör.md

*Egység:* `M6.2` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M6.2-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Kétoszlopos „Oké / Figyelj rá” táblázat-ábra | — | alt-szöveg | AI-generált |
| `M6.2-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Tartalmi ikonok – „Miért mesélünk?” (szív, tükör, kérdőjel) | — | alt-szöveg | AI-generált |
| `M6.2-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 2 „Miért mesélünk történeteket?” (40–50 mp) | `M6.2-NAR-02-VO` | felirat, leirat | AI-generált |
| `M6.2-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 4 történet 2. rész (40–50 mp) | `M6.2-NAR-04-VO` | felirat, leirat | AI-generált |
| `M6.2-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 5 „Történet, mint tükör – kérdések” (45–60 mp) | `M6.2-NAR-05-VO` | felirat, leirat | AI-generált |
| `M6.2-NAR-06` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 6 „Nem minden téma/nyelv jó” (45–60 mp) | `M6.2-NAR-06-VO` | felirat, leirat | AI-generált |
| `M6.2-NAR-07` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 7 Activity „Te hogyan tennéd tükörré?” (30–40 mp) | `M6.2-NAR-07-VO` | felirat, leirat | AI-generált |
| `M6.2-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Hook – AI beszélő fej: „fagyott csend lett a sztoritól?” | `M6.2-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |
| `M6.2-VID-02` | video/ai-talking-head | legyártandó | jogtisztázás alatt | Opcionális beszélő fej / narrációs videó – „Az új lány a körben” (1. rész) | `M6.2-VID-02-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M6/Online leckék/M6.3 – Kézműves, ami tanít is.md

*Egység:* `M6.3` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M6.3-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Három-kérdés keret – ikon/box diagram (Cél–Inkluzivitás–Variációk) | — | alt-szöveg | AI-generált |
| `M6.3-FOTO-01` | illustration | legyártandó | produkciós szabályra vár | HOOK – Unottan színezgető gyerekek (bal kép) | — | alt-szöveg | AI-generált |
| `M6.3-FOTO-02` | illustration | újrahasznosítás | specifikáció kész | HOOK – Kvuca közös plakáton dolgozik (jobb kép) | — | — | AI-generált |
| `M6.3-FOTO-03` | illustration | legyártandó | produkciós szabályra vár | Közös kvuca-plakát – sok kéz dolgozik rajta | — | alt-szöveg | AI-generált |
| `M6.3-FOTO-04` | illustration | legyártandó | produkciós szabályra vár | Személyes szimbólum-karkötő – gyöngyfűzés | — | alt-szöveg | AI-generált |
| `M6.3-FOTO-05` | illustration | legyártandó | produkciós szabályra vár | Kvuca-zászló – közös festés | — | alt-szöveg | AI-generált |
| `M6.3-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Ikon-készlet – Cél / Inkluzivitás / Variációk | — | — | AI-generált |
| `M6.3-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 1 HOOK (35–45 mp) | `M6.3-NAR-01-VO` | felirat, leirat | AI-generált |
| `M6.3-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 2 INPUT 1 (45–55 mp) | `M6.3-NAR-02-VO` | felirat, leirat | AI-generált |
| `M6.3-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 3 PÉLDA 1 Közös plakát (45–60 mp) | `M6.3-NAR-03-VO` | felirat, leirat | AI-generált |
| `M6.3-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 4 PÉLDA 2 Karkötő (45–60 mp) | `M6.3-NAR-04-VO` | felirat, leirat | AI-generált |
| `M6.3-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 5 PÉLDA 3 Kvuca-zászló (45–60 mp) | `M6.3-NAR-05-VO` | felirat, leirat | AI-generált |
| `M6.3-NAR-06` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SLIDE 6 ACTIVITY (30–40 mp) | `M6.3-NAR-06-VO` | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M6/Online leckék/M6.4 – Döntési szcenáriók – mit választanál.md

*Egység:* `M6.4` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M6.4-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Szcenárió- és feedback-szekció ikonkészlet (9 szemantikus jelölő) | — | alt-szöveg | AI-generált |

### 02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 4 kvucára (45’).md

*Egység:* `M6.A` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M6.A-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Exit ticket – „1 játék, amiről játéklapot készítenél” | — | nyomtatható PDF | AI-generált |
| `M6.A-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist – „Játék-labor 4 kvucára” (1 oldalas cheat-sheet) | — | nyomtatható PDF | AI-generált |
| `M6.A-POSZ-01` | poster | legyártandó | produkciós szabályra vár | 4 kvuca-sarok korosztály-lapok (szett) | — | nyomtatható PDF | AI-generált |
| `M6.A-POSZ-02` | poster | legyártandó | produkciós szabályra vár | CÉL–KVUCA–RIZIKÓ–VARIÁCIÓ mátrix flipchart-sablon | — | nyomtatható PDF | AI-generált |
| `M6.A-POSZ-03` | poster | legyártandó | produkciós szabályra vár | Inkluzivitás-elemző tábla-sablon (4 oszlop) | — | nyomtatható PDF | AI-generált |

### 02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap workshop – saját eszköz tervezése (45’).md

*Egység:* `M6.B` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M6.B-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Játéklap-sablon (üres kitölthető munkalap) | — | nyomtatható PDF, szerkeszthető, kitölthető változat | emberi |
| `M6.B-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Rubrika / minimum-checklista (értékelő lap) | — | nyomtatható PDF | emberi |
| `M6.B-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Kész minta-játéklap – JÁTÉK példa (képzői mintalap) | — | nyomtatható PDF | emberi |
| `M6.B-MUNK-04` | worksheet | legyártandó | produkciós szabályra vár | Kész minta-játéklap – TÖRTÉNET példa (képzői mintalap) | — | nyomtatható PDF | emberi |
| `M6.B-MUNK-05` | worksheet | legyártandó | produkciós szabályra vár | Kész minta-játéklap – KÉZMŰVES példa (képzői mintalap) | — | nyomtatható PDF | emberi |
| `M6.B-MUNK-06` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist (1 A4 – peula előtt/közben) | — | nyomtatható PDF | emberi |
| `M6.B-POSZ-01` | poster | legyártandó | produkciós szabályra vár | SBI flipchart-sablon (S–B–I emlékeztető + kész minta-mondat) | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Toolbox & játéklap (Study Lab).md

*Egység:* `M6.F` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M6.F-EGY-01` | print/consumable | külső forrás | jogtisztázás alatt | Check-in matricák / post-it készlet (beszerzendő irodaszer) | — | — | stock |
| `M6.F-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Jegyzetlap – „1 gondolat / 1 kérdés leckénként + játéklap” | — | nyomtatható PDF | AI-generált |
| `M6.F-MUNK-02` | worksheet | újrahasznosítás | specifikáció kész | Üres játéklap-sablon (offline B-terv + Study Lab) | — | — | AI-generált |
| `M6.F-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Lecke-összefoglalók M6.1–M6.4 (offline B-terv, 1–1 oldal) | — | nyomtatható PDF | AI-generált |
| `M6.F-MUNK-04` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist – 1 A4 (peula előtt/közben/után) | — | nyomtatható PDF | AI-generált |
| `M6.F-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Állapotfelmérő tábla – M6 leckesorok + játéklap | — | nyomtatható PDF | AI-generált |
| `M6.F-POSZ-02` | poster | legyártandó | produkciós szabályra vár | Fogalom-térkép sablon – 5–6 buborék (Toolbox nagy képe) | — | nyomtatható PDF | AI-generált |

### 02 Tervezet/Modulok/M7/M7 – Peula a papírtól a valóságig – Programírás, Zmán Kvucá & AI-támogatott tervezés.md

*Egység:* `M7-HUB` · *típus:* hub

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M7-HUB-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Modul-fogalomtérkép: SMART – Peula 11 pont – Zmán Kvucá – Peula v2 | — | alt-szöveg | AI-generált |
| `M7-HUB-DIA-02` | diagram | legyártandó | produkciós szabályra vár | Kétkapus capstone idővonal: v1 first-draft gate → spacing → v2 mastery-kapu | — | alt-szöveg | AI-generált |
| `M7-HUB-DIA-03` | diagram | legyártandó | produkciós szabályra vár | Portfólió-átkötés / capstone-konvergencia: M1 SBI … M6 játéklap → 1 Peula v2 | — | alt-szöveg | AI-generált |
| `M7-HUB-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | 1 perces exit-ticket munkalap (M7.A/M7.B/M7.F utáni offline visszajelzés) | — | nyomtatható PDF | vegyes |

### 02 Tervezet/Modulok/M7/Online leckék/M7.1 – Ez még csak vágy, nem cél – SMART nevelési cél someres módra.md

*Egység:* `M7.1` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M7.1-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | SMART 5 elem ikon-készlet (S-M-A-R-T) | — | alt-szöveg | AI-generált |
| `M7.1-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Hook – 3 vágy-mondat kártya | — | alt-szöveg | AI-generált |
| `M7.1-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Someres SMART példa – 2 kártya (szolidaritás / biztonság) | — | alt-szöveg | AI-generált |
| `M7.1-ILL-03` | illustration | legyártandó | produkciós szabályra vár | Példa prompt-kártya (AI-blokk) | — | alt-szöveg | AI-generált |
| `M7.1-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – SMART madrich-nyelven (opcionális) | `M7.1-NAR-01-VO` | felirat, leirat | AI-generált |
| `M7.1-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Narráció – záró feladat instrukció (opcionális) | — | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M7/Online leckék/M7.2 – Nem csak játék, hanem peula – 11 tervezési pont & AI-támogatás.md

*Egység:* `M7.2` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M7.2-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Peula 11 pontja – 3 fázisú térkép diagram | — | alt-szöveg | AI-generált |
| `M7.2-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Ikon-készlet – Megírás 4 pontja (játék, idővonal, óra, doboz) | — | alt-szöveg | AI-generált |
| `M7.2-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Illusztráció – madrich tervez (laptopnál/jegyzetfüzettel) | — | alt-szöveg | AI-generált |
| `M7.2-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 2 narráció – „A Peula 11 pontjának térképe” | `M7.2-NAR-02-VO` | felirat, leirat | AI-generált |
| `M7.2-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 3 narráció – Előkészítés (4 pont) | `M7.2-NAR-03-VO` | felirat, leirat | AI-generált |
| `M7.2-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 4 narráció – Megírás (4 pont) + 4 fázis | `M7.2-NAR-04-VO` | felirat, leirat | AI-generált |
| `M7.2-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | SLIDE 5 narráció – Utómunka & safety (3 pont) | `M7.2-NAR-05-VO` | felirat, leirat | AI-generált |
| `M7.2-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | HOOK – AI beszélő fej: „Csak játék maradt a peula?” | `M7.2-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M7/Online leckék/M7.3 – Zmán Kvucá-checklist – idő, tér, felelősség.md

*Egység:* `M7.3` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M7.3-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Zmán Kvucá-checklist 5 fő terület – kattintható diagram/kártyaszett | — | alt-szöveg | AI-generált |
| `M7.3-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Ikon-készlet – Zmán Kvucá 5 területe | — | alt-szöveg | AI-generált |
| `M7.3-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Két hasábos kontraszt-vizuál: „Csak játékban” vs. „Zmán Kvucában gondolkozunk” | — | alt-szöveg | AI-generált |
| `M7.3-ILL-02` | illustration | legyártandó | produkciós szabályra vár | Illusztrált mintaprogram-kártya: „Péntek esti Zmán Kvucá a kenben” | — | alt-szöveg | AI-generált |
| `M7.3-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | INPUT 1 narráció (SLIDE 2) | `M7.3-NAR-02-VO` | felirat, leirat | AI-generált |
| `M7.3-NAR-03` | voiceover/narration | legyártandó | produkciós szabályra vár | INPUT 2 narráció – mintaprogram (SLIDE 3) | `M7.3-NAR-03-VO` | felirat, leirat | AI-generált |
| `M7.3-NAR-04` | voiceover/narration | legyártandó | produkciós szabályra vár | ACTIVITY narráció – 5 terület végigvétele (SLIDE 4) | `M7.3-NAR-04-VO` | felirat, leirat | AI-generált |
| `M7.3-NAR-05` | voiceover/narration | legyártandó | produkciós szabályra vár | OUTRO narráció – híd a Moodle Checklistre (SLIDE 6, opcionális) | `M7.3-NAR-05-VO` | felirat, leirat | AI-generált |
| `M7.3-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | HOOK beszélő-fej: „Zmán Kvucá = csak programidő…?” | `M7.3-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M7/Online leckék/M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md

*Egység:* `M7.4` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M7.4-DIA-01` | diagram | legyártandó | produkciós szabályra vár | 3 építőkocka diagram – SMART cél / Peula 11 pontja / Zmán Kvucá | — | alt-szöveg | AI-generált |
| `M7.4-IKO-01` | icon-set | újrahasznosítás | specifikáció kész | Kvuca-típus piktogramok – Parparim / Kivsza / Leviatan / Zorea | — | — | AI-generált |
| `M7.4-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | Opcionális narráció – ACTIVITY 1 (kvuca-típus + meta + SMART cél) | `M7.4-NAR-01-VO` | felirat, leirat | AI-generált |
| `M7.4-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Opcionális narráció – OUTRO (gratuláció + next step) | `M7.4-NAR-02-VO` | felirat, leirat | AI-generált |
| `M7.4-VID-01` | video/ai-talking-head | legyártandó | jogtisztázás alatt | HOOK – AI beszélő fej: papíron szép vs. vállalható peula | `M7.4-VID-01-VO` | felmondott hang, felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/M7/Peulák/M7.A – Célból peula – SMART & 11 pont élőben.md

*Egység:* `M7.A` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M7.A-KART-01` | card-set | legyártandó | produkciós szabályra vár | „Szétfolyó cél” kártyaszett a sarok-játékhoz | — | nyomtatható PDF | emberi |
| `M7.A-KART-02` | card-set | legyártandó | produkciós szabályra vár | Minta-peula-ötlet kártyák (tartalék, ha valaki elakad) | — | nyomtatható PDF | emberi |
| `M7.A-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist (1 A4) – peula előtti átfutó | — | nyomtatható PDF | emberi |
| `M7.A-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Képzői felolvasó-kulcs a sarok-játékhoz (besorolás + indok) | — | nyomtatható PDF | emberi |
| `M7.A-POSZ-01` | poster | legyártandó | produkciós szabályra vár | „Peula 11 pontja” flipchart / poszter – kanonikus pont-lista | — | nyomtatható PDF | emberi |
| `M7.A-POSZ-02` | poster | legyártandó | produkciós szabályra vár | Tábla / flipchart-sablon – kulcsszavak és SMART irányító-kérdések | — | nyomtatható PDF | emberi |
| `M7.A-POSZ-03` | poster | legyártandó | produkciós szabályra vár | Peer feedback – két mondatkezdő tábla / flipchart-sablon | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M7/Peulák/M7.B – Peula v2 & Zmán Kvucá – amikor a papír találkozik a valósággal.md

*Egység:* `M7.B` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M7.B-EGY-01` | card-set | legyártandó | produkciós szabályra vár | A/B sarok-kvíz 5 állítása (felolvasandó kártyaszett / képzői segédlap) | — | nyomtatható PDF | emberi |
| `M7.B-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Zmán Kvucá-mini-checklist (kiscsoportos munkalap) | — | nyomtatható PDF | emberi |
| `M7.B-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | "Előtte–utána"-lap (gallery walk artefaktum-sablon) | — | nyomtatható PDF | emberi |
| `M7.B-MUNK-03` | worksheet | legyártandó | produkciós szabályra vár | Minta-Peula v1 (B-terv tartalék vázlat) | — | nyomtatható PDF | emberi |
| `M7.B-MUNK-04` | worksheet | legyártandó | produkciós szabályra vár | Exit ticket – mini visszajelző cetli | — | nyomtatható PDF | emberi |
| `M7.B-MUNK-05` | worksheet | legyártandó | produkciós szabályra vár | Kipróbálási kötelezettségvállalás – if–then mini sablon (3 sor) | — | nyomtatható PDF | emberi |
| `M7.B-MUNK-06` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist (1 A4 – gyors átfutásra) | — | nyomtatható PDF | emberi |
| `M7.B-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Flipchart-poszter: "Zmán Kvucá = …" definíció + "AI-határok" | — | nyomtatható PDF | emberi |
| `M7.B-POSZ-02` | poster | legyártandó | produkciós szabályra vár | Falra kifüggesztett poszter: a Zmán Kvucá-checklist 5 területe nagyban | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/M7/Peulák/M7.F – Felzárkóztató peula – Peula & Zmán Kvucá (Study Lab).md

*Egység:* `M7.F` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `M7.F-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Jegyzetlap – '1 gondolat / 1 kérdés leckénként' (L1–L4) + opcionális pótlási terv | — | nyomtatható PDF, szerkeszthető, kitölthető változat | emberi |
| `M7.F-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist (1 A4) – peula előtt/közben/után | — | nyomtatható PDF | emberi |
| `M7.F-POSZ-01` | poster | legyártandó | produkciós szabályra vár | Állapotfelmérő tábla – M7 leckesorok + 'Kész' sor | — | nyomtatható PDF | emberi |
| `M7.F-POSZ-02` | poster | legyártandó | produkciós szabályra vár | Fogalom-térkép sablon – 4 buborék (SMART, 11 pont, Zmán Kvucá, Peula v2 & AI) | — | nyomtatható PDF | emberi |

### 02 Tervezet/Modulok/Z/Z – Zárás & híd a terepre.md

*Egység:* `Z-HUB` · *típus:* hub

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `Z-HUB-POSZ-02` | poster | újrahasznosítás | specifikáció kész | Lezáró rituálé – közös „felhő” plakát-sablon (opcionális) | — | — | AI-generált |

### 02 Tervezet/Modulok/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 timeline.md

*Egység:* `Z.1` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `Z.1-DIA-01` | diagram | legyártandó | produkciós szabályra vár | Vízszintes féléves idővonal M0→M7 | — | alt-szöveg | AI-generált |
| `Z.1-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Napló-ikon a highlight-esszéhez | — | alt-szöveg | AI-generált |
| `Z.1-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Sorozat-plakát ikon M0–M7 epizódokkal | — | alt-szöveg | AI-generált |
| `Z.1-NAR-01` | voiceover/narration | legyártandó | produkciós szabályra vár | Opcionális narráció – idővonal (30–40 mp) | `Z.1-NAR-01-VO` | felirat, leirat | AI-generált |
| `Z.1-NAR-02` | voiceover/narration | legyártandó | produkciós szabályra vár | Opcionális záró narráció – outro (20–30 mp) | `Z.1-NAR-02-VO` | felirat, leirat | AI-generált |

### 02 Tervezet/Modulok/Z/Online leckék/Z.2 – Tanultam valamit! – saját tanulási pillanataim.md

*Egység:* `Z.2` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `Z.2-ILL-01` | illustration | legyártandó | produkciós szabályra vár | Hook-illusztráció: gondolkodó figura villanykörtével | — | alt-szöveg | AI-generált |

### 02 Tervezet/Modulok/Z/Online leckék/Z.3 – Híd a terepre – következő lépések.md

*Egység:* `Z.3` · *típus:* online-lecke

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `Z.3-IKO-01` | icon-set | legyártandó | produkciós szabályra vár | Óriáslépés vs. apró lépések ikonpár | — | alt-szöveg | AI-generált |

### 02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md

*Egység:* `Z.A` · *típus:* peula

| ID | Típus | Mód | Státusz | Cím | Forrásblokk | Derivatívák | Eredet |
|---|---|---|---|---|---|---|---|
| `Z.A-KART-01` | card-set | legyártandó | produkciós szabályra vár | Előhívó kérdések kártya – „üres kézzel” érkezőknek | — | nyomtatható PDF | vegyes |
| `Z.A-KART-02` | card-set | legyártandó | produkciós szabályra vár | Poszter seed-példák kártya – ha egy csoport megakad | — | nyomtatható PDF | vegyes |
| `Z.A-KART-03` | card-set | legyártandó | produkciós szabályra vár | SBI-elismerés mintamondat kártya – párcseréhez | — | nyomtatható PDF | vegyes |
| `Z.A-KART-04` | card-set | legyártandó | produkciós szabályra vár | M0-tükör anonim idézet-kártyák (M0.A kickoff visszakötés) | — | nyomtatható PDF | vegyes |
| `Z.A-MUNK-01` | worksheet | legyártandó | produkciós szabályra vár | Híd a terepre – kétoszlopos poszter-sablon | — | nyomtatható PDF | vegyes |
| `Z.A-MUNK-02` | worksheet | legyártandó | produkciós szabályra vár | Képzői checklist – 1 oldalas előkészítő ellenőrzőlista | — | nyomtatható PDF | vegyes |
| `Z.A-POSZ-01` | poster | legyártandó | produkciós szabályra vár | „Mit viszek magammal?” – szó-felhő fejléc-poszter | — | nyomtatható PDF | vegyes |

## 🈳 Ellenőrzötten asset nélküli fájlok

| Fájl | Egység | Típus | Indoklás |
|---|---|---|---|
| 02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md | `M0-HUB` | hub | Modul-áttekintő fájl: a benne említett médiát a modul saját leckéi és peulái deklarálják; itt nincs önálló legyártandó anyag. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.) |
| 02 Tervezet/Modulok/M1/M1 – Kapu – értékelő (item-bank + rubrika).md | `M1-KAPU` | kapu | Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.) |
| 02 Tervezet/Modulok/M2/M2 – Kapu – értékelő (item-bank + rubrika).md | `M2-KAPU` | kapu | Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.) |
| 02 Tervezet/Modulok/M3/M3 – Kapu – értékelő (item-bank + rubrika).md | `M3-KAPU` | kapu | Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.) |
| 02 Tervezet/Modulok/M4/M4 – Hallható és érthető vagyok – Kiállás, kapcsolódás & kérdezéstechnika.md | `M4-HUB` | hub | Modul-áttekintő fájl: a benne említett médiát a modul saját leckéi és peulái deklarálják; itt nincs önálló legyártandó anyag. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.) |
| 02 Tervezet/Modulok/M5/M5 – Kapu – értékelő (item-bank + rubrika).md | `M5-KAPU` | kapu | Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.) |
| 02 Tervezet/Modulok/M6/M6 – Kapu – értékelő (item-bank + rubrika).md | `M6-KAPU` | kapu | Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.) |
| 02 Tervezet/Modulok/M7/M7 – Kapu – értékelő (item-bank + rubrika).md | `M7-KAPU` | kapu | Kapu-fájl: item-bank és rubrika. A benne szereplő plakát-, kártya- és videóemlítések kvíz-szituációk vagy tanulói beadványok, nem legyártandó anyagok; a külső PDF-hivatkozások szakirodalmi források. A kapu Moodle-beállítása a `02 Tervezet/LMS – activity manifest.md` kontrolltáblájában él, nem média-deliverable. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.) |
| 02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzés feedback.md | `Z.4` | online-lecke | Moodle Assignment + Feedback lecke: a tartalmat a tanuló állítja elő (reflexiós szöveg vagy videó), a beállítás a `02 Tervezet/LMS – activity manifest.md`-ben él. Nincs legyártandó média-anyag. (A v1 leltár is ellenőrzötten média nélkülinek sorolta.) |
| 02 Tervezet/Adatvédelem – tanulói adatok és AI.md | `ADATVEDELEM` | program-doc | — |
| 02 Tervezet/Emberi jóváhagyás szükséges.md | `EMBERIJOVAHAGYASSZUKSEGES` | program-doc | — |
| 02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md | `GLOSSZARIUM` | program-doc | — |
| 02 Tervezet/Gyermekvédelem – release gate.md | `GYERMEKVEDELEM` | program-doc | — |
| 02 Tervezet/LMS – H5P runtime acceptance.md | `LMS` | program-doc | — |
| 02 Tervezet/LMS – activity manifest.md | `LMS` | program-doc | — |
| 02 Tervezet/LMS – hozzáférhetőségi sztenderd.md | `LMS` | program-doc | — |
| 02 Tervezet/Program terv.md | `PROGRAMTERV` | program-doc | — |
| 02 Tervezet/RELEASE-READINESS.md | `RELEASEREADINESS` | program-doc | — |
| 02 Tervezet/Terepgyakorlat – 2. félév.md | `TEREPGYAKORLAT` | program-doc | — |

## ⚖️ Emberi döntésre váró tételek

| ID | Fájl | Mit kell eldönteni |
|---|---|---|
| `M3-HUB-POSZ-01` | 02 Tervezet/Modulok/M3/M3 – Kvuca, red flag, felelősség – Csoportdinamika, korosztályok és gyermekvédelem.md | A modul-áttekintő NÉGY lépéses gyermekvédelmi lépés-térkép posztert ír le (észreveszem → jelzek → nem maradok egyedül → bevonás), a peula kanonikus sablonja viszont ÖT csomópontosat, amelynek 2. eleme a nem alkudható instrukció: „Meghallgatom röviden, biztonságosan (nem ígérek 100% titoktartást)”. A v1 leltár a kettőt ugyanannak a médiának vette. Gyermekvédelmi felelős döntse el, hány lépéses a kanonikus lépés-térkép, és igazítsa hozzá a hub összefoglaló mondatát — addig ez a poszter nem gyártható. |
| `M3.B-KART-03` | 02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépés-térkép.md | A v1 leltárban szereplő spec olyan foglalkozásformára épült, amit a jelenlegi tananyag már nem tartalmaz, és a jelenlegi peula-szöveg nem hivatkozik erre a segédanyagra. Emberi döntés kell arról, hogy szükség van-e rá, és ha igen, milyen tartalommal — a témáért felelős szakmai/gyermekvédelmi jóváhagyóval. Az eredeti v1 megfogalmazás a befagyasztott leltárban változatlanul megvan (M3.B-KART-03). |
| `M4.2-ILL-01` | 02 Tervezet/Modulok/M4/Online leckék/M4.2 – Aktív hallgatás & visszatükrözés.md | HOOK-formátum inkonzisztencia az M4 modulon belül: az M4.1-VID-01 beszélőfej-videóval indít (mint az M1–M3 és M6–M7 leckék többsége), de az M4.2-ILL-01, M4.3-ILL-01 és M4.4-ILL-01 mind STATIKUS illusztrációval nyitja a HOOK-ot, beszélőfej-videó nélkül. Ez a modulon belüli nyitó-élmény váltakozása; a tanuló az M4.1 után már videós HOOK-ot várna. — [⟬SZERZŐI DÖNTÉS⟭ M4 HOOK-formátum: javaslat — M4.1 marad videó-HOOK (indokolt), M4.2–4.4 egységes statikus illusztráció + narráció. Megerősítendő.] Döntsd el modul-szinten a HOOK-formátumot (beszélőfej-videó vagy statikus illusztráció + narráció), és tartsd egységesen az M4.1–M4.4 leckéken belül, vagy rögzítsd, miért tér el az M4.1. |

---

Újraépítés: `python3 tools/media_manifest.py build` ·
ellenőrzés: `python3 tools/media_manifest.py check`
