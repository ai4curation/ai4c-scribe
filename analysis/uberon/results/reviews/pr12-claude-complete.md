---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 12
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.473
precision: 0.329
recall: 0.839
jaccard: 0.310
outcome: partial_success
failure_modes:
  - missed_requirement
case_quality: poor
case_quality_reason: gold_reserialization_and_odk_import_domination
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This attempt is functionally identical to pr17 (same codex runtime, gpt-5.4 instead of gpt-5.5) and produces a byte-identical diff (blob `2a8dee9`, F1 0.473). It correctly replaced the contradictory `in_taxon NCBITaxon:6712 ! Astacidea` + `in_taxon NCBITaxon:6752 ! Brachyura` pair with a single `in_taxon NCBITaxon:6692` on all affected stomatogastric terms, then reserialized `uberon-edit.obo` with `robot convert`, incidentally reproducing much of the gold PR's serialization noise (xref normalization, tag reordering, whitespace trims, the `! unipolar brush cell` fill-in). The metadiff score under-represents the correctness of the core fix.

## Strengths

- Core taxon-constraint repair is ontologically correct and complete across all 15 affected terms (UBERON:8910001, UBERON:8910010–UBERON:8910023), matching the issue author's explicit Pleocyemata (NCBITaxon:6692) recommendation.
- Good methodology: PR comment documents reading `__issue_context__.json`, locating terms with `obo-grep.pl`, the checkout/checkin workflow, `robot convert` reserialization, and a sanity check that the parent `stomatogastric nervous system` (UBERON:8910000) remained scoped to Arthropoda — a thoughtful consistency observation.
- No spurious ontological edits; definitions/synonyms/is_a/part_of left correct.

## Issues

- **Omission (genuine, shared by all 8 attempts):** did not add `NCBITaxon:6692` to `ncbitaxon_terms.txt` or refresh `merged_import.owl`; gold explicitly imported Pleocyemata and its ancestors. Build/import is incomplete without it. Main real defect.
- **Style vs human:** `in_taxon NCBITaxon:6692` written without `! Pleocyemata` label comment (gold included it). Cosmetic; reserialization would normally re-add it.
- **Metadiff caveat:** precision (0.329) depressed by the absent ODK-regenerated `merged_import.owl` and reserialization-order differences, not by errors. F1 under-represents quality. See METADATA.md case-quality flag.
