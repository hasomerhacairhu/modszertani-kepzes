---
name: course-fix
description: Validált findingok sebészi javítása a tananyagban. Csak bizonyított, objektív hibát javít, egyesével, minimális szerkesztéssel. Nem indít új auditot, nem commitol magától, emberi döntést igénylő kérdésnél megáll.
argument-hint: <finding-ID-k, vagy "az előző review P0-P1 findingjai", vagy konkrét fájl+probléma>
disable-model-invocation: true
---

# Validált findingok javítása

**Ez a skill nem auditál.** Nem keres új problémákat, nem olvas végig modulokat
„hátha". Csak azt javítja, ami már **validált findingként** a kezében van.

Bemenet: `$ARGUMENTS`

Elfogadható bemenet: egy korábbi `/course-review` validált findingjai, a felhasználó
explicit listája, vagy egy konkrét fájl + konkrétan megnevezett probléma.
Ha a bemenet „nézd át és javítsd, amit találsz" — **ez nem érvényes bemenet.**
Mondd meg, hogy előbb `/course-review` kell.

## Findingonként, egyesével — soha nem kötegelve

### 1. Kontextus
Olvasd be a fájlt a hely körül, és a hivatkozó helyeket is (modulhub, kapu-fájl,
`02 Tervezet/Program terv.md`, Study Lab zárómondat,
`02 Tervezet/LMS – activity manifest.md`).

### 2. Bizonyítsd a hibát **most**
Idézd a jelenlegi állapotot a fájlból. Ha nem egyezik a findinggel — a fájl közben
változott, vagy a finding téves —, **ne javíts.** Jelezd, és lépj a következőre.

### 3. Minimális szerkesztés
Egy `Edit`, a lehető legkisebb egyedi horgonnyal. **Soha ne generáld újra a fájlt**,
és ne írj át bekezdést, ha egy szó a hiba.

### 4. Olvasd vissza
A módosított helyet és a körülötte lévő 5–10 sort. Nézd meg, nem esett-e áldozatul
a `.claude/rules/hungarian-editorial.md` regressziós mintáinak (morfológia, névelő,
névmási referencia, elveszett minősítő).

### 5. Vidd végig a következményeket
Egy átnevezés soha nem elég önmagában — a hivatkozó helyek is változnak, vagy egyik sem.

### 6. Ellenőrizd
```bash
python3 tools/content_integrity.py
git diff --check
```

A sérthetetlen invariánsok kánoni listája: `.claude/rules/course-content.md`
(a `02 Tervezet/**` alatt automatikusan be is töltődik). Ne fejből dolgozz.

## Ahol MEGÁLLSZ, és nem javítasz

- **gyermekvédelmi, jogi, adatvédelmi, AI- vagy helyi someres bizonytalanság**:
  a `.claude/rules/safety-and-human-gates.md` szerint findingnál maradsz.
  Ne találj ki „ésszerű" szakpolitikai mondatot azért, hogy lezárd a tételt.
- **answer key, küszöb, ponthatár, rubrikaszint, szemantikus azonosító**: csak
  bizonyított objektív hibánál, a bizonyítékot a javítás mellé idézve.
- **tömeges átírás**: ha egy finding 20 helyet érintene, azt bontsd és kérj döntést.
- **ha nem érted, mit akart mondani az eredeti mondat**: nem írod át.

## A végén

1. Célzott újraellenőrzés: a módosított fájlra futtasd le **azt az egy specialistát**,
   amelyik a findingot adta. Ne a `verifier`-t — annak a szerződése szerint már meglévő
   findingokat vizsgál, javítás után pedig nincs mit. És **nem teljes új auditot.**
2. `/release-check`
3. Olvasd vissza a **teljes** `git diff`-et.
4. Jelentés: mit javítottál, mit hagytál ki és miért, mi vár emberi döntésre.

**Ez a skill nem commitol és nem pushol** — a commit/push szabály kánoni helye a
CLAUDE.md „Git-biztonság" szakasza.
