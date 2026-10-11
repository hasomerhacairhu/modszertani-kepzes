# 2026-10-11 Validált findingok – M0, nyelvi lencse, AP-2026-10-11-01

> **Audit trail — nem kánon, nem tanulói tartalom.** Read-only `/course-review M0 --lens language --run AP-2026-10-11-01`
> (`next-version` autopilot-futás). A tananyag a review alatt nem változott.
>
> - **Scope:** a teljes M0 modul, csak a hiányzó `language` lencse. A másik négy lencse (pedagógia, értékelés,
>   implementáció, biztonság-jog) a `2026-10-10 Validált findingok – M0 course-review, B sáv.md` riportban lefutott,
>   és a M0 a review-bázisa (82d0c7c) óta nem változott — ezek újrahasznosítva (REUSED).
> - **Lencsék ebben a riportban:** language. **Run-ID:** AP-2026-10-11-01.
> - **Review-bázis:** `886165b` (a `02 Tervezet/` tartalma azonos a `main@213a4c5`-tel); nem commitolt változás a scope-ban: nincs.
> - **Read-only bizonyíték (kezdet):** `git diff HEAD -- "02 Tervezet" | shasum` = `da39a3ee5e6b4b0d3255bfef95601890afd80709`;
>   `git ls-files --others --exclude-standard -- "02 Tervezet" | shasum` = `da39a3ee5e6b4b0d3255bfef95601890afd80709`.
> - **Read-only bizonyíték (mentés előtt):** `da39a3ee5e6b4b0d3255bfef95601890afd80709` / `da39a3ee5e6b4b0d3255bfef95601890afd80709` — egyezik a kezdő értékkel.
> - **Állapot:** VALIDÁLT (42/42 verdikt).
> - **Szerkezet:** I. riport · A. verifier-kontextus · B. verdiktek · C. nyers lencse-kimenetek (szó szerint; a helyi
>   abszolút útvonal-előtag repó-relatívra rövidítve, sorvégi szóközök törölve).

---

# I. M0 nyelvi lencse — validált riport (2026-10-11)

> Read-only review. Tananyag nem változott. Nyers findingok: C. melléklet (42: NYELV-G1-1…20, NYELV-G2-1…22); verdiktek:
> B. melléklet (három verifier, 42/42). Git-history a reviewereknél és a verifiereknél nem állt rendelkezésre: a
> restauráció/baseline kérdésre „baseline ismeretlen”, a súlyosság emiatt nem emelkedett.

## 1. Scope és futtatott lencsék

- **Scope:** a teljes M0 (6 fájl), két fájlcsoportban: G1 = hub, M0.1, M0.2, M0.3 · G2 = M0.4, M0.A.
- **Ténylegesen lefutott lencse ebben a riportban:** `language` (hungarian-editorial-reviewer; a levágott tételeket
  folytatással mind leadták: G1 20, G2 22 — hiányos lencse nincs).
- **Újrahasznosítva (REUSED):** pedagógia, értékelés, implementáció, biztonság-jog — a `2026-10-10 Validált findingok – M0
  course-review, B sáv.md` riportból (review-bázis `82d0c7c`); az M0 azóta nem változott. Így az M0-ra mind az öt lencse lefutott.
- **Read-only bizonyíték:** a kezdő és a mentés előtti `git diff HEAD -- "02 Tervezet" | shasum` és
  `git ls-files --others --exclude-standard -- "02 Tervezet" | shasum` egyaránt `da39a3ee5e6b4b0d3255bfef95601890afd80709`.

**Számok (a verdiktsorokból):** MEGERŐSÍTVE + objektív 20 · EMBERI DÖNTÉS 4 (ebből 1 duplikátum) · ELVETVE 18 · bizonyíték-kapu 0.

## 2. Validált objektív findingok (20, mind P2)

Javítási út: `/hungarian-edit` fájlonként. Látható szövegváltozás után `--pin-visible`; `@asset`-spec után `media_manifest.py build`.
Az M0.2 gyermekvédelmi helyein (G1-2, G1-8) a javítás után a Memuna-QA bizonyíték-kapu (G1) függő marad (vö. M0 BIZT-1).

| ID | Hely | Probléma | Javítás és korlát (verifier) |
|---|---|---|---|
| NYELV-G1-2 | M0.2:342 | „furcsának … látok / hallok” — a „-nak” vonzat a „hall” igével nem áll; perjel | olyan alak, amely a „-nak lát” szubjektív minősítést megtartja; a :341 lépéscím, az öt lépés, a DIA-01 és a HUB:147 nem változik |
| NYELV-G1-5 | M0.2:40 | húszszavas betoldás szakítja szét a birtokos szerkezetet; a Memuna első előfordulása nem a GK:80 formulájával | két mondat; a GK:80 formula betűhűen; a három szereplő és a „nem a te dolgod egyedül” jelentés marad |
| NYELV-G1-6 (részben) | M0.2:279 | „Az 1. helyzet … tudatosan kisebb tét” | csak „kisebb tétű”; a „fejlesztői visszajelzés” helyes, marad; az ERT-1-gyel egy menetben |
| NYELV-G1-7 | M0.1:198, :298; M0.2:279; M0.3:254, :292; M0.2:142 (spec) | „peula-terv(ezés)” ↔ a hub és a Glosszárium „peulaterv(ezés)”; a spec „Zmán Kvuca” ↔ Glosszárium:101 „Zmán Kvucá” | egybeírás; a 6. item projektgazdai szövege nem változik; a :142 build-del |
| NYELV-G1-8 | M0.2:260; M0.3:302, :312 (és ugyanígy :251, :257) | nyíl és „+” kötőszó helyett kérdés-, opció- és visszajelzés-szövegben | „Nem maradok egyedül: azonnal bevonom a Memunát”; „…kilépsz, ezért nincs pipa.”; „jelzés és támogatás”; a ✅ helye és az opciók jelentése marad; a leképező listák maradnak |
| NYELV-G1-11 | HUB:22, :38/:159, :43, :77, :83, :109; M0.2:173, :141 (spec) | különírt „alap” jelzőként | „alapelvárások”, „alapszintű” (ahol a jelentés alapszintű, nem „alapvető"); a :38 és a :159 együtt; a spec build-del |
| NYELV-G1-12 | M0.2:141 (spec), :173, :279; M0.3:102 (spec), :139, :235; M0.1:59, M0.2:62, M0.3:59 (+ M0.4:61) | kéttagú összetételek különírva/kötőjellel (AkH 139.) | „szereptisztázás”, „kapulogika”, „kurzusszerkezet”, „a célverzión”, „a célkörnyezetben”; csak az írásmód; specek build-del |
| NYELV-G1-13 | HUB:275, :283 | „elakadnak M0.3-nál”, „nem „complete” M0-ban” | „az M0.3-nál”, „nem teljesítette az M0-t”; a 30%-os küszöb és az „első hét” marad |
| NYELV-G1-15 | HUB:59 | a lecke címe eltér a :72-től és az M0.2:6-tól | „Madrih, nem terapeuta – szerepek és elvárások”; fájlnév, link nem változik |
| NYELV-G2-1 | M0.A:147–149, :152, :154–156, :647 | két címkerendszer egy percbontásban; „Kihez fordulhatok” kérdőjel nélkül | a 4.x blokkcímkék átvétele, „?” pótlása; percek, leírások maradnak; a 45’-es részen a PED-5-tel egy lépésben |
| NYELV-G2-3 | M0.4:554 (↔ :146) | a „kvucád” két csoportot jelöl egy leckében | „a képzős kvucáddal”; a PED-10-zel egy lépésben, a „Segítség és kapcsolatok” utalás marad |
| NYELV-G2-4 | M0.A:636 (↔ :90), :58 (spec) | az ellenőrző lista mást idéz, mint a 2.3 mondata | a :90 első mondata szó szerint; a :58-ból csak az ellenőrző listára vonatkozó rész kerül ki; build, pin |
| NYELV-G2-5 | M0.A:638 | a kánoni 5. lépés csonka („előbb a 112”) | „(közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés)” betűhűen (HUM-SAFE-01; Glosszárium:164–166) |
| NYELV-G2-6 | M0.A:610 | „az áttekintő” előzmény nélkül | csak az előzmény megnevezése („az M0 modul áttekintője”); a „szándékoltan” marad |
| NYELV-G2-12 | M0.4:565 (↔ :482–486) | a fórumleírás utolsó pontja felszólítás egy kérdéslistában | csak a :565 utolsó pontja kérdő formába, a mostani szóhasználattal; a teljes SLIDE 6-összhang az NYELV-G2-11 döntése után; a BIZT-8 és az IMPL-7 helyeihez nem nyúl |
| NYELV-G2-14 | M0.4:552 | „belépő-jelző” alkalmi képzés | a HUB:131 „belépő jellegű” átvétele szó szerint; a javasolt egyéni-láthatósági mondat nem használható (PED-8); a „mind a 7 kérdésre” mondat marad |
| NYELV-G2-16 | M0.4:501, :505, :525 | a toldalék az idézőjeles névben | „a „Bemutatkozó fal” fórumon/fórumra”; a :501 a BIZT-8-cal, a :525 névalakja az IMPL-7 után |
| NYELV-G2-17 | M0.A:474, :481, :196 (spec) | vessző a -ként jelentésű „mint” előtt | csak a vessző törlése („ÉN mint madrih”); a nagybetűsítés marad; spec build-del |
| NYELV-G2-18 | M0.A:40, :102, :129, :168, :170, :174, :180, :264, :268, :286, :288, :321, :366, :367, :385, :427, :502, :629, :639, :657; Z.A:55, :423, :440, :458 | kéttagú köznévi összetételek kötőjellel (stábdosszié, indulószavak, példajavaslat, miniprotokoll) | egybeírás minden helyen, az M0.A-ban, a Z.A-ban és az assetekben egyformán; a héber tagú konvenciós alakok (kvuca-plakát) maradnak; specek build-del |
| NYELV-G2-21 | M0.A:355, :426, :594 (+ MUNK-02 spec :520), :598 | perjel a felolvasandó idézetekben | „vagy”/„és”; a :594 a nyomtatott kártyával együtt (build, pin), vagy egyik sem; oszlopfejlécek maradnak |

## 3. Emberi döntést igénylő tételek — javasolt szöveg nélkül

| ID | Kérdés | Ki dönt |
|---|---|---|
| NYELV-G2-11 (= NYELV-G1-1) | A Glosszárium:27 „kerüld” szabálya (megszemélyesített „Dugma Isitnek lenni”; :219 „nagybetűs”) kiterjed-e a kisbetűs „dugma isit vagy / dugma isit madrih” alakra (M0.2:26, :417; M0.4:25, :154, :248/:293 diacím, :296, :486; HUB:144, :238; M0.4-ILL-03); két kánoni forrás ütközik. A projektgazdai itemtörzs (HUB:235) is így szól | projektgazda; QA: ken-vezető / mozgalmi felelős |
| NYELV-G1-14 | A belépőkvíz projektgazdai itemszövege (HUB:180) nyelvileg javítható-e: a 7. item „a completion állapotát” különírása, a 4. item alanya | projektgazda, az értékelési felelős QA-jával (vö. ERT-4) |
| NYELV-G2-22 | Az M0.A:347 „vagy páratlan a létszám” feltételének jelentése | modulgazda / projektgazda |

## 4. Bizonyíték-kapuk

Nincs új. (A G1-2 és a G1-8 javítása után az M0.2 gyermekvédelmi helyeinek Memuna-QA-ja a meglévő M0 BIZT-1 / G1 kapuhoz tartozik.)

## 5. Elvetve (18)

NYELV-G1-3 (a csatornaszabály szerkezete a korpusz kánoni alakja; a „csinálok” cseréje szűkítene) · G1-4 (közvetlen hangnem,
nem magázás) · G1-9 (bevett fordulat) · G1-10 (H5P típusnév, érvényes escape) · G1-16 (a nagykötőjel viszonyt is jelöl) ·
G1-17 (a beágyazott strong CommonMark szerint helyes) · G1-18 (jelentésében többes alany) · G1-19 (informális, de egyértelmű
címke; a többes szám helyes) · G1-20 (bevett szerkezet) · G2-2 (szabályos különírás, diaszöveg) · G2-7 (korpusz-szintű
konvenció; a javasolt csere rontana) · G2-8 (távirati képzői stílus) · G2-9 (a „jelen lenni” kánoni alak) · G2-10 (a
szakszó megengedett; a csere jelentéseltolás) · G2-13 (a hub is „komment”-et ír) · G2-15 (szabályos szerkezet) · G2-19
(szabályos szórend; a K1 átírja) · G2-20 (szabályos olvasat; nyomtatott biztonsági kártyát írna át).

## 6. Következő lépés

- `/hungarian-edit` fájlonként: HUB (G1-11, G1-13, G1-15), M0.1 (G1-7, G1-12), M0.2 (G1-2, G1-5, G1-6, G1-7, G1-8, G1-11,
  G1-12), M0.3 (G1-7, G1-8, G1-12), M0.4 (G1-12, G2-3, G2-12, G2-14, G2-16), M0.A (G2-1, G2-4, G2-5, G2-6, G2-17, G2-18,
  G2-21), Z.A (G2-18 négy helye, a Z-javítással egy menetben).
- Sorrendi függés a B sávos javításokkal: G1-6 ↔ ERT-1; G2-1 ↔ PED-5; G2-3 ↔ PED-10; G2-16 ↔ BIZT-8, IMPL-7; G2-12 ↔ NYELV-G2-11.
- Az emberi döntések a ledger Külső kapuinál.

---

# A. melléklet – verifier-kontextus

## M0 nyelvi lencse — verifier-kontextus és klaszter-térkép (fő munkamenet, 2026-10-11)

Findinglista: a riport C. melléklete — 42 nyers finding: NYELV-G1-1…20 (hub, M0.1, M0.2, M0.3), NYELV-G2-1…22 (M0.4, M0.A).

**Szabályok:** `.claude/rules/safety-and-human-gates.md` „Lezárt döntések” (szó szerint a promptban); `.claude/rules/hungarian-editorial.md`; `next-version` felhatalmazás (2026-10-11); a 2026-10-10-i projektgazdai döntés 5. pontja (szükségtelen módosítás kerülendő → preferencia = ELVETVE); a belépőkvíz projektgazdai itemszövege (HUB:180) — nyelvi javítása projektgazdai/értékelési QA-kérdés; a HUM-SAFE-03 blokk és a kánoni gyermekvédelmi mondatok szövege nem változik; a validált B sávos M0-findingok (2026-10-10) nem ismételhetők — átfedésnél csak a nyelvi többlet számít. Git-history nincs: „baseline ismeretlen”.

**Klaszterek (ugyanabba a hívásba):**

| Klaszter | Findingok | Tárgy |
|---|---|---|
| L1 | NYELV-G1-1, NYELV-G2-11 | a „dugma isit” megszemélyesítése (M0.2:26, HUB:238, :144 ↔ M0.4:25, :154, :486) ↔ Glosszárium:27 „kerüld” |
| L2 | NYELV-G1-7, NYELV-G1-12, NYELV-G2-17, NYELV-G2-18 | egybe-/különírás, kötőjel, „mint” előtti vessző; asset-specek is |
| L3 | NYELV-G1-8, NYELV-G2-21 | nyíl és perjel kötőszó helyett tanulói/felolvasandó szövegben |
| L4 | NYELV-G2-16, NYELV-G2-12, NYELV-G2-13 | a „Bemutatkozó fal” fórum (név, kérdések, „komment”) — vö. validált IMPL-7, BIZT-8 |
| L5 | NYELV-G2-19, NYELV-G2-3 | az M0.4 validált K1 (ERT-1) és PED-10 helyei |

**Mit kérünk minden findingnál:** verdikt és típus; ha a javítás jelentést változtatna vagy a szándék nem dönthető el → EMBERI DÖNTÉS; preferencia → ELVETVE; duplikátumnál a megtartandó ID; a javasolt szöveg nem ront-e.

---

# B. melléklet – verifier-verdiktek

## VERIFIER V1 — NYELV-G1-1…6, G1-8…11, NYELV-G2-11 (11 ID)

NYELV-G1-1 · EMBERI DÖNTÉS · emberi-döntés · P2 · Az idézet stimmel: M0.2:26 „hanem *dugma isit* (‘személyes példamutatás’), aki példát mutat”, HUB:238 „privát üzenetben is dugma isit vagy”, HUB:144 „egy **dugma isit** madrihhoz”. Csakhogy a Glosszárium nem fedi le egyértelműen a kisbetűs alakot: a :27 a nagybetűs „Dugma Isitnek lenni” alakot idézi, a :219 kifejezetten „A megszemélyesített nagybetűs `Dugma Isit` kerülendő” mondatot ír, a VOICE-BIBLE:135 pedig „személynévi alak”-ot. A modul közben következetesen állítmányi és jelzői alakot használ (M0.2:417 „Dugma isit = példa vagyok”, M0.4:25, :248/:293 diacím „Dugma isit vagy sem?”, :296 „egy dugma isit madrih”, M0.4-ILL-03 asset-cím). A projektgazdai itemtörzs is így szól (HUB:235 „Melyik online reakció dugma isit?”). Ez nyitott helyi terminológiai kérdés: a projektgazda dönt, utólagos QA a ken-vezető / mozgalmi felelős. Az M6-NY-D9 („csak a madrihra”) erre nem ad választ, és a HUM-nyilvántartásban sincs benne. Baseline ismeretlen. · duplikátum: a NYELV-G2-11 a megtartandó; ebből a findingból az M0.2:26 („aki” egy elvont glosszára mutat) és a HUB:144 helyet kell átvinni bele · javítási korlát: az M0.2:26 „aki”-hibája csak a megszemélyesítési döntéssel együtt javítható. A helylista hiányos (M0.2:417, M0.4:248/293/296, az ILL-03 asset-cím). A HUB:235 projektgazdai itemtörzse nem változhat, és a HUB:238 visszajelzés-szövege az értékelési felelős QA-ja alá esik.

NYELV-G2-11 · EMBERI DÖNTÉS · emberi-döntés · P2 · Ugyanaz a kérdés, mint a G1-1-nél: az M0.4:154 „Milyen dugma isit vagy az online térben?” és a :486 „**online is dugma isit** vagy” ütközik a Glosszárium:27 szabályával. A szabály hatálya a kisbetűs alakra nem egyértelmű (a :219 „nagybetűs”-t mond), a modul és a projektgazdai itemtörzs pedig rendszeresen ezt az alakot használja. Ez két kánoni forrás ellentmondása, amelyet a projektgazdának kell eldöntenie (QA: ken-vezető / mozgalmi felelős). A finding típusa és megfogalmazása helyes. · duplikátum: EZ a megtartandó (a G1-1 helyeivel kiegészítve) · javítási korlát: ha a döntés „igen”, a változás a diacímekre (M0.4:248/:293), az M0.2:417-re, az M0.4-ILL-03 asset-címre (media_manifest build) és a pinre is kiterjed. A HUB:235 itemtörzs csak a projektgazda és az értékelési felelős jóváhagyásával változhat. Az írásmód (HUM-SOMER-02) nem változik.

NYELV-G1-2 · MEGERŐSÍTVE · objektív · P2 · Az M0.2:342 „Valamit furcsának, ijesztőnek, zavarónak látok / hallok.” szerkezetében a „-nak” vonzat a „hall” igével nem standard („furcsának hangzik” volna). A tanulói diaszövegben álló perjel ellen szól a szerkesztői szabály is („`+`, `/` … helyett rendes mondat”). Baseline ismeretlen. · javítási korlát: a javasolt „Valami furcsát … látok vagy hallok” elhagyja a „-nak lát” szubjektív minősítést, amelyhez az 1. lépés („komolyan veszem”) kötődik. Olyan alak kell, amely ezt megtartja. A :341 lépéscím, az öt lépés, az M0.2-DIA-01 és a HUB:147 nem változik. A szerkesztés után a Memuna QA-ja bizonyíték-kapu (G1): nem feltételezhető, nem írható be.

NYELV-G1-3 · ELVETVE · — · P2 · A :431 „a személyes közösségimédia-fiókomról írok, hanem a szervezet csatornáján” szerkezete a korpusz kanonikus csatornaszabályával azonos. Ugyanez a „-ról ír … -n” alak áll az M0.4:419-ben, az M2.4:207-ben, az M3.4:358-ban és az M2 kapu item-bank :113-ban: nem hiba, és egy helyen átírva következetlenséget okozna. A :430-ban a „csinálok” → „írok” csere szűkítené a szabályt, mert az M0.4:417 üzenetet, mémet, képet és „megmutatnád”-ot is lefed. Ez jelentésváltozás a HUM-SAFE-02-höz kötött szövegben.

NYELV-G1-4 · ELVETVE · — · P2 · Az M0.1:382 „nem fogalmazásverseny, csak legyen őszinte” rejtett alanya természetesen a leírt szöveg („legyen [az írás] őszinte”). Magázás nem bizonyítható, a vesszős összefűzés beszélt nyelvi, közvetlen hangnem. Stílus-preferencia, a 2026-10-10-i döntés 5. pontja szerint elvetendő.

NYELV-G1-5 · MEGERŐSÍTVE · objektív · P2 · Az M0.2:40 „(hanem más – egy szakember, … a kijelölt **Memuna**, a Somer gyermekvédelmi felelőse – felelőssége)” birtokos szerkezetét egy hosszú betoldás szakítja szét. Ez a Memuna első tanulói előfordulása a fájlban, és eltér a GK:80 kötelező formulájától („a kijelölt **Memuna** (a Somer gyermekvédelmi felelőse)”). A formula szó szerinti átvezetése objektív javítás. · javítási korlát: a három szereplő, az „egyedül” és a GK:80 formula betűhűen marad. A javított mondat nem sugallhatja, hogy a madrihnak semmi része nincs a helyzetben: a „nem a te dolgod egyedül” jelentés megmarad. Látható szöveg → pin.

NYELV-G1-6 · MEGERŐSÍTVE · objektív · P2 · Csak részben: az M0.2:279 „Az 1. helyzet (peula-tervezés) tudatosan kisebb tét” szerkezete hibás, egy helyzet nem „tét”, helyesen „kisebb tétű”. A „fejlesztői → fejlesztő visszajelzés” rész nem bizonyított. A korpuszban a „fejlesztő visszajelzés” a mentor produktumra adott formatív visszajelzése (Glosszárium:203), itt viszont a fejlesztő által megírt H5P-visszajelzésről van szó, tehát a „fejlesztői” nem hiba. · javítási korlát: csak a „tétű” javítható. A „fejlesztői” maradjon. A megjegyzés szabálytartalma (a 2. helyzet kiemelése, a „köztünk marad” disztraktor) nem változik. Ugyanezt a helyet a validált ERT-1 is érinti.

NYELV-G1-8 · MEGERŐSÍTVE · objektív · P2 · A tanulói kérdés-, opció- és visszajelzés-szövegben a jel kötőszót helyettesít: M0.2:260 „**Nem maradok egyedül → azonnal bevonom a Memunát** ✅”, M0.3:302 „félúton kilépsz → nincs pipa.”, M0.3:312 „**jelzés + támogatás**”. A szerkesztői szabály szerint a `+` és a `/` helyére rendes mondat kell, és a képernyőolvasó a nyilat a nevén olvassa fel. A javasolt kettőspont, „ezért” és „és” a jelentést megtartja. · javítási korlát: a ✅ helye és az opciók jelentése nem változik. Az M0.2 2. kérdése a Memuna-QA hatálya alá esik (bizonyíték-kapu, nem feltételezhető). A leképező listák maradnak. Az azonos típusú tanulói nyilakat az M0.3:251 és :257 is tartalmazza, a finding mégsem sorolja fel őket: vagy egységesen kezelendők, vagy tudatosan maradnak. Látható szöveg → pin.

NYELV-G1-9 · ELVETVE · — · P2 · Az M0.3:233 „a technikai szavak **alapjai már megvannak**” a bevett „az alapjai megvannak” fordulat: megvan a technikai szókincs alapja. Értelmes, közvetlen hangú visszajelzés, a csere nem javítás, hanem preferencia.

NYELV-G1-10 · ELVETVE · — · P2 · Az M0.3:180 felsorolása H5P tartalomtípusokat sorol („kattintós videó, kvíz, drag\&drop”). A szerkesztői szabály megengedi az angol H5P UI-elem- és típusnevet, a `\&` pedig érvényes Markdown-escape, renderelve „&”. A H5P-be másolás kockázata feltételezés. A HUB:48 „social media” a stábnak szóló kompetencialeírásban áll, a csere ott preferencia. Bizonytalanság miatt elvetve.

NYELV-G1-11 · MEGERŐSÍTVE · objektív · P2 · Az „alap” különírva áll: HUB:22 „érti az alap elvárásokat …, megismeri az alap technikai eszközöket”, :38/:159 „Alap technikai működés”, :43, :77, :83 „alap H5P-t”, :109, továbbá M0.2:173 és :141. Főnévvel összetételt alkot („alapelvárás”), és melléknév előtt nem állhat jelzőként. Ez helyesírási hiba, nem stílus. Baseline ismeretlen. · javítási korlát: ahol a jelentés „alapszintű”, ne „alapvető” kerüljön a helyére, mert az „fundamentális”-ra tolja a jelentést. Különösen a HUB:77 „alap gyermekvédelmi logika jelzésszinten” → „alapszintű”. A HUB:22-ben elég a legkisebb módosítás („alapelvárásokat”). A kompetenciák tartalma és számozása nem változik, a :38 és a :159 együtt mozog. Az M0.2:141 `@asset`-metaadat módosítása után media_manifest build kell.

Összesítés: 5 MEGERŐSÍTVE (G1-2, G1-5, G1-6, G1-8, G1-11), 4 ELVETVE (G1-3, G1-4, G1-9, G1-10), 2 EMBERI DÖNTÉS (G1-1, G2-11). Bizonyíték-kapu típusú finding nincs; a G1-2 és a G1-8 javítása után a Memuna-QA viszont bizonyíték-kapuként függő marad. Duplikátum: NYELV-G1-1 = NYELV-G2-11 (L1), a megtartandó a NYELV-G2-11, kiegészítve a G1-1 M0.2:26 és HUB:144 helyével.

Hivatkozott fájlok:
- 02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md (:27, :203, :219)
- 02 Tervezet/Gyermekvédelem – release gate.md (:80)
- 02 Tervezet/Média-assetek/VOICE-BIBLE.md (:135)
- 01 Fejlesztés/04 Audit/2026-10-04 Projektgazdai döntések – M6 nyelvi review.md (M6-NY-D9)

## VERIFIER V2 — NYELV-G1-7, G1-12…20, NYELV-G2-17, G2-18, G2-21 (13 ID)

AP-2026-10-11-01 · M0 nyelvi lencse · adverzális verifikáció, 13 finding (L2, L3 és szóló tételek). Read-only, fájlt nem módosítottam. Baseline mindenhol ismeretlen, mert git-history nincs. Ezért egyik súlyosság sem emelkedett.

Forrás: `01 Fejlesztés/04 Audit/2026-10-11 Validált findingok – M0, nyelvi lencse, AP-2026-10-11-01.md`, C. melléklet. Minden helyet a jelenlegi fájlokban olvastam vissza: HUB, M0.1, M0.2, M0.3, M0.A és Z.A (`02 Tervezet/Modulok/M0/…`, `02 Tervezet/Modulok/Z/Peulák/Z.A – …`). A webes ellenőrzés eredménye: az AkH 12. 139. pontját a helyesiras.mta.hu-n szó szerint ellenőriztem: „A két egyszerű közszóból alakult alárendelő összetételeket (akárhány szótagból állnak is) egybeírjuk”. A 245. pont (vessző a „mint” előtt) WebFetch-csel nem volt elérhető, ott a közismert szabályra támaszkodtam.

NYELV-G1-7 · MEGERŐSÍTVE · objektív · P2 · Az M0-on belül két írásmód él: a HUB:145/247/249 és a Glosszárium:143 „peulaterv(ezés)”-t ír, a leckék „peula-terv(ezés)”-t (M0.1:198, :298; M0.2:279; M0.3:254, :292). Az M0.2:142 asset-spec „peula/Zmán Kvuca” alakja ellentmond a Glosszárium:101 „egységesen `Zmán Kvucá`” előírásának. · duplikátum: nincs (az M0.2:279 sort a G1-12 is érinti, de más szót javít) · javítási korlát: a 6. item projektgazdai szövege nem változik. Az M0.2:142 csak a `media_manifest build` úton módosulhat. A más modulokban maradó kb. 22 kötőjeles alak nem ennek a scope-nak a része.

NYELV-G1-12 · MEGERŐSÍTVE · objektív · P2 · Kéttagú köznévi összetételről van szó, ezért az AkH 139. szerint egybeírandó. A különírt vagy kötőjeles alak mellett ugyanabban a fájlban, sőt ugyanabban a sorban ott a helyes alak is: M0.3:235 „célkörnyezetben” ↔ „cél-környezetben”; M0.3:241 „kapulogika” ↔ M0.2:279 „kapu-logika”; M0.2:251, M0.3:278 „célverzió” ↔ M0.1:59, M0.2:62, M0.3:59 „cél verzión”. · duplikátum: nincs · javítási korlát: csak az írásmód változik. A „cél verzión” az M0.4:61-ben is előfordul (a G2 csoportban kimaradt), az M0-n belüli egységességhez ott is javítandó. Az M0.2:141 és az M0.3:102 `@asset`-metaadat csak a build úton módosulhat.

NYELV-G1-13 · MEGERŐSÍTVE · objektív · P2 · Az M0 egészében csak a HUB:275 „elakadnak M0.3-nál” és a HUB:283 „nem „complete” M0-ban” áll névelő nélkül, minden más helyen névelővel szerepel az azonosító („az M0-n belül”, :281). Az angol „complete” stábszövegben nem UI-elem. · duplikátum: nincs · javítási korlát: a >30%-os küszöb és az „első hét” nem változik.

NYELV-G1-14 · EMBERI DÖNTÉS · emberi-döntés · P2 · A HUB:180 szerint az itemszöveg és a kulcs projektgazdai szöveg (2026-10-02). A 7. item „a completion állapotát” (HUB:254) különírása valós helyesírási hiba, mert idegen írásmódú előtag után kötőjel kell. A 4. itemnél állított alanykétértelműség („Automatikusan megfelel”) gyenge. Mindkét javítás projektgazdai szöveghez nyúlna, a C) ✅ opció szövegéhez („completion-státusszal”) is. · duplikátum: nincs (rokon tétele az ERT-4) · javítási korlát: a projektgazda döntsön az értékelési felelős QA-jával. A ✅, a kulcs és a disztraktorok tartalma nem változhat.

NYELV-G1-15 · MEGERŐSÍTVE · objektív · P2 · A HUB:59 „szerepek, elvárások, dugma isit alapok” eltér a HUB:72 fejléctől, a HUB:293 linkcímkétől és az M0.2:6 tanulói címtől („Madrih, nem terapeuta – szerepek és elvárások”). Ugyanaz a lecke a HUB-on belül két címen fut. · duplikátum: nincs · javítási korlát: csak a :59 mapping-sor változik, a fájlnév és a link nem.

NYELV-G1-16 · ELVETVE · objektív · P2 · A HUB:125 „1–1-ben vagy kis csoportban” állítását nem tartom bizonyítottnak. A nagykötőjel az AkH szerint nemcsak tartományt jelöl, hanem viszonyt is (vö. HUB:88 „fogalom–definíció”), és a „vagy kis csoportban” egyértelművé teszi a jelentést. Az „értelmetlen” minősítés túlzó, a csere preferencia. · duplikátum: nincs · javítási korlát: a felnőtt és az esetleg kiskorú madrih egyéni helyzetének kérdése nem nyelvi kérdés, ez a finding nem dönti el.

NYELV-G1-17 · ELVETVE · objektív · P2 · A M0.3:12 fő állítása technikailag hamis. A belső `**felirat kötelező**` CommonMark szerint beágyazott strong lesz, így a kulcsszó is félkövér marad, nem fordul meg a hangsúly. A záró mondat („A tanulási cél így sem érhető el kizárólag hang/kép útján.”) érthető normaként, az átírása preferencia. · duplikátum: nincs · javítási korlát: ha valaki mégis hozzányúl, az akadálymentességi kikötés tartalma (alt-szöveg, SC 1.2.2, SC 1.2.1) nem gyengülhet.

NYELV-G1-18 · ELVETVE · objektív · P2 · Az M0.1:59 és az M0.2:62 alanya („A SLIDE 1, a SLIDE 6 és a SLIDE 7 szöveges lépése”) jelentésében többes. A mondat maga is többes számban folytatódik („hozzájuk”), és a többes számú névszói állítmány („nem completion-feltételek”) magyarul elfogadható. A jelentés nem torzul, a javaslat a „hozzájuk”-ot is meghagyná, így a csere preferencia. · duplikátum: nincs (a „cél verzión” a G1-12-ben marad).

NYELV-G1-19 · ELVETVE · objektív · P2 · A HUB:281 „„kihez jelzek?”” informális címke, de a 2. itemre egyértelműen ráismerni. A „vagy”-gyal összekötött két itemre a többes számú „itemeket” is helyes, tehát az „itemet”-javítás indoka téves. A finding bizalma alacsony, a javítás preferencia. · duplikátum: nincs.

NYELV-G1-20 · ELVETVE · objektív · P2 · Az M0.2:504 „nem marad meg az online leckében” bevett szerkezet, vö. „nem marad meg az elmélet szintjén”. A szándékolt jelentés („nem korlátozódik rá”) a kettőspont utáni „is”-szel egyértelmű. A finding bizalma alacsony, a javítás preferencia. · duplikátum: nincs.

NYELV-G2-17 · MEGERŐSÍTVE · objektív · P2 · A M0.A:474 (a finding :475-öt ír, a sorszám eggyel elcsúszott, de az idézet egyezik) „**ÉN, mint madrih**”, a :481 „**téged, mint képzőt**” és a :196 asset-spec „ÉN, mint madrih” mind -ként jelentésű „mint”. Ilyen „mint” elé az AkH 12. 245. szerint nem kell vessző. · duplikátum: nincs · javítási korlát: csak a vessző törlendő. A nagybetűsítés nem változik: „ÉN mint madrih”. A javasolt „ÉN MINT MADRIH” túllépne a vesszőhibán. A :196 csak a build úton módosulhat, a látható szöveg miatt pin kell.

NYELV-G2-18 · MEGERŐSÍTVE · objektív · P2 · Minden felsorolt hely egyezik (M0.A:40, :366, :367, :629, :170, :174, :264, :268, :286, :321; :502, :657, :168, :170, :288; :427, :385; :129, :639, :102; Z.A:55, :423, :440, :458). Ezek kéttagú köznévi összetételek, az AkH 139. szerint egybeírandók. Egybeírt alak a korpuszban egyszer sem fordul elő, ez tehát egységes hiba, nem írásmód-ingadozás. · duplikátum: nincs · javítási korlát: az „induló-szó” alakja a javítónak választandó, és a M0.A-ban, a Z.A-ban és az assetekben egyformán kell végigvinni. A lista kihagyta a M0.A:174 „Induló-szavak – M0.A” címét és a :180 „induló-szó-rögzítést”. A héber tagú konvenciós alakok (kvuca-plakát, madrih-szerep) maradnak. Az asset-specek csak a build úton módosulhatnak.

NYELV-G2-21 · MEGERŐSÍTVE · objektív · P2 · A felolvasandó idézetekben perjel áll: M0.A:355 „Írjatok / rajzoljatok”, :426 „a stáb / program”, :594 „kérdés / bizonytalanság”, :598 „laptoppal / telefonnal”, „Moodle / H5P”. Ez sérti a `.claude/rules/hungarian-editorial.md`:37 normáját („`+`, `/` … helyett rendes mondat”). · duplikátum: nincs (a G1-8-cal egy klaszter, de más helyek) · javítási korlát: a :594 a nyomtatott kilépőkártya kérdése, és ugyanez a szöveg áll az M0.A-MUNK-02 spec :520 sorában. Vagy mindkettő változik (build és pin), vagy egyik sem, különben szétválik a felolvasott és a nyomtatott szöveg (7. regressziós minta). A :422/:423 oszlopfejlécek maradnak.

Összesítés: 7 MEGERŐSÍTVE (G1-7, G1-12, G1-13, G1-15, G2-17, G2-18, G2-21), 5 ELVETVE (G1-16, G1-17, G1-18, G1-19, G1-20), 1 EMBERI DÖNTÉS (G1-14). Bizonyíték-kapu: 0. Duplikátum: nincs. Átfedés van a G1-12 és a G1-18 között a „cél verzión” helyen, és a G1-7 és a G1-12 között az M0.2:279 soron, de mindkét esetben más szót javítanak.

## VERIFIER V3 — NYELV-G2-1…10, G2-12…16, G2-19, G2-20, G2-22 (18 ID)

Verifier-verdiktek: M0 nyelvi lencse, G2 (M0.4, M0.A), AP-2026-10-11-01. Read-only, fájlt nem szerkesztettem. A baseline mind a 18 tételnél ismeretlen (nincs git-history), ezért egyik súlyosság sem emelkedett.

Forrásfájlok:
- 02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md
- 02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md
- Összevetve: 01 Fejlesztés/04 Audit/2026-10-10 Validált findingok – M0 course-review, B sáv.md; Glosszárium :27, :155, :164–169; M0 hub :131–148; Emberi jóváhagyás szükséges.md :139–147

- NYELV-G2-1 · MEGERŐSÍTVE · objektív · P2 · Egy percbontás-listán belül két címkerendszer áll („**10–25’** – 1. fő tevékenység” :147 és „**40–55’** – Blokk 4” :149). A „Kihez fordulhatok” :152-ben és :647-ben kérdőjel nélkül áll, a :156 és a 4.4 viszont „Kihez fordulhatok?” alakot használ. · duplikátum: nincs · javítási korlát: a finding „a blokkcímek is eltérnek” állítása nem áll meg, mert a „Mit várunk, mit hozunk?” (Blokk 2) és a „Mit várunk, mit vállalunk?” (Blokk 3) két különböző blokk címe, nem ellentmondás. Csak a címkék egységesítése és a „?” pótlása a javítás; a percek és a leírások maradnak. A 45’-es percbontásnál sorrendi függés van a PED-5-tel (ő bontja lépésszintre): egy lépésben, a PED-5 után vagy vele együtt.
- NYELV-G2-2 · ELVETVE · objektív · P2 · A „nem csak peulán találkoznak veled.” „hanem” nélkül szabályos különírás, utána diaszövegben bevett felsorolás következik. A „kiesett hanem” exportmaradvány volta feltételezés, baseline nélkül nem bizonyítható; ez stílus-preferencia (2026-10-10, 5. pont). · duplikátum: nincs · javítási korlát: —
- NYELV-G2-3 · MEGERŐSÍTVE · objektív · P2 · A lecke két különböző csoportot hív kvucának: a :146 „(a kvucád tagjai, akiket vezetsz)” (vö. :158, :222, :417 is a hanihok csoportja) a :554-ben „a kvucáddal élőben a kickoff-peulán találkoztál” már a képzős csoport. A fórum láthatóságának megértését ez érdemben zavarja. · duplikátum: nincs (a G2-19-cel csak klasztertárs, L5) · javítási korlát: csak a minimális jelölés („a képzős kvucáddal”) fér bele. Sorrendi függés: a validált PED-10 ugyanezt a mondatot feltételesre írja át, ezért a kettő egy lépésben menjen; a PED-10 utalása a „Segítség és kapcsolatok” blokkra maradjon meg.
- NYELV-G2-4 · MEGERŐSÍTVE · objektív · P2 · A :636 „Megvan a mondat:” a 2.3-ban előkészített mondatra utal, de mást idéz („fájdalmas” a :90 „nagyon személyes” helyett, „most” nélkül). Az M0.A-KART-02 spec (:58) maga rögzíti, hogy „a változatok még nincsenek egységesítve”. · duplikátum: nincs · javítási korlát: a :636 a :90 első mondatát vegye át szó szerint (ezt idézi a KART-02 is), új szöveg nincs. A :58 megjegyzéséből csak az ellenőrző listára vonatkozó rész kerül ki; a Blokk 2 (:342) változata marad. Asset-spec változik, ezért `media_manifest build` kell külön `chore(media)` commitban, utána pin.
- NYELV-G2-5 · MEGERŐSÍTVE · objektív · P2 · A :638 „(közvetlen veszélynél előbb a 112)” az 5. lépés csonka változata. A kánoni formula (:93, :137, Glosszárium :164: „Közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés”) szerint a Glosszárium :166 kimondja: „Négylépéses, csonka vagy versengő változat nincs.” A kánoni mondat szó szerinti visszaállítása a HUM-SAFE-01 projektgazdai döntés (Glosszárium :169) átvezetése. · duplikátum: nincs · javítási korlát: csak a zárójel tartalma cserélődik a formulára, betű szerint (HUM-SAFE-01). A 2.4 mini-protokoll (:129–140) és az ellenőrző lista többi része nem változik, új tartalom nem kerülhet be. Látható szöveg, ezért pin kell.
- NYELV-G2-6 · MEGERŐSÍTVE · objektív · P2 · A :610 „Ha az áttekintő több peula-szerű elemre utal” mondatban az „áttekintő”-nek nincs előzménye a fájlban. A tényleges forrás a modul-áttekintő hub, ahol a :12 és a :117 a technikai segítségpontot külön elemként tárgyalja. · duplikátum: nincs · javítási korlát: csak az előzmény megnevezése a javítás („az M0 modul áttekintője”). A „szándékoltan → szándékosan” csere elvetendő, mert a „szándékoltan” helyes magyar szó. A főnévtorlódás felbontása preferencia, ez is elvetendő. Új magyarázat nem kerülhet be.
- NYELV-G2-7 · ELVETVE · objektív · P2 · A :367 látható attribúciója („projektgazdai döntés, 2026-10-02; utólagos ellenőrzés (vétó/QA): a DPO”) korpusz-szintű konvenció: 15 modulfájlban 21-szer fordul elő. A finding saját feltétele szerint ilyenkor ez a rész elvetendő. A :366 „alapút” és a :502 „Z-oldalon” érthető, ezek cseréje preferencia. · duplikátum: nincs · javítási korlát: a :366-ra javasolt csere rontana. A HUM-PRIV-02 általános mondata („ne gyűjts felvételt, ha…”) nem mondja ki, hogy a plakát fizikai megőrzése az alapértelmezés, így a konkrét kikötés elveszne. Az adatvédelmi kikötés egyik eleme (alapértelmezés, kitakarás, hozzájárulás, 90 nap, törlés) sem változhat.
- NYELV-G2-8 · ELVETVE · objektív · P2 · A :351 „A plakát három részre osztva (…). Instrukció:”, a :360 „kirakjátok” és a :442 töredéke a képzői forgatókönyv bevett távirati stílusa. A „ti” megszólítás képzőt és csoportot együtt szólíthat meg, ez nem bizonyított hiba. Az E/2 és T/3 szerinti átírás tömeges stílusátírás volna (2026-10-10, 5. pont). A :348 „mindenét” javítása gyanú, nem bizonyíték. · duplikátum: nincs · javítási korlát: —
- NYELV-G2-9 · ELVETVE · objektív · P2 · A „jelen lenni” mentális jelenlét értelmében magában az M0.4-ben is kánoni alak („online is dugma isitként jelen lenni”, :18, :39, :518), így a :506 nem jelentéshiba. A javasolt „figyelmesen részt vettetek” értelmezést tenne hozzá. A :248 „tedd minimálissá a tétet” érthető, a csere preferencia. · duplikátum: nincs · javítási korlát: —
- NYELV-G2-10 · ELVETVE · objektív · P2 · A szerkesztői szabály a bevett pedagógiai szakszót megengedi, és a Glosszárium :155 maga is szinonimaként adja a „(bullying)”-t. A kulcs nélküli véleményopcióban („Szívatás / bullying chatben”) a „kortárs bántalmazás” az M3-ban szigorú kritériumokkal (célzott, ismétlődő, erőfölény) definiált fogalmat tenné a „szívatás” mellé, ez jelentéseltolás. · duplikátum: nincs · javítási korlát: —
- NYELV-G2-12 · MEGERŐSÍTVE · objektív · P2 · A :565 fórumleírás kérdéslistájában az utolsó pont felszólítás („Írj egy szót, ami eszedbe jut…”), a SLIDE 6 (:482–486) kérdései pedig eltérnek tőle („vagy a képzésben”, „szeretnél jelen lenni”). Ez párhuzamossági hiba, és a 7-es minta szerinti széttartás. · duplikátum: nincs · javítási korlát: a javaslat iránya („a :565 vegye át szó szerint a SLIDE 6-ot”) nem használható. Az utolsó pontba a G2-11 által vitatott „dugma isit vagy” alakot vinné be, holott a :565 alakja a Glosszárium :27-hez igazodik (vö. :18, :518). A „vagy a képzésben” iránya nem dönthető el, ezért marad. Most csak a :565 utolsó pontja kerüljön kérdő formába a mostani szóhasználattal; a SLIDE 6-tal való teljes összhang a G2-11 döntése után jöhet. A :486 „Mi az az egy szó” részt elvetem (nem bizonyított). A BIZT-8 láthatósági mondatához és az IMPL-7 névalakjához nem nyúlhat.
- NYELV-G2-13 · ELVETVE · objektív · P2 · A hub maga is „komment”-nek hívja a fórumválaszt: HUB :136 „1 rövid komment legalább 1 másik résztvevő posztjára”. A lecke-komment összekeverése feltételezés. A teljes feltétel ugyanazon a dián szerepel (:524), a :549 a záró mondat rövidítése. · duplikátum: nincs · javítási korlát: —
- NYELV-G2-14 · MEGERŐSÍTVE · objektív · P2 · A :552 „belépő-jelző” alkalmi képzés, kötőjellel hibásan írt összetétel. A kánoni alak a HUB :131 „belépő jellegű, nem vizsga”. · duplikátum: nincs · javítási korlát: a javasolt mondat („azt jelzi a stábnak, mennyire sikerült belépned”) rontana, mert tanulónak szóló, egyéni szintű adatláthatósági állítást tenne. A HUB :148 szerint a stáb-jelzés átlag és témakörszintű, az egyéni válaszok láthatósága pedig a nyitott PED-8 (DPO) kérdése. Csak a HUB :131 „belépő jellegű” alakja vehető át szó szerint. A „Csak arra figyelj, hogy mind a 7 kérdésre válaszolj.” mondat marad (ERT-2), utána pin kell.
- NYELV-G2-15 · ELVETVE · objektív · P2 · A jelen idő jövő jelentésben szabályos magyar szerkezet (:16 „A peula végére … van egy első közös élményetek”). A :18 „Elhangzanak közösen” érthető, és a javasolt T/1 („Közösen kimondjuk”) sem hozná vissza az E/2-es párhuzamot. Ez stílus-preferencia. · duplikátum: nincs · javítási korlát: —
- NYELV-G2-16 · MEGERŐSÍTVE · objektív · P2 · Idézőjeles névnél a toldalék az idézőjelen belülre került: :501 „a „Bemutatkozó falon””, a :505 diacím „„Bemutatkozó falra””, :525 „„M0 belépőkvízt””. Ugyanez a fájl a :48, :522 és :540 helyen a helyes formát használja („„Bemutatkozó fal” fórumot”). · duplikátum: nincs (az IMPL-7-tel részben átfed: a névalak az övé, ez a finding csak a toldalék helyéről szól) · javítási korlát: csak a toldalék helye változik. Sorrendi függés: a :501 láthatósági tartalmát a BIZT-8 írja át, ezért egy lépésben menjen. A :525 névalakja az IMPL-7 egységesítését követi, előbb az IMPL-7 dönti el az irányt. A „Bemutatkozó fal” activity-név nem változhat. Látható szöveg, utána pin kell.
- NYELV-G2-19 · ELVETVE · objektív · P2 · A :325 „ezekben közös, hogy” a szabályos „közös bennük, hogy” szórendi változata, nem hiba. Ráadásul a validált ERT-1/K1 helyzetenként szétbontja ezt a visszajelzést, így a mondat megszűnik, és a :309–333 a BIZT-3 Memuna-döntése alatt áll. A :470 fejlesztői célszöveg, a köznyelvi „hogy” nélküli célhatározó elfogadható. A :358 „az egy-egy” árnyalati kérdés, nem bizonyított hiba. · duplikátum: nincs · javítási korlát: a :325-höz az ERT-1/K1 előtt és attól függetlenül nem szabad nyúlni.
- NYELV-G2-20 · ELVETVE · objektív · P2 · A finding maga is alacsony bizalmú, és elismeri az érvényes olvasatot: a kötőmódú „jelezhetsz, hogy beszéljünk” kérés vagy célhatározó olvasatban alanyi ragozással is szabályos (:90). Ez nyomtatott biztonsági kártyamondatot (KART-02, :58) írna át bizonytalan haszonért. · duplikátum: nincs · javítási korlát: —
- NYELV-G2-22 · EMBERI DÖNTÉS · emberi-döntés · P2 · A :347 „vagy páratlan a létszám” feltétele nem következik a :344 „3–5 fős csoportokba” szabályából (7 vagy 9 főnél két csoport is kijön). A szándék a repóból nem dönthető el, a javításhoz pedig új pedagógiai tartalom kellene. · duplikátum: nincs · javítási korlát: a modulgazdának vagy a projektgazdának kell megmondania, mit jelent a feltétel; addig nem írható át, és magyarázat sem található ki rá (8-as minta). Alacsony tét, mert az „akár” opcionálissá teszi.

Összesítés (18 tétel):
- MEGERŐSÍTVE: 8 (G2-1, G2-3, G2-4, G2-5, G2-6, G2-12, G2-14, G2-16)
  - ebből a javaslat szűkítendő vagy részben nem használható: G2-1, G2-6, G2-12, G2-14
  - sorrendi függés: G2-1 → PED-5; G2-3 → PED-10; G2-16 → BIZT-8 és IMPL-7; G2-12 → G2-11 döntése, BIZT-8 és IMPL-7
- ELVETVE: 9 (G2-2, G2-7, G2-8, G2-9, G2-10, G2-13, G2-15, G2-19, G2-20)
- EMBERI DÖNTÉS: 1 (G2-22)
- bizonyíték-kapu: 0
- Duplikátum: nincs. Részleges átfedések, nem duplikátumok: G2-16 ↔ IMPL-7 (a névalak az IMPL-7-é), G2-3 ↔ PED-10 (ugyanaz a mondat, egy lépésben), G2-12 ↔ G2-19 (a :486; a G2-19 elvetve).

---

# C. melléklet – nyers lencse-kimenetek (szó szerint)

## LENCSE: NYELV — G1 (hub, M0.1, M0.2, M0.3)

## NYELV lencse — M0, G1 fájlcsoport (AP-2026-10-11-01, `next-version`), read-only

**Fájlok** (a Hely mezőben rövid névvel, a szám a fájl sora):
- HUB = `02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md`
- M0.1 = `02 Tervezet/Modulok/M0/Online leckék/M0.1 – Üdv a képzésben! – Éves útiterv & mi köze hozzám.md`
- M0.2 = `02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrih, nem terapeuta – szerepek és elvárások.md`
- M0.3 = `02 Tervezet/Modulok/M0/Online leckék/M0.3 – Hogyan működik a Moodle, H5P és a kapu.md`
- Glosszárium = `02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md`; GK = `02 Tervezet/Gyermekvédelem – release gate.md`

**Előzetes megjegyzések:**
- Régi írásmódra (madrich, chanich, hagshama, dugma ishit, Leviatan) az M0-ban 0 a találat, ilyen regresszió nincs.
- A B sáv validált M0-findingjait nem ismétlem. Ahol egy nyelvi javítás érint egy validált tételt (ERT-1, ERT-4, IMPL-7, BIZT-1), jelzem.
- Pilot-besorolást nem adok.
- `@source`/VO-szövegben nem találtam nyelvi hibát. Az M0.2:141–142 és az M0.3:102 `@asset`-metaadat, nem `@source`.

---

**NYELV-G1-1**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M0.2:26 (Központi mondat); HUB:238 (5. item, B visszajelzés, szerkesztői kiegészítés); HUB:144 (kvízleírás, 5. item)
- **Probléma:** A dugma isit megszemélyesítve áll („dugma isit vagy”, „egy dugma isit madrih”), pedig a Glosszárium ezt kifejezetten kerülteti. Az M0.2:26-ban emiatt a glossza után álló „aki” egy elvont főnévre mutat: „személyes példamutatás, aki példát mutat”.
- **Bizonyíték:** M0.2:26 „Nem terapeuta vagy, hanem *dugma isit* (‘személyes példamutatás’), aki példát mutat, észrevesz…”; Glosszárium:27 „A megszemélyesített „Dugma Isitnek lenni” formát **kerüld** – helyette: „dugma isitként viselkedni””
- **Hatás:** A lecke kulcsmondata önmagába fordul: a példamutatás „mutat példát”. A tanuló a Glosszárium által elvetett szerepképet tanulja. Valószínűleg a glossza utólagos beszúrásának nyoma (3. regressziós minta, névmási zuhanás).
- **Javaslat:**
  - M0.2:26 → „Nem terapeuta vagy, hanem madrih, aki *dugma isitként* (‘személyes példamutatás’) viselkedik: példát mutat, észrevesz, tartja a kereteket, és jelzi, ha bajt lát.”
  - HUB:238 → „Nem jó: privát üzenetben is dugma isitként viselkedsz, és amit…”
  - HUB:144 → „…illik egy **dugma isitként** viselkedő madrihhoz…”
  - Korlát: a négy ige és a glossza marad, új tartalom nem kerül be. Az 5. item projektgazdai törzse („Melyik online reakció dugma isit?”) és a kulcs nem változik. A HUB:238 az értékelési felelős QA-ja alá esik. Látható szöveg változik → pin.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-2**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M0.2:342 (SLIDE 4, a jelzési út 1. lépésének alsora, diaszöveg)
- **Probléma:** A „-nak/-nek” vonzat („furcsának látok”) csak a „lát” igével áll, a „hall” igével nem, ezért a „látok / hallok” fele nyelvtanilag hibás.
- **Bizonyíték:** M0.2:342 „> Valamit furcsának, ijesztőnek, zavarónak látok / hallok.”
- **Hatás:** A gyermekvédelmi jelzési út első lépésének magyarázata döccen. A perjelet a képernyőolvasó külön felolvassa.
- **Javaslat:** „Valami furcsát, ijesztőt vagy zavarót látok vagy hallok.” Korlát: a :341 lépéscím, az öt lépés sorrendje és szövege, az M0.2-DIA-01 spec és a HUB:147 lépésleírás változatlan. Memuna-QA hatály (G1, vö. BIZT-1). Látható szöveg → pin.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-3**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M0.2:430–431 (SLIDE 5, „Csoportchatben / online” példák, diaszöveg)
- **Probléma:** Két hiba:
  - A :430 tettet („csinálok”) köt felolvasáshoz.
  - A :431 „nem …-ról, hanem …-n” szerkezete nem párhuzamos, és a „fiókomról írok” úgy is érthető, hogy a fiókomról mint témáról írok.
- **Bizonyíték:** „– nem csinálok olyat privátban, amit szégyellenék nagykörben is felolvasva,” / „– hanihnak nem a személyes közösségimédia-fiókomról írok, hanem a szervezet csatornáján.”
- **Hatás:** A két online szabály homályosabb, mint a korpusz többi megfogalmazása (HUB:238: „amit nem olvasnál fel nagykörben, azt privátban se írd le”). Az egyik a HUM-SAFE-02 csatornaszabálya.
- **Javaslat:**
  - :430 → „– nem írok privátban olyat, amit szégyellenék nagykörben felolvasni,”
  - :431 → „– hanihnak nem a személyes közösségimédia-fiókomon, hanem a szervezet csatornáján írok.”
  - Korlát: a csatornaszabály tartalma (szervezeti csatorna, nem személyes fiók) változatlan, Memuna-QA hatály. Ha a „csinálok” szándékosan a nem írásos viselkedést is lefedi, a :430-hoz ne nyúlj, hanem jelezd. Látható szöveg → pin.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-4**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M0.1:382 (SLIDE 6, Instrukció, tanulói szöveg)
- **Probléma:** Három, eltérő alanyú tagmondat áll vesszővel összefűzve, és a „csak legyen őszinte” a tegező szövegben magázó felszólításként is olvasható („Legyen őszinte!”).
- **Bizonyíték:** M0.1:382 „Írj 2–4 mondatot, nem fogalmazásverseny, csak legyen őszinte.”
- **Hatás:** A tegező lecke ezen a ponton magázásba csúszik (6. regressziós minta), és a mondatot nehéz felolvasni.
- **Javaslat:** „Írj 2–4 mondatot. Ez nem fogalmazásverseny, csak őszintén írj.” Korlát: a 2–4 mondat és a tanuló-lokális státusz (D-4) változatlan. Látható szöveg → pin.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-5**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M0.2:40 (Moodle-intro, tanulói szöveg)
- **Probléma:** A „más … felelőssége” birtokos szerkezetet egy húszszavas, gondolatjeles betoldás szakítja szét, így a mondat vége elszakad a birtokostól.
- **Bizonyíték:** M0.2:40 „(hanem más – egy szakember, a ken-vezető, gyermekvédelmi ügyben pedig a kijelölt **Memuna**, a Somer gyermekvédelmi felelőse – felelőssége).”
- **Hatás:** A lecke első tanulói mondata, amely a szerephatárt kimondja, csak második olvasásra érthető.
- **Javaslat:** két mondat: „…és **mi az, ami már nem a te dolgod egyedül**. Ezekért más felel: egy szakember, a ken-vezető, gyermekvédelmi ügyben pedig a kijelölt **Memuna** (a Somer gyermekvédelmi felelőse).” Korlát: a három szereplő és az „egyedül” megmarad. A Memuna a GK:80 első-előfordulási formulájával áll. Látható szöveg → pin.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-6**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M0.2:279 (SLIDE 3, fejlesztői megjegyzés)
- **Probléma:** Két szóhiba:
  - A korpusz terminusa a „fejlesztő visszajelzés” (formatív), itt viszont „fejlesztői visszajelzés” (a fejlesztőé) áll.
  - „Az 1. helyzet … kisebb tét” egy helyzetet téttel azonosít.
- **Bizonyíték:** M0.2:279 „A fejlesztői visszajelzés ezt a 2. helyzetet emelje ki”; „Az 1. helyzet (peula-tervezés) tudatosan kisebb tét”
- **Hatás:** A fejlesztői blokkban a megvalósító a saját visszajelzésének értheti azt, ami a tanulónak szóló H5P-visszajelzés. A tananyagban a „fejlesztő visszajelzés” 21-szer fordul elő, a „fejlesztői” csak itt.
- **Javaslat:** „A fejlesztő visszajelzés ezt a 2. helyzetet emelje ki”; „tudatosan kisebb tétű”. Korlát: a megjegyzés szabálytartalma (a 2. helyzet kiemelése, a „köztünk marad” disztraktor) változatlan. Az ERT-1 Q2-javításával érdemes egy menetben elvégezni.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-7**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv (D10 terminológia)
- **Hely:** M0.1:198, :298; M0.2:279; M0.3:254, :292 („peula-terv/-tervezés”); M0.2:142 (`@asset`-metaadat, nem `@source`: „Zmán Kvuca”)
- **Probléma:** Ugyanaz a fogalom az M0-n belül kétféle írásmóddal áll: a HUB és a Glosszárium „peulaterv(ezés)”-t ír, a leckék „peula-terv(ezés)”-t. Az M0.2 asset-specifikációja a Glosszárium egységes „Zmán Kvucá” alakjától is eltér.
- **Bizonyíték:** M0.1:198 „→ peula-tervezés, Zmán Kvucá, AI-támogatás” ↔ HUB:249 „peulatervezés → M7 ✅”; Glosszárium:101 „**egységesen `Zmán Kvucá`** … ne bontsd meg.”
- **Hatás:** A 6. kvízitem az M0.1 SLIDE 2 idővonalára épül, mégis más írásmóddal nevezi meg ugyanazt a témát. Az asset-specből az elvetett alak a diagramfeliratba kerülhet.
- **Javaslat:**
  - Kötőjel nélkül: „peulatervezés” (M0.1:198, M0.2:279), „peulaterv” (M0.1:298, M0.3:254), „peulatervedet” (M0.3:292).
  - M0.2:142 → „Zmán Kvucá”.
  - Korlát: a 6. item projektgazdai szövege már egybeírt, nem változik. Az asset-metaadat módosítása után media_manifest build. Látható szöveg → pin.
  - Megjegyzés: a korpusz más moduljaiban (M5, M7, Program terv) további kb. 35 kötőjeles előfordulás van, az a saját scope-juk feladata.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-8**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M0.2:260 (SLIDE 3, 2. kérdés ✅ opció); M0.3:302 (SLIDE 6, 3. kérdés törzse); M0.3:312 (SLIDE 6 visszajelzés)
- **Probléma:** Kérdésszövegben, válaszopcióban és visszajelzésben teljes mondaton belül nyíl és pluszjel áll a kötőszó helyett.
- **Bizonyíték:** M0.2:260 „B) **Nem maradok egyedül → azonnal bevonom a Memunát** ✅”; M0.3:302 „„Egy H5P-leckét elkezdesz, de félúton kilépsz → nincs pipa.””
- **Hatás:** A képernyőolvasó a jelet a nevén olvassa fel („jobbra mutató nyíl”), így a gyermekvédelmi kulcsopció mondata széttörik. A szerkesztői norma szerint a `+`, `/` és hasonló jelek helyett rendes mondat kell.
- **Javaslat:**
  - M0.2:260 → „Nem maradok egyedül: azonnal bevonom a Memunát”
  - M0.3:302 → „…félúton kilépsz, ezért nincs pipa.”
  - M0.3:312 → „**jelzés és támogatás**”
  - Korlát: a ✅ helye és az opciók jelentése változatlan. Az M0.2 2. kérdése Memuna-QA hatály alá esik. A diák leképező listái (M0.1:184–200, M0.3:158–160) maradnak. Látható szöveg → pin.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-9**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M0.3:233 (SLIDE 4 visszajelzés)
- **Probléma:** A „technikai szavak alapjai” értelmetlen birtokos szerkezet, hiszen a szavaknak nincs „alapja”. A mondat az alapfogalmak elsajátítását akarja kimondani.
- **Bizonyíték:** M0.3:233 „akkor a technikai szavak **alapjai már megvannak**.”
- **Hatás:** A párosítás utáni megerősítő visszajelzés döccen, és nem kapcsolódik a dia címéhez („Alapfogalmak”, :174).
- **Javaslat:** „akkor a technikai **alapfogalmak már megvannak**.” Korlát: a visszajelzés többi része változatlan. Látható szöveg → pin.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-10**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** M0.3:180 (SLIDE 3, diaszöveg); HUB:48 (2. szakasz, 5. kompetencia)
- **Probléma:** A tanulói diaszövegben exportból maradt, escape-elt angol „drag\&drop” áll, a HUB kompetencialeírásában pedig „social media”, holott a korpusz mindkettőre magyar szót használ.
- **Bizonyíték:** M0.3:180 „(kattintós videó, kvíz, drag\&drop stb.).”; HUB:48 „(Moodle, csoportchat, social media)” ↔ M0.2:431 „közösségimédia-fiókomról”
- **Hatás:** Ha a nyers szöveg bekerül a H5P-be, a visszaper is megjelenhet. Ugyanarra a műveletre a tanuló két szót lát (M0.3:213: „húzással”).
- **Javaslat:** M0.3:180 → „(kattintós videó, kvíz, húzásos feladat stb.)”; ha a terméknév marad, escape nélkül, „Drag & Drop” alakban. HUB:48 → „közösségi média”. Korlát: a H5P típusnevek a fejlesztői sorokban (pl. :11, :215) változatlanok. Látható szöveg → pin.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-11**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** HUB:22 (2×), :38 és :159 (kompetencianév és táblázatsor), :43, :77, :83, :109; M0.2:173; M0.2:141 (`@asset`-metaadat)
- **Probléma:** Az „alap” különírt melléknévként áll. Főnév előtt egybe kell írni („alapelvárás”), melléknév előtt „alapvető” vagy „alapszintű” kell, az „alap H5P-t” szerkezetből pedig hiányzik a fej (1. regressziós minta).
- **Bizonyíték:** HUB:22 „érti az alap elvárásokat és határokat …, megismeri az alap technikai eszközöket”; HUB:83 „megtanulja kezelni a Moodle-felületet, alap H5P-t”
- **Hatás:** Helyesírási hiba a modul kánoni áttekintőjében, miközben a scope-ban a helyes alak is szerepel (M0.3:174 „Alapfogalmak”, :254 „alapkvíz”).
- **Javaslat:**
  - HUB:22 → „az alapvető elvárásokat és határokat”, „az alapvető technikai eszközöket”
  - HUB:38 és :159 együtt → „Alapszintű technikai működés…”
  - HUB:43 → „alapszintű megértése”
  - HUB:77 → „alapvető gyermekvédelmi logika”
  - HUB:83 → „a Moodle-felületet és alapszinten a H5P-t”
  - HUB:109 → „az alapvető **biztonság és bizalom**”
  - M0.2:173 és :141 → „alapvető szereptisztázás”
  - Korlát: a kompetenciák tartalma és számozása változatlan; a :38 és a :159 együtt változik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-12**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:**
  - „szerep-tisztázás”: M0.2:141, :173
  - „kapu-logika”: M0.2:279
  - „kurzus-szerkezet”: M0.3:102, :139
  - „a cél verzión”: M0.1:59, M0.2:62, M0.3:59
  - „cél-környezetben”: M0.3:235
- **Probléma:** Kéttagú összetételek kötőjellel vagy különírva állnak, miközben ugyanebben a scope-ban egybeírva is szerepelnek.
- **Bizonyíték:** M0.3:235 „a célkörnyezetben **igazoltan húzásmentes**”, ugyanabban a sorban „a cél-környezetben ténylegesen húzásmentes-e”; M0.2:279 „kapu-logika” ↔ M0.3:241 „kapulogika”
- **Hatás:** A következetlenség fejlesztői szövegben áll, de látszik. A keresés (pl. „célverzió”) nem találja meg az összes előfordulást.
- **Javaslat:** egybeírva: „szereptisztázás”, „kapulogika”, „kurzusszerkezet”, „a célverzión”, „a célkörnyezetben”. Korlát: csak az írásmód változik. Az `@asset`-metaadat (M0.2:141, M0.3:102) módosítása után media_manifest build.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-13**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** HUB:275, :283 (6. szakasz, stábnak szóló szöveg)
- **Probléma:** A szemantikus azonosítók elől hiányzik a névelő („M0.3-nál”, „M0-ban”), és a teljesítést az angol „complete” jelöli.
- **Bizonyíték:** HUB:275 „(pl. elakadnak M0.3-nál, ahol több technikai elem van.)”; HUB:283 „a résztvevők **>30%-a nem „complete”** M0-ban:”
- **Hatás:** A stábnak szóló beavatkozási pont nehezebben olvasható, holott ugyanebben a szakaszban a helyes alak is szerepel („az M0-n belül”, :281).
- **Javaslat:** :275 → „elakadnak az M0.3-nál”; :283 → „a résztvevők **>30%-a nem teljesítette** az M0-t:”. Korlát: a 30%-os küszöb és az „első hét” időpont változatlan.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-14**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** HUB:223–230 (4. item); HUB:254, :260 (7. item törzse és kulcsa). Mindkettő projektgazdai itemszöveg (HUB:180).
- **Probléma:** Két nyelvi hiba a projektgazdai itemszövegben:
  - A 4. item törzsének alanya „egy éles kapu”, a válaszopciók alanya viszont kimondatlanul váltakozik: az A és a C a madrihra vonatkozik, a B („Automatikusan megfelel”) a kapura is érthető.
  - A 7. itemben ugyanaz a fogalom háromféle alakban áll.
- **Bizonyíték:** HUB:223/225 „Mi történik, ha egy éles kapu elsőre nem teljesül?” / „A) Kiesik a képzésből.”; HUB:254 „a completion állapotát” ↔ :258 „a completion-állapotot” ↔ :260 „completion-státusszal”
- **Hatás:** A diagnosztikus kvíz 4. itemének opciói kétféleképp érthetők. A „completion állapotát” különírása helyesírási hiba.
- **Javaslat:** EMBERI DÖNTÉS: a projektgazda döntse el az értékelési felelős QA-jával, hogy javítható-e nyelvileg az általa megadott itemszöveg. Két pontról van szó: a 4. item törzsében az alany egyértelműsítése, a 7. itemben egyetlen alak („completion-állapot”). A ✅, a kulcs tartalma és a disztraktorok nem változhatnak. A szerkesztői disztraktorok (7. item B és D) már egységesek. Rokon tétel: ERT-4 (QA-csomag).
- **Típus:** emberi-döntés · **Verdikt:** —

**NYELV-G1-15**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv (D10 terminológia)
- **Hely:** HUB:59 (3. szakasz, Mapping)
- **Probléma:** A HUB az M0.2 leckét a valódi címétől eltérő címmel sorolja fel, és a betoldott „dugma isit alapok” birtokos rag nélküli, különírt tükörszerkezet.
- **Bizonyíték:** HUB:59 „**L2 = M0.2** – Madrih, nem terapeuta – szerepek, elvárások, dugma isit alapok” ↔ HUB:72 és M0.2:6 „Madrih, nem terapeuta – szerepek és elvárások”
- **Hatás:** Ugyanaz a lecke a HUB-on belül két címen fut, így a képző vagy a fejlesztő nem tudja, melyik a kánoni cím (a manifest-nevek ügye külön: IMPL-7).
- **Javaslat:** HUB:59 → „Madrih, nem terapeuta – szerepek és elvárások” (a :72 és a leckefájl címe szerint). Korlát: a fájlnév és a link nem változik.
- **Típus:** objektív · **Verdikt:** —

LEVÁGVA: 5 további finding, súlyosságuk: 5×P2

## LENCSE: NYELV — G1 (hub, M0.1, M0.2, M0.3) (folytatás 2)

## NYELV lencse — M0, G1 (folytatás, NYELV-G1-16-tól)

Ez az utolsó adag: az első adagban LEVÁGVA jelölt 5 finding, mind P2. Fájlrövidítések, mint az első adagban:
- HUB = `02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md`
- M0.1 = `02 Tervezet/Modulok/M0/Online leckék/M0.1 – Üdv a képzésben! – Éves útiterv & mi köze hozzám.md`
- M0.2 = `02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrih, nem terapeuta – szerepek és elvárások.md`
- M0.3 = `02 Tervezet/Modulok/M0/Online leckék/M0.3 – Hogyan működik a Moodle, H5P és a kapu.md`

---

**NYELV-G1-16**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** HUB:125 (4. szakasz, Technikai segítségpont, Formátum)
- **Probléma:** Az „1–1-ben” alakban nagykötőjel áll, ami tartományt jelöl („1-től 1-ig”). A szöveg viszont egyéni segítséget akar mondani.
- **Bizonyíték:** HUB:125 „1–1-ben vagy kis csoportban segítenek bejelentkezni és megtalálni az M0.1–M0.4-et.”
- **Hatás:** Az „1–1” felolvasva és olvasva is értelmetlen; a képző csak kitalálja, hogy egyéni segítségről van szó.
- **Javaslat:** „egyénileg vagy kis csoportban segítenek bejelentkezni…”
  - Korlát: a jelentés (egyéni vagy kiscsoportos segítség, a teremben maradó képzők) változatlan.
  - A „négyszemközt” szó ne kerüljön be: az gyermekvédelmi kapu-jel. Hogy kell-e szabály a kiskorú madrihval folytatott egyéni helyzetre, az nem nyelvi kérdés, ezt a finding nem dönti el.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-17**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M0.3:12 (Lecke meta, akadálymentességi flag)
- **Probléma:** A kötelező akadálymentességi kikötésben két hiba van:
  - A félkövér jelölés egymásba van ágyazva: a belső `**felirat kötelező**` lezárja a külsőt, így a renderben épp a kulcsszó nem lesz félkövér, a körülötte álló szöveg viszont igen.
  - A záró mondat „így sem érhető el” szerkezete homályos: lehetetlenséget állít, ahelyett hogy előírná, hogy a cél ne legyen csak hangon vagy képen elérhető.
- **Bizonyíték:** M0.3:12 „ahhoz magyar **felirat kötelező** (WCAG 2.2 SC 1.2.2)” (egy már nyitott `**…` szakaszon belül); „A tanulási cél így sem érhető el kizárólag hang/kép útján.**”
- **Hatás:** A megvalósító egy kötelező a11y-kikötés hangsúlyát fordítva látja, és a záró mondat normaként nehezen értelmezhető.
- **Javaslat:**
  - A félkövér jelölés ne legyen egymásba ágyazva: egyetlen, nem beágyazott félkövér szakasz kell, vagy csak a „felirat kötelező” félkövér.
  - A záró mondat a korpusz megfogalmazásához igazodjon (M2.1:120 „hogy a tartalom ne kizárólag hang útján legyen elérhető”), pl. „A tanulási cél tehát nem lehet kizárólag hang vagy kép útján elérhető.”
  - Korlát: az akadálymentességi kikötés tartalma (alt-szöveg, felirat SC 1.2.2, diaszöveg SC 1.2.1) nem gyengülhet, és nem törölhető. A hozzáférhetőségi gazda QA-ja alá esik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-18**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** M0.1:59; M0.2:62 (3. szakasz, a runtime-követelmény blokkja, fejlesztői szöveg)
- **Probléma:** A mondat egyes számú alannyal indul („szöveges lépése kötelező”), majd többes számú állítmánnyal zárul („nem completion-feltételek”). Ugyanez a blokk az M0.1:13-ban, az M0.2:13-ban és az M0.3:59-ben következetesen egyes számú.
- **Bizonyíték:** M0.1:59 „A SLIDE 1, a SLIDE 6 és a SLIDE 7 szöveges lépése kötelező, de tanuló-lokális … és nem completion-feltételek”
- **Hatás:** A számegyeztetés elcsúszik (6. regressziós minta), valószínűleg a BSPEC-02 blokk beszúrásakor. A követelmény maga érthető marad.
- **Javaslat:** Mindkét helyen egyes szám: „…nem épül hozzájuk, és nem completion-feltétel”.
  - Korlát: a tanuló-lokális státusz, a D-4 hivatkozás és a felsorolt diák változatlanok.
  - A „cél verzión” írásmódja a NYELV-G1-12-ben szerepel, ugyanebben a menetben javítható.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-19**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** nyelv (D10 terminológia)
- **Hely:** HUB:281 (6. szakasz, 4. pont)
- **Probléma:** A stábelemzés a 2. kvízitemet idézőjeles, itemnévnek látszó „„kihez jelzek?”” címkével nevezi meg. A HUB ezt az itemet mindenhol máshol „jelzési út gyermekvédelmi ügyben” néven nevezi.
- **Bizonyíték:** HUB:281 „Ha sokan félreértik a „madrih, nem terapeuta” vagy a „kihez jelzek?” itemeket”; vö. HUB:142, :154, :197 „jelzési út gyermekvédelmi ügyben”
- **Hatás:** A stábnak a §6 jelzését a kvízterv táblázatához (HUB:151–159) kell kötnie, de a kért név ott nem szerepel.
- **Javaslat:** „…a „madrih, nem terapeuta” vagy a „jelzési út gyermekvédelmi ügyben” itemet…”
  - Korlát: a §6 beavatkozási logikája (M2/M3 megerősítés) változatlan.
  - Az „itemeket” helyett „itemet” áll, mert a „vagy” két külön itemet köt össze.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G1-20**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** nyelv
- **Hely:** M0.2:504 (SLIDE 7, kapcsolat a kickoff-peulához, tanulói szöveg)
- **Probléma:** A „nem marad meg” igekötős alak elsősorban azt jelenti, hogy a kulcsmondat nem rögzül vagy elvész. A szándékolt jelentés az, hogy a mondat nem csak az online leckében hangzik el.
- **Bizonyíték:** M0.2:504 „ez a kulcsmondat – **„madrih, nem terapeuta”** – nem marad meg az online leckében: a **kickoff-peulán élőben is kimondjuk**”
- **Hatás:** Első olvasásra úgy hat, mintha a kulcsmondat nem maradna meg a tanulóban. A kettőspont utáni „is” helyreállítja az értelmet, ezért a bizalom alacsony.
- **Javaslat:** „…– nem marad az online leckében: a **kickoff-peulán élőben is kimondjuk**…”, azaz az igekötő elhagyása.
  - Korlát: a mondat többi része, az M0.A „Közös keret” utalás és a PED-6 által érintett M0.1-szöveg változatlan.
  - Látható szöveg változik, ezért pin kell.
- **Típus:** objektív · **Verdikt:** —

---

NINCS TÖBB

## LENCSE: NYELV — G2 (M0.4, M0.A)

NYELV-G2: nyelvi review az M0 G2 fájlcsoportján (read-only, AP-2026-10-11-01). 15 findingot adok le, 7 további P2 vár a folytatásra.

Rövidítések:
- [M0.4] = 02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md
- [M0.A] = 02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md
- [GL] = 02 Tervezet/Glosszárium – someres és pedagógiai fogalmak.md
- [HUB] = 02 Tervezet/Modulok/M0/M0 – Kickoff, keret, technika.md

---

**NYELV-G2-1**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** [M0.A]:147–149 és :154–156 (3. Percbontás); :152; :647. A blokkcímek: :255, :330, :376, :410, :459
- **Probléma:** Ugyanazokat a blokkokat a fájl háromféle néven hívja: „1./2. fő tevékenység”, „Blokk 2–4”, „Élmény / gyakorlat 1–2”. A percbontás egy listán belül keveri a „fő tevékenység” és a „Blokk 4” címkét. A blokkcímek is eltérnek: a percbontásban a Blokk 2 neve „Mit várunk, mit hozunk?”, a 4.3-ban a Blokk 3-é „Mit várunk, mit vállalunk?”. A „Kihez fordulhatok” kétszer kérdőjel nélkül áll (:152, :647).
- **Bizonyíték:** :147 „**10–25’** – 1. fő tevékenység – „Mire jöttünk? Mit várunk, mit hozunk?” – kiscsoportos plakát” / :149 „**40–55’** – Blokk 4 – „Kihez fordulhatok?” + zárókör”
- **Hatás:** A képző az „1. fő tevékenységet” a „Blokk 1”-gyel azonosíthatja, és vágás közben rossz blokkot rövidít.
- **Javaslat:** A 60’-es és a 45’-ös percbontás, valamint a :152 vegye át a 4.x szakasz címkéit és címeit szó szerint („Blokk 2 – „Mire jöttünk?” …”, „Blokk 3 – „Mit várunk, mit vállalunk?” …”). A :152-ben és a :647-ben az alak „„Kihez fordulhatok?””. Korlát: a perceket ne írd át (azokat a PED-5 kezeli), és tartalom ne változzon.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-2**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** [M0.4]:146–151 (SLIDE 1, diaszöveg)
- **Probléma:** A mondat ponttal lezárul, utána bevezetés nélkül jön egy kisbetűs, vesszőkkel tagolt felsorolás. A szerkezetből kiesett a „hanem”, és emiatt a „nem csak” különírása is hibás lett. Valószínűleg exportmaradvány.
- **Bizonyíték:** :146 „Gondolj bele: a *hanihjaid* (a kvucád tagjai, akiket vezetsz) nem csak peulán találkoznak veled.” / :148 „– csoportchatben,”
- **Hatás:** A diaszöveg töredékesnek hat, a lista nem kapcsolódik semmihez.
- **Javaslat:** „…nemcsak peulán találkoznak veled, hanem” (a pont helyett), utána a változatlan lista. A „nemcsak … hanem” egybeírás így szabályos.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-3**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.4]:146 ↔ :554 (lásd még :158, :222, :417)
- **Probléma:** A „kvucád” egy leckén belül két különböző csoportot jelöl. A SLIDE 1 meghatározása szerint a hanihok csoportja, akiket a tanuló vezet. A :554-ben viszont a képzős csoport, akivel a kickoffon találkozott, és akinek a „Bemutatkozó falon” bemutatkozik.
- **Bizonyíték:** :146 „(a kvucád tagjai, akiket vezetsz)” / :554 „a kvucáddal **élőben a kickoff-peulán találkoztál először** … itt írásban is bemutatkozol ugyanannak a közösségnek”
- **Hatás:** Aki a SLIDE 1 meghatározását követi, azt hiheti, hogy a fórumposztot a saját hanihjai látják. Ez a láthatóság megértését is zavarja.
- **Javaslat:** A :554-ben jelöld, hogy a képzős csoportról van szó, például „a képzős kvucáddal”. Ugyanezt a mondatot a validált PED-10 (feltételes kickoff-részvétel) is átírja, ezért a kettőt egy lépésben javítsd.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-4**
- **Súlyosság:** P2 · **Bizalom:** magas · **Lencse:** nyelv
- **Hely:** [M0.A]:90 (2.3) ↔ :636 (5. ellenőrző lista, 4. pont). Kapcsolódik: :58 (az M0.A-KART-02 spec megjegyzése)
- **Probléma:** Az ellenőrző lista „Megvan a mondat:” bevezetéssel a 2.3-ban előkészített biztonsági mondatra utal, de attól eltérő szöveget idéz („fájdalmas” a „nagyon személyes” helyett, a „most” nélkül). Az asset-spec maga is rögzíti, hogy a változatok nincsenek egységesítve.
- **Bizonyíték:** :90 „Nem kötelező mély vagy nagyon személyes dolgot megosztani – annyit mondasz, amennyi neked most oké.” / :636 „Nem kötelező mély vagy fájdalmas dolgot megosztani; annyit mondasz, amennyi neked oké.”
- **Hatás:** A képző két „kész mondatot” kap ugyanarra a pillanatra, a nyomtatott kártya (KART-02) pedig a harmadik forrást követi.
- **Javaslat:** A :636 idézze szó szerint a :90 első mondatát. Ez a legkisebb módosítás, és a KART-02 spec is ezt a változatot idézi. Utána a :58 zárójeles megjegyzéséből törlendő az ellenőrző listára vonatkozó rész, mert csak a Blokk 2 változata marad eltérő. Asset-spec változik, ezért `media_manifest build` kell, a látható szöveg miatt pedig pin. Korlát: a Blokk 2 (:342) csoportnak szóló változata maradhat.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-5**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.A]:638 (5. ellenőrző lista, 4. pont)
- **Probléma:** A kánoni formula csonka változata áll itt, kiesett belőle az „előbb a biztonság” és az „utána a belső jelzés” (2-es regressziós minta: elveszett minősítő). A Glosszárium szerint csonka változat nincs.
- **Bizonyíték:** :638 „hogyan vonod be azonnal a Memunát, ha valami komolyabb jön fel (közvetlen veszélynél előbb a 112)?” ↔ :137 „**Közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés.**”
- **Hatás:** Az ellenőrző lista a sorrend első elemét (a biztonságot) nem idézi fel.
- **Javaslat:** A zárójelben a kánoni formula álljon szó szerint: „(közvetlen veszélynél előbb a biztonság és a 112, utána a belső jelzés)”. Forrás: :93, :137, [GL]:164.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-6**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.A]:610 (Megjegyzés a modul felépítéséről)
- **Probléma:** „Az áttekintő”-nek nincs előzménye a fájlban. A mondat egy másik dokumentum megfogalmazását magyarázza utólag, nem képzői utasítás; korábbi szerkesztés nyomának tűnik. A „szándékoltan” helyesen „szándékosan”, a „fenti minimum-leírású segítő blokk” pedig főnévtorlódás.
- **Bizonyíték:** :610 „Ha az áttekintő több peula-szerű elemre utal, az erre a tagolásra vonatkozik.” / „**szándékoltan csak ez az egy peula (M0.A) van**”
- **Hatás:** A képző nem tudja, melyik dokumentumról van szó. A valószínű forrás a [HUB]:12 („Peula A (M0.A, 45–60’) – Kickoff & ismerkedés + technikai segítségpont”).
- **Javaslat:** Nevezd meg az előzményt (az M0 modul áttekintője, „Offline alkalom” sor), írd „szándékosan”-ra, és bontsd fel a főnévtorlódást („ez az opcionális segítő blokk, lásd a fenti minimális forgatókönyvet”). Korlát: új magyarázat nem kerülhet be. Ha az ellentmondás a hub megfogalmazásából ered, azt az implementációs lencse dönti el, nyelvi javítással nem foltozható.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-7**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.A]:366, :367, :502 (képzői szöveg)
- **Probléma:** Fejlesztői és compliance-regiszter került a képzőnek szóló utasításba: „a felvétel nélküli alapút”, a látható döntés-attribúció „(… utólagos ellenőrzés (vétó/QA): a DPO)” és a „Z-oldalon”.
- **Bizonyíték:** :366 „A plakát fizikai megőrzése a felvétel nélküli alapút;” / :367 „(projektgazdai döntés, 2026-10-02; utólagos ellenőrzés (vétó/QA): a DPO)”
- **Hatás:** A képzőnek a „vétó/QA” és az „alapút” értelmezhetetlen governance-szó, nehezíti a felolvasható utasítást.
- **Javaslat:** A :366 a HUM-PRIV-02 saját, hétköznapi mondatát kövesse (`Emberi jóváhagyás szükséges.md`:147: „ne gyűjts felvételt, ha ugyanaz a pedagógiai cél elérhető nélküle”). A :367 zárójeles attribúciója kerüljön át ugyanennek a sornak a meglévő `<!-- Döntésazonosító: HUM-PRIV-02 … -->` kommentjébe. A :502-ben „a Z-oldalon” helyett „a Z.A-n” álljon. Korlát: az adatvédelmi kikötés minden eleme szó szerint marad (alapértelmezés, kitakarás, hozzájárulás, 90 nap, törlés). A látható attribúció 15 fájlban 21-szer fordul elő; ha szándékos konvenció, a :367-es rész elvetendő, a :366 és a :502 akkor is áll.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-8**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.A]:351, :360–362, :348, :442 (4.2 és 4.3, képzői lépésleírás)
- **Probléma:** A lépésleírásokban mondattöredékek és személy-elcsúszások vannak. A :351-ben ige nélküli töredék áll („három részre osztva”), hibás vonzattal („három oszlopnak”), és a képzőnek szóló leírás „ti”-re vált. Egy lépésen belül keveredik a „kirakjátok” / „A résztvevők … körbesétálnak” / „foglald össze”. A :348 „mindenét” nem standard, a :442-ben pedig töredék után vesszős összevonás áll (6-os regressziós minta).
- **Bizonyíték:** :351 „A plakát három részre osztva (rajzolhatjátok három oszlopnak is). Instrukció:” / :360 „* A plakátokat kirakjátok a térben.”
- **Hatás:** Nem világos, mit csinál a képző és mit a csoport, a leírás így nem felolvasható.
- **Javaslat:** A képző teendői E/2-ben, a csoporté T/3-ban álljanak. Például :351 „A plakátot három részre osztják – akár három oszlopot is rajzolhatnak rá.”; :360 „A csoportok kirakják a plakátokat a térben.”; :348 „mindenét” → „mindent”; :442 két mondatra bontva. Korlát: lépés, sorrend és időtartam nem változik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-9**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.A]:248, :506 (felolvasandó és képzői szöveg)
- **Probléma:** Két tükörfordítás: „tedd minimálissá a tétet” („minimize the stakes”) és „ennyire aktívak és jelen voltatok” („engaged and present”). Magyarul a „jelen voltatok” azt jelenti, hogy ott voltatok.
- **Bizonyíték:** :248 „és tedd minimálissá a tétet:” / :506 „„Köszi, hogy ennyire aktívak és jelen voltatok az első alkalmon.”
- **Hatás:** A felolvasott zárómondat idegenül szól, a „jelen voltatok” jelentése elcsúszik.
- **Javaslat:** :248 „és csökkentsd a tétet:”; :506 „Köszi, hogy ilyen aktívan és figyelmesen részt vettetek az első alkalmon.”
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-10**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.4]:236 (SLIDE 2, válaszopció)
- **Probléma:** Tanulói opcióban áll az angol „bullying”, holott a Glosszárium kanonikus magyar alakja a „kortárs bántalmazás”. A korpusz minden más helyén az angol szó csak zárójelben követi a magyart.
- **Bizonyíték:** :236 „* Szívatás / bullying chatben” ↔ [GL]:155 „A kortárs bántalmazás (bullying) célzott, bántó dinamika”
- **Hatás:** Egy fogalom két megnevezést kap; az M3 a magyar terminust tanítja.
- **Javaslat:** „Szívatás / kortárs bántalmazás chatben”. Véleménykérdés, nincs kulcsa. Látható szöveg, ezért pin kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-11**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.4]:25 (Központi mondat), :154, :486. Scope-on kívül ugyanez: [HUB]:238
- **Probléma:** A „dugma isit vagy” megszemélyesítő szerkezet („dugma isitnek lenni”) ütközik a Glosszárium szócikkével, amely ezt kerülendőnek mondja, és helyette a „dugma isitként viselkedni” vagy a „személyes példát mutatni” formát ajánlja. A modulszöveg (2. kánoni forrás) és a Glosszárium (3. kánoni forrás) itt ellentmond egymásnak, ezért nem választok közülük.
- **Bizonyíték:** :154 „Az a kérdés: *„Milyen dugma isit vagy az online térben?”*” ↔ [GL]:27 „A megszemélyesített „Dugma Isitnek lenni” formát **kerüld** – helyette: „dugma isitként viselkedni””
- **Hatás:** A lecke központi mondata a terminológiai referenciával ellentétes alakot rögzít.
- **Javaslat:** EMBERI DÖNTÉS: a projektgazda döntse el (utólagos QA: ken-vezető / mozgalmi felelős, [GL]:5), hogy a Glosszárium „kerüld” szabálya a kisbetűs „dugma isit vagy” alakra is vonatkozik-e. Ha igen, a három hely „dugma isitként viselkedsz” formára vált, és a [HUB]:238 vele együtt mozog. Az írásmódot (HUM-SOMER-02) ez nem érinti.
- **Típus:** emberi-döntés · **Verdikt:** —

**NYELV-G2-12**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.4]:482–486 (SLIDE 6 segítő kérdések) ↔ :565 (fórumleírás, tanulói szöveg)
- **Probléma:** Ugyanaz az öt segítő kérdés két helyen eltérő szöveggel áll (7-es regressziós minta). A :565 hozzáteszi a „vagy a képzésben” részt, az utolsó pontban „vagy” helyett „szeretnél jelen lenni” áll, és ez a pont felszólítás egy „kérdések” felvezetésű listában. A :486-ból hiányzik az utalószó („Mi az 1 szó” helyett „Mi az az egy szó”).
- **Bizonyíték:** :486 „– Mi az 1 szó, ami eszedbe jut arról, hogy **online is dugma isit** vagy?” / :565 „– Írj egy szót, ami eszedbe jut arról, hogy **online is dugma isitként** szeretnél jelen lenni.”
- **Hatás:** A tanuló a vázlatot a dia kérdéseire írja, a fórumon viszont más kérdéseket lát.
- **Javaslat:** A :565 vegye át szó szerint a SLIDE 6 kérdéseit, kérdő formában; ha a „vagy a képzésben” szándékos bővítés, fordítva: a SLIDE 6 is kapja meg. Új kérdés nem kerül be. A :486-ban „Mi az az egy szó”. Az utolsó pont igéje a G2-11 döntését követi. A :565 BIZT-8 alá eső láthatósági mondatához ne nyúlj.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-13**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.4]:549 ↔ :48, :524, :566, :570
- **Probléma:** A záró lépés a fórumválaszt „komment”-nek hívja, a fájl minden más helyén viszont „válasz” áll. A „Moodle-komment” a SLIDE 1–2-ben más jelentésű: a lecke alatti hozzászólás. A mondatban „+” jel is van.
- **Bizonyíték:** :549 „**1. lépés: Moodle → „Bemutatkozó fal” fórum → poszt + 1 komment.**” / :570 „Legalább **1 saját téma** + **1 válasz**.”
- **Hatás:** A completion-feltétel (válasz egy másik résztvevő posztjára) elmosódik, és összekeveredhet a lecke-kommenttel.
- **Javaslat:** „… → poszt és 1 válasz egy másik résztvevő posztjára.” A kiegészítés a :524-ből szó szerint jön, új tartalom nincs. Látható szöveg, pin kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-14**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.4]:552 (SLIDE 7 záró mondat)
- **Probléma:** A „belépő-jelző” tanulói szövegben nem értelmezhető alkalmi szóképzés, ráadásul kötőjellel írva. A jelentése a hubból rekonstruálható.
- **Bizonyíték:** :552 „(nem vizsga, hanem belépő-jelző)” ↔ [HUB]:131 „**belépő jellegű**, nem vizsga; jelzést ad a stábnak, hogy ki mennyire tudott belépni a rendszerbe.”
- **Hatás:** A tanuló nem érti, mit jelent a kvíz eredménye.
- **Javaslat:** „(nem vizsga: azt jelzi a stábnak, mennyire sikerült belépned a rendszerbe)”, a [HUB]:131 alapján. Korlát: a „Csak arra figyelj, hogy mind a 7 kérdésre válaszolj.” mondat marad (validált ERT-2 javítási korlát), a kvíz jellege nem változik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-15**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.A]:16, :18 (Fő célok, tanulói nyelven)
- **Probléma:** Az 1. célban jövő idő és jelen idejű „van” keveredik („A peula végére … van”). A 3. cél kiesik a tanulói nézőpontú, E/2-es párhuzamból, és az „elhangzanak közösen” szerkezet nem magyaros (az „elhangzik” mellé nem illik a „közösen”).
- **Bizonyíték:** :16 „A peula végére **ismerni fogod névről–arcról** a kvucát, és van egy első közös élményetek.” / :18 „Elhangzanak közösen a **keretek és határok**”
- **Hatás:** A tanulói célmondatok pontatlanok, és a felsorolás nem párhuzamos.
- **Javaslat:** :16 „… és lesz egy első közös élményetek.”; :18 „Közösen kimondjuk a **kereteket és határokat** (…)”, a 4.3 céljához igazítva (:415 „közösen kimondani a kereteket”). A zárójel tartalma változatlan.
- **Típus:** objektív · **Verdikt:** —

LEVÁGVA: 7 további finding, súlyosságuk: 7×P2

---

Megjegyzések a verifiernek és a javítónak:
- Egyik fájlban sincs `@source` (VO) blokk. Régi írásmód (`madrich`, `chanich`, `ishit`, `hagshama`, `Leviatan`, `madrihák`) egyikben sincs.
- Nem jelentettem újra a validált M0-findingokat: PED-5, PED-10, BIZT-6, BIZT-8, IMPL-6, IMPL-7, ERT-2 és a K1 klaszter.
- A befagyasztott [M0.4]:309–333 szöveghez (BIZT-3 Memuna-döntés, K1 újraírás) nyelvi javaslatot nem tettem.
- A 2.4 mini-protokoll mondatait csak ott vizsgáltam, ahol kánoni formula csonkult (G2-5). Ezek: [M0.A]:131–137, a KART-01 spec szerint szó szerint kártyára kerül.
- A G2-4 és a G2-7 asset-specet vagy -megjegyzést is érint: `media_manifest build` kell, külön `chore(media)` commitban. A látható szöveget érintő tételeknél (G2-2, -3, -8–-10, -12–-15) pin kell.

## LENCSE: NYELV — G2 (M0.4, M0.A) (folytatás 2)

NYELV-G2 folytatás: a kimaradt 7 finding (NYELV-G2-16…22). Ezzel a lista teljes, a már leadott 15 tételt nem ismétlem.

Rövidítések (ugyanazok, mint az első adagban):
- [M0.4] = 02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md
- [M0.A] = 02 Tervezet/Modulok/M0/Peulák/M0.A – Kickoff & ismerkedés + közös keret.md
- [Z.A] = 02 Tervezet/Modulok/Z/Peulák/Z.A – Mit viszek magammal – Záró kvuca-peula.md

---

**NYELV-G2-16**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.4]:501, :505, :525. A helyes forma ugyanebben a fájlban: :48, :522, :540
- **Probléma:** Idézőjeles név toldalékolásánál a rag az idézőjelen belülre került. Így egy nem létező név áll idézőjelben („Bemutatkozó falon”, „M0 belépőkvízt”). A fájl más helyein a helyes forma szerepel, ahol a név változatlan és a toldalékot a mögé tett „fórum” szó kapja.
- **Bizonyíték:** :501 „a végső poszt a „Bemutatkozó falon” a csoportnak látszik” / :525 „**kitöltsd az „M0 belépőkvízt”**” ↔ :522 „felkeresd a kurzusban a **„Bemutatkozó fal” fórumot**”
- **Hatás:** Az activity neve nem egyezik a Moodle-ben látott névvel, és a fájl belül következetlen.
- **Javaslat:** :501 „a „Bemutatkozó fal” fórumon”; :505 „a „Bemutatkozó fal” fórumra”; :525-ben a toldalék az idézőjel után, kötőjellel álljon, a névalak pedig kövesse az IMPL-7 egységesítését. Korlát: a :501 láthatósági mondatának tartalmát a BIZT-8 javítja, ezért itt csak a toldalék helye változik, és a két javítás egy lépésben menjen.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-17**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.A]:475, :481. Asset-spec: :196 (M0.A-POSZ-02)
- **Probléma:** A „-ként” jelentésű (minőséget jelölő) „mint” elé vessző került. Ilyen jelentésben a „mint” elé nem teszünk vesszőt („én mint madrih”).
- **Bizonyíték:** :475 „* középen: „**ÉN, mint madrih**”” / :481 „**téged, mint képzőt** –,”
- **Hatás:** Tipográfiai hiba a nyomtatott poszteren és a képzői szövegben.
- **Javaslat:** „ÉN MINT MADRIH” / „Én mint madrih”; „téged mint képzőt”. A :196-os spec ugyanígy változik, mert asset-spec: `media_manifest build`, a látható szöveg miatt pin is kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-18**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:**
  - „stáb-dosszié”: [M0.A]:40, :366, :367, :629; asset-blokkokban :170, :174, :264, :268, :286, :321
  - „induló-szavak”: :502, :657; asset: :168, :170, :288
  - „példa-javaslatok”: :427; asset: :385
  - „mini-protokoll”: :129, :639; asset: :102
  - Scope-on kívül ugyanez: [Z.A]:55, :423, :440, :458
- **Probléma:** Kéttagú köznévi összetételek kötőjellel. A helyes alak egybeírt: „stábdosszié”, „példajavaslat”, „miniprotokoll”. Az „induló-szavak” egybe („indulószavak”) vagy jelzős szerkezetként külön írandó, kötőjellel semmiképp. A héber tagú, korpuszkonvenció szerinti összetételeket (pl. „kvuca-plakát”, „madrih-szerep”) szándékosan nem soroltam ide.
- **Bizonyíték:** :502 „**jegyezd fel név nélkül egy cetlire az elhangzott induló-szavakat**” / :366 „**göngyöld fel mindegyik kvuca-plakátot, és tedd el a stáb-dossziéba**”
- **Hatás:** Helyesírási hiba a képzői szövegben, és ugyanaz a hiba a nyomtatott asset-leírásokban is.
- **Javaslat:** Egybeírás minden felsorolt helyen. Az „induló-szavak” a [Z.A] négy helyével együtt változzon, mert a Z.A erre a fogalomra köt vissza (7-es regressziós minta). Ha az „indulószó” mozgalmi saját fogalom, azt a javító a Z.A-val egyeztetve dönti el. Asset-specek változnak, ezért `media_manifest build` kell.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-19**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.4]:325 (SLIDE 3, helyes válasz visszajelzése); [M0.4]:470 (SLIDE 6 Cél, fejlesztői szöveg); [M0.A]:358 (4.2, 4. lépés)
- **Probléma:** Hiányzik egy utalószó vagy kötőszó. „Ezekben közös, hogy” helyett „ezekben az a közös, hogy” kell. A „…, ne ott kelljen” elől hiányzik a „hogy”. A „mi az egy-egy dolog” helyett „mi az az egy-egy dolog” kell. A :486 hasonló hiányát a G2-12 már tartalmazza.
- **Bizonyíték:** :325 „„Igen, ezekben közös, hogy **nem mész bele a csúfolódásba / nem hagyod magára az érintettet**,” / [M0.A]:358 „– mi az egy-egy dolog, amit legfontosabbnak éreznek a három oszlopból.”
- **Hatás:** Döccenő, nem magyaros mondatok, a :325 ráadásul tanulói visszajelzés.
- **Javaslat:** :325 „Igen, ezekben az a közös, hogy…”; :470 „…, hogy ne ott kelljen nulláról kitalálnia.”; :358 „mi az az egy-egy dolog…”. Korlát: a :325 a validált K1 (N-M0-14) újraírási körébe esik, ezért csak akkor javítandó, ha a mondat a K1 után is megmarad. A ✅-hoz és a disztraktorokhoz nem nyúlunk.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-20**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** nyelv
- **Hely:** [M0.A]:90 (2.3, biztonsági mondat). Asset-spec: :58 (M0.A-KART-02, szó szerinti idézet)
- **Probléma:** A „hogy” tárgyi mellékmondatot alanyi ragozású ige vezeti be („jelezhetsz, hogy”). Ugyanebben a mondatban a párja határozott ragozású („mondhatod, hogy”). Egy célhatározói olvasat („jelezhetsz, hogy így beszéljünk”) elvben lehetséges, ezért alacsony a bizalom.
- **Bizonyíték:** :90 „nyugodtan mondhatod, hogy erről most nem szeretnél beszélni, vagy jelezhetsz, hogy beszéljünk róla később külön.”
- **Hatás:** A felolvasandó képzői mondat a párhuzamos szerkezetben ragozási hibának hat.
- **Javaslat:** „vagy jelezheted, hogy beszéljünk róla később külön”. A :58 spec ugyanígy változik, mert szó szerint idézi: `media_manifest build` és pin kell. A mondat tartalma és a passzolási jog nem változik.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-21**
- **Súlyosság:** P2 · **Bizalom:** közepes · **Lencse:** nyelv
- **Hely:** [M0.A]:355, :426, :594, :598 (a képző által felolvasandó, idézőjeles szövegek)
- **Probléma:** A felolvasandó szövegekben perjel áll kötőszó helyett. Ez a szerkesztői norma szerint („`+`, `/` … helyett rendes mondat”) kerülendő, és hangosan nem olvasható fel egyértelműen.
- **Bizonyíték:** :426 „Mit ígér nektek a stáb / program?” / :598 „nyugodtan gyertek oda laptoppal / telefonnal,”
- **Hatás:** A képzőnek felolvasás közben kell eldöntenie, hogy „és”-t vagy „vagy”-ot mond.
- **Javaslat:**
  - :355 „Írjatok vagy rajzoljatok”
  - :426 „a stáb vagy a program”
  - :594 „kérdés vagy bizonytalanság”
  - :598 „laptoppal vagy telefonnal”, valamint „a Moodle és a H5P világában”

  Korlát: csak az idézőjeles, felolvasandó szövegek változnak; az opciócímkék, a fejlécek és az eszközlisták perjelei maradnak.
- **Típus:** objektív · **Verdikt:** —

**NYELV-G2-22**
- **Súlyosság:** P2 · **Bizalom:** alacsony · **Lencse:** nyelv
- **Hely:** [M0.A]:347 (4.2, 2. lépés, „Kis létszámnál”)
- **Probléma:** A „vagy páratlan a létszám” feltétel nem következik a környezetből. A :344 szerint a csoportok 3–5 fősek, így 8 fő körüli páratlan létszámnál (7, 9) is kijön két csoport. Nem dönthető el, mit akart mondani a mondat, ezért szöveget nem javaslok rá.
- **Bizonyíték:** :347 „elég 2 csoport (vagy ha nagyon kevesen vannak, vagy páratlan a létszám, akár 1 közös plakát, és a megosztás körben történik”
- **Hatás:** Páratlan létszámnál a képző fölöslegesen összevonhatja a csoportokat egyetlen plakátra.
- **Javaslat:** EMBERI DÖNTÉS: a modulgazda vagy a projektgazda mondja meg, mit jelent a „páratlan a létszám” feltétel (pl. egyenlőtlen csoportméret?). Addig a mondat nem írható át, és nem található ki rá magyarázat (8-as regressziós minta).
- **Típus:** emberi-döntés · **Verdikt:** —

---

NINCS TÖBB

Megjegyzés: a G2-17, -18 és -20 asset-specet is érint, ezekhez `media_manifest build` kell, külön `chore(media)` commitban. A látható szöveget érintő tételek után pinnelni kell. A G2-16 és a G2-19 a validált BIZT-8, illetve K1 javítással egy lépésben kezelendő.
