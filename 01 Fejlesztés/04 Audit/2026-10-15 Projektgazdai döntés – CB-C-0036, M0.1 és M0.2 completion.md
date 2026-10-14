# Projektgazdai döntés – CB-C-0036: M0.1 és M0.2 completion (D-039 / D-040)

> **Audit trail, nem kánon.** A projektgazda 2026-10-14-i D-039 döntésének és a 2026-10-15-i D-040 átvezetési felhatalmazásának körülhatárolt nyilvántartása. A kánoni döntés helye: `02 Tervezet/Emberi jóváhagyás szükséges.md` **20. szakasz**. Ez a jegyzőkönyv sem Moodle-deploymentet, sem adatvédelmi jóváhagyást, sem learner release-t nem igazol.

## Forrás és bizonyíték

- A D-039 projektgazdai üzenete szó szerint megőrizve: `heymarcell/mk-coursebuild/docs/decisions/D-039.md`, ellenőrzött builder-commit `5f9a91daa6c4c83ff6a36e3b5238ce1b7f62ce41`.
- Technikai kutatás: `heymarcell/mk-coursebuild/reports/2026-10-14-h5p-completion-skip.md` (ugyanez a commit); az RC1 H5P Interactive Book üres végjelentése miatt teljesülhetett kérdésválasz nélkül.
- D-039 prototípus: `heymarcell/mk-coursebuild/reports/2026-10-14-d039-decision-prototype.md` (ugyanez a commit): kizárólag zárt Moodle fixture kurzus, szintetikus tanulók; a Lesson szerveroldali követelménye negatív esetekkel mérve. A D-040 újabb, 12/12 sikeres fixture-körről számol be, de ez nem éles vagy kanonikus RC1-bizonyíték.
- Kánoni forrás: `c354f17a92722cac171b817a474b62f483a5d4a9`; M0.1 és M0.2 lecke-meták 13. sora, továbbá az ERT-1 és ERT-2 a HUM 14. szakaszában.
- Kapcsolódó döntéselőzmények: a builder `docs/DECISIONS.md` D-019, D-021, D-023–D-027 és D-039; kurzus finding `CB-C-0036`.

## D-039 – a hatókört meghatározó projektgazdai döntés (2026-10-14)

A korábbi, dokumentált projektgazdai döntés szó szerinti részletei:

> ERT-1 applies only to the Course Presentation behavior it explicitly governs. Its generalization to all Interactive Books was an implementation error and is not accepted.

> Every explicitly mandatory question must be answered before its required completion condition can be satisfied, regardless of correctness. No new passing threshold. Optional reflections and opinion questions stay non-gating unless the canonical specification explicitly requires otherwise.

> Preserve M0.1's existing Interactive Book + required Feedback direction and address its current view-only completion defect. Respect its DPO and accessibility conditions.

> For M0.2, test the four original mandatory questions using a server-validated construction. Do not invent a fifth question or assume Moodle's minimum-question scoring setting proves completion.

> No learner release while the R4 failures remain.

A forrásként hivatkozott D-039 dokumentumban szerepel a teljes projektgazdai üzenet. A részletek nem jogosítanak más leckék automatikus Moodle Lesson-konverziójára.

## CB-C-0036 – átvezetett, pontosított döntés

**M0.2:** A SLIDE 3 négy, eredetileg megírt Multiple Choice kérdésének tényleges megválaszolása kötelező, helyességtől függetlenül. Nem kerül be új ponthatár vagy ötödik kérdés. A zárt staging fixture-ben vizsgált natív Moodle Lesson a jóváhagyott **megvalósítási irány**: négy kötelező kérdésoldal; minimum négy megválaszolt kérdés; legfeljebb egy elfogadott válasz kérdésenként; lecke vége és jegyrögzítés szükséges; minden válasz lehet hibás; a kérdések utáni gyermekvédelmi tartalom megmarad. A választáshoz a Moodle-verzió és a teljes konfiguráció regressziós tesztje tartozik. **Éles adatkezelési és release-engedély nincs**: a tárolt egyéni válaszok DPO-jóváhagyása, szerzői forrásegyeztetés és szerepköri QA szükséges.

**M0.1:** A D-019/D-021 és a D-039 szerinti Interactive Book + háromoldalas, nem pontozott, **kötelezően beküldendő Feedback** irány elfogadott. A könyv megtekintése előfeltétel; a lecke teljesülését a Feedback mindhárom válaszának beküldése adja, nem a könyv puszta megnyitása vagy pontszám. Ez **kifejezett, kizárólag az M0.1-re vonatkozó új kivétel** a későbbi ERT-2 általános nem kapuzó szabálya alól; nem állítjuk, hogy az ERT-2 eredetileg is ezt írta elő. A véleményeknek nincs helyes/hibás minősítése és nincs küszöbe. Érzékeny személyes önfeltárás nem kényszeríthető ki: semleges „nem szeretném megosztani” lehetőséget a szerző hagyjon jóvá, mielőtt valódi tanulók kitöltik. A válaszok személyhez köthető tárolásáról, hozzáféréséről, megtartásáról és törléséről a DPO dönt. Emberi képernyőolvasós teszt és szerzői szövegjóváhagyás szükséges.

**ERT-hatókör:** Az ERT-1 kizárólag a tényleges H5P Course Presentation összefoglaló képernyőjének completion-szemantikájára vonatkozik. Az ERT-2 általános nem kapuzó véleményválasztó szabálya M0.1 fenti, név szerint rögzített kivételén kívül változatlan. Más lecke kötelező vagy opcionális besorolása ezzel a döntéssel nem változik.

## Nyitva maradó szakmai és kiadási kapuk

1. **Szerzői átvezetés:** M0.1 és M0.2 13. sorának, az ott megnevezett H5P/Moodle formátumnak és a tényleges completionnek az összehangolása; új válaszszöveg csak jóváhagyással. A négy M0.2 kérdés szövege, kulcsa és visszajelzése változatlan.
2. **DPO:** a Moodle Feedback és Moodle Lesson válaszok, naplók, mentett állapotok, hozzáférések, megőrzési/törlési idő és a kiskorú tanulók adatkezelési tájékoztatójának írásos vizsgálata.
3. **Memuna / szakmai QA:** az M0.2 gyermekvédelmi oldal megőrzése, és annak közvetlen, teljesítés utáni elérhetősége.
4. **Hozzáférhetőségi reviewer:** valódi képernyőolvasós próba és a Feedback required-field hibájának ellenőrzése.
5. **LMS/QA:** az elfogadott natív Lesson-invariánsok célverziós, negatív runtime tesztje, a résztvevői út és a Completion / Restrict access lánc visszaolvasása. A fixture-teszt önmagában nem `RUNTIME_VERIFIED` a kanonikus RC1-ben.
6. A teljes M0–Z H5P-leckekör külön, forrásalapú completion-regiszter szerint halad; nincs tömeges konverziós felhatalmazás.

**Végrehajtási határ:** jelen átvezetés csak a döntési nyilvántartást és az audit trailt módosítja. Nem javítja automatikusan a lecke-szövegeket, és nem ad `MK-FINAL`, export-, élesítés- vagy learner-release felhatalmazást.
