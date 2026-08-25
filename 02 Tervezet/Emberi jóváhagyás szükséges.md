# Emberi jóváhagyás / kitöltés szükséges

> Ez az egyetlen, rövid átadó-jegyzék. A teljes audit- és javítás-folyamat a **git-history-ban**
> él (`git log`); az abból származó **szakmailag eldönthető** döntéseket **beépítettük**. Ami
> **szervezet-specifikus tény, jog, vagy mozgalmi/szakértői aláírás**, az itt és a szövegben
> **`⟬KITÖLTENDŐ: …⟭`** jelöléssel vár emberi kézre.
>
> **Az összes inline jelölő egy paranccsal:** `grep -rn "⟬KITÖLTENDŐ" "02 Tervezet"`  (jelenleg ~30 db)

---

## 1. Gyermekvédelmi felelős + eszkalációs lánc (a legmagasabb prioritás)

A program **több ponton** a nevesített gyermekvédelmi felelősre (DSL) épül. **Egyetlen aláírás-hiány az M3-at és az M7 félévzáró kaput is blokkolja** (lásd Program terv §9). Kitöltendő:

| Hol | Mit |
|---|---|
| **M3.3** / **M3.B** / **M3 – KAPU** fejléc | gyermekvédelmi felelős **neve**, jóváhagyás + felülvizsgálat **dátuma** |
| **M3 – KAPU** §3 (külső eszkalációs út) | ha a gyanú épp a felelősre vonatkozik: **alternatív/külső** jelzési út |
| **M7 – KAPU** (~211. sor) | a ken nevesített **gyermekvédelmi felelőse + helyi jelzési protokoll** (azonnali-veszély / 112 ág) |
| **M0.2** (~270. sor) | kihez fordulhat a madrich személyesen (**felelős/mentor + elérhetőség**) — **kiterjed** a „ha a tananyag téged is érint” **bizalmas trainee-útra** is (lásd §4), nem csak a tanulási/technikai elakadásra |
| **M3.4** | a ken **alkohol- és dohányzási magatartási kódexe** (mit/hol/milyen kortól) |

## 2. Kapu-dátumok — M7 kétkapus capstone (ÚJ)

A jóváhagyott M7-átalakítás bevezetett egy **kétkapus, időben elosztott** capstone-ütemtervet (Peula v1 first-draft gate → ~1 hét spacing-köz → v2 mastery-kapu). A **pontos naptári dátumok** kitöltendők:

- **M7 hub** (~34/36/201/203), **M7 – KAPU** (~24/26), **M7.B** (~14): v1-leadás + v2 mastery-leadás határideje
- **Program terv** §3.1 / §3.2 / §5 (~97/186/249): ugyanezek a kapu-dátumok
- *Döntés:* a v1-kapu Moodle-ben „külön határidős, de nem buktató” aktivitás-e, vagy mentor-jelölt mérföldkő.

## 3. Governance & megfelelőség — Program terv §9 compliance gate (ÚJ)

A §9 **élesítés-előtti, blokkoló aláírólista** (7 sor). Kitöltendő:

- **Módszertani felelős** + **DSL/gyermekvédelmi felelős** neve (§9 új 6. sor – kétlépcsős AI+safeguarding lektorálás; Program terv ~333/334)
- **AI-média provenance-eljárás** (§4 + §9 7. sor): az **ember-olvasható** jelölés szövege és elhelyezése kötelező elem; a gépi provenance-jelölés (pl. C2PA / Content Credentials / vízjel) megőrzése ajánlott jó gyakorlat. Az EU AI Act 50. cikk (2) gépi jelölési kötelezettsége az AI-rendszer **szolgáltatóját** terheli; a deployer-oldali 50. cikk (4) közzétételi esetek (deepfake, közérdekű AI-szöveg) alkalmazhatóságát **jogi review** minősítse.
- **Támogatási elérhetőségek** (§5/§6 `[...]`): adatkezelési felelős + a technikai segítség megnevezett elérhetősége; **M4.1** (~54) technikai segítségkérési csatorna
- **Mentor:madrich arány** (§6 stáb-kapacitás realitás-megjegyzés) — a stáb tényleges kapacitása szerint
- **Akadálymentesítési lektor** neve (LMS-sztenderd KAPUS pre-flight)

## 4. Adatvédelem (GDPR / kiskorúak) — jogi döntés

Szakember (gyermekvédelmi + adatvédelmi) döntse el:
- A reflexiós napló-, Essay- és Assignment-adatok **megőrzési ideje, törlési/anonimizálási folyamata, valamint célonként a GDPR 6. cikk szerinti jogalapja** (és ahol a jogalap a hozzájárulás, ott az is, hogy a 8. cikk egyáltalán alkalmazandó-e, illetve kell-e szülői/gondviselői engedélyezés) (érintett: M0, M2.4, M4-Essay-k + M4.4 Assignment).
- **M6.3 fotók** (~48/49/52): kép **forrása/fotós**, **licenc**, és felismerhető kiskorú képmása esetén a **jogalap + dokumentáció** meghatározása (GDPR 6. cikk, szükség esetén 9. cikk; a magyar polgári jog szerinti képmáshoz fűződő jog; szülői/gondviselői engedélyezés **ott, ahol az alkalmazandó jogalap vagy a szervezeti policy ezt kéri**). **Nem vezetünk le univerzális „minden gyerekfotóhoz mindig írásos szülői hozzájárulás” szabályt** – lásd `Adatvédelem – tanulói adatok és AI.md`.
- **Kiskorú (15–17) madrich kettős státusza:** 18 alatti ne felügyeljen egyedül; saját bejelentési útja **nem csak** a transzfer-próba (M7→Z terepi vállalás) felügyeletéhez kötve, **hanem a teljes félévre** kiterjedően — szervezeti policy.
- **„Ha a tananyag téged is érint” — program-szintű, trainee-felé néző biztonsági út:** a célcsoport 15+, tehát maga a madrich is gyakran kiskorú, és a tananyag súlyos témákat dolgoztat fel (önsértés, bántalmazás, határátlépés). A program **in-the-moment szinten MÁR kezeli** a madrich saját érintettségét (M3.B azonnali kezelés blokkja: bizalmas zárás + nevesített kontakt/krízisvonalak; M0.2 reflexiós napló: mentor-út + safeguarding-kivétel), de **nincs program-szintű, a teljes félévre kiterjedő, egységesen nevesített bizalmas út és szégyenítés nélküli kimaradási lehetőség**. Kitöltendő szervezeti policyként: **(a)** kihez fordulhat a madrich **bizalmasan** (mentor / DSL / külső kontakt – nevek, elérhetőség); **(b)** **szégyenítés nélküli kimaradási lehetőség** az érzékeny gyakorlatból (M1 önismeret, M3 gyermekvédelem, M2.4 reflexiós napló); **(c)** a felkavaró témát érintő modulok introjába egy rövid, **a madrichnak címzett** biztonsági sor. *(A program-szintű szövegezés a **Program terv §2/§6**-ba és a felkavaró témát érintő modulok introjába épül be — az a fájl gazdájának feladata; itt a jogi/policy-döntés és a DSL-sign-off rögzül. Forrás: NYA Safeguarding for Youth Work; Safeguarding Network – supervision: a feltárásokat érintő tartalom kétirányú, a feldolgozó maga is érintett lehet, ezért szupervízió / reflektív feldolgozó kör jár a résztvevő védelmére.)*

## 5. Mozgalmi / ken-megerősítés — tartalmi (ÚJ)

A helyi Somer / ken erősítse meg:
- **Izrael/cionizmus — palesztin-/béke-dimenzió** (M2.3 ~227. sor + M2.B emlékeztető): a kánon-hű kiegészítés **pontos mozgalmi szövegezése** (`⟬KITÖLTENDŐ: ken-megerősítés⟭`). Politikailag érzékeny — a mozgalmi vezetés hatásköre.
- **Kvuca-korosztályok és profilok** (Parparim 6–10 / Kivsza 11–13 / Leviatan 14–16 / Zorea 16+): mozgalom-belső konvenció, a helyi ken-vezetővel megerősítendő (glosszárium 🧑‍🏫 jelölés).
- **Hagshama** pontos mozgalmi megfogalmazása (glosszárium).

## 6. Opcionális szerzői / stiláris döntés

- **„Dugma ishit” leckecím (M0.4) — fájlnév:** a látható szövegekben már kisbetűsítve; a **fájlnév** (+ ~7 link-URL) maradt nagybetűs (a fájl-átnevezés a linkeket is érinti). Döntés: marad-e a fájlnév, vagy átnevezés + link-frissítés.
- **M0 belépő-kvíz:** jelenleg **completion-jelző** (nem küszöbös). Ha éles kapu kell: item-bank + answer key + cél→item tábla.
- **Gyártási becslések** (pl. M2.3 Branching-embernap ~13. sor; M5.3 Moodle-időzítő eszköz): a tényleges fejlesztési ráfordítás/eszköz behelyettesítése.

---

## Dokumentált, elfogadott reziduumok (NEM hiba, tudatos megállás)

- **Lecke-beágyazott kvízek hossz-cue:** a 6 KAPU-bank (éles kapuk) + a lecke-kvízek javítva (a helyes válasz már sehol nem a szigorúan leghosszabb); a **kulcsok igazoltan változatlanok**. Ahol az M3-KAPU safeguarding-itemje hosszabb, az **elkerülhetetlen** (a teljes, biztonságos válasz eleve hosszabb) — elfogadható.
- **Peula módszer-paletta:** a mag érett és változatos; a **nagycsoportos önszervező dialógus** (fishbowl / world café / open space) **tudatosan NEM** került be (45' időkeret + önkéntes-stáb facilitációs teher). **Frissítve (2026-08-25 follow-up):** a korábban itt „opcionálisként” jelölt **fórum-színház az M3.B-ből kikerült** – a modul hivatalos és kötelező formátuma a **harmadik személyű esetelemzés**, szerepjáték nélkül (lásd `Gyermekvédelem – release gate.md`). Az M3.B opcionális „mondat-labor” mikroeleme **nem szerepjáték**: csak a madrich reakciómondatát mondják ki kívülről, és a gyermekvédelmi felelős engedélyéhez kötött.
- **Sablon-konzisztencia (modalitás):** a #3 modalitás-pilot (M5.3 Dialog Cards, M2.3 Branching) beépült; **a Z.4 NEM Documentation Toolra épül** — a H5P Documentation Tool nem támogatja a content state savinget, ezért a Z.4 hivatalos futtatókörnyezete **Moodle Assignment** (lásd `LMS – H5P runtime acceptance.md`); a teljes terv a `[[modality-variety-plan]]` memóriában.

---

*Vezérelv a továbblépéshez: **„kevesebb gépezet, több mozgalom”** — a meglévő nonformális
erősségekre építeni, reális önkéntes-kapacitással, MVP-logikával (5 → 4 → 3 modul/kapu
élesben → mérés → bővítés). A teljes audit-history: `git log`.*
