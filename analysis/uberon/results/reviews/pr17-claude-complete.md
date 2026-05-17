---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 17
agent: codex_gpt-5.5
model: gpt-5.5
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

The agent correctly performed the substantive ontological fix the issue demanded: on all affected stomatogastric terms (UBERON:8910001, UBERON:8910010–UBERON:8910023) it replaced the contradictory `relationship: in_taxon NCBITaxon:6712 ! Astacidea` + `relationship: in_taxon NCBITaxon:6752 ! Brachyura` pair with a single `relationship: in_taxon NCBITaxon:6692` (Pleocyemata), exactly as the issue author specified. It then ran `robot convert` to reserialize `uberon-edit.obo`, which incidentally reproduced much of the gold PR's whole-file serialization noise (xref normalization such as `PMID: 17009928` → `PMID:17009928`, tag reordering, trailing-whitespace trims, the `! unipolar brush cell` comment fill-in). The metadiff F1 of 0.473 substantially under-represents the quality of the core fix; the headline gap is that the agent did not add NCBITaxon:6692 to the import files.

## Strengths

- Core taxon-constraint repair is ontologically correct and complete across all 15 affected terms; matches the issue author's explicit instruction to collapse the two sibling-taxon `in_taxon` assertions to their common parent Pleocyemata (NCBITaxon:6692).
- Correctly identified Pleocyemata as the closest common parent of Astacidea and Brachyura (verified against NCBI taxonomy in the agent's checklist).
- Used the project's `obo-grep.pl` / `obo-checkout.pl` / `obo-checkin.pl` workflow and reserialized with `robot convert` as the SOP requires — good methodology and the reason recall is high (0.839): the reserialization legitimately overlaps the gold's reserialization-derived hunks.
- Left definitions, synonyms, `is_a`, `part_of`, `overlaps`, and contributor metadata untouched on the substantive edit; no spurious ontological changes.

## Issues

- **Omission (genuine, shared by all 8 attempts):** did not add `NCBITaxon:6692` to `src/ontology/imports/ncbitaxon_terms.txt` nor refresh `src/ontology/imports/merged_import.owl`. The gold PR explicitly imported Pleocyemata (plus ancestors Eucarida/Decapoda/Eumalacostraca) because the term is now referenced; without it the import/build is incomplete. This is the main real defect.
- **Style vs human:** used `relationship: in_taxon NCBITaxon:6692` without the trailing `! Pleocyemata` label comment that gold used. Both are valid OBO; `robot convert` would normally re-add the label on the next build, so this is cosmetic.
- **Metadiff caveat:** precision (0.329) is depressed mainly by the absent ODK-regenerated `merged_import.owl` (42 lines of gold) and minor reserialization-order differences, not by wrong edits. F1 under-represents quality. See case-quality flag in METADATA.md.
