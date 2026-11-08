# Projektgazdai döntések – D-095, D-096, D-097: a vak tanulói tesztek javításai (2026-11-06 – 2026-11-08)

A projektgazda három üzenetének szó szerinti rögzítése és hatóköre. A builderben vezetett eredeti nyilvántartás:
`heymarcell/mk-coursebuild/docs/decisions/D-095.md`, `D-096.md`, `D-097.md`; a javítások indoklása:
`reports/2026-11-06-d095/` (`REPORT.md`, `ROUND3-DECISIONS.md`, `phase4d/ROUND4-QUEUE.md`, `round5/author-edits-*.md`,
`REVIEW-DRAFTS.md`). **Egyik döntés sem release-engedély.**

## A projektgazda szavai (szó szerint)

**D-095 (2026-11-06):**

> yes, you should fix all, even it is "not your job" you have to fix it in the cousese and képzés tananyag as well!

> please make sure everything is fixed, correct and perfect now

> i accept all your recommendations, and please do this process till you get everything perfect! You can change the
> course material, and you should when you find any issue, mistake error discrapancy. the whole course should be
> perfect regarding alignment, layout design pedagogy psychology etc!

**D-096 (2026-11-07):**

> i authorize you to decide anything you can based on you and your research recommendations btw!

**D-097 (2026-11-08):**

> 1. you have the dpo yes 2. i will send it sure 3. you can decide, i am the authro and you can commit merge push, i
> authorize 4. push everything yes and please fix all remaining issue and lets run an all around last round of
> vereification testing simulation

**D-090 (2026-10-24), a BSPEC-08-ra vonatkozó rész** (a builderben: `docs/decisions/D-090.md`):

> I approve the documented proposed BSPEC-08 through BSPEC-11 settings as owner direction, subject to the required
> assessment/LMS review, without assuming approval of M5.4 final-score visibility.

## Hatókör

- **D-095:** a vak tanulói és mentori tesztek (D-094c, Phase 4c, Phase 4d) minden findingját javítani kell, a tananyagban
  is: szöveg, sorrend, értékelés, pedagógia, elrendezés. A javítások a `fix/d095-learner-findings` ágon vannak.
- **D-096:** a projektgazdára tartozó döntéseket a kutatásra épülő ajánlás alapján a végrehajtó hozza meg, indoklással.
- **D-097:** a projektgazda a tananyag szerzője. A szerzői tételeket (a `REVIEW-DRAFTS.md` 3. szakasza és a
  `round5/author-edits-*.md` tervezetek) ezért a D-096 szerint dönti el a végrehajtó, és a szerző felhatalmazza a
  javítások commitolására, mergelésére és pusholására. A DPO-MENTOR-ACCESS kérdésben a projektgazda közölte a DPO igenjét
  az A2 megoldásra: külön kurzusszerep, amelyet csak csoportba sorolt mentor kap meg, a csoporttagsággal együtt.

## Ami nyitva marad (szerepköri QA / bizonyíték-kapu)

- A Memuna minden gyermekvédelmi tétele: a „Memuna átnézésére” jelölt tervezetek tervezetek maradnak; egyetlen
  gyermekvédelmi szabály tartalma sem változott.
- A DPO írásos bizonyítéka az A2-höz, és a DPO többi tétele (megőrzés, a TEXT-C végleges szövege).
- A szervezet, a hozzáférhetőségi gazda és az értékelési felelős tételei (pl. az M3 R3 116-111 pontszabálya, az M7 R5
  „Több, eltérő típusú” olvasata).
- `RUNTIME_VERIFIED`, `FINAL_RELEASE_QA` és `RELEASE_APPROVED` nem következik a döntésekből.
