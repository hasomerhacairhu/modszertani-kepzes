# BSPEC-02 leltár — projektgazdai utasítás és review-brief (2026-10-04)

> **Audit trail, nem kánon.** A projektgazda 2026-10-04-i, a munkamenetben beillesztett utasítása szó szerint (lent), és
> a belőle készült brief a BSPEC-02 maradék leltárának scope-onkénti `/course-review` futásaihoz. Bázis: `ed82dbb`,
> munkaág `fix/moodle-build-hardening`, tiszta munkafa, nem pusholva. Új döntést nem tartalmaz: a lezárt döntések
> (BS-D1…D6, BS-D8, Q-REL-2, RM-D6; az M3.1 és az M3.2 reflexiója opcionális) változatlanok.

## Review-brief a `/course-review` futásokhoz

**Cél:** kizárólag a BSPEC-02 (`02 Tervezet/LMS – activity manifest.md`, „Nyitott build-spec tételek”, BSPEC-02 sor).
Nem általános audit: más témájú finding csak akkor kerüljön a riportba, ha egy mező kötelező vagy tárolt státuszát, a
completion-feltételét vagy a manifest-leképezését érinti.

**Mezők köre:** a scope-lecke minden tanulói szabad szöveges mezője, és minden elem, amely annak látszik („írd le”,
„írj … mondatot”, reflexió, napló, minimális karakterszám), a dián, a completion-sorban és a `**Completion (lecke):**`
alakban is.

**Mezőnként a projektgazda nyolc kérdése:**

1. Megköveteli-e a kánoni lecke a tanulói szöveget?
2. Kötelező-e a továbblépéshez vagy a teljesítéshez, vagy csak opcionális reflexió?
3. Kell-e egyáltalán tárolni?
4. Ha tárolt, a tanulóhoz kell-e kötni?
5. Valóban látnia kell-e mentornak vagy értékelőnek?
6. Leképezi-e már a manifest?
7. Ha kötelező és tárolt, és nincs hozzá manifest-activity: kell-e új TEXT-C sor?
8. Csak a H5P-n belüli pedagógiai pozicionálásról van-e szó, miközben a megvalósítás a Moodle-oldali kísérő Feedback?

**Adatvédelmi elv (szigorúan):** az önreflexió tanuló-lokális marad, hacsak a tárolás nem szükséges a pedagógiai vagy
teljesítési célhoz. Opcionális reflexiót nem alakítunk kötelező, tárolt tanulói adattá pusztán azért, hogy a manifest
teljes legyen.

**Besorolás, mezőnként pontosan egy:** `REQUIRED_STORED_MANIFEST_ROW_MISSING`, `REQUIRED_STORED_ALREADY_COVERED`,
`REQUIRED_BUT_LEARNER_LOCAL`, `OPTIONAL_STORED`, `OPTIONAL_LEARNER_LOCAL`, `NOT_ACTUALLY_FREE_TEXT`,
`HUMAN_DECISION_REQUIRED`.

**Mezőnként visszaadandó:** fájl:sor; a prompt vagy a mező rövid, szó szerinti idézete; kötelező/opcionális;
tárolt/nem tárolt; completion-függés; privacy-osztály (manifest §1: `P0`/`P1`/`P2`/`P2-PUBLIC-IN-COURSE`); jelenlegi
manifest-sor (`build_id`) vagy „nincs”; javasolt teendő; bizonyíték helye. Ha a lecke két helye ellentmond egymásnak
(pl. a completion-sor kötelezőnek, a dia opcionálisnak írja a mezőt), az önálló finding.

**Lezárt, nem nyitható újra:** BS-D1…D6 és BS-D8 (`2026-10-04 Projektgazdai döntések – BSPEC-01…04 maradék.md`; HUM 10.
szakasz); BS-D7 nincs: a 4.5–5.2 csak kutatási tartomány, a célverzió `UNKNOWN / TARGET-ENVIRONMENT EVIDENCE REQUIRED`;
az M3.1 és az M3.2 reflexiója opcionális, sor nélkül; az LMS-Z-06 megőrzése DPO-döntés; a Z.3 beküldése és szemantikus
mentori elfogadása külön állapot (LMS-Z-07); automatikus szemantikus validációt nem találunk ki. A TEXT-C profil:
Moodle Feedback, „Longer text answer” (manifest §1).

**A leltár közben hozott projektgazdai döntések (2026-10-04): D-1…D-3.** Szó szerint:
`2026-10-04 Projektgazdai döntések – BSPEC-02 leltár D-1…D-3.md`. Röviden: az M1.3 5. dia, a Z.1 SLIDE 5 és a
Z.2 SLIDE 5–7 `REQUIRED_BUT_LEARNER_LOCAL` (kötelező tanulási lépés, nem tárolt, nem completion-feltétel, nincs új
TEXT-C sor); a Z.4 marad a formális, tárolt záró produktum. Ezek projektgazdai döntések: ne jelentsd őket nyitottként.
A HUM 10. szakaszba való átvezetésük a `/course-fix` nyilvántartott teendője, ezt se jelentsd külön findingként.
Analóg mezőnél (önreflexiós scaffolding, amelynek beadandó változatát egy későbbi, tárolt produktum gyűjti) a
döntés indoklását mérlegelési szempontként alkalmazhatod, de új alkalmazási esetnél az `EMBERI DÖNTÉS` szabálya él.

**Emberi döntés** csak akkor, ha a kánon (Program terv, modul- és leckefájl, Glosszárium, `Emberi jóváhagyás
szükséges.md` LEZÁRVA-tételei és 8. szakasztól kezdődő döntései, az `01 Fejlesztés/04 Audit/` projektgazdai döntési
jegyzőkönyvei) nem ad választ. Ilyenkor a legkisebb pontos kérdést add meg a gazdájával; ne tágítsd általános
DPO-kérdéssé.

**Evidence (nem kánon):** `2026-10-04 Moodle-kutatás – BIZT-1, GATE_CONFIRMED tartalékút, IMPL-8.md`; az előző kör
naplója és nyitott kérdései: `2026-10-04 course-fix napló – BSPEC-01…02 javítókör.md` („Célzott újraellenőrzés”).

### Scope-ok (egy invocation = egy scope)

A jelölt mezők sorszámai a manifest BSPEC-02 sorából valók (`ed82dbb`).

| # | Scope | Jelölt mező a nyilvántartásban | Lencsék |
|---|---|---|---|
| 1 | M1.3 | :926 „Csak **completion**: ha mindhárom mezőben van valami, „kész”.” | implementation, safety |
| 2 | M2.2 | :507 „kötelező kérdés”; M2 hub :183 | implementation, safety |
| 3 | M2.3 | ág-specifikus mini-reflexiók; a záró mondat (LMS-M2-07) tárolásának kérdése (BIZT-R5) | implementation, safety, assessment |
| 4 | M2.4 | :584 „A Moodle-be csak ezt az egy, **nem érzékeny** mondatot add be”; M2 hub :183 | implementation, safety |
| 5 | M7.1 | :540 „ehhez manifest-sor is kell” | implementation, safety, assessment |
| 6 | Z.1 | :453 (valószínűleg kötelező) | implementation, safety, assessment |
| 7 | Z.2 | :276 (minimális karakterszám) | implementation, safety, assessment |
| 8–11 | M0.1, M0.2, M0.3, M0.4 | tisztázandó státuszú mezők | implementation, safety |
| 12–13 | M3.3, M3.4 | tisztázandó státuszú mezők | implementation, safety |
| 14–15 | M5.2, M5.4 | tisztázandó státuszú mezők | implementation, safety |
| 16–19 | M6.1, M6.2, M6.3, M6.4 | tisztázandó státuszú mezők | implementation, safety |
| 20 | M7.4 | tisztázandó státuszú mezők | implementation, safety, assessment |

**M2.3 külön:** a záró mondatnál (LMS-M2-07) válaszd szét: (a) a pedagógiai követelmény megköveteli-e a mondatot;
(b) a teljesítés megköveteli-e a beírását; (c) a teljesítéshez kell-e tartós, név szerinti tárolás; (d) tanuló-lokális
vagy kevésbé azonosító megvalósítás teljesítené-e ugyanazt a követelményt. Ha a meglévő döntések ezt eldöntik, hivatkozd
őket; ha nem, a legkisebb pontos nyitott kérdést add meg.

## A projektgazda utasítása (2026-10-04, szó szerint, beillesztett szövegként)

> Continue `hasomerhacairhu/modszertani-kepzes` on branch:
>
> `fix/moodle-build-hardening`
>
> Current expected HEAD:
>
> `ed82dbb`
>
> Previous implementation commit:
>
> `9fdeebc`
>
> The working tree was reported clean and nothing has been pushed.
>
> Start by verifying:
>
> - branch
> - HEAD
> - `git status`
> - diff from `e980a7058fba7e6aa5295e035dd334df12d436dd`
> - the current BSPEC registry state
>
> Do not reset or rewrite the two existing commits.
>
> ## Mission
>
> Close **BSPEC-02 only**.
>
> Do NOT start the separate 38-checklist-item classification or 4-photo/fallback work yet.
>
> Do NOT perform a broad course audit.
>
> Use the repo-local `/course-review` workflow and `/course-fix` workflow according to their SKILL.md files.
>
> The previous fix round established that BSPEC-01 is resolved and BSPEC-02 remains open because the required free-text inventory may still be incomplete.
>
> ## Current known BSPEC-02 state
>
> The previous round migrated normal required free-text storage to a core Moodle Feedback-based `TEXT-C` primitive and added:
>
> - `LMS-M2-07` — M2.3 closing sentence
> - `LMS-M4-09` — M4.4 lesson draft
>
> M3.1 and M3.2 were explicitly reviewed and MUST remain optional. Do not create mandatory stored-text rows for them.
>
> Existing TEXT-C rows include at least:
>
> - LMS-M2-06
> - LMS-M2-07
> - LMS-M4-06
> - LMS-M4-07
> - LMS-M4-08
> - LMS-M4-09
> - LMS-Z-06
>
> Z.3 additionally has the separate mentor acceptance state `LMS-Z-07`.
>
> ## Required first phase: narrow read-only inventory review
>
> Run isolated `/course-review` passes only for the remaining suspected/unclear free-text lessons.
>
> At minimum inspect:
>
> - M1.3
> - M2.2
> - M2.4
> - M7.1
> - Z.1
> - Z.2
>
> Also inspect every other lesson currently identified by the previous fix log as having an unclear free-text requirement, including the approximately ten ambiguous fields and the M2.3 mini-reflections.
>
> The question for every candidate field is:
>
> 1. Is learner text actually required by the canonical lesson?
> 2. Is it mandatory for progression/completion, or merely optional reflection?
> 3. Does it need to be stored at all?
> 4. If stored, must it be associated with the learner?
> 5. Does a mentor/evaluator genuinely need to see it?
> 6. Does the current manifest already model it?
> 7. If mandatory + stored and no manifest activity exists, is a new TEXT-C row required?
> 8. Is the wording merely pedagogical positioning inside H5P, while the actual implementation should be the Moodle-side companion Feedback activity?
>
> Apply the privacy principle strictly:
>
> > self-reflection should remain learner-local unless storage is actually necessary for the pedagogical/completion objective.
>
> Do NOT convert optional reflective prompts into mandatory stored learner data merely to make the manifest exhaustive.
>
> ## Classification output before fixing
>
> Before changing files, produce one deduplicated inventory table with every candidate field classified as exactly one of:
>
> - `REQUIRED_STORED_MANIFEST_ROW_MISSING`
> - `REQUIRED_STORED_ALREADY_COVERED`
> - `REQUIRED_BUT_LEARNER_LOCAL`
> - `OPTIONAL_STORED`
> - `OPTIONAL_LEARNER_LOCAL`
> - `NOT_ACTUALLY_FREE_TEXT`
> - `HUMAN_DECISION_REQUIRED`
>
> For every item include:
>
> - lesson/file
> - exact prompt or field
> - mandatory/optional
> - stored/not stored
> - completion dependency
> - privacy level
> - current manifest mapping if any
> - proposed action
> - evidence location
>
> Only after this inventory is complete should `/course-fix` begin.
>
> ## Important existing decisions
>
> Do not reopen these:
>
> - M3.1 optional reflection stays optional.
> - M3.2 optional reflection stays optional.
> - BS-D1…D6 and BS-D8 are project-owner decisions.
> - There is NO BS-D7 decision.
> - target Moodle version remains `UNKNOWN / TARGET-ENVIRONMENT EVIDENCE REQUIRED`.
> - research range 4.5–5.2 is only a research constraint.
> - `LMS-Z-06` retention remains a DPO decision.
> - Z.3 submission and semantic mentor acceptance remain separate.
> - do not invent automatic semantic validation.
>
> ## M2.3 special point
>
> The current closing sentence was implemented as mandatory named stored text.
>
> A reviewer raised a human/DPO question about whether it may be stored this way.
>
> Before treating this as a blocker, distinguish:
>
> - whether the **pedagogical requirement** requires the sentence;
> - whether completion requires entering it;
> - whether completion actually requires persistent named storage;
> - whether learner-local or less-identifying implementation could meet the same requirement.
>
> Do not silently turn this into a policy decision.
>
> If the repo's existing approved decisions already resolve it, use them.
>
> If they genuinely do not, report the smallest exact unresolved decision instead of broadening the DPO question.
>
> ## Other human questions from the previous round
>
> Do not accidentally solve these by assumption:
>
> - LMS-Z-06 retention classification.
> - designated-mentor-per-learner access mechanism if it is not technically pinned.
> - whether Z.3 should collect a third party's actual name.
> - Z.3 mentor-acceptance minimum.
> - overwrite behavior after mentor acceptance, if current policy does not settle it.
> - scope of Memuna veto over individual Z.3 acceptance.
> - M7-09 confirmation deadline.
> - re-evaluation vs F-peula sequencing.
> - interpretation of “min. 3–5 mondat”, if still genuinely ambiguous.
>
> However, verify whether any of these are actually already answered in canonical project-owner files before labeling them human decisions.
>
> ## Fix phase
>
> After the inventory review:
>
> 1. Fix only validated BSPEC-02 findings.
> 2. Add missing manifest rows only where required.
> 3. Remove stale completion/storage claims where fields are optional or learner-local.
> 4. Keep privacy minimization.
> 5. Update runtime acceptance for any newly identified required field.
> 6. Update the fix log.
> 7. Re-run:
>    - content integrity
>    - media manifest/reconcile
>    - media tests
>    - diff check
>    - relevant governance/selftests
> 8. Run narrow implementation, safety/privacy, assessment and Hungarian diff reviewers.
> 9. Resolve all objective reviewer findings.
> 10. Recompute BSPEC-02 state.
>
> If BSPEC-02 is objectively complete, mark it `BUILD_SPEC_RESOLVED` with real commit provenance according to the repo's registry convention.
>
> Do not fabricate a commit SHA before the implementation commit exists.
>
> If registry provenance requires a separate registry-only commit, use the same pattern as the previous round.
>
> ## Stop condition
>
> Stop after BSPEC-02 is either:
>
> A. objectively resolved, or
> B. reduced to a precise unavoidable HUMAN/DPO decision that genuinely prevents specification closure.
>
> Do not continue automatically into the 38 checklist items or the 4 photos.
>
> ## Final report
>
> Return:
>
> 1. current HEAD and commits created
> 2. exact BSPEC-02 inventory
> 3. fields added to manifest
> 4. fields deliberately NOT stored, with reason
> 5. fields determined optional
> 6. objective fixes made
> 7. remaining genuine human/DPO decisions
> 8. test/reviewer results
> 9. final BSPEC-02 state
> 10. resulting `MOODLE-BUILD-VERDICT`
> 11. remaining blockers after BSPEC-02
> 12. git status
> 13. confirm nothing was pushed
