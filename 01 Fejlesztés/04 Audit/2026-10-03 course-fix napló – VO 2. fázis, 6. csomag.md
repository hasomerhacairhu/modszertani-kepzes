# course-fix napló – VO 2. fázis, 6. csomag (2026-10-03)

> **Audit trail, nem kánon.** A `/course-fix` futás állapota és a célzott újraellenőrzés nyitott findingjai. A 12
> lépéses csomag a nagy csomagos eljárás küszöbe alatt van; bizonyíték a fájlok végállapota. A projektgazda ugyanabban
> az üzenetben a UE5-PED-3 kérdésben is döntött („illetve 2.A”, K8); a K8 a döntési jegyzőkönyvben rögzítve, és ebben a
> futásban szó szerint átvezetve.

- **Forrás:** `01 Fejlesztés/04 Audit/2026-10-03 Fix pack – VO 2. fázis, 6. csomag.md`, P6-01…P6-06, 12 lépés, 3 fájl;
  K8: `2026-10-03 Projektgazdai döntések – VO 2. fázis, kiegészítés.md`.
- **Bázis:** `vo/phase2-fix-pack-6` @ `9144058`.

| ID | lépés | fájl | állapot |
|---|---|---|---|
| P6-01 | a, b, c, d | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P6-02 | — | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P6-03 | — | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P6-04 | a, b, c, d | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P6-05 | — | VOICE-BIBLE.md | alkalmazva |
| P6-06 | — | PRODUCTION-DECISIONS.md | alkalmazva |
| K8 | `M1.3-NAR-08` `spec`; gyártási jegyzet | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva (a döntés szó szerinti átvezetése) |
| K8 | „Lezárt döntések”, új K8 sor | PRODUCTION-DECISIONS.md | alkalmazva |

**Ellenőrzések:** a végállapot lépésenként visszaolvasva (12/12: a bizonyíték-blokk 0×, a javítás-blokk 1×; a K8 három
helyen) · a teljes diff visszaolvasva, csomagon és K8-on kívüli változás nincs · `py_compile` OK · `content_integrity.py`
0 ERROR · `--pin-visible` 1 fájl (M1.3) · `build` ×2 bájtra azonos (415 asset, 903 deliverable, 123 forrásblokk) ·
`check` OK · `reconcile` 747/747 · `validate` OK · `lint --high-only` 0 · `unittest` 150 OK · `git diff --check` és a
PR-tartományé tiszta · hangnév-ellenőrzés a diffen 0 találat · `RELEASE-VERDICT: NO-GO` (változatlan, 6 blocker).

## Célzott újraellenőrzés — nyitott findingok (nem verifikáltak, ebben a futásban nem javítva)

Három lencse-reviewer (nyelv, implementáció, pedagógia) a diff-hunkokon; a biztonsági lencse nem futott, mert a diff
gyermekvédelmi, adatvédelmi vagy jogi szöveget nem érint. 5 finding, összevonva 4 tétel.

| ID | Hely (M1.3) | Probléma (röviden) | Javaslat | Típus |
|---|---|---|---|---|
| UE6-NYELV-1 | `M1.3-NAR-08` `spec` (184.), gyártási jegyzet (268.) | a K8 átvezetésének „ha nem” / „Ha nem” kezdete kétértelmű: „ha nem ugyanaz a hang mondja” olvasat is lehetséges, ami a K4-gyel ütközne | „ha nem különül el, előbb …” / „Ha nem különül el, előbb …”; a K8 tartalma változatlan | objektív |
| UE6-IMPL-1 = UE6-PED-1 (1. rész) | `M1.3-VID-01` `technical.note` (137.), Mobil-tippek (316.) | „alul overlay-ben vagy alatta a kérdés” — a H5P Interactive Video mobilnézetben a kérdést gombként jeleníti meg, a videó alá helyezést nem ismeri (`interaction.js` `isButton()`, `semantics.json`); ellentmond a 288. sornak | a mobil-szöveg igazodjon a 288. sorhoz („mobilnézetben a kérdés gombként jelenik meg, és a gomb nyitja meg”); a tappolási felület és a szám marad; 316. → pin, 137. → build | objektív |
| UE6-PED-1 (2. rész) | megvalósítási jegyzet (288.) | mobilon a kérdés gombbal nyílik, de a gomb címkéje nincs előírva; aki nem veszi észre, kihagyja a HOOK aktiváló kérdését | beszédes gombcímke (H5P „Label”) előírása — új követelmény, a szövegét a szerzőnek/projektgazdának kell jóváhagynia | emberi-döntés |
| UE6-PED-2 | `M1.3-VID-01` `spec` (132.) | a spec nem mondja meg, mit mutat a kép az 5. rész alatt (B válasza után, a kérdés előtt), miközben a narráció az ikonokra hivatkozik | vizuális előírás az 5. rész idejére (pl. a három szövegrész és az ikonok újbóli felvillanása) — új képi tartalom, a videó tervezőjének/projektgazdának kell eldöntenie; a NAR-08 szövege és a K7 időzítés nem változik | emberi-döntés |
| UE6-NYELV-2 | `M1.3-VID-01` `a11y.note` (143.), `notes` (160.) | két régebbi, állítmány nélküli tagmondat („…megjeleníthető jelölés.”; „…helyett tartalmi (informative), szöveges alternatívával.”) — nem ez a csomag okozta | „…megjeleníthető jelölés kell.”; „…helyett tartalmi (informative) jelölést kap, szöveges alternatívával.” | objektív |

**Javítva a projektgazda megnevezésére (2026-10-03, ugyanazon az ágon, a commit előtt):** a projektgazda szó szerint:
„javítsd a UE6-NYELV-1, UE6-IMPL-1, UE6-NYELV-2-t, aztán commitolj pusholj mergelj”. A három tétel a fenti javaslat
szerint alkalmazva, egyenként a fájlban bizonyítva és visszaolvasva (UE6-NYELV-1: 184., 268.; UE6-IMPL-1: 137., 316.
— a 137. sorban a mező elején már megnevezett „H5P Interactive Video” nem ismétlődik; UE6-NYELV-2: 143., 160.); új
review-kör nélkül. Nyitva marad: UE6-PED-1 (2. rész, gombcímke) és UE6-PED-2 (képi előírás az 5. rész idejére) —
emberi döntés.

**Rendben talált pontok:** a 288. sor H5P-állításai a `master` ágon ellenőrizve („Pause video”, „Display as”,
`button` alapérték, „Poster”, mobilnézetben gomb); a módosított `@asset`-mezők JSON-érvényesek, a 189. és a 137. sor új
szövege szó szerint megvan a generált manifesztben; a K7 sor 3. oszlopában megnevezett minden hely a K7 szerinti
megállási pontot tartalmazza; a K8 sorban megnevezett két hely szó szerint egyezik a döntési jegyzőkönyvvel; a 189. sor
négy hosszjelölési helye létezik; a P6-03 mondat nem visz el tanulói információt.

## Vétólista

- **Answer key, helyes-válasz jelölés, elosztó, küszöb, rubrika, kapu-típus, completion:** nincs változás (a kérdés, az
  opciók, a ✅, a visszajelzések és a completion-beállítás érintetlen; „Require full score” nem került be).
- **Időtartam:** a számok nem változnak (25–35 mp, 60–70 mp); csak a becslés jelölése és a mért érték helyei.
- **Gyermekvédelmi, adatvédelmi, jogi megfogalmazás:** nincs változás.
- **Akadálymentesség:** P6-01…P6-03 — a képleírás tartalma változatlan, a kérdés az 5. rész után; a felirat-, leirat- és
  alt-szöveg-követelmény változatlan. K8: a hallgatási próba elbukásának eljárása (előbb hangsúly, tempó, szünet,
  keverés; utána a hozzáférhetőségi felelős dönt) — a K4 és a VO D-18 változatlan.
