# Handoff to D-029 (mk-coursebuild): candidate source state from modszertani-kepzes

**Status:** information only. Not sent; the owner forwards it.

**1. Source SHAs**
- **Candidate source: `e67cce5`.** Branch `next-version/AP-2026-10-11-01`, draft PR #30. It is a provisional candidate, **not an approved release SHA**. It was not merged; draft PR #30 is not a release approval.
- **Running M0+M1 pilot source: `main@213a4c5`.** It is unchanged.
- Machine verdicts on `e67cce5` (`python3 tools/content_integrity.py --release-report`):
  - `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`. This allows planning a staging build, but it does not authorize one.
  - `LEARNER-RELEASE-VERDICT: NO-GO`.

**2. Your reported state needs re-verification**
- The latest D-029 result reported to us: 16 PASS, 19 INCOMPLETE, 39 BLOCKED of 74 manifest rows.
- We have not verified it, and we don't know which source SHA it ran against.
- Before anyone claims full staging readiness, re-run against the **actual builder state**, built from `e67cce5`, and report per row:
  - build-ID;
  - Moodle `cmid`;
  - the result;
  - the builder evidence.

**3. What differs between `213a4c5` and `e67cce5`**
- `LMS – activity manifest.md` has 74 `LMS-*` rows in both, but **10 rows changed text**: LMS-M1-05, LMS-M2-01, LMS-M2-02, LMS-M2-05, LMS-M3-04, LMS-M3-05, LMS-M4-03, LMS-M5-04, LMS-M5-07, LMS-M7-04. Results for these rows from a `213a4c5`-based run do not carry over.
  - Example: LMS-M1-05 now requires rubric preview before submission ("Allow users to preview rubric" = Yes) and per-row level and remarks after grading.
- The §1 profiles also changed. For example, ASSIGN-M now specifies "Grant attempts" = "Manually" and "Allowed attempts" = "Unlimited". Diff the whole file, not only the rows.
- `LMS – H5P runtime acceptance.md` gains:
  - item 25 (QUIZ-D empty submission, LMS-M0-06);
  - item 26 (rubric student view, LMS-M1-05);
  - a SAFE-1 pause/return case in item 11;
  - a negative case in item 9.

  There are now 38 RT rows, none `RUNTIME_VERIFIED`.
- 90 files changed under `02 Tervezet/`, including the generated media outputs (rebuilt with `tools/media_manifest.py build`).

**4. Runtime tests**
A builder PASS is not `RUNTIME_VERIFIED`. RT rows move only with a dated, version-pinned target-environment result (RA:31). The M0+M1 runtime checklist (RT-2) is available on request. It covers RT-P0-01, -06, -08, -09, -13, -14, -15, -17, -19, -24, -25 and -26, including the N-M1-04 default: LMS-M1-01 SLIDE 5 has no input element.

**5. Open decisions that can change build rows**
- **ADV-6:** forum retention and notice. This may change LMS-M0-05 or M0 completion.
- **ERT-12:** LMS-M1-07 notice text and MAN:48.
- **N-M1-04:** the LMS-M1-01 input element, only if RT-P0-24 passes.
- **RT-1:** the real contacts in "Segítség és kapcsolatok" (PILOT-3).

Do not fill these with assumed values; a build placeholder must not appear in any learner-facing view (RR staging rule 2).

**6. Boundaries**
- Synthetic test data only.
- No real learner access.
- No change to the running pilot course from this candidate.

**7. Please send back**
- the SHA you built;
- per-row status for the 74 rows, especially the 10 changed ones;
- the `cmid` list;
- the Environment record values (Moodle, H5P, content types, `enablesavestate`, `savestatefreq`).
