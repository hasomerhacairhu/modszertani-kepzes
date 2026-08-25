# Finding-formátum

Minden review-finding ebben a formában készül — ez a formátum kánoni otthona.
Hivatkozik rá: `.claude/agents/*`, `/course-review`, `/course-fix`, `/hungarian-edit`,
`/course-develop`.

## Egy finding mezői

- **ID** — `<LENCSE>-<sorszám>`, pl. `PED-3`, `NYELV-7`
- **Súlyosság** — `P0` / `P1` / `P2`. P3 és lejjebb nincs.
- **Bizalom** — `magas` / `közepes` / `alacsony`
- **Lencse** — pedagógia | értékelés | nyelv | biztonság-jog | implementáció
- **Hely** — `fájl útvonala:sor`, vagy `fájl > szakaszcím`
- **Probléma** — egy mondat, konkrétan
- **Bizonyíték** — szó szerinti idézet a fájlból (max 2 sor), ami miatt ez hiba
- **Hatás** — mi romlik el a tanulónál vagy a képzőnél, ha marad
- **Javaslat** — konkrét javítás, VAGY `EMBERI DÖNTÉS: <mit kell eldönteni, kinek>`
- **Típus** — `objektív` (bizonyítható) vagy `emberi-döntés`
- **Verdikt** — a verifier tölti ki: `MEGERŐSÍTVE` / `ELVETVE` / `EMBERI DÖNTÉS`

## Súlyossági küszöb

| | |
|---|---|
| **P0** | gyermekvédelmi vagy jogi kockázat; hamis completion; blokkoló sorrendi hiba; törött kánoni hivatkozás; nem létező futtatókörnyezet ígérete |
| **P1** | cél ↔ értékelés széttartás; félrevezető szakmai állítás; jelentést torzító nyelvi hiba; akadálymentesítési hiány; ismert regresszió visszatérése |
| **P2** | érdemi, de nem blokkoló minőségjavítás |

## Szabályok

- **Bizonyíték nélküli finding nem finding.**
- Ismétlődő mintát **egy** findingba vonj össze — de sorold fel a konkrét helyeket.
- Ne írj „rendben van" megállapítást. Csak problémát jelents.
- Bizonytalanságnál inkább ne jelents, vagy jelöld `alacsony` bizalommal.
- Ne dumpolj vissza fájltartalmat — csak a bizonyíték-idézeteket.
