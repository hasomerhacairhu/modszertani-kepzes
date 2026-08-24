# Release audit – 2026-08-25

## Scope

Teljes repository- és commit-history alapú stabilizáció Anna 2026.07.20–08.12 közötti kézi auditja után. A vizsgálat kiterjed: konstruktív alignment, modulok/kapuk, safeguarding, kiskorúak/adatvédelem, AI, fejlődéslélektan, Moodle/H5P implementálhatóság, accessibility, repo-integritás, terminológia, program-transzfer és release-governance.

## Eredmény

**Pedagógiai architektúra: erős. Release: NO-GO a globális kapuk lezárásáig.**

A stabilizáció objektíven javítható regressziókat javít (duplikátumok, törött útvonalak, belső ellentmondások, félrevezető runtime/jogi állítások), de nem hamisít szakértői aláírást.

### Kritikus, végrehajtott változások

- M1/M3 duplikált kánoni fájlok eltávolítása és linkkorrekció.
- M1 feedback/alignment és titoktartási keret korrekció.
- M3 jogi szerepleírás pontosítása; kiskorú madrich nem kap önálló hatósági/jogi döntéshozó szerepet.
- M3.2 determinisztikus életkori/„amygdala gáz – PFC fék” állítások helyett fejlődési heurisztika + egyéni/context variability.
- M3.B súlyos safeguarding-helyzeteknél harmadik személyű esetanalízis az alapértelmezés, nem traumatizáló szerepjáték.
- M6.A kiesés/székszerző ellentmondás megszüntetése.
- M6.4 cél ↔ completion alignment: legalább 3 eset.
- AI Act provider/deployer kötelezettségek szétválasztása; C2PA best practice, nem univerzális deployer-kötelezettség.
- M7 külső AI: szervezetileg jóváhagyott eszköz, kiskorú terms/permission, no-AI alternatíva, sensitive-data tiltás.
- M7.4 v1/v2 fogalmi rend: M7.4 = v1, M7.B után = v2.
- Z.3 minor-role korrekció; Z.4 unsupported H5P Documentation Tool resume helyett Moodle Assignment draft.
- Accessibility: prerecorded synchronized videónál captions-követelmény egyértelmű.
- Release governance, LMS manifest, runtime acceptance, privacy, safeguarding és terepgyakorlati kontrollréteg hozzáadva.

## Külső validáció – elsődleges / magas minőségű források

- Gyvt. 17. §, Nemzeti Jogszabálytár: https://njt.hu/
- 2026 gyermekjóléti módszertani útmutató és jelzőrendszeri protokoll, kormányzati források.
- GDPR, különösen Article 8: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- EU AI Act, konszolidált Article 50: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng
- WCAG 2.2, SC 1.2.2: https://www.w3.org/TR/WCAG22/
- H5P Documentation Tool / Branching Scenario community + official docs: https://h5p.org/
- OpenAI aktuális Terms/age requirements: https://openai.com/policies/terms-of-use/ és https://help.openai.com/
- Kirschner & De Bruyckere (2017), digital native/multitasker myth.
- Frontiers in Psychology (2024), learning-styles matching meta-analysis, DOI 10.3389/fpsyg.2024.1428732.
- Kortárs adolescent-development áttekintések és nagy mintás executive-function kutatások: Nature Reviews Neuroscience / Nature Communications.
- Hasomer Hacair Hungary aktuális nyilvános Somer–Magyar szótár és programoldalak: https://somer.hu/

## Nem automatizálható P0

A `RELEASE-READINESS.md` globális kapui. Ezeket issue-ként is nyitni kell, felelőssel és bizonyítékkal kell lezárni.
