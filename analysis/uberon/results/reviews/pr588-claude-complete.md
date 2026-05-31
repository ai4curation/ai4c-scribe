---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 588
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
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
reviewed_at: 2026-05-17
---

## Summary

The agent performed the correct substantive repair the issue demanded: across all
affected stomatogastric terms (UBERON:8910001 and the UBERON:8910010-series) it replaced
the contradictory `relationship: in_taxon NCBITaxon:6712 ! Astacidea` + `relationship:
in_taxon NCBITaxon:6752 ! Brachyura` pair with a single `relationship: in_taxon
NCBITaxon:6692` (Pleocyemata), exactly the closest-common-ancestor consolidation the
issue author specified. It then ran `robot convert` to reserialize `uberon-edit.obo`,
which incidentally reproduced much of gold's whole-file serialization noise (xref
normalization e.g. `PMID: 17009928` → `PMID:17009928`, xref/synonym/relationship
reordering, trailing-whitespace trims, the `! unipolar brush cell` label fill-in on
CL:4023161). The blob (`2a8dee9`) is byte-identical to PR647 and the codex/gpt-5.x
attempts. F1=0.473 substantially under-represents the quality of the core fix; the real
defect is the missing import update.

## Strengths

- Core taxon-constraint repair is ontologically correct and complete across all ~15
  affected terms — matches the issue author's explicit instruction to collapse the two
  sibling-taxon `in_taxon` assertions to their common parent Pleocyemata
  (NCBITaxon:6692). Correctly chose `in_taxon` (RO:0002162), not the issue's
  alternative `present_in_taxon`, which is the right call given the author's guidance.
- High recall (0.839): the SOP-mandated `robot convert` reserialization legitimately
  overlaps the gold PR's reserialization-derived hunks, so most of the non-substantive
  gold lines were reproduced faithfully.
- No spurious ontological edits: definitions, `is_a`, `part_of`, `overlaps`, and
  contributor metadata are preserved on the substantive change; differences are
  serialization-order only.

## Issues

- **Omission (genuine, shared by all 8 substantive attempts):** did not add
  `NCBITaxon:6692` to `src/ontology/imports/ncbitaxon_terms.txt` nor refresh
  `src/ontology/imports/merged_import.owl`. Gold imported Pleocyemata (plus ancestors
  Eucarida/Decapoda/Eumalacostraca) because the term is now referenced; without it the
  build/import is incomplete. This is the main real defect — a true `missed_requirement`.
- **Style vs human:** used `relationship: in_taxon NCBITaxon:6692` without the trailing
  `! Pleocyemata` label comment gold used. Both are valid OBO; a subsequent build would
  re-add the label, so this is cosmetic.
- **Metadiff caveat:** precision (0.329) is depressed mainly by the absent
  ODK-regenerated `merged_import.owl` (~42 gold lines) and minor reserialization-order
  differences, not by wrong edits. F1 under-represents quality on this `case_quality:
  poor` case — see METADATA.md.
