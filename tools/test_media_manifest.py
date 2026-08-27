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

import json
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

    def test_no_generated_field_carries_the_retired_h5p_type(self):
        """`Short Answer` / `Essay` survived only in the frozen snapshot."""
        legacy_hits = [r["assetId"] for r in mm.load_legacy()["assets"]
                       if "Short Answer" in (r["lineRef"] or "") + (r["verbatim"] or "")]
        self.assertTrue(legacy_hits, "a v1 pillanatkép tartalmazta a visszavont típust")
        payload = mm.render_manifest_json(self.model)
        self.assertNotIn("Short Answer", payload)
        self.assertNotIn("Short answer", payload)

    def test_m41_caption_rule_follows_the_current_lesson(self):
        """M4.1 separates audio-only from spoken video; captions are not optional."""
        videos = [a for a in self.model["assets"]
                  if a["unit"] == "M4.1" and a["kind"] == "video"
                  and a["a11y"].get("audio") == "spoken"]
        self.assertTrue(videos)
        for asset in videos:
            self.assertIn("captions", asset["derivatives"], asset["id"])
            self.assertIn("transcript", asset["derivatives"], asset["id"])
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

    def test_asset_free_files_state_a_reason(self):
        for file_rec in self.model["files"]:
            if file_rec["assets"] or not file_rec["file"].startswith("02 Tervezet/Modulok"):
                continue
            self.assertTrue(file_rec["asset_free_reason"],
                            f"{file_rec['file']}: nincs @asset-free indoklás")


# ==========================================================================
# Drift detection and the content invariant
# ==========================================================================

class TestDriftDetection(unittest.TestCase):

    def test_editing_narration_without_rebuilding_makes_check_fail(self):
        """The exact CI scenario: a VO wording change with a stale registry."""
        model = mm.compile_manifest()
        outputs = mm.build_outputs(model)
        self.assertEqual([], mm.compare_outputs(outputs))

        target = next(s for s in model["sources"] if s["kind"] == "narration")
        path = mm.ROOT / target["file"]
        original = path.read_text(encoding="utf-8")
        first, last = target["body_lines"]
        lines = original.split("\n")
        lines[first - 1] = lines[first - 1] + " EGY-ÚJ-SZÓ"
        try:
            path.write_text("\n".join(lines), encoding="utf-8")
            edited = mm.build_outputs(mm.compile_manifest())
            stale = mm.compare_outputs(edited)
            self.assertTrue(stale, "a narráció megváltozott, mégsem lett elcsúszás")
            self.assertTrue(any("assetek.csv" in entry for entry in stale))
        finally:
            path.write_text(original, encoding="utf-8")
        self.assertEqual([], mm.compare_outputs(mm.build_outputs(mm.compile_manifest())))

    def test_hand_edited_generated_csv_makes_check_fail(self):
        path = mm.OUT_ASSETS_CSV
        original = path.read_bytes()
        try:
            path.write_bytes(original + "kézi,sor\r\n".encode("utf-8"))
            stale = mm.compare_outputs(mm.build_outputs(mm.compile_manifest()))
            self.assertTrue(any("assetek.csv" in entry for entry in stale))
        finally:
            path.write_bytes(original)

    def test_removing_a_declaration_makes_the_lint_speak_up(self):
        """The safety net has to be able to fire, not just stay silent."""
        model = mm.compile_manifest()
        self.assertEqual([], [f for f in mm.lint(model) if f["confidence"] == "HIGH"])
        target = next(s for s in model["sources"] if s["kind"] == "narration")
        path = mm.ROOT / target["file"]
        original = path.read_text(encoding="utf-8")
        stripped = mig.strip_metadata(original)
        try:
            path.write_text(stripped, encoding="utf-8")
            findings = mm.lint(mm.compile_manifest(strict=False))
            high = [f for f in findings if f["confidence"] == "HIGH"
                    and f["file"] == target["file"]]
            self.assertTrue(high, "a lint nem jelezte a deklaráció eltűnését")
        finally:
            path.write_text(original, encoding="utf-8")


class TestContentInvariant(unittest.TestCase):
    """No learner- or trainer-visible text may hide inside the migration."""

    @staticmethod
    def _baseline_available() -> bool:
        result = subprocess.run(["git", "-C", str(mm.ROOT), "cat-file", "-e",
                                 f"{BASELINE_COMMIT}^{{commit}}"],
                                capture_output=True)
        return result.returncode == 0

    def test_stripping_v2_metadata_restores_the_baseline_byte_for_byte(self):
        if not self._baseline_available():
            self.skipTest(f"a kiindulási commit ({BASELINE_COMMIT[:7]}) nem elérhető "
                          "(sekély klón) — a CI teljes historyval futtatja")
        differences = []
        touched = 0
        for path in mm.discover_sources():
            rel = path.relative_to(mm.ROOT).as_posix()
            blob = subprocess.run(["git", "-C", str(mm.ROOT), "show",
                                   f"{BASELINE_COMMIT}:{rel}"], capture_output=True)
            if blob.returncode != 0:
                differences.append(f"{rel}: nincs a kiindulási commitban")
                continue
            baseline = blob.stdout.decode("utf-8")
            current = path.read_text(encoding="utf-8")
            if current != baseline:
                touched += 1
            if mig.strip_metadata(current) != baseline:
                differences.append(rel)
        self.assertEqual([], differences,
                         "a v2 metaadat eltávolítása után is maradt eltérés")
        self.assertGreater(touched, 0, "a migrációnak érintenie kellett fájlokat")


if __name__ == "__main__":
    unittest.main()
