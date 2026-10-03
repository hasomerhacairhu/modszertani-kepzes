---
name: course-review
description: Tananyag read-only review-ja — modul, lecke vagy peula pedagógiai, értékelési, nyelvi, gyermekvédelmi/jogi és implementációs átvizsgálása specialista subagentekkel, adverzális ellenőrzéssel. Nem szerkeszt semmit, validált finding-listát ad.
argument-hint: <M3 | "02 Tervezet/.../fájl.md" | Z.4> [--lens pedagogy,assessment,language,safety,implementation|all]
disable-model-invocation: true
context: fork
agent: course-review-orchestrator
background: false
---

# Tananyag-review

Ez a skill egy külön, **read-only** subagentben fut (`course-review-orchestrator`: Read, Grep,
Glob, Agent — szerkesztő eszköze nincs, és csak az öt lencse-reviewert meg a `verifier`-t
indíthatja). A fő beszélgetés megvárja, és csak a riportot kapja meg. A kimenet egy validált
finding-lista, amiről **ember dönt**; a javítás külön skill (`/course-fix`, `/hungarian-edit`).

Scope és lencsék: `$ARGUMENTS`

## 1. Scope feloldása

- `M3` → `02 Tervezet/Modulok/M3/` teljes fája (hub, kapu, online leckék, peulák)
- `M4.A`, `Z.4`, `M7.1` → az adott azonosítójú fájl a modulon belül (Glob-bal keresd meg)
- útvonal → pontosan az a fájl vagy mappa
- ha nem egyértelmű: **ne találgass** — riport helyett add vissza, mit kell pontosítani.

## 2. Lencsék kiválasztása — ne indítsd el mindet

| Scope | Alapértelmezett lencsék |
|---|---|
| egyetlen lecke vagy peula | `pedagógia` + `nyelv` |
| teljes modul | `pedagógia` + `értékelés` + `implementáció` |
| `--lens <lista>` | pontosan a felsoroltak |
| `--lens all` / „teljes" | mind az öt |

**Plusz kötelező** a `biztonság-jog` lencse, ha a scope érinti az **M3**-at, az **M6**-ot, az
**M7 AI-leckéit**, vagy a `02 Tervezet/Adatvédelem – tanulói adatok és AI.md`,
`02 Tervezet/Gyermekvédelem – release gate.md`, `02 Tervezet/Emberi jóváhagyás szükséges.md`
fájlokat — illetve ha a Grep **szókezdetre illesztve** (csak bal oldali szóhatárral, mert a
toldalék jobbra hosszabbít) talál ilyet: `gyermekvédel`, `kiskorú`, `személyes adat`,
`adatvéd`, `jelzési kötelezettség`, `jelzőrendszer`, `hozzájárulás`, `feltárás`, `krízis`,
`önfeltár`; valamint az önálló `AI` szót **a `<!-- @asset … -->` blokkokon kívül** (az asset-
blokkok `"AI-generált"` provenance-jegyzete nem trigger).

> A puszta `adat` és `jelzés` **nem** trigger: magyarban a `feladat` és a `visszajelzés` is
> illeszkedne rájuk, és akkor a lencse minden fájlon elindulna.

Explicit `--lens` lista az erősebb: pontosan azt futtasd. Ha ezzel egy kötelező
`biztonság-jog` lencse kimarad, a riport **első pontjában** mondd ki („kötelező biztonsági
lencse kimaradt az explicit --lens miatt, mert …”). Bekapcsolt kötelező lencsénél is mondd ki,
miért kapcsolt be.

## 3. Kontextus

Csak amire tényleg szükség van: a scope-ba eső fájlok listája, a modulhub, és a releváns
kánoni dokumentum érintett szakasza. **Ne olvasd be a teljes korpuszt.**

## 4. Delegálás

| Lencse (`--lens` token) | Agent |
|---|---|
| pedagógia (`pedagogy`) | `pedagogy-reviewer` |
| értékelés (`assessment`) | `assessment-reviewer` |
| nyelv (`language`) | `hungarian-editorial-reviewer` |
| biztonság-jog (`safety`) | `safety-policy-reviewer` |
| implementáció (`implementation`) | `implementation-reviewer` |

Lencsénként egy hívás a scope fájllistájával; nagy modulnál lencsénként fájlcsoportokra bontva
(a csoportok minden kiválasztott lencsénél ugyanazok). Minden prompt tartalmazza:

- a konkrét fájlútvonalakat és a scope leírását;
- hogy a `.claude/finding-format.md` szerint válaszoljon, fájltartalmat ne adjon vissza;
- a **lezárt döntés** és a **bizonyíték-kapu** definícióját szó szerint a
  `.claude/rules/safety-and-human-gates.md` „Lezárt döntések” szakaszából (minden reviewer
  ugyanazt a szabályt kapja).

Ha egy reviewer a lépéskorlátja miatt részleges eredménnyel tér vissza, azt a lencsét a
riportban **hiányosként** jelöld.

## 5. Adverzális ellenőrzés

Az összes findingot **egyetlen** `verifier`-hívásnak add át, a teljes listával — a
duplikátumok épp a lencsék között keletkeznek. A promptban jelezd, hogy git-history nem áll
rendelkezésre (a „restauráció vagy baseline” kérdésre „baseline ismeretlen” a válasz, és a
súlyosság nem emelkedik). **Minden finding kapjon verdiktet**; egy sem eshet ki csendben.

## 6. Riport

Sorrend: `P0` → `P1` → `P2`, ezen belül lencse szerint. Alapértelmezett maximum:
**25 finding** teljes modulnál, **15** egyetlen fájlnál. Az `ELVETVE` verdiktűek közül a
**P0 és P1** súlyosságúakat akkor is sorold fel egy-egy sorban (ID + az elvetés oka); a
P2-esekből elég a darabszám.

1. **Scope és futtatott lencsék** — mit néztünk meg, mit nem, miért; kimaradt kötelező vagy
   hiányos lencse
2. **Validált findingok** (`objektív` típus) a `.claude/finding-format.md` mezőivel
3. **Emberi döntést igénylő tételek** külön blokkban — ezekre nincs javasolt szöveg
4. **Bizonyíték-kapuk** külön blokkban — szerep, G-kapu (`02 Tervezet/RELEASE-READINESS.md`)
   és a tracker-issue; ezek **nem** mennek `/course-fix`-be
5. **Cap miatt kihagyott és levágott findingok** (`LEVÁGVA: n …`) felsorolása
6. **Következő lépés** — melyik `objektív` findingra melyik skill (`/course-fix`,
   `/hungarian-edit`, új tartalomnál `/course-develop`)
