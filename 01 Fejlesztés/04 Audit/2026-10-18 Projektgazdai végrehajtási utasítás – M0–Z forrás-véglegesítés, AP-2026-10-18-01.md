# Projektgazdai végrehajtási utasítás – M0–Z forrás-véglegesítés (AP-2026-10-18-01)

> **Audit trail, nem kánon.** A projektgazda 2026-10-18-i végrehajtási utasítása szó szerint, ahogy a
> sessionben érkezett. Ez a `/course-autopilot M0-Z --lens all --next-version` futás (`AP-2026-10-18-01`)
> felhatalmazásának forrása. Nem release-, runtime-, DPO-, Memuna-, jogi vagy szakmai jóváhagyás.

---

PROJECT OWNER EXECUTION ORDER — AUTONOMOUS M0–Z COURSE SOURCE FINALIZATION
Date: 2026-10-18
Repository: hasomerhacairhu/modszertani-kepzes
Mode: IMPLEMENT + VERIFY + CLOSE, not review-only
Target: complete next-version source, without modifying the running pilot

You are working inside the methodological training repository for the Hasomer Hacair blended madrih training programme.

Your assignment is to bring the ENTIRE CANONICAL COURSE SOURCE as close as technically, pedagogically, editorially and operationally possible to a finished, coherent, excellent, buildable and pilot-ready state.

This is a PROJECT OWNER AUTHORIZATION to execute the work, not a request to prepare another plan or ask me to choose between routine alternatives.

You must work autonomously, make substantive progress, implement verified fixes, write missing material, run tests, perform independent quality checks, commit the results locally, and continue until all autonomously actionable source problems have been resolved.

DO NOT STOP after producing an audit, proposal, fix pack, checklist, review package or decision memo.

DO NOT ask me routine clarification questions.

DO NOT wait for an author, reviewer, coordinator or external stakeholder before continuing independent work.

A missing external approval is NOT a reason to stop the overall execution. Record it accurately, complete everything independent of it, and proceed.

However, never fabricate professional signoffs, legal determinations, safeguarding approvals, runtime evidence or release authorization. Never weaken an actual safety requirement to manufacture a green verdict.

The desired outcome is a substantially finished COURSE, not an impressive collection of reports.

============================================================
1. EXACT SCOPE AND AUTHORIZATION
============================================================

I expressly authorize:

- Finalizing the next version of the entire M0–M7 + Z curriculum.
- Working on a dedicated next-version branch.
- Correcting all currently provable source defects.
- Applying all previously approved project-owner decisions that have not yet been correctly propagated.
- Correcting POST-PILOT issues in the next-version branch without changing the running M0/M1 pilot.
- Writing missing learner-facing instructions, assignment descriptions, assessment explanations, teaching examples, formative feedback and implementation specifications, provided these implement the existing programme's approved learning objectives and do not invent new safety or organizational policies.
- Completing missing answer-key specifications when the pedagogically correct answers can be established from authoritative source material and verified independently.
- Correcting objectively inconsistent rubrics, terminology, activity descriptions, prerequisites, cross-references, worksheets and completion descriptions.
- Making conservative, evidence-supported editorial and implementation choices rather than escalating every ambiguity.
- Updating affected canonical documentation, traceability records, source-linked tests, media declarations and generated manifests through the existing approved tooling.
- Researching primary sources when required to establish technical feasibility or pedagogical correctness.
- Running existing specialist skills, read-only reviewers, targeted verification and local regression testing.
- Creating small, logical local commits and maintaining the existing autopilot ledger.

This instruction is also an explicit authorization for NEXT-VERSION work, including previously frozen M0/M1 POST-PILOT corrections. It does not authorize modifying the running pilot.

I am NOT authorizing:
- Editing production Moodle.
- Editing the existing mk-coursebuild staging installation or its database.
- Enrolling real learners or altering their progress.
- Changing or bypassing the repository's safety hooks, sandbox or permissions.
- Rewriting Git history, discarding existing work or deleting backups.
- Publishing credentials, identifiable learner information or private organizational records.
- Automatically merging a PR or deploying/releasing course content.
- Inventing a DPO, Memuna, legal, accessibility or assessment-professional signoff.

Use local commits on the working branch. Do not push or merge during this run; those are separate protected operations and must not become a source of interactive interruptions.

The goal is to finish the actual source implementation locally with the maximum possible independence.

============================================================
2. THE COURSE IS THE PRODUCT — NON-NEGOTIABLE QUALITY
============================================================

The primary audience is madrihim, including participants who may be minors.

The course must be:

- Pedagogically purposeful.
- Genuinely useful in real kvuca work.
- Understandable without a trainer explaining every screen.
- Enjoyable and motivating without becoming childish.
- Easy to navigate on a phone.
- Realistically completable within its stated time commitments.
- Internally consistent across online and face-to-face components.
- Fair and transparent in assessment.
- Accessible through appropriate non-drag, keyboard, screen-reader and low-bandwidth alternatives.
- Safe with respect to safeguarding, sensitive disclosures, private reflections and external AI.
- Respectful of the learner's autonomy and privacy.
- Technically buildable using REAL Moodle/H5P capabilities.
- Simple wherever simplicity serves learning better than additional interactivity.

Do not maximize the number of interactions, media assets, slides, questions, assignments or restrictions.

Maximize useful learning.

Never force a technological format that is inappropriate for a learning activity.

If a simple Moodle Page, Lesson, Quiz, Feedback activity, Assignment or downloadable worksheet achieves the learning objective better than a complicated H5P workaround, prefer the simpler valid solution, within the existing approved design.

A learner must always understand:
1. What am I learning?
2. Why does it matter in my actual role?
3. What do I need to do?
4. Where do I do it?
5. Is this compulsory or optional?
6. What happens after I submit?
7. How do I know I have completed it?
8. What do I do if I make a mistake or cannot complete it?
9. How can I get help?
10. How will the knowledge transfer into real kvuca work?

Every important assessment should offer meaningful feedback, not merely a red cross.

Do not confuse attendance, viewing, submission, successful assessment and confirmed mastery.

Do not turn personal opinions or honest self-reflection into right/wrong examination questions.

Protect the ability to pass or use fictional scenarios instead of disclosing private experiences.

============================================================
3. READ THE EXISTING PROJECT SYSTEM FIRST
============================================================

This repository ALREADY contains an elaborate Claude Code workflow.

Do not create a competing autopilot, new workflow framework or redundant auditing system.

Read and obey:

- CLAUDE.md
- .claude/rules/course-content.md
- .claude/rules/hungarian-editorial.md
- .claude/rules/safety-and-human-gates.md
- .claude/skills/course-autopilot/SKILL.md
- .claude/skills/course-review/SKILL.md
- .claude/skills/course-fix/SKILL.md
- .claude/skills/hungarian-edit/SKILL.md
- .claude/skills/release-check/SKILL.md
- .claude/finding-format.md
- 01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md

Use the existing /course-autopilot workflow:

/course-autopilot M0-Z --lens all --next-version

Invoke the appropriate Skill tool and actually execute the workflow. Do not merely describe what the command would do.

Important historical context:

The repository already completed several autopilot iterations, including AP-2026-10-13-06. Their terminal state DOES NOT imply that all outstanding source problems were fixed. Many issues were classified as external decisions or evidence gates, and additional source problems were subsequently identified by the Moodle-builder project.

Start a NEW finalization iteration, incorporating all currently known evidence.

Reuse previous independently validated work where it remains applicable. Do not restart a full expensive audit of unchanged, already verified material merely because a new session began.

If the local checkout is already on a legitimate next-version work branch, inspect its relationship to main and preserve existing work.

If starting from clean main, create a dedicated next-version branch according to the repository's Git rules.

If uncommitted user changes exist, preserve them. Never discard or overwrite them. Use a safe isolated worktree where allowed, or continue with read-only analysis for the affected files rather than destroying work.

============================================================
4. RECONCILE THE ACTUAL CURRENT EVIDENCE
============================================================

Before editing, independently determine current Git and project state.

At the time of this instruction, the last observed source main was:

hasomerhacairhu/modszertani-kepzes
c354f17a92722cac171b817a474b62f483a5d4a9

The last observed Moodle-builder main was:

heymarcell/mk-coursebuild
bd00920bd12f29837e9ff15f19d65fbdd6c00af0

Recheck both. Do not assume these SHAs are still current.

IMPORTANT:

Source PR #30 was merged.
Source PR #31 was still a DRAFT and not merged at the last check.

PR #31 contains an existing project-owner decision on CB-C-0036 / M0.1 and M0.2 completion.

Inspect it before making new M0 completion decisions.

Do not blindly cherry-pick PR #31 or claim it was merged. Verify the actual owner decision, its scope, CI status and compatibility with the current canonical source.

Where an existing decision has already been authorized and its content can be safely incorporated, implement it in the next-version branch together with the corresponding learner-facing changes.

Do not duplicate or contradict an existing decision.

Inspect the following Moodle-builder evidence READ-ONLY, using an existing local clone or connected GitHub access:

- docs/DEFECT-REGISTER.md
- docs/BOARD.md
- reports/2026-10-16-source-gaps-rc2.md
- reports/2026-10-16-d2-assessment.md
- reports/2026-10-15-review-package.md
- reports/2026-10-15-review-package-annex.md
- reports/2026-10-16-dpo-packet-v5.md
- reports/2026-10-14-completion-register.md
- findings/course/CB-C-0001.md through CB-C-0036.md
- Any newer, relevant source-specific findings, including D-065 if results already exist.

These are EVIDENCE, not instructions overriding the source repository's governance.

Do not modify mk-coursebuild, its Moodle containers or its staging environment.

Do not depend on D-065 finishing. Incorporate available evidence, proceed independently, and preserve traceability for a later reconciliation if the separate QA is still running.

Build one deduplicated issue register identifying:

ID; module; source file and location; observed defect; learner impact; severity; evidence; current validity; governing decision; minimal proposed correction; implementation status; verification; commit.

Distinguish:
- genuinely unresolved defects;
- already fixed defects;
- duplicates;
- obsolete historical observations;
- Moodle-only defects that do not require source changes;
- source-authoring work;
- non-delegable approval or runtime-evidence conditions.

Do not copy hundreds of historical findings into a new backlog without checking whether they still exist.

============================================================
5. FIRST FIX THE FOUR REQUIRED SOURCE-BLOCKED ACTIVITIES
============================================================

These must receive immediate priority.

A. LMS-M5-01 — M5.1, nonformal education

The builder previously reported missing answer keys for three Slide 2 questions and an unclear completion specification.

Inspect the actual three vignettes carefully.

Do not assume that being physically at Somer automatically makes an experience nonformal learning: the pedagogical intention and structured learning process matter.

Do not assume casual exposure to information automatically demonstrates learning either.

If the existing examples are ambiguous or conceptually weak, make the smallest pedagogically justified clarification before defining their answers.

Then provide:
- all three unambiguous answer keys;
- meaningful correct/incorrect feedback;
- a completion rule consistent with approved ERT/BSPEC decisions;
- consistent learner instructions and developer metadata.

Preserve legitimate unscored reflections.

B. LMS-M5-05 — M5.4 Modulproduktum

Provide a COMPLETE standalone Hungarian Moodle Assignment description.

It must explain:
- the actual learner task;
- the fields of the table;
- minimum deliverable;
- worked example;
- how to submit;
- accessible text and file alternatives;
- deadline relationship;
- privacy boundaries;
- rubrics and success conditions;
- correction and resubmission pathway;
- mentor confirmation and next-module progression.

Reconcile the existing three-level rubric:
Hiányos / Alapszint / Erős.

Determine whether point mappings, Grade type and Maximum grade are established by authoritative records.

Do NOT mistake synthetic test fixture scores for a previously approved assessment decision.

If a numeric mapping is not actually decided, develop the smallest coherent proposal, independently verify it, and separate the proposed assessment decision from already authoritative criteria. Do not falsely mark it approved.

Correct the R4 Alapszint rubric cell so internal assessor instructions are not accidentally displayed as learner-facing level descriptors.

C. LMS-M6-05 — M6 Játéklap

Write the missing COMPLETE learner-facing Assignment description.

Use the existing M6.B and M6 KAPU source as the specification.

Preserve:
- independent individual submission;
- tool type;
- pedagogical goal;
- target kvuca;
- concrete implementation;
- safety;
- inclusion;
- observable assessment requirements;
- online-text or accessible file submission.

Do NOT recreate the rubric or grade system unnecessarily. Point / 15 and existing rubric rules already exist in the source.

D. LMS-M7-06 — Peula v2 + Zmán Kvucá

Write a complete, understandable learner-facing final assignment and establish ONE internally consistent template specification.

Reconcile:
- M7.4 Peula v1;
- M7.B workshop;
- M7 KAPU;
- the Peula 11-point structure;
- the five Zmán Kvucá checklist dimensions;
- the time–task–responsible-person operational plan;
- AI-use transparency;
- the three-line if–then commitment;
- the M7 revision period;
- the 24-point analytic rubric.

Preserve the existing mastery rule:
at least 17/24 overall, with the already prescribed critical R1/R4/R5/R6 criteria.

The separate 10-point Zmán Kvucá checklist is supporting assessment, not an extra independent passing gate.

Ensure the v2 assignment is not confused with the formative v1 assignment.

Create or complete the necessary accessible template specification.

Do not invent an additional submission activity, requirement or penalty without explicit canonical support.

For all four activities:

- Reconcile their manifest entries.
- Reconcile module hubs, lessons, rubrics and relevant peulas.
- Check incoming and outgoing prerequisites.
- Check grading, completion and remediation separately.
- Check that all mandatory source elements are buildable.
- Verify that no downstream module unlocks incorrectly.
- Document exactly what source blocker each correction resolves.

============================================================
6. FIX THE REMAINING CROSS-COURSE DEFECTS
============================================================

After the four source-blocked activities, process all currently confirmed and newly verified findings.

Prioritize these root-cause groups.

A. Completion and mastery

- M0.1/M0.2 conflicting completion definitions and CB-C-0036.
- H5P opinion responses accidentally treated as grades.
- Zero-point H5P activities that can never satisfy the configured completion.
- Interactive Books or split lessons completing before required tasks.
- Course completion incorrectly accepting failed GATE-CP outcomes.
- SUBMITTED versus CONFIRMED ambiguity.
- QUIZ-M review and retry paths.
- ASSIGN-S reassessment potentially undoing completion.
- Nine split lessons from the D2 assessment:
  M0.3, M1.2, M1.3, M3.1, M3.2, M3.4, M7.1, M7.2, M7.4.

For each, decide what the educationally intended behavior actually is, then make the specification match that intent and the real platform.

Do not invent artificial scored questions just to produce a grade.

B. Misleading interaction instructions

Find and repair cases where the learner is told to:
- drag items when only radio buttons exist;
- write text where no field exists;
- press a button that does not exist;
- continue to a summary slide that is absent;
- submit something not actually collected;
- download a file that does not exist;
- use a resource that has moved or was never created.

Respect the distinction between:
- privately reflecting;
- writing into a learner-local worksheet;
- writing into stored Moodle input;
- submitting a formally assessed Assignment.

C. Feedback and assessment quality

Review:
- ambiguous answer keys;
- feedback that contradicts the chosen answer;
- incorrect red crosses on subjective opinions;
- feedback that explains nothing;
- inadvertent answer leakage between examination attempts;
- inconsistent rubric criteria;
- inconsistent response lengths;
- unintended grade/score exposure;
- unclear retry and mentor-review instructions.

Special attention:
M1.4 SBI length, M2 rubric terminology, M3.2, M3.4, M4.2, M4.3, M5.1 and M7.

D. Actual learning transfer

For each module, check that:
- learning objectives are actually taught;
- there is meaningful practice before summative assessment;
- learners receive actionable formative feedback;
- face-to-face activities reinforce online learning;
- Study Lab remediation targets real difficulties;
- required worksheets are usable;
- previous module products contribute logically to later work;
- M7 Peula v2 integrates the earlier competencies;
- Z closure prepares the learner for supervised field practice.

Do not add busywork to make every module look symmetrical.

E. Teaching quality and workload

Review cognitive load, lesson length, task complexity, repetition, progression, instructional clarity, practical examples, motivational structure, learner agency and realistic time requirements.

Reduce unnecessary repetition only when doing so preserves the teaching function.

Never remove important rehearsal, safeguarding or spaced-retrieval practice merely because it repeats a concept.

F. Specific known source problems

Investigate and close the applicable cases involving:
- M2.2 TOP-3 values and missing retained selection state;
- M7.3 downloadable Zmán Kvucá worksheet;
- M1.1 and M6.1–M6.3 texts referring to obsolete H5P UI;
- M2.4 appearing before M2.3 without explanation;
- M5.3 delayed retrieval appearing outside the expected sequence;
- misleading internal GATE_CONFIRMED names;
- student-visible Glossary internal metadata;
- learner-facing English Moodle implementation jargon;
- inconsistent document and activity titles;
- missing quiz introductions;
- offline and printable instructions referring to online-only actions;
- inconsistent Hungarian wording, grammar, typography and formatting.

Do not treat this list as exhaustive.

============================================================
7. SAFEGUARDING, PRIVACY AND ACCESSIBILITY
============================================================

Use the existing source policies and closed decisions as the authority.

Do NOT create new child-protection escalation rules, special-data legal bases, retention policies or organizational roles.

When a previously adopted rule has not reached a learner-facing file, propagate it accurately.

When no authoritative decision exists, prefer a design that does not create the risky data flow or require the questionable interaction, provided this does not remove a mandatory learning objective.

For example:
- An unapproved sensitive opinion collection should not silently become a new required stored response.
- A personal reflection should remain learner-local if the goal does not genuinely require storage.
- A third-party AI service must not become mandatory for course completion.
- Sensitive real-world examples can usually be replaced with fictional scenarios.
- Safeguarding instructions must remain prominent even when a lesson is made shorter.

Pay particular attention to:

1. The 25 optional Moodle Feedback activities and their privacy implications.
2. Individual completion logs versus supposedly anonymous responses.
3. TEXT-C free-text submissions.
4. Z.3 and Z.4 personal reflections.
5. M2 ideological/opinion input.
6. Mentor and teacher group visibility.
7. Learner-facing privacy notices.
8. The Memuna escalation pathway.
9. Boundary-setting between madrih and hanih.
10. Situations involving minors, private communication and disclosures.
11. AI tools and the equivalence of no-AI alternatives.

Where a genuine DPO, Memuna or legal signoff is required:

- Do not request it interactively.
- Do not invent it.
- Do not misclassify it as completed.
- Prepare the exact finished, source-linked decision/evidence package.
- Complete all other independently correctable changes.
- Preserve the genuine release gate.

A missing external signature should not prevent completion of unrelated editorial and technical work.

Accessibility and media:

- Follow the repository's WCAG 2.2 AA specification.
- Check real keyboard and non-drag paths.
- Specify accessible names, labels, alt text, transcripts, captions and text alternatives where necessary.
- Do not burn important instructional text into an image unnecessarily.
- Ensure no-AI, low-bandwidth and printable alternatives remain usable.
- If an optional video, audio or graphic adds no instructional value, do not make it a pilot prerequisite.

============================================================
8. HUNGARIAN EDITORIAL AND DESIGN QUALITY
============================================================

All learner-facing and trainer-facing prose must be natural, accurate Hungarian.

Follow the repository's Hungarian editorial rule rather than generic AI prose.

The voice should be:
- direct;
- clear;
- adult;
- practical;
- encouraging without excessive cheerleading;
- human and natural;
- consistent in tegezés;
- appropriate for Hungarian-speaking Somer participants.

Preserve the approved terminology:
madrih, hanih, kvuca, peula, hágsámá, dugma isit, Leviatán, Zmán Kvucá, Memuna, etc.

Do not casually normalize proper names or specialized organizational terms.

Inspect:
- heading hierarchy;
- broken sentence structure;
- awkward line breaks;
- readability of paragraphs;
- parallel grammatical structure of lists;
- unclear references such as "ez", "az", "itt";
- consistent typographic quotation marks;
- punctuation;
- overly long sentences;
- inconsistent capitalization;
- unnecessary code-like labels;
- unnecessarily repeated instructions;
- consistency between titles, questions, options and feedback.

Keep metadata, production specifications and learner text clearly separated.

For multimedia and printable materials, ensure the source can produce balanced, readable layouts. Do not attempt to solve rendered PDF defects merely by inserting arbitrary newlines into Markdown.

Most importantly:

DO NOT MASS-REWRITE WORK THAT IS ALREADY GOOD.

Minimal, proven, high-value corrections are preferred.

============================================================
9. RESEARCH AND INDEPENDENT CHALLENGE
============================================================

Research whenever genuinely necessary to avoid guessing.

Source hierarchy:
1. Approved project-owner decisions and canonical repository documents.
2. Official technical specifications and platform documentation.
3. Primary pedagogical, accessibility or legal sources.
4. Existing independently verified project evidence.
5. Secondary explanations, used cautiously.

For Moodle, confirm behavior against the actual target version or its source code and official documentation, not generic memory of older Moodle releases.

For H5P, verify that proposed content types, completion signals and UI behaviors actually exist.

For accessibility, use W3C and project standards.

For pedagogical claims, prioritize sound evidence on formative feedback, retrieval practice, spacing, transfer, worked examples and constructive alignment.

For policy or legal questions, research can inform a proposal but cannot substitute for an organizational or professional authorization.

Whenever research changes a material recommendation, include its source and checked date in the technical audit trail.

Use independent reviewer agents when justified:
- pedagogy-reviewer;
- assessment-reviewer;
- hungarian-editorial-reviewer;
- safety-policy-reviewer;
- implementation-reviewer;
- verifier.

Keep reviewer agents read-only.

Only the principal session may modify course files, sequentially.

Do not launch expensive redundant reviews of unchanged, already verified material.

An independent review is useful only if you incorporate its validated findings into the implementation.

============================================================
10. EXECUTION STRATEGY — FINISH, DO NOT CIRCLE
============================================================

Use a disciplined sequence:

PHASE A — PREFLIGHT
- Confirm repository, branch, working tree and previous work.
- Verify active and historical autopilot state.
- Check the current base commit.
- Read relevant governance and canonical material.
- Establish safe work branch.
- Run baseline integrity and release checks.

PHASE B — RECONCILE
- Merge and deduplicate confirmed source findings.
- Recheck affected files.
- Identify already-correct material.
- Identify genuinely actionable fixes.
- Record non-delegable approval/evidence conditions separately.

PHASE C — SOURCE-BLOCKER REPAIR
- Complete M5.1, M5.4, M6 Játéklap and M7 Peula v2 source deficiencies.
- Correct related source references and completion definitions.
- Perform targeted validation.
- Commit completed work.

PHASE D — MODULE-BY-MODULE REPAIR
- Process M0, M1, M2, M3, M4, M5, M6, M7, Z.
- Fix every independently verified, currently present source defect that is within the authorized scope.
- Reuse old validated reports when their evidence remains applicable.
- Perform targeted QA.
- Commit logical changes.
- Continue immediately.

PHASE E — CROSS-MODULE AND CANONICAL RECONCILIATION
- Program plan.
- Module hubs.
- Rubrics.
- LMS activity manifest.
- Runtime acceptance specifications.
- Glossary.
- Privacy and safeguarding declarations.
- Release readiness.
- Media declarations and cross-references.

Do not alter closed policies; propagate them accurately.

PHASE F — FINAL SOURCE QA
- Full cross-module consistency review.
- Learner journey review.
- Trainer journey review.
- Assessment and completion review.
- Safeguarding/privacy review.
- Accessibility and low-bandwidth review.
- Hungarian language review.
- Media/asset/link integrity.
- Adversarial regression review.

PHASE G — FINAL VALIDATION AND REPORT
- Run the full existing release-check procedure.
- Fix regressions.
- Read every changed diff.
- Produce final traceable reports.
- Update the autopilot ledger.
- Commit and verify the final local state.

Efficiency rules:
- Never stop after one phase.
- Never regenerate a plan that already exists without a real change in evidence.
- Never loop endlessly on the same undecidable issue.
- Never create three duplicate reports where one decision-grade report suffices.
- Do not defer ordinary source work because unrelated external evidence is missing.
- Do not weaken tests to make them green.
- Do not spend time polishing internal audit bureaucracy while mandatory learner content remains incomplete.
- Keep the main context lean; delegate evidence extraction and review where appropriate.
- Resume from the persisted ledger after compaction instead of repeating completed work.

============================================================
11. TESTING AND VERIFICATION
============================================================

At each significant checkpoint and in the final state, use the repository's approved validation process.

The final pass must include, as applicable:

python3 -X pycache_prefix="${TMPDIR:-/tmp}/pyc" -m py_compile tools/*.py

python3 tools/content_integrity.py

python3 tools/content_integrity.py --release-report

python3 tools/media_manifest.py --selftest

python3 tools/media_manifest.py validate

python3 tools/media_manifest.py check

python3 tools/media_manifest.py reconcile

python3 tools/media_manifest.py lint --high-only

python3 -m unittest tools.test_media_manifest

python3 tools/autopilot_ledger.py validate

python3 tools/autopilot_ledger.py check

git diff --check

git diff --check origin/main...HEAD

Also invoke /release-check according to its own rules.

For visible-text changes, use the approved visible-text pinning procedure with actual finding/decision IDs, AFTER validating the changes.

Never manually edit generated manifests or the approved-visible-text JSON.

If an approved media regeneration is required, use the existing media_manifest.py build process and keep generated changes in a separate logical commit.

Do not edit .claude rules, safety hooks or CI configuration to evade failure.

Test source-level invariants, including:
- answer keys;
- grade thresholds;
- retry counts;
- mandatory versus optional activities;
- section and activity IDs;
- links and referenced files;
- module prerequisites;
- required asset declarations;
- safety instructions;
- privacy restrictions;
- learner-visible text;
- consistency between assignment instructions and rubrics.

Static source tests are not proof of Moodle runtime behavior. Explicitly distinguish verified source correctness from pending runtime verification.

A zero-error content-integrity result does not mean the course is pedagogically complete.

============================================================
12. DEFINITION OF DONE
============================================================

Do not end merely because the autopilot ledger says TERMINAL.

TERMINAL may coexist with many genuine unresolved items.

Your actual completion target is:

1. Every source file and module has a traceable review status.
2. All previously verified findings have been reconciled against the current source.
3. No independently fixable source defect remains open.
4. The four required source-blocked activities have been corrected to the fullest extent supported by authoritative decisions and owner-delegated source authoring.
5. All justified source changes are reflected in dependent files.
6. No valid project-owner decision has been accidentally overwritten.
7. Every changed teaching text is natural, clear Hungarian.
8. The learner and trainer instructions agree with actual activity behavior.
9. Every required resource has a complete, traceable source specification or a clearly identified legitimate outstanding dependency.
10. Source and media validation pass without suppressing failures.
11. The final diff has been inspected for regressions and content loss.
12. Local commits exist and the worktree is clean.
13. The remaining non-delegable conditions, if any, are fully specified and are NOT disguised as fixed.
14. The final report states the source readiness honestly and distinguishes it from runtime and final-release readiness.

If a genuine non-delegable external condition remains, it does NOT cancel the completed work. Exhaust all actionable improvements and report that condition separately.

Do not invent the word "approved" or the status READY_FOR_CONTROLLED_PILOT.

Do not downgrade real blockers simply to reach ALL_FIXED.

============================================================
13. REQUIRED FINAL DELIVERABLES
============================================================

Produce persistent, concise but complete evidence in the existing audit area:

01 Fejlesztés/04 Audit/

At minimum create a final SOURCE FINALIZATION report documenting:

A. Executive verdict
- Starting and ending source SHA.
- Branch.
- Source implementation status.
- What was actually completed.
- What remains outside autonomous source implementation.

B. Changes by module
- Before/after summary.
- Changed files.
- Finding or decision IDs.
- Learner and trainer benefits.
- Validation evidence.
- Commit SHAs.

C. Cross-module repairs
- Completion.
- Assessment.
- Prerequisites.
- Privacy.
- Safeguarding.
- Terminology.
- Accessibility.
- Resources and media.

D. Source-blocker closure
A dedicated table for LMS-M5-01, LMS-M5-05, LMS-M6-05 and LMS-M7-06, with exact evidence proving which parts are no longer blocked.

E. Independent QA
- Scope and coverage.
- Reviewers actually used.
- New defects found.
- Corrections made.
- Test commands and outcomes.
- Unassessed runtime behavior clearly marked.

F. Residual items
Only genuinely outstanding items.
Group them by:
- professional decision;
- professional signoff;
- runtime evidence;
- unavailable external information;
- technical blocker that cannot be safely resolved inside this repository.

For each remaining item: exact file, consequence, existing evidence, what is already prepared, and what is still missing.

Do not dump obsolete historical issues here.

G. Course readiness
Separately report:
- SOURCE CONTENT readiness;
- SOURCE BUILD-SPEC readiness;
- actual Moodle runtime readiness, if evidence exists;
- final controlled-pilot release authorization.

H. Final handoff
- Current branch and local commits.
- Test results.
- Worktree status.
- The smallest necessary next action outside this autonomous repository task.

Update the existing AUTOPILOT-LEDGER.md accurately. Do not start yet another parallel tracking system.

============================================================
14. EXECUTE NOW
============================================================

Start with the preflight, identify the highest-value existing source blockers, and BEGIN EDITING.

Do not ask me to confirm the plan.

Do not present multiple-choice questions.

Do not stop to request a missing authorial comment when the requirement can be reliably derived from the approved programme, existing rubrics and source.

Do not block an entire module because one independent policy question remains unresolved.

Do not treat an existing previous "TERMINAL" status as permission to do nothing.

Do not push, merge, deploy or modify Moodle.

Do not promise or fabricate a professional signoff.

Do the work. Verify it. Commit it. Continue.

The measure of success is the amount of VERIFIED, HIGH-QUALITY, COMPLETED COURSE SOURCE delivered without damaging already-correct material.

Your final response must be in Hungarian and must report actual implemented results, not intentions.

BEGIN EXECUTION.
