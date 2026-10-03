# Projektgazdai döntéscsomag — VO QA, 2. fázis (2026-10-03)

> **Kurzusrepó-másolat:** a hangneveket a 2026-10-03-A projektgazdai döntés szerint szerepnevek váltják („kanonikus narrátorhang” / canonical narrator voice, „második hang” / second voice; a hangnevet tartalmazó szótár- és fájlnevekben is), a QA-repó neve helyén „VO QA-repó” áll; az ADDENDUM 1. kérdéséből egy, a hangnevek és a forrás-beszélők viszonyáról szóló félmondat kimaradt (projektgazdai döntés, 2026-10-03 — `2026-10-03 Projektgazdai döntések – VO 2. fázis, kiegészítés.md`, K1); a teljes szöveg a VO QA-repóban van; minden más szó szerinti.

> Ez a fájl a projektgazda 2026-10-03-i, a 2. fázist elindító döntéscsomagját rögzíti **szó szerint**, ahogy beérkezett
> (a felhasználó a csomag kötelező érvényét és a 2. fázis indítását külön is megerősítette; a kurzusoldali javításokat
> a felhasználó a `/course-fix` skill-lel maga futtatja). Ez a D-01…D-23 döntések bizonyítéka; a gépi olvasatú
> változat: `decisions/pronunciation-register.json` és `decisions/decision-log.json`.

---

PROJECT OWNER DECISION PACK
VO QA — Phase 2
Date: 2026-10-03

Use this message as the binding project-owner decision input for Phase 2 of:

VO QA-repó: reports/vo-audit-2026-10-02/report.md

The course repository source of truth is:

hasomerhacairhu/modszertani-kepzes
main @ cfeef1efb30ce1e0942281d5657d83cc765fa719

PR #12 is already merged.

The Phase 1 audit is complete. Do not re-run a general audit and do not reopen decisions that are explicitly resolved below unless new objective evidence makes the selected implementation impossible.

The previous B4 listening decisions remain binding.

RUN PHASE 2.

======================================================================
1. VOICE RIGHTS AND NARRATOR STRATEGY
======================================================================

The canonical narrator voice and the second voice both already exist as usable voices.

Their voice-use rights have been clarified and there is explicit consent from the relevant voice owners.

Therefore the Phase 1 statement that “the voices do not exist yet” is stale and must be corrected wherever it occurs.

Important privacy/provenance rule:

- keep the public/course repository pseudonymous using VOICE-SRC-01 / VOICE-SRC-02 or the existing approved alias scheme;
- do not add real legal names to the public repository;
- do not invent the VOICE-SRC ↔ person mapping if the restricted rights register is not available;
- preserve/use the existing mapping from the restricted VOICE-RIGHTS-REGISTER if available;
- voice IDs and sensitive evidence should only be stored where the existing evidence architecture allows them.

For the first production pass:

THE CANONICAL NARRATOR VOICE IS THE PRIMARY NARRATOR.

Generate the first complete VO pass with the canonical narrator voice.

The second voice is a valid, rights-cleared secondary voice, but do NOT make its calibration a prerequisite for the first production pass.

If the second voice is calibrated successfully later, we can regenerate the VO lines that are intended for a second/different voice.

Architect the pipeline now so speaker-specific lines remain individually addressable and can later be re-rendered with the second voice without changing source IDs, captions, course structure or unrelated audio.

Do not mass-generate final production VO until the Phase 2 pipeline, dictionary, extraction, timing and regression checks are green.

======================================================================
2. RESOLUTION OF D-01 ... D-23
======================================================================

Treat the following as the project owner's decisions.

D-01 — VOICE RIGHTS / EXISTENCE
RESOLVED.

Both voices (the canonical narrator voice and the second voice) exist.
Rights are cleared.
Explicit consent exists.

The rights/consent decision is therefore closed.

Correct stale documentation saying the voices do not exist.

Do not fabricate administrative evidence fields that are not actually present. If the evidence schema requires additional factual fields such as account ownership, age/majority evidence, training-opt-out state, etc., populate them only from real existing evidence. Do not infer them.

The substantive voice-use permission is settled.

--------------------------------------------------

D-02 — PRODUCTION MODEL / SETTINGS
APPROVE RECOMMENDATION (a).

Canonical tested configuration for this production generation:

- model: eleven_v4
- stability: 0.35
- similarity: 0.75

Do not document unsupported v4 controls as if they exist.

In particular:

- no fictional speed control;
- no fictional style control;
- timing is solved through text, duration windows, and limited post-processing;
- settings actually sent in the request must be recorded in the production sidecar/manifest.

Update VO documentation so it describes the actual tested v4 configuration rather than the previous Flash/v3 assumptions.

--------------------------------------------------

D-03 — CANONICAL PRONUNCIATION DICTIONARY
APPROVE RECOMMENDATION (a).

The QA-generated production dictionary becomes the canonical pronunciation layer.

Requirements:

- stable dictionary ID;
- stable version ID;
- dictionary version recorded with each production configuration;
- exact PLS/config source reproducible;
- no “first production pass without dictionary” workflow anymore.

The known bad no-dictionary pronunciations must not be reintroduced.

--------------------------------------------------

D-04 — B4 PRONUNCIATIONS
APPROVE RECOMMENDATION (a).

The VOICE-BIBLE and all pilot/test copies must record the already approved B4 pronunciations.

Keep the visible written course text unchanged.

Canonical spoken forms include the already approved forms for:

- madrih → approved “mádrih” pronunciation / [maːdrix]
- hanih → approved [xanix]-family pronunciation
- Tuckman → “Takmen” / “Brúsz Takmen”
- forming / storming / norming / performing / adjourning
  → the already approved Hungarian-friendly spoken forms

Do not re-propose variants previously rejected by ear.

--------------------------------------------------

D-05 — LEVIATÁN
RESOLVED: USE OPTION (b).

The LAST / B Leviatán listening variant was approved by ear.

Therefore:

DISPLAY / COURSE / CAPTION TEXT:
Leviatán

TTS pronunciation:
use the previously approved “Leviatan” sound, i.e. the B4 pronunciation.

Implement the necessary TTS aliases, including inflected forms, for example:

Leviatán → Leviatan
Leviatánnál → Leviatannál

Do not change the canonical written spelling in learner-facing material.

The long-final-á raw reading is NOT the selected production pronunciation.

--------------------------------------------------

D-06 — ZMÁN KVUCÁ / DUGMA ISIT
CLOSE THE LISTENING DECISION.

The currently recommended/approved pronunciations sound acceptable.

Use the current approved pronunciations for:

- Zmán Kvucá
- dugma isit

Do not schedule another dedicated listening round for these unless the Phase 2 implementation causes an audible regression.

Do not change their canonical written spelling.

--------------------------------------------------

D-07 — 112
RESOLVED: OPTION (a).

Pronounce:

“száztizenkettő”

The learner-facing written text remains 112.

Update the VOICE-BIBLE exception accordingly.

Do not pronounce it as “egy-egy-kettő”.

--------------------------------------------------

D-08 — LEGAL / AI TRANSPARENCY CLASSIFICATION
IMPLEMENT CONSERVATIVELY, BUT DO NOT FABRICATE A THIRD-PARTY SIGNATURE.

As project owner I approve implementing the conservative transparency path.

However:

do NOT claim that a lawyer, DPO or Memuna personally signed something unless actual evidence of that sign-off exists.

Distinguish:

A) CONTENT / IMPLEMENTATION DECISION
approved by project owner;

from:

B) FORMAL RELEASE EVIDENCE
which remains an evidence gate if the required role has not actually signed.

Therefore:

- do not state “legal review completed” unless there is real evidence;
- do not state “DPO approved” unless there is real evidence;
- do not state “Memuna approved” unless there is real evidence;
- do implement the safe transparency treatment now.

Use D-21 below for D9 placement.

Formal evidence gates may remain open without reopening the implementation decision.

--------------------------------------------------

D-09 — TEXT NORMALIZATION
APPROVE THE AUDIT'S EVIDENCE-DRIVEN RECOMMENDATION.

Initial canonical behavior:

apply_text_normalization = auto

plus targeted deterministic tts_text normalization for known failures.

Examples include:

13–17 → spoken “tizenhárom–tizenhét”

and other explicitly validated transformations.

Make apply_text_normalization an explicit configurable and logged parameter.

Run the Phase 2 auto-vs-off probe specified by the audit.

If the measured test demonstrates that `off` + deterministic preprocessing is objectively superior, document the evidence and switch the production setting without asking me to repeat the same policy decision.

Do not silently change it.

--------------------------------------------------

D-10 — PAUSE POLICY
APPROVE THE RECOMMENDATION.

Base policy:

1. punctuation is the primary TTS pause mechanism;
2. Markdown line breaks and blank lines are NOT TTS pause controls;
3. where listening QA shows an insufficient paragraph boundary, post-production may insert approximately 0.6–1.0 s spacing;
4. do not split every paragraph into separate TTS API requests merely to manufacture pauses.

Update VOICE-BIBLE and pilot documentation accordingly.

--------------------------------------------------

D-11 — EMPHASIS
APPROVE OPTION (a).

The acceptance criterion becomes:

“a jelentést hordozó hangsúly nem sérül (fülre)”

Markdown bold is not a TTS command.

CAPS is not a reliable emphasis control for this model.

Use sentence construction and, only when actually necessary, an editorial text adjustment whose display/caption consequences are handled consistently.

Do not keep a test criterion that the TTS engine cannot technically satisfy.

--------------------------------------------------

D-12 — MASTER AUDIO FORMAT
TARGET:

48 kHz PCM/WAV production master
+ delivery derivatives as required.

Use 48 kHz only if the actual production account/API output supports a real 48 kHz PCM/WAV source.

Do NOT upsample a 44.1 kHz output and call it a 48 kHz master.

If the current production capability objectively cannot return 48 kHz PCM:

- use native 44.1 kHz;
- update the canonical documentation consistently;
- document the reason.

The actual output format and request metadata must be captured in the sidecar.

--------------------------------------------------

D-13 — CANONICAL PRONUNCIATION APPROVAL / P-NAR
APPROVE:

option (a)
+
M4.2-NAR-03 as P-NAR.

The QA B4 register is the canonical pronunciation-decision source.

P1–P3 and P-NAR verify those decisions in production context; they do not reopen them automatically.

Use M4.2-NAR-03 for P-NAR.

Adjust its expected duration to the measured natural duration rather than forcing it into an unrealistic window.

--------------------------------------------------

D-14 — M1.3 TWO-SPEAKER DIALOGUE
MODIFIED STAGED DECISION.

For the FIRST production pass:

use THE CANONICAL NARRATOR VOICE for both spoken roles.

However:

- split the dialogue into proper speaker-specific segments;
- retain speaker identity/labels structurally;
- captions must clearly identify the speakers;
- do NOT concatenate the complete dialogue into a single anonymous TTS stream;
- make each role independently re-renderable.

Later, after the second voice is calibrated, one of the appropriate speaker tracks can be regenerated with the second voice without redesigning the asset.

Therefore:

do not block the first-pass VO production on the calibration of the second voice.

Also do not pretend that two acoustically distinct voices already exist in the first-pass render.

Update VOICE-BIBLE §8 to document this staged production policy honestly.

--------------------------------------------------

D-15 — M4.1 CHARACTER SCENES
APPROVE OPTION (A).

The character remains silent.

The canonical narrator voice, as narrator, quotes the “Sziasztok…” line.

Do not create an additional character voice for this first production path.

Update the contradictory VOICE-BIBLE wording.

--------------------------------------------------

D-16 — M5.3-NAR-01 AND M7.1-NAR-02
APPROVE OPTION (C).

REMOVE the optional audio narration for both.

The complete information remains visually available and in the transcript/text equivalent.

Do not solve these by reading an entire dense slide at extreme speed.

Remove the unnecessary VO production items cleanly through the normal course-fix path and regenerate dependent manifests.

--------------------------------------------------

D-17 — TIMING
APPROVE:

1a + 2 + 3.

That means:

1. For genuine VO overruns, expand the documented duration window to a realistic natural-speech duration rather than accelerating the voice or cutting protected meaning.

2. Z.1-NAR-01:
change the misleading 30–40 s window to approximately 15–20 s, consistent with its actual short source text.

3. For audio introductions where the documented block includes learner thinking time, explicitly distinguish:

- spoken-audio duration
from
- learner thinking/pause duration.

DO NOT attempt 267 words/minute or similar unnatural delivery.

Do not use time-stretching as the main fix.

A tiny <=5% post adjustment may only be used when acoustically harmless and when the underlying duration is already valid.

--------------------------------------------------

D-18 — M1.3 AUDIO DESCRIPTION
APPROVE OPTION (a).

Create a proper audio-description script as a new @source and place it in available dialogue gaps using the existing voiceover derivative architecture.

Use the canonical narrator voice for the first production pass.

Do not invent extended-description player behavior unless necessary.

--------------------------------------------------

D-19 — AUDIO-ONLY ACCESSIBILITY
APPROVE OPTION (B).

For audio-only narration:

- a visible transcript on or adjacent to the slide is the textual equivalent;
- .vtt may remain an archived/derivative artifact;
- do not require a fake caption track inside an H5P Audio component that cannot render it.

Make the LMS/runtime standard explicit and test it.

Apply the same rule consistently to the exceptional M3.3 items.

--------------------------------------------------

D-20 — AVATAR / VOICE PAIRING
APPROVE THE CONTENT RECOMMENDATION:

one consistent stock avatar
+
canonical narration (canonical narrator voice)

for this production path.

Resolve the M1.1 “alternating faces” contradiction accordingly through /course-fix.

The separate J3 contractual/legal evidence question must NOT be falsely marked signed if no real evidence exists.

Project-owner implementation approval is given; formal third-party evidence remains a separate release-evidence matter.

--------------------------------------------------

D-21 — D9 LABEL PLACEMENT
APPROVE OPTION (c).

For audio narration place the required AI-media label:

1. as the first line of the narration transcript / textual equivalent;
AND
2. as the lesson-level footer line.

Use the canonical D9 label text already defined by the course.

Do not invent alternative disclosure copy.

--------------------------------------------------

D-22 — OLD PRONUNCIATION DICTIONARIES
APPROVE OPTION (a).

After the new canonical production dictionary is live and verified:

archive all 10 old “[hangnév] Hungarian QA” dictionaries.

Archive the final evidence dictionary 0d8afa1b last.

Do not delete evidence required to reconstruct previous listening decisions.

Leave the two non-harness active dictionaries:

- somer_[hangnév]_hu_v4.pls
- Dictionary

untouched until their purpose is positively identified.

Never archive/delete an unknown external dictionary just because its name looks stale.

--------------------------------------------------

D-23 — REMAINING LISTENING ITEMS
CLOSE ACCORDING TO THE AUDIT'S RECOMMENDED CURRENT VARIANTS.

I consider the current recommended pronunciations acceptable.

No additional dedicated owner listening round is required before Phase 2.

Implement the audit-recommended/current forms, including:

- energizer → recommended “enerdzsájzer” form;
- Johari → use the currently recommended accepted reading;
- ÉN → it must sound like Hungarian “én”, not English “ín”; use tts_text such as “az én” when required;
- Memunát → current stable pronunciation accepted;
- 13–17 → “tizenhárom–tizenhét”;
- M2.A → “em kettő pont á”;
- madrih / hanih → use the already approved B4 pronunciations re-keyed to the new written forms.

If a Phase 2 regression causes any of these to sound materially different from the accepted probe, flag that regression rather than treating the pronunciation decision as newly open.

======================================================================
3. SPELLING AND TTS SEPARATION
======================================================================

The learner-facing written canon does NOT change.

Keep:

- madrih
- hanih
- hágsámá
- dugma isit
- Zmán Kvucá
- Leviatán

Do not “fix” the course spelling back to old forms merely to influence TTS.

Instead separate:

display_text / caption_text
from
tts_text

where pronunciation normalization is required.

The display text and captions must continue to reflect the canonical learner-facing spelling.

======================================================================
4. REQUIRED PHASE 2 QA-REPO FIXES
======================================================================

Implement every confirmed Phase 1 pipeline defect relevant to production.

At minimum:

A. Fix the narration extractor.

Fully bold lines must NOT be automatically discarded as labels.

Specifically regression-test the blocks identified by IMPL-1, including the M6.3 and M5.3 cases.

After the fix:

spoken source
=
TTS input semantics
=
caption/transcript semantics

except for explicitly documented pronunciation-only tts_text normalization.

B. Re-key the pronunciation system after the spelling migration.

Add proper families/rules for:

- madrih and inflections;
- hanih and inflections;
- dugma isit;
- Zmán Kvucá base form;
- Leviatán using the approved B pronunciation;
- all other forms identified in NYELV-1 / NYELV-3.

Preserve the already accepted sound, not the old spelling.

C. Fix the coverage linter.

The previous migration was able to change spelling while the coverage test still reported zero warnings.

That must become impossible.

Add regression tests proving that an unmapped canonical course spelling such as:

madrih
hanih
dugma isit
Leviatán

causes the expected coverage failure.

D. Implement display_text vs tts_text normalization.

This should handle pronunciation-only substitutions such as:

M2.A → em kettő pont á
13–17 → tizenhárom–tizenhét
Leviatán → approved TTS alias

without altering learner-facing source text.

E. Make text-normalization behavior explicit and logged.

F. Fix/reconcile all stale QA documentation that still describes the pre-2026-10-02 spelling state.

G. Pin the phonetics/test environment sufficiently for reproduction.

H. Implement proper per-request / per-block metadata.

The production sidecar should be able to reconstruct, at minimum:

- source block ID;
- source hash;
- display text hash where relevant;
- tts_text or its hash;
- model;
- voice alias;
- voice ID in an appropriate non-public/evidence-safe representation;
- dictionary ID/version;
- language;
- stability;
- similarity;
- normalization mode;
- output format/sample rate;
- request ID;
- character count / character cost;
- generated file hash;
- timestamps;
- stitching/segment relationship where applicable.

Do not store secrets.

I. Implement synthesis usage accounting.

Every synthesis/probe should produce a usage record.

Protect PROBE_BUDGET automatically rather than relying on manual memory.

J. Make dictionary archival safe.

Before archiving any dictionary, verify its ID/name and that it is one created/owned by the expected workflow.

K. Build structured listening/review evidence.

The Phase 1 audit correctly noted that listening decisions are currently buried in prose.

Create a durable review/decision record so accepted pronunciation decisions can be traced without re-listening to everything.

======================================================================
5. QA REPOSITORY VERSION CONTROL
======================================================================

The VO QA-repó folder was not a git repository during Phase 1.

At the START of Phase 2:

1. verify .gitignore excludes:
   - .env
   - secrets
   - cache
   - generated/private results that should not be committed

2. inspect for secrets before staging;

3. `git init`;

4. make a baseline commit of the current pre-Phase-2 tooling/config state.

Do NOT configure or push a remote repository unless I separately ask for that.

Never commit API keys or the restricted rights register.

======================================================================
6. COURSE-SIDE FIXES
======================================================================

Do NOT directly mix uncontrolled course edits into the QA-tooling pass.

Use the project's /course-fix workflow/skill for actual course-repository changes.

The course fix pack must include all course/doc changes implied by the approved decisions, including at minimum:

- remove stale “voices do not exist” claims;
- update v4 model/settings documentation;
- make the canonical dictionary workflow explicit;
- correct the pronunciation tables;
- implement the approved Leviatán spoken form while preserving written Leviatán;
- 112 → “száztizenkettő” VO rule;
- correct pause policy;
- correct emphasis policy;
- correct P-NAR authority;
- document canonical-narrator-voice-first / second-voice-later staged voice strategy;
- document first-pass M1.3 speaker strategy honestly;
- M4.1 narrator-quoted / silent-character decision;
- remove M5.3-NAR-01 and M7.1-NAR-02 optional narration;
- repair all affected timing windows;
- fix Z.1 timing;
- distinguish audio duration from thinking time;
- create M1.3 audio-description source;
- harmonise audio-only transcript requirements;
- resolve the stock-avatar / alternating-face contradiction;
- implement D9 transcript-first-line + lesson-footer placement;
- regenerate all derived media manifests/registers after source changes.

Preserve the course's existing decision history and IDs.

Do not renumber assets unnecessarily.

Do not move answer-key letters.

Do not silently change curriculum meaning just to make TTS easier.

======================================================================
7. LEGAL / DPO / MEMUNA HANDLING
======================================================================

Important:

My project-owner approval means:

“implement the recommended conservative course/production behavior.”

It does NOT authorize fabricating evidence that another role personally signed.

Therefore if a checklist specifically requires:

- legal approver;
- DPO;
- Memuna;
- accessibility reviewer;
- another named role;

and there is no actual evidence from that role:

leave the FORMAL EVIDENCE checkbox open.

But do NOT reopen the underlying project-owner content decision.

Use wording such as:

“implementation decision approved by project owner; formal role evidence pending”

where appropriate.

For the voice-use rights of the canonical narrator voice and the second voice specifically, the substantive fact supplied by me is:

- both voices exist;
- rights are clarified;
- explicit consent exists.

Record that without inventing additional unsupported personal details.

======================================================================
8. TIMING ACCEPTANCE
======================================================================

Recalculate timing after:

- extractor fixes;
- dictionary fixes;
- optional-narration removal;
- tts_text normalization.

No narration should require an absurd delivery rate to meet its declared window.

Specifically, do not leave anything equivalent to the previous M7.1 267 wpm situation.

For every changed timing item report:

- asset ID;
- word count;
- measured/rendered duration;
- previous window;
- new window;
- effective words/minute;
- reason for the change.

Build an automated timing regression check so future text edits cannot silently break the window.

======================================================================
9. PHASE 2 VALIDATION
======================================================================

Before declaring Phase 2 complete, run the complete relevant regression suite.

At minimum prove:

1. no meaningful bold-only narration content is dropped;
2. new canonical Somer spellings have dictionary coverage;
3. the coverage checker fails when a required rule is deliberately removed;
4. madrih/hanih still produce the B4-approved sounds;
5. Leviatán produces the approved B/“Leviatan” sound;
6. M2.A produces “em kettő pont á”;
7. 112 produces “száztizenkettő”;
8. display text and captions retain canonical spelling;
9. M5.3-NAR-01 and M7.1-NAR-02 are cleanly removed from VO production without breaking their visible information;
10. speaker segmentation exists for M1.3;
11. M4.1 has no accidental duplicate character/narrator speech;
12. timing validation has no unresolved impossible windows;
13. dictionary/version/model/settings are recorded reproducibly;
14. generated manifests show no unexplained drift;
15. course integrity and media regression tests remain green after /course-fix.

Do not weaken existing tests merely to make Phase 2 pass.

======================================================================
10. PHASE 2 OUTPUT
======================================================================

When finished, give me one final Phase 2 report containing:

A. exact QA_REPO changes;
B. exact course repo changes;
C. all D-01...D-23 resolutions as implemented;
D. any intentional deviations from the Phase 1 recommendation;
E. tests run + exact results;
F. before/after timing table for changed assets;
G. pronunciation regression results;
H. dictionary ID/version used;
I. production configuration of the canonical narrator voice;
J. what is now ready for full synthesis with the canonical narrator voice;
K. what remains a real release-evidence gate;
L. any item that genuinely still requires me to decide something.

Do not list an item as “open decision” merely because formal release evidence is still pending.

Distinguish:

DECISION
vs.
IMPLEMENTATION
vs.
FORMAL EVIDENCE
vs.
RUNTIME ACCEPTANCE.

Do not ask me again about any of the resolved D-01...D-23 items unless Phase 2 produces new evidence that directly contradicts the selected decision.

======================================================================
11. STOP CONDITION
======================================================================

Phase 2 is complete only when:

- the QA pipeline is fixed and reproducible;
- the canonical pronunciation layer matches the approved sounds;
- the course-side fix pack has been applied through /course-fix;
- relevant tests pass;
- timing is coherent;
- documentation matches actual v4 behavior;
- no stale “voices do not exist” or pre-migration pronunciation rule remains;
- no decision above is accidentally reopened;
- remaining blockers are honestly classified as runtime/evidence gates rather than unresolved owner decisions.

Then report the result.

RUN PHASE 2 NOW.

======================================================================
ADDENDUM — two further owner answers (2026-10-03, during Phase 2)
======================================================================

Asked in the session after the course fix pack was drafted (AskUserQuestion); answers verbatim:

1. Voice names in the public course repo.
   Question: the course repo is public and names the voice-source speakers only as VOICE-SRC-01/02
   (HUM-MEDIA-02); [a hangnevek és a forrás-beszélők viszonyáról szóló félmondat a nyilvános
   másolatból kihagyva]. What should the public course repo call the two voices?
   Answer: "Neutral roles (Recommended)" — in the course repo "kanonikus narrátorhang" and
   "második hang"; the voice names stay only in this private QA repo.

2. IMPL-34 (autoplay).
   Question: should narration/video ever autoplay?
   Answer: "No autoplay (Recommended)" — narration and video never start by themselves; the learner
   presses play (WCAG 2.2 SC 1.4.2, the H5P default). Added to the accessibility standard and the
   runtime acceptance test through the course fix pack.
