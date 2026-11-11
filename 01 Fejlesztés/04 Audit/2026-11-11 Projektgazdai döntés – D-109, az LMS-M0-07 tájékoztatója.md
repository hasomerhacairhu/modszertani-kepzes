# Projektgazdai döntés – D-109, az LMS-M0-07 tájékoztatója (2026-11-11)

A projektgazda üzenete 2026-11-11-én (kb. 15:00 UTC), szó szerint, angolul. A projektgazda projektgazdaként, szerzőként és ideiglenes adatvédelmi döntéshozóként döntött; ez nem független DPO-jóváhagyás. Nyilvántartás: `02 Tervezet/Emberi jóváhagyás szükséges.md` 24. szakasz.

**Az ellenőrzés eredménye (a D-109 1. pontja kéri):** az A változat két mondata szerint a csoport mentora látja a válaszokat. A kurzusban a mentori szerepnek a `mod/feedback:viewreports` és a `viewanalysepage` kurzusszinten tiltva van, a D-108 mentori hozzáférése (A2) csak a Z.3 név szerinti kérdőívére szól, és a staging másolaton a csoport mentora nem nyithatja meg sem a válaszokat, sem az elemzést. Ezért az A változat nem került be; a projektgazda elé a C változat került (ugyanaz a szerkezet, a tényleges hozzáféréshez igazított két mondattal).

> # D-109: Immediate Owner Decisions and Publish Authorization
>
> **Hard deadline: 2026-11-11, 23:59 Asia/Jerusalem.**
>
> I approve the following decisions as project owner, course author and interim privacy decision-maker.
>
> **1. LMS-M0-07: OPTION A APPROVED.**
>
> Use the exact Option A wording in `reports/2026-11-11-d108/M0-07-PROPOSAL.md`.
>
> Keep the form name-free (`anonymous=1`), retain separate-groups access, and preserve the 11 named / 25 name-free form split.
>
> Do not enable individualized mentor feedback for name-free answers. Verify the wording and mentor access against the actual Moodle configuration.
>
> **2. A2: CONDITIONAL ALLOWLIST AUTHORIZED.**
>
> I authorize you to add an A2 allowlist entry for the new disposable, hidden, synthetic restored course created by this run, once its exact course ID, short name, staging identity and synthetic mentor group membership have been verified.
>
> Do not grant A2 to production, the definitive course 113, or protected courses. Preserve the existing guard, group-scoping, negative tests and rollback evidence.
>
> **3. PUBLICATION PREPARATION APPROVED.**
>
> Apply M0-07 Option A and complete its tests first.
>
> Important: `publish.sh` currently expects branch commit `a1dbc59`. Since this decision changes the source branch, update and verify the expected commit against the new, tested HEAD. Validate the destination repository, branch, diff, permissions and clean working state.
>
> Ensure the replacement PR is created and verified successfully before closing PR #36 as superseded. Prefer closing #36 after the replacement PR is merged. Do not lose the original review history.
>
> When everything is ready, give me the exact owner command to run.
>
> I will perform the required manual PR merge and `/course-pin` steps. Use a merge commit, not squash, so ancestry can be verified.
>
> **4. CRITICAL PATH**
>
> Immediately after the new pin is verified, execute the single definitive build and its complete regression, export, integrity, independent restore and rollback sequence.
>
> Finish all remaining authorized work in parallel. Do not wait for further approvals unrelated to the technical build.
>
> Keep the independent safeguarding, accessibility, assessment and pilot/release gates intact.
>
> **Target: complete the technical handover today.**
>
> Do not stop at a plan or status report. Tell me immediately when the publish command is ready, because my manual merge and pin are on the critical path.
