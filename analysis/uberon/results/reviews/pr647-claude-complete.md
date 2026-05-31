---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 647
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

A re-run of the same gpt-5.4/opencode configuration as PR588 (identical blob `2a8dee9`,
same F1=0.473). The agent performed the correct substantive repair: across all affected
stomatogastric terms (UBERON:8910001 and the UBERON:8910010-series) it replaced the
contradictory `relationship: in_taxon NCBITaxon:6712 ! Astacidea` + `relationship:
in_taxon NCBITaxon:6752 ! Brachyura` pair with a single `relationship: in_taxon
NCBITaxon:6692` (Pleocyemata), then reserialized with `robot convert` (reproducing gold's
xref-normalization / line-reordering / whitespace-trim / CL:4023161 label-fill noise).
This run additionally produced an articulate PR comment correctly explaining that `in
taxon` is exclusory and that Pleocyemata is the correct common exclusive parent of
Astacidea and Brachyura — sound ontological reasoning matching the issue author's intent.
F1=0.473 substantially under-represents the core fix; the real defect is the missing
import update.

## Strengths

- Core taxon-constraint repair is ontologically correct and complete across all ~15
  affected terms — exactly the closest-common-ancestor (`in_taxon NCBITaxon:6692`,
  Pleocyemata) consolidation the issue author specified; correctly preferred `in_taxon`
  over the issue's `present_in_taxon` alternative.
- Strong, transparent methodology documented in the PR comment: read
  `__issue_context__.json`, used `obo-grep.pl` to locate terms, edited via the
  `obo-checkout.pl`/`obo-checkin.pl` workflow, reserialized with `robot convert`, and
  re-queried to verify the old NCBITaxon:6712/6752 assertions were gone — the SOP the
  config prescribes.
- High recall (0.839) from the legitimate reserialization overlap with gold; no spurious
  ontological edits beyond serialization-order normalization.

## Issues

- **Omission (genuine, shared by all 8 substantive attempts):** did not add
  `NCBITaxon:6692` to `src/ontology/imports/ncbitaxon_terms.txt` nor refresh
  `merged_import.owl`; the PR comment's "Committed only `src/ontology/uberon-edit.obo`"
  confirms the import-membership step was deliberately skipped. Gold imported Pleocyemata
  (and ancestors Eucarida/Decapoda/Eumalacostraca) because it is now referenced — without
  it the build is incomplete. This is the main real `missed_requirement`.
- **Style vs human:** `relationship: in_taxon NCBITaxon:6692` lacks the trailing
  `! Pleocyemata` label comment gold used; valid OBO, cosmetic, would be re-added on
  build.
- **Metadiff caveat:** precision (0.329) is depressed by the absent ODK-regenerated
  `merged_import.owl` and reserialization-order differences, not wrong edits. F1
  under-represents quality on this `case_quality: poor` case — see METADATA.md.
