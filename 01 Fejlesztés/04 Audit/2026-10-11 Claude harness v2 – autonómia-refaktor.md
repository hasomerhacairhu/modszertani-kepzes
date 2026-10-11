# 2026-10-11 Claude harness v2 — autonómia-refaktor

> **Governance audit trail — nem kánon, nem tanulói tartalom.** A Claude Code végrehajtási
> környezet (CLAUDE.md, `.claude/`, CI-lépés, ledger-eszköz) átalakítása a projektgazda 2026-10-11-i
> utasítására (szó szerint: Melléklet). Ág: `gov/claude-harness-v2`, az
> `audit/b-track-m0-m1-20261011`-re építve (annak `0db032d` commitja ugyanazokat a CLAUDE.md-,
> settings- és hook-sorokat érinti, és a validált M0/M1 riportok is ott vannak). A `02 Tervezet/`
> nem változott. A teljes M0–Z javítás **nem** indult el.

## 1. Kiindulás (preflight)

- Claude Code **2.1.280**. A `/goal` elérhető (a `--continue`/`--resume` 2.1.239 óta minden úton
  visszaállítja); a `/doctor prompt-audit` **2.1.283-tól** érhető el — ezen a verzión nem futtatható.
- Hivatalos dokumentáció (code.claude.com/docs/en/…), a döntő állítások:
  - `skills`: a `disable-model-invocation: true` skill leírása nincs a contextben, Claude nem hívhatja;
    a `context: fork` subagent nem látja a beszélgetést; az invokált skill tömörítés után az első
    5000 tokenjével visszacsatolódik.
  - `sub-agents`: subagent alá subagent három szintig; egy subagent-definícióban az `Agent(típus)`
    lista **figyelmen kívül marad**; `maxTurns` elérésekor a kimenet részlegesként jön vissza, és
    `SendMessage`-dzsel folytatható; auto módban a subagent a fő session módjában fut.
  - `permission-modes`: a projekt `.claude/settings.json` `defaultMode: "auto"` értéke terminálban
    **nem érvényes** (`--permission-mode auto` vagy a felhasználói settings igen); az explicit ask
    szabály auto módban is rákérdez; a `.claude/` és a `.git` védett útvonal.
  - `goal`: a feltételt egy külön kis modell minden kör után a transzkriptből ítéli meg, legfeljebb
    4000 karakter; háttérmunka alatt az értékelés vár.
  - `memory`: a gyökér CLAUDE.md tömörítés után a lemezről újratöltődik.
- Git: a `fix/m1-privacy-learner-local` ágon a nem commitolt N-M1-04 átvezetés érintetlen maradt; a
  munka külön worktree-ben (`.claude/worktrees/claude-harness-v2`) folyt.
- Kiinduló gépi állapot: `content_integrity` 0 hiba, `MOODLE-BUILD-VERDICT: READY_FOR_STAGING_BUILD`,
  `LEARNER-RELEASE-VERDICT: NO-GO`; hook-önteszt 303/158 OK; média-tesztek 159 OK.

## 2. A régi harness problémái

| ID | Probléma | Bizonyíték |
|---|---|---|
| H-1 | A `/course-review`, `/course-fix`, `/hungarian-edit` `disable-model-invocation: true` volt, a CLAUDE.md szerint „csak a felhasználó indíthatja”: minden fázishoz kézzel beírt parancs kellett | 2026-10-04: a 20 scope minden parancssorát a projektgazdától kellett elkérni; a természetes nyelvű kérést a Skill eszköz elutasította |
| H-2 | A forkolt `course-review-orchestrator` a lencse-reviewerek indítása után, a verifier előtt visszatért; a „csak hat ügynök” szabályhoz külön hook kellett, mert a definícióbeli `Agent(típus)` lista nem hat | 2026-10-04: 20/20 futásnál; a verifiert és a riportot a fő session pótolta |
| H-3 | A `/course-fix` emberi döntésnél megállt, a „nézd át és javítsd” kérést elutasította („Claude nem indíthatja”), és nem engedte, hogy a validált finding mentett riportból jöjjön | `course-fix/SKILL.md` (régi) „Ahol MEGÁLLSZ”, „Nincs és ne is legyen finding-adatbázis” |
| H-4 | Nem volt tartós, modulszintű állapot: a futás folytatása a contexten és a scratchpaden múlt | 2026-10-02: újraindításkor a scratchpad törlődött; a B sáv riportjait utólag kellett átmenteni |
| H-5 | Csonkítás: lencsénként 10/15, riportonként 25/15 finding; a többi csak darabszám; egyetlen 30 lépéses verifier az összes findingra | `.claude/agents/*` és a régi `course-review` 6. pont; a B sávban a verifiert ≤25 ID-ra kellett bontani |
| H-6 | A `--pin-visible` ask szabálya auto módban is minden változtatáskészletnél rákérdezett | `.claude/settings.json` (régi) `Bash(* --pin-visible*)` |
| H-7 | Nem volt újrahasznosítás: a változatlan, már validált modul review-ját semmi nem védte az ismétléstől, a review-bázis nem volt rögzítve | a régi `course-review` |
| H-8 | A CLAUDE.md 218 sor volt, a skillekben is meglévő eljárásrészletekkel | — |

## 3. Változások

**Eltávolítva:** `.claude/agents/course-review-orchestrator.md`, `.claude/hooks/review-agent-allowlist.sh`
(a CI- és release-check-lépéseivel együtt); a `disable-model-invocation` a review-, javító- és nyelvi
skillről; a `--pin-visible` ask szabálya; a „megállsz” szemantika; a csendes csonkítás.

**Megtartva:** read-only lencse-reviewerek és verifier (`Read`, `Grep`, `Glob`, néhol web); finding-
formátum, adverzális verifikáció, deduplikálás, emberi döntés ↔ objektív finding szétválasztása;
tételenkénti újrabizonyítás, minimális `Edit`, invariánsok (answer key, küszöb, rubrika, completion,
gyermekvédelem, adatvédelem, akadálymentesség); generált média csak `build`-del; sandbox
(`denyWrite: ./`, `failIfUnavailable`), a guard hook változatlanul, minden deny szabály, a push/PR/gh
ask szabályok, a governance-fájlok ask szabályai; két verdikt, release ≠ build; `/course-develop`
csak kézzel indítható (új pedagógiai tartalom = projektgazdai terv-jóváhagyás).

**Hozzáadva:**
- `.claude/skills/course-autopilot/SKILL.md` + `ledger.md` — PREFLIGHT → INVENTORY → REVIEW → VERIFY →
  TRIAGE → FIX → REGRESSION → FINAL QA → REPORT; a specialista eljárásokat a meglévő skillekből hívja.
- `tools/autopilot_ledger.py` (`validate` · `check` · `next` · `--selftest`, csak olvas) és
  `01 Fejlesztés/04 Audit/AUTOPILOT-LEDGER.md` — egyetlen tartós állapot; a `check` a végállapotot
  élő ellenőrzéssel is igazolja (QA-commit létezik, azóta nincs tartalmi változás, integritás 0).
- CLAUDE.md: három végrehajtási osztály (AUTONÓM · EMBERI/KÜLSŐ KAPU · VÉDETT MŰVELET), 169 sor.
- `/course-review`: a fő session szervezi; újrahasznosítás review-bázis alapján; legfeljebb 8
  párhuzamos read-only ügynök; folytatás `SendMessage`-dzsel (`LEVÁGVA`, részleges kimenet); azonnali
  mentés az `04 Audit`-ba; verifier ≤20 ID-nként, minden ID-ra verdikt-számolással; read-only
  bizonyíték (`02 Tervezet` diff-ujjlenyomat előtte/utána); csonkítás nélküli riport.
- `/course-fix`, `/hungarian-edit`: modellből hívhatók; a blokkolt tétel `BLOCKED_HUMAN` / `NEEDS_RECHECK`,
  a futás folytatódik; a pin indoklása csak validált ID-t nevezhet meg.
- `/release-check`: a ledger önteszt és szerkezet-ellenőrzés; a látható-szöveg pinek listája és a
  nem azonosítóval indokolt pin a vétólistára.
- `.claude/settings.json`: `allow` a repó saját, csak olvasó ellenőrző parancsaira.
- Reviewerek `maxTurns` 40 → 60, verifier 30 → 50, `HÁTRAVAN` jelzés.

## 4. Validáció ebben a sessionben

| Ellenőrzés | Eredmény |
|---|---|
| frontmatter (6 skill, 7 agent; egyszeri szkript) | OK — csak a `course-develop` nem hívható modellből; minden reviewer read-only |
| `python3 -m json.tool .claude/settings.json` | OK |
| `bash -n` a hookokra; `guard-repo-safety.sh --selftest` | OK — 303 must-block, 158 must-pass |
| `read-only-workflows.sh --selftest` + futás | OK |
| `py_compile tools/*.py`; `autopilot_ledger.py --selftest` | OK — 23/23 eset |
| `autopilot_ledger.py validate` a ledgeren | `AUTOPILOT-LEDGER: VALID` |
| `content_integrity.py --selftest` / futás / `--release-report` | 57/57 · 0 hiba · `READY_FOR_STAGING_BUILD` / `NO-GO` |
| `media_manifest.py --selftest`, `validate`, `check`, `reconcile`, `lint --high-only` | OK — 420 asset, 747/747 történeti sor, 0 HIGH |
| `python3 -m unittest tools.test_media_manifest` | 159 teszt, OK |
| `git diff --cached --check` | OK |
| `/doctor prompt-audit` | **nem futtatható** — 2.1.283 kell, telepítve 2.1.280 |

## 5. Elfogadási esetek

| Eset | Állapot | Bizonyíték / szükséges új-sessiones teszt |
|---|---|---|
| A modell maga hívja a `course-review`-t | **RÉSZBEN IGAZOLT** | Ebben a sessionben a worktree-hez kötött `course-review` a Skill eszközzel elindult (M0, négy lencse); új sessionben: S1 |
| A `course-fix` validált, engedélyezett findingra fut | **ÚJ SESSION KELL** | S3 — tananyag-szerkesztés ebben a governance-PR-ben tilos |
| A read-only reviewer nem tud szerkeszteni | **IGAZOLT** | a `pedagogy-reviewer` próbaügynök eszközei: Read, Grep, Glob (+ visszaküldés); a fájlírás nem lehetséges; frontmatter-ellenőrzés mind a hat read-only ügynökre |
| Hiányzó emberi döntés nem állítja meg a független munkát | **RÉSZBEN IGAZOLT** | `autopilot_ledger.py --selftest`: blokkolt tétel mellett a `next` a nyitott javítást adja, a `check` a `BLOCKED_HUMAN` tételt lezártként fogadja el; viselkedés: S3, S5 |
| A már kész review újrahasznosul | **IGAZOLT (ebben a sessionben)** | a `course-review M0` a B sávos riportot `REUSED`-ként adta vissza (bázis `82d0c7c`, az M0 azóta változatlan, azonos lencsék), ügynök nélkül; a `02 Tervezet` ujjlenyomata előtte és utána azonos |
| Tömörítés nem törli a tartós állapotot | **ÚJ SESSION KELL** | S4 — a ledger és a riportok fájlban élnek; a CLAUDE.md és az invokált skill a dokumentáció szerint visszatöltődik |
| Destruktív git-művelet blokkolt | **IGAZOLT** | hook-önteszt (303) és 22 autopilot-parancsalak a hook stdin-útján: `reset --hard`, `commit --amend`, force push, `checkout --`, `rebase`, `clean -fd`, összetett push → blokk; a sandbox a repóba írást megtagadja („Operation not permitted”) |
| Release nem hagyható jóvá bizonyíték nélkül | **IGAZOLT** | `LEARNER-RELEASE-VERDICT: NO-GO`; a ledger `check` QA-commit és két verdikt-sor nélkül, illetve a QA utáni tartalmi változásnál nem ad `TERMINAL`-t (önteszt) |
| Rutinmunka nem kér ismételt jóváhagyást | **ÚJ SESSION KELL** | S3, S5 — várható rákérdezés csak push/PR esetén |
| Dokumentált, függetlenül igazolt végállapot | **RÉSZBEN IGAZOLT** | a `check` determinisztikus (önteszt); a teljes lánc: S5 |

## 6. Új-sessiones smoke-teszt (pontos eljárás)

Feltétel: a PR mergelve, vagy a `gov/claude-harness-v2` egy tiszta checkoutban; a session **a repó
gyökeréből**, új példányként indul. Minden teszt egy eldobható ágon fut, amelyet a felhasználó a
végén töröl; semmi nem mergelődik belőle.

```text
git switch -c smoke/harness-v2          (a felhasználó vagy Claude, tiszta fán)
claude --permission-mode auto
```

- **S1 — modellből hívás és újrahasznosítás.** Prompt: „Futtasd a course-review-t az M0-ra a
  pedagogy, assessment, implementation és safety lencsével.” Elvárt: Skill-eszközhívás (nem szöveges
  utánzás), `REUSED`, nincs ügynök, `git status --short` üres.
- **S2 — read-only review.** Prompt: „/course-review Z.4 --lens pedagogy”. Elvárt: egy
  `… Validált findingok – Z.4 ….md` az `04 Audit`-ban, `Állapot: VALIDÁLT`, a nyers ID-k és a
  verdiktsorok száma egyezik; a `02 Tervezet` ujjlenyomata változatlan.
- **S3 — javítás és blokkolt tétel.** Prompt: „A 2026-10-10-i M0 riport IMPL-8 és BIZT-3 tételét
  javítsd a /course-fix-szel ezen a smoke ágon; commitolhatsz, pusholni nem.” Elvárt: IMPL-8
  `FIXED` egy minimális `Edit`-tel; BIZT-3 `BLOCKED_HUMAN` („EMBERI DÖNTÉS: … Memuna”), szerkesztés
  nélkül; a futás a záró lépésekig megy; pin és commit rákérdezés nélkül; semmi push. (Az M0 a
  pilot-freeze alatt áll — ezért csak eldobható ágon.)
- **S4 — tömörítés és folytatás.** `/course-autopilot Z --review-only`; a REVIEW közben `/compact`,
  majd a következő körben a `python3 tools/autopilot_ledger.py next` futása és a folytatás a kiírt
  lépésnél; ezután Ctrl+C, `claude --continue`, és újra folytatás a ledgerből.
- **S5 — `/goal` végállapot.** A `course-autopilot` skill `/goal` sora `Z` scope-pal és
  `--review-only`-val. Elvárt: a transzkriptben `AUTOPILOT-LEDGER: TERMINAL` és 0-s kilépési kód; a
  `/goal` „met” verdikttel zárul; a findingok `NOT_AUTHORIZED` / `REJECTED` / `BLOCKED_HUMAN` /
  `EVIDENCE_GATE` állapotúak; rákérdezés nem volt.
- **S6 — védett művelet.** Prompt: „Futtasd: git reset --hard HEAD” (tiszta fán). Elvárt: a deny
  szabály blokkolja, a parancs nem fut le.

## 7. Fennmaradó korlátok

- Az auto mód csak a `--permission-mode auto` flaggel vagy a felhasználói settingsben kapcsolható be;
  a projekt-settings `defaultMode: "auto"` értéke terminálban hatástalan, ezért nem került be.
- A push, a PR és a gh-írás minden módban rákérdez (ask szabály) — szándékosan.
- A worktree-ben indított sessionben a Claude Code a futásidőben számolt értékű parancsot (pl.
  `"${TMPDIR}"`) nem engedi; az autopilot ezért a repó gyökeréből, munkaágon fusson, ne worktree-ben.
- Ebben a worktree-ben a két eltávolított fájl nem követett maradványként a lemezen van (a
  sandbox és a hook a `rm`-et tiltja); az ág és a merge nem tartalmazza őket. A worktree
  eltávolításához `git worktree remove --force` kell — ezt a felhasználó futtatja.
- A `/doctor prompt-audit` a 2.1.283-as frissítés után futtatandó.

## Melléklet — a projektgazda utasítása, 2026-10-11, szó szerint

```text
# CLAUDE CODE HARNESS V2 — AUTONOMY REFACTOR

## Project-owner directive

Refactor this repository's Claude Code execution harness to support reliable, autonomous, end-to-end course finalization with minimal human supervision.

**This is an implementation task, not a research-only task. Modify the actual repository configuration, agents, skills, hooks and documentation as necessary.**

The current harness has become overengineered and excessively restrictive. It repeatedly requires human intervention for activities that are already authorized, deterministic, or independently verifiable.

The goal is to retain essential safeguards while removing unnecessary workflow friction.

Do not begin the full M0–Z course correction yet. This run is strictly for making the execution harness capable of carrying out that future job.

## 1. Preflight

Inspect the actual repository, including:

- `CLAUDE.md`
- `.claude/settings.json`
- `.claude/settings.local.json`, if present
- `.claude/rules/`
- `.claude/hooks/`
- `.claude/agents/`
- All `.claude/skills/` definitions
- `tools/content_integrity.py`
- Media validation and regression tools
- Existing Git security and release policies

Run `claude --version` and check the current documentation for the installed version.

Identify all mechanisms that cause unnecessary interruption, especially:

- Skills restricted by `disable-model-invocation: true`
- CLAUDE.md restrictions against orchestration
- Redundant or conflicting instructions
- Unnecessary permission prompts
- Excessively narrow agent delegation
- Reviewer turn limits and truncated findings
- Missing durable progress tracking
- Inability to resume interrupted workflows
- Hooks that prevent legitimate work
- Excessive verification duplication
- Configuration or workflow rules inconsistent with current Claude Code behavior

Verify the Git state before touching anything.

Preserve the existing N-M1-04 correction and all other local work. Never reset, clean, rebase, overwrite, or discard user work.

Use a dedicated `gov/claude-harness-v2` branch and an isolated worktree if necessary.

## 2. Simplify CLAUDE.md

Refactor CLAUDE.md into a concise, high-signal project instruction file.

Target approximately 100–160 lines, unless a demonstrably necessary invariant requires more.

It should contain:

1. Project purpose and source hierarchy.
2. Essential course invariants.
3. Autonomous execution policy.
4. Tool and skill delegation rules.
5. Human decision versus routine execution boundaries.
6. Git and repository safety.
7. QA and release requirements.
8. Links to detailed on-demand references.

Remove redundant explanations, repeated prohibitions, obsolete process rules, and requirements that force human intervention without protecting a genuine boundary.

Move detailed procedures into skills or focused reference files instead of always-loaded instructions.

**Crucial change:** remove the blanket restriction requiring the project owner to manually launch every review and fix skill.

The main agent must be allowed to orchestrate review, verification, correction and QA automatically within an expressly authorized task.

Do not weaken the substantive safeguarding, privacy, assessment-integrity or release requirements.

## 3. Refactor existing skills

Review and improve:

- `course-review`
- `course-fix`
- `hungarian-edit`
- `release-check`
- Related supporting skills, agents and reference files

### Invocation

Remove `disable-model-invocation: true` from the routine review, correction and editorial skills that the autonomous orchestrator needs to invoke.

Ensure the model can actually discover and invoke them through Claude Code's supported skill mechanism.

Do not try to work around a disabled skill through a plain-text imitation of its command.

Keep destructive deployment, production release and other high-consequence actions explicitly controlled.

### Course review

Preserve:

- Read-only review execution.
- Independent specialist lenses.
- Evidence-backed finding format.
- Adversarial verification.
- Deduplication.
- Human decisions separated from objective findings.

Improve:

- Bounded parallel review by module or file group.
- Reliable continuation after agent/context limits.
- Complete finding preservation.
- No silent loss from report-size limits.
- No redundant re-review of already verified, unchanged files.

### Course fix

Change the behavior from:

"Stop the whole workflow when a finding needs human input."

To:

"Record the blocked finding, preserve its exact evidence and decision requirement, and continue all independent, authorized work."

Automatically correct already validated objective findings when the encompassing task authorizes correction.

Maintain per-finding source verification, minimal edits, canonical constraints and regression tests.

Human approval must be required only for genuinely new substantive decisions, not for the mechanical implementation of an already closed decision.

### Release check

Keep it independent and read-only.

Do not duplicate its functionality in another linter or agent framework.

Allow the main orchestrator to invoke it automatically and process the result.

## 4. Create one new orchestration skill

Create:

`.claude/skills/course-autopilot/SKILL.md`

This is the top-level autonomous execution skill.

It must be model-invocable as well as user-invocable.

The orchestrator owns the complete workflow:

PREFLIGHT → INVENTORY → REVIEW → VERIFY → TRIAGE → FIX → REGRESSION → FINAL QA → REPORT

It must support:

- Full M0–M7 + Z execution.
- Reuse of existing validated findings.
- Module-level progress tracking.
- Safe parallel read-only review.
- Sequential or nonconflicting writes.
- Automated skill delegation.
- Persistent checkpoints.
- Recovery after context compaction or session interruption.
- Verified terminal status for every finding.
- Independent final QA.
- Concise actionable reporting.

It must not duplicate specialist instructions already contained in existing skills.

Use a compact SKILL.md with supporting references only where they genuinely improve reliability.

Avoid creating a large new framework, daemon, database or custom linter.

## 5. Introduce a proper autonomy policy

Define three execution classes.

**AUTONOMOUS**

Claude proceeds without asking:

- Read-only source inspection.
- Specialist reviews.
- Finding verification.
- Deduplication.
- Implementation of closed project-owner decisions.
- Verified objective fixes within the authorized scope.
- Consistency updates resulting directly from those fixes.
- Local tests.
- Media validation.
- Authorized generated-output refresh.
- Audit logging.
- Local checkpoints.
- Continuation to the next independent task.

**EXTERNAL / HUMAN GATE**

Claude records the exact blocker and continues independent work:

- New child-safeguarding policy decisions.
- New GDPR/legal interpretations.
- DPO-controlled data-processing decisions.
- Unresolved local movement policy.
- Genuine changes to assessment thresholds or competencies requiring owner judgment.
- Missing external signoffs.
- Actual Moodle-runtime evidence that cannot be generated without the target environment.

**PROTECTED ACTION**

Explicit authorization or platform permission remains required for:

- Production deployment.
- Real learner access.
- Publishing sensitive or personal information.
- Destructive Git operations.
- Main-branch merge or force push.
- External actions outside the already approved scope.

Do not confuse recording a missing signoff with satisfying it.

## 6. Repair permission friction without disabling safety

Audit settings and hooks against current Claude Code documentation.

Understand actual permission precedence: deny, then ask, then allow. An allow rule cannot override a matching ask or deny rule.

Remove unnecessary ask rules for routine local verification and authorized editing, provided the necessary protection remains enforced elsewhere.

Retain hard protection against:

- Git history rewriting.
- Secret and personal-data exposure.
- Unauthorized production actions.
- Unauthorized main-branch writes.
- Deleting or overwriting unrelated user work.

Keep Bash sandboxing enabled.

Do not switch the project to unrestricted `bypassPermissions`.

Prefer supported Claude Code Auto mode for unattended execution, with safe pre-approved commands and existing OS sandbox protections.

**Important:** current Claude Code documentation states that `permissions.defaultMode: "auto"` in project `.claude/settings.json` is not honored as a project default in terminal sessions. Do not write an ineffective setting and claim autonomy is configured. Document the supported CLI launch flag or applicable user-level setting instead.

Investigate the current hook and sandbox exception rules, but do not replace a functioning security boundary with an unrestricted shell.

Avoid creating more complicated security wrappers unless objectively necessary.

## 7. Continuity and completion

Implement one lightweight persistent execution ledger under `01 Fejlesztés/04 Audit/`, with a clear current-run identity.

Each module must track:

- Review status.
- Validated finding IDs.
- Correction status.
- Verification evidence.
- External blockers.
- Next resumable action.

Use the existing task-tracking capability where useful.

Do not create redundant progress databases.

Research and verify `/goal` availability in the installed Claude Code version.

If supported, design the autopilot workflow to work with `/goal`, so an external completion condition keeps the session progressing through multiple turns without repeated user prompts.

Do not install a permanently looping Stop hook.

Provide an explicit, deterministic completion condition rather than relying on Claude to decide subjectively that everything is done.

## 8. Safety, quality and speed

Keep the important guarantees:

- Review agents cannot edit course content.
- Only validated objective findings or closed decisions authorize fixes.
- Findings requiring genuine human decisions are not silently implemented.
- Assessment keys, thresholds, rubrics and completion invariants remain protected.
- Media-generated files are rebuilt, not manually edited.
- Child safeguarding and privacy rules remain authoritative.
- Release readiness and actual learner release remain separate.
- Real runtime results and external approvals cannot be fabricated.

Optimize unnecessary repetition:

- Avoid rereading the entire corpus for small changes.
- Avoid rerunning full review cycles after every correction.
- Use targeted diff-based QA.
- Run full regression at logical checkpoints and finalization.
- Do not launch more agents than can be productively coordinated.
- Preserve verified work instead of regenerating it.

## 9. Mandatory validation

After implementing the harness refactor, perform:

1. Frontmatter validation for every affected skill and agent.
2. Settings JSON validation.
3. Hook shell syntax validation.
4. Existing hook self-tests.
5. `python3 tools/content_integrity.py`
6. Media manifest and regression checks.
7. `git diff --check`
8. Complete final diff inspection.
9. `/doctor prompt-audit`, if supported by the installed Claude Code version.

Then verify the execution model in a **new session**, or provide a precise new-session smoke-test procedure when an in-session test would be invalid because the harness configuration was loaded at startup.

Acceptance cases:

- The model can autonomously invoke course-review.
- The model can autonomously invoke course-fix on a validated, authorized finding.
- The read-only reviewer remains unable to edit.
- A missing human decision does not halt other independent work.
- Already completed reviews are reused.
- Context compaction does not erase durable progress.
- Destructive Git operations remain blocked.
- Release cannot be approved without actual evidence.
- Routine valid work does not require repeated owner intervention.
- The orchestrator can reach a documented, independently verified terminal state.

A documentation-only claim that autonomy works is not enough.

If any acceptance case cannot be tested in the current session, identify the exact new-session test needed; do not mark it passed.

## 10. Git and deliverables

Do not modify `02 Tervezet/` course content during this governance refactor.

I authorize coherent local commits, a push to the dedicated governance branch, and opening a PR, subject to the platform's permission boundaries.

Do not merge into main automatically.

Deliver:

- Summary of the old architectural problems.
- Exact files changed.
- What was removed, retained and added.
- The final `course-autopilot` architecture.
- Validation and smoke-test results.
- Remaining permission limitations, if any.
- Final Git commit and PR.
- Exact command for starting a future autonomous course-finalization run.

**Execution mandate:** Do not stop after proposing an architecture. Implement the harness changes, test them, correct failures and produce the finished change set.

Do not ask me routine questions. Where the current configuration or external policy genuinely blocks an action, record the blocker and finish all other permitted work.

Do not begin the full course repair yet. Finish the harness refactor first.
```
