# course-fix napló – VO 2. fázis, 3. csomag (2026-10-03)

> **Audit trail, nem kánon.** A `/course-fix` nagy csomagos futásának lépésenkénti naplója
> (`.claude/skills/course-fix/nagy-csomag.md`). A napló a sorrendet és az állapotot rögzíti; bizonyíték a
> fájlok végállapota.

- **Forrás:** `01 Fejlesztés/04 Audit/2026-10-03 Fix pack – VO 2. fázis, 3. csomag.md`, P3-01…P3-15, 45 lépés,
  19 fájl. Alap: a follow-up pack utáni célzott újraellenőrzés verifikált findingjai (UE2-…) és a projektgazda K5
  tényközlése; döntések: VO D-07, D-08, D-14, D-15, D-18, D-19, D-21, K2–K5 (`01 Fejlesztés/04 Audit/` döntési
  jegyzőkönyvei).
- **Bázis:** a csomag `332862b`-re készült; a munkaágon (`vo/phase2-fix-pack-3`) azóta csak maga a csomagfájl és
  az előző napló kiegészítése került be (`a8e2f37`), a 19 célfájl a bázison azonos.
- **Sorrend:** a csomag lépéssorrendje (P3-01 → P3-15).
- **Köztes állapot:** fájlcsoportonként csak `content_integrity.py` és `git diff --check` fut; a pin, a build,
  a `check`/`reconcile` és a tesztek a végén.

| ID | lépés | fájl | állapot | megjegyzés |
|---|---|---|---|---|
| P3-01 | — | VOICE-BIBLE.md | alkalmazva | vétólista: gyermekvédelmi kontextus; a „narrációban nem hangzanak el” alapszabály, a 116-os mondat és a Memuna-hivatkozás érintetlen |
| P3-02 | a | M6.3 – Kézműves, ami tanít is.md | alkalmazva | `replace_all`, 6 előfordulás, mind csak hangos narráció (M6.3-NAR-01…06) fölött |
| P3-02 | b | M6.2 – Történet, mint tükör.md | alkalmazva | |
| P3-02 | c | M6.2 – Történet, mint tükör.md | alkalmazva | |
| P3-02 | d | M6.2 – Történet, mint tükör.md | alkalmazva | |
| P3-02 | e | M6.2 – Történet, mint tükör.md | alkalmazva | |
| P3-02 | f | M6.2 – Történet, mint tükör.md | alkalmazva | az M6.2-VID-01/02 két videós ♿ sora (119., 386.) a felirattal marad |
| P3-03 | a | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| P3-03 | b | PRODUCTION-STACK.md | alkalmazva | |
| P3-04 | a | M4.1 – Mit üzen a testem – Nonverbális kiállás.md | alkalmazva | |
| P3-04 | b | M4.1 – Mit üzen a testem – Nonverbális kiállás.md | alkalmazva | |
| P3-05 | a | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | most igazolva a manifestből: M6.1-NAR-02…07 `voiceover`/`narration`, „Hang (TTS)…”, `captions` + `transcript` derivatíva |
| P3-05 | b | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | |
| P3-05 | c | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | |
| P3-05 | d | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | |
| P3-05 | e | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | |
| P3-05 | f | M6.1 – Játék-kategóriák 3 aktuális kvucára.md | alkalmazva | a videóág felirat-követelménye marad |
| P3-06 | — | RIGHTS-EVIDENCE.md | alkalmazva | |
| P3-07 | a | PRODUCTION-DECISIONS.md | alkalmazva | beszúrás a történeti mondat mögé; a horgony marad |
| P3-07 | b | PRODUCTION-DECISIONS.md | alkalmazva | |
| P3-08 | a | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | most igazolva: a „Mit látunk?” (236–238.) mindhárom ikont a megnevezett szövegrészhez köti; a párbeszéd forrásában (252–260.) nincs „résznél” |
| P3-08 | b | test_media_manifest.py | alkalmazva | az `assertNotIn("résznél", …)` őr változatlan |
| P3-09 | a | M3.1 – Történetek egy kvucáról – Tuckman-szakaszok felismerése.md | alkalmazva | |
| P3-09 | b | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| P3-10 | a | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |
| P3-10 | b | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |
| P3-10 | c | Z.1 – Visszanéző tükör – M0–M7 idővonal.md | alkalmazva | |
| P3-11 | a | PILOT-PRODUCTION-PACK.md | alkalmazva | |
| P3-11 | b | PRODUCTION-STACK.md | alkalmazva | |
| P3-11 | c | PRODUCTION-STACK.md | alkalmazva | |
| P3-12 | — | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva | |
| P3-13 | a | VOICE-BIBLE.md | alkalmazva | |
| P3-13 | b | VOICE-BIBLE.md | alkalmazva | |
| P3-13 | c | VOICE-BIBLE.md | alkalmazva | |
| P3-13 | d | PRODUCTION-DECISIONS.md | alkalmazva | |
| P3-14 | a | M1.1 – Johari-ablak – vakfoltjaim felismerése.md | alkalmazva | |
| P3-14 | b | M1.2 – Megfigyelés ≠ értelmezés.md | alkalmazva | |
| P3-14 | c | M1.2 – Megfigyelés ≠ értelmezés.md | alkalmazva | |
| P3-14 | d | M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md | alkalmazva | |
| P3-14 | e | M7.3 – Zmán Kvucá-checklist – idő, tér, felelősség.md | alkalmazva | |
| P3-14 | f | M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md | alkalmazva | |
| P3-14 | g | M7.4 – Peula v1 + AI – első modulproduktum-vázlat.md | alkalmazva | |
| P3-15 | a | ELEVENLABS-VOICE-TEST.md | alkalmazva | |
| P3-15 | b | RIGHTS-EVIDENCE.md | alkalmazva | K5: tényközlés; jóváhagyást nem állít, személyes adat nincs |
| P3-15 | c | PRODUCTION-DECISIONS.md | alkalmazva | |

## Összesítés és záró ellenőrzés

- **Állapot:** 45 / 45 `alkalmazva`; `már alkalmazva`, `kihagyva`, `megállva` nincs. A végállapot lépésenként
  visszaolvasva (bizonyíték-blokk 0×, javítás-blokk a lépés szerint; a két beszúró lépésnél — P3-07 (a), P3-15 (a) —
  a horgony a helyén, az új sorok megvannak). Az M6.2 két videós ♿ sora (M6.2-VID-01/02) a felirattal maradt.
- **Diff:** 19 célfájl + ez a napló, a teljes diff visszaolvasva; csomagon kívüli változás nincs.
- **Ellenőrzések:** `py_compile` OK · `content_integrity.py` 0 ERROR · `--pin-visible` 3 fájl (M1.3, M6.2, M6.3) ·
  `build` ×2 bájtra azonos (415 asset, 903 deliverable, 123 forrásblokk; 6 generált kimenet változott) · `check` OK ·
  `reconcile` 747/747 · `validate` OK · `lint --high-only` 0 · `unittest` 150 OK · `git diff --check` tiszta ·
  hangnév-ellenőrzés a diffen 0 találat · `--release-report`: `RELEASE-VERDICT: NO-GO` (a 6 blokkoló változatlan).

## Célzott újraellenőrzés (diff-hunkok, lencsénként) — nyitott findingok

Nem verifikáltak, ebben a futásban nem javítottuk őket (azonos hely egy sorban):

| ID | Hely | Probléma (röviden) | Javaslat / típus |
|---|---|---|---|
| UE3-BIZT-1 | `VOICE-BIBLE.md` 7. „Segélyvonalak” (P3-01) | a „száztizenkettő” kiejtés az `M3.3-NAR-01-VO`-hoz kötött; az előtte álló „számjegyenként” szabály miatt egy jövőbeli új elhelyezésnél a D-07-tel ellentétes kiejtés adódna | két mondat: elhelyezés (egyetlen engedett hely az `M3.3-NAR-01-VO`) és kiejtés (a 112 mindig „száztizenkettő”, VO D-07); az alapszabály, a 116 és a Memuna-hivatkozás marad — objektív, gyermekvédelmi vétólista |
| UE3-BIZT-2 = UE3-IMPL-1 | HUM-MEDIA-02 2026-10-03-i bekezdés; `PRODUCTION-DECISIONS.md` K5 sor | a K5 jegyzőkönyve a HUM-MEDIA-02-t is átvezetési helynek nevezi, a 3. csomag kihagyta | a K5 mondata a HUM-bekezdésbe (jóváhagyás-állítás és személyes adat nélkül) és a K5 sor 3. oszlopába; pin kell (a HUM-fájl pinnelt) |
| UE3-BIZT-3 | `ELEVENLABS-VOICE-TEST.md` 1.0. (K5-mondat) | a formális igazolást a `VOICE-RIGHTS-REGISTER`-hez köti, de a nagykorúság igazolása nincs a nyilvántartás kötelező mezői között | EMBERI DÖNTÉS — DPO + jogi felelős: kerüljön-e a nyilvántartásba (pl. „ellenőrizve: igen/nem”, szerep, dátum; életkor/születési dátum nélkül), és a V2 része-e |
| UE3-IMPL-2 | M1.3-NAR-01 `a11y.note` (P3-09 b) | a videóág felirata nincs a meglévő `::CAPTIONS` derivatívához kötve (az M6.1-NAR-07 igen) | „az M1.3-NAR-01::CAPTIONS a videó kapcsolható, szinkron magyar feliratsávja, és kötelező (WCAG 2.2 SC 1.2.2)” — a csak hangos ág „archivált” státusza marad |
| UE3-PED-3 | M1.3-NAR-01 `a11y.note` (P3-09 b) | a videófelirat kötelezettségét a K2-nek tulajdonítja; a forrása a WCAG 1.2.2 (a K2 hatókörén kívül) | a zárójel „(WCAG 2.2 SC 1.2.2)”, az M6.1-NAR-07 mintájára — az UE3-IMPL-2-vel együtt |
| UE3-PED-1 = UE3-NYELV-1 | `M1.3-NAR-08-VO` 4. rész (P3-08) | felolvasva csak a pontosvessző választja el az idézeteket; „a B ennél:” hasonlításnak is hallható; azonos hang (K4) | három külön mondat, mindhárom „ennél a résznél” (NYELV-1); a spec és a gyártási jegyzet kapjon hallgatási próba-kritériumot (PED-1); teszt-őr és pin együtt |
| UE3-PED-2 | `M1.3-NAR-08-VO` 4. rész helye és a „kb. 25–35 mp” | a 4. rész ~19 mp az SBI-mondat és Madrih B reakciója között (az 1. verzióban ~2 mp); a teljes képleírás ~39 mp | (1) a QA-újramérés után a mért hossz az időkeretbe (külön számváltozás); (2) EMBERI DÖNTÉS — projektgazda: maradjon-e a hozzárendelés A és B között, vagy kerüljön B replikája utánra |
| UE3-NYELV-2 | `RIGHTS-EVIDENCE.md` 101. sor (P3-06) | „a hiányzó rész — voice-ID, modell, … — mind nyitott még”, miközben a zárójel szerint „a modell eldőlt” | a „modell” kikerül a felsorolásból |
| UE3-NYELV-3 | M6.1-NAR-07 `a11y.note` | a második hivatkozás „WCAG 1.2.2” (az első „WCAG 2.2 SC 1.2.1”) | „(WCAG 2.2 SC 1.2.2)” |
| UE3-NYELV-4 | `PRODUCTION-DECISIONS.md` 168. sor (P3-07 a) | a beszúrt „… Madrih B szerepét mondja” alany nélkül áll; az előző alany „ez a lap” | „eldőlt — az első gyártási körben a második hang mondja az `M1.3-VID-01` Madrih B szerepét, a kalibrálása után; …” |

**Rendben talált pontok:** a 112-es alapszabály, a 116-os szabály és a Memuna vétó/QA megmaradt, az `M3.3-NAR-01-VO`
a tiltás megnevezett kivétele; a K5-szövegek nem állítanak jóváhagyást, és nincs bennük személyes adat; minden
`::CAPTIONS`/`::TRANSCRIPT` hivatkozás létező derivatívára mutat; a videós felirat-követelmények megmaradtak; a K5
táblasor formailag illeszkedik; az új képleírás-mondat a „Mit látunk?” tényeit mondja, és nem árul el többet a
kérdések válaszából, mint az ikonok.

**Továbbvezetés (2026-10-03, a PR #14 merge-e után):** a projektgazda döntött az UE3-BIZT-3-ról (K6: a nyilvántartás
„nagykorúság ellenőrizve” bejegyzést rögzít, életkor nélkül) és az UE3-PED-2-ről (K7: az ikon-hozzárendelés Madrih B
válasza után). A többi tétel a K5–K7 átvezetésével együtt: `2026-10-03 Fix pack – VO 2. fázis, 4. csomag.md`
(P4-01…P4-11; két független `verifier` ellenőrizte). Az UE3-PED-2 (1) — a mért hossz az időkeretbe — a VO QA-repó
újramérésére vár.

## Vétólista

- **Answer key, helyes-válasz jelölés, elosztó, küszöb, rubrika, kapu-típus, completion, időtartam:** nincs változás.
- **Gyermekvédelmi megfogalmazás:** `VOICE-BIBLE.md` 7. „Segélyvonalak” (P3-01, VO D-07) — előtte: „— **kivéve a 112-t**,
  amely mindig „száztizenkettő” alakban hangzik el, soha nem „egy-egy-kettő”-ként. Ma egyedül az `M3.3-NAR-01-VO`
  gyermekvédelmi lépéssorában hangzik el”; utána: „. **Kivétel: a 112** az `M3.3-NAR-01-VO` gyermekvédelmi
  lépéssorában elhangzik, mindig „száztizenkettő” alakban, soha nem „egy-egy-kettő”-ként”. Lásd UE3-BIZT-1.
- **Adatvédelem / jog:** K5 (P3-15 a–c) — „a két forrás-beszélő nagykorú (projektgazdai tényközlés, 2026-10-03, K5)”;
  a formális igazolás bizonyíték-kapu (VO D-08), személyes adat nincs. Lásd UE3-BIZT-2, -3.
- **Akadálymentesség:** P3-02…P3-05, P3-09, P3-10, P3-14 — a videós felirat-követelmények (M6.2-VID-01/02,
  M6.1-NAR-07, M1.3-NAR-01 opcionális videóága) megmaradtak, illetve kifejezetten rögzültek.
