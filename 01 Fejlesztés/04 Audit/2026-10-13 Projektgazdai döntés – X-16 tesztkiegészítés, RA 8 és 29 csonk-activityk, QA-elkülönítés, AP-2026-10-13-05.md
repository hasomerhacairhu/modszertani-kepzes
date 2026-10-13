# Projektgazdai döntés – X-16 tesztkiegészítés, RA 8/29 csonk-activityk és QA-elkülönítés, AP-2026-10-13-05

> **Audit trail, nem kánon.** A projektgazda 2026-10-13-i üzenete szó szerint, a `next-version/AP-2026-10-11-01` ágon,
> a `4d02fcd` állapotra. Átvezetés: `02 Tervezet/Emberi jóváhagyás szükséges.md` 18. szakasz, `02 Tervezet/LMS – activity
> manifest.md`, `02 Tervezet/LMS – H5P runtime acceptance.md`, `02 Tervezet/RELEASE-READINESS.md`; ledger: `AUTOPILOT-LEDGER.md`
> (`AP-2026-10-13-05`).

---

Folytasd az AP-2026-10-13-04 staging build-terv alapján, a PR #30 aktuális HEAD-jéről (`4d02fcd` ellenőrzési alap).

**Projektgazdai döntések a két nyitott tesztkiegészítésről:**

1. X-16: elfogadom az (a) változatot. Az LMS-M2-05, LMS-M4-05 és LMS-M6-05 Assignmentek, valamint a hozzájuk tartozó három GATE-CP sor tesztcélú, előfeltétel nélküli példányként készüljenek el a zárt staging QA-környezetben. A tényleges rubrika, pontozás, szintek és GATE-CP-szemantika változatlan. Az eredeti manifestben szereplő valódi unlock-szabályok nem változhatnak.

2. RA 8 és RA 29: jóváhagyom a két tesztcélú csonk-activity tervét. A csonkok a megfelelő valódi Grade-alapú hozzáférési feltételt modellezzék az LMS-M1-06 alapján. A negatív és pozitív próbákhoz mindkét szükséges állapot legyen előállítható. Az eredmények kizárólag az adott mechanizmus tesztjét igazolhatják, nem a teljes M2–Z end-to-end működést.

**QA-elkülönítés**

- A 13 eredeti M0+M1 activity maradjon önálló, változatlan build-szelet.
- A hat X-16 tesztelem és a két csonk kizárólag belső QA-elemként szerepeljen ugyanabban a zárt staging-kurzusban, elkülönített tesztszekcióban.
- A QA-elemek kapjanak egyértelmű tesztazonosítót, ne kerüljenek a kanonikus completion-követelményekbe vagy a tanulói release-be.
- A QA-elemeket a release előtt el kell távolítani, majd a valódi előfeltétel-láncot külön tesztelni.
- A manifestben a kanonikus build-ID-k és a teszt-only azonosítók legyenek elkülönítve.

**X-16 adatvédelmi kérdés**

A következő értelmezést rögzítsd projektgazdai javaslatként, de ne zárd le a DPO és a jogász döntési kapuját:

A numerikus értékelés ne jelenjen meg a normál tanulói Assignment-, Grades-, Quiz- vagy mobilos tanulási felületen. A GDPR szerinti, jogosult sajátadat-hozzáférést és adatexportot ettől külön kell kezelni. A nyers értékelési adat pusztán a felületi rejtés érdekében nem tartható vissza automatikusan.

A mobil-webszolgáltatások letiltása még NINCS jóváhagyva. A site-szintű hatásokat, a már kiadott tokeneket és az alternatív jogosultságkorlátozást a site-adminisztrátorral kell tisztázni.

**Végrehajtás**

Most a két döntést, a szükséges build-specet, a tesztfixture-tervet és a tesztelési/eltávolítási protokollt vezesd át. Futtass célzott integritás- és regressziós teszteket, majd commitolj és pusholj.

A tényleges staging deploymenthez továbbra is kell a külön engedélyem és a P2–P6 környezeti bemenet. Ezek hiányában ne építs semmit a Moodle-példányra, és ne jelölj runtime-tesztet sikeresnek.

Ne indíts új általános auditot, és ne kérj újra már eldöntött kérdéseket.

A végén kizárólag három dolgot kérek:
1. A két tesztkiegészítés átvezetésének státusza.
2. A tényleges staging deploymenthez még hiányzó P1–P6 bemenetek.
3. Az X-16 nyitott, release-t blokkoló technikai és adatvédelmi döntései.

Main, pilot és CC-04 freeze változatlan. PR #30 draft. Merge, staging deployment és learner release nincs.
