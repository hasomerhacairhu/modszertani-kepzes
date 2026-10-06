# Fix pack — R-4 (négy fotó) és a FREEZE-A utáni pontosítások (2026-10-05)

> **Audit trail, nem kánon — a `/course-fix` bemenete.** Döntési forrás: `2026-10-05 Projektgazdai döntés – pilot-ütemezés
> és M0+M1 freeze.md` 5. szakasz (A11Y-15/18, pilot-hétköznap, SAFE-7, Memuna-hatókör, M3.4 → M4); a négy fotó: a
> projektgazda 2026-10-05-i utasítása (ugyanott, a sémamunka bekezdése), Q-MED-1 és D-c (`Emberi jóváhagyás
> szükséges.md` 10. és 11. szakasz), `Média-assetek/RELEASE-MEDIA-STATUS.md` 3.2, az R5 és R7 produkciós szabály. A séma
> (`release_phase`, `fallback`, `fallback_final`) a `tools/media_manifest.py`-ban már él (`Média-assetek/ASSET-AUTHORING.md`
> 3. és 4. pont). Bázis: `fix/moodle-build-hardening` @ `9ef2b25` + a FREEZE-A nem commitolt változásai.
> Alkalmazási sorrend: FP-01 … FP-11. Köztes állapot: a látható-szöveg pinek a csomag végéig bukhatnak; a média-build az
> `@asset` mezők után kötelező (a `build` kétszer, majd `check` és `reconcile`).

## A. A négy fotó (R-4)

A mezőket az `@asset` JSON-blokkba kell felvenni, a meglévő mezők változatlanul hagyásával. A szövegek szó szerint.

| ID | Asset | Mezők | Várt gépi hatás |
|---|---|---|---|
| FP-01 | `M0.3-FOTO-01` (M0.3 SLIDE 2) | `"release_phase": "A"`, `"fallback": "Stagingben szöveges navigáció: a SLIDE 2 diaszövege (a kurzusstruktúra) és az alt-szöveg; a valós képernyőkép csak a staging build után, a stabil célfelületről készül (R7; RELEASE-MEDIA-STATUS 3.2)."` — `fallback_final` nincs (átmeneti fallback) | build nem blokkolja; a tanulói release-ben `MEDIA-ASSETS on fallback` (→ `CONTENT_READY / MEDIA_PENDING`), amíg a képernyőkép el nem készül |
| FP-02 | `M0.A-FOTO-01` (M0.A peula) | `"release_phase": "A"` (a fail-safe alapértelmezés kimondva), `"fallback": "Felvétel nélküli megőrzés: a kitöltött kvuca-plakát fizikailag, a stáb-dossziéban (HUM-PRIV-02 alapértelmezés); a Z.A visszakötéséhez a képzői jegyzet az adatminimalizált fallback (RELEASE-MEDIA-STATUS 3.2)."`, `"fallback_final": true` | nem blokkol, nem média-pending; az R8 a ténylegesen készülő fotóra marad |
| FP-03 | `M4.1-FOTO-01` (M4.1 SLIDE 4, 1. képpár) | `"release_phase": "C"`, `"fallback": "Bal/jobb jelölésű szöveges leíró kártyák a SLIDE 4-en az asset leírása szerint (karba tett kéz vs. nyitott kéz és felsőtest), AI-címke nélkül; a freeze-frame a C fázisú karakterjelenet-videókkal (M4.1-VID-03/04/05) együtt készül (R5; Q-MED-1)."` | nem blokkol (C fázis) |
| FP-04 | `M4.1-FOTO-02` (M4.1 SLIDE 4, 2. képpár) | `"release_phase": "C"`, `"fallback": "Bal/jobb jelölésű szöveges leíró kártyák a SLIDE 4-en az asset leírása szerint (földre néz, kicsit befelé fordul vs. végignéz a csoporton, nyitott felsőtest), AI-címke nélkül; a freeze-frame a C fázisú karakterjelenet-videókkal (M4.1-VID-03/05) együtt készül (R5; Q-MED-1)."` | nem blokkol (C fázis) |
| FP-05 | M4.1 SLIDE 4 tanulói szövege | a fallback csak akkor valós, ha a dián ott van: mindkét képpár helyén, amíg a kép nem készül el, két szöveges kártya „Bal oldali kép: …” / „Jobb oldali kép: …” címkével, **kizárólag** az FP-03/FP-04 asset `spec` leírásából levezetett tartalommal (a 2. pár kártyái egyezzenek a meglévő 2. kérdés opcióinak leírásával); a „A képpárok AI-generált jelenetekből vett állóképek, ezért mellettük … AI-címke” mondat csak a kép megjelenésekor érvényes — ezt a „Mit látunk?” blokkban kell jelezni. A kérdések, a ✅, az opciók és a visszajelzések nem változnak. | látható szöveg → pin; nyelvi utóellenőrzés |

## B. A FREEZE-A utáni projektgazdai pontosítások (5. szakasz)

| ID | Hely | Javítás | Korlát |
|---|---|---|---|
| FP-06 | `LMS – hozzáférhetőségi sztenderd.md` :111 (A11Y-15), :114 (A11Y-18) | a sor végére `<!-- gate: release-evidence, repo-fixable -->` (D-a; 5. szakasz 1. pont) | a tétel szövege nem változik. A statikus előfeltételek (A11Y-15: az M3 Drag & Drop-elsődleges leckéi, M3.1 :548, M3.4 :400 ↔ STD :32–33; A11Y-18: a nem deklarált Assignment-sablonok) a leltárban **validálatlanok** — ebben a csomagban nem javíthatók, a riportba kerülnek |
| FP-07 | `Gyermekvédelem – release gate.md` §6 | új nyitott tétel a :152 (1:1 / HUM-SAFE-02) után: `- [ ] SAFE-7: az M3.3 S1 23:15-ös bejövő privát üzenete és a ✅ első válasz HUM-SAFE-02-megfelelése a Memuna által QA-zva; nyitott, learner release előtt kötelező lezárni, a staging buildet nem blokkolja (`Emberi jóváhagyás szükséges.md` 11. szakasz). <!-- gate: human-qa -->` | a ✅ és az M3.3 szövege nem változik; SAFE-7 nem jelölhető megoldottnak |
| FP-08 | `Emberi jóváhagyás szükséges.md` 11. szakasz bevezetője | státusz-szemantika (5. szakasz 3. pont): egy lezárt projektgazdai döntés mellett a későbbi QA-/bizonyíték-kapu nyitva maradhat; a datált döntés-szakasz önmagában nem jelenti, hogy a benne álló minden QA-/bizonyíték-sor lezárt (pl. SAFE-7) | a `.claude/rules/safety-and-human-gates.md` „Lezárt döntések” szakaszának azonos pontosítása governance-módosítás: nem ennek a csomagnak a része (utána új session kell) |
| FP-09 | `Emberi jóváhagyás szükséges.md` :481 (9. szakasz, „A Memuna átnézése élesítés előtt”) | a történeti szöveg marad; jelölés: `[a felsorolás példálózó; a kánoni hatókör a GK §2 — 2026-10-05, 11. szakasz]` (5. szakasz 4. pont) | a lezárt döntés szövege nem törlődik |
| FP-10 | `Emberi jóváhagyás szükséges.md` 11. szakasz táblázata | új sorok az 5. szakasz öt pontjára (A11Y-15/18 besorolás; pilot-hétköznap és kurzus-hozzáférés; SAFE-7 státusz-szemantika; a Memuna-átnézés hatóköre; az M3.4 → M4 Q-REL-2 szerint), szó szerinti átvezetéssel, utólagos ellenőrző nélkül („—”) | új tartalom nem kerül be |
| FP-11 | `LMS – activity manifest.md` §7 | pilot-hétköznap (5. szakasz 2. pont): a bevezetőben a „péntekek rendje … változatlan” mondat mellé: a régi pénteki feltevések ütközés esetén a pilotra nem érvényesek (a cohort 2026-10-10-én, szombaton indul); a „Kurzus-hozzáférés” sor és a `M0_L1`, `M0_L2` nyitása: **2026-10-10** (időpont nélkül); az M0.A, valamint az M1 kapu-, F-peula-, javító- és megerősítési dátumai `SCHEDULE_TO_RESYNC` maradnak | időpontot nem találunk ki; az M0.A dátuma nem következtethető a cohort-indulásból; a Q-REL-4 „péntek 18:00” a pilotra csak ütközésmentesen érvényes |
| FP-12 | `M3.4 … modulproduktum.md` :808 | „Az **M4** csak a kapu megerősített teljesítése után nyílik meg.” → a Q-REL-2 / BSPEC-04 kánoni megkülönböztetése, az M1.4 :496 tanulói mondatának mintájára: az M4 leckéi akkor nyílnak meg, amikor a kapueredményedet megerősítették — akkor is, ha „Még nem teljesítve”; a sikeres kapueredményhez kötött következő lépés (az M5 kapufeladata) csak a sikeres eredmény után (MAN §4 „M3 megerősítve” / „M3 complete”) | új szabály nincs; a határidő-mondatok (a FREEZE-A-ban igazítva) nem változnak; pin |

## C. Várt gépi állapot a csomag után

`MEDIA-REQUIRED-WITHOUT-FALLBACK` 0; `CHECKLIST-UNCLASSIFIED` 0; `FINAL-RELEASE-QA: CHECKLIST` +1 (SAFE-7);
`MEDIA-ASSETS 1 on fallback: M0.3-FOTO-01` (tanulói release-tétel). A build-verdikt ettől még `NOT_READY` marad a
`MANIFEST-OPEN 3` (BSPEC-05…07) és a `CHECKLIST-BUILD 4` (PR-01, PR-02, A11Y-07, A11Y-17) miatt.

## D. Futás (`/course-fix`, 2026-10-05) — állapot és célzott újraellenőrzés

FP-01…FP-12 alkalmazva, nem commitolva. A célzott újraellenőrzés (nyelvi, implementációs, biztonsági lencse, csak a
módosított sorokra) a saját szerkesztéseimben talált hibákat az alábbiak szerint kezelte:

| ID | Hely | Megállapítás | Kezelés |
|---|---|---|---|
| FP-NYELV-1, -2, -4 | M4.1 SLIDE 4 „Mit látunk?” és kártyafejlécek; M3.4 :808 | igekötő-szórend, névmási referencia, alanyi/személyragozás | utójavítva |
| FP-IMPL-1 | M4.1 SLIDE 4 első pont | „ilyenkor AI-címke nem kell” túl tág: a NAR-06 leiratának R1 AI-címkéje marad | utójavítva: „a kártyák mellé nem kell AI-címke, a narráció (M4.1-NAR-06) leiratának AI-címkéje viszont marad (R1)” |
| FP-IMPL-3 | MAN §7 bevezető | a „Modulonként az első péntek …” szabály a pilot-kivétel után zárta a bekezdést, mintha a pilotra is érvényes volna | utójavítva: a két mondat sorrendje felcserélve, tartalmi változás nélkül |
| FP-IMPL-4 | MAN §7 „Kurzus-hozzáférés”, `M0_L1`/`M0_L2` sor | „időpont nélkül” Moodle-ben nem konfigurálható érték | utójavítva a PILOT-2 szerint: „időpont: `SCHEDULE_TO_RESYNC`” (időpont nem kitalálva) |
| FP-NYELV-3 | M4.1 NAR-06 narráció és a 2. kérdés | a narráció és a kérdés „képről” beszél, miközben a fallbackben szöveges kártyák látszanak | emberi döntés (projektgazda + média/VO-felelős): a narráció hangszövege nem írható át ebben a körben |
| FP-IMPL-2 | M4.1 SLIDE 4, a Példa 1 előtt | hiányzik a tanulónak szóló állapotmondat („ha szöveges kártyát látsz, …”) a @source blokkon kívül | az FP-NYELV-3 döntéséhez kötött új tanulói szöveg → riport |
| FP-IMPL-5 | STD :111, :114 | a `repo-fixable` jelölést az ellenőrző nem követi; az A11Y-15/18 statikus előfeltételei (R-13, R-15) validálatlanok | riport; validálás külön `/course-review`-val |
| FP-BIZT-1 | `.claude/rules/safety-and-human-gates.md` „Lezárt döntések” | a státusz-szemantika (FP-08) a szabályfájlban még nincs | governance-módosítás, nem ennek a körnek a része; utána új session |
| FP-BIZT-2 | `Program terv.md` §9.3 :392 | a Memuna-átnézés szűk felsorolása példálózó jelölés nélkül áll (a HUM :481 már jelölve) | riport: kánoni forrás, külön validált finding kell |
