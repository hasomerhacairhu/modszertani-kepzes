# Emberi jóváhagyás / kitöltés szükséges

> Ez az egyetlen, rövid átadó-jegyzék. Az audit-folyamat részletes nyomait (riportok,
> review-doksik) **eltakarítottuk** — a belőlük származó döntéseket **beépítettük** a
> tananyagba. Ami **nem volt szakmailag eldönthető** (szervezet-specifikus tény, jogi
> kérdés, mozgalmi/szakértői aláírás), az itt és a szövegben **⟬KITÖLTENDŐ: …⟭**
> jelöléssel vár emberi kézre. A teljes audit-history a git-ben megmarad.

---

## 1. Inline kitöltendők (12 db) — keresd: `grep -rn "⟬" "02 Tervezet"`

| Hol | Mit kell kitölteni |
|-----|--------------------|
| **M3.3** fejléc (sor 8–10) | gyerekvédelmi felelős **neve**, jóváhagyás **dátuma**, következő felülvizsgálat dátuma |
| **M3.B** fejléc (sor 8–10) | gyerekvédelmi felelős **neve**, (ajánlott) mentálhigiénés szakértő **neve**, dátum |
| **M3 – KAPU** fejléc (sor 11–13) | gyerekvédelmi felelős **neve**, jóváhagyás + felülvizsgálat **dátuma** |
| **M3.4** (sor 161) | a ken **hivatalos alkohol- és dohányzási magatartási kódexe** (mit szabad/nem, hol, milyen kortól) |
| **M0.2** (sor 257) | kihez fordulhat a madrich személyesen (megnevezett **gyerekvédelmi felelős/mentor + elérhetőség**) |
| **M7 – KAPU** (sor 206) | a ken nevesített **gyerekvédelmi felelőse + helyi jelzési protokoll** (azonnali-veszély / 112 ág) |
| **Program terv** §5/§6 (`[...]` jelölés) | a **support-kapcsolatok**: adatkezelési felelős + technikai support **megnevezett címe/elérhetősége** (a `[a mentorodnak / megnevezett felelős – kapcsolat]` zárójeles helyek) |

> A szöveg ezeken a helyeken a **best-practice keretet** már tartalmazza (transzparencia,
> jelzési kötelezettség, „nem hagylak egyedül"); csak a **konkrét nevet/dátumot/helyi
> politikát** kell behelyettesíteni.

## 2. Jogi / szervezeti döntést igénylő tételek (szándékosan NEM auto-írtuk meg)

Ezeket egy szakember (gyerekvédelmi felelős + szükség esetén jogi/adatvédelmi) döntse el:

- **Adatvédelem (GDPR / kiskorúak):** a reflexiós napló- és Assignment-/Essay-adatok
  **megőrzési ideje, törlési folyamata, korhatár-kezelése és 16 alatti szülői hozzájárulása**
  (érintett: M0, M2.4, M4 Essay-k + M4.4 Assignment). Adatminimalizálási elv: csak ami kell.
- **Nevesített eszkalációs lánc:** madrich → **megnevezett** gyerekvédelmi felelős (DSL) →
  hatóság, külön **azonnali-veszély / 112** ág — a szerepek és elérhetőségek behelyettesítése.
- **Kiskorú (15–17) madrich kettős státusza:** 18 alatti ne felügyeljen egyedül; saját
  bejelentési útja és a hatalmi egyenlőtlenség kezelése — szervezeti policy.
- **AI-tartalom kétlépcsős lektorálási policy** kimondása az indító dokumentumban
  (általános: módszertani felelős; safeguarding: + gyerekvédelmi felelős sign-off).

## 3. Opcionális szerzői / stiláris döntés

- **M0 belépő-kvíz:** jelenleg **completion-jelzőként** építettük be (nem küszöbös vizsga).
  Ha a stáb mégis éles, küszöbös kaput akar: 6–8 megírt item + answer key + cél→item tábla
  (kiemelten az „éves ív" és „online dugma ishit" kompetenciákra) szükséges.
- **„Dugma Ishit az online térben" leckecím (M0.4) — casing:** a glosszárium szerint a
  *dugma ishit* kisbetűs köznév, de ez a cím (és a **fájlnév** + ~7 link) nagybetűs
  címformát használ. A folyószövegben már kisbetűsítettük; a **címet/fájlnevet NEM**
  neveztük át (a fájl-átnevezés a linkeket is érinti). Döntés: maradjon-e a címben a
  nagybetűs forma (mint tulajdonnévszerű lecke-cím), vagy egységesítsük kisbetűsre
  (akkor fájl-átnevezés + a hivatkozó linkek frissítése kell).
- **M3.1 Tuckman magyar címkék:** a lecke a „storming"-ra helyenként „viharzás",
  máshol „balhék" alakot használ (utóbbi szándékos, Gen Z-barát glossza lehet) — ha
  teljes egységesség a cél, a stáb döntse el a kanonikus magyar megfeleltetést.

---

*A részletes javítási terv (P0/P1/P2 prioritások, kutatás-alapú ajánlások, források) és a
teljes audit a git-history-ban elérhető (`git log`, a `docs(audit)` és `fix(deep-audit)`
commitok). Vezérelv a továbblépéshez: **„kevesebb gépezet, több mozgalom"** — a meglévő
nonformális erősségekre építeni, reális önkéntes-kapacitással, MVP-logikával (1 modul +
1 kapu élesben → mérés → bővítés).*
