# Projektgazdai döntések — build-blocker leltár, D-a…D-d (2026-10-05)

> **Döntési jegyzőkönyv (audit trail).** A projektgazda 2026-10-05-i válasza a `2026-10-05 Build-blocker leltár – H-1…H-5,
> 38 checklist-tétel, 4 fotó.md` 6. pontjának kérdéseire, szó szerint (1. szakasz). Kánoni fájl nem változott; a
> döntéseket később a `/course-fix` vezeti át (2. szakasz). Munkaág: `fix/moodle-build-hardening` @ `9ef2b25`.

## 1. A projektgazda válasza, szó szerint

```text
Projektgazdai döntések a 2026-10-05 Build-blocker leltár alapján:

D-a — APPROVED
Elfogadom a 38 checklist item osztályozását. Build-relevant checklist blocker jelenleg:
- PR-01
- PR-02
- A11Y-07
- A11Y-17

A többi a leltár szerinti human-qa / signoff / runtime / environment / post-build / learner-release kategóriában marad.

D-b — APPROVED
Regisztráljuk:
- BSPEC-05 — Branching Scenario completion/fallback
- BSPEC-06 — standard Moodle H5P activity completion profile

D-c — SAME BRANCH
A media-manifest `release_phase / fallback / fallback_final` schema work ezen a `fix/moodle-build-hardening` branchen készüljön. Ez ugyanannak a build-hardening körnek a része.

D-d — M7.4 SLIDE 4
Az unscored focus choice NEM önálló completion element. Pedagógiai interakció marad, de a válasz megléte önmagában nem gate-eli a lesson completiont és nem igényel külön Moodle completion rule-t.

Rögzítsd ezeket az audit trailben. Canonical course fájlt még ne módosíts.

További primer Moodle research eredmény, amelyet a validation review-nak ellenőriznie/használnia kell:

1. Core Moodle H5P activity:
   - standard Moodle completionként view/grade alapú mechanizmus áll rendelkezésre;
   - a H5P Attempts report belső `completion` állapota nem azonos a Moodle Activity completionnel;
   - nincs olyan általános core H5P completion-rule, amely tetszőleges specifikus interakciót, például „3 külön branch végigjárva” feltételt közvetlenül Moodle Activity completionné tenne.
   Következmény: BSPEC-05/06 indokolt; ne feltételezz implicit H5P completion-semanticsot.

2. P2 Feedback mentor visibility candidate:
   Core Moodle candidate:
   - Feedback activity: Separate groups
   - learner a saját mentor-csoportjához rendelve
   - mentor ugyanannak a csoportnak tagja
   - mentor role: mod/feedback:viewreports
   - mentor NEM kap moodle/site:accessallgroups jogot
   - learner nem kap report capabilityt

   Ez access-scope mechanizmus, NEM a BS-D1 által tiltott group-based gate-state fallback.

   A mechanizmust RT-P0-15 staging tesztnek kell igazolnia legalább két mentorral és két elkülönített learner-csoporttal:
   - Mentor A csak A-csoport válaszait látja
   - Mentor B csak B-csoport válaszait látja
   - egyik mentor sem tud közvetlen URL-lel más csoport learner response-ára jutni
   - learner nem lát más learner válaszát

   Ha ez a target Moodle környezetben működik, PR-01 technikai mentor-routing része specifikálható DPO-szintű új mechanizmusdöntés nélkül; DPO QA továbbra is megmarad.

Most még ne fixelj.
```

(A beillesztett üzenet ezután a validálási review parancsát és fókuszát tartalmazta; az a review futtatására szól, nem
döntés.)

## 2. Mit jelentenek, és mi a teendő

| ID | Döntés | Hatás | Átvezetés (később, `/course-fix`) |
|---|---|---|---|
| D-a | a 38 checklist-tétel besorolása elfogadva; build-tétel: PR-01, PR-02, A11Y-07, A11Y-17 | a leltár 3. pontjának jelölései (`<!-- gate: … -->`) alkalmazhatók | a jelölések a GK §6, ADV §9, STD tételeire (leltár R-2) |
| D-b | BSPEC-05 (Branching Scenario completion/fallback) és BSPEC-06 (a standard H5P activity completion-profilja) felvétele | a MAN „Nyitott build-spec tételek” táblájába `BUILD_SPEC_OPEN`-ként (leltár R-1); a pontos hatókört a validálási review adja | MAN BSPEC-tábla |
| D-c | a média-manifest `release_phase` / `fallback` / `fallback_final` sémamunkája ezen az ágon | a leltár R-3 lépése ugyanezen a munkaágon készül | eszközkód + tesztek, majd R-4 |
| D-d | az M7.4 SLIDE 4 nem pontozott fókuszválasztása nem önálló completion-elem | a leltár R-24 kérdése lezárva; az M7.4 completion-sorának „nyitott” tagmondata ennek megfelelően átvezetendő; külön Moodle completion-szabály nem kell | M7.4 completion-sora (:14), HUM 10. szakasz |

A projektgazda által hozott kutatási eredmény (1. szakasz, „További primer Moodle research eredmény”) **bemenet a
validálási review-hoz**, nem kánon: a review-nak ellenőriznie kell. A mentor-láthatósági jelölt (Separate groups +
`mod/feedback:viewreports`, `moodle/site:accessallgroups` nélkül) a PR-01 technikai részéhez tartozik; ha a
célkörnyezetben az RT-P0-15 kiterjesztett tesztje igazolja, a mentor szerepkör tanulónkénti szűkítéséhez nem kell
DPO-szintű mechanizmusdöntés; a DPO QA marad. **Pontosítás (a validálási review után, 2026-10-05):** a jelölt csak a
mentor szerepkört szűkíti; az editing teacher, a manager és a site admin csoportfüggetlen hozzáférése, valamint a
Feedbacken kívüli profilok láthatósága DPO-kérdés marad (`2026-10-05 Validált findingok – MAN completion és
mentor-láthatóság.md`, BIZT-2, BIZT-5).

Változatlanul nyitva (ez a jegyzőkönyv nem dönti el): N-1, N-3, N-4, N-5…N-9, BIZT-R5, RT-P0-24, G1/G2/G3b, LMS-Z-06
megőrzése (BS-D6), H-3, PR-04, a G1–G8 release-bizonyítékok.
