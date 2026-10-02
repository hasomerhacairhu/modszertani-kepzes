#!/usr/bin/env python3
"""Deterministic tests for the Asset Manifest v2 compiler.

Two layers:

* **Fixture tests** build a throwaway corpus in a temp directory and assert what
  the compiler accepts, rejects and derives. They are hermetic — no network, no
  clock, no dependency on the real curriculum.
* **Corpus tests** run against this repository. They are the ones that would
  catch the failure the v1 architecture could not see: a generated file that no
  longer matches the current Markdown, a historical row that lost its
  disposition, or learner-visible text quietly changed by the migration.

Run:  python3 -m unittest tools.test_media_manifest -v
"""

from __future__ import annotations

import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import contextmanager
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import media_manifest as mm  # noqa: E402
import media_migrate_v2 as mig  # noqa: E402

#: The commit the migration started from. The content invariant is measured
#: against it: everything the migration added must be strippable back to this.
BASELINE_COMMIT = "a8629732e46eb489644dc90a624e6c8466612eda"




# Approved filename migrations in the 2026-09-29 cleanup. The content-invariant
# guard still compares each current file to its historical baseline content; this
# map only tells git which pre-rename path carried that baseline.
FINAL_CLEANUP_2026_09_29_RENAMES = {
    "02 Tervezet/Modulok/M0/Online leckék/M0.3 – Hogyan működik a Moodle, H5P és a kapu.md":
        "02 Tervezet/Modulok/M0/Online leckék/M0.3 – Hogyan működik a Moodle, H5P és a gate.md",
    "02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, visszajelzés – Önismeret & visszajelzés – Johari + SBI.md":
        "02 Tervezet/Modulok/M1/M1 – Vakfolt, tükör, feedback – Önismeret & visszajelzés – Johari + SBI.md",
    "02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan – 3 kvuca, 3 világ.md":
        "02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan, Zorea – 4 kvuca, 4 világ.md",
    "02 Tervezet/Modulok/M4/Online leckék/M4.4 – 45 mp-es peulabemutató – vázlat egy konkrét kvucára.md":
        "02 Tervezet/Modulok/M4/Online leckék/M4.4 – 45 mp-es peula-pitch – vázlat egy konkrét kvucára.md",
    "02 Tervezet/Modulok/M4/Peulák/M4.B – Mit és hogyan kérdezek – Kérdezés & peulabemutató gyakorlása.md":
        "02 Tervezet/Modulok/M4/Peulák/M4.B – Mit és hogyan kérdezek – Kérdezés & pitch gyakorlása.md",
    "02 Tervezet/Modulok/M4/Peulák/M4.F – Felzárkóztató peula – Test, hang, kérdések & peulabemutató (Study Lab).md":
        "02 Tervezet/Modulok/M4/Peulák/M4.F – Felzárkóztató peula – Test, hang, kérdések & pitch (Study Lab).md",
    "02 Tervezet/Modulok/M5/Online leckék/M5.3 – Hogyan tanulunk tényleg – Gyakorlás, aktív felidézés, időben elosztott gyakorlás.md":
        "02 Tervezet/Modulok/M5/Online leckék/M5.3 – Hogyan tanulunk tényleg – Gyakorlás, visszahívás, spacing.md",
    "02 Tervezet/Modulok/M6/M6 – Eszköztár – játék, történet, kézműves & inkluzivitás.md":
        "02 Tervezet/Modulok/M6/M6 – Toolbox – játék, történet, kézműves & inkluzivitás.md",
    "02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 3 aktuális kvucára.md":
        "02 Tervezet/Modulok/M6/Online leckék/M6.1 – Játék-kategóriák 4 kvucára.md",
    "02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 3 aktuális kvucára (45’).md":
        "02 Tervezet/Modulok/M6/Peulák/M6.A – Peula – Játék-labor 4 kvucára (45’).md",
    "02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap-műhely – saját eszköz tervezése (45’).md":
        "02 Tervezet/Modulok/M6/Peulák/M6.B – Peula – Játéklap workshop – saját eszköz tervezése (45’).md",
    "02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Eszköztár & játéklap (Study Lab).md":
        "02 Tervezet/Modulok/M6/Peulák/M6.F – Felzárkóztató peula – Toolbox & játéklap (Study Lab).md",
    "02 Tervezet/Modulok/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 idővonal.md":
        "02 Tervezet/Modulok/Z/Online leckék/Z.1 – Visszanéző tükör – M0–M7 timeline.md",
    "02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzési visszajelzés.md":
        "02 Tervezet/Modulok/Z/Online leckék/Z.4 – Záró reflexió + képzés feedback.md",
}

# The 2026-10-02 owner decisions renamed files atomically: "lépéstérkép" and
# "Nemcsak", then the local Somer spelling (madrih, dugma isit, Leviatán). Same
# purpose as above: the pre-rename path that carried the baseline. M3.2 was
# renamed twice, so it maps straight to its baseline path.
DECISIONS_2026_10_02_RENAMES = {
    "02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépéstérkép.md":
        "02 Tervezet/Modulok/M3/Peulák/M3.B – Red flag vagy nem – Esetelemzés & lépés-térkép.md",
    "02 Tervezet/Modulok/M7/Online leckék/M7.2 – Nemcsak játék, hanem peula – 11 tervezési pont & AI-támogatás.md":
        "02 Tervezet/Modulok/M7/Online leckék/M7.2 – Nem csak játék, hanem peula – 11 tervezési pont & AI-támogatás.md",
    "02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrih, nem terapeuta – szerepek és elvárások.md":
        "02 Tervezet/Modulok/M0/Online leckék/M0.2 – Madrich, nem terapeuta – szerepek és elvárások.md",
    "02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma isit az online térben + bemutatkozó fórum.md":
        "02 Tervezet/Modulok/M0/Online leckék/M0.4 – Dugma ishit az online térben + bemutatkozó fórum.md",
    "02 Tervezet/Modulok/M2/M2 – Ki vagyok madrihként – Identitás, Somer-értékek és dugma isit.md":
        "02 Tervezet/Modulok/M2/M2 – Ki vagyok madrichként – Identitás, Somer-értékek és dugma ishit.md",
    "02 Tervezet/Modulok/M2/Online leckék/M2.1 – Ki vagyok én madrihként – identitás-körök.md":
        "02 Tervezet/Modulok/M2/Online leckék/M2.1 – Ki vagyok én madrichként – identitás-körök.md",
    "02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma isit nem terapeuta.md":
        "02 Tervezet/Modulok/M2/Online leckék/M2.4 – Reflektív napló & határok – A dugma ishit nem terapeuta.md",
    "02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md":
        "02 Tervezet/Modulok/M3/Online leckék/M3.2 – Parparim, Kivsza, Leviatan, Zorea – 4 kvuca, 4 világ.md",
    "02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrihként – határok, red flag-ek és modulproduktum.md":
        "02 Tervezet/Modulok/M3/Online leckék/M3.4 – Do és Don’t madrichként – határok, red flag-ek és modulproduktum.md",
    "02 Tervezet/Modulok/M5/Online leckék/M5.4 – Cél–kvuca–módszer mini-táblázat – saját adatbázisod madrihként.md":
        "02 Tervezet/Modulok/M5/Online leckék/M5.4 – Cél–kvuca–módszer mini-táblázat – saját adatbázisod madrichként.md",
}
BASELINE_RENAMES = {**FINAL_CLEANUP_2026_09_29_RENAMES, **DECISIONS_2026_10_02_RENAMES}

#: Approved learner- and trainer-visible text. Every authoring file whose visible
#: text (metadata blocks stripped) differs from the baseline above is pinned here
#: by sha256, with the reason it was approved. Re-pin only with a reason:
#:   python3 tools/test_media_manifest.py --pin-visible "<indoklás>"
VISIBLE_PINS = Path(__file__).resolve().parent / "approved-visible-text.json"


def visible_fingerprint(text: str) -> str:
    """sha256 of the learner/trainer-visible text (metadata blocks stripped)."""
    return hashlib.sha256(mig.strip_metadata(text).encode("utf-8")).hexdigest()


def baseline_text(rel: str) -> str | None:
    """The file's text at the baseline commit, or None when it did not exist."""
    baseline_rel = BASELINE_RENAMES.get(rel, rel)
    blob = subprocess.run(["git", "-C", str(mm.ROOT), "show",
                           f"{BASELINE_COMMIT}:{baseline_rel}"], capture_output=True)
    return blob.stdout.decode("utf-8") if blob.returncode == 0 else None


def visible_texts_needing_pins() -> dict[str, str]:
    """Fingerprints of every authoring file whose visible text left the baseline."""
    needing = {}
    for path in mm.discover_sources():
        rel = path.relative_to(mm.ROOT).as_posix()
        current = path.read_text(encoding="utf-8")
        baseline = baseline_text(rel)
        if baseline is not None and mig.strip_metadata(current) == baseline:
            continue
        needing[rel] = visible_fingerprint(current)
    return needing


def pin_mismatches(pins: dict, needing: dict[str, str]) -> dict[str, list[str]]:
    """Changed, unpinned and stale files — empty lists when everything matches."""
    return {
        "changed": sorted(rel for rel, digest in needing.items()
                          if rel in pins and pins[rel]["sha256"] != digest),
        "unpinned": sorted(set(needing) - set(pins)),
        "stale": sorted(set(pins) - set(needing)),
    }


def pin_visible_text(reason: str) -> int:
    """Re-pin changed or new files with ``reason``; drop pins no longer needed."""
    reason = reason.strip()
    if not reason:
        print('Indoklás kötelező: --pin-visible "<miért változott a látható szöveg>"')
        return 2
    check = subprocess.run(["git", "-C", str(mm.ROOT), "cat-file", "-e",
                            f"{BASELINE_COMMIT}^{{commit}}"], capture_output=True)
    if check.returncode != 0:
        print(f"A kiindulási commit ({BASELINE_COMMIT[:7]}) nem elérhető — teljes history kell.")
        return 2
    data = (json.loads(VISIBLE_PINS.read_text(encoding="utf-8"))
            if VISIBLE_PINS.exists() else {"schema": 1, "files": {}})
    pins = data["files"]
    needing = visible_texts_needing_pins()
    repinned = 0
    for rel, digest in needing.items():
        if pins.get(rel, {}).get("sha256") != digest:
            pins[rel] = {"sha256": digest, "reason": reason}
            repinned += 1
    for rel in set(pins) - set(needing):
        del pins[rel]
    VISIBLE_PINS.write_text(json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)
                            + "\n", encoding="utf-8")
    print(f"{repinned} fájl látható szövege újrapinnelve: {reason}")
    return 0


LESSON_DIR = "02 Tervezet/Modulok/M9/Online leckék"
LESSON = f"{LESSON_DIR}/M9.1 – Teszt lecke.md"


def declaration(**fields) -> str:
    return "<!-- @asset\n" + json.dumps(fields, ensure_ascii=False, indent=2) + "\n-->\n"


def source_block(source_id: str, kind: str, body: str) -> str:
    return (f'<!-- @source {{"id": "{source_id}", "kind": "{kind}"}} -->\n'
            f"{body}\n<!-- @endsource -->\n")


@contextmanager
def corpus(files: dict[str, str]):
    """A temporary curriculum tree, compiled with paths relative to it."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        for rel, text in files.items():
            path = root / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        with mm._rel_root(root):
            yield root


def compile_corpus(files: dict[str, str]) -> dict:
    with corpus(files) as root:
        return mm.compile_manifest(root / "02 Tervezet", strict=False)


def errors_of(files: dict[str, str]) -> list[str]:
    return [str(e) for e in compile_corpus(files)["errors"]]


def lesson(*parts: str) -> str:
    return "# M9.1 – Teszt lecke\n\n## 1. Slide\n\n" + "\n".join(parts)


MINIMAL = declaration(id="M9.1-ILL-01", kind="illustration", title="Teszt illusztráció",
                      a11y={"visual": "decorative"})


# ==========================================================================
# Parsing and the schema
# ==========================================================================

class TestSchema(unittest.TestCase):

    def test_valid_minimal_asset(self):
        model = compile_corpus({LESSON: lesson(MINIMAL)})
        self.assertEqual([], [str(e) for e in model["errors"]])
        self.assertEqual(1, len(model["assets"]))
        self.assertEqual("M9.1", model["assets"][0]["unit"])
        self.assertEqual("generate", model["assets"][0]["mode"])

    def test_talking_head_with_narration(self):
        files = {LESSON: lesson(
            declaration(id="M9.1-VID-01", kind="video", subtype="ai-talking-head",
                        title="Hook videó", source_ref="M9.1-VID-01-VO",
                        a11y={"audio": "spoken", "visual": "decorative",
                              "alt_note": "a feliratok lefedik"},
                        derivatives=["voiceover", "captions", "transcript"]),
            source_block("M9.1-VID-01-VO", "narration", "> „Szia!\n> Ez a narráció."))}
        model = compile_corpus(files)
        self.assertEqual([], [str(e) for e in model["errors"]])
        asset = model["assets"][0]
        self.assertTrue(asset["source_text"].startswith("„Szia!"))
        self.assertEqual(["M9.1-VID-01", "M9.1-VID-01::VOICEOVER",
                          "M9.1-VID-01::CAPTIONS", "M9.1-VID-01::TRANSCRIPT"],
                         asset["deliverable_ids"])

    def test_multiline_narration_keeps_paragraphs_and_punctuation(self):
        body = ("> „Első bekezdés – gondolatjellel.\n"
                "> Második sor.\n"
                ">\n"
                "> Új bekezdés, ‘belső idézettel’ és **kiemeléssel**.”")
        files = {LESSON: lesson(
            declaration(id="M9.1-NAR-01", kind="voiceover", title="Narráció",
                        source_ref="M9.1-NAR-01-VO", derivatives=["transcript"]),
            source_block("M9.1-NAR-01-VO", "narration", body))}
        text = compile_corpus(files)["sources"][0]["text"]
        self.assertNotIn(">", text)
        self.assertIn("„Első bekezdés – gondolatjellel.", text)
        self.assertIn("‘belső idézettel’", text)
        self.assertIn("**kiemeléssel**.”", text)
        paragraphs = [p for p in text.split("\n\n") if p.strip()]
        self.assertEqual(2, len(paragraphs), "a bekezdéshatárnak meg kell maradnia")

    def test_blockquote_marker_stripped_but_words_untouched(self):
        raw = "> „Szia!   \n>   Behúzott sor.\n> Vége.”"
        self.assertEqual("„Szia!\n  Behúzott sor.\nVége.”",
                         mm.normalise_source_text(raw))

    def test_duplicate_asset_id_rejected(self):
        files = {LESSON: lesson(MINIMAL, MINIMAL)}
        self.assertTrue(any("duplikált asset-ID" in e for e in errors_of(files)))

    def test_duplicate_source_id_rejected(self):
        files = {LESSON: lesson(
            declaration(id="M9.1-NAR-01", kind="voiceover", title="N",
                        source_ref="M9.1-S", derivatives=["transcript"]),
            source_block("M9.1-S", "narration", "> „A"),
            source_block("M9.1-S", "narration", "> „B"))}
        self.assertTrue(any("duplikált forrás-ID" in e for e in errors_of(files)))

    def test_dangling_source_ref_rejected(self):
        files = {LESSON: lesson(
            declaration(id="M9.1-NAR-01", kind="voiceover", title="N",
                        source_ref="M9.1-NINCS", derivatives=["transcript"]))}
        self.assertTrue(any("nem létező forrásra mutat" in e for e in errors_of(files)))

    def test_unreferenced_source_rejected(self):
        files = {LESSON: lesson(MINIMAL, source_block("M9.1-S", "narration", "> „Árva"))}
        self.assertTrue(any("egyetlen asset sem hivatkozik" in e for e in errors_of(files)))

    def test_malformed_declaration_rejected(self):
        files = {LESSON: lesson("<!-- @asset\n{id: 'M9.1-X'}\n-->\n")}
        self.assertTrue(any("JSON-je hibás" in e for e in errors_of(files)))

    def test_unclosed_source_block_rejected(self):
        files = {LESSON: lesson(
            declaration(id="M9.1-NAR-01", kind="voiceover", title="N",
                        source_ref="M9.1-S", derivatives=["transcript"]),
            '<!-- @source {"id": "M9.1-S", "kind": "narration"} -->\n> „Nyitva maradt\n')}
        self.assertTrue(any("lezáratlan @source" in e for e in errors_of(files)))

    def test_unknown_field_rejected(self):
        files = {LESSON: lesson(declaration(id="M9.1-ILL-01", kind="illustration",
                                            title="T", szinesz="nincs ilyen mező"))}
        self.assertTrue(any("ismeretlen @asset mező" in e for e in errors_of(files)))

    def test_unknown_enum_rejected(self):
        files = {LESSON: lesson(declaration(id="M9.1-ILL-01", kind="hologram", title="T"))}
        self.assertTrue(any("ismeretlen `kind`" in e for e in errors_of(files)))

    def test_id_must_match_the_file_unit(self):
        files = {LESSON: lesson(declaration(id="M9.2-ILL-01", kind="illustration",
                                            title="T", a11y={"visual": "decorative"}))}
        self.assertTrue(any("nem a fájl egységéhez tartozik" in e for e in errors_of(files)))

    def test_hub_and_lesson_ids_no_longer_collide(self):
        hub = "02 Tervezet/Modulok/M9/M9 – Modul áttekintő.md"
        files = {
            LESSON: lesson(MINIMAL),
            hub: ("# M9 – Modul áttekintő\n\n## §3\n\n"
                  + declaration(id="M9-HUB-ILL-01", kind="illustration",
                                title="Hub illusztráció", mode="reuse",
                                reuse_of="M9.1-ILL-01")),
        }
        model = compile_corpus(files)
        self.assertEqual([], [str(e) for e in model["errors"]])
        units = {a["id"]: a["unit"] for a in model["assets"]}
        self.assertEqual({"M9.1-ILL-01": "M9.1", "M9-HUB-ILL-01": "M9-HUB"}, units)


# ==========================================================================
# Reuse
# ==========================================================================

class TestReuse(unittest.TestCase):

    def _two(self, second: dict) -> dict:
        return {LESSON: lesson(MINIMAL, declaration(**second))}

    def test_valid_reuse(self):
        model = compile_corpus(self._two(dict(
            id="M9.1-ILL-02", kind="illustration", title="Újrahasznált",
            mode="reuse", reuse_of="M9.1-ILL-01")))
        self.assertEqual([], [str(e) for e in model["errors"]])
        reused = [a for a in model["assets"] if a["mode"] == "reuse"][0]
        self.assertEqual("M9.1-ILL-01", reused["reuse_resolves_to"])
        self.assertEqual([], reused["deliverable_ids"],
                         "az újrahasznosítás nem gyárt új deliverable-t")

    def test_self_reuse_rejected(self):
        files = {LESSON: lesson(declaration(
            id="M9.1-ILL-01", kind="illustration", title="Ön-hivatkozó",
            mode="reuse", reuse_of="M9.1-ILL-01"))}
        self.assertTrue(any("önmagát hasznosítja újra" in e for e in errors_of(files)))

    def test_dangling_reuse_rejected(self):
        files = {LESSON: lesson(declaration(
            id="M9.1-ILL-02", kind="illustration", title="Lógó",
            mode="reuse", reuse_of="M9.1-NINCS"))}
        self.assertTrue(any("nem létező assetre mutat" in e for e in errors_of(files)))

    def test_reuse_cycle_rejected(self):
        files = {LESSON: lesson(
            declaration(id="M9.1-ILL-01", kind="illustration", title="A",
                        mode="reuse", reuse_of="M9.1-ILL-02"),
            declaration(id="M9.1-ILL-02", kind="illustration", title="B",
                        mode="reuse", reuse_of="M9.1-ILL-01"))}
        self.assertTrue(any("körkörös újrahasznosítás" in e for e in errors_of(files)))

    def test_incompatible_kind_reuse_rejected(self):
        files = {LESSON: lesson(MINIMAL, declaration(
            id="M9.1-NAR-01", kind="voiceover", title="Hang",
            mode="reuse", reuse_of="M9.1-ILL-01"))}
        self.assertTrue(any("nem hasznosíthatja újra" in e for e in errors_of(files)))

    def test_reuse_may_not_declare_derivatives(self):
        files = {LESSON: lesson(MINIMAL, declaration(
            id="M9.1-ILL-02", kind="illustration", title="B", mode="reuse",
            reuse_of="M9.1-ILL-01", derivatives=["alt-text"]))}
        self.assertTrue(any("mégis vannak derivatívái" in e for e in errors_of(files)))


# ==========================================================================
# Accessibility structure
# ==========================================================================

class TestAccessibility(unittest.TestCase):

    def test_decorative_visual_accepted(self):
        model = compile_corpus({LESSON: lesson(MINIMAL)})
        self.assertEqual([], [str(e) for e in model["errors"]])

    def test_visual_without_a11y_declaration_rejected(self):
        files = {LESSON: lesson(declaration(id="M9.1-ILL-01", kind="illustration",
                                            title="T"))}
        self.assertTrue(any("nincs a11y.visual megjelölve" in e for e in errors_of(files)))

    def test_informative_visual_without_alt_rejected(self):
        files = {LESSON: lesson(declaration(
            id="M9.1-DIA-01", kind="diagram", title="Ábra",
            a11y={"visual": "informative"}))}
        problems = errors_of(files)
        self.assertTrue(any("nincs alt-text derivatívája" in e for e in problems))
        self.assertTrue(any("nincs alt-szöveg forrás" in e for e in problems))

    def test_spoken_video_without_captions_rejected(self):
        files = {LESSON: lesson(declaration(
            id="M9.1-VID-01", kind="video", subtype="explainer", title="V",
            spec="rövid magyarázó videó",
            a11y={"audio": "spoken", "visual": "decorative", "alt_note": "x"},
            derivatives=["transcript"]))}
        self.assertTrue(any("felirat-derivatíva nélkül" in e for e in errors_of(files)))

    def test_audio_without_transcript_rejected(self):
        files = {LESSON: lesson(declaration(
            id="M9.1-NAR-01", kind="voiceover", title="N", spec="felmondás",
            derivatives=["captions"]))}
        self.assertTrue(any("szöveges ekvivalens nélkül" in e for e in errors_of(files)))

    def test_silent_video_needs_no_captions(self):
        files = {LESSON: lesson(declaration(
            id="M9.1-VID-01", kind="video", subtype="screen-recording", title="V",
            spec="néma képernyőfelvétel",
            a11y={"audio": "silent", "visual": "decorative", "alt_note": "dekoratív"}))}
        self.assertEqual([], errors_of(files))

    def test_alt_source_selects_the_quoted_span(self):
        prescription = ("> **Alt-szöveg (kötelező):** „Két oszlop egymás mellett.” "
                        "Az ikonok dekoratívak.")
        files = {LESSON: lesson(
            declaration(id="M9.1-DIA-01", kind="diagram", title="Ábra",
                        a11y={"visual": "informative",
                              "alt_source_ref": "M9.1-DIA-01-ALT#1"},
                        derivatives=["alt-text"]),
            source_block("M9.1-DIA-01-ALT", "alt-text", prescription))}
        model = compile_corpus(files)
        self.assertEqual([], [str(e) for e in model["errors"]])
        self.assertEqual("Két oszlop egymás mellett.", model["assets"][0]["alt_text"])

    def test_out_of_range_quote_selector_rejected(self):
        files = {LESSON: lesson(
            declaration(id="M9.1-DIA-01", kind="diagram", title="Ábra",
                        a11y={"visual": "informative",
                              "alt_source_ref": "M9.1-DIA-01-ALT#3"},
                        derivatives=["alt-text"]),
            source_block("M9.1-DIA-01-ALT", "alt-text", "> **Alt:** „Egy idézet.”"))}
        with self.assertRaises(mm.ManifestError):
            compile_corpus(files)


# ==========================================================================
# Modes, decisions, discovery
# ==========================================================================

class TestModesAndDiscovery(unittest.TestCase):

    def test_external_asset_needs_a_reference(self):
        files = {LESSON: lesson(declaration(
            id="M9.1-FOTO-01", kind="photo", title="Stock kép", mode="external",
            a11y={"visual": "informative", "alt_note": "megírandó"},
            derivatives=["alt-text"]))}
        self.assertTrue(any("nincs forrás-hivatkozása" in e for e in errors_of(files)))

    def test_human_decision_must_say_what_to_decide(self):
        files = {LESSON: lesson(declaration(
            id="M9.1-POSZ-01", kind="poster", title="P", mode="human-decision"))}
        self.assertTrue(any("nincs leírva, mit kell eldönteni" in e for e in errors_of(files)))

    def test_human_decision_status_is_derived_not_hidden(self):
        files = {LESSON: lesson(declaration(
            id="M9.1-POSZ-01", kind="poster", title="P", mode="human-decision",
            decision="Kell-e egyáltalán? — a képzés szakmai felelőse"))}
        model = compile_corpus(files)
        self.assertEqual("pending-human-decision", model["assets"][0]["status"])

    def test_new_lesson_file_is_discovered_without_code_change(self):
        base = {LESSON: lesson(MINIMAL)}
        self.assertEqual(1, compile_corpus(base)["counts"]["files_discovered"]
                         if "counts" in compile_corpus(base) else
                         mm.compute_stats(compile_corpus(base))["files_discovered"])
        extended = dict(base)
        extended["02 Tervezet/Modulok/M9/Online leckék/M9.2 – Vadonatúj lecke.md"] = (
            "# M9.2 – Vadonatúj lecke\n\n## 1. Slide\n\n"
            + declaration(id="M9.2-ILL-01", kind="illustration", title="Új",
                          a11y={"visual": "decorative"}))
        model = compile_corpus(extended)
        stats = mm.compute_stats(model)
        self.assertEqual(2, stats["files_discovered"])
        self.assertIn("M9.2-ILL-01", {a["id"] for a in model["assets"]})

    def test_generated_directory_is_excluded_from_discovery(self):
        files = {LESSON: lesson(MINIMAL),
                 "02 Tervezet/Média-assetek/Média-asset regiszter.md":
                     "# generált\n\n" + declaration(id="X-ILL-01", kind="illustration",
                                                    title="Nem szabad beolvasni")}
        model = compile_corpus(files)
        self.assertEqual([LESSON], [f["file"] for f in model["files"]])

    def test_asset_free_declaration_requires_a_reason(self):
        files = {LESSON: "# M9.1\n\n<!-- @asset-free\n{}\n-->\n"}
        self.assertTrue(any("kötelező a `reason`" in e for e in errors_of(files)))

    def test_asset_free_file_may_not_also_declare_assets(self):
        files = {LESSON: ('# M9.1\n\n<!-- @asset-free\n{"reason": "nincs média"}\n-->\n\n'
                          + MINIMAL)}
        self.assertTrue(any("mégis van benne @asset" in e for e in errors_of(files)))


# ==========================================================================
# Hashes, ordering, determinism
# ==========================================================================

class TestHashesAndDeterminism(unittest.TestCase):

    def _two_assets(self, first_text: str, second_text: str) -> dict:
        return {LESSON: lesson(
            declaration(id="M9.1-NAR-01", kind="voiceover", title="A",
                        source_ref="M9.1-A", derivatives=["transcript"]),
            source_block("M9.1-A", "narration", first_text),
            declaration(id="M9.1-NAR-02", kind="voiceover", title="B",
                        source_ref="M9.1-B", derivatives=["transcript"]),
            source_block("M9.1-B", "narration", second_text))}

    def test_source_hash_is_stable(self):
        files = self._two_assets("> „Első.", "> „Második.")
        first = {a["id"]: a["source_hash"] for a in compile_corpus(files)["assets"]}
        second = {a["id"]: a["source_hash"] for a in compile_corpus(files)["assets"]}
        self.assertEqual(first, second)

    def test_copy_change_changes_that_hash(self):
        before = compile_corpus(self._two_assets("> „Első.", "> „Második."))
        after = compile_corpus(self._two_assets("> „Első, átírva.", "> „Második."))
        by_id_before = {a["id"]: a for a in before["assets"]}
        by_id_after = {a["id"]: a for a in after["assets"]}
        self.assertNotEqual(by_id_before["M9.1-NAR-01"]["source_hash"],
                            by_id_after["M9.1-NAR-01"]["source_hash"])
        self.assertNotEqual(by_id_before["M9.1-NAR-01"]["copy_hash"],
                            by_id_after["M9.1-NAR-01"]["copy_hash"])

    def test_unrelated_copy_change_leaves_other_hashes_alone(self):
        before = compile_corpus(self._two_assets("> „Első.", "> „Második."))
        after = compile_corpus(self._two_assets("> „Első.", "> „Második, átírva."))
        by_id_before = {a["id"]: a for a in before["assets"]}
        by_id_after = {a["id"]: a for a in after["assets"]}
        self.assertEqual(by_id_before["M9.1-NAR-01"]["source_hash"],
                         by_id_after["M9.1-NAR-01"]["source_hash"])
        self.assertEqual(by_id_before["M9.1-NAR-01"]["spec_hash"],
                         by_id_after["M9.1-NAR-01"]["spec_hash"])

    def test_spec_hash_reacts_to_spec_only(self):
        base = {LESSON: lesson(MINIMAL)}
        changed = {LESSON: lesson(declaration(
            id="M9.1-ILL-01", kind="illustration", title="Teszt illusztráció",
            spec="Új gyártási leírás.", a11y={"visual": "decorative"}))}
        self.assertNotEqual(compile_corpus(base)["assets"][0]["spec_hash"],
                            compile_corpus(changed)["assets"][0]["spec_hash"])

    def test_xlsx_zip_normalisation_canonicalises_equivalent_xml(self):
        def make_zip(xml: bytes) -> bytes:
            buf = io.BytesIO()
            with mm.zipfile.ZipFile(buf, "w", mm.zipfile.ZIP_DEFLATED) as zf:
                zf.writestr("xl/test.xml", xml)
            return buf.getvalue()

        first = make_zip(b'<root xmlns="urn:test"><item b="2" a="1"></item></root>')
        second = make_zip(b'<root xmlns="urn:test"><item a="1" b="2"/></root>')
        self.assertNotEqual(first, second)
        self.assertEqual(mm._normalise_zip(first), mm._normalise_zip(second))

    def test_ordering_is_deterministic_and_module_first(self):
        files = {
            "02 Tervezet/Modulok/M9/Online leckék/M9.2 – B.md":
                "# B\n\n## S\n\n" + declaration(id="M9.2-ILL-01", kind="illustration",
                                                title="B", a11y={"visual": "decorative"}),
            "02 Tervezet/Modulok/M0/Online leckék/M0.1 – A.md":
                "# A\n\n## S\n\n" + declaration(id="M0.1-ILL-01", kind="illustration",
                                                title="A", a11y={"visual": "decorative"}),
            LESSON: lesson(MINIMAL),
        }
        ids = [a["id"] for a in compile_corpus(files)["assets"]]
        self.assertEqual(["M0.1-ILL-01", "M9.1-ILL-01", "M9.2-ILL-01"], ids)


# ==========================================================================
# The real corpus
# ==========================================================================

class TestRepositoryCorpus(unittest.TestCase):
    """Tests against this repository's current curriculum."""

    @classmethod
    def setUpClass(cls):
        cls.model = mm.compile_manifest()
        cls.stats = mm.compute_stats(cls.model)

    def test_manifest_validates(self):
        errors = mm.compile_manifest(strict=False)["errors"]
        self.assertEqual([], [str(e) for e in errors])

    def test_generated_outputs_are_current(self):
        outputs = mm.build_outputs(self.model)
        self.assertEqual([], mm.compare_outputs(outputs),
                         "a generált regiszter elcsúszott — futtasd: "
                         "python3 tools/media_manifest.py build")

    def test_rendered_xlsx_roundtrips_through_openpyxl(self):
        from openpyxl import load_workbook

        wb = load_workbook(io.BytesIO(mm.render_xlsx(self.model)), read_only=True)
        try:
            self.assertIn("Összesítő", wb.sheetnames)
            self.assertIn("Assetek", wb.sheetnames)
            self.assertIn("Deliverable-ek", wb.sheetnames)
        finally:
            wb.close()

    def test_build_is_deterministic(self):
        first = mm.build_outputs(mm.compile_manifest())
        second = mm.build_outputs(mm.compile_manifest())
        self.assertEqual({p: mm.sha256_text(str(len(v))) for p, v in first.items()},
                         {p: mm.sha256_text(str(len(v))) for p, v in second.items()})
        for path, data in first.items():
            self.assertEqual(data, second[path], f"{path.name} nem determinisztikus")

    def test_views_agree_on_counts(self):
        assets_rows = mm.asset_csv_rows(self.model)
        deliverable_rows = mm.deliverable_csv_rows(self.model)
        register = mm.render_register_md(self.model)
        self.assertEqual(len(assets_rows), self.stats["assets"])
        self.assertEqual(len(deliverable_rows), self.stats["deliverables"])
        self.assertIn(f"| Szemantikus asset | **{self.stats['assets']}** |", register)
        self.assertIn(f"| Produkciós deliverable | **{self.stats['deliverables']}** |",
                      register)
        payload = json.loads(mm.render_manifest_json(self.model))
        self.assertEqual(payload["counts"]["assets"], self.stats["assets"])
        self.assertEqual(len(payload["assets"]), self.stats["assets"])
        self.assertEqual(len(payload["deliverables"]), self.stats["deliverables"])

    def test_reuse_targets_resolve_to_a_produced_asset(self):
        by_id = {a["id"]: a for a in self.model["assets"]}
        for asset in self.model["assets"]:
            if asset["mode"] != "reuse":
                continue
            target = by_id.get(asset["reuse_resolves_to"])
            self.assertIsNotNone(target, f"{asset['id']} nem oldódik fel")
            self.assertNotEqual("reuse", target["mode"])

    def test_no_reuse_rests_on_the_v1_identifier_collision(self):
        """The v1 register's hub↔lesson ID clash must not survive as fake reuse.

        Several v1 dedup tags meant "the module overview's row equals this one",
        but the merge had already dropped the overview's row, so the tag landed on
        the detailed file's own, unrelated asset. Signature: both sides live in
        the same non-hub file while the justification explains the match by
        pointing at the overview.
        """
        by_id = {a["id"]: a for a in self.model["assets"]}
        for asset in self.model["assets"]:
            if asset["mode"] != "reuse":
                continue
            target = by_id[asset["reuse_of"]]
            if asset["file"] != target["file"] or asset["file_kind"] == "hub":
                continue
            self.assertNotRegex(
                asset["notes"], r"áttekintő|\bhub\b",
                f"{asset['id']} ugyanabban a fájlban lévő assetre hivatkozik, "
                "és az indoklás a modul-áttekintőre mutat — ez a v1 ID-ütközés")

    def test_deliverable_ids_are_unique_and_never_collide_with_asset_ids(self):
        asset_ids = {a["id"] for a in self.model["assets"]}
        deliverable_ids = [d["id"] for d in self.model["deliverables"]]
        self.assertEqual(len(deliverable_ids), len(set(deliverable_ids)))
        derived = {d for d in deliverable_ids if "::" in d}
        self.assertFalse(derived & asset_ids)

    def test_m51_narration_follows_the_current_lesson_not_the_frozen_snapshot(self):
        """The headline drift case the v1 register documented and could not fix."""
        asset = next(a for a in self.model["assets"] if a["id"] == "M5.1-VID-01")
        legacy = {r["assetId"]: r for r in mm.load_legacy()["assets"]}
        frozen = legacy["M5.1-NAR-01"]["verbatim"]
        self.assertIn("teljesen random pillanatok", frozen)
        self.assertIn("teljesen **más pillanatok**", asset["source_text"])
        self.assertNotIn("teljesen random pillanatok", asset["source_text"])
        self.assertIn("Néha a tanár feleltet", asset["source_text"])

    def test_m51_alt_follows_the_current_lesson_not_the_frozen_snapshot(self):
        asset = next(a for a in self.model["assets"] if a["id"] == "M5.1-DIA-01")
        legacy = {r["assetId"]: r for r in mm.load_legacy()["assets"]}
        frozen = legacy["M5.1-ALT-02"]["verbatim"]
        self.assertIn("szervezett, önkéntes, nevelési cél", frozen)
        self.assertIn("szervezett, van nevelési cél", asset["alt_text"])
        self.assertIn("sokszor észre sem veszed", asset["alt_text"])

    def test_no_generated_field_names_a_free_text_runtime(self):
        """The lessons leave the free-text element to runtime acceptance §6.

        `Short Answer` does not exist in H5P at all; `Essay` exists but the current
        lessons refuse to assume it inside a Course Presentation slide. Both
        survive only in the frozen snapshot.
        """
        legacy = mm.load_legacy()["assets"]
        self.assertTrue([r["assetId"] for r in legacy
                         if "Short Answer" in (r["lineRef"] or "") + (r["verbatim"] or "")],
                        "a v1 pillanatkép tartalmazta a nem létező típust")
        self.assertGreaterEqual(
            len([r for r in legacy if "Essay" in json.dumps(r, ensure_ascii=False)]), 10,
            "a v1 pillanatkép sok soron megnevezte a szabad szöveges runtime-ot")
        payload = mm.render_manifest_json(self.model)
        for retired in ("Short Answer", "Short answer", "short answer", "Essay"):
            self.assertNotIn(retired, payload,
                             f"a v2 manifeszt megnevezi a visszavont futtatókörnyezetet: {retired}")

    def test_lessons_still_state_the_free_text_runtime_rule(self):
        """Removing the type name must not remove the rule that replaced it."""
        lesson = (mm.ACTIVE_ROOT / "Modulok/M1/Online leckék"
                  / "M1.1 – Johari-ablak – vakfoltjaim felismerése.md")
        text = lesson.read_text(encoding="utf-8")
        self.assertIn("H5P runtime acceptance.md", text)
        self.assertIn("nem feltételezhető", text)

    def test_m41_caption_rule_follows_the_current_lesson(self):
        """M4.1 separates audio-only from spoken video; captions are not optional.

        A spoken video either carries its own caption and transcript, or it is a
        scene inside a composed Interactive Video whose container carries them —
        an H5P Interactive Video has one base video and one `textTracks` list, so
        a scene has nowhere of its own to attach them. The obligation may move up
        to the container; it may never disappear.
        """
        by_id = {a["id"]: a for a in self.model["assets"]}
        container_of = {cid: a["id"] for a in self.model["assets"]
                        for cid in a["composed_of"]}
        videos = [a for a in self.model["assets"]
                  if a["unit"] == "M4.1" and a["kind"] == "video"
                  and a["a11y"].get("audio") == "spoken"]
        self.assertTrue(videos)
        for asset in videos:
            owner = by_id[container_of.get(asset["id"], asset["id"])]
            self.assertIn("captions", owner["derivatives"],
                          f"{asset['id']} → {owner['id']}")
            self.assertIn("transcript", owner["derivatives"],
                          f"{asset['id']} → {owner['id']}")
            if owner["id"] != asset["id"]:
                self.assertNotIn("captions", asset["derivatives"],
                                 f"{asset['id']} duplikálja a konténer felirat-sávját")
                self.assertNotIn("transcript", asset["derivatives"], asset["id"])
        source = (mm.ACTIVE_ROOT / "Modulok/M4/Online leckék"
                  / "M4.1 – Mit üzen a testem – Nonverbális kiállás.md")
        self.assertNotIn("felirat VAGY", source.read_text(encoding="utf-8"))

    def test_every_historical_row_has_a_disposition(self):
        recon = mm.reconcile(self.model)
        self.assertEqual(747, recon["legacy_total"])
        self.assertEqual(recon["legacy_total"], recon["mapped_total"])
        self.assertEqual(0, recon["unmapped"])
        self.assertEqual([], recon["conflicts"])

    def test_four_known_ambiguous_rows_are_handled_explicitly(self):
        recon = mm.reconcile(self.model)
        by_old = {row[0]: row for row in recon["rows"]}
        for old_id in ("M3.F-MUNK-01", "M3.F-MUNK-02", "Z.A-POSZ-01", "Z.A-POSZ-02"):
            self.assertIn(old_id, by_old)
            status, reason = by_old[old_id][7], by_old[old_id][8]
            self.assertIn(status, mm.RECON_STATUSES)
            self.assertNotEqual("CURRENTLY_UNMAPPED_ERROR", status)
            self.assertTrue(reason.strip(), f"{old_id} indoklás nélkül")

    def test_discovery_lint_is_clean(self):
        high = [f for f in mm.lint(self.model) if f["confidence"] == "HIGH"]
        self.assertEqual([], high, "feloldatlan HIGH jelzés a felderítő lintben")

    def test_open_production_gates_stay_machine_detectable(self):
        """A regenerated register may not quietly drop a release blocker.

        The canonical production rules carry the open values; the generated register
        must still surface those gates for production operators. A renderer change
        may not make an unresolved rule disappear from the human-facing register.
        """
        open_rules = [r for r in mm.production_rules() if "KITÖLTENDŐ" in r["text"]]
        self.assertTrue(open_rules, "R2/R3/R5 még nyitott — kell lennie jelölőnek")
        register = mm.OUT_REGISTER_MD.read_text(encoding="utf-8")
        self.assertIn("KITÖLTENDŐ", register)
        for rule in open_rules:
            self.assertIn(rule["id"], register, f"{rule['id']} kapu nem látszik a regiszterben")

    def test_production_rules_are_not_read_from_the_retired_snapshot(self):
        self.assertTrue(mm.PRODUCTION_RULES_FILE.exists())
        self.assertNotIn("_legacy", mm.PRODUCTION_RULES_FILE.as_posix().rsplit("/", 1)[0])
        self.assertEqual(8, len(mm.production_rules()))

    def test_r5_uses_the_current_three_group_canon(self):
        rules = {r["id"]: r for r in mm.production_rules()}
        self.assertNotIn("4-kvuca", rules["R5"]["text"])
        self.assertIn("három aktuális kvuca", rules["R5"]["text"])

    def test_every_open_decision_surfaces_in_the_register(self):
        register = mm.OUT_REGISTER_MD.read_text(encoding="utf-8")
        decided = [a for a in self.model["assets"]
                   if a["mode"] == "human-decision" or a["decision"]]
        self.assertTrue(decided)
        for asset in decided:
            self.assertIn(asset["id"], register,
                          f"{asset['id']} nyitott döntése nem látszik a regiszterben")

    def test_no_alt_reference_depends_on_quote_position(self):
        sources = {s["id"]: s for s in self.model["sources"]}
        checked = 0
        for asset in self.model["assets"]:
            ref = asset["a11y"].get("alt_source_ref", "")
            if not ref:
                continue
            checked += 1
            source_id, index = mm.split_ref(ref)
            quotes = mm.QUOTED_SPAN.findall(sources[source_id]["text"])
            self.assertEqual(1, len(quotes),
                             f"{asset['id']} alt-forrása több idézetet tartalmaz")
            self.assertEqual(1, index, f"{asset['id']} pozíciós szelektort használ")
        self.assertGreater(checked, 5)

    def test_no_spoken_asset_can_become_ready_without_its_script(self):
        for asset in self.model["assets"]:
            if mm.requires_spoken_source(asset) and not mm.has_spoken_source(asset):
                self.assertEqual("blocked", asset["status"], asset["id"])
                self.assertIn(mm.MISSING_SPOKEN_SOURCE, asset["readiness_issues"])
        for deliverable in self.model["deliverables"]:
            if mm.MISSING_SPOKEN_SOURCE in deliverable["readiness_issues"]:
                self.assertEqual("blocked", deliverable["status"], deliverable["id"])

    def test_m51_hidden_spec_no_longer_contradicts_the_live_narration(self):
        """F-04: the drift had moved from `verbatim` into the hidden spec."""
        by_id = {a["id"]: a for a in self.model["assets"]}
        video = by_id["M5.1-VID-01"]
        self.assertNotIn("random pillanat", video["spec"])
        self.assertIn("teljesen **más pillanatok**", video["source_text"])
        narration = by_id["M5.1-NAR-02"]
        self.assertNotRegex(narration["spec"],
                            r"nonformális\s*(és|ÉS)\s*(az\s*)?informális[^.]{0,90}önkéntes")
        self.assertIn("tudatos nevelési cél", narration["spec"])

    def test_no_spec_field_carries_a_documented_stale_claim(self):
        """`review` may quote the retired wording; a spec may not assert it."""
        stale = ("random pillanat", "Short Answer", "Essay", "felirat VAGY")
        for asset in self.model["assets"]:
            texts = [asset[f] for f in ("title", "purpose", "spec", "notes")]
            texts += [v for v in asset["technical"].values() if isinstance(v, str)]
            texts += [v for v in asset["a11y"].values() if isinstance(v, str)]
            for text in texts:
                for phrase in stale:
                    self.assertNotIn(phrase, text or "",
                                     f"{asset['id']} spec-mezője elavult állítást tartalmaz")

    def test_markers_never_break_a_list_or_a_quote_box(self):
        """Narrowing the alt blocks put markers inside lists and blockquotes.

        Three ways that goes wrong and the reader sees it: an unprefixed marker
        between two list items ends the list, one between two quoted lines splits
        the quote box, and an indented marker after a blank line turns a tight
        list loose.
        """
        opener = re.compile(r"^(?P<prefix>[ \t>]*)<!--\s*@(asset|source|asset-free|endsource)\b")
        item = re.compile(r"^\s*([-*+]|\d+[.)])\s")
        problems = []
        for path in mm.discover_sources():
            lines = path.read_text(encoding="utf-8").split("\n")
            fence = False
            for i, line in enumerate(lines):
                if line.lstrip().startswith("```"):
                    fence = not fence
                    continue
                match = opener.match(line)
                if not match:
                    continue
                prefix = match.group("prefix")
                previous = lines[i - 1] if i else ""
                following = lines[i + 1] if i + 1 < len(lines) else ""
                quoted = prefix.lstrip().startswith(">")
                indented = bool(prefix) and not prefix.strip()
                where = f"{path.name}:{i + 1}"
                if fence:
                    problems.append(f"{where} kódblokkban")
                if previous.lstrip().startswith("|") or following.lstrip().startswith("|"):
                    problems.append(f"{where} táblázatban")
                if (previous.lstrip().startswith(">") and following.lstrip().startswith(">")
                        and not quoted):
                    problems.append(f"{where} idézetblokkot vág ketté")
                if (item.match(previous) and item.match(following)
                        and not indented and not quoted):
                    problems.append(f"{where} listát vág ketté")
                if indented and not previous.strip():
                    problems.append(f"{where} üres sor után behúzva (laza listát okoz)")
                block_start = re.compile(
                    r"^\s*(?:>\s?)*(?:[-*+]\s|\d+[.)]\s|#{1,6}\s|\*\*\*|---)")
                between_paragraph_lines = (
                    previous.strip() and following.strip()
                    and not block_start.match(previous) and not block_start.match(following))
                if between_paragraph_lines and (indented or quoted):
                    problems.append(f"{where} bekezdést vág ketté")
        self.assertEqual([], problems)

    def test_hidden_metadata_renders_to_the_same_html(self):
        """The strongest available proof that the reader sees nothing new.

        Every migrated file is rendered twice with pandoc's GFM reader — GitHub's
        dialect — once as committed and once with the metadata stripped. Comments
        and whitespace aside, the DOM has to be identical: no split list, no split
        quote box, no loose list, no split paragraph. Skipped where pandoc is
        absent; `test_markers_never_break_a_list_or_a_quote_box` is the
        dependency-free guard that always runs.
        """
        if shutil.which("pandoc") is None:
            self.skipTest("pandoc nincs telepítve")
        comment = re.compile(r"<!--.*?-->", re.S)
        whitespace = re.compile(r"\s+")
        around_tag = re.compile(r"\s*(<[^>]+>)\s*")

        def render(markdown: str) -> str:
            result = subprocess.run(["pandoc", "-f", "gfm", "-t", "html"],
                                    input=markdown.encode("utf-8"), capture_output=True)
            html = result.stdout.decode("utf-8")
            return around_tag.sub(r"\1", whitespace.sub(" ", comment.sub("", html))).strip()

        differing = []
        for path in mm.discover_sources():
            current = path.read_text(encoding="utf-8")
            stripped = mig.strip_metadata(current)
            if current == stripped:
                continue
            if render(stripped) != render(current):
                differing.append(path.name)
        self.assertEqual([], differing)

    def test_slide_text_narrations_are_source_backed(self):
        """Where the lesson says the narration is the slide text, it must be linked."""
        by_id = {a["id"]: a for a in self.model["assets"]}
        for asset_id in ("M5.3-NAR-01", "M7.1-NAR-02"):
            asset = by_id[asset_id]
            self.assertTrue(asset["source_ref"], f"{asset_id} forrás nélkül maradt")
            self.assertTrue(asset["source_text"].strip())
            self.assertEqual([], asset["readiness_issues"], asset_id)

    def test_asset_free_files_state_a_reason(self):
        for file_rec in self.model["files"]:
            if file_rec["assets"] or not file_rec["file"].startswith("02 Tervezet/Modulok"):
                continue
            self.assertTrue(file_rec["asset_free_reason"],
                            f"{file_rec['file']}: nincs @asset-free indoklás")


# ==========================================================================
# Structural readiness (F-01, F-02)
# ==========================================================================

class TestStructuralReadiness(unittest.TestCase):
    """A missing script or an open decision outranks every production rule."""

    def _asset(self, **fields):
        base = dict(id="M9.1-VID-01", kind="video", subtype="explainer",
                    title="Teszt videó", spec="rövid magyarázó videó",
                    a11y={"audio": "spoken", "visual": "decorative",
                          "alt_note": "a felirat lefedi"},
                    derivatives=["captions", "transcript"])
        base.update(fields)
        return compile_corpus({LESSON: lesson(declaration(**base))})

    def test_spoken_video_without_source_is_inventory_valid_but_blocked(self):
        model = self._asset()
        self.assertEqual([], [str(e) for e in model["errors"]],
                         "a hiányzó szkript nem érvényteleníti a manifesztet")
        asset = model["assets"][0]
        self.assertEqual("blocked", asset["status"])
        self.assertIn(mm.MISSING_SPOKEN_SOURCE, asset["readiness_issues"])

    def test_the_caption_and_transcript_deliverables_are_blocked_too(self):
        model = self._asset()
        derived = [d for d in model["deliverables"] if d["role"] in ("captions", "transcript")]
        self.assertEqual(2, len(derived))
        for deliverable in derived:
            self.assertEqual("blocked", deliverable["status"], deliverable["id"])
            self.assertIn(mm.MISSING_SPOKEN_SOURCE, deliverable["readiness_issues"])

    def test_generated_voiceover_without_source_is_blocked(self):
        model = compile_corpus({LESSON: lesson(declaration(
            id="M9.1-NAR-01", kind="voiceover", title="Narráció",
            spec="felmondandó szöveg megírandó", derivatives=["transcript"]))})
        self.assertEqual("blocked", model["assets"][0]["status"])

    def test_a_valid_source_ref_lifts_the_structural_block(self):
        files = {LESSON: lesson(
            declaration(id="M9.1-VID-01", kind="video", subtype="explainer",
                        title="Teszt videó", source_ref="M9.1-VO",
                        a11y={"audio": "spoken", "visual": "decorative",
                              "alt_note": "x"},
                        derivatives=["captions", "transcript"],
                        blockers=["R5"]),
            source_block("M9.1-VO", "narration", "> „Szia!"))}
        asset = compile_corpus(files)["assets"][0]
        self.assertEqual([], asset["readiness_issues"])
        self.assertEqual("pending-production-rule", asset["status"],
                         "a strukturális gát megszűnt, a szabály-blokkoló veszi át")

    def test_authored_spec_ready_cannot_mask_a_missing_script(self):
        asset = self._asset(status="spec-ready")["assets"][0]
        self.assertEqual("blocked", asset["status"])

    def test_silent_video_is_not_blocked_for_a_missing_script(self):
        model = compile_corpus({LESSON: lesson(declaration(
            id="M9.1-VID-01", kind="video", subtype="screen-recording",
            title="Néma felvétel", spec="képernyőfelvétel",
            a11y={"audio": "silent", "visual": "decorative", "alt_note": "x"}))})
        asset = model["assets"][0]
        self.assertEqual([], asset["readiness_issues"])
        self.assertEqual("spec-ready", asset["status"])

    def test_music_without_a_script_is_not_treated_as_missing_narration(self):
        model = compile_corpus({LESSON: lesson(declaration(
            id="M9.1-HANG-01", kind="audio", subtype="music",
            title="Aláfestő zene", spec="licencelt zenei alap",
            derivatives=["transcript"]))})
        asset = model["assets"][0]
        self.assertEqual([], asset["readiness_issues"])
        self.assertNotEqual("blocked", asset["status"])

    def test_an_open_decision_outranks_a_production_rule(self):
        asset = compile_corpus({LESSON: lesson(declaration(
            id="M9.1-ILL-01", kind="illustration", title="Illusztráció",
            a11y={"visual": "decorative"}, blockers=["R5"],
            decision="Nyitott szerzői kérdés — a modul felelősével."))}) ["assets"][0]
        self.assertEqual("pending-human-decision", asset["status"])
        self.assertIn(mm.OPEN_DECISION, asset["readiness_issues"])

    def test_authored_spec_ready_cannot_hide_an_open_decision(self):
        asset = compile_corpus({LESSON: lesson(declaration(
            id="M9.1-ILL-01", kind="illustration", title="Illusztráció",
            a11y={"visual": "decorative"}, status="spec-ready",
            decision="Nyitott kérdés."))}) ["assets"][0]
        self.assertEqual("pending-human-decision", asset["status"])

    def test_clearing_the_decision_returns_the_rule_derived_status(self):
        asset = compile_corpus({LESSON: lesson(declaration(
            id="M9.1-ILL-01", kind="illustration", title="Illusztráció",
            a11y={"visual": "decorative"}, blockers=["R5"]))}) ["assets"][0]
        self.assertEqual([], asset["readiness_issues"])
        self.assertEqual("pending-production-rule", asset["status"])


# ==========================================================================
# Alt selectors cannot rebind (F-03)
# ==========================================================================

class TestAltSelectorSafety(unittest.TestCase):

    @staticmethod
    def _files(prescription: str, ref: str = "M9.1-DIA-01-ALT#1"):
        return {LESSON: lesson(
            declaration(id="M9.1-DIA-01", kind="diagram", title="Ábra",
                        a11y={"visual": "informative", "alt_source_ref": ref},
                        derivatives=["alt-text"]),
            source_block("M9.1-DIA-01-ALT", "alt-text", prescription))}

    def test_single_quote_source_resolves(self):
        model = compile_corpus(self._files('> **Alt-szöveg:** „Két oszlop.”'))
        self.assertEqual([], [str(e) for e in model["errors"]])
        self.assertEqual("Két oszlop.", model["assets"][0]["alt_text"])

    def test_an_unrelated_second_quote_makes_it_ambiguous(self):
        """The mutation that used to pass silently: one extra quotation."""
        problems = errors_of(self._files(
            '> A mezők „villannak fel”.\n> **Alt-szöveg:** „Két oszlop.”'))
        self.assertTrue(any("idézetet tartalmaz" in e for e in problems), problems)

    def test_a_positional_selector_is_rejected(self):
        """`#2` was how the Johari alt used to bind — never valid again."""
        problems = errors_of(self._files(
            '> A mezők „villannak fel”.\n> **Alt-szöveg:** „Két oszlop.”',
            ref="M9.1-DIA-01-ALT#2"))
        self.assertTrue(any("idézetet tartalmaz" in e for e in problems), problems)

    def test_an_out_of_range_selector_on_a_valid_source_is_a_hard_error(self):
        with self.assertRaises(mm.ManifestError):
            compile_corpus(self._files('> **Alt-szöveg:** „Két oszlop.”',
                                       ref="M9.1-DIA-01-ALT#2"))

    def test_out_of_range_selector_still_rejected(self):
        with self.assertRaises(mm.ManifestError):
            compile_corpus(self._files('> **Alt-szöveg:** „Egy.”',
                                       ref="M9.1-DIA-01-ALT#3"))


# ==========================================================================
# Drift detection and the content invariant
# ==========================================================================

class TestDriftDetection(unittest.TestCase):
    """Drift detection, exercised on a throwaway copy of the repository.

    These tests must mutate a lesson file and a generated CSV to prove the check
    fires. They do that in a temp copy and drive the copied CLI, never the live
    working tree: this repository carries unpushed hand-edited curriculum, and an
    interrupted run that left a lesson stripped of its metadata is exactly the
    failure class its history warns about.
    """

    @contextmanager
    def sandbox(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            (root / "tools").mkdir(parents=True)
            for name in ("media_manifest.py", "media_migrate_v2.py"):
                shutil.copy2(mm.ROOT / "tools" / name, root / "tools" / name)
            shutil.copytree(mm.ACTIVE_ROOT, root / "02 Tervezet")
            yield root

    @staticmethod
    def run_cli(root: Path, *args) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, str(root / "tools" / "media_manifest.py"),
                               *args], capture_output=True, text=True, cwd=str(root))

    def test_sandbox_starts_green(self):
        with self.sandbox() as root:
            result = self.run_cli(root, "check")
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)

    def test_editing_narration_without_rebuilding_makes_check_fail(self):
        """The exact CI scenario: a VO wording change with a stale registry."""
        with self.sandbox() as root:
            with mm._rel_root(root):
                model = mm.compile_manifest(root / "02 Tervezet", strict=False)
            target = next(s for s in model["sources"] if s["kind"] == "narration")
            path = root / target["file"]
            lines = path.read_text(encoding="utf-8").split("\n")
            first = target["body_lines"][0]
            lines[first - 1] += " EGY-ÚJ-SZÓ"
            path.write_text("\n".join(lines), encoding="utf-8")

            result = self.run_cli(root, "check")
            self.assertEqual(1, result.returncode, "a narráció megváltozott, mégsem bukott")
            self.assertIn("ELCSÚSZOTT", result.stderr)
            self.assertIn("assetek.csv", result.stderr)

            self.assertEqual(0, self.run_cli(root, "build").returncode)
            self.assertEqual(0, self.run_cli(root, "check").returncode)

    def test_hand_edited_generated_csv_makes_check_fail(self):
        with self.sandbox() as root:
            csv_path = root / mm.OUT_ASSETS_CSV.relative_to(mm.ROOT)
            csv_path.write_bytes(csv_path.read_bytes() + "kézi,sor\n".encode("utf-8"))
            result = self.run_cli(root, "check")
            self.assertEqual(1, result.returncode)
            self.assertIn("assetek.csv", result.stderr)

    def test_removing_a_declaration_makes_the_lint_speak_up(self):
        """The safety net has to be able to fire, not just stay silent."""
        with self.sandbox() as root:
            self.assertEqual(0, self.run_cli(root, "lint", "--high-only").returncode)
            with mm._rel_root(root):
                model = mm.compile_manifest(root / "02 Tervezet", strict=False)
            target = next(s for s in model["sources"] if s["kind"] == "narration")
            path = root / target["file"]
            path.write_text(mig.strip_metadata(path.read_text(encoding="utf-8")),
                            encoding="utf-8")
            result = self.run_cli(root, "lint", "--high-only")
            self.assertEqual(1, result.returncode, "a lint nem jelezte a hiányt")
            self.assertIn(Path(target["file"]).name, result.stdout)

    def test_a_new_lesson_with_an_undeclared_video_fails_the_lint(self):
        """An undeclared video drags mandatory captions with it — never MEDIUM."""
        with self.sandbox() as root:
            lesson = (root / "02 Tervezet/Modulok/M2/Online leckék"
                      / "M2.9 – Vadonatúj lecke.md")
            lesson.write_text(
                "# M2.9 – Vadonatúj lecke\n\n## SLIDE 1 – HOOK\n\n"
                "* Középen **AI beszélő fej videó** (16:9, felirattal).\n",
                encoding="utf-8")
            result = self.run_cli(root, "lint", "--high-only")
            self.assertEqual(1, result.returncode,
                             "deklarálatlan videó nem bukatta el a lintet")
            self.assertIn("M2.9", result.stdout)


class TestContentInvariant(unittest.TestCase):
    """No learner- or trainer-visible text may change without a recorded reason."""

    @staticmethod
    def _baseline_available() -> bool:
        result = subprocess.run(["git", "-C", str(mm.ROOT), "cat-file", "-e",
                                 f"{BASELINE_COMMIT}^{{commit}}"],
                                capture_output=True)
        return result.returncode == 0

    def test_only_approved_edits_changed_learner_visible_text(self):
        """Visible text may leave the baseline only as an approved, pinned version.

        The earlier allow-list had grown to name every authoring file, so it no
        longer caught anything. A file whose visible text differs from the
        baseline must now match its fingerprint in ``VISIBLE_PINS``; a visible
        edit fails here until it is re-pinned with a reason, and a pin that is no
        longer needed fails too. Metadata-only edits keep the fingerprint.
        """
        if not self._baseline_available():
            self.skipTest(f"a kiindulási commit ({BASELINE_COMMIT[:7]}) nem elérhető "
                          "(sekély klón) — a CI teljes historyval futtatja")
        pins = json.loads(VISIBLE_PINS.read_text(encoding="utf-8"))["files"]
        mismatches = pin_mismatches(pins, visible_texts_needing_pins())
        self.assertEqual([], mismatches["changed"],
                         "látható szöveg változott újrapinnelés (indoklás) nélkül")
        self.assertEqual([], mismatches["unpinned"],
                         "a kiindulástól eltérő látható szöveg pin nélkül")
        self.assertEqual([], mismatches["stale"], "elavult pin")

    def test_every_pin_records_its_reason(self):
        pins = json.loads(VISIBLE_PINS.read_text(encoding="utf-8"))["files"]
        self.assertTrue(pins, "a pin-fájl nem lehet üres")
        self.assertEqual([], sorted(rel for rel, pin in pins.items()
                                    if not str(pin.get("reason", "")).strip()))

    def test_a_visible_edit_is_reported_and_a_metadata_edit_is_not(self):
        body = lesson("Látható mondat a tanulónak.")
        pinned = {LESSON: {"sha256": visible_fingerprint(body), "reason": "teszt"}}
        with_metadata = lesson(MINIMAL, "Látható mondat a tanulónak.")
        self.assertEqual(visible_fingerprint(body), visible_fingerprint(with_metadata))
        self.assertEqual({"changed": [], "unpinned": [], "stale": []},
                         pin_mismatches(pinned, {LESSON: visible_fingerprint(with_metadata)}))
        edited = lesson("Látható mondat a tanulónak, átírva.")
        self.assertEqual([LESSON],
                         pin_mismatches(pinned, {LESSON: visible_fingerprint(edited)})["changed"])
        self.assertEqual(["új.md"],
                         pin_mismatches(pinned, {LESSON: pinned[LESSON]["sha256"],
                                                 "új.md": "x"})["unpinned"])
        self.assertEqual([LESSON], pin_mismatches(pinned, {})["stale"])


class TestForensicRemediationInvariants(unittest.TestCase):
    """Guards for the regressions fixed in the 2026-08-28 forensic remediation.

    These check instruction classes, not single sentences: the hidden media
    layer must not quietly reintroduce what the visible curriculum removed.
    """

    @classmethod
    def setUpClass(cls):
        cls.model = mm.compile_manifest()
        cls.assets = cls.model["assets"]
        cls.by_id = {a["id"]: a for a in cls.assets}

    @staticmethod
    def _asset_text(asset) -> str:
        parts = [str(asset.get(k, "")) for k in
                 ("title", "purpose", "spec", "notes", "review")]
        a11y = asset.get("a11y") or {}
        tech = asset.get("technical") or {}
        parts += [str(v) for v in a11y.values()] + [str(v) for v in tech.values()]
        return " ".join(parts)

    # --- F-01: Study Lab hidden specs stay non-identifying -------------------

    #: Phrases that prescribe a public, per-person progress marking. Negated
    #: mentions ("nincs … állapotsor") deliberately do not match.
    _PUBLIC_STATUS = (
        "állapotfelmérő tábl", "állapot-tábla", "haladás-követő",
        "ki hol tart", "hol tartanak az", "állapotánál lévő",
        "matricával jelölik", "leckesorhoz ragaszt", "lecke-sorhoz ragaszt",
        "sor: „kész az m",
    )

    def test_study_lab_specs_do_not_encode_public_per_person_progress(self):
        violations = []
        for asset in self.assets:
            if not asset.get("unit", "").endswith(".F"):
                continue
            text = self._asset_text(asset).lower()
            for phrase in self._PUBLIC_STATUS:
                if phrase in text:
                    violations.append(f"{asset['id']}: {phrase!r}")
        self.assertEqual([], violations,
                         "Study Lab rejtett spec újra nyilvános, személyhez "
                         "köthető haladás-jelölést ír elő")

    def test_every_study_lab_orientation_board_exists_and_is_anonymous(self):
        for unit in ("M1.F", "M2.F", "M3.F", "M4.F", "M5.F", "M6.F", "M7.F"):
            asset = self.by_id.get(f"{unit}-POSZ-01")
            self.assertIsNotNone(asset, f"{unit}-POSZ-01 hiányzik")
            self.assertIn("név nélküli témakérés", self._asset_text(asset),
                          f"{unit}-POSZ-01: a tájékozódó tábla anonim "
                          "témakérés-funkciója eltűnt")

    # --- F-09: a narration's transcript pointer names its own deliverable ----

    _TRANSCRIPT_REF = re.compile(
        r"Felirat/leirat szükséges \(([A-Za-z0-9.\-]+)::TRANSCRIPT")

    def test_narration_transcript_notes_reference_their_own_asset(self):
        wrong = []
        for asset in self.assets:
            note = str((asset.get("a11y") or {}).get("note", ""))
            for ref in self._TRANSCRIPT_REF.findall(note):
                if ref != asset["id"]:
                    wrong.append(f"{asset['id']} → {ref}::TRANSCRIPT")
        self.assertEqual([], wrong,
                         "narráció a szomszéd asset leiratára hivatkozik")

    # --- R-16: M7.F media wording tracks the real v1 product of M7.4 ---------

    def test_m7f_media_specs_do_not_call_the_m74_product_v2(self):
        for asset in self.assets:
            if asset.get("unit") != "M7.F":
                continue
            self.assertNotIn("L4 – Peula v2", self._asset_text(asset),
                             f"{asset['id']}: az M7.4 terméke Peula v1, nem v2")


# ==========================================================================
# Composition — one runtime artefact assembled from several components
# ==========================================================================

class TestComposition(unittest.TestCase):
    """`composed_of`: the H5P Interactive Video case, made machine-checkable.

    An Interactive Video takes one base video and one `textTracks` list, so three
    scene clips become one file with one caption track. The container therefore
    owns the text tracks and its script is the components' scripts in order —
    never a fourth copy of the same words.
    """

    def _corpus(self, container=None, scene_extra=None, scenes=3, scene_source=True):
        container = container or {}
        scene_extra = scene_extra or {}
        parts = []
        for n in range(1, scenes + 1):
            fields = dict(id=f"M9.1-VID-0{n + 1}", kind="video", subtype="explainer",
                          title=f"Jelenet {n}", spec="jelenetvideó",
                          a11y={"audio": "spoken", "visual": "decorative",
                                "alt_note": "a felirat lefedi"},
                          derivatives=[])
            if scene_source:
                fields["source_ref"] = f"M9.1-NAR-0{n}-VO"
            fields.update(scene_extra)
            parts.append(declaration(**fields))
            if scene_source:
                parts.append(source_block(f"M9.1-NAR-0{n}-VO", "narration",
                                          f"> „{n}. jelenet szövege."))
        fields = dict(id="M9.1-VID-01", kind="video", subtype="interactive",
                      title="Interactive Video", spec="konténer",
                      composed_of=[f"M9.1-VID-0{n + 1}" for n in range(1, scenes + 1)],
                      a11y={"audio": "spoken", "visual": "decorative",
                            "alt_note": "a felirat lefedi"},
                      derivatives=["captions", "transcript"])
        fields.update(container)
        return compile_corpus({LESSON: lesson(declaration(**fields), *parts)})

    def test_container_script_is_the_components_in_order(self):
        model = self._corpus()
        self.assertEqual([], [str(e) for e in model["errors"]])
        container = next(a for a in model["assets"] if a["id"] == "M9.1-VID-01")
        self.assertEqual([], container["readiness_issues"])
        self.assertEqual("spec-ready", container["status"])
        self.assertEqual(["M9.1-NAR-01-VO", "M9.1-NAR-02-VO", "M9.1-NAR-03-VO"],
                         container["composed_source_ids"])
        self.assertEqual("„1. jelenet szövege.\n\n„2. jelenet szövege."
                         "\n\n„3. jelenet szövege.", container["source_text"])

    def test_caption_text_follows_the_lesson_through_the_components(self):
        captions = [d for d in self._corpus()["deliverables"]
                    if d["id"] == "M9.1-VID-01::CAPTIONS"]
        self.assertEqual(1, len(captions))
        self.assertIn("2. jelenet szövege", captions[0]["text"])

    def test_components_produce_no_second_caption_file(self):
        ids = [d["id"] for d in self._corpus()["deliverables"]]
        self.assertIn("M9.1-VID-01::CAPTIONS", ids)
        self.assertNotIn("M9.1-VID-02::CAPTIONS", ids)
        self.assertNotIn("M9.1-VID-02::TRANSCRIPT", ids)

    def test_a_component_may_not_duplicate_the_runtime_track(self):
        errors = " ".join(str(e) for e in self._corpus(
            scene_extra={"derivatives": ["captions", "transcript"]})["errors"])
        self.assertIn("konténer része", errors)

    def test_a_component_without_a_script_is_rejected(self):
        errors = " ".join(str(e) for e in
                          self._corpus(scene_source=False)["errors"])
        self.assertIn("nincs forrásszövege", errors)

    def test_a_component_without_a_script_never_makes_the_container_ready(self):
        model = self._corpus(scene_source=False)
        container = next(a for a in model["assets"] if a["id"] == "M9.1-VID-01")
        self.assertIn(mm.MISSING_SPOKEN_SOURCE, container["readiness_issues"])
        self.assertEqual("blocked", container["status"])

    def test_container_may_not_have_two_scripts(self):
        errors = " ".join(str(e) for e in self._corpus(
            container={"source_ref": "M9.1-NAR-01-VO"})["errors"])
        self.assertIn("két igazsága", errors)

    def test_container_must_declare_the_text_tracks(self):
        errors = " ".join(str(e) for e in
                          self._corpus(container={"derivatives": []})["errors"])
        self.assertIn("kompozit konténer", errors)

    def test_dangling_component_rejected(self):
        errors = " ".join(str(e) for e in self._corpus(
            container={"composed_of": ["M9.1-VID-99"]})["errors"])
        self.assertIn("nem létező assetre mutat", errors)

    def test_nested_composition_rejected(self):
        errors = " ".join(str(e) for e in self._corpus(
            scene_extra={"composed_of": ["M9.1-VID-02"]})["errors"])
        self.assertIn("maga is kompozit", errors)

    def test_composition_only_on_a_spoken_video(self):
        errors = " ".join(str(e) for e in self._corpus(
            container={"kind": "illustration", "subtype": "",
                       "a11y": {"visual": "decorative"}, "derivatives": []})["errors"])
        self.assertIn("nem beszélt videó", errors)

    def test_composition_is_part_of_the_spec_hash(self):
        one = self._corpus()["assets"]
        two = self._corpus(container={"composed_of": ["M9.1-VID-03", "M9.1-VID-02",
                                                      "M9.1-VID-04"]})["assets"]
        first = next(a for a in one if a["id"] == "M9.1-VID-01")["spec_hash"]
        second = next(a for a in two if a["id"] == "M9.1-VID-01")["spec_hash"]
        self.assertNotEqual(first, second, "a sorrend a szkript része")


# ==========================================================================
# Blocker semantics — a gate may not spread beyond what its rule says
# ==========================================================================

class TestBlockerSemantics(unittest.TestCase):
    """Each production gate must sit on exactly the assets its own text covers."""

    @classmethod
    def setUpClass(cls):
        cls.model = mm.compile_manifest()
        cls.by_id = {a["id"]: a for a in cls.model["assets"]}

    def _with(self, blocker):
        return [a for a in self.model["assets"] if blocker in a["blockers"]]

    def test_r2_covers_synthetic_human_personas_only(self):
        """R2 is avatar/voice rights, not a general AI-content gate."""
        for asset in self._with("R2"):
            self.assertIn(asset["kind"], ("video", "photo", "voiceover"), asset["id"])
            self.assertEqual("ai", asset["provenance"], asset["id"])
        ai_visuals = [a for a in self.model["assets"]
                      if a["provenance"] == "ai"
                      and a["kind"] in ("illustration", "icon-set", "diagram",
                                        "poster", "card-set", "worksheet")]
        self.assertTrue(ai_visuals)
        for asset in ai_visuals:
            self.assertNotIn("R2", asset["blockers"],
                             f"{asset['id']} hétköznapi AI-vizuál, nem avatar")

    def test_r2_holds_every_synthetic_narration(self):
        """With D2 = synthetic voice, R2 covers every narration
        (RIGHTS-EVIDENCE.md, "Fontos következmény" under the R2 table)."""
        narrations = [a for a in self.model["assets"]
                      if a["kind"] == "voiceover" and a["provenance"] == "ai"]
        self.assertTrue(narrations)
        for asset in narrations:
            self.assertIn("R2", asset["blockers"], asset["id"])

    def test_r2_holds_every_talking_head_and_character_scene(self):
        for asset in self.model["assets"]:
            if asset["kind"] == "video" and asset["subtype"] == "ai-talking-head":
                self.assertIn("R2", asset["blockers"], asset["id"])
        for aid in ("M4.1-VID-03", "M4.1-VID-04", "M4.1-VID-05", "M1.3-VID-01"):
            self.assertIn("R2", self.by_id[aid]["blockers"], aid)

    def test_r8_covers_real_captures_only(self):
        """R8's text is scoped to a real photo or screenshot."""
        for asset in self._with("R8"):
            self.assertEqual("photo", asset["kind"], asset["id"])
            self.assertEqual("human", asset["provenance"], asset["id"])
        for asset in self.model["assets"]:
            if asset["kind"] == "photo" and asset["provenance"] == "human":
                self.assertIn("R8", asset["blockers"], asset["id"])

    def test_a_procurement_item_is_not_gated_on_image_rights(self):
        for asset in self.model["assets"]:
            if asset["mode"] == "external" and asset["subtype"] == "consumable":
                self.assertNotIn("R8", asset["blockers"], asset["id"])
                self.assertEqual("spec-ready", asset["status"], asset["id"])

    def test_r7_only_gates_the_runtime_dependent_screenshot(self):
        gated = self._with("R7")
        self.assertEqual(["M0.3-FOTO-01"], [a["id"] for a in gated])
        self.assertIn("screenshot", gated[0]["title"].lower())

    def test_r5_is_a_closed_convention_that_blocks_no_asset(self):
        """D1 closed on 2026-10-02 (HUM-MEDIA-01): the palette and style token are fixed.

        R5 stays a production rule (one icon batch, a locked reference character for
        the AI character scenes), but it has no open value left, so it may not hold
        any asset. The character scenes stay blocked by their rights gates.
        """
        rule = next(r for r in mm.production_rules() if r["id"] == "R5")
        self.assertNotIn("KITÖLTENDŐ", rule["text"])
        self.assertIn("M1.3-VID-01", rule["text"])
        self.assertIn("M4.1-VID-03/04/05", rule["text"])
        self.assertEqual([], self._with("R5"))
        for aid in ("M1.3-VID-01", "M4.1-VID-03", "M4.1-VID-04", "M4.1-VID-05"):
            self.assertIn("R2", self.by_id[aid]["blockers"], aid)

    def test_resolving_a_rule_never_lifts_a_structural_block(self):
        for asset in self.model["assets"]:
            if mm.MISSING_SPOKEN_SOURCE in asset["readiness_issues"]:
                self.assertEqual("blocked", asset["status"], asset["id"])
            elif asset["decision"]:
                self.assertIn(asset["status"], ("blocked", "pending-human-decision"),
                              asset["id"])

    def test_the_reworked_card_kept_its_historical_row(self):
        """M3.B-KART-03 was re-specified, not deleted: its v1 row still maps."""
        asset = self.by_id["M3.B-KART-03"]
        self.assertEqual(["M3.B-KART-03"], asset["legacy"]["asset"])
        recon = mm.reconcile(self.model)
        row = next(r for r in recon["rows"] if r[0] == "M3.B-KART-03")
        self.assertNotEqual("CURRENTLY_UNMAPPED_ERROR", row[7])
        self.assertEqual(747, recon["legacy_total"])
        self.assertEqual(0, recon["unmapped"])


# ==========================================================================
# Production plan — a derived view, never a second source of truth
# ==========================================================================

class TestProductionPlan(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model = mm.compile_manifest()
        cls.plan = mm.plan_model(cls.model)
        cls.produced = mm.central_production(cls.model)

    def test_every_produced_asset_lands_in_exactly_one_batch(self):
        """Batches plus the live-session section together cover everything made."""
        placed = [a["id"] for batch in self.plan["batches"] for a in batch["assets"]]
        self.assertEqual(len(placed), len(set(placed)))
        made = {a["id"] for a in self.model["assets"] if a["mode"] != "reuse"}
        self.assertEqual(made, set(placed))
        central = {a["id"] for a in self.produced}
        live = {a["id"] for a in self.model["assets"] if mm.is_live_deliverable(a)}
        self.assertEqual(made, central | live)
        self.assertEqual(set(), central & live)

    def test_batch_zero_has_no_open_gate(self):
        batch = next(b for b in self.plan["batches"] if b["key"] == "B0")
        for asset in batch["assets"]:
            self.assertEqual(set(), mm.asset_gates(asset), asset["id"])
            self.assertEqual("spec-ready", asset["status"], asset["id"])
        self.assertTrue(batch["assets"], "üres BATCH 0 gyanús")

    def test_no_batch_hides_a_later_gate(self):
        """A batch's own gate may not be the only one listed for its members."""
        for batch in self.plan["batches"]:
            for asset in batch["assets"]:
                self.assertEqual(batch["key"], mm.batch_of(asset), asset["id"])

    def test_plan_csv_covers_every_deliverable(self):
        rows = mm.plan_csv_rows(self.model)
        self.assertEqual(len(self.model["deliverables"]), len(rows))
        self.assertEqual({d["id"] for d in self.model["deliverables"]},
                         {row[3] for row in rows})

    def test_gate_impact_arithmetic_holds(self):
        for row in self.plan["impact"]:
            gate = row["gate"]
            affected = [a for a in self.produced if gate in mm.asset_gates(a)]
            alone = [a for a in affected if mm.asset_gates(a) == {gate}]
            self.assertEqual(len(affected), row["assets"], gate)
            self.assertEqual(len(alone), row["unblocked_alone"], gate)
            self.assertEqual(row["assets"], row["unblocked_alone"] + row["still_blocked"],
                             gate)

    def test_impact_never_claims_more_than_the_reference_count(self):
        for row in self.plan["impact"]:
            self.assertLessEqual(row["unblocked_alone"], row["assets"], row["gate"])

    def test_waves_end_with_everything_producible(self):
        waves = self.plan["waves"]
        self.assertEqual(sorted(w["cumulative_assets"] for w in waves),
                         [w["cumulative_assets"] for w in waves])
        self.assertEqual(len(self.produced), waves[-1]["cumulative_assets"])

    def test_each_pilot_is_a_real_producible_member_of_its_family(self):
        by_id = {a["id"]: a for a in self.model["assets"]}
        for key, info in self.plan["pilots"].items():
            asset = by_id[info["asset"]["id"]]
            self.assertNotEqual("reuse", asset["mode"], key)
            matches = next(m for k, _l, m in mm.PILOT_FAMILIES if k == key)
            self.assertTrue(matches(asset), key)
            fewest = min(len(mm.asset_gates(a)) for a in self.produced if matches(a))
            self.assertEqual(fewest, len(mm.asset_gates(asset)),
                             f"{key}: a pilot nem a legkevésbé blokkolt tétel")

    def test_plan_is_derived_and_deterministic(self):
        first = mm.render_plan_md(mm.compile_manifest())
        second = mm.render_plan_md(mm.compile_manifest())
        self.assertEqual(first, second)
        self.assertIn(f"| Szemantikus asset | **{len(self.model['assets'])}** |", first)

    def test_plan_does_not_mint_a_new_release_blocker(self):
        """The open gates are counted once, where their canonical text lives."""
        self.assertNotIn("KITÖLTENDŐ", mm.OUT_PLAN_MD.read_text(encoding="utf-8"))

    def test_colour_dependency_reads_the_declaration_not_a_guess(self):
        by_id = {a["id"]: a for a in self.model["assets"]}
        self.assertEqual("colour", mm.colour_dependency(by_id["M1.3-IKO-01"]))
        self.assertEqual("bw", mm.colour_dependency(by_id["M1.F-MUNK-01"]))


# ==========================================================================
# Approved production decisions — the closure this pass applied
# ==========================================================================

class TestApprovedDecisions(unittest.TestCase):
    """Each user-approved decision must be visible in the canonical source.

    A decision that only exists in a decision document has not been applied. These
    assert the manifest and the lessons actually carry it.
    """

    @classmethod
    def setUpClass(cls):
        cls.model = mm.compile_manifest()
        cls.by_id = {a["id"]: a for a in cls.model["assets"]}

    # --- D9: one canonical learner-visible AI provenance label ---------------

    #: A quoted span reads as a provenance label when it names AI, says the thing
    #: was generated, and credits the human review. Calibrated against the whole
    #: active curriculum: it matches every real label and nothing else — not
    #: "Mit NEM teszel AI-val?", not the learner's own AI-use sentence.
    _QUOTE = re.compile(r"„([^„”]{0,200})”")
    _NAMES_AI = re.compile(r"AI", re.IGNORECASE)
    _WAS_GENERATED = re.compile(r"generált|generatív|AI-eszközzel|AI-val", re.IGNORECASE)
    _HUMAN_REVIEWED = re.compile(r"lektorál|emberi|ember írta|médiaelem", re.IGNORECASE)

    @classmethod
    def _label_shaped_quotes(cls):
        """(file, line, text) for every quote in the active curriculum that reads
        as an AI provenance label. `Média-assetek/` is excluded: it is the
        production area, and its decision records legitimately quote retired
        wordings as history."""
        for path in sorted(mm.ACTIVE_ROOT.rglob("*.md")):
            if path.is_relative_to(mm.MEDIA_ROOT):
                continue
            for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                for match in cls._QUOTE.finditer(line):
                    quote = match.group(1)
                    if (cls._NAMES_AI.search(quote) and cls._WAS_GENERATED.search(quote)
                            and cls._HUMAN_REVIEWED.search(quote)):
                        yield path.name, lineno, quote

    def test_the_canonical_ai_label_is_recorded_with_its_rule(self):
        label = mm.human_ai_label()
        self.assertTrue(label, "az R1-nek hordoznia kell a jóváhagyott címkeszöveget")
        rule = next(r for r in mm.production_rules() if r["id"] == "R1")
        self.assertIn(label, rule["text"],
                      "a szabály szövege és a `human_label` mező nem mondhat mást")

    def test_every_live_ai_provenance_label_uses_the_canonical_wording(self):
        label = mm.human_ai_label()
        found = list(self._label_shaped_quotes())
        self.assertGreater(len(found), 10, "a felderítő nem talált címkéket — romlott a minta")
        divergent = [f"{name}:{line} → {quote!r}"
                     for name, line, quote in found if quote != label]
        self.assertEqual([], divergent,
                         "eltérő AI-provenance címkeszöveg az aktív tananyagban")

    def test_the_retired_label_variants_are_gone_from_the_curriculum(self):
        retired = ("🤖 Ez a videó generatív AI-val készült.",
                   "AI-generált avatar, a szöveget ember írta és lektorálta",
                   "A videó AI-eszközzel készült, emberi lektorálással.",
                   "AI-generált avatar, narrációt madrich lektorálta")
        for path in sorted(mm.ACTIVE_ROOT.rglob("*.md")):
            if path.is_relative_to(mm.MEDIA_ROOT):
                continue
            text = path.read_text(encoding="utf-8")
            for variant in retired:
                self.assertNotIn(variant, text, f"{path.name}: visszavont címkeváltozat")

    def test_the_provenance_ui_text_assets_carry_the_canonical_copy(self):
        label = mm.human_ai_label()
        for asset_id in ("M5.1-EGY-01", "M6.1-EGY-01"):
            self.assertIn(label, self.by_id[asset_id]["spec"], asset_id)

    # --- D6: the approved M1.3 dialogue is now a canonical source -------------

    def test_m13_hook_dialogue_is_a_live_source_not_a_pending_draft(self):
        asset = self.by_id["M1.3-VID-01"]
        self.assertEqual("M1.3-VID-01-VO", asset["source_ref"])
        # D6 closed the script; the open D11 (dialogue voices, lip-sync production)
        # is a separate decision and must not reopen it.
        self.assertIn("D11", asset["decision"])
        self.assertNotIn("szkript-döntés", asset["decision"])
        self.assertEqual([mm.OPEN_DECISION], asset["readiness_issues"])
        self.assertNotIn(mm.MISSING_SPOKEN_SOURCE, asset["readiness_issues"])
        for phrase in ("Te mindig szétvered a peulát, komolyan mondom",
                       "Mi van?! Csak próbáltam feldobni a hangulatot",
                       "háromszor félbeszakítottad a többieket",
                       "megtartani a figyelmüket és a bevonódásukat",
                       "Jaa… erre nem is gondoltam. Oké, figyelek rá"):
            self.assertIn(phrase, asset["source_text"], phrase)

    def test_m13_hook_still_carries_its_real_gates(self):
        """Approving the script must not make the video producible.

        D1 (the visual system) closed on 2026-10-02, so R5 no longer holds it;
        the rights gates (R2, R3) and the D11 voice decision still do.
        """
        asset = self.by_id["M1.3-VID-01"]
        self.assertEqual({"R2", "R3"}, set(asset["blockers"]))
        self.assertEqual("pending-human-decision", asset["status"])

    def test_the_lesson_no_longer_hedges_the_approved_dialogue(self):
        lesson = (mm.ACTIVE_ROOT / "Modulok/M1/Online leckék"
                  / "M1.3 – SBI-modell – hogyan adjak korrekt visszajelzést.md")
        rendered = mig.strip_metadata(lesson.read_text(encoding="utf-8"))
        self.assertNotIn("Nagyjából a fenti mondatok", rendered)

    # --- D5: one canonical M3 safeguarding map, reused by the hub ------------

    def test_m3_hub_safeguarding_map_reuses_the_canonical_five_step_asset(self):
        hub = self.by_id["M3-HUB-POSZ-01"]
        self.assertEqual("reuse", hub["mode"])
        self.assertEqual("M3.B-MUNK-01", hub["reuse_of"])
        self.assertEqual("M3.B-MUNK-01", hub["reuse_resolves_to"])
        self.assertEqual([], hub["deliverable_ids"],
                         "a hub reuse nem gyárthat külön 903. deliverable-t")
        deliverables = {d["id"] for d in self.model["deliverables"]}
        self.assertIn("M3.B-MUNK-01", deliverables)
        self.assertNotIn("M3-HUB-POSZ-01", deliverables)

    # --- D7: the optional M3.2 narration is not produced ----------------------

    def test_m32_optional_narration_is_no_longer_a_current_asset(self):
        self.assertNotIn("M3.2-NAR-02", self.by_id)
        deliverables = {d["id"] for d in self.model["deliverables"]}
        for gone in ("M3.2-NAR-02", "M3.2-NAR-02::CAPTIONS", "M3.2-NAR-02::TRANSCRIPT"):
            self.assertNotIn(gone, deliverables)

    def test_the_dropped_narration_keeps_an_honest_historical_disposition(self):
        recon = mm.reconcile(self.model)
        by_old = {row[0]: row for row in recon["rows"]}
        for old_id in ("M3.2-NAR-02", "M3.2-FEL-02", "M3.2-LEI-02"):
            self.assertIn(old_id, by_old)
            status, reason = by_old[old_id][7], by_old[old_id][8]
            self.assertEqual("NO_LONGER_REQUIRED", status, old_id)
            self.assertTrue(reason.strip(), f"{old_id} indoklás nélkül")
        self.assertEqual(747, recon["legacy_total"])
        self.assertEqual(0, recon["unmapped"])
        self.assertEqual([], recon["conflicts"])

    def test_the_m32_slide_keeps_its_visible_content(self):
        lesson = (mm.ACTIVE_ROOT / "Modulok/M3/Online leckék"
                  / "M3.2 – Parparim, Kivsza, Leviatán – 3 kvuca, 3 világ.md")
        text = lesson.read_text(encoding="utf-8")
        for kept in ("Miért fontos, hogy máshogy nézz rá a kvucákra?",
                     "előbb-utóbb vagy ők fognak unatkozni, vagy te készülsz ki teljesen",
                     "gyors **„fejprofilod”** mind a három aktuális kvucáról"):
            self.assertIn(kept, text, kept)

    # --- D4: the M4 HOOK format question is answered -------------------------

    def test_the_m4_hook_decision_is_closed_and_the_closed_d1_released_the_asset(self):
        asset = self.by_id["M4.2-ILL-01"]
        self.assertEqual("", asset["decision"])
        self.assertEqual("spec-ready", asset["status"])
        self.assertNotIn("R5", asset["blockers"])
        for lesson in ("M4.2 – Aktív hallgatás & visszatükrözés.md",
                       "M4.3 – Kérdezési minták – nyitott, zárt, tisztázó, irányító kérdések.md",
                       "M4.4 – 45 mp-es peulabemutató – vázlat egy konkrét kvucára.md"):
            unit = lesson.split(" ")[0]
            videos = [a for a in self.model["assets"]
                      if a["unit"] == unit and a["kind"] == "video"]
            self.assertEqual([], videos, f"{unit}: nem készül új beszélőfej-videó")

    # --- D3: R2 scope stays conservative -------------------------------------

    def test_r2_still_covers_the_character_scenes_and_their_stills(self):
        for asset_id in ("M1.3-VID-01", "M4.1-VID-02", "M4.1-VID-03",
                         "M4.1-VID-04", "M4.1-VID-05",
                         "M4.1-FOTO-01", "M4.1-FOTO-02"):
            self.assertIn("R2", self.by_id[asset_id]["blockers"], asset_id)


# ==========================================================================
# Live-session deliverables — real, required, but not pre-producible
# ==========================================================================

class TestLiveDeliverables(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.model = mm.compile_manifest()
        cls.plan = mm.plan_model(cls.model)
        cls.by_id = {a["id"]: a for a in cls.model["assets"]}

    def test_the_closing_circle_note_is_marked_live(self):
        asset = self.by_id["M0.A-EGY-01"]
        self.assertTrue(mm.is_live_deliverable(asset))
        self.assertEqual("trainer-at-runtime", asset["technical"]["production_phase"])

    def test_a_live_item_is_never_in_the_ready_now_batch(self):
        batch0 = next(b for b in self.plan["batches"] if b["key"] == "B0")
        for asset in batch0["assets"]:
            self.assertFalse(mm.is_live_deliverable(asset), asset["id"])
        self.assertNotIn("M0.A-EGY-01", [a["id"] for a in batch0["assets"]])

    def test_a_live_item_stays_in_the_manifest_and_in_the_plan(self):
        """Not counted as ready — but never quietly dropped either."""
        live = [a for a in self.model["assets"] if mm.is_live_deliverable(a)]
        self.assertTrue(live)
        deliverables = {d["asset_id"] for d in self.model["deliverables"]}
        section = next(b for b in self.plan["batches"] if b["key"] == "BRT")
        for asset in live:
            self.assertIn(asset["id"], deliverables, f"{asset['id']} deliverable nélkül")
            self.assertIn(asset["id"], [a["id"] for a in section["assets"]])
        plan_md = mm.OUT_PLAN_MD.read_text(encoding="utf-8")
        for asset in live:
            self.assertIn(asset["id"], plan_md)

    def test_live_items_are_outside_the_central_production_universe(self):
        central = {a["id"] for a in mm.central_production(self.model)}
        for asset in self.model["assets"]:
            if mm.is_live_deliverable(asset):
                self.assertNotIn(asset["id"], central, asset["id"])

    def test_a_live_item_is_never_nominated_as_a_pilot(self):
        for key, info in self.plan["pilots"].items():
            self.assertFalse(mm.is_live_deliverable(info["asset"]), key)

    def test_an_org_decision_closed_in_the_register_releases_its_assets(self):
        """`M3.4-EGY-03` and `M3.4-DIA-01` waited on HUM-SAFE-04 (the ken alcohol and tobacco code).

        The approval register closed HUM-SAFE-04 on 2026-10-02, so neither asset may
        still carry a `decision` or read as pending-human-decision. If a veto reopens
        the item, the `decision` field goes back on both assets and this test flips
        back with the register heading.
        """
        approvals = (mm.ACTIVE_ROOT / "Emberi jóváhagyás szükséges.md").read_text(encoding="utf-8")
        self.assertIn("HUM-SAFE-04 — Alkohol- és dohányzási szabály — LEZÁRVA", approvals)
        by_id = {a["id"]: a for a in self.model["assets"]}
        for asset_id in ("M3.4-EGY-03", "M3.4-DIA-01"):
            asset = by_id[asset_id]
            self.assertFalse(asset.get("decision"), asset_id)
            self.assertNotEqual("pending-human-decision", asset["status"], asset_id)

    def test_plan_totals_still_agree_with_the_manifest(self):
        rows = mm.plan_csv_rows(self.model)
        self.assertEqual(len(self.model["deliverables"]), len(rows))
        placed = [a["id"] for b in self.plan["batches"] for a in b["assets"]]
        produced = [a["id"] for a in self.model["assets"] if a["mode"] != "reuse"]
        self.assertEqual(sorted(produced), sorted(placed))


if __name__ == "__main__":
    if len(sys.argv) >= 2 and sys.argv[1] == "--pin-visible":
        sys.exit(pin_visible_text(" ".join(sys.argv[2:])))
    unittest.main()
