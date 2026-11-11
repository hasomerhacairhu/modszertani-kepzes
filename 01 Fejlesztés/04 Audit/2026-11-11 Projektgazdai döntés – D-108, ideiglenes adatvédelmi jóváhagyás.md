# Projektgazdai döntés – D-108, ideiglenes adatvédelmi jóváhagyás (2026-11-11)

A projektgazda üzenete 2026-11-11-én (kb. 14:05 UTC), szó szerint, angolul. A projektgazda ideiglenes adatvédelmi döntéshozóként jár el; ez nem független DPO-felülvizsgálat és nem DPO-aláírás. Nyilvántartás: `02 Tervezet/Emberi jóváhagyás szükséges.md` 23. szakasz.

> # D-108: Interim Privacy Approval and Same-Day Final Build
>
> **Deadline: 2026-11-11, 23:59 Asia/Jerusalem.**
>
> The owner has declared that they are acting as the interim privacy decision-maker for this project and approves the recommended privacy decisions below.
>
> This is a new explicit owner decision. Record it verbatim and with its date, separately from previous decisions.
>
> It authorizes the privacy-related source changes and their technical implementation within the existing project permissions. It does **not** certify independent GDPR-DPO review, approve unrelated specialist responsibilities, or authorize real learners or production.
>
> ## 1. Nine privacy notices: APPROVED WITH SPECIFIED CHANGES
>
> Review the exact current content of course PR #36, then resolve the outstanding DPO decision placeholders as follows.
>
> | Activity | Decision |
> |---|---|
> | LMS-Z-06, Z.3 | Approve the notice. Clearly describe the actual text answers collected, 90-day retention after course completion, named submission and group-scoped mentor access. Keep the child-safeguarding instructions in their appropriate instructional context. No automatic mentor email notification by default. |
> | LMS-M3-06, M3 gate quiz | Approve the recorded 90-day retention for attempt details after confirmed result and 24 months for final score and gate result, subject to the documented deletion process and restricted access. |
> | LMS-M0-06, entry quiz | Approve the diagnostic purpose. Individual results must not be exposed to mentors. Use aggregate reporting for the team. Retain identifiable diagnostic results only as long as necessary, with 90 days as the proposed default, rather than automatically extending gate-result retention to this quiz. |
> | LMS-M0-07, M0.1 questionnaire | Approve the stated learner-support purpose, access only for the assigned group mentor and approved technical administrators, and deletion/anonymization 90 days after course completion. |
> | LMS-M5-06, self-check | Approve the educational and formative purpose. Recommend 90-day retention for identifiable diagnostic results, not the 24-month gate-result rule. |
> | LMS-M6-06, self-check | Same decision as M5. |
> | LMS-M7-05, Peula v1 | Approve the documented 12-month retention after course completion, restricted to the assigned mentor/evaluator and necessary administrators. |
> | LMS-M7-07, readiness quiz | Approve the recorded 90-day attempt-details and 24-month final-result retention for this gate, with the established restricted evaluator access. |
> | LMS-Z-04, closing reflection | Approve 90-day retention after course completion. The video submission path remains disabled. Enabling it later requires a separate privacy notice, lawful basis and applicable participant/guardian consent process. |
>
> These approvals are conditional on the statements matching the actual Moodle configuration and enforceable data-retention policy.
>
> Do not invent retention guarantees, access restrictions, contacts or operational facts. If an approved wording decision conflicts with the existing source policy or current functionality, prepare the corresponding policy/configuration change and verify it before considering that notice complete.
>
> Remove every `[PROPOSED]` and `DPO-döntés` placeholder from the final approved learner-facing text, resolving each explicitly, never by blind deletion.
>
> ## 2. Additional privacy decisions
>
> **E025:** Approve an accessible text marker, **"Névvel rögzített"**, for the 11 named forms. Place it with the form/activity name and ensure assistive technology can read it. Do not apply it to the 25 forms configured without recorded names. Verify the exact 11/25 mapping using `tools/d106/named_forms.py`. Do not imply that Moodle's name-free mode provides absolute technical anonymity.
>
> **"Név nélküli":** Approve replacing the misleading generic "Névtelen" terminology, while ensuring the privacy notice accurately describes the database's remaining technical identifiers.
>
> **A2:** Approve the strictly group-scoped mentor access required to review named Z.3 responses. No broad teacher or administrator privilege expansion. Require positive and negative access tests.
>
> **Mentor notifications:** Default OFF. A later opt-in requires confirmation of the actual mechanism, recipients, minimal notification content and updated learner notice.
>
> **X-16-PRIV:** A learner's authenticated personal-data access/export may include their own assessment records where legally applicable, without making hidden pedagogical points visible in ordinary course views. Verify access control.
>
> **X-16-WS:** Do not expose restricted grades through mobile or web-service endpoints. Keep learner mobile access unavailable until a role-specific solution is verified and accepted by the LMS owner. Do not silently disable services for other roles.
>
> **D-100 privacy values:** Confirm the previously recorded retention, access-minimization and contact-at-deployment decisions, subject to the specific non-gate diagnostic retention decisions above.
>
> **Privacy contact:** The contact field must contain the organization's real, approved, reachable contact before any learner has access. Do not invent an email address or publish an unresolved placeholder.
>
> **Supervised real-learner pilot:** Privacy approval in principle only, conditional on verified controls, appropriate information and lawful basis, age-appropriate safeguards, Memuna agreement and a separate written pilot GO.
>
> ## 3. Record the decision correctly
>
> Create one canonical D-108 decision record with the owner's statement, date, exact per-item decisions, required amendments and verification conditions.
>
> Attribute it to the **owner acting as interim privacy reviewer**, as declared in this conversation.
>
> Do not misrepresent it as an independent external DPO's signature or as evidence of formal appointment. Flag any separation-of-duties/conflict-of-interest requirement for subsequent organizational compliance review.
>
> Update the existing DPO decision register and approval evidence. Populate `APPROVALS.json` only for decisions that are actually recorded and whose conditions have been met. Never manufacture missing evidence to satisfy a gate.
>
> ## 4. Execute the source and build preparation
>
> Apply the approved notice changes to the actual source, together with the approved E018 fix pack, E025 marker and previously tested E040 correction.
>
> Resolve the diagnostic retention policy consistently across source wording, deployment configuration and implementation. Where actual deletion behavior remains unverified, keep the relevant release acceptance item open.
>
> Preserve the author's original pedagogical meaning, the safeguard instructions and traceable source citations.
>
> Review PR #36, prepare the exact approved version, and perform course repository operations only under the existing owner authorization and repository safeguards. If the guard requires a manual merge or `/course-pin`, provide the exact action and do not bypass it.
>
> Once the required source decisions are genuinely satisfied, proceed with the one definitive build, full targeted regression, data-free export, integrity checks, independent restore and rollback verification.
>
> Use the already-installed private `push-dev.sh` for authorized private pushes. Do not reintroduce compound-command approval stalls or widen the public publishing permissions.
>
> ## 5. Remaining independent gates
>
> The owner's interim privacy decision does not substitute for:
>
> - Memuna's safeguarding review, especially CB-C-0040.
> - Accessibility review and the physical iPhone/Android tests.
> - Assessment-owner confirmation of E039's wording and grading semantics.
> - Verified deployment contacts and receiving-site configuration.
> - Final pilot and production GO decisions.
>
> Proceed with every technically authorized task in parallel. Do not halt the entire engineering workflow because a separate human approval remains pending.
>
> **The priority is to complete the updated, technically verified handover today, without falsifying independent approvals or exposing real learners prematurely.**
>
> Report the exact approvals recorded, source commits, final pin, test results, export hash, remaining true dependencies and distinct technical/pilot/production readiness statuses.
>
> Start executing now.
