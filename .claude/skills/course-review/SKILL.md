---
name: course-review
description: Tananyag read-only review-ja — modul, lecke vagy peula pedagógiai, értékelési, nyelvi, gyermekvédelmi/jogi és implementációs átvizsgálása specialista subagentekkel, adverzális ellenőrzéssel. Nem szerkeszt semmit, validált finding-listát ad.
argument-hint: <M3 | "02 Tervezet/.../fájl.md" | Z.4> [--lens pedagogy,assessment,language,safety,implementation|all]
disable-model-invocation: true
disallowed-tools: Edit, Write, NotebookEdit, Bash
---

# Tananyag-review

**Ez a skill nem szerkeszt.** Az `Edit`, `Write` és `Bash` eszközök el vannak véve tőle
erre a körre. A kimenet egy validált finding-lista, amiről **ember dönt**.
A javítás külön skill: `/course-fix` vagy `/hungarian-edit`.

Scope és lencsék: `$ARGUMENTS`

## 1. Scope feloldása

- `M3` → `02 Tervezet/Modulok/M3/` teljes fája (hub, kapu, online leckék, peulák)
- `M4.A`, `Z.4`, `M7.1` → az adott azonosítójú fájl a modulon belül (Glob-bal keresd meg)
- útvonal → pontosan az a fájl vagy mappa
- ha nem egyértelmű: **kérdezz vissza**, ne találgass

## 2. Lencsék kiválasztása — ne indítsd el mindet

| Scope | Alapértelmezett lencsék |
|---|---|
| egyetlen lecke vagy peula | `pedagógia` + `nyelv` |
| teljes modul | `pedagógia` + `értékelés` + `implementáció` |
| `--lens <lista>` | pontosan a felsoroltak |
| `--lens all` / „teljes" | mind az öt |

**Plusz kötelező**: futtasd a `biztonság-jog` lencsét is, ha a scope érinti az **M3**-at,
az **M6**-ot, az **M7 AI-leckéit**, vagy a `02 Tervezet/Adatvédelem – tanulói adatok és AI.md`,
`02 Tervezet/Gyermekvédelem – release gate.md`, `02 Tervezet/Emberi jóváhagyás szükséges.md`
fájlokat — illetve ha a Grep **szóhatárra illesztve** talál ilyet: `gyermekvédel`, `kiskorú`,
`személyes adat`, `adatvéd`, `jelzési kötelezettség`, `jelzőrendszer`, `hozzájárulás`,
`feltárás`, `krízis`, `önfeltár`, `\bAI\b`.

> A puszta `adat` és `jelzés` **nem** trigger: magyarban a `feladat` és a `visszajelzés` is
> illeszkedne rájuk, és akkor a lencse minden fájlon elindulna — ami épp azt a szabályt
> ürítené ki, ami fölötte áll.

Ezt mondd is ki a riportban („biztonsági lencse bekapcsolva, mert …").

Ha csak nyelvi review-t kértek, **ne futtass pedagógiai vagy jogi auditot.**

## 3. Kontextus beolvasása (te, a fő contextben)

Csak amire tényleg szükség van: a scope-ba eső fájlok listája, a modulhub, és a
releváns kánoni dokumentum (`02 Tervezet/Program terv.md` érintett szakasza, a modul kapu-fájlja,
vagy a `Glosszárium`). **Ne olvasd be a teljes korpuszt.**

## 4. Delegálás

Minden kiválasztott lencsét egy-egy subagentnek adj át **egy üzenetben, párhuzamosan**:

| Lencse (`--lens` token) | Agent |
|---|---|
| pedagógia (`pedagogy`) | `pedagogy-reviewer` |
| értékelés (`assessment`) | `assessment-reviewer` |
| nyelv (`language`) | `hungarian-editorial-reviewer` |
| biztonság-jog (`safety`) | `safety-policy-reviewer` |
| implementáció (`implementation`) | `implementation-reviewer` |

**Kizárólag ez az öt agent + a `verifier` indítható.** `general-purpose` vagy bármely
más agent tiltott: azoknak `Edit`/`Write` eszközük van a `02 Tervezet/`-re. Ha egy
lencse nem képezhető le ezekre, **kérdezz vissza**, ne helyettesítsd.

A prompt tartalmazza: a konkrét fájlútvonalakat, a scope leírását, és hogy a
`.claude/finding-format.md` szerint válaszoljon. **Ne kérj tőlük fájltartalmat vissza.**

## 5. Adverzális ellenőrzés

Az összegyűjtött findingokat add át a `verifier` agentnek — egyetlen hívásban, a
teljes listával, hogy a duplikátumokat is lássa. Nagy lista esetén **lencsénként** bontsd,
ne fájlonként: a duplikátumok jellemzően lencsék között keletkeznek (ugyanaz a
terminológiai csúszás a `nyelv` és az `implementáció` lencsében). **Minden finding
kapjon verdiktet.** Egy finding sem eshet ki csendben: ha valami
kimarad a caps miatt, azt a riport végén **sorold fel** név szerint.

## 6. Riport

Sorrend: `P0` → `P1` → `P2`, ezen belül lencse szerint. Alapértelmezett maximum:
**25 finding** teljes modulnál, **15** egyetlen fájlnál. Az `ELVETVE` verdiktűek közül
a **P0 és P1** súlyosságúakat akkor is sorold fel egy-egy sorban (ID + az elvetés oka);
a P2-esekből elég a darabszám. Ha egy specialista `LEVÁGVA` sorral tért vissza, azt is
add tovább a 4. szakaszban.

A riport szerkezete:

1. **Scope és futtatott lencsék** — mit néztünk meg, mit nem, és miért
2. **Validált findingok** a `.claude/finding-format.md` mezőivel
3. **Emberi döntést igénylő tételek** külön blokkban — ezekre nincs javasolt szöveg
4. **Cap miatt kihagyott findingok** felsorolása, ha volt ilyen
4b. **Levágott findingok** — ha egy specialista elérte a saját capjét (`LEVÁGVA: n …`)
5. **Következő lépés** — melyik findingra melyik skill (`/course-fix`, `/hungarian-edit`,
   új tartalomnál `/course-develop`)
