# Adatvédelem – tanulói adatok és AI

## 1. Release-szabály

A learner-facing Moodle-kurzust a tényleges adatkezelő szervezet privacy/DPO/jogi felelőse hagyja jóvá. Zárt stagingben csak szintetikus tesztadat használható.

A repository **nem választ jogalapot, megőrzési időt vagy szülői folyamatot a szervezet helyett**. Ezek a döntések az `Emberi jóváhagyás szükséges.md` fájlban, stabil azonosítókkal élnek:

- **HUM-PRIV-01:** Moodle-adatkezelési mátrix;
- **HUM-PRIV-02:** fotó, videó, hang és kézírás;
- **HUM-PRIV-03:** Z.4 visszajelzés anonimitási szintje;
- **HUM-PRIV-04:** külső generatív AI tanulói használata.

## 2. Adatminimalizálási alapelv

Minden learner inputnál ebben a sorrendben kérdezzük:

1. szükséges-e egyáltalán begyűjteni;
2. szükséges-e Moodle-ban tárolni;
3. szükséges-e, hogy mentor/képző lássa;
4. elég-e, ha csak a madrich saját jegyzetében marad;
5. elérhető-e ugyanaz a pedagógiai cél kevesebb személyes adattal;
6. kérünk-e érzékeny vagy más személyre vonatkozó adatot valódi indok nélkül.

**Alapértelmezés:** ami csak önreflexióhoz kell, maradjon a madrichnál, hacsak a tanulási cél nem igényel beadandó produktumot. Érzékeny identitás-, családi-, egészségügyi/mentális vagy gyermekvédelmi történet **nem lehet kötelező tanulási artefaktum**. Mindig elfogadható legyen fiktív, általánosított vagy csak a tanulónál maradó alternatíva, ha a személyes adat nem a mérés tárgya.

## 3. Activity-szintű adatleltár

Az `LMS – activity manifest.md` minden tényleges activityhez privacy-osztályt rendel. A HUM-PRIV-01 lezárásakor az LMS-owner + privacy felelős ehhez adja hozzá a szervezeti döntéseket:

| Mező | Kötelező tartalom |
|---|---|
| adatmező | pontosan mi kerül tárolásra |
| cél | miért kell ehhez a pedagógiai/üzemeltetési célhoz |
| jogalap | a tényleges adatkezelő által jóváhagyva |
| kötelező/opcionális | része-e a teljesítésnek |
| címzettek | ki láthatja |
| szerepkör | milyen Moodle-role/capability alapján |
| megőrzés | konkrét idő vagy esemény |
| törlés | automatikus/manuális folyamat + felelős |
| export/hozzáférési kérelem | hogyan teljesíthető |
| harmadik fél | szolgáltató, adatfeldolgozói szerep, ország/adattovábbítás |
| kiskorú-specifikus szabály | ha alkalmazandó |

Külön review szükséges legalább:

- M0 „Bemutatkozó fal”: kurzuson belül más résztvevőknek látható;
- M1 SBI-beadandó;
- M2 identitás- és értékreflexiók, identitás-jegyzet;
- M3 gyermekvédelmi helyzetelemzés, ahol **tilos valós, beazonosítható esetet kötelezően kérni**;
- M4 pitch és bármilyen felvételi workflow;
- M5/M6 produktumok;
- M6 fotó/kézműves dokumentáció, ha egyáltalán szükséges;
- M7 AI-promptok és Peula v1/v2;
- Z.2/Z.4 személyes reflexiók és mentor-hozzáférés;
- Z.4 Feedback.

## 4. Kiskorúak és hozzájárulás

A GDPR 8. cikke csak akkor alkalmazandó a saját korhatárszabályával, ha **az adatkezelés a 6. cikk (1) a) szerinti hozzájáruláson alapul, és információs társadalmi szolgáltatást kínálnak közvetlenül gyermeknek**. Az uniós alapszabály 16 éves korhatárt mond, és lehetővé teszi, hogy a tagállam ezt 13 éves korig csökkentse.

Ez **nem** jelenti azt, hogy „minden 18 év alatti Moodle-adatkezeléshez szülői hozzájárulás kell”. A képzés minden adatkezelési céljának jogalapját külön kell meghatározni, és azt is külön kell vizsgálni, hogy a GDPR 8. cikke egyáltalán alkalmazandó-e.

A szülői/gondviselői tájékoztatás vagy engedélyezés helyi folyamata ezért **HUM-PRIV-01/HUM-SAFE-03 emberi-jogi döntés**, nem a tananyag által kitalálható szabály.

## 5. Mentor- és képzői hozzáférés

A „mentor láthatja, mert hasznos lehet” nem elég indok.

- **P0/P1:** csak az a szerepkör lássa, amelynek a completion/értékelés üzemeltetéséhez szüksége van rá.
- **P2 beadandó:** a kijelölt értékelő/mentor, és csak a szükséges ideig.
- **kurzusfórum:** a résztvevő előre tudja, hogy a csoport látja.
- **saját önreflexió:** ne legyen mentor-látható, ha nincs rá konkrét pedagógiai szükség.
- **gyermekvédelmi feltárás:** nem kezeljük egyszerű „tanulói beadandóként”; a safeguarding-protokoll lép életbe.

A tényleges Moodle-role/capability beállítást stagingben vissza kell olvasni és tesztfiókokkal ellenőrizni.

## 6. Fotó, videó, hang és kézírás

Felvétel csak előre rögzített cél, jogalap, hozzáférés, tárolási hely, megőrzés és törlés mellett kerülhet a folyamatba.

**Első kérdés:** kell-e egyáltalán felvétel? Ha ugyanaz a pedagógiai cél felvétel nélkül is teljesül, az legyen az alapút.

Minimum:
- személyes telefon/felhő nem alapértelmezett tároló;
- azonosítható kiskorú, felhasználónév, kézírás vagy más beazonosító tartalom ne kerüljön tovább csak azért, mert „dokumentálni jó”;
- legyen felvétel nélküli alternatíva, ha a felvétel nem nélkülözhetetlen;
- a learner-facing instrukció mondja meg, **mit készítünk, ki látja, és mi történik vele utána**, amikor felvétel valóban része a feladatnak.

A jogalap és az esetleges szülői/gondviselői folyamat **HUM-PRIV-02**.

## 7. Külső generatív AI

Tanulói külső AI-használat csak **HUM-PRIV-04** lezárása után nevezhet meg konkrét szolgáltatót.

Nem alku tárgya:
- AI használata a madrichnak **opcionális**;
- legyen teljes értékű no-AI út;
- chanich neve, képe, elérhetősége, pontos helye, egészségügyi/mentális állapota, családi háttere, vallási/etnikai vagy más érzékeny identitása és beazonosítható eseménye **nem kerülhet promptba**;
- valós gyermekvédelmi döntést, veszélyértékelést vagy kríziskezelést nem delegálunk AI-nak;
- a szervezet dokumentálja a szolgáltató aktuális korhatárát, guardian-feltételeit, adatkezelési/training beállításait, admin kontrolljait, szerződéses/adatfeldolgozói helyzetét és a jóváhagyás dátumát.

A tananyagban addig az általános **„jóváhagyott AI-eszköz”** megfogalmazás marad.

## 8. Z.4 visszajelzés

A core Moodle Feedback `Record user names = No` beállítása esetén a válaszok név nélkül jelenhetnek meg, de a Moodle dokumentációja külön figyelmeztet arra, hogy ez **nem azonos a GDPR-értelemben vett teljes anonimitással**. A completion és a rendszer működése továbbra is kapcsolódhat felhasználói fiókhoz.

Ezért:
- learner-facing szövegben nem ígérünk „teljes anonimitást”;
- a jelenlegi biztonságos megfogalmazás: **„a válaszok név nélkül jelennek meg”**;
- ha a szervezet erősebb technikai anonimitást akar, azt HUM-PRIV-03-ban kell eldönteni és runtime-ban bizonyítani.

## 9. Release acceptance

- [ ] HUM-PRIV-01–04 lezárva;
- [ ] teljes activity-szintű adatleltár elkészült;
- [ ] learner-facing privacy notice rövid, magyar és érthető;
- [ ] mentor/képző hozzáférések tesztfiókkal ellenőrizve;
- [ ] retention/törlés folyamata és felelőse dokumentálva és tesztelve;
- [ ] no-AI út ténylegesen végigvihető;
- [ ] érzékeny saját történet nem kötelező teljesítési elem;
- [ ] fotó/videó/hang folyamat HUM-PRIV-02 szerint lezárva;
- [ ] Z.4 nem ígér bizonyítatlan anonimitást;
- [ ] privacy/DPO/jogi signoff bizonyítéka rögzítve.

## 10. Elsődleges források

- GDPR, különösen **5., 6., 8., 9., 13–15., 28. és 32. cikk**, EUR-Lex.
- Moodle aktuális privacy/completion/Feedback dokumentáció.
- A választott külső szolgáltatók aktuális hivatalos feltételei és adatvédelmi dokumentációja.

Ez a dokumentum adatvédelmi követelményrendszer, nem egyedi jogi tanács és nem helyettesíti a tényleges adatkezelő jogi/DPO döntését.
