# Emberi döntési csomag

> **Cél:** egyetlen helyen legyen minden olyan nyitott tétel, amelyet a repository nem dönthet el a szervezet helyett.
> A szakmailag vagy dokumentációból eldönthető kérdések nem kerülnek ide.
>
> **Szabály:** minden érintett fájl az alábbi döntésazonosítóra hivatkozik. Ugyanazt a döntést nem tartjuk fenn több, egymástól független `KITÖLTENDŐ` mezőben.
>
> **Staging ≠ élesítés:** ezek a döntések nem akadályozzák a zárt, szerkesztői Moodle-staging felépítését tesztadatokkal. Ahol a táblázat „éles kurzust” blokkol, ott valódi madrich nem kaphat hozzáférést a döntés lezárásáig.

## 1. Gyermekvédelem

### HUM-SAFE-01 — Helyi gyermekvédelmi jelzési lánc

| Mező | Tartalom |
|---|---|
| **Kérdés** | Ki a kijelölt gyermekvédelmi felelős, mi az elérhetősége, ki a helyettes/alternatív út összeférhetetlenség esetén, és mi a helyi akut-veszély eszkaláció? |
| **Miért szükséges** | M0, M3 és M7 több helyen konkrét felelőshöz küldi a madrichot. Ezt név és jóváhagyott helyi folyamat nélkül nem szabad élesben ígérni. |
| **Mi bizonyítható a repóból** | A madrich nem nyomoz, nem konfrontál feltételezett elkövetőt, nem ígér teljes titoktartást, és felelős felnőttet von be. Közvetlen életveszélynél a 112 sürgősségi út. |
| **Mit kell eldönteni** | felelős neve/szerepe és elérhetősége; helyettes/külső út; mozgalmi/országos eszkaláció; akut veszély helyi protokollja; dokumentálás helye és jogosultsága; jóváhagyás és következő felülvizsgálat dátuma |
| **Javasolt alapértelmezés** | Nincs szervezetfüggetlen alapértelmezés. A kurzus addig csak szerepnevet használhat belső stagingben, learner-facing kiadásban nem maradhat névtelen kontakt. |
| **Jóváhagyó** | gyermekvédelmi felelős + szervezeti vezetés; a jogi minősítésnél szükség szerint jogi szakértő |
| **Blokkol** | éles M0 safety-kontakt, M3.3, M3.B, M3-kapu, M7 gyermekvédelmi részei és M7-kapu |
| **Érintett források** | `Gyermekvédelem – release gate.md`, M0.2, M0.A, M3.3, M3.B, M3-kapu, M7.3, M7-kapu |
| **Implementáció a döntés után** | egyetlen jóváhagyott kontaktblokk kerül a Moodle-be; minden tananyag-hivatkozás ezt használja. |

### HUM-SAFE-02 — Négyszemközti / safer-working szabály

| Mező | Tartalom |
|---|---|
| **Kérdés** | Milyen feltételekkel beszélhet képző vagy madrich kettesben kiskorúval? |
| **Miért szükséges** | A tananyag több helyen felkavaró témát dolgoz fel, és M7-ben a peulatervnek is kezelnie kell a négyszemközti helyzeteket. |
| **Biztonságos jelenlegi minimum** | A tananyag nem ír elő automatikus félrevonulást. A beszélgetés diszkrét, de átlátható; ha nincs jóváhagyott helyi szabály, kérj be egy másik képzőt/felnőttet. |
| **Valódi alternatívák** | pl. látótávolság/nyitott ajtó; második felnőtt jelenléte; második felnőtt tudtával végzett beszélgetés. A szervezet dönti el, melyik és milyen dokumentálással elfogadható. |
| **Jóváhagyó** | gyermekvédelmi felelős |
| **Blokkol** | learner-facing safety instrukciók véglegesítése és M7 R4/Q14 helyi megfelelése |
| **Implementáció a döntés után** | a `Gyermekvédelem – release gate.md` egyetlen szabálymezője frissül; a tananyag nem másolja szét, csak erre hivatkozik. |

### HUM-SAFE-03 — A madrich saját érintettsége és kiskorú madrich státusza

| Mező | Tartalom |
|---|---|
| **Kérdés** | Kihez fordulhat bizalmasan a 15–17 éves madrich, hogyan maradhat ki érzékeny gyakorlatból, és milyen felnőtt felügyelet kötelező számára terepen? |
| **Miért szükséges** | A tananyag bántalmazást, önsértést, identitást és határhelyzeteket érint. A résztvevő maga is lehet érintett és kiskorú. |
| **Javasolt szakmai minimum** | szégyenítés nélküli `passz`/alternatív feladat; érzékeny feltárásnál nem marad egyedül; a 18 év alatti madrich nem kap egyedüli felnőtt felelősséget. |
| **Mit nem döntünk el** | konkrét bizalmas kontakt, szülő/gondviselő bevonásának helyi folyamata, felnőtt:madrich felügyeleti arány |
| **Jóváhagyó** | gyermekvédelmi felelős + programvezető |
| **Blokkol** | éles learner-facing safety tájékoztató és terepgyakorlat |
| **Implementáció a döntés után** | rövid, azonos szövegű „ha téged is érint” blokk a releváns modulokban és a kurzus elején. |

### HUM-SAFE-04 — Alkohol- és dohányzási szabály

A konkrét helyi szabályt nem a tananyag találja ki. **Jóváhagyó:** szervezeti vezetés + gyermekvédelmi felelős. **Blokkol:** csak azokat a learner-facing példákat, amelyek konkrét helyi tiltást vagy korhatárt állítanak. **Implementáció:** a jóváhagyott policy-re hivatkozás, nem a szabály teljes lemásolása az M3.4-be.

### HUM-SAFE-05 — Stáb-alkalmasság és safeguarding-induction

| Mező | Tartalom |
|---|---|
| **Kérdés** | Milyen alkalmassági/vetting ellenőrzés és milyen dokumentált gyermekvédelmi felkészítés kell a programban dolgozó felnőtt képzőknek, mentoroknak és madrichoknak? |
| **Miért szükséges** | A program kiskorúakkal dolgozik, de a repository nem nevezhet meg automatikusan egy konkrét hatósági ellenőrzést vagy dokumentumtípust minden szerepre. |
| **Szakmai minimum** | a stáb ismeri a jóváhagyott gyermekvédelmi láncot, az összeférhetetlenségi utat, a disclosure-kezelést és a safer-working szabályt; a kiskorú madrich nem kap egyedüli felnőtt felelősséget. |
| **Mit kell eldönteni** | szerepkörönként szükséges alkalmassági ellenőrzés; induction tartalma; nyilvántartás; megújítás/felülvizsgálat |
| **Jóváhagyó** | szervezeti vezetés + gyermekvédelmi felelős, jogszabályi alkalmassági kérdésnél jogi szakértő |
| **Blokkol** | valódi résztvevőkkel futó program indítása, nem a zárt Moodle-staging |
| **Implementáció** | stáb-checklist, jóváhagyási bizonyíték és induction-nyilvántartás; a tananyag csak a jóváhagyott eljárásra hivatkozik. |

---

## 2. Adatvédelem

### HUM-PRIV-01 — Moodle-adatkezelési mátrix

| Mező | Tartalom |
|---|---|
| **Kérdés** | Activitynként mi a cél, jogalap, hozzáférés, megőrzés, törlés/export és harmadik fél? |
| **Miért szükséges** | A kurzus reflexiókat, Assignmenteket, kvízeredményt és részben identitáshoz kötődő szöveget kezel. |
| **Jogi keret** | A GDPR 8. cikk nem általános „minden kiskorú adatához szülői hozzájárulás” szabály. A jogalapot adatkezelési célonként kell meghatározni. |
| **Javasolt alapértelmezés** | adatminimalizálás; személyes/érzékeny történet ne legyen kötelező; mentor csak azt lássa, amihez pedagógiai vagy biztonsági feladata van. A konkrét jogalap és retention nem található ki. |
| **Jóváhagyó** | adatkezelő privacy/DPO/jogi felelőse |
| **Blokkol** | éles learner release minden személyes adatot tároló activitynél |
| **Implementáció a döntés után** | az activity manifest `privacy_class` soraihoz beállítás + learner-facing privacy notice + törlési folyamat. |

### HUM-PRIV-02 — Fotó, videó, hang és kézírás

A szervezet dönti el a felvétel célját, jogalapját, hozzáférését, tárhelyét, retentionjét és törlését, továbbá azt, hogy az **M0.A kézírásos plakát fotózásánál** a beazonosítható tartalom eltávolítása önmagában elegendő-e az adott célhoz. A tananyag alapértelmezése: **ne gyűjts felvételt, ha ugyanaz a pedagógiai cél elérhető nélküle; személyes telefon/felhő nem alapfolyamat.**  
**Jóváhagyó:** privacy/DPO/jogi felelős. **Implementáció:** központi média-/felvételi szabály, amelyre M0/M4/M6 hivatkozik.

### HUM-PRIV-03 — Z.4 visszajelzés anonimitási szintje

A core Moodle Feedback `Record user names = No` beállítása **név nélkül jeleníti meg a válaszokat**, de a Moodle saját dokumentációja szerint ez nem GDPR-értelemben vett teljes anonimitás; az activity completion is felhasználói fiókhoz kötődhet.  
**Döntés:** ez az álnévtelen/név nélküli működés megfelel-e a szervezeti célnak, vagy külön technikai anonimitás kell.  
**Javasolt alapértelmezés:** learner-facing szövegben csak „név nélkül jelenik meg” állítás maradjon, amíg erősebb anonimitás nincs bizonyítva.  
**Jóváhagyó:** privacy/DPO + programvezető. **Implementáció:** Z.4 Feedback-beállítás és privacy notice.

### HUM-PRIV-04 — Külső generatív AI tanulói használata

**Döntés:** mely szolgáltató használható a madrichoknak, milyen életkori/guardian feltételekkel, milyen fiókkal és adatvédelmi beállítással.  
**Nem alku tárgya a tananyagban:** no-AI út; nincs beazonosítható chanich-adat promptban; safeguarding-döntést nem adunk át AI-nak.  
**Jóváhagyó:** privacy/DPO/jogi felelős + programvezető. **Implementáció:** a Moodle csak jóváhagyott szolgáltatót nevez meg; ellenkező esetben általános „jóváhagyott AI-eszköz” megfogalmazás és teljes no-AI alternatíva.

---

## 3. Programüzemeltetés

### HUM-OPS-01 — Központi ütemezés

A repository **nem talál ki naptári dátumot**. Egyetlen program-szintű ütemezésből kell származtatni minden Moodle availability/due date értéket.

Kötelező döntések:
- program kezdete és a modulhetek tényleges dátumai;
- az offline peulák időpontjai;
- Assignment/Quiz határidők;
- **M7 v1 → M7.B feedback/revízió → v2** konkrét dátumai úgy, hogy v1 és v2 ne essen ugyanarra a napra, és a kettő között tényleges köztes feedback + külön revíziós szakasz legyen;
- Z sorrend: Z.1–Z.3 → Z.A → Z.4.

**Jóváhagyó:** programvezető.  
**Implementáció:** az LMS-agent egy központi schedule-táblából tölti ki a dátumokat, nem egyes fájlok `KITÖLTENDŐ` mezőiből.

### HUM-OPS-02 — Támogatási kontaktok és mentori kapacitás

**Döntés:** technikai support csatorna, tanulási/mentor kontakt, valamint a tényleges mentor:madrich kapacitás.  
**Jóváhagyó:** programvezető.  
**Blokkol:** learner-facing support szöveg véglegesítése, nem a belső staging build.  
**Implementáció:** egy központi kurzusoldal „Segítség és kapcsolatok” blokkjából hivatkozik minden modul.

### HUM-A11Y-01 — Hozzáférhetőségi jóváhagyó szerepkör

A szervezet nevezze meg, ki írja alá a kapus elemek pre-flight ellenőrzését. A specifikációban addig **szerepkör**, nem kitalált személynév szerepel.  
**Jóváhagyó:** programvezető. **Blokkol:** learner-facing release, nem a staging.

### HUM-GOV-01 — Terepgyakorlat rubrika ↔ KPI megfeleltetés

A `Terepgyakorlat – 2. félév.md` 0–2 skálája és az intake „rubrikaátlag ≥4/5” célja nem azonos skála.  
**Döntés:** vagy 5 fokozatúra változik a terepi rubrika, vagy a KPI-t definiálja újra a szervezet a 0–2 skálán.  
**Jóváhagyó:** programvezető + módszertani felelős. **Blokkol:** KPI-riport, nem a Moodle-staging.

---

## 4. Mozgalmi tartalom

### HUM-SOMER-01 — Izrael/cionizmus és béke/palesztin dimenzió helyi megfogalmazása

A repository nem alkot mozgalmi állásfoglalást. A helyi Somer/ken erősítse meg az M2-ben használt pontos megfogalmazást.  
**Jóváhagyó:** helyi mozgalmi/ideológiai felelős. **Blokkol:** az érintett M2-rész learner-facing véglegesítése.

### HUM-SOMER-02 — Kvuca-korosztályok

A jelenlegi munkaverzió: Parparim 6–10, Kivsza 11–13, Leviatan 14–16, Zorea 16+. Ezt helyi mozgalmi konvencióként kell megerősíteni.  
**Jóváhagyó:** ken-vezető / mozgalmi felelős. **Blokkol:** a korosztályprofilok hivatalosként való kommunikálása.

### HUM-SOMER-03 — Hagshama helyi megfogalmazása

A pontos helyi jelentés és tananyagbeli megfogalmazás mozgalmi döntés. **Jóváhagyó:** mozgalmi/ideológiai felelős.

---

## 5. Média és szolgáltatók

A részletes gyártási alternatívák a `Média-assetek/PRODUCTION-DECISIONS.md` fájlban vannak. Ez a döntési csomag csak azokat a pontokat tartja nyilván, amelyek emberi jóváhagyás nélkül nem zárhatók.

### HUM-MEDIA-01 — Vizuális rendszer
A márka/stílus végleges választása a `PRODUCTION-DECISIONS.md` **D1** döntése. **Jóváhagyó:** projekt kreatív/márkafelelős.

### HUM-MEDIA-02 — Hangjogosultság és ElevenLabs-hang létrehozása
A két forrásbeszélő hangjához dokumentált jogosultság kell. A konkrét klónozási módot csak az aktuális ElevenLabs-feltételek szerint szabad választani. **Professional Voice Clone esetén a szolgáltató jelenlegi szabálya szerint a beszélő a saját hangját maga hozza létre és hitelesíti, majd privát módon oszthatja meg; más személy PVC-jét a projektfiók nem hozhatja létre helyette.**  
**Jóváhagyó:** jogi/privacy felelős + a hang tulajdonosa. **Implementáció:** a `VOICE-BIBLE.md` csak a ténylegesen létrehozott, jogosult voice ID-t kapja meg.

### HUM-MEDIA-03 — HeyGen/avatar és média-jogok
A választott HeyGen-folyamathoz szükséges személy-, hang-, képmás- és szolgáltatói jogosultságokat a `RIGHTS-EVIDENCE.md` szerint kell lezárni. **Jóváhagyó:** jogi/privacy felelős + érintett jogosult(ak).

---

## 6. Nem emberi döntés, ezért nem marad itt nyitott kapuként

- M0 belépő-kvíz: a jelenlegi kánon szerint diagnosztikus completion-jelző, nem éles kapu.
- H5P szabad szöveg: technikai megvalósítási/acceptance-kérdés, nem szervezeti döntés.
- Moodle activity-ID-k: build-kimenetek; a staging build után automatikusan rögzítendők.
- Moodle/H5P verziók: célkörnyezetből kiolvasható tények.
- Gyártási becslések: projekttervezési adat, nem learner-facing release-kapu.
- Fájlnév-stílusok: szerkesztői karbantartás, nem release-gate.

---

## 7. Dokumentált, elfogadott reziduumok

- A súlyos M3-es eseteket harmadik személyű esetelemzéssel dolgozzuk fel; traumatikus szerepjáték nincs.
- A Z.4 hivatalos reflektív produktuma **Moodle Assignment**.
- Az M0-kvíz completion-alapú diagnosztikus jelző.
- Az M7 kétlépcsős produktumfolyam invariánsa: **v1 → köztes feedback/revízió → v2**.
- A pedagógiai alapelv: **kevesebb gépezet, több mozgalom**.
