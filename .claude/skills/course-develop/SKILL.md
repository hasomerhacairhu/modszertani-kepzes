---
name: course-develop
description: Új lecke vagy peula tervezése és megírása, illetve meglévő jelentős továbbfejlesztése — céltól az értékelésen át az implementációig, kötelező review-kapukkal. Ez az egyetlen skill, amely szándékosan hoz létre új pedagógiai tartalmat.
argument-hint: <mi készüljön, pl. "M5 új online lecke a konfliktuskezelésről" vagy "M2.B peula újratervezése">
disable-model-invocation: true
---

# Lecke- és peulafejlesztés

Ez az **egyetlen** skill, amely szándékosan hozhat létre új pedagógiai tartalmat.
Cserébe a legszigorúbb kapui vannak: **Claude megírta ≠ kész.**

Feladat: `$ARGUMENTS`

## A. Tervezés — írás előtt, a felhasználóval egyeztetve

1. **Kontextus**: olvasd be a `02 Tervezet/Program terv.md` érintett szakaszát, a modulhubot,
   a modul kapu-fájlját és a `Glosszárium` releváns tételeit. Nézd meg a szomszédos
   leckéket — formátumban és hangnemben illeszkedni kell.
2. **Célcsoport**: 15+ korosztály, a madrichok maguk is lehetnek kiskorúak.
3. **Prerekvizit**: mit tud már a tanuló, és honnan. Nevezd meg a forrásmodult.
4. **Tanulási cél**: kevés, mérhető, egy célt mondó.
5. **Konstruktív illeszkedés**: cél → tevékenység → értékelés egy tengelyen.
6. **Élmény és tevékenység**: mi történik ténylegesen; modalitás; miért ez a forma.
7. **Gyakorlás**: van-e próba a mérés előtt, és kap-e rá visszajelzést.
8. **Értékelés**: item vagy rubrika, answer key, küszöb — indokolva.
9. **Ív és terhelés**: hány új fogalom, mennyi idő, hol a szünet. Az időbecslés
   a leírt lépésekből jöjjön ki, ne kerekítésből.
10. **Akadálymentesítés**: `02 Tervezet/LMS – hozzáférhetőségi sztenderd.md` szerint.
11. **Gyermekvédelem és adatvédelem**: milyen adat keletkezik; kell-e nem-AI alternatíva;
    van-e önfeltárási kényszer; `.claude/rules/safety-and-human-gates.md`.
12. **Implementáció**: Moodle-aktivitás és H5P-típus, ami **tényleg létezik és tud** annyit;
    egyeztetve a `02 Tervezet/LMS – activity manifest.md` és
    `02 Tervezet/LMS – H5P runtime acceptance.md` fájlokkal.

**A pedagógiai design a te dolgod. A szervezeti, jogi, gyermekvédelmi és helyi someres
döntés nem.** Ez utóbbit ne találd ki: jelöld `KITÖLTENDŐ`-vel vagy explicit
`EMBERI DÖNTÉS` megjegyzéssel, és vedd fel a riportba.

Mutasd meg a tervet, mielőtt írsz. Ha a felhasználó jóváhagyta, folytasd.

## B. Megírás

Írd meg a fájlt a szomszédos leckék szerkezetét és hangnemét követve, a
`.claude/rules/course-content.md` és `.claude/rules/hungarian-editorial.md` szerint.
Új fájlnál: a fájlnév konvenció szerinti, a hivatkozásokat **fel is kell venni** a
modulhubba és ahol a program szintjén szerepelnie kell.

## C. Definition of done — ezek nélkül nincs kész

1. `pedagogy-reviewer` az elkészült fájlra
2. `hungarian-editorial-reviewer` az elkészült fájlra
3. `assessment-reviewer`, ha van benne kvíz, rubrika vagy kapu
4. `safety-policy-reviewer`, ha kiskorúakat, adatot, AI-t vagy érzékeny témát érint
5. `implementation-reviewer` a Moodle/H5P/akadálymentesítési részre
6. `verifier` az összegyűlt findingokra
7. a megerősített findingok javítása
8. `/release-check`
9. a **teljes** `git diff` visszaolvasása

A riportban sorold fel, melyik kapu futott le, és mi az eredménye. Ha egy kapu kimaradt,
**mondd ki** — ne jelentsd késznek.

**Ez a skill nem commitol és nem pushol** — a commit/push szabály kánoni helye a
CLAUDE.md „Git-biztonság" szakasza.
