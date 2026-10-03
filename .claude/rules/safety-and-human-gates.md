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

- **kiskorúak szerepe**: a madrih maga is lehet kiskorú — nem ő az egyedüli felelős felnőtt,
  és nem kaphat önálló hatósági/jogi döntéshozói szerepet
- **gyermekvédelmi eszkaláció**: jelzési kötelezettség, jelzőrendszer, krízisvonalak,
  feltárás kezelése, „négyszemközt" jellegű instrukció kiskorúval
- **adatvédelem**: személyes vagy különleges adat, jogalap, megőrzés, hozzáférés,
  szülői hozzájárulás alkalmazhatósága
- **AI**: harmadik fél szolgáltatása, szolgáltatási feltételek, kiskorúak hozzáférése,
  AI Act szerepbesorolás (provider ≠ deployer), és a **kötelező nem-AI alternatíva**
- **helyi someres döntés**: ideológiai keret, mozgalmi konvenció, terminológia
  (az írásmód 2026-10-02 óta eldöntött, HUM-SOMER-02: `madrih`, `hanih`, `hágsámá`, `dugma isit`, `Leviatán` — a migráció megtörtént, új szöveg ezeket használja)
- **release**: bármely állítás arról, hogy valami éles vagy kész. Egy HUM-tétel lezárása
  nem release-jóváhagyás; a release-állapotot csak a `content_integrity.py --release-report`
  `RELEASE-VERDICT` sora és a `RELEASE-READINESS.md` adja

A kánoni gate-dokumentumok: `02 Tervezet/Emberi jóváhagyás szükséges.md`,
`02 Tervezet/Gyermekvédelem – release gate.md`,
`02 Tervezet/Adatvédelem – tanulói adatok és AI.md`,
`02 Tervezet/RELEASE-READINESS.md`.

## Lezárt döntések

Ez a szakasz a lezárt döntés és a bizonyíték-kapu **egyetlen** definíciója; CLAUDE.md, a
verifier és a reviewerek erre hivatkoznak.

- **Lezárt projektgazdai döntés** (PROJEKT-DÖNTÉS): az `Emberi jóváhagyás szükséges.md`
  `LEZÁRVA` + `Jóváhagyta:` tételei, **és** ugyanennek a fájlnak a 8. szakasztól kezdődő,
  datált projektgazdai döntés-szakaszai (HUM-azonosító nélkül is; ma a 8. és a 9., egy
  később hozzáadott datált szakasz ugyanígy számít); **és** a média- és hangdöntések
  nyilvántartása, a `Média-assetek/PRODUCTION-DECISIONS.md` `LEZÁRVA` szakaszai, datált
  „Projektgazdai döntés (…)” blokkjai és „Lezárt döntések” táblázata. Bizonyítékuk a
  `01 Fejlesztés/04 Audit/` döntési
  jegyzőkönyveiben van. Kövesd és vezesd át őket; ne
  nyisd újra, és ne jelentsd nyitott emberi döntésként. A döntés a kánoni sorrend 1–3.
  forrásai fölött áll: ha egy forrás ellentmond neki, az a forrás javítandó (objektív
  finding), nem választási kérdés.
- **Hivatkozott, de még át nem vezetett döntés:** ha egy forrás datált projektgazdai döntésre
  hivatkozik (pl. „projektgazdai döntés 2026-10-03-B”, „VO D-19”), előbb keresd meg a
  `04 Audit` döntési jegyzőkönyvében. Ha ott sincs, vagy a fenti két nyilvántartás egyikébe sincs
  átvezetve, az nem nyitott emberi döntés, és a tartalmát nem találgatod: objektív finding,
  hogy a döntést át kell vezetni (forrás: a döntési csomag, szerepnéven).
- **Vétó/QA-szerepek:** a HUM-fájl „Utólagos ellenőrzés (vétó/QA)” soraiban megnevezett
  szerepek (pl. Memuna, DPO, programvezető, jogi felelős, ken-vezető, hozzáférhetőségi gazda,
  értékelési felelős). Későbbi ellenőrzésük vétó / minőségellenőrzés; vétónál a tétel
  újranyílik.
- **Bizonyíték-kapu:** ezeknek a szerepeknek az írásos bizonyítéka (a Memuna „átnéztem”
  bejegyzése, DPO-, jogi jóváhagyás, runtime- és build-bizonyíték) a `RELEASE-READINESS.md`
  G1–G8 kapuihoz tartozik, nem nyitott döntés: nem írod be és nem feltételezed, a hiányát
  `bizonyíték-kapu` típusú findingként jelented. Megfogalmazás, ahol kell: „megvalósítási
  döntés: projektgazda jóváhagyta; a formális szerepköri bizonyíték függő”.
- Egy lezárt tétel vagy kánoni mondat szó szerinti átvezetése egy másik fájlba objektív
  javítás (a HUM-azonosítóval). Ami a lezárt döntésen túlmegy, vagy annak új alkalmazási
  esete, az továbbra is EMBERI JÓVÁHAGYÁS KELL.

## Ha tárgyi kérdés merül fel

Kutass, de **elsődleges forrásból** (jogszabály hivatalos szövege, W3C, h5p.org,
a szolgáltató saját dokumentációja). Ha elsődleges forrás nem érhető el, ezt **mondd ki**,
és fogalmazz óvatosan. Ne találj ki policy-t azért, hogy „lezárd" a findingot.

## A leggyakoribb csapda

Egy rosszul hangzó biztonsági mondat javítása közben **ne írj helyette új, hihető
szakpolitikai állítást.** A megfogalmazás javítható; a szabály tartalma nem.
