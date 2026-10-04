# Kérdések és döntések – összesítő (2026-10-04)

> **Audit trail, nem kánon és nem tananyag.** Egy helyen gyűjti a projekt **projektgazdai döntéseit** és azt, ami a
> megvalósításukból még hátravan. A döntések kánoni helye nem ez a fájl: a szó szerinti válaszok a hivatkozott döntési
> jegyzőkönyvekben (`01 Fejlesztés/04 Audit/`), a lezárt tételek a `02 Tervezet/Emberi jóváhagyás szükséges.md`-ben és
> a `02 Tervezet/Média-assetek/PRODUCTION-DECISIONS.md`-ben élnek. Ha ez a fájl eltér tőlük, azok az irányadók.
> Állapot: `main` @ `ea36214`, `RELEASE-VERDICT: NO-GO`.

**Projektgazdai döntésre váró kérdés: 0** (2026-10-04). A korábban nyitott 24 kérdést a projektgazda megválaszolta
(`2026-10-04 Projektgazdai döntések – összesítő 24 kérdése.md`). Ami hátravan, az megvalósítás, szakértői QA, runtime-
ellenőrzés vagy külső bizonyíték — ezeket nem szabad újra „nyitott projektgazdai kérdésként” visszahozni.

**Állapotok** (a Q-REL-3 döntés kánoni lánca): `OWNER_DECIDED` → `EXPERT_QA` → `IMPLEMENTED` → `RUNTIME_VERIFIED` →
`RELEASE_APPROVED`; továbbá `SUPERSEDED`, `REOPENED`. **Jelölés:** 🔴 a release vagy a programlogika szempontjából
kritikus · 🟠 fontos · 🟡 kisebb.

---

# I. Mi van hátra a 2026-10-04-i döntésekből

**Megvalósítás módja:** `course-fix` = tananyag- és kánondokumentum-módosítás javítócsomaggal, amit a projektgazda
indít; `eszköz` = `tools/` vagy `.github/` módosítás (Claude kérésre elkészíti, PR-ben); `GitHub` = repó-beállítás vagy
history-művelet (csak a projektgazda vagy a repó-admin); `VO QA` = a privát VO QA-repóban; `QA` = a megnevezett szerep
írásos bizonyítéka.

| ID | Állapot | A döntés röviden | Hátravan | Mód |
|---|---|---|---|---|
| 🔴 Q-REL-1 | OWNER_DECIDED | Külön `CONTROLLED_PILOT`; lánc: `INTERNAL_STAGING → CONTROLLED_PILOT → GENERAL_RELEASE → PROGRAM_TRANSFER_VALIDATED`; a 6 terepi peula utólagos programtranszfer-validáció, nem release előtti kapu | `RELEASE-READINESS.md` állapotmodellje; a `content_integrity.py` PROGRAM-TRANSFER logikája (ne a checkboxokból jöjjön a release-szemantika); az issue #9 szövege | course-fix + eszköz + GitHub (issue) |
| 🔴 Q-REL-2 | OWNER_DECIDED | Nincs pufferhét; bukott éles kapu után a következő modul tanulási része nyílhat, a következő éles kapu és a magas tétű előrehaladás blokkolt; F-peula a megerősítés utáni hétfőn, javító határidő szerda 18:00 | Az LMS-manifest és a Program terv kapu-szabályai; ütemezési invariáns a checkerben | course-fix + eszköz |
| 🟠 Q-REL-3 | OWNER_DECIDED | A „LEZÁRVA” felbontása: `PROPOSED → OWNER_DECIDED → EXPERT_QA → IMPLEMENTED → RUNTIME_VERIFIED → RELEASE_APPROVED`, + `SUPERSEDED`, `REOPENED` | A HUM-fájl állapotjelölése; a lezárási szabály a checkerben és a `.claude/rules/safety-and-human-gates.md`-ben | course-fix + eszköz (governance) |
| 🟠 Q-REL-4 | OWNER_DECIDED | Péntek 18:00, Europe/Budapest | A központi naptár és a határidő-szabály (HUM-OPS-01, manifest) | course-fix |
| 🔴 Q-GH-1 | OWNER_DECIDED / IMPLEMENTATION_PENDING | History-tisztítás (`git filter-repo`, force push, GitHub Support, újraklónozás) a ruleset előtt | Végrehajtás | GitHub (projektgazda) |
| 🔴 Q-GH-2 | OWNER_DECIDED | `main` ruleset: PR, ≥1 approval, CODEOWNER approval, kötelező `content-integrity` + `media-manifest`, unresolved conversation tiltás, törlés és force push tiltás; merge commit marad. CODEOWNERS szerepek szerint | **A CODEOWNERS valódi GitHub-fiókjai** (Memuna + helyettes/Ros Hinuh, DPO/jogi felelős, producer, a11y-felelős, repó-admin) — ezeket a projektgazda adja meg; utána a `CODEOWNERS` fájl; a ruleset bekapcsolása a Q-GH-1 után | eszköz + GitHub |
| — Q-GH-3 | RELEASE_APPROVED / CLOSED | Az #6 issue 2026-10-02 óta lezárt, a #12-re hivatkozó lezáró kommenttel (2026-10-04-én ellenőrizve) | nincs | — |
| 🟡 Q-GH-4 | OWNER_DECIDED | `SECURITY.md`, `CONTRIBUTING.md`, Dependabot (`github-actions`, heti); az actions teljes commit-SHA-ra pinelve; az `openpyxl` fix verzió | A fájlok és a workflow-pinek (a read-only workflow-allowlisttel összhangban) | eszköz |
| — Q-PED-1 | OWNER_DECIDED | A HUM-GOV-01 marad: egyéni minimum csak a „biztonság és határtartás” sor ≥1; az 1,6/2 program-KPI | nincs (nincs változás) | — |
| 🟠 Q-PED-2 | OWNER_DECIDED | A terepgyakorlat 9 rubrikasorának 0/1/2 leírása (a döntési jegyzőkönyv táblázata szerint) | A `Terepgyakorlat – 2. félév.md` rubrikája | course-fix; QA: módszertani felelős |
| 🟠 Q-PED-3 | OWNER_DECIDED | M3.A 4.3: 2 + 8 + 5 perc = 15 (kiscsoport 10 → 8, átbeszélés 5 perc, 3 kártyával) | Az M3.A percei | course-fix; QA: modulgazda |
| 🟡 Q-PED-4 | OWNER_DECIDED | M3.1: „A modell szemüveg, nem menetrend: …” mondat | Az M3.1 szövege | course-fix |
| 🟡 Q-PED-5 | OWNER_DECIDED | M5.3 forrásjegyzék: Dunlosky et al. 2013, Cepeda et al. 2006, Rowland 2014 | A pontos bibliográfiai adatok elsődleges forrásból; az M5.3 szövege | course-fix |
| 🟡 Q-PED-6 | OWNER_DECIDED | „strukturált szakértői küszöb-megállapítás (Angoff-elemekkel)”; két szakértő, utólagos kalibráció a pilot itemadataiból | `Program terv.md` (és a hivatkozó helyek) | course-fix |
| 🟡 Q-PED-7 | OWNER_DECIDED | Az `M1.1-NAR-05` is VO D-17.3 hatálya alá tartozik | A narrációs címke; a VO-mérés | course-fix + VO QA |
| 🔴 Q-LEG-1 | OWNER_DECIDED (operatív) | A „csak deployer” állítás törlendő; legalább deployer, a saját néven működő AI-segédnél provider/downstream provider szerep is felmerül; addig a szigorúbb, kettős szerepű compliance az alap | Az adatvédelmi/AI-dokumentumok érintett mondatai | course-fix; **QA: jogi felelős (release-bizonyíték)** |
| 🟠 Q-LEG-2 | OWNER_DECIDED (operatív) | A V1 tartalmi kapu is; a VO D-08 nem fedi le; tényleges gondviselői tájékoztatás a megnevezett elemekkel, bizonyíték nélküli jogtisztasági állítás nélkül | A V1 tartalmi előírása (`RIGHTS-EVIDENCE.md` és kapcsolódó helyek) | course-fix; **QA: Memuna + DPO** |
| 🟠 Q-LEG-3 | OWNER_DECIDED | A V2-ben külön nagykorúsági nyilatkozat; a nyilvántartás csak „ellenőrizve: igen/nem + dátum + ellenőrző szerepe” | A V2 előírása a média-dokumentumokban | course-fix; QA: DPO |
| 🟡 Q-LEG-4 | OWNER_DECIDED (operatív) | Valóban anonim papír munkalap és hanih-visszajelzés: nincs 6. cikk szerinti jogalap; visszaazonosítható digitális megoldásnál jogos érdek + DPO érdekmérlegelés; mentori jegyzet: jogos érdek | Az adatkezelési mátrix két új sora | course-fix; **QA: DPO** |
| 🟡 Q-LEG-5 | OWNER_DECIDED (operatív) | QR-kilépőkártya: Moodle Feedback, `Record user names = Anonymous`, nem completion-feltétel, nem „valóban anonim” tájékoztató, nyers válaszok 90 nap, QR mellett szöveges URL | Az M7 kilépőkártya és az adatkezelési mátrix | course-fix; **QA: DPO** |
| 🟠 Q-MED-1 | OWNER_DECIDED | A/B/C média-MVP; a manifeszt `release_phase: A/B/C` mezője a scope-freeze; nem a 415/903 teljes legyártása a release-feltétel | A manifeszt-séma és a besorolás (`tools/media_manifest.py` + asset-szintű érték vagy szabály szerinti alapérték) | eszköz + course-fix |
| 🟡 Q-MED-2 | OWNER_DECIDED | `M1.1-NAR-03`, `M1.2-NAR-02`, `M1.2-NAR-03`, `M3.1-NAR-02` = animáció hangsávja (felirat + leirat); `M4.1-NAR-02` = önálló dia-narráció (mellett látható leirat) | Az öt asset a11y-jegyzete | course-fix; QA: a11y-felelős |
| 🟡 Q-MED-3 | OWNER_DECIDED | Az M1.3 mobilos kérdésgomb címkéje: „Kérdés: melyik az SBI-mondat?” | Az M1.3 megvalósítási jegyzete | course-fix |
| 🟡 Q-MED-4 | OWNER_DECIDED | A képleírás 5. része alatt a 2. verzió záróképe marad, az S/B/I megfeleltetés sorban újra felvillan (vizuális recap), utána áll meg a videó | Az `M1.3-VID-01` `spec` mezője | course-fix |

## Bizonyíték-kapuk (nem döntés: a megnevezett szerepek írásos bizonyítéka zárja; Claude nem írja be)

- **Release-blokkolók** (`content_integrity.py --release-report`): RUNTIME-ACCEPTANCE (17), LMS-BUILD (52),
  SAFEGUARDING-CHECKLIST (11), PRIVACY-CHECKLIST (7), A11Y-CHECKLIST (20), PROGRAM-TRANSFER (1); gyártási szabály: R2, R3.
  A Q-REL-1 megvalósítása után a PROGRAM-TRANSFER kapu helye megváltozik.
- **UE-BIZT-6:** `VOICE-RIGHTS-REGISTER` nem személyes hivatkozása, jogi/adatvédelmi minősítés, AI Act 50. cikk (4)
  minősítése, a Memuna átnézése (G1).
- **A Memuna release előtti írásos QA-ja** (2026-10-02-i döntés).
- **Jogi és DPO-QA** a Q-LEG-1…5 operatív döntésein.
- **VO QA-repó feladatai** (onnan indított sessionből): az M1.3 képleírás hallgatási próbája (K8) és újraidőzítése; a
  második hang kalibrálása; a voice-ID a gyártási konfigurációban; a „nagykorúság ellenőrizve” bejegyzés; az
  `M1.1-NAR-05` mérése (Q-PED-7).

## Döntés nélkül, objektíven javítható (csak indítani kell)

- **M6 nyelvi javítás:** 55 objektív tétel és a 23 döntés átvezetése — `/course-fix "01 Fejlesztés/04 Audit/2026-10-04
  Nyelvi review – M6, Anna-baseline összevetés.md"`.
- **Leirat-sor a korpuszban:** az M6-NY-D22 (UE-IMPL-4 lezárva) minden modulra szól: ahol „mellől elérhető” leirat áll,
  „mellett látható” kerül a helyére.
- **„Workshop” mint Moodle-tevékenység:** ahol a „Workshop → műhely” csere a Moodle Workshop nevét is lecserélte, vissza
  kell állítani (M6-NY-D20).
- **`RELEASE-READINESS.md` régi bizonyítékszámai** (417 / 902 / 143 → 415 / 903 / 150) — külső audit 2026-10-04 P1.3.
- **Nyelvi review a többi modulra:** `/course-review M3 --lens language`, majd M4, M7, M2, M1, M5, M0, Z.

---

# II. Megválaszolt kérdések (időrendben)

## 2026-10-02 — HUM-tételek és maradék kérdések

Forrás: `2026-10-02 Projektgazdai döntések.md` (1–3. válasz); a lezárt tételek: `02 Tervezet/Emberi jóváhagyás
szükséges.md`. A „LEZÁRVA” a Q-REL-3 szerint `OWNER_DECIDED`-et jelent, nem release-készséget.

| ID | Tárgy | Állapot |
|---|---|---|
| HUM-SAFE-01 | Helyi gyermekvédelmi jelzési lánc | LEZÁRVA |
| HUM-SAFE-02 | Négyszemközti / safer-working szabály | LEZÁRVA |
| HUM-SAFE-03 | A madrih saját érintettsége és a kiskorú madrih státusza | LEZÁRVA |
| HUM-SAFE-04 | Alkohol- és dohányzási szabály | LEZÁRVA |
| HUM-SAFE-05 | Stáb-alkalmasság és gyermekvédelmi felkészítés | LEZÁRVA |
| HUM-PRIV-01 | Moodle-adatkezelési mátrix | LEZÁRVA |
| HUM-PRIV-02 | Fotó, videó, hang és kézírás | LEZÁRVA |
| HUM-PRIV-03 | Z.4 visszajelzés anonimitási szintje | LEZÁRVA |
| HUM-PRIV-04 | Külső generatív AI tanulói használata | LEZÁRVA |
| HUM-OPS-01 | Központi ütemezés | LEZÁRVA |
| HUM-OPS-02 | Támogatási kontaktok és mentori kapacitás | LEZÁRVA |
| HUM-A11Y-01 | Hozzáférhetőségi jóváhagyó szerepkör | LEZÁRVA |
| HUM-PED-01 | Az M4 szakmai lektorálása | LEZÁRVA |
| HUM-GOV-01 | Terepgyakorlat rubrika ↔ KPI megfeleltetés | LEZÁRVA (a Q-PED-1 megerősítette) |
| HUM-SOMER-01 | Izrael/cionizmus és béke/palesztin dimenzió helyi megfogalmazása | LEZÁRVA |
| HUM-SOMER-02 | Kvuca-korosztályok és írásmód (`madrih`, `hanih`, `hágsámá`, `dugma isit`, `Leviatán`) | LEZÁRVA |
| HUM-SOMER-03 | Hágsámá helyi megfogalmazása | LEZÁRVA |
| HUM-MEDIA-01 | Vizuális rendszer (D1) | LEZÁRVA |
| HUM-MEDIA-02 | Hangjogosultság és ElevenLabs-hang létrehozása; nyilvántartás; git-előzmények tisztítása | LEZÁRVA |
| HUM-MEDIA-03 | HeyGen/avatar és média-jogok | LEZÁRVA |

**A 2. válasz** („A 21 maradék kérdés, végleges válasz”) és **a 3. válasz** (12 maradék kérdés, „ajánlás szerint”):
izrael/palesztin tanulói szöveg; M4 szakmai review; V1 időkeretek pilot nélkül; központi naptár; adatvédelmi mátrix,
jogalap és megőrzés; AI-szolgáltató; 1:1 és „ha téged is érint” tanulói szöveg; D1 vizuális rendszer; M0 belépőkvíz;
a javító próbálkozás csak az F-peula után; kiegészítő naptár; a Memuna release előtti írásos QA-ja; gondviselői és
résztvevői médiahozzájárulás; új megőrzési sorok; az M2.1 identitás-válasz nem tárolódik; kapucímkék
(„Teljesítve” / „Még nem teljesítve”). A maradék pontjait a 2026-10-04-i Q-PED-2, Q-PED-3, Q-LEG-4 és Q-LEG-5 zárta.

## 2026-10-03 — VO 2. fázis (D-01…D-23)

Forrás: `2026-10-03 Projektgazdai döntések – VO 2. fázis.md`; nyilvántartás: `PRODUCTION-DECISIONS.md` „Lezárt
döntések”.

| ID | Tárgy |
|---|---|
| D-01 | A két hang létezik, a hanghasználati jog tisztázott, a tulajdonosok hozzájárultak |
| D-02 | Gyártási modell (`eleven_v4`) és beállítások |
| D-03 | Kanonikus kiejtési szótár |
| D-04 | A B4-ben fülre jóváhagyott kiejtések kötelezők (madrih, hanih, Tuckman) |
| D-05 | A Leviatán kiejtése; az írott alak marad |
| D-06 | Zmán Kvucá és dugma isit kiejtése elfogadva |
| D-07 | A 112 kimondva „száztizenkettő” |
| D-08 | Konzervatív AI-átláthatóság, harmadik fél aláírásának állítása nélkül |
| D-09 | Szövegnormalizálás |
| D-10 | Szünetpolitika (központozás; utómunkában 0,6–1,0 mp) |
| D-11 | Hangsúly: a jelentést hordozó hangsúly nem sérülhet |
| D-12 | Mester-hangformátum |
| D-13 | A kiejtés kanonikus forrása a VO QA-repó B4-regisztere; P-NAR |
| D-14 | M1.3 kétszereplős dialógus (a K4 módosította) |
| D-15 | M4.1 karakterjelenetek |
| D-16 | Az `M5.3-NAR-01` és az `M7.1-NAR-02` nem készül el |
| D-17 | Időzítés: a keret a mért természetes hosszhoz igazodik |
| D-18 | Az `M1.3-VID-01` hangalámondásos képleírást kap |
| D-19 | Csak hangos narráció: a mellett látható leirat a szöveges ekvivalens |
| D-20 | Egy visszatérő készlet-avatar a kanonikus narrátorhanggal |
| D-21 | A D9 AI-címke helye csak hangos narrációnál |
| D-22 | A régi kiejtési szótárak sorsa |
| D-23 | A további hallgatási tételek az ajánlott alakokkal |
| 2026-10-03-A | A nyilvános repóban a hangok csak szerepnéven szerepelnek |
| 2026-10-03-B | Nincs automatikus lejátszás |

## 2026-10-03 — VO 2. fázis, kiegészítés (K1–K8)

Forrás: `2026-10-03 Projektgazdai döntések – VO 2. fázis, kiegészítés.md`.

| ID | Kérdés | Válasz |
|---|---|---|
| K1 | Hangnév-utalás a nyilvános döntésmásolatban | Semlegesítve (a félmondat kimaradt) |
| K2 | A csak hangos narrációk a11y-jegyzete | Mindre, egységesen a VO D-19 szerint |
| K3 | A voice-ID helye | Csak a VO QA-repó gyártási konfigurációjában |
| K4 | A második hang az első gyártási körben | Az M1.3 Madrih B szerepét már most a második hang mondja (kalibrálás után) |
| K5 | A forrás-beszélők nagykorúsága | Projektgazdai tényközlés: nagykorúak (formális igazolás bizonyíték-kapu) |
| K6 | Nagykorúság a hangjogosultsági nyilvántartásban | „ellenőrizve: igen/nem”, dátum, az ellenőrző szerepe; életkor, születési dátum nélkül |
| K7 | Az M1.3 képleírás ikon-hozzárendelésének helye | Madrih B válasza után, egy 5. részben, a kérdés előtt |
| K8 | Ha az M1.3 hallgatási próbája elbukik | Előbb hangsúly, tempó, szünet, keverés; ha ez sem elég, a hozzáférhetőségi felelős dönt |

**Folyamat:** a PR-ek merge-módja merge commit (2026-10-03).

## 2026-10-04 — M6 nyelvi review (M6-NY-D1…D23)

Forrás: `2026-10-04 Projektgazdai döntések – M6 nyelvi review.md`.

| ID | Kérdés | Válasz |
|---|---|---|
| D1 | NYELV-501: a „kibillenés” önmagában elindítja-e a jelzési utat? | Nem, csak a feltárás; a kibillenést az M0.A mini-protokoll kezeli |
| D2 | NYELV-301/406: a „Fontos” dobozokban rövid utalás vagy az öt lépés szó szerint? | Utalás marad (nyelvi javítással) |
| D3 | NYELV-101: a kvízben a Memuna bevonása feltételes vagy mindig? | Feltételes, mint az M6.A („ha valaki erősen érintett”) |
| D4 | NYELV-602: az M6.B „kinek jelzel” milyen helyzetre szól? | Érzelmi megterhelődés: a Memunának jelzel (M6.A:180) |
| D5 | NYELV-103: R1 „pontosan 1” vagy „legalább 1” cél? | Legalább 1 |
| D6 | NYELV-104: mi különbözteti meg az R2 „Oké” és „Erős” szintjét? | Erős = legalább 1 M3.2-es korosztály-jellemzővel indokol |
| D7 | NYELV-115: mi kötelező a gyenge kvízeredmény után? | A stáb figyel (kötelező), a mentori egyeztetés ajánlott |
| D8 | NYELV-410: egységesíthető-e az M6.3 kvízopciók személye? | Igen (✅ és tartalom változatlan) |
| D9 | *Dugma isit* használata az M6-ban | Csak a madrih személyes példamutatására |
| D10 | NYELV-404: van-e Somer zászló- és színhagyomány? | Van, a hivatkozás marad |
| D11 | NYELV-214: az M6.1 B kártyája | Az 5. kategória (mélyebb élményjáték) példája |
| D12 | NYELV-601: kiesős játék a szűrőben | Csak a tét nélküli kerülendő (az 572. sort pontosítani kell) |
| D13 | NYELV-402: „az mondhatja csak a viselő nevét” | Kikerül |
| D14 | NYELV-405: „mi van rajtunk, mi nincs” | „mi kerül rá, mi nem” |
| D15 | NYELV-411: „(cél, kérdések, inkluzivitás)” | Elírás: „(cél, inkluzivitás, variációk)” |
| D16 | NYELV-503: az 5C-T napzárás utalásai | „egy csoport a nap végén összegzi, mi volt jó” / „Nektek mi volt ma egy jó pillanat?” |
| D17 | NYELV-610 (b): „identitás-sérüléshez” | „identitást sértő megjegyzéshez” |
| D18 | NYELV-610 (c): „félplénum” | A csoport fele (két félcsoport) |
| D19 | NYELV-610 (d): „(ha van, 2–3 perc)” | Ha van rá idő |
| D20 | NYELV-610 (e): „élő műhely” vagy Moodle Workshop? | Moodle Workshop (az eredeti értelem) |
| D21 | NYELV-613: a 4.2.1 „Biztonsági keret +” címrésze | Kikerül a címből |
| D22 | NYELV-403 / UE-IMPL-4: elég-e a gombbal megnyitható leirat? | Nem: a médiaelem mellett látható kell (UE-IMPL-4 lezárva) |
| D23 | NYELV-404/2: az érzékenységi szabály a mozgalmi jelképekre is vonatkozik? | Igen |

## 2026-10-04 — Az összesítő 24 kérdése (Q-REL, Q-GH, Q-PED, Q-LEG, Q-MED)

Forrás: `2026-10-04 Projektgazdai döntések – összesítő 24 kérdése.md` (a válasz szó szerint, és függelékben a 24
eredeti kérdés). A döntések rövid tartalma és a hátralévő teendők: I. rész.
