# IMPROVEMENT-PLAN — Kutatás-alapú, prioritált javítási terv

**Tárgy:** A Hasomer Hacair madrichképzés igazolt gyengeségeinek prioritált, kutatás-alapú javítási terve.
**Forrás-alap:** Ez a terv az `_AUDIT/` korpusz verifikált megállapításaira ÉPÍT — nem ismétli újra az auditot. Elsődleges bemenetek: `OPINION-AUDIT.md` (14 kalibrált állítás, C1–C14), `GATE-VALIDITY.md` (🔴 10 · 🟡 23 · 🟢 11), `IDEOLOGY-GATE-REVIEW.md`, `SAFEGUARDING-REVIEW.md`, `ARCHITECTURE-REVIEW.md`, `CURRICULUM-IV.md`.
**Dátum:** 2026-06-19
**Hatókör:** A javaslatok döntés-előkészítők. A „mozgalmi/szervezeti döntés" jelzésű tételeket szándékosan NEM oldjuk meg helyettetek — a magyarországi Somer vezetésének / a pedagógiai stáb / a gyerekvédelmi felelős hatásköre.

---

## 1. Vezetői összefoglaló

### Mit mond az audit, és mit NEM
Az `OPINION-AUDIT.md` kalibrációja után a kép józan: a program **megáll a lábán** (14 állításból egy sem megalapozatlan, 5 minden ponton tartható). A gyengeségek **lokalizáltak és mintázatosak**, nem rendszerszintűek. Ezért ez a terv NEM újratervezést javasol, hanem **célzott, olcsó, magas hatású beavatkozásokat** a 3–4 igazolt fájdalompontra:

1. **Értékelés-validitás** — nem az egész program, hanem konkrét kapuk (M0 belépő-kvíz, M2 kapstone, M3/M5/M6/M7 item-bank és rubrika) hiányosak vagy konvergens-kvíz-feszültségben állnak (C5, C6, C11; `GATE-VALIDITY`).
2. **Ideológiai mélység** — gyakorlatilag az M2.3 leckére koncentrálódik; a hagshama 0× operacionalizált (C3; `IDEOLOGY-GATE-REVIEW` A1–A4).
3. **Gyerekvédelem élesítése** — a keret a mezőny fölött van, DE a felelős neve/dátuma placeholder, és van pár konkrét tartalmi kockázat (C4; `SAFEGUARDING-REVIEW`).
4. **Fenntarthatóság** — a szűk keresztmetszet NEM a technikai stack, hanem a **tartalom- és kapu-karbantartás emberi munkaigénye** egy 2-képzős önkéntes stábnál (C12; interjú-jelentés).
5. **Terhelés-realizmus** — a peula-percbontások feszesek, lokálisan alulbecsült (M7 szintézis-produktum, M0/M2/M4); a „rendre alulbecsült" túlzó (C7).
6. **AI-governance + QA** — az AI-tartalom emberi lektorálást igényel, fokozottan a safeguarding-résznél; a QA-felelős jelenleg placeholder (C13; README).

### Vezérelv: „kevesebb gépezet, több mozgalom"
A program legnagyobb erőssége a someres beágyazás (kvuca, dugma ishit — C2), a curriculáris ív (C1) és a Gen Z / 15+ hangolás (C9). A legnagyobb kockázata a túl-építés (C12). **A terv minden tétele erre a vezérelvre van fűzve:**

- **Építs a meglévő nonformális erősségekre**, ne fölébük. A reflexiós rutin (SBI, Johari), a peula-sablon és a kvuca-keret már megvan — az ideológiai mélység, a portfólió-értékelés és a hagshama is EZEKBE illeszkedjen, ne új eszközként.
- **Az eszközök nagy része már létezik** — a kapu-rubrikák megírva, az analytics manuális. A munka java **kijelölés és horgonyzás**, nem fejlesztés.
- **Reális erőforrás**: minden tétel mellett szerepel a ráfordítás (kicsi/közepes/nagy) és a gazda, hogy egy 2-képzős önkéntes stáb tervezni tudjon.
- **MVP-logika**: egy modul + egy kapu élesben, mérés, tanulás — utána bővítés. Nem „big bang".

### A prioritások logikája
- **P0 (most, alacsony költség, magas hatás):** biztonság-kritikus és bizalom-kritikus tételek, amelyek nélkül a program élesítése felelőtlen lenne, ÉS amelyek olcsók. Itt a kapu-élesítés és a gyerekvédelmi sign-off.
- **P1 (közép táv):** validitást és mélységet emelő tételek, amelyek mérhető minőséget adnak, de több munkát és néhány mozgalmi döntést igényelnek.
- **P2 (hosszú táv):** fenntarthatósági és minőségbiztosítási rendszer, amely a programot évek alatt tartja életben — fontos, de nem blokkolja az indulást.

---

## 2. PRIORITÁSOK

> Minden tétel: **PROBLÉMA** (igazolt finding) → **AJÁNLÁS** (kutatás-alapú) → **LÉPÉSEK** → **RÁFORDÍTÁS** → **GAZDA** → **FORRÁS**.
> Jelölés: 🟦 = szakmai/operatív · 🟥 = MOZGALMI/SZERVEZETI DÖNTÉS (lásd §3).

---

### P0 — Most (alacsony költség, magas hatás)

#### P0.1 — Gyerekvédelmi sign-off lezárása (placeholder → nevesített felelős) 🟥
- **PROBLÉMA:** A gyerekvédelmi keret kemény és a mezőny fölött részletezett, DE az élesedése feltételhez kötött és jelenleg befejezetlen: a felelős neve/dátuma `⟬kitöltendő⟭` placeholder az M3.3 és M3-KAPU fejlécében (C4; `OPINION-AUDIT` C4; `GATE-VALIDITY` M3). A safeguarding-tartalom emberi szakértői jóváhagyás nélkül NEM publikálható.
- **AJÁNLÁS:** Nevesített szakértői sign-off felelős + „négy szem" elv a gyerekvédelmi tartalomra. Rögzítsétek névvel/szereppel, ki a tartalmi sign-off felelős (képzésvezető) és ki a gyerekvédelmi sign-off felelős. A safeguarding-tartalmat e kettőnek külön kell jóváhagynia. Önkéntes-vezetésnél elég 1–2 betanított ember + backup, a szerepet a képzés indító dokumentumában rögzítve.
- **LÉPÉSEK:**
  1. Jelöljétek ki név szerint a gyerekvédelmi felelőst + egy backupot.
  2. Töltsétek ki az M3.3 / M3-KAPU placeholder-mezőit (név, dátum, review-státusz).
  3. A felelős nézze át a teljes M3-at és a jelzési láncot a helyi protokollhoz illesztve.
  4. Rögzítsétek: safeguarding-tartalom nem élesedik a felelős aláírása nélkül.
- **RÁFORDÍTÁS:** kicsi (a tartalom kész, ez jóváhagyás + 1 review-kör).
- **GAZDA:** gyerekvédelmi felelős + szervezeti vezető.
- **FORRÁS:** https://docs.modulos.ai/frameworks/nist-ai-rmf/generative-ai-profile · https://predictionguard.com/blog/ai-governance-compliance-evidence-a-framework-for-nist-ai-rmf-nist-ai-600-1-owasp-and-eu-ai-act-audit-readiness

#### P0.2 — „Rejtsd el" logika és titoktartás-csapda javítása 🟥
- **PROBLÉMA:** (a) M3.4 a dohány/alkohol kapcsán a **titkolás/rejtegetés** mintáját normalizálja („menj olyan helyre, ahol nem látnak"), ami ütközik a modul saját dugma ishit / transzparencia üzenetével (`SAFEGUARDING-REVIEW` 1). (b) A reflexiós napló „csak a mentorod látja" megnyugtatás (M3.4, M0.2, M2.4) ugyanazt a **titoktartás-csapdát** hozza létre, amit a modul a chanichokra helyesen tilt — a mentor sem ígérhet titoktartást veszélyeztetettség esetén (`SAFEGUARDING-REVIEW` 2).
- **AJÁNLÁS:** Fejlettség-érzékeny, kontextuális safeguarding-review (nem kulcsszó-szűrő): a kockázatos részeket emberi szakértő nézi át. A „rejtsd el" logikát a ken hivatalos magatartási kódexéhez kell igazítani (mit szabad, mit nem, transzparensen). A napló-megnyugtatásokat egészítsétek ki a jelzési kötelezettség elvével.
- **LÉPÉSEK:**
  1. M3.4 dohány/alkohol rész: cseréljétek a „rejtsd el"-t a ken code-of-conduct alapú, transzparens megfogalmazásra.
  2. M3.4 / M0.2 / M2.4 napló-mezők: a „csak a mentorod látja" mellé tegyétek be a feltételt (ha veszély derül ki, a mentornak jeleznie kell — ez a te biztonságodat szolgálja).
  3. A pontos szöveget a gyerekvédelmi felelős hagyja jóvá.
- **RÁFORDÍTÁS:** kicsi (szövegszintű javítás + 1 review).
- **GAZDA:** gyerekvédelmi felelős + szervezeti vezető.
- **FORRÁS:** https://arxiv.org/abs/2502.11242 · https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research

#### P0.3 — M3.B retraumatizáció-kockázat: triage-terv + „elemezni, ne eljátszani" 🟥
- **PROBLÉMA:** Az M3.B peula élőben **eljátszat** súlyos témákat (önsértés, bántalmazás, grooming) 15+ képzős madrichokkal, akik maguk is lehetnek érintettek. Nincs konkrét utógondozási/triage-pont, és a legsúlyosabb szituációk eljátszása retraumatizáló lehet (`SAFEGUARDING-REVIEW` 3).
- **AJÁNLÁS:** Pre-deployment „adverzariális" próba + incidens-út. Adjatok a képzőnek explicit triage-tervet (kit, hogyan, mikor von be, ha valaki krízisbe kerül vagy érintettséget fed fel), és a legsúlyosabb szituációkat **elemezzétek** (kártya/eset-leírás), ne játszassátok el.
- **LÉPÉSEK:**
  1. Írjatok explicit triage-tervet a peula-vezetőnek (krízis-jelek, kihez fordul, hogyan zár).
  2. A legsúlyosabb szcenáriókat (aktív önsértés) eset-elemzéssé alakítsátok eljátszás helyett.
  3. Trauma-érzékeny lebonyolítás review-ja: gyerekvédelmi felelős + mentálhigiénés szakember.
- **RÁFORDÍTÁS:** kicsi–közepes (1 új triage-segédlet + tartalom-átdolgozás + review).
- **GAZDA:** gyerekvédelmi felelős + mentálhigiénés szakember.
- **FORRÁS:** https://www.libertify.com/interactive-library/nist-ai-600-1-generative-ai-profile/ · https://www.solidaritynow.org/wp-content/uploads/2025/02/Manual-Trauma-Informed-Youth-Work_ENGLISH_compressed.pdf

#### P0.4 — Safeguarding minimum-kvíz konvergens megtartása (NE lazítsd!) 🟦
- **PROBLÉMA:** A C6/C11 feszültség (konvergens kvíz vs. nonformális) miatt csábító lenne minden kapunál divergens értékelésre váltani. DE az M3 gyerekvédelmi kvíz konvergenciája gyerekvédelmi okból **indokolt** — itt a „több helyes válasz" nonformális logika kockázatos (`IDEOLOGY-GATE-REVIEW` B3; `OPINION-AUDIT` C6).
- **AJÁNLÁS:** Az általános produktum/peer/reflektív értékelésre váltás MELLETT a gyerekvédelmi modulnál tartsd meg a konvergens minimum-kvízt mint nem-alkudható kaput: tényalapú megfelelés-rész (felismerés, jelzési kötelezettség, kihez fordulj) + szcenárió-kérdések, fix átmenő-küszöbbel (75–100% a kritikus jelzési tételeknél). A cél annak igazolása, hogy a madrich biztosan TUDJA és ALKALMAZZA a védelmi minimumot.
- **LÉPÉSEK:**
  1. Az M3-KAPU kvíz-komponensét tartsátok konvergensnek és szcenárió-alapúnak (a megírt item-bank már ilyen jellegű).
  2. Jelöljétek ki a kötelezően helyesen megválaszolandó kritikus itemeket (titoktartás, jelzési reflex, nem-nyomoz/nem-konfrontál).
  3. Dokumentáljátok, miért NEM divergens ez a kapu (safeguarding-minimum).
- **RÁFORDÍTÁS:** kicsi (megerősítés + dokumentálás; a kapu kétkomponensű felépítése már megvan).
- **GAZDA:** gyerekvédelmi felelős + pedagógiai stáb.
- **FORRÁS:** https://safeguarding.network/content/e-learning/keeping-children-safe-in-education-knowledge-check

#### P0.5 — AI-tartalom kétlépcsős lektorálási policy kimondása 🟦
- **PROBLÉMA:** Az AI-generált oktatási — különösen gyerekvédelmi/biztonsági — tartalom emberi szakértői lektorálást igényel; a mértékadó útmutatás (UNESCO) ezt nyomatékosan elvárja (C13). A 307 hézag eredete bizonytalan (lehet AI), de ettől függetlenül a forrás-anyag minőségbiztosítás nélkül futott (C8).
- **AJÁNLÁS:** Kétlépcsős kötelező lektorálás. 1. szint (általános modul-tartalom): képzett madrich/módszertani felelős pedagógiai-tartalmi átolvasása élesítés előtt. 2. szint (megemelt küszöb — minden gyerekvédelmi/mentális egészség/krízis/határsértés AI-tartalom): kötelező második, témaszakértői jóváhagyás. A lektor-checklistre a tényszerűség MELLÉ tegyetek pedagógiai-etikai szempontokat (15+ korosztály-megfelelőség, someres-érték összhang, reprezentációs torzítás).
- **LÉPÉSEK:**
  1. Írjátok le a kétszintű review-policyt a képzés indító dokumentumába (ki, mit, mikor hagy jóvá).
  2. Készítsetek egy rövid lektor-checklistet (tényszerűség + pedagógia + etika + bias).
  3. Kössétek ki: safeguarding-AI-tartalom 2. szintű jóváhagyás nélkül nem élesedik (kapcsolódik P0.1-hez).
- **RÁFORDÍTÁS:** kicsi (policy + checklist; a folyamat emberi, nem technikai).
- **GAZDA:** képzésvezető (1. szint) + gyerekvédelmi felelős (2. szint).
- **FORRÁS:** https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research · https://docs.modulos.ai/frameworks/nist-ai-rmf/generative-ai-profile

#### P0.6 — Terhelés őszinte, felfelé kerekített kommunikálása 🟦
- **PROBLÉMA:** A peula-percbontások feszesek, és lokálisan alulbecsült a terhelés (kiemelten az M7 végleges szintézis-produktum + M0/M2/M4 produktum-ideje) (C7). Az alá-ígért, majd nagyobbnak bizonyuló modul dokumentált lemorzsolódási ok.
- **AJÁNLÁS:** Kommunikáld a terhelést őszintén ÉS felfelé kerekítve — sávval és a felső érték hangsúlyozásával („2–3 óra, tervezz inkább 3-mal"). Lazítsd a feszes peula-percbontást: 10–15% puffer + minden aktivitásnál egy „core" és egy „elhagyható/rövidíthető" rész.
- **LÉPÉSEK:**
  1. Minden modul fejlécén tüntessétek fel a terhelést sávval, a felső értéket kiemelve.
  2. Az M7 szintézis-produktumhoz és az M0/M2/M4 produktumokhoz adjatok külön, reális percbecslést.
  3. Minden peula-percbontásba tegyetek 10–15% puffert és jelöljétek a „core / elhagyható" részeket.
- **RÁFORDÍTÁS:** kicsi (szöveg/becslés-finomítás; sok modulban a struktúra már megvan).
- **GAZDA:** pedagógiai stáb.
- **FORRÁS:** https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.902070/full · https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4673075/

---

### P1 — Közép táv (validitás + mélység)

#### P1.1 — M0 belépő-kvíz: döntsd el, kapu vagy completion — és építsd meg 🟦
- **PROBLÉMA:** Az M0 belépő-kvíz mint kapu nem build-ready: nincs authored item-készlet (csak témalista), nincs answer key, a cut-score ellentmondásos („60–70%" / „eredménytől függetlenül"), és a kompetencia 1 + 5 (éves ív, online dugma ishit) nincs lefedve (`ARCHITECTURE-REVIEW` 1–2; `GATE-VALIDITY` M0).
- **AJÁNLÁS:** Vagy mondjátok ki, hogy ez puha completion-jelző (akkor ne nevezzétek kapunak küszöbbel), vagy authored itemek + answer key + kritérium-referenciás küszöbindoklás. Témánként 2–3 item (összesen 10–12), cél→item leképező táblával, hogy a learning-analytics értelmes legyen.
- **LÉPÉSEK:**
  1. Döntés: kapu vagy completion-tracker.
  2. Ha kapu: írjátok meg a 10–12 itemet az M0.3 mintaminőségen, cél→item táblával (kompetencia 1 és 5 is kapjon itemet).
  3. Egységesítsétek a küszöböt (javasolt: ≥70% = zöld, alatta nem-blokkoló mentori jelzés).
- **RÁFORDÍTÁS:** közepes (item-authoring).
- **GAZDA:** pedagógiai stáb (item-szerző) + tech (Moodle-build).
- **FORRÁS:** https://safeguarding.network/content/e-learning/keeping-children-safe-in-education-knowledge-check · https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9358671/

#### P1.2 — Hiányzó item-bankok és rubrikák megírása (M3, M5, M6, M7) 🟦
- **PROBLÉMA:** A „mastery" kapuk EGY RÉSZÉNÉL a konkrét item-bank és/vagy rubrika hiányzott (C5). Konkrétan: M3 kapu-kvíz item-bank 🔴 + Assignment-rubrika 🔴; M5.4 rubrika 🟡; M6 szcenárió-kvíz item-bank 🔴; M7 Moodle Quiz item-bank 🔴 + analitikus rubrika 🟡 (`GATE-VALIDITY`). Az item-szám hiánya miatt a ≥80% küszöb statisztikailag nem védhető.
- **AJÁNLÁS:** Authentic / produktum-alapú feladat ELŐRE ismert, nyilvános rubrikával. Minden hiányzó kapuhoz: dedikált item-bank (min. 8–12 szcenárió-item, kulccsal és indoklással) ÉS analitikus, szintezett rubrika megfigyelhető indikátorokkal + 2–3 annotált mintamunkával (horgony). A rubrikát és a sztenderdet add ki ELŐRE.
- **LÉPÉSEK:**
  1. M3: dedikált, a leckéktől eltérő kapu-item-bank (8–10) + 4–5 soros megfigyelhető Assignment-rubrika kötelező itemekkel.
  2. M6: szcenárió-kvíz tényleges itemei kompetencia-alapú distraktorokkal + a játéklap-rubrika „oké"-szintjének operacionalizálása.
  3. M7: teljes 8–10 itemes kvíz-bank + 5 soros analitikus rubrika 3 szintleírással; a „Biztonság & gyerekvédelem" sor blokkoló.
  4. M5.4: 3–4 soros megfigyelhető rubrika (módszer–cél illeszkedés, valódi tanulástan-elem).
  5. Minden rubrikához 2–3 annotált mintamunka (gyenge/közepes/erős horgony).
- **RÁFORDÍTÁS:** nagy (a legnagyobb tartalmi tétel; több modult érint).
- **GAZDA:** pedagógiai stáb (item + rubrika) + mozgalmi szakértő (someres-tartalmú itemekhez).
- **FORRÁS:** https://citl.indiana.edu/teaching-resources/assessing-student-learning/authentic-assessment/index.html · https://link.springer.com/article/10.1007/s12528-021-09297-9 · https://www.edutopia.org/grant-wiggins-assessment

#### P1.3 — Kapu-filozófia kimondása: produktum az elsődleges, kvíz a formatív 🟥
- **PROBLÉMA:** A program nonformális nevelést hirdet, de több éles kapu konvergens kvízt is tartalmaz — feszültség, amelyet a program saját auditja is dokumentál (C6, C11; `IDEOLOGY-GATE-REVIEW` B). Az 5 éles kapu két pedagógiai családra esik anélkül, hogy a §5 ezt tudatosan kezelné (B4).
- **AJÁNLÁS:** Programmatic assessment-logika: ne egyetlen kapu-kvíz döntsön mastery-ről; a tét leválasztva a kvízről, a formatív (fejlődés) szétválasztva a szummatívtól (továbbléphet-e). Mondjátok ki a §5-ben az elvet: „Ahol van modulproduktum, a produktum rubrikás értékelése az elsődleges éles kapu; a kvíz formatív/diagnosztikus. Tisztán kvíz-kapu csak ott éles, ahol biztonsági minimum-tudás konvergens ellenőrzése indokolt (M3), és ott is szcenárió-alapú."
- **LÉPÉSEK:**
  1. Mozgalmi/pedagógiai döntés: fogadjátok el az elvet.
  2. M5: a kvíz → diagnosztikus, az éles kapu az M5.4 produktum rubrikás értékelése.
  3. M6: a játéklap-rubrika legyen az elsődleges éles kapu; a kvíz formatív vagy nyíltan divergens.
  4. Írjátok be az elvet a Program terv §5-be.
- **RÁFORDÍTÁS:** kicsi–közepes (az eszközök megvannak; ez átsúlyozás + elv-rögzítés, nem új fejlesztés).
- **GAZDA:** pedagógiai stáb (döntés) + mozgalmi vezetés (jóváhagyás).
- **FORRÁS:** https://pmc.ncbi.nlm.nih.gov/articles/PMC6283777/ · https://citl.indiana.edu/teaching-resources/assessing-student-learning/authentic-assessment/index.html

#### P1.4 — Peer/self-értékelés validitás-óvintézkedései (ha kapuként használjátok) 🟦
- **PROBLÉMA:** A produktum-/peer-/reflektív értékelés elismert nonformális-kompatibilis alternatíva, DE a minőségbiztosítás NEM automatikusan őrződik meg — csak rubrika, kalibráció/moderáció és tanulói felkészítés mellett (C14). A self-assessment validitása rendszeresen gyenge (Dunning-Kruger: 35,5% túlbecslés).
- **AJÁNLÁS:** Három egymást erősítő óvintézkedés: (1) horgonyzott rubrika + 2–3 annotált mintamunka (a legolcsóbb, önkéntes-vezetésre skálázható lépés); (2) több értékelő (2–3, pl. 2 társ + madrich-moderátor) + rövid kalibrációs ülés; (3) self-pont SOSE önállóan kapu — mindig külső jelzéshez (peer/madrich/produktum) kalibrálva, az eltérést megbeszélve.
- **LÉPÉSEK:**
  1. Ahol peer/Workshop a kapu (M6): adjatok analitikus rubrikát + horgony-mintákat + döntési szabályt a határesetekre.
  2. Tartsatok rövid kalibrációt: a csapat ugyanazt a mintamunkát pontozza, eltérést megbeszéli.
  3. Reflektív kapunál: a résztvevő először maga pontoz, majd megkapja a külső pontot, és az ELTÉRÉST beszélik meg.
- **RÁFORDÍTÁS:** közepes (rubrika-horgonyok + kalibrációs rutin).
- **GAZDA:** pedagógiai stáb.
- **FORRÁS:** https://pmc.ncbi.nlm.nih.gov/articles/PMC11515314/ · https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9358671/ · https://www.sciencedirect.com/science/article/abs/pii/S0191491X22001109

#### P1.5 — Reflektív kapu megerősítése bizonyíték-kötelezettséggel (Youthpass-modell) 🟦
- **PROBLÉMA:** Több puha kapu (M2 kapstone, reflexiós naplók) teljesítés-alapú, nem teljesítmény-alapú: a „leadva" státusz csak a beküldést igazolja, nem a kompetenciát; a leadás kiváltható felszínes tartalommal (`GATE-VALIDITY` M2).
- **AJÁNLÁS:** Self/reflektív validitás megerősítése bizonyíték-kötelezettséggel + támogatott dialógussal (Youthpass / CoE Portfolio modell). A reflexiónál ne smiley/önbevallás döntsön: kérjetek KONKRÉT leírást (mit csináltam, melyik kompetenciát hol mutattam meg), a 8 kulcskompetencia / a mozgalmi kompetenciakeret mint horgony köré. Rendeljetek minden résztvevőhöz egy „support person" madrichot.
- **LÉPÉSEK:**
  1. M2 kapstone: 4–5 soros megfigyelhető checklist-rubrika + 1 oldalas sablon (jelenleg nincs).
  2. Vezessetek be egyszerű leadási kritériumot kapuelemenként (pl. „minden értékhez EGY konkrét, viselkedés-szintű mondat — nem absztrakt értékszó").
  3. Kössétek a reflexiót a mozgalmi kompetenciakerethez mint horgonyhoz, support-person dialógussal.
- **RÁFORDÍTÁS:** közepes (rubrika + sablon + dialógus-rutin).
- **GAZDA:** pedagógiai stáb + mozgalmi szakértő (kompetenciakeret).
- **FORRÁS:** https://www.coe.int/en/web/youth-portfolio/help-self-assessment · https://www.youthpass.eu/en/help/faqs/keycompetences/ · https://www.coe.int/en/web/youth-portfolio

#### P1.6 — Ideológiai mélység: prompt→reflexió + problem-posing (NE frontális lecke) 🟥
- **PROBLÉMA:** Az ideológiai mélység híg, gyakorlatilag az M2.3 leckére koncentrálódik: a szocializmus interperszonális kvuca-etikára szűkül (strukturális dimenzió nélkül), a cionizmus relációs „kapcsolat Izraellel"-re, a hagshama a teljes MODULOK-korpuszban 0×-szor szerepel (C3; `IDEOLOGY-GATE-REVIEW` A2–A4).
- **AJÁNLÁS:** A mélységet NE egy új frontális leckével pótold (az ütközne a nonformális elvvel és a terhelés-realizmussal). Háromrétegű, olcsó megoldás: (1) minden ideológiai peulát zárj rendszeres SIKUM-reflexióval („mit jelent ez NEKED / a kvutzádnak / a világban?"); (2) problem-posing — az ideológiát dilemmaként vidd be, ne dogmaként („hol láttál olyat, hogy valaki egyedül nyert, de a csoport vesztett?"); (3) a madrich tudatos facilitátor-szerep-váltása (Oxfam 6 szerep), ne a Committed szerep túlhasználata. Erőforrás-igénye nulla: csak a kérdésfeltevés módja változik.
- **LÉPÉSEK:**
  1. Egészítsétek ki a szocializmus-pillért 1 híddal a tágabb társadalmi igazságosság felé (A3).
  2. Operacionalizáljátok a hagshamát NYITOTT, személyes praxis-kérdésként, az M0.1 „mi köze hozzám" kerethez kötve („mi az a mozgalmi érték, amit a saját életedben meg akarsz valósítani — és mi az első lépés?").
  3. Adjátok a madrichoknak az Oxfam 6 facilitátor-szerep eszköztárát + a közösen alkotott vita-alapszabályok rutint.
- **RÁFORDÍTÁS:** kicsi (kérdés-átfogalmazás + meglévő peula-formátum; NEM új tananyag).
- **GAZDA:** mozgalmi szakértő (mit jelent ma a hagshama nálatok — DÖNTÉS) + pedagógiai stáb (forma).
- **FORRÁS:** https://utoronto.scholaris.ca/server/api/core/bitstreams/b716eede-f1a0-43ee-97f9-0096c18ee818/content · https://en.wikipedia.org/wiki/Problem-posing_education · https://policy-practice.oxfam.org/resources/teaching-controversial-issues-a-guide-for-teachers-620473/ · https://www.livingvalues.net/about-lve

#### P1.7 — Terhelés tényleges mérése mini-felméréssel + mikroleckék 🟦
- **PROBLÉMA:** A terhelés-becslés tervezői optimizmuson nyugszik, nem mért adaton (C7). Az online leckék (10–20 perc) hosszabbak a microlearning 3–5 perces ideáljánál (C9 árnyalás).
- **AJÁNLÁS:** Mérd a TÉNYLEGES felkészülési időt egy 3 kérdéses mini-felméréssel a leckék/kvízek végén (mennyi időt vett, mennyire ismerős, mennyire nehéz), és a kommunikált percszámot a valós mediánhoz igazítsd. Az online leckéket vágd 2–5 perces, egy-koncepció-per-egység mikroleckékre. Ütemezd szét a modulokat spacinggel (3×40–50 perc) — ez NEM többletmunka, ugyanaz az idő hatékonyabban.
- **LÉPÉSEK:**
  1. Tegyetek a Moodle-kvízek/gate-ek végére opcionális 3 kérdést (idő / ismerősség / nehézség).
  2. Egy turnus adata alapján igazítsátok a kommunikált percszámot.
  3. A hosszabb online leckéket bontsátok egy-fogalmú mikroegységekre; egy modult bontsatok 2–3 növekvő-közű alkalomra.
- **RÁFORDÍTÁS:** kicsi–közepes (mini-felmérés olcsó; a chunkolás közepes).
- **GAZDA:** pedagógiai stáb + tech (Moodle-beépítés).
- **FORRÁS:** https://pmc.ncbi.nlm.nih.gov/articles/PMC10193725/ · https://www.compozer.com/post/how-long-should-microlearning-videos-be · https://learnexperts.ai/blog/spaced-practice/ · https://ie.nu.edu.kz/calculating-student-workload/

#### P1.8 — Curriculum-lyukak: korosztály-tanítás + peula-dramaturgia + capstone-horgonyok 🟦
- **PROBLÉMA:** Korosztályi/fejlődéslélektani alap sehol nincs TANÍTVA, de az M6/M7 méri (🔴). A peula 4-fázisú dramaturgiája feltételezett, de korábban egyik modul sem tanítja (🟡). A modul-produktumok nem állnak össze tisztán egy Peula v2-be (🔴 capstone-gap) — az M2 identitás és a Tuckman-modell zsákutcába fut (`CURRICULUM-IV`).
- **AJÁNLÁS:** Single-source, moduláris elemek: a korosztály-mátrixot és a peula-dramaturgiát EGY forrás-blokkban tanítsátok, amit több modul újrahasznosít. Vezessetek be explicit produktum-portfólió logikát: az M7 Peula v2 sablon nevesítse, honnan emeli át a célt (M5), módszert (M6), kvuca-illeszkedést (M3), emberi keretet (M2).
- **LÉPÉSEK:**
  1. Tegyetek rövid korosztály-tanító elemet az M3-ba vagy M6 elejére (6–10/11–13/14–16/16+ sávok), és kössétek a someres profilokhoz.
  2. Tegyetek minimál peula-dramaturgia (4 fázis) tanító elemet M5/M6-ba, amire az M7 Peula 11 pont épülhet.
  3. Az M7 sablonban tegyétek explicitté a produktum-átkötéseket; rögzítsétek a végleges Peula v2 leadás naptári pontját és felelősét.
- **RÁFORDÍTÁS:** közepes (2 új tanító mikroelem + sablon-átkötések).
- **GAZDA:** pedagógiai stáb + mozgalmi szakértő (someres profil-illesztés).
- **FORRÁS:** https://www.coe.int/en/web/compass/approaches-to-human-rights-education-in-compass · https://www.mindsmith.ai/blog/build-once-train-often-the-power-of-content-reusability-and-modular-design-in-elearning

---

### P2 — Hosszú táv (fenntarthatóság + minőségbiztosítás)

#### P2.1 — MVP-indulás: egy modul + egy kapu, ne a teljes architektúra 🟦
- **PROBLÉMA:** Túl-építés kockázata: egy LMS + H5P branching + analytics + AI rendszer nehéz egy 2-képzős önkéntes stábnak; a szakadék valós, dokumentált (C12; interjú-jelentés #1 kockázat).
- **AJÁNLÁS:** Indíts MVP-vel: az M0–M1-et vidd élesbe a legkisebb működő készletben (Moodle Page + 1 H5P + 1 fórum + 1 mastery-gate kvíz), a branching/analytics/AI funkciókat kapcsold ki az első körben. Cél: a Build–Measure–Learn ciklus lefuttatása egy madrich-csoporton, majd modulonkénti bővítés. Prioritizáld a „sweet spotot" (gyors győzelem + magas hatás): a fórum és a self-check kvíz alacsony komplexitás / magas hatás — ezek mennek elsőként.
- **LÉPÉSEK:**
  1. Élesítsétek M0–M1-et minimál készlettel, AI/branching/analytics kikapcsolva.
  2. Futtassátok egy turnuson, mérjetek (P2.4 metrikák).
  3. A tanultak alapján bővítsetek modulonként, a komplex elemeket a 2–3. fázisba tolva.
- **RÁFORDÍTÁS:** közepes (de MEGTAKARÍTÁS a big bang-hez képest).
- **GAZDA:** tech + képzésvezető.
- **FORRÁS:** https://trailhead.salesforce.com/content/learn/modules/nonprofit-cloud-implementation-best-practices/take-a-phased-approach · https://www.digitalocean.com/resources/articles/minimum-viable-product

#### P2.2 — Nevesített platform-gazdák + train-the-trainer skálázás 🟦
- **PROBLÉMA:** A fő szűk keresztmetszet a folyamatos tartalom- és kapu-karbantartás emberi munkaigénye (C12). A szoftver önmagában nem tartja a minőséget.
- **AJÁNLÁS:** Nevezzetek meg konkrét platform-gazdát minden karbantartási feladatra (hozzáférés, tartalom-frissítés, support, gate-nézés), mindegyikhez backuppal. Skálázzatok train-the-trainer / peer-content modellel: a végzett madrichok legyenek a következő kör fórum-moderátorai és peula-fejlesztői — a kapacitást a szervezeten belül termeljétek újra.
- **LÉPÉSEK:**
  1. Owner-mátrix: minden karbantartási feladathoz nevesített gazda + backup (az interjú-jelentés owner-mátrixára építve).
  2. Építsetek be „tartalom-örökbefogadás" lépést: tapasztalt önkéntes gondozza a saját modulját.
  3. A végzett madrichokat vonjátok be moderátorként/fejlesztőként.
- **RÁFORDÍTÁS:** közepes (folyamat-építés, nem fejlesztés).
- **GAZDA:** képzésvezető + szervezeti vezetés.
- **FORRÁS:** https://www.smallbusinesscoach.org/how-to-implement-lms-in-nonprofits-successfully/ · https://www.nonprofitlearninglab.org/post-1/volunteers-training-volunteers-how-the-train-the-trainer-model-enhances-training-and-volunteer-lead

#### P2.3 — Single-source tartalom + interaktivitás-költség döntési szabály 🟦
- **PROBLÉMA:** A H5P branching, szimulációk és AI-elemek karbantartási költsége sokszorosa a statikus tartalomnak (C12). A közös elemek (gyerekvédelmi alapfogalmak, SBI-modell) több helyen ismétlődnek.
- **AJÁNLÁS:** Tartsd moduláris, single-source elemekben a tartalmat — a közös blokkok EGY forrásból éljenek, hogy egyszer frissíts, ne nyolc helyen. Vezess be döntési szabályt: interaktív/branching elem csak ott, ahol a tanulási cél statikusan NEM érhető el. Kezdj Moodle core-aktivitásokkal (fórum + kvíz + assignment) és minimalista témával (Boost).
- **LÉPÉSEK:**
  1. Azonosítsátok a közös blokkokat (safeguarding-alapfogalmak, SBI), tegyétek egy forrásba egységes tag-rendszerrel.
  2. Döntési szabály: interaktivitás csak magas értékű, statikusan nem elérhető ponton.
  3. A gazdag H5P nagy részét helyettesítsétek „good enough" statikus + self-check kombóval.
- **RÁFORDÍTÁS:** közepes.
- **GAZDA:** tech + pedagógiai stáb.
- **FORRÁS:** https://www.mindsmith.ai/blog/build-once-train-often-the-power-of-content-reusability-and-modular-design-in-elearning · https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2022.866917/full · https://teachinghub.bath.ac.uk/guide/an-introduction-to-moodle-activities-and-resources/

#### P2.4 — Minőségbiztosítás: egy nevesített QA-gazda + 3 cselekvő metrika + PDSA 🟦
- **PROBLÉMA:** A README QA-szerepei placeholder-nevek; az „adatvezérelt finomhangolás" ígérete teljes analytics-dashboard nélkül lebeg (C12; README).
- **AJÁNLÁS:** Egy nevesített QA-gazda döntésenként (ne placeholder, ne megosztott felelősség), mérhető éves céllal. Döntés-specifikus mini-RACI (3–4 sablon: tartalom-módosítás, gate-küszöb hangolás, gyerekvédelmi frissítés) a teljes mátrix helyett. Három reális, automatikus metrika: (1) lecke completion rate, (2) gate pass-rate első próbára, (3) drop-off pont. A completion rate önmagában NE legyen a siker mércéje — kösd peula-megfigyeléshez (a tartó 3 mondatos észrevétele: alkalmazták-e élőben?). PDSA-mikrociklus EGY modulra (adopt/adapt/abandon), nem az egész programra.
- **LÉPÉSEK:**
  1. Nevezzetek ki EGY QA-gazdát + backupot, időkerettel (pl. havi 2 óra), a mozgalmi tisztségleírásban.
  2. Vezessetek be 3 metrikát + modulonkénti 3 kérdéses anonim záró-űrlapot, először EGY modulon pilotálva.
  3. Rögzítsetek éves QA-kadenciát (turnus-záró mini-review + éves program-review); minden mutatóhoz legyen felelős a beavatkozásra.
- **RÁFORDÍTÁS:** közepes (folyamat + szerep, nem dashboard-fejlesztés).
- **GAZDA:** QA-gazda (nevesített madrich-koordinátor).
- **FORRÁS:** https://umbrex.com/resources/data-governance-playbook/roles-responsibilities-and-raci-that-actually-works/ · https://nirn.fpg.unc.edu/blog/pdsa-cycles-improvement-and-implementation/ · https://360learning.com/blog/lms-analytics-maximize-learning-outcomes/ · https://trainingindustry.com/articles/measurement-and-analytics/10-key-corporate-learning-metrics-you-need-to-know/ · https://www.nonprofitlearninglab.org/post/volunteer-feedback-and-continuous-improvement-loops · https://www.jisc.ac.uk/guides/code-of-practice-for-learning-analytics

#### P2.5 — AI-provenance jelölés + verziózás + audit-nyom 🟦
- **PROBLÉMA:** A 307 hézag eredete bizonytalan; nincs prompt-nyom, modell-metaadat vagy generálási log (C8). Az AI-tartalom nyomon követhetősége hiányzik.
- **AJÁNLÁS:** Provenance-jelölés minden AI-érintett tartalmon (látható címke „AI-asszisztált — emberi lektor: [név], dátum" + ahol megoldható C2PA metaadat). Verziózás és audit-nyom: a Git/GitLab (amit már használtok) ingyen alkalmas — a commit-history az audit-nyom, a PR-review a jóváhagyás; a logot tartsátok meg legalább 6 hónapig.
- **LÉPÉSEK:**
  1. Egységes „AI-asszisztált + lektor + dátum" jelölés minden érintett leckén.
  2. A lektorálás fusson Git PR-review-n keresztül (jóváhagyás = merge).
  3. Tartsatok minimál accountability-rekordot (eszköz/modell, ki lektorálta, mi változott).
- **RÁFORDÍTÁS:** kicsi–közepes (a Git már megvan; ez konvenció + címke).
- **GAZDA:** tech + képzésvezető.
- **FORRÁS:** https://www.numonic.ai/blog/iptc-2025-c2pa-ai-provenance-metadata · https://www.cxtoday.com/security-privacy-compliance/ai-audit-trail-regulatory-scrutiny/

#### P2.6 — GDPR / adatkezelés a reflexiós mezőknél 🟥
- **PROBLÉMA:** A leckék több helyen kérnek érzelmileg érzékeny reflexiót (red flag, önsértés, „mikor kérnél segítséget"), de SEHOL nincs adatminimalizálási nyilatkozat, plain-language tájékoztató, megőrzési idő vagy törlési folyamat — 15+ célcsoportnál érzékeny személyes adat (`ARCHITECTURE-REVIEW` 3).
- **AJÁNLÁS:** Rögzítsétek a gyűjtés célját már gyűjtéskor (learning-analytics code of practice). Minden érzékeny reflexiós mezőhöz: plain-language tájékoztató (milyen adat, mire, meddig, kihez fordulhat) + megőrzési/törlési folyamat.
- **LÉPÉSEK:**
  1. Készítsetek rövid adatkezelési nyilatkozatot a reflexiós mezőkhöz.
  2. Rögzítsétek a megőrzési időt és a törlési folyamatot.
  3. Korhatár/hozzájárulás (15+) tisztázása a helyi jogi kerethez.
- **RÁFORDÍTÁS:** kicsi–közepes (jogi/szervezeti, nem technikai).
- **GAZDA:** szervezeti vezetés (jogi felelős) + gyerekvédelmi felelős.
- **FORRÁS:** https://www.jisc.ac.uk/guides/code-of-practice-for-learning-analytics

---

## 3. Mozgalmi/szervezeti döntés vs. szakmai/operatív

A terv tudatosan elkülöníti, mi tartozik a **mozgalom/vezetőség** hatáskörébe (érték-tartalom, kapu-filozófia, gyerekvédelmi policy), és mi **szakmai/operatív** (item-írás, rubrika, Moodle-build, mérés).

### 🟥 MOZGALMI / SZERVEZETI DÖNTÉS (NEM oldjuk meg helyettetek)
- **Ideológiai mélység és tartalom (P1.6):** mit jelent MA a hagshama nálatok; mennyi strukturális szocializmus / cionista önrendelkezés korosztály-arányos 15+-on; a „világi (szekuláris) humanista zsidóság" címke használata. Ezeket szándékosan nem írtuk a forrásba — mozgalmi/Judaica szakértő dönti.
- **Kapu-filozófia (P1.3):** elfogadjátok-e az elvet, hogy a produktum az elsődleges éles kapu, a kvíz formatív. Pedagógiai stáb + mozgalmi jóváhagyás.
- **Gyerekvédelmi policy (P0.1–P0.3, P2.6):** a felelős nevesítése; a ken alkohol-/dohány-kódexe; a napló-titoktartás megfogalmazása; a súlyos szituációk eljátszás-vs-elemzés döntése; a korhatár/hozzájárulás. Gyerekvédelmi felelős + vezetőség (egy ponton mentálhigiénés szakember).

### 🟦 SZAKMAI / OPERATÍV (a stáb/tech megcsinálja)
- Item-bankok és rubrikák megírása (P1.1, P1.2), peer/self-óvintézkedések (P1.4), reflektív-kapu sablon (P1.5).
- Terhelés mérése és kommunikálása, mikroleckék, spacing (P0.6, P1.7).
- Curriculum-horgonyok, korosztály- és dramaturgia-tanító elemek (P1.8).
- MVP-build, platform-gazdák, single-source, QA-metrikák, AI-provenance (P2.1–P2.5).

---

## 4. Mit NE csináljatok (a túl-építés ellen)

A vezérelv („kevesebb gépezet, több mozgalom") negatív oldala — ezeket a kutatás és az audit egybehangzóan ellenjavallja:

1. **NE indíts „big bang"-gel** — ne élesítsd a teljes 8-modulos rendszert egyszerre branching + analytics + AI-val. Ez felesleges komplexitást ad és lassítja a megtérülést (P2.1).
2. **NE építs teljes learning-analytics dashboardot** — három cselekvő metrika elég. Kerüld a „vanity" metrikákat (kattintás, online töltött idő, összes belépés) (P2.4).
3. **NE pótold az ideológiai mélységet új frontális leckével** — az ütközne a nonformális elvvel ÉS a terhelés-realizmussal. A mélység a chanich saját értelmezéséből nő, nem fentről (P1.6).
4. **NE válts MINDEN kaput divergens értékelésre** — a gyerekvédelmi minimum-kvíz maradjon konvergens. A „több helyes válasz" itt kockázatos (P0.4).
5. **NE használj gazdag H5P branchinget ott, ahol statikus + self-check is elég** — az interaktivitás karbantartási költsége arányosan nő (P2.3).
6. **NE bízd a safeguarding-review-t kulcsszó-szűrőre vagy automatikára** — kontextuális, emberi szakértői átnézés kell (P0.2, P0.5).
7. **NE hagyd a QA-felelősséget placeholderen vagy megosztva** — „a megosztott felelősség gyakran a felelősség kerülésének udvarias formája" (P2.4).
8. **NE ígérd a terhelést alá** — a váratlan terhelésnövekedés dokumentált lemorzsolódási ok; őszintén, felfelé kerekítve kommunikálj (P0.6).
9. **NE adj ki rubrika nélküli „mastery" kaput** — item-bank/rubrika nélkül a kapu auditálhatatlan és nem reprodukálható (P1.1, P1.2).

---

## 5. Javasolt sorrend / ütemterv (1 félév)

| Időszak | Fókusz | Tételek | Eredmény |
|---|---|---|---|
| **1. hónap** | Biztonság + bizalom élesítése | P0.1, P0.2, P0.3, P0.4, P0.5 | A program élesíthető: a gyerekvédelmi keret aláírva, a kockázatos tartalom javítva, az AI-policy kimondva. |
| **1–2. hónap** | Terhelés-őszinteség + MVP-előkészítés | P0.6, P2.1 (előkészítés) | Reális terhelés-kommunikáció; M0–M1 MVP build-kész. |
| **2–3. hónap** | Kapuk megépítése | P1.1, P1.2, P1.3 | M0 belépő-kvíz eldöntve/megépítve; M3/M5/M6/M7 item-bank + rubrika kész; kapu-filozófia kimondva §5-ben. |
| **3–4. hónap** | Validitás + mélység | P1.4, P1.5, P1.6, P1.8 | Peer/self-óvintézkedések; reflektív kapu megerősítve; ideológiai mélység + curriculum-horgonyok. |
| **4. hónap** | MVP élesítés + mérés | P2.1 (futtatás), P1.7 | M0–M1 egy turnuson élesben; tényleges terhelés mérve. |
| **5–6. hónap** | Fenntarthatóság + QA beüzemelése | P2.2, P2.3, P2.4, P2.5, P2.6 | Platform-gazdák, single-source, QA-gazda + 3 metrika, AI-provenance, GDPR-nyilatkozat. |
| **folyamatos** | PDSA + bővítés | P2.4 (mikrociklus) | A tanultak alapján modulonkénti bővítés és finomhangolás. |

**Kritikus út:** P0.1 → P0.5 → P2.1-előkészítés → P1.1/P1.2 → P2.1-futtatás. A P0-blokk nélkül a program NEM élesíthető felelősen; a P1.1/P1.2 nélkül a „mastery" címke nem fedett; minden más erre épül.

---

## 6. Forrásjegyzék

- https://pmc.ncbi.nlm.nih.gov/articles/PMC6283777/
- https://citl.indiana.edu/teaching-resources/assessing-student-learning/authentic-assessment/index.html
- https://link.springer.com/article/10.1007/s12528-021-09297-9
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9358671/
- https://www.coe.int/en/web/youth-portfolio/help-self-assessment
- https://www.youthpass.eu/en/help/faqs/keycompetences/
- https://www.coe.int/en/web/youth-portfolio
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11515314/
- https://www.sciencedirect.com/science/article/abs/pii/S0191491X22001109
- https://safeguarding.network/content/e-learning/keeping-children-safe-in-education-knowledge-check
- https://www.edutopia.org/grant-wiggins-assessment
- https://utoronto.scholaris.ca/server/api/core/bitstreams/b716eede-f1a0-43ee-97f9-0096c18ee818/content
- https://en.wikipedia.org/wiki/Problem-posing_education
- https://policy-practice.oxfam.org/resources/teaching-controversial-issues-a-guide-for-teachers-620473/
- https://www.livingvalues.net/about-lve
- https://www.coe.int/en/web/compass/approaches-to-human-rights-education-in-compass
- https://infed.org/mobi/the-world-of-the-jewish-youth-movement/
- https://www.coe.int/en/web/youth/manuals-and-handbooks
- https://livetoplant.com/education-systems-within-kibbutzim-what-makes-them-unique/
- https://ie.nu.edu.kz/calculating-student-workload/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10193725/
- https://www.compozer.com/post/how-long-should-microlearning-videos-be
- https://learnexperts.ai/blog/spaced-practice/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC5612372/
- https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2022.902070/full
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4673075/
- https://trailhead.salesforce.com/content/learn/modules/nonprofit-cloud-implementation-best-practices/take-a-phased-approach
- https://www.smallbusinesscoach.org/how-to-implement-lms-in-nonprofits-successfully/
- https://www.nonprofitlearninglab.org/post-1/volunteers-training-volunteers-how-the-train-the-trainer-model-enhances-training-and-volunteer-lead
- https://www.mindsmith.ai/blog/build-once-train-often-the-power-of-content-reusability-and-modular-design-in-elearning
- https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2022.866917/full
- https://www.lambdasolutions.net/en/blog/how-to-ditch-vanity-metrics-for-actionable-metrics-for-better-elearning
- https://teachinghub.bath.ac.uk/guide/an-introduction-to-moodle-activities-and-resources/
- https://www.unesco.org/en/articles/post-pandemic-learning-exploring-sustainable-open-education-resources-oer-business-models
- https://www.digitalocean.com/resources/articles/minimum-viable-product
- https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research
- https://www.unesco.org/en/articles/unesco-governments-must-quickly-regulate-generative-ai-schools
- https://docs.modulos.ai/frameworks/nist-ai-rmf/generative-ai-profile
- https://www.libertify.com/interactive-library/nist-ai-600-1-generative-ai-profile/
- https://predictionguard.com/blog/ai-governance-compliance-evidence-a-framework-for-nist-ai-rmf-nist-ai-600-1-owasp-and-eu-ai-act-audit-readiness
- https://www.cxtoday.com/security-privacy-compliance/ai-audit-trail-regulatory-scrutiny/
- https://www.numonic.ai/blog/iptc-2025-c2pa-ai-provenance-metadata
- https://arxiv.org/abs/2502.11242
- https://umbrex.com/resources/data-governance-playbook/roles-responsibilities-and-raci-that-actually-works/
- https://nirn.fpg.unc.edu/blog/pdsa-cycles-improvement-and-implementation/
- https://portico.inflexion.org/implement-pdsa-process/
- https://360learning.com/blog/lms-analytics-maximize-learning-outcomes/
- https://trainingindustry.com/articles/measurement-and-analytics/10-key-corporate-learning-metrics-you-need-to-know/
- https://www.nonprofitlearninglab.org/post/volunteer-feedback-and-continuous-improvement-loops
- https://www.jisc.ac.uk/guides/code-of-practice-for-learning-analytics

---

*Megjegyzés a hatókörről: ez a terv az `_AUDIT/` korpusz verifikált megállapításaira épül és a 6 kutatott téma (értékelés-redesign, ideológia-mélység, terhelés-realizmus, fenntarthatóság-MVP, AI-governance, minőségbiztosítás) ajánlásait illeszti rájuk. A 🟥 tételek mozgalmi/szervezeti döntésre várnak; a 🟦 tételek a stáb/tech által megvalósíthatók.*
