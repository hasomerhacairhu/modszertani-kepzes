# Projektgazdai döntés – X-16 kanonikus visszaellenőrzés, X-16-PRIV hatókör, X-16-WS, AP-2026-10-13-06

> **Audit trail, nem kánon.** A projektgazda 2026-10-13-i üzenete szó szerint, a `next-version/AP-2026-10-11-01` ágon,
> a `277338c` állapotra. Átvezetés: `02 Tervezet/Emberi jóváhagyás szükséges.md` 19. szakasz, `02 Tervezet/LMS – activity
> manifest.md` (LMS-M4-05), `02 Tervezet/LMS – H5P runtime acceptance.md` (28–30. pont, Teszt-állapot); ledger:
> `AUTOPILOT-LEDGER.md` (`AP-2026-10-13-06`).

---

Folytasd a `hasomerhacairhu/modszertani-kepzes` projektet a PR #30 aktuális HEAD-jéről (ellenőrzési alap: `277338c`).

## Projektgazdai döntések – AP-2026-10-13-06

### 1. X-16 tesztbizonyíték és kanonikus visszaellenőrzés

Elfogadom, hogy a hat QA-X16 tesztelemen végzett RT-P0-28, valamint RT-P0-29 (a), (f) vizsgálatok előzetes, mechanizmusszintű runtime-bizonyítékot szolgáltassanak.

A végleges `RUNTIME_VERIFIED` státuszhoz azonban a kanonikus LMS-M2-05, LMS-M4-05 és LMS-M6-05 elemeken is kell célzott visszaellenőrzés.

Nem szükséges a QA-másolaton már sikeresen, ugyanabban a Moodle-környezetben lefuttatott összes negatív és pozitív eset teljes megismétlése, ha az alábbiak bizonyítottak:

- Az érintett kanonikus activity és QA-másolata releváns beállításai ténylegesen azonosak, dokumentált eltérésekkel.
- Mindhárom kanonikus Assignment esetében tanulói tesztfiókkal ellenőrzött a numerikus összpont rejtése, a szöveges rubrikaszint és a mentori komment láthatósága.
- Az értékelői munkafolyamat, a GATE-CP, a rubrikapontok, a completion és a kapuküszöbök nem változtak.
- Az RT-P0-29 (a), (f) kanonikus megjelenítési eredménye dokumentált.
- A kapcsolódó, külön nyitott API-, mobil- és adatvédelmi kapuk státusza változatlanul, valós bizonyíték alapján van kezelve.

Amíg a kanonikus elemek nincsenek megépítve és ellenőrizve, a QA-másolatok eredménye csak `QA_FIXTURE_VERIFIED` vagy a repository meglévő, ezzel egyenértékű bizonyítékjelölés lehet. Ne hozz létre új státuszt, ha a jelenlegi modell megfelelően megkülönbözteti a részleges bizonyítékot.

Az RT-P0-28 nem nyilvánítható sikeresnek, ha valamelyik kötelező negatív eset ténylegesen megbukott. Az RT-P0-29 egészét nem zárhatja le kizárólag az (a) és (f) eset eredménye.

### 2. X-16-PRIV – a numerikus értékelés pontos hatóköre

A projektgazdai javaslat hatóköre kizárólag a következő három Assignment numerikus összpontja:

- LMS-M2-05
- LMS-M4-05
- LMS-M6-05

Nem vonatkozik a kvízpontszámok általános elrejtésére.

Az ERT-5 szerinti M7 kapukvíz első próbálkozás utáni pontszámmegjelenítése változatlan, a megoldókulcs és a helyes válaszok védelmével együtt. A többi kvíz saját, már jóváhagyott review-beállítása sem változik.

A kurzusszintű Grade letters és tanulói pontkönyv-beállítások regresszióját külön kell igazolni. A „Szöveges értékelés” címke kizárólag a három kijelölt Assignmentre alkalmazható, nem terjedhet át véletlenül más activityre.

Az X-16-PRIV javaslatot pontosítsd ennek megfelelően. A normál tanulói felületre vonatkozó rejtést különítsd el a GDPR szerinti sajátadat-hozzáféréstől és adatexporttól.

A DPO és a jogi felelős jóváhagyása továbbra is szükséges; az adatexport-út nem zárható le pusztán projektgazdai döntéssel.

### 3. X-16-WS – változatlanul nyitott

A mobil-webszolgáltatás site-szintű letiltását nem engedélyezem.

Az LMS-gazda és a site-adminisztrátor készítsen rövid, döntésre alkalmas összehasonlítást a technikailag megvalósítható korlátozások között, különös tekintettel a már kiadott tokenekre, a többi felhasználóra és a meglévő mobilfunkciókra.

Ne állíts be olyan jogosultsági korlátozást, amelynek hatása a cél-Moodle-ben nem bizonyított.

## Végrehajtás

1. Rögzítsd a két projektgazdai döntést a HUM következő szakaszában.
2. Pontosítsd a manifest, a runtime acceptance és az X-16-PRIV dokumentációjának érintett részeit.
3. A meglévő QA-fixture és eltávolítási terv maradjon érvényben.
4. Ne készíts új tesztelemet vagy új activityt.
5. Futtasd a módosított fájlok célzott statikus és regressziós ellenőrzéseit.
6. Commitolj és pusholj a next-version ágra.

**Ezután ne indíts újabb audit- vagy döntésgeneráló ciklust.**

Amennyiben nincs valós Moodle staging-környezet és nincs külön deployment-engedély, a fejlesztési munkát ennél a mérföldkőnél zárd le.

Ne jelölj runtime-tesztet sikeresnek tényleges Moodle-futtatás nélkül.

A végső válasz legyen rövid:
- Projektgazdai döntések átvezetve: igen/nem.
- CI és regresszió.
- P1–P6 előfeltételek aktuális állapota.
- Mi az első konkrét művelet a tényleges Moodle staging deployment során?

A main, a pilot és a CC-04 freeze változatlan. PR #30 draft marad. Nincs merge, staging deployment vagy learner release.
