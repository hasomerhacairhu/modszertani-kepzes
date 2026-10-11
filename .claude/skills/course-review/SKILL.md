---
name: course-review
description: Read-only tananyag-review — modul, lecke vagy peula pedagógiai, értékelési, nyelvi, gyermekvédelmi/jogi és implementációs átvizsgálása read-only specialista ügynökökkel, adverzális verifikációval és deduplikálással; a validált riportot a nyers findingokkal és minden verdikttel együtt az 01 Fejlesztés/04 Audit/ mappába menti. Tananyagot nem szerkeszt. Használd review-, audit- vagy „nézd át” kérésre, és a /course-autopilot REVIEW fázisában.
argument-hint: <M3 | "02 Tervezet/.../fájl.md" | Z.4> [--lens pedagogy,assessment,language,safety,implementation|all] [--run <Run-ID>]
---

# Tananyag-review

A review **read-only**: ebben a skillben a `02 Tervezet/` alatt semmit nem szerkesztesz. A
vizsgálatot read-only ügynökök végzik (`Read`, `Grep`, `Glob`, néhol web — szerkesztő eszközük
nincs); te a fő sessionben szervezed, és csak az `01 Fejlesztés/04 Audit/` alá írsz. A kimenet egy
validált finding-riport; a javítás külön fázis (`/course-fix`, `/hungarian-edit`).

Scope és lencsék: `$ARGUMENTS`

## 0. Read-only bizonyíték

Az elején és a mentés előtt ugyanaz a két érték kell:
`git diff HEAD -- "02 Tervezet" | shasum` és `git ls-files --others --exclude-standard -- "02 Tervezet" | shasum`.
Eltérésnél a review érvénytelen; a riport első sora ezt mondja ki.

## 1. Scope

- `M3` → `02 Tervezet/Modulok/M3/` teljes fája (hub, kapu, online leckék, peulák)
- `M4.A`, `Z.4`, `M7.1` → az adott azonosítójú fájl a modulon belül (Glob)
- útvonal → pontosan az a fájl vagy mappa
- nem egyértelmű → nem találgatsz: a riport helyén a pontosítandó kérdés; autopilotban a modul
  `PRECONDITION`-kaput kap, és a futás a többi modullal folytatódik.

## 2. Újrahasznosítás — ne vizsgáld újra, ami validált és nem változott

Keresd meg a scope legutóbbi validált riportját az `04 Audit`-ban és a review-bázisát.
- A scope fájljai a bázis óta nem változtak (`git diff --quiet <bázis> HEAD -- <fájlok>`, nem
  commitolt változás sincs), és a kért lencsék lefutottak → nem indítasz ügynököt: a riportot adod
  vissza (`REUSED`).
- Csak egyes fájlok változtak → csak azokra futtatod a lencséket; a régi riport többi findingja
  érvényes, a változott fájlokéi `NEEDS_RECHECK`.
- Egy kért lencse hiányzott → csak azt a lencsét futtatod.
- Egy `NEEDS_RECHECK` tétel újraellenőrzése: a tétel lencséjének reviewere csak arra a helyre, a
  jelenlegi szöveggel, és a verifier.

## 3. Lencsék

| Scope | Alapértelmezett lencsék |
|---|---|
| egyetlen lecke vagy peula | `pedagógia` + `nyelv` |
| teljes modul | `pedagógia` + `értékelés` + `implementáció` |
| `--lens <lista>` | pontosan a felsoroltak |
| `--lens all` / „teljes” | mind az öt |

**Plusz kötelező** a `biztonság-jog` lencse, ha a scope érinti az **M3**-at, az **M6**-ot, az
**M7 AI-leckéit**, vagy a `02 Tervezet/Adatvédelem – tanulói adatok és AI.md`,
`02 Tervezet/Gyermekvédelem – release gate.md`, `02 Tervezet/Emberi jóváhagyás szükséges.md`
fájlokat — illetve ha a Grep **szókezdetre illesztve** (csak bal oldali szóhatárral, mert a
toldalék jobbra hosszabbít) talál ilyet: `gyermekvédel`, `kiskorú`, `személyes adat`, `adatvéd`,
`jelzési kötelezettség`, `jelzőrendszer`, `hozzájárulás`, `feltárás`, `krízis`, `önfeltár`; valamint
az önálló `AI` szót **a `<!-- @asset … -->` blokkokon kívül**. A puszta `adat` és `jelzés` nem
trigger (a `feladat` és a `visszajelzés` is illeszkedne).

Explicit `--lens` lista az erősebb; ha így egy kötelező `biztonság-jog` lencse kimarad, a riport
első pontja kimondja, miért. Bekapcsolt kötelező lencsénél is megnevezed a triggert.

## 4. Delegálás — korlátos párhuzamosság

| Lencse (`--lens` token) | Agent | ID-prefix |
|---|---|---|
| pedagógia (`pedagogy`) | `pedagogy-reviewer` | `PED` |
| értékelés (`assessment`) | `assessment-reviewer` | `ERT` |
| nyelv (`language`) | `hungarian-editorial-reviewer` | `NYELV` |
| biztonság-jog (`safety`) | `safety-policy-reviewer` | `BIZT` |
| implementáció (`implementation`) | `implementation-reviewer` | `IMPL` |

- **Fájlcsoportok:** lencsénként legfeljebb kb. 6 fájl vagy 150 KB szöveg egy hívásban; a csoportok
  minden lencsénél ugyanazok. Több csoportnál az ID `<PREFIX>-G<n>-<k>`, így a scope-on belül egyedi.
- **Egyszerre legfeljebb 8 ügynök fut**; a többi sorban vár. Az ügynökök a háttérben futnak: az
  értesítésükre vársz, közben nem keresgélsz várakozásként (különösen nem a repón kívül).
- **Minden prompt** tartalmazza: a konkrét fájlútvonalakat és a scope-ot; hogy a
  `.claude/finding-format.md` szerint válaszoljon, fájltartalmat ne adjon vissza; az ID-prefixet és
  a csoportjelet; a **lezárt döntés** és a **bizonyíték-kapu** definícióját szó szerint a
  `.claude/rules/safety-and-human-gates.md` „Lezárt döntések” szakaszából; és a scope-ra érvényes
  lezárt freeze- vagy scope-döntést, ha van.
- **Folytatás:** részleges eredmény (lépéskorlát) vagy `LEVÁGVA: n …` sor esetén ugyanazt az
  ügynököt `SendMessage`-dzsel folytatod („folytasd: a még le nem adott findingok, a már leadottak
  ismétlése nélkül”), amíg nincs több. Ami így sem teljes, az a riportban **hiányos lencse**, a
  hiányzó rész megnevezésével. Csendben egy finding sem eshet ki.

## 5. Mentés — azonnal, tartósan

A riportfájl: `01 Fejlesztés/04 Audit/<ÉÉÉÉ-HH-NN> Validált findingok – <scope>[, <Run-ID>].md`.
Az első lencse-kimenet megérkezésekor hozd létre (`Write`) ezzel a fejléccel: scope, lencsék,
Run-ID, **Review-bázis: `<HEAD rövid SHA>`** (+ nem commitolt változás a scope-ban, ha van),
`Állapot: NYERS — verifikáció folyamatban`, és a szerkezet: I. riport · A. verifier-kontextus ·
B. verdiktek · C. nyers lencse-kimenetek. Minden további lencse-kimenetet **megérkezéskor**,
szó szerint fűzz a C. melléklethez (`Edit`) — a scratchpad újraindításkor törlődik, a context
tömörödik. (Kész, nagy fájlhoz: `python3 tools/audit_import.py`.) Az abszolút helyi útvonal-előtagot
repó-relatívra rövidíted; privát repónév és hangnév nem kerülhet bele.

## 6. Adverzális ellenőrzés

- A `verifier` hívásonként legfeljebb kb. **20 findingot** kap; az egy tényállásról szóló, több
  lencséből jött findingok (klaszter) ugyanabba a hívásba kerülnek, a klaszter-térképpel együtt
  (A. melléklet). A prompt tartalmazza a „Lezárt döntések” szabályt, a scope korlátait, és hogy a
  restauráció/baseline kérdésre a válasz „baseline ismeretlen”, ha nem kap baseline-kivonatot.
- **Minden ID kap verdiktet:** a nyers ID-k és a verdiktsorok számát összeveted; a hiányzókat
  ugyanattól a verifiertől kéred (`SendMessage`). A verdikteket megérkezéskor a B. mellékletbe írod.
- A riport számait a verdiktsorokból számolod, nem a verifier összesítőjéből.

## 7. Riport (I. rész) — csonkítás nélkül

Sorrend `P0` → `P3`, ezen belül lencse szerint. A fájlban nincs darabszám-korlát:
1. **Scope és lencsék** — mit néztünk meg, mit nem, miért; kimaradt kötelező vagy hiányos lencse;
   újrahasznosított rész; read-only bizonyíték (0. pont).
2. **Validált objektív findingok** (`MEGERŐSÍTVE` + `objektív`): ID (összevont duplikátumokkal),
   súly, hely, probléma, javítás és javítási korlát — a bizonyíték-idézet a C. mellékletben.
3. **Emberi döntést igénylő tételek** — javasolt szöveg nélkül: mit kell eldönteni, kinek.
4. **Bizonyíték-kapuk** — szerep, G-kapu (`02 Tervezet/RELEASE-READINESS.md`); ezek nem mennek
   `/course-fix`-be.
5. **Elvetve** — minden elvetett ID egy sorban, az okkal.
6. **Következő lépés** — melyik objektív findingra melyik skill.

A fejlécben az `Állapot` → `VALIDÁLT`. Ezután a 0. pont ellenőrzése, majd a hívónak: a riport
útvonala, a darabszámok verdiktenként és a P0/P1 tételek egy-egy sorban — a teljes riportot nem
másolod vissza a beszélgetésbe.
