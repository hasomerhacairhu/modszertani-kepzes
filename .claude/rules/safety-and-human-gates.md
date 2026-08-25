---
paths:
  - "02 Tervezet/**/*.md"
---

# Biztonsági és emberi döntési kapuk

Ez a fájl arról szól, **mikor kell megállni.** A tananyag kiskorúakkal dolgozó
ifjúsági vezetőket képez; több kérdésben a helyes válasz nem levezethető a repóból.

## Állítás-osztályok — mindig különítsd el

| Osztály | Mit tehetsz vele |
|---|---|
| **TÉNY** | ellenőrizhető elsődleges forrásból; javítható, ha bizonyítottan hibás |
| **PROJEKT-DÖNTÉS** | a repóban már rögzített szándék; követni kell, nem újraértelmezni |
| **EMBERI JÓVÁHAGYÁS KELL** | findingot írsz és megállsz — nem írsz be „ésszerű" választ |

Ha nem tudod eldönteni, melyik osztály: az **EMBERI JÓVÁHAGYÁS KELL**.

## Megállási jelek

Állj meg és jelezz, ha a szöveg ezekhez nyúlna:

- **kiskorúak szerepe**: a madrich maga is lehet kiskorú — nem ő az egyedüli felelős felnőtt,
  és nem kaphat önálló hatósági/jogi döntéshozói szerepet
- **gyermekvédelmi eszkaláció**: jelzési kötelezettség, jelzőrendszer, krízisvonalak,
  feltárás kezelése, „négyszemközt" jellegű instrukció kiskorúval
- **adatvédelem**: személyes vagy különleges adat, jogalap, megőrzés, hozzáférés,
  szülői hozzájárulás alkalmazhatósága
- **AI**: harmadik fél szolgáltatása, szolgáltatási feltételek, kiskorúak hozzáférése,
  AI Act szerepbesorolás (provider ≠ deployer), és a **kötelező nem-AI alternatíva**
- **helyi someres döntés**: ideológiai keret, mozgalmi konvenció, terminológia
  (nyitott: `madrich`/`madrih`, `chanich`/`hánih` — globális migráció tilos megerősítésig)
- **release**: bármely állítás arról, hogy valami éles, jóváhagyott vagy kész

A kánoni gate-dokumentumok: `02 Tervezet/Emberi jóváhagyás szükséges.md`,
`02 Tervezet/Gyermekvédelem – release gate.md`,
`02 Tervezet/Adatvédelem – tanulói adatok és AI.md`,
`02 Tervezet/RELEASE-READINESS.md`.

## Ha tárgyi kérdés merül fel

Kutass, de **elsődleges forrásból** (jogszabály hivatalos szövege, W3C, h5p.org,
a szolgáltató saját dokumentációja). Ha elsődleges forrás nem érhető el, ezt **mondd ki**,
és fogalmazz óvatosan. Ne találj ki policy-t azért, hogy „lezárd" a findingot.

## A leggyakoribb csapda

Egy rosszul hangzó biztonsági mondat javítása közben **ne írj helyette új, hihető
szakpolitikai állítást.** A megfogalmazás javítható; a szabály tartalma nem.
