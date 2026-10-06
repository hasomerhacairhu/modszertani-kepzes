# Projektgazdai döntés — az M6.4 elfogadása és a teljes Command 5 hatóköre (2026-10-05)

> **Audit trail.** Ez a jegyzőkönyv a projektgazda 2026-10-05-i üzenetét rögzíti, szó szerint; az üzenet az M6.4
> `/course-develop` köre után érkezett. A tartalmát a teljes Command 5 (`/course-fix`) vezeti át a kánonba. Ez a fájl
> csak döntési bizonyíték: javítás nem történt, commit nincs.
>
> **A döntés részei:**
> - Az M6.4 build-spec bemenetként elfogadva. Külön M6-kör nincs.
> - Az objektív pontok a teljes Command 5-be kerülnek:
>   - a C-VÁLASZTÓ nyelvi javítása;
>   - az M6 kapu 3. és 10. itemének konzisztencia-javítása, answer key-, küszöb- és rubrikaváltozás nélkül.
> - A Memuna-QA-pontok nyitva maradnak:
>   - a 6D és a ZÁRÓ ismétlése;
>   - a „nem játék” fordulat;
>   - a 6D Memuna-átnézése, amely learner-release / final-QA bizonyíték.
> - Megmarad a jóváhagyott időtartam.
> - A „Kb. 5 perc…” mondat nem kerül be.

## A projektgazda üzenete, szó szerint

```text
No new M6.4 round.

M6.4 is accepted as build-spec input.

Close the reviewer points as follows and fold the objective ones into the upcoming FULL BSPEC Command 5; do not create a separate M6 fix round:

- grammar: C-VÁLASZTÓ `egy fáradt, 13 éves kvucát` → `egy fáradt, 13 éves kvucával`.
- do NOT add the proposed “Kb. 5 perc…” sentence.
- keep the approved duration: 15–20 min base path; 20–25 min with optional C.
- the 6D/ZÁRÓ safeguarding repetition remains Memuna QA; do not change it now.
- the “nem játék” wording remains Memuna QA; do not change it now.
- 6D Memuna review remains learner-release/final-QA evidence, not a build blocker.

M6 gate item 3 and item 10 need an objective consistency fix in the SAME BSPEC run:
- C is now optional, so it cannot be the sole teaching source for a quiz item every learner receives.
- do NOT change either answer key.
- item 3: ground the feedback/reference in mandatory M6.1 + M6.3 content; M6.4 C may only be mentioned as an optional example.
- item 10: remove dependency on the C-only label “energiatakarékos üzemmód”; express the same correct principle directly as participation while seated / with fewer movements, preserving option A as correct and grounding the construct in the mandatory inclusivity/material already taught.
- no threshold, score or rubric change.

Now prepare the CURRENT-STATE full Command 5, using the already validated finding packs and decisions:

`2026-10-05 Validált findingok – MAN completion és mentor-láthatóság.md`
- IMPL-3
- IMPL-4
- IMPL-5
- IMPL-6
- IMPL-7
- IMPL-9

`2026-10-05 Validált findingok – M3.3 Branching Scenario-flow.md`
- M33-IMPL-1
- M33-IMPL-2
- M33-IMPL-3
- M33-IMPL-4
- M33-IMPL-7
- M33-IMPL-8
- SAFE-2
- SAFE-3
- SAFE-5

Apply the closed decisions:
- D-d
- D-e, including the now-implemented M6.4 topology
- D-f / BSPEC-07
- D-g option (a)
- D-h
- D-i
- D-j
- M33-IMPL-6
- SAFE-1
- SAFE-4
- §7.1
- §7.2

Required result of this one round:

BSPEC-05:
- deterministically resolve LMS-M2-04, LMS-M3-03, LMS-M5-02 and LMS-M6-04;
- runtime proof stays separate evidence and must not keep the spec row open;
- negative runtime failure later reopens it;
- no Group/manual workaround for scored Branching Scenario rows;
- attempts/report data is evidence only, never the unlock trigger;
- completion must not be weakened.

M3.3:
- pin the full SAFE-1 pass topology and SAFE-4 S1-K1 flow;
- pass is inside the same BS, not a fallback activity;
- each S1–S4 gets a pass-choice;
- no reason is requested for passing;
- pass and continue have equal scoring effect;
- every route reaches the appropriate safety node;
- all four scenario checkpoints are completed-or-passed before FINAL;
- all-wrong and all-pass routes both reach FINAL and produce non-empty grade;
- no learner-visible performance score;
- no early completion;
- no separate activity, Group, manual completion workaround or staff checkpoint;
- randomise off; explicit Navigate back;
- runtime negative tests recorded separately.

BSPEC-06:
- close the standard H5P completion/configuration rows across the full M0–Z scope according to the validated finding and existing canon.

BSPEC-07:
- pin Assignment SUBMITTED vs CONFIRMED as separate states;
- downstream unlock follows row-by-row canon;
- LMS-M7-07 opens from Peula v1 SUBMITTED, not mentor confirmation;
- mentor confirmation remains where canon requires confirmed completion;
- Z.3 remains mandatory/non-blocking as already decided; final module/course completion uses the separate mentor acceptance logic;
- no fake semantic automation.

BSPEC rows may become BUILD_SPEC_RESOLVED when the deterministic repository configuration is fully pinned.
Do not require target-Moodle runtime proof to close the repository spec.

Do not falsely close:
- target runtime evidence;
- Memuna/DPO/final QA;
- SAFE-7;
- A11Y-15/18 runtime/release evidence;
- cmids/build outputs.

Loop-break rule:
fix objective defects introduced by this Command 5 in the same run.
There is no Command-5 cleanup round unless an actually new owner/DPO/Memuna decision is required.

No review.
No new general audit.
No commit.
No push.

Return ONLY the exact final user-invoked `/course-fix` command for this full Command 5 and STOP.
```

## Kiegészítő projektgazdai safeguardok (2026-10-05, második üzenet), szó szerint

```text
További két kötelező safeguard:

(1) M6 kapu 3. és 10. item forrás-integritás:
ne állítsd, hogy az M6.1/M6.3 explicit tanít egy tesztelt elvet, ha a forrásszövegben az ténylegesen nincs benne. Ellenőrizd a kötelező forrásokat. Ha az item 3 vagy 10 helyes válaszához szükséges konkrét elv jelenleg csak az opcionális M6.4 C-ben szerepel, akkor ugyanebben a Command 5 futásban vezesd át a már meglévő elvet minimális learner-facing mondatként a legmegfelelőbb kötelező M6.1 vagy M6.3 forrásba, és utána erre hivatkozz. Új pedagógiai szabályt ne találj ki; csak a már meglévő M6.4-elvet tedd minden learner számára kötelezően elérhetővé. A ✅, item-szár, küszöb és pontozás ne változzon.

(2) M3.3 scoring stop-feltétel:
ha a választott Branching Scenario + Moodle konfiguráció repó-szinten nem specifikálható determinisztikusan úgy, hogy a csupa-rossz és a csupa-passz út is nem üres grade-et adjon, miközben a learner számára nincs teljesítménypontszám-jelentés, akkor NE gyengítsd egyik követelményt sem és NE jelöld a vonatkozó BSPEC-05 sort BUILD_SPEC_RESOLVED-nek. Állj meg az exact technikai blockerrel. Runtime-bizonyíték hiánya önmagában nem blocker; a determinisztikus konfiguráció hiánya igen.
```
