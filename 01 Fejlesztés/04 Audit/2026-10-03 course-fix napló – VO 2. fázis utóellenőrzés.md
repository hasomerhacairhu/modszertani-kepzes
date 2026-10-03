# course-fix napló – VO 2. fázis utóellenőrzés (2026-10-03)

> **Audit trail, nem kánon.** A `/course-fix` nagy csomagos futásának lépésenkénti naplója
> (`.claude/skills/course-fix/nagy-csomag.md`). A napló a sorrendet és az állapotot rögzíti; bizonyíték a
> fájlok végállapota.

- **Forrás:** `01 Fejlesztés/04 Audit/2026-10-03 Fix pack – VO 2. fázis utóellenőrzés.md`, UF-01…UF-16,
  124 lépés, 36 fájl. Döntési alap: a VO 2. fázis projektgazdai döntéscsomagja (VO D-01…D-23, 2026-10-03-A
  és -B) és a kiegészítő döntések (K2–K4), mindkettő a `01 Fejlesztés/04 Audit/` döntési jegyzőkönyveiben.
- **Bázis:** a csomag `6859fcc`-re készült; a munkaágon (`vo/phase2-course-fix`) azóta csak maga a csomagfájl
  került be (`6d82b3a`), a 36 célfájl a bázison azonos.
- **Sorrend:** a csomag lépéssorrendje (UF-01 → UF-16); az UF-13 (l) az UF-04 javított szövegére horgonyoz.
- **Köztes állapot:** fájlcsoportonként csak `content_integrity.py` és `git diff --check` fut; a pin, a build,
  a `check`/`reconcile` és a tesztek a végén.

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| UF-01 | — | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| UF-02 | a | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | a három szövegrész a lecke saját szövegében megvan (3, 4, 8 előfordulás); beágyazott idézőjel ‘…’ a szerkesztői szabály szerint |
| UF-02 | b | test_media_manifest.py | alkalmazva | |
| UF-02 | c | test_media_manifest.py | alkalmazva | |
| UF-03 | a | M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md | alkalmazva | `replace_all`, 2 előfordulás |
| UF-03 | b | M3.3 – Gyermekvédelem 101 – red flag felismerése & első lépések.md | alkalmazva | csak a gondolatjel |
| UF-04 | — | Emberi jóváhagyás szükséges.md | alkalmazva | |
| UF-05 | a | LMS – H5P runtime acceptance.md | alkalmazva | a „látható”-e kérdés (gombbal megnyitható leirat) emberi döntés marad (UE-IMPL-4) |
| UF-05 | b | LMS – H5P runtime acceptance.md | alkalmazva | |
| UF-06 | — | LMS – H5P runtime acceptance.md | alkalmazva | |
| UF-07 | a | PRODUCTION-DECISIONS.md | alkalmazva | most igazolva: `MEDIA-PRODUCTION-PLAN.md` R3 = 116 |
| UF-07 | b | PRODUCTION-DECISIONS.md | alkalmazva | most igazolva: BATCH 3 = 117 asset / 366 deliverable |
| UF-07 | c | PRODUCTION-DECISIONS.md | alkalmazva | most igazolva: R2 = 118 (29 vizuális + 89 hang) |
| UF-07 | d | PRODUCTION-DECISIONS.md | alkalmazva | most igazolva: az R2 önmagában 2 / 4 |
| UF-07 | e | PRODUCTION-STACK.md | alkalmazva | |
| UF-07 | f | RIGHTS-EVIDENCE.md | alkalmazva | most igazolva: a tábla R2-1…R2-6 állapotai |
| UF-07 | g | RIGHTS-EVIDENCE.md | alkalmazva | most igazolva: 415 szemantikus asset |
| UF-08 | — | RIGHTS-EVIDENCE.md | alkalmazva | most igazolva: AI beszélőfej-videó = 18 |
| UF-09 | — | VOICE-BIBLE.md | alkalmazva | most igazolva (elsődleges forrás): W3C WebVTT 6.5. „WebVTT cue text DOM construction rules” — a Voice Object „HTML span element with a title attribute set to the WebVTT Voice Object’s value”, tehát nem megjelenített szöveg; a verziócímkét az `M1.3-NAR-08-VO` mondja („A képen ez a felirat: első verzió – címke”) |
| UF-10 | — | VOICE-PILOT-SCRIPTS.md | alkalmazva | most igazolva: a tesztlap 4. = kiejtési figyelőlista, 5. = pontozólap (SRC-01/SRC-02 oszlopok), a lap fejléce szerint történeti; e lap 6. = elfogadási feltétel |
| UF-11 | — | VOICE-BIBLE.md | alkalmazva | most igazolva: VO D-07 („Pronounce: száztizenkettő … Do not pronounce it as egy-egy-kettő”); a manifestben a 112 csak az `M3.3-NAR-01` forrásszövegében áll. Vétólista: gyermekvédelmi kontextus, csak kiejtési szabály |
| UF-12 | a | PRODUCTION-DECISIONS.md | alkalmazva | |
| UF-12 | b | PRODUCTION-DECISIONS.md | alkalmazva | 18 sor; mindegyik most összevetve a döntési jegyzőkönyvvel (VO D-04…D-23, ADDENDUM 1–2) és a kiegészítéssel (K2–K4) |
| UF-12 | c | PRODUCTION-DECISIONS.md | alkalmazva | VO D-21 |
| UF-13 | a | VOICE-BIBLE.md | alkalmazva | a futás eleji ellenőrzés után (bizonyíték 1/1, a sor azóta nem változott); a felváltott sor: HUM-MEDIA-02 „**Implementáció:** a `VOICE-BIBLE.md` csak a ténylegesen létrehozott, jogosult voice ID-t kapja meg” |
| UF-13 | b | VOICE-BIBLE.md | alkalmazva | |
| UF-13 | c | PRODUCTION-DECISIONS.md | alkalmazva | |
| UF-13 | d | PRODUCTION-DECISIONS.md | alkalmazva | |
| UF-13 | e | PRODUCTION-DECISIONS.md | alkalmazva | |
| UF-13 | f | README.md | alkalmazva | |
| UF-13 | g | README.md | alkalmazva | |
| UF-13 | h | RIGHTS-EVIDENCE.md | alkalmazva | |
| UF-13 | i | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| UF-13 | j | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| UF-13 | k | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| UF-13 | l | Emberi jóváhagyás szükséges.md | alkalmazva | az UF-04 után; a HUM-MEDIA-02 dátuma, jóváhagyója és bizonyítéka nem változott. Vétólista: HUM-szöveg |
| UF-14 | a | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | a `decision` mező a D11-re hivatkozik tovább |
| UF-14 | b | Emberi jóváhagyás szükséges.md | alkalmazva | az UF-13 (l) után (ugyanaz a bekezdés). Vétólista: HUM-szöveg |
| UF-14 | c | VOICE-BIBLE.md | alkalmazva | |
| UF-14 | d | VOICE-BIBLE.md | alkalmazva | |
| UF-14 | e | VOICE-BIBLE.md | alkalmazva | a D6 szkript és a forrásblokk érintetlen |
| UF-14 | f | VOICE-BIBLE.md | alkalmazva | |
| UF-14 | g | VOICE-BIBLE.md | alkalmazva | |
| UF-14 | h | PRODUCTION-DECISIONS.md | alkalmazva | a 2026-10-03-i döntésblokk érintetlen, keltezett kiegészítő sor alatta |
| UF-14 | i | PRODUCTION-DECISIONS.md | alkalmazva | |
| UF-14 | j | PRODUCTION-DECISIONS.md | alkalmazva | |
| UF-14 | k | PRODUCTION-DECISIONS.md | alkalmazva | |
| UF-14 | l | PRODUCTION-STACK.md | alkalmazva | |
| UF-14 | m | PRODUCTION-STACK.md | alkalmazva | |
| UF-14 | n | PRODUCTION-STACK.md | alkalmazva | |
| UF-14 | o | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| UF-14 | p | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| UF-14 | q | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| UF-14 | r | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| UF-15 | a | produkcios-szabalyok.json | alkalmazva | a JSON érvényes |
| UF-15 | b | produkcios-szabalyok.json | alkalmazva | egy ⟬KITÖLTENDŐ⟭ szándékosan marad (az R3 nyitott) |
| UF-16 | M1.1-NAR-02 | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | UF-16 előtt most igazolva a manifestből: mind a 70 asset `voiceover`/`narration`, egyiket sem építi be videó (`composed_of`/`reuse_of` üres), mindegyiknek van `captions` és `transcript` derivatívája |
| UF-16 | M1.1-NAR-05 | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | |
| UF-16 | M1.1-NAR-06 | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | |
| UF-16 | M1.2-NAR-04 | M1.2 – Megfigyelés ≠ értelmezés.md | alkalmazva | |
| UF-16 | M1.2-NAR-05 | M1.2 – Megfigyelés ≠ értelmezés.md | alkalmazva | |
| UF-16 | M1.2-NAR-06 | M1.2 – Megfigyelés ≠ értelmezés.md | alkalmazva | |
| UF-16 | M1.3-NAR-01 | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| UF-16 | M1.3-NAR-02 | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| UF-16 | M1.3-NAR-03 | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| UF-16 | M1.3-NAR-04 | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| UF-16 | M1.3-NAR-05 | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| UF-16 | M1.3-NAR-06 | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| UF-16 | M1.3-NAR-07 | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| UF-16 | M1.4-NAR-01 | M1.4 – Miniszituációk – Mondd el SBI-ben.md | alkalmazva | |
| UF-16 | M1.4-NAR-02 | M1.4 – Miniszituációk – Mondd el SBI-ben.md | alkalmazva | |
| UF-16 | M1.4-NAR-03 | M1.4 – Miniszituációk – Mondd el SBI-ben.md | alkalmazva | |
| UF-16 | M2.1-NAR-02 | M2.1 – Ki vagyok én madrihként – identitás-körök.md | alkalmazva | határeset: „Kíséri az M2.1-DIA-01 animációt” — az ábra külön asset (diagram, a feliratok sorban felvillannak, saját alt-szöveg és bullet-ekvivalens), szinkron nincs előírva; ha a megvalósításban a narrációhoz időzített animáció lesz, a felirat-követelmény visszatér (K2 hatókör-korlát) |
| UF-16 | M2.1-NAR-03 | M2.1 – Ki vagyok én madrihként – identitás-körök.md | alkalmazva | |
| UF-16 | M2.1-NAR-04 | M2.1 – Ki vagyok én madrihként – identitás-körök.md | alkalmazva | |
| UF-16 | M2.2-NAR-02 | M2.2 – Értékeim mint iránytű.md | alkalmazva | |
| UF-16 | M2.2-NAR-03 | M2.2 – Értékeim mint iránytű.md | alkalmazva | |
| UF-16 | M2.3-NAR-02 | M2.3 – Somer 3 pillére – mini-kapszula.md | alkalmazva | |
| UF-16 | M2.4-NAR-02 | M2.4 – Reflektív napló & határok – A dugma isit nem terapeuta.md | alkalmazva | |
| UF-16 | M2.4-NAR-03 | M2.4 – Reflektív napló & határok – A dugma isit nem terapeuta.md | alkalmazva | |
| UF-16 | M2.4-NAR-04 | M2.4 – Reflektív napló & határok – A dugma isit nem terapeuta.md | alkalmazva | |
| UF-16 | M3.1-NAR-03 | M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md | alkalmazva | |
| UF-16 | M3.1-NAR-04 | M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md | alkalmazva | |
| UF-16 | M3.1-NAR-05 | M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md | alkalmazva | |
| UF-16 | M3.2-NAR-03 | M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md | alkalmazva | |
| UF-16 | M3.2-NAR-04 | M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md | alkalmazva | |
| UF-16 | M3.2-NAR-05 | M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md | alkalmazva | |
| UF-16 | M3.4-NAR-02 | M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md | alkalmazva | |
| UF-16 | M4.1-NAR-06 | M4.1 – Mit üzen a testem – Nonverbális kiállás.md | alkalmazva | |
| UF-16 | M4.1-NAR-07 | M4.1 – Mit üzen a testem – Nonverbális kiállás.md | alkalmazva | |
| UF-16 | M4.2-NAR-01 | M4.2 – Aktív hallgatás & visszatükrözés.md | alkalmazva | |
| UF-16 | M4.2-NAR-02 | M4.2 – Aktív hallgatás & visszatükrözés.md | alkalmazva | |
| UF-16 | M4.2-NAR-03 | M4.2 – Aktív hallgatás & visszatükrözés.md | alkalmazva | |
| UF-16 | M4.2-NAR-04 | M4.2 – Aktív hallgatás & visszatükrözés.md | alkalmazva | |
| UF-16 | M4.3-NAR-01 | M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md | alkalmazva | |
| UF-16 | M4.3-NAR-02 | M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md | alkalmazva | |
| UF-16 | M4.3-NAR-03 | M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md | alkalmazva | |
| UF-16 | M4.4-NAR-01 | M4.4 – 45 mp-es peulabemutató – vázlat egy konkrét kvucára.md | alkalmazva | |
| UF-16 | M4.4-NAR-02 | M4.4 – 45 mp-es peulabemutató – vázlat egy konkrét kvucára.md | alkalmazva | |
| UF-16 | M4.4-NAR-03 | M4.4 – 45 mp-es peulabemutató – vázlat egy konkrét kvucára.md | alkalmazva | |
| UF-16 | M4.4-NAR-05 | M4.4 – 45 mp-es peulabemutató – vázlat egy konkrét kvucára.md | alkalmazva | |
| UF-16 | M5.1-NAR-02 | M5.1 – Mi a nonformális nevelés – Suli, Somer, random.md | alkalmazva | |
| UF-16 | M6.2-NAR-02 | M6.2 – Történet, mint tükör.md | alkalmazva | |
| UF-16 | M6.2-NAR-04 | M6.2 – Történet, mint tükör.md | alkalmazva | |
| UF-16 | M6.2-NAR-05 | M6.2 – Történet, mint tükör.md | alkalmazva | |
| UF-16 | M6.2-NAR-06 | M6.2 – Történet, mint tükör.md | alkalmazva | |
| UF-16 | M6.2-NAR-07 | M6.2 – Történet, mint tükör.md | alkalmazva | |
| UF-16 | M6.3-NAR-01 | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| UF-16 | M6.3-NAR-02 | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| UF-16 | M6.3-NAR-03 | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| UF-16 | M6.3-NAR-04 | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| UF-16 | M6.3-NAR-05 | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| UF-16 | M6.3-NAR-06 | M6.3 – Kézműves, ami tanít is.md | alkalmazva | |
| UF-16 | M7.1-NAR-01 | M7.1 – Ez még csak vágy, nem cél – SMART nevelési cél someres módra.md | alkalmazva | |
| UF-16 | M7.2-NAR-02 | M7.2 – Nemcsak játék, hanem peula – 11 tervezési pont & AI-támogatás.md | alkalmazva | |
| UF-16 | M7.2-NAR-03/04/05 | M7.2 – Nemcsak játék, hanem peula – 11 tervezési pont & AI-támogatás.md | alkalmazva | `replace_all`, 3 előfordulás; a lektorálási kitétel marad |
| UF-16 | M7.3-NAR-02 | M7.3 – Zmán Kvucá-checklist – idő, tér, felelősség.md | alkalmazva | |
| UF-16 | M7.3-NAR-03 | M7.3 – Zmán Kvucá-checklist – idő, tér, felelősség.md | alkalmazva | |
| UF-16 | M7.3-NAR-04 | M7.3 – Zmán Kvucá-checklist – idő, tér, felelősség.md | alkalmazva | |
| UF-16 | M7.3-NAR-05 | M7.3 – Zmán Kvucá-checklist – idő, tér, felelősség.md | alkalmazva | |
| UF-16 | M7.4-NAR-01 | M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md | alkalmazva | |
| UF-16 | M7.4-NAR-02 | M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md | alkalmazva | |
| UF-16 | Z.1-NAR-01 | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |
| UF-16 | Z.1-NAR-02 | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |

## Összesítés és záró ellenőrzés

- **Állapot:** 124 / 124 `alkalmazva`; `már alkalmazva`, `kihagyva`, `megállva` nincs. A végállapot lépésenként
  visszaolvasva (bizonyíték-blokk 0×, javítás-blokk a lépés szerinti darabszámmal; a három beszúró lépésnél — UF-12 (b),
  UF-14 (h), (i) — a horgony a helyén, az új sorok megvannak; az UF-13 (l) szövegét az UF-14 (b) folytatja).
- **Diff:** 36 célfájl + ez a napló, a teljes diff visszaolvasva; csomagon kívüli változás nincs.
- **Ellenőrzések:** `py_compile` OK · `content_integrity.py` 0 ERROR · `--pin-visible` 5 fájl (M1.3, M3.1, M3.3,
  `Emberi jóváhagyás szükséges.md`, `LMS – H5P runtime acceptance.md`) · `build` ×2 bájtra azonos (415 asset, 903
  deliverable, 123 forrásblokk; 6 generált kimenet változott) · `check` OK · `reconcile` 747/747 · `validate` OK ·
  `lint --high-only` 0 · `unittest` 150 OK · `git diff --check` tiszta · hangnév-ellenőrzés a diffen 0 találat ·
  `--release-report`: `RELEASE-VERDICT: NO-GO` (a 6 blokkoló változatlan).

## Célzott újraellenőrzés (diff-hunkok, lencsénként) — nyitott findingok

A négy specialista (nyelvi, megvalósíthatósági, pedagógiai, biztonsági) csak a módosított sorokat kapta. A findingok
nem verifikáltak, és ebben a futásban nem javítottuk őket: `/course-review`/`verifier` után egy következő
`/course-fix` bemenetei lehetnek. Összevonva (azonos hely egy sorban):

| ID | Hely | Probléma (röviden) | Javaslat / típus |
|---|---|---|---|
| UE2-BIZT-1 (P1) | `VOICE-BIBLE.md` 7. „Segélyvonalak” (UF-11) | a 112 `M3.3-NAR-01-VO`-beli előfordulása a „kivétel” helyett leíró „Ma egyedül” mondat lett; a D-07 csak a kiejtésről szól | a normatív kivétel visszaállítása („kizárólag ott hangzik el”), a kiejtési szabály marad; más elhelyezés Memuna-döntés — objektív, gyermekvédelmi vétólista |
| UE2-BIZT-2 | HUM-MEDIA-02 2026-10-03-i bekezdés; `VOICE-BIBLE.md` Voice-ID sor (UF-13 a, l) | a „felváltja” az egész „Implementáció” sorra szól, a K3 csak a helyről döntött; a „ténylegesen létrehozott, jogosult” feltétel kiesett | a felváltás csak a helyre vonatkozzon, a jogosultsági feltétel maradjon; ha a projektgazda mást akart: emberi döntés |
| UE2-BIZT-3 | `RIGHTS-EVIDENCE.md` R2-4, `VOICE-BIBLE.md`, HUM (K3) | a K3 jövő idejű („lesz”), az új szöveg tényként állítja, hogy a voice-ID ott „él” | a K3 szerint: „a voice-ID helye a VO QA-repó gyártási konfigurációja” |
| UE2-IMPL-1 (P1) | M6.2 (5), M6.3 (6) csak hangos narráció előtti látható ♿ sor | „Felirat + teljes szöveges leirat…” a H5P Audio-hoz, ellentmond az új a11y-jegyzetnek és a runtime 22. pontnak | a látható sor a VO D-19 szerint; a két M6.2-videónál a felirat marad; pin |
| UE2-IMPL-2 | `PILOT-PRODUCTION-PACK.md` P-NAR checklist, `PRODUCTION-STACK.md` „Leirat” sor | a linkelt leirat-oldalt még megengedik, a runtime 22. pont már „mellett látható”-t vár | csak hangos narrációnál a D-19 szövegére igazítás; a gombos/lenyitható leirat kérdése az UE-IMPL-4 emberi döntése |
| UE2-IMPL-3 = UE2-NYELV-2 | M4.1-NAR-06/07 `a11y.note` | a megmaradt „a slide-szöveg részben … lefedi” a „teljes szöveges ekvivalens” után tárgy nélkül áll, és gyengítésként olvasható | a tárgy megnevezése („a narráció szövegét…”), a „teljes” követelmény nem gyengülhet |
| UE2-IMPL-4 | M6.1-NAR-02…06, M4.1-NAR-02 `a11y.note` | a K2 („Mindre, egységesen”) ezeket nem érte el (M6.1: „felirat ajánlott”, nincs AI-címkés első sor) | átvezetés a K2-sablonra; az M4.1-NAR-02-nél csak a csak hangos ág |
| UE2-IMPL-5 | `RIGHTS-EVIDENCE.md` 1/A. bevezető (99–101. sor) | a voice-ID-t hiányzóként sorolja; „mind megvan még.**” — fordított jelentés és árva `**` (a futás előtti állapot) | a K3 átvezetése a zárójeles 2026-10-03-i részbe, a jelentés és a `**` javítása |
| UE2-IMPL-6 | `PRODUCTION-DECISIONS.md` D2 („a lap nem osztja ki neki”) | a második hang szerepe a D11/K4 szerint már kiosztva | datált utalás: „(2026-10-03: eldőlt — VO D-14, K4, lásd D11)” |
| UE2-PED-1 = UE2-NYELV-4 | `M1.3-NAR-08-VO` 4. rész (UF-02) | felolvasva az idézőjel nem hallatszik; a narrátor és Madrih A hangja azonos (K4), ezért A szavainak idézése hallásra összemosódik; a 4. rész ~13–16 mp | helyzetet mondjon idézet helyett (pl. „az első mondata elején / közepén / végén”), vagy hallható idézet-bevezetés; teszt-őr és pin együtt; a QA-oldalon újramérés |
| UE2-PED-2 | M3.1-NAR-04 `notes` („feliratot+leiratot is kér”); M1.3-NAR-01 (`technical`: opcionálisan beszélőfej) | blokkon belüli ellentmondás az új a11y-jegyzettel | M3.1: „a dián látható leiratot is kér (VO D-19)”; M1.3-NAR-01: feltétel, ha beszélőfejes videó készül |
| UE2-PED-3 | az új a11y-jegyzetek „mellett látható leirat” | állandóan nyitott teljes szöveg redundancia-hatást okozhat | emberi döntés — az UE-IMPL-4 maradékához (projektgazda + hozzáférhetőségi gazda) |
| UE2-NYELV-1 | Z.1-NAR-01/02 `notes` és a hivatkozó sor (173., 216., 490.) | a CAPTIONS-t nevezi szöveges ekvivalensnek, az új a11y-jegyzet a TRANSCRIPT-et | a szöveges ekvivalens a `::TRANSCRIPT` legyen (VO D-19, K2) |
| UE2-NYELV-3 | `PILOT-PRODUCTION-PACK.md` P-KAR, `PRODUCTION-STACK.md` 243., 569. | a K4 „a kalibrálása után” feltétele kimaradt (elveszett minősítő) | „Madrih B: a második hang (a kalibrálása után)” |
| UE2-NYELV-5 | `VOICE-BIBLE.md` 9. Párbeszéd (UF-09) | „hangjelölés” — a korpusz szava „beszélőjelölés” | „beszélőjelölés” |
| UE2-NYELV-6 | M1.3 `decision` (UF-14 a) | „a dialógushangokat … eldöntötte” — vonzat | „a dialógushangokról … döntött” |
| UE2-NYELV-7 | `VOICE-BIBLE.md` 8., 11.; `PRODUCTION-DECISIONS.md` D11-kiegészítés | „Madrih B-t … mondja”, „az M4.1-jeleneteket … mondja” — tárgy | „Madrih B szerepét …”, „az M4.1-jelenetek narrációját …” |
| UE2-NYELV-8 | a K2-sablon feltételes változata (7 hely) | „Ha legyártják: … kötelező: csak hang” — két kettőspont | „Ha legyártják, a leirat/transzkript (…) kötelező: csak hang, …” |
| (hatókörön kívül) | `PRODUCTION-DECISIONS.md` VO D-18 sor | párosítatlan zárójel („(a) opció; … 2026-10-03).”) | központozás |

**Rendben talált pontok (újraellenőrzés):** a darabszámok egyeznek a `MEDIA-PRODUCTION-PLAN.md`-vel; a WebVTT-állítás
helyes (W3C WebVTT 6.5); a `::CAPTIONS`/`::TRANSCRIPT` hivatkozások érvényes derivatívákra mutatnak; nem maradt
„a voice-ID rögzítési helye nyitott” mondat; a HUM-MEDIA-02 dátuma, jóváhagyója és bizonyítéka változatlan; jogi,
DPO- vagy Memuna-jóváhagyást az új szöveg nem állít (VO D-08); nem nyilvános adat nem került be.

**Verifikáció és továbbvezetés (2026-10-03, a PR #13 merge-e után):** három független `verifier`-kör. MEGERŐSÍTVE vagy
RÉSZBEN (objektív rész): UE2-BIZT-1, UE2-IMPL-1…6, UE2-PED-1 (= UE2-NYELV-4), UE2-PED-2, UE2-NYELV-1, -3, -6, -7, -8
→ `2026-10-03 Fix pack – VO 2. fázis, 3. csomag.md` (P3-01…P3-14), a K5 tényközlés átvezetésével (P3-15). ELVETVE:
UE2-BIZT-2, UE2-BIZT-3, UE2-NYELV-5, a VO D-18 sor „zárójele”. Emberi döntés: UE2-PED-3 (az UE-IMPL-4 maradéka), az
`M4.1-NAR-02` besorolása.

## Vétólista

- **Answer key, helyes-válasz jelölés, elosztó, küszöb, rubrika, kapu-típus, completion, időtartam:** nincs változás.
- **Gyermekvédelmi megfogalmazás:** `VOICE-BIBLE.md` 7. „Segélyvonalak” (UF-11; VO D-07) — előtte: „**Kivétel: a 112** az
  `M3.3-NAR-01-VO` gyermekvédelmi lépéssorában elhangzik, „száztizenkettő” alakban”; utána: „— **kivéve a 112-t**, amely
  mindig „száztizenkettő” alakban hangzik el, soha nem „egy-egy-kettő”-ként. Ma egyedül az `M3.3-NAR-01-VO`
  gyermekvédelmi lépéssorában hangzik el”. Lásd UE2-BIZT-1. M3.3: csak gondolatjel (UF-03 b).
- **Jog / adatvédelem / HUM:** `Emberi jóváhagyás szükséges.md` HUM-MEDIA-02 2026-10-03-i bekezdés (UF-04, UF-13 l,
  UF-14 b) — központozás, K3 voice-ID-hely, K4 dialógushangok; a lezárt tétel dátuma, jóváhagyója, bizonyítéka nem
  változott. Lásd UE2-BIZT-2, -3.
- **Akadálymentesség:** UF-05, UF-09, UF-16 — összehangolás a VO D-19-cel és a K2-vel; szinkronizált videónál a
  felirat-követelmény nem változott. Határeset: `M2.1-NAR-02` (lásd a sorát).
