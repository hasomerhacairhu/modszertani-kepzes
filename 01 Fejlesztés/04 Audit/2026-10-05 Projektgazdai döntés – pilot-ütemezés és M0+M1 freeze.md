# Projektgazdai döntés — pilot-ütemezés és M0+M1 freeze (2026-10-05)

> **Döntési jegyzőkönyv (audit trail).** A projektgazda 2026-10-05-i operatív pontosítása, szó szerint (1. szakasz).
> **Felülírja** a HUM-OPS-01 2026-10-02-i naptári értékeit (indulás 2026-11-06, zárás 2027-03-05, kurzus-hozzáférés
> 2026-11-02 és az ezekből levezetett központi naptár); a 2026-10-02-i audit trail történeti rekord marad,
> változatlanul. Kánoni fájl nem változott; az átvezetés (új datált HUM-szakasz, a régi dátumok superseded-jelölése a
> kánoni fájlokban) a `/course-fix` feladata. Munkaág: `fix/moodle-build-hardening` @ `9ef2b25`.

## 1. A projektgazda üzenete, szó szerint

```text
Projektgazdai operatív pontosítás — sürgős prioritásváltás.

## Valós ütemezés

A korábbi 2026-11-02 / 2026-11-06 indulási naptár elavult.

Aktuális tények:

- ma: **2026-10-05**
- a Moodle-t építő csapatnak **2026-10-06-tól** már stabil kurzusanyagot kell használnia;
- az első valódi learner cohort indulása: **2026-10-10**
- ez az első, kontrollált tesztkurzus / pilot;
- a pilot után valós learner- és staff-feedback alapján lesz újabb javítási kör.

A cél ezért NEM „minden M0–Z elem production-perfect 2026-10-05-re”.

A cél:

**M0 + M1 authoring freeze ma → Moodle build 2026-10-06-tól → controlled-pilot GO/NO-GO 2026-10-10 előtt.**

Ez illeszkedjen a repository Q-REL-1 életciklusához:
`INTERNAL_STAGING → CONTROLLED_PILOT → GENERAL_RELEASE`.

A `CONTROLLED_PILOT` az első valódi learner release; a pilot-findingok később javíthatók. Ne követelj GENERAL_RELEASE-szintű polish-t a pilot megkezdéséhez.

## Ma kötelező

Ma zárjuk le mindazt, ami ahhoz szükséges, hogy Anna 2026-10-06-án félreérthetetlen, implementálható M0+M1 forrásból tudjon Moodle-t építeni:

- M0/M1 canonical learner content;
- M0/M1 activity manifest sorok és prerequisite/completion semantics;
- LMS-M0-06 teljes 7-itemes belépőkvíz;
- M0 forum;
- M0 → M1 unlock;
- M0/M1 privacy class és build-time just-in-time notice követelmények;
- support/contact blokk build-spec;
- M0/M1 accessibility build-spec;
- M0/M1 release-required media vagy elfogadott fallback;
- stale schedule eltávolítása a kanonikus fájlokból;
- learner-facing placeholder / bizonytalan build-paraméter ne maradjon M0/M1-ben.

A target-Moodle runtime során bizonyítható dolgokat NE próbáld repo-elmélettel lezárni. Azok 2026-10-06–09 között staging evidence-ként készülnek.

## Pilot quality bar

Az első kontrollált pilotnak használhatónak és biztonságosnak kell lennie, nem tökéletesnek.

Pilot előtt nem halasztható:
- safety/privacy probléma, amely valódi learnert veszélyeztet;
- hibás hozzáférés vagy érzékeny adat láthatósága;
- törött prerequisite/completion/unlock;
- learner nem tudja végigvinni a szükséges M0/M1 útvonalat;
- P0 accessibility blocker, amely miatt valaki nem tudja használni;
- learner-facing placeholder / hibás kontakt;
- törött kvízkulcs vagy olyan gate, amely tévesen blokkol.

Pilot utánra halasztható és backlogolható, ha a használhatóságot nem akadályozza:
- vizuális polish;
- opcionális narráció/videó;
- apró copy finomítás;
- nem kritikus layout-hiba;
- analytics finomhangolás;
- későbbi modulok runtime proofja;
- M2–Z olyan problémája, amelyet a cohort még nem ér el.

Ne jelöld ezeket megoldottnak; csak `POST-PILOT` / backlog státuszt kapjanak.

## Naptár

A régi konkrét november–márciusi dátumokat supersede-eld a kanonikus fájlokban.

Amit most biztosan tudunk:
- authoring/build indul: 2026-10-06
- cohort/course indul: 2026-10-10
- M0 és M1 az első aktív tartalmi prioritás.

A későbbi modulok új konkrét dátumait NE találd ki. `SCHEDULE_TO_RESYNC` / programvezetői új ütemezés szükséges.

A 2026-10-02-i audit trail történeti rekord marad; azt ne írd át. Készíts új 2026-10-05-i superseding schedule decision recordot.

## Scope discipline

Mostantól a mai munkában:

- ne indíts új általános auditot;
- ne nyiss új pedagógiai/redesign scope-ot, ha nem blokkolja M0/M1 authoringot vagy a 2026-10-10 controlled pilotot;
- M3.3/M6.4 és a teljes-course hardening eddigi döntései nem vesznek el, de ne tartsák fel az M0/M1 freeze-t;
- ne commitolj és ne pusholj.

Először add vissza egyetlen rövid execution tervben:

1. mi az a minimum canonical módosítás, amit MA el kell végezni az M0+M1 freeze-hez;
2. mi maradhat staging-runtime feladat 2026-10-06–09-re;
3. mi tolható pilot utáni backlogba;
4. milyen meglévő `/course-fix` köröket kell most előrehozni, szűkíteni vagy későbbre tenni;
5. a legkisebb konkrét következő parancsot, amellyel ma elindítjuk az M0+M1 freeze-t.

STOP utána. Ne indíts új review-t.
```

## 2. Hatás és nyitva maradó pontok (rögzítés, nem döntés)

- **Superseded:** a HUM-OPS-01 naptári értékei (HUM :226, :483; RR :42; PT :60; a MAN §7 központi és kiegészítő
  naptára; a modulfájlok zárójeles dátumai). Ami biztos: build/authoring 2026-10-06, cohort-indulás 2026-10-10; a
  későbbi dátumok `SCHEDULE_TO_RESYNC` (programvezető).
- **Nyitva, a build és a pilot szempontjából releváns** (nem találjuk ki): az M0/M1 konkrét naptári pontjai
  (pl. az LMS-M0-03 „M0.A után nyílik dátummal”, az M1 kapu-beadás, -megerősítés, F-peula és javító határidő);
  a pilot GO/NO-GO értékelésének módja egy M0+M1-re szűkített pilotnál (a `content_integrity.py --release-report`
  ma a teljes kurzusra ad verdiktet, hatókör-paramétere nincs).
- Az eddigi döntések (D-a…D-j, M33-IMPL-6, SAFE-1/-4, 7.1–7.2) érvényesek; az M0/M1-et nem érintő részük
  végrehajtása `POST-PILOT` sorrendbe kerül. **[SUPERSEDED — 4. szakasz, 2026-10-05 scope-korrekció: az M0–Z
  repo-fixable és build-spec munka nem `POST-PILOT`, hanem a 2026-10-05-i teljes lezárási scope része.]**

## 3. PILOT-1…PILOT-4 — a két nyitott pilot-operációs kérdés projektgazdai döntése (2026-10-05), szó szerint

```text
A két nyitott pilot-operációs kérdés projektgazdai döntése:

## PILOT-1 — M0+M1 GO/NO-GO

Választás: **A**.

A 2026-10-10-i controlled pilot hatóköre első körben **M0+M1**.

A teljes kurzus gépi `LEARNER-RELEASE-VERDICT` továbbra is lehet `NO-GO` az M2–Z nyitott tételei miatt. Ezt nem értelmezzük át, és nem állítjuk, hogy a teljes kurzus READY.

A 2026-10-10-i pilot GO/NO-GO külön, explicit **M0+M1 evidence list** alapján kerül rögzítésre.

Ne módosítsd ma a release-report toolt modul-scope támogatásra.

## PILOT-2 — ismeretlen dátumok

Biztos tények:
- authoring/build indul: **2026-10-06**
- első valódi cohort / első képzés: **2026-10-10**
- 2026 októberében a cohort a teljes M0 és M1 modulokkal foglalkozik.

Nem ismert még:
- M0.A pontos dátuma/időpontja;
- M1 konkrét gate-beadás / confirmation / F-peula / retry dátumai;
- M2–Z új dátumai.

Ezek hiánya NEM blokkolja a 2026-10-05-i M0+M1 authoring freeze-t.

Szabály:
- build-specben `SCHEDULE_TO_RESYNC`;
- learner-facing placeholder nem jelenhet meg;
- amely Moodle activity konkrét ismeretlen dátumtól függ, az authoring során felépíthető, de valódi learnernek nem nyitható meg, amíg a dátum nincs konfigurálva;
- LMS-M0-03 esetén az elv változatlan: **M0.A után nyílik dátummal**; M0.A dátumát ne következtesd automatikusan a 2026-10-10-i cohort-startból;
- M1 gate-dátumokat se találd ki.

## PILOT-3 — Segítség és kapcsolatok

A technikai support és a tanulási/programkontakt konkrét elérhetősége még nincs megadva.

Ez:
- NEM blokkolja Anna 2026-10-06-i authoringját;
- BLOKKOLJA a learner-facing pilot release-t addig, amíg a tényleges csatornák nincsenek kitöltve.

A blokk szerkezetét most teljesen specifikáld a négy szereppel:
1. technikai segítség
2. tanulási/programkontakt
3. assigned mentor
4. Memuna / safeguarding

A már kanonikus Memuna/safeguarding adatokat használd.
Technikai vagy programkontaktot ne találj ki.
Belső build-jelölő stagingben megengedett; learner-facing nézetben nem.

## PILOT-4 — M0/M1 média

Pontosítás:

Ne azt rögzítsd, hogy „M0/M1 ships no video”.

A szabály:

**Az M0+M1 controlled pilot nem függ videó vagy narráció elkészültétől.**

- videó/karaktervideó: optional;
- narráció: optional;
- díszítő illusztráció: optional;
- információhordozó vizuálhoz strukturált HTML/szöveges fallback;
- a tanulási célnak média nélkül is teljesülnie kell;
- elkészült és jogilag/technikailag használható média később hozzáadható.

Ez megfelel a jelenlegi `RELEASE-MEDIA-STATUS.md` M0/M1 besorolásának.

## Következő lépés

A korábban megadott **FREEZE-A** parancs most futtatható.

Futtasd le.

Utána:
1. add vissza a módosított fájlokat és verdiktet;
2. ne indíts új review-t;
3. ne commitolj és ne pusholj;
4. STOP.

A következő kör közvetlenül a media-manifest schema + M0 R-4 lesz.
```

**Hatás:** PILOT-1: a 2026-10-10-i pilot hatóköre M0+M1, a GO/NO-GO explicit M0+M1 evidence list alapján; a teljes
kurzus gépi verdiktje nem értelmeződik át; a tool ma nem változik. PILOT-2: ismeretlen dátum a build-specben
`SCHEDULE_TO_RESYNC`, tanulói nézetben nem; dátumfüggő activity felépíthető, valódi tanulónak a dátum konfigurálásáig
nem nyitható; az LMS-M0-03 elve változatlan, az M0.A dátuma nem következtethető a cohort-startból. PILOT-3: a
„Segítség és kapcsolatok” blokk szerkezete négy szereppel specifikálandó; a technikai és a programkontakt hiánya a
tanulói pilot release-t blokkolja, az authoringot nem. PILOT-4: az M0+M1 pilot nem függ videó vagy narráció
elkészültétől (a RELEASE-MEDIA-STATUS 3.2 szerint).

## 4. Scope-korrekció (2026-10-05), szó szerint — a 2. szakasz `POST-PILOT` mondatát felülírja

```text
Fontos scope-korrekció a pilot-ütemezési jegyzőkönyvhöz.

A korábbi megfogalmazás, amely szerint az M0/M1-en kívüli végrehajtás `POST-PILOT`, NEM érvényes.

Projektgazdai döntés:

- M0 és M1 az első prioritás, mert 2026-10-06-tól már Moodle-authoringhoz kell a stabil forrás;
- DE **2026-10-05 végéig az egész M0–Z repository/spec hardeninget le kell zárni**, amennyire azt repo-ban, runtime nélkül determinisztikusan le lehet zárni;
- M2–Z repo-fixable vagy build-spec munkát ne sorolj `POST-PILOT` státuszba;
- csak olyan tétel maradhat post-build / release-evidence / final-QA állapotban, amely ténylegesen Moodle runtime-ot, renderelt felületet, cmid-et vagy még meg nem adott emberi jóváhagyást igényel.

A mai cél:
`MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`

A `LEARNER-RELEASE-VERDICT` ettől még maradhat `NO-GO`, amíg a runtime és final-QA bizonyítékok nincsenek meg.

A pilot decision recordba ezt add hozzá új, dátumozott pontosításként. A korábbi `POST-PILOT` megfogalmazást jelöld supersedednek; ne töröld a történeti szöveget.

Ezután a FREEZE-A-ban:
- NE szerepeljen az, hogy „a végrehajtásuk az M0/M1-en kívül POST-PILOT”;
- helyette: „az M0/M1-en kívüli implementáció nem ebben a FREEZE-A körben történik, de a mai teljes M0–Z lezárási scope része”.

A media következő kör sem M0-only:
- teljes `release_phase` / `fallback` / `fallback_final` schema;
- mind a 4 ismert fotó/fallback eset;
- majd R-4.

Ne indíts review-t, ne commitolj, ne pusholj.

Add vissza a javított FREEZE-A parancsot, és STOP.
```

**Hatás:** a mai (2026-10-05) lezárási scope a teljes M0–Z repó/spec hardening, amennyire runtime nélkül
determinisztikusan lezárható; cél: `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`. M0/M1 az első prioritás. `POST-PILOT`
státuszba repo-fixable vagy build-spec munka nem kerülhet; post-build / release-evidence / final-QA állapotban csak az
marad, ami Moodle runtime-ot, renderelt felületet, cmid-et vagy még meg nem adott emberi jóváhagyást igényel. A
`LEARNER-RELEASE-VERDICT` maradhat `NO-GO`. A következő média-kör teljes sémát és mind a 4 fotót fedi, majd R-4.

## 5. Projektgazdai pontosítások a FREEZE-A után (2026-10-05), szó szerint

```text
Owner clarifications after FREEZE-A. Record these in the 2026-10-05 pilot/scope decision record as a new dated section. Do not modify canonical course files for these clarifications yet; carry the required canonical changes into the next /course-fix command.

1. A11Y-15 / A11Y-18
The D-a classification remains authoritative: RELEASE-EVIDENCE.
The 2026-10-05 scope correction was a timing/scope rule, not a taxonomy change.
If either item has a static/repository-fixable prerequisite, that static fix must be completed today; the runtime/rendered proof remains RELEASE-EVIDENCE.
Therefore tag A11Y-15 and A11Y-18 as release-evidence, not BUILD, and do not leave them unclassified.

2. Pilot weekday
2026-10-10 Saturday is the authoritative first learner/course start for this pilot.
The old Friday-session assumptions do not automatically apply to this pilot and are superseded where they conflict.
Learner course access date = 2026-10-10.
Do not invent an access time.
M0.A exact date/time and the concrete M1 gate/F-peula/retry/confirmation dates remain SCHEDULE_TO_RESYNC.

3. SAFE-7
SAFE-7 remains OPEN and is FINAL_RELEASE_QA / learner-release only. It does not block staging build.
It must be added to GK §6 as an explicit open QA item.
Clarify the generic status semantics: a project-owner decision may be closed while its later QA/evidence gate remains open. A dated decision section therefore does not itself mean all QA/evidence rows inside it are closed.
Do not mark SAFE-7 resolved.

4. Memuna review scope
The older 2026-10-02 enumeration at HUM :481 is illustrative, not exhaustive.
The canonical scope is the broader GK §2 wording, as already propagated by R-11.
Keep the historical text but annotate/supersede its scope accordingly in the next /course-fix.

5. M3.4 → M4 contradiction
This is not a new policy decision. Existing Q-REL-2 / BSPEC-04 wins.
The learner-facing statement that M4 only opens after confirmed successful completion is wrong if it blocks the M4 learning portion after a confirmed fail.
In the next /course-fix, align M3.4 with the canonical distinction: the next learning portion may open after the confirmed result, including “Még nem teljesítve”; only success-bound downstream/gated elements remain blocked.
Use the existing canonical Q-REL-2/BSPEC-04 wording; do not invent a new rule.

Now perform the media-manifest schema work directly. This is tool/schema work, not /course-fix.
[…a sémamunka utasításai; a jegyzőkönyvben csak a döntési rész áll szó szerint…]
```

**Hatás (a következő `/course-fix`-be):** A11Y-15 (STD :111) és A11Y-18 (STD :114) → `<!-- gate: release-evidence, repo-fixable -->`
(a D-a szerint; ha statikus előfeltétel van, azt ma kell javítani); a 2026-10-10 (szombat) a pilot első tanulói/kurzus-
napja és a tanulói kurzus-hozzáférés dátuma (időpont nélkül), a régi pénteki feltevések ütközés esetén superseded; az M0.A
és az M1 kapu-, F-peula-, javító- és megerősítési dátumai `SCHEDULE_TO_RESYNC`; a SAFE-7 nyitott FINAL_RELEASE_QA-tétel
a GK §6-ban, és a státusz-szemantika pontosítása (lezárt projektgazdai döntés mellett a későbbi QA/bizonyíték-kapu nyitva
maradhat); a HUM :481 felsorolása példálózó, a kánoni hatókör a GK §2; az M3.4 → M4 mondat a Q-REL-2 / BSPEC-04 kánoni
megfogalmazásához igazítandó.
