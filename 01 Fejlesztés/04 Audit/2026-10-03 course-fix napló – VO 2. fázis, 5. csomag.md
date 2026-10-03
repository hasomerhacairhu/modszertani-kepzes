# course-fix napló – VO 2. fázis, 5. csomag (2026-10-03)

> **Audit trail, nem kánon.** A `/course-fix` futás állapota és a célzott újraellenőrzés nyitott findingjai. A 17
> lépéses csomag a nagy csomagos eljárás küszöbe alatt van; bizonyíték a fájlok végállapota.

- **Forrás:** `01 Fejlesztés/04 Audit/2026-10-03 Fix pack – VO 2. fázis, 5. csomag.md`, P5-01…P5-11, 17 lépés, 6 fájl.
- **Bázis:** `vo/phase2-fix-pack-5` @ `c850cba`.

| ID | lépés | fájl | állapot |
|---|---|---|---|
| P5-01 | a, b, c | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P5-02 | — | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P5-03 | — | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P5-04 | a, b | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P5-05 | a, b, c | M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md | alkalmazva |
| P5-06, P5-07 | — | RIGHTS-EVIDENCE.md | alkalmazva |
| P5-08 | — | Emberi jóváhagyás szükséges.md | alkalmazva |
| P5-09 | — | VOICE-BIBLE.md | alkalmazva |
| P5-10 | a, b | PRODUCTION-DECISIONS.md | alkalmazva |
| P5-11 | — | ELEVENLABS-VOICE-TEST.md | alkalmazva |

**Ellenőrzések:** a végállapot lépésenként visszaolvasva (17/17: a bizonyíték-blokk 0×, a javítás-blokk 1×) · a teljes
diff visszaolvasva, csomagon kívüli változás nincs · `py_compile` OK · `content_integrity.py` 0 ERROR · `--pin-visible`
2 fájl (M1.3, `Emberi jóváhagyás szükséges.md`) · `build` ×2 bájtra azonos (415 asset, 903 deliverable, 123 forrásblokk)
· `check` OK · `reconcile` 747/747 · `validate` OK · `lint --high-only` 0 · `unittest` 150 OK · `git diff --check` és a
PR-tartományé tiszta · hangnév-ellenőrzés a diffen 0 találat · `RELEASE-VERDICT: NO-GO` (változatlan, 6 blocker).

## Célzott újraellenőrzés — nyitott findingok (nem verifikáltak, ebben a futásban nem javítva)

Négy lencse-reviewer a diff-hunkokon: 9 finding, összevonva 5 tétel. A biztonsági lencse nem talált findingot.

| ID | Hely (M1.3) | Probléma (röviden) | Javaslat | Típus |
|---|---|---|---|---|
| UE5-PED-2 = UE5-IMPL-2 | `M1.3-VID-01` `spec` (132.), `a11y.note` (143.); `M1.3-NAR-08` `spec` bevezetője (184.) | a K7 szerinti új megállási pont és a „2. verzió után” elhelyezés nincs átvezetve az asset-mezőkbe; a videógyártó a régi helyet olvassa | 132.: „a 2. verzió és a hangalámondásos képleírás 5. része után (videó megáll)”; 143.: „a párbeszéd szüneteiben és a 2. verzió után”; 184.: „öt rövid részben, a párbeszéd szüneteiben és a 2. verzió után:”; build | objektív |
| UE5-IMPL-1 (+ UE5-NYELV-3) | megvalósítási jegyzet (288.) | a H5P Interactive Video felületi címkéje „Pause video”, nem „Pause”; a „Display as” alapértéke „button”, így a kérdés nem jelenik meg magától (a 290. sor ígérete nem teljesül) — forrás: a h5p-interactive-video `semantics.json` és `interaction.js` | „(„Pause”) beállítással” → „„Pause video” beállítással, „Display as: Poster” megjelenítéssel”; „Require full score” nem kerül be; kérdés, opciók, ✅, visszajelzés változatlan | objektív |
| UE5-NYELV-2 = UE5-PED-1 = UE5-IMPL-3 | „Mit hallunk?” cím (266.); kapcsolódik: 246., 1105. | a cím a „kb. 25–35 mp”-et jelölés nélkül adja, a `technical.note` (189.) viszont K7 előtti becslésnek nevezi; az öt rész ~95 szó (~38–48 mp, reviewer-becslés) | a címben: „összesen kb. 25–35 mp, a K7 előtti becslés”; a 189. jegyzet nevezze meg, hogy a mért érték a 266., 246. és 1105. sorba is bekerül; szám nem változik (VO D-17) | objektív |
| UE5-NYELV-1 | `M1.3-NAR-08-VO` 5. rész (280.) | a 4. rész rövidítése (P5-02) után az „Az S ennél a résznél” előzmény nélkül marad: a hallgató a betűt nem hallja ikonnévként | „Az S ennél a résznél:” → „Az S ikon ennél a résznél:”; a 278. sor (K7) változatlan; `@source` → pin, build | objektív |
| UE5-PED-3 | hallgatási próba (184., 268.) | nincs rögzítve, mi a teendő, ha a próbán a képleírás az 5. rész idézeteinél nem válik el Madrih A replikájától | projektgazdai döntés (utólagos QA: hozzáférhetőségi felelős); a K4 és a VO D-18 nem nyílik újra | emberi-döntés |

**Rendben talált pontok:** a K6 mező mindenhol „igen/nem, dátum, az ellenőrző szerepe”, életkor, születési dátum,
igazolvány-adat kizárva, az ellenőrzőnek csak a szerepe szerepel; „az ellenőrző szerepe” a K6 döntésszövegéből jön; a
diff jóváhagyást, aláírást vagy meglévő bejegyzést nem állít (VO D-08); a HUM-MEDIA-02 dátuma, jóváhagyója és
bizonyítéka érintetlen; a K6 sor 3. oszlopa mind a négy hivatkozott helyre helyesen mutat; a P5-02 rövidítése nem visz
el információt, mert az 5. rész pótolja; a P5-03 megszünteti a kétértelműséget.

**Továbbvezetés (2026-10-03, a PR #16 merge-e után):** a négy tárgyi tétel a
`2026-10-03 Fix pack – VO 2. fázis, 6. csomag.md`-be került (P6-01…P6-06, 12 lépés; két független `verifier`
ellenőrizte, 3 lépést az ő szövegükkel pontosítva, 2 általuk talált kihagyott hellyel bővítve). A P6-02 elsődleges
forrásból azt is rögzíti, hogy mobilnézetben a H5P a „Poster” interakciót is gombként jeleníti meg. A P6-03 a reviewer
javaslata helyett az 5. rész első mondatában nevezi meg az ikonokat, mert a regressziós teszt az „Az S ennél a résznél”
frázist rögzíti. A UE5-PED-3 emberi döntés, nem került csomagba.

## Vétólista

- **Answer key, helyes-válasz jelölés, elosztó, küszöb, rubrika, kapu-típus, completion:** nincs változás (a kérdés, az
  opciók, a ✅ és a visszajelzések érintetlenek).
- **Időtartam:** a számok nem változnak (25–35 mp, 60–70 mp); P5-05 csak jelöli, hogy a becslés a K7 előtti.
- **Adatvédelem / jog / HUM:** P5-07…P5-10 — a K6 mező datált toldásként a HUM-MEDIA-02 nyilvántartási bekezdésében
  (408.) és a `VOICE-BIBLE.md`-ben (32–34.); az R2-5 bizonyíték-kapuként; jóváhagyás-állítás nincs.
- **Gyermekvédelmi megfogalmazás:** nincs változás.
- **Akadálymentesség:** P5-01…P5-04 — a képleírás tartalma (melyik ikon melyik szövegrésznél) változatlan; a kérdés a
  képleírás 5. része után jelenik meg (WCAG 2.2 SC 1.2.5); a 4. rész rövidebb, a hozzárendelést az 5. rész mondja el.
