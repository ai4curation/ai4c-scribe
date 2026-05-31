---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 53
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.468
precision: 0.329
recall: 0.812
jaccard: 0.306
outcome: partial_success
failure_modes:
  - missed_requirement
  - scope_creep
case_quality: poor
case_quality_reason: gold_reserialization_and_odk_import_domination
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This pi/opencode-runtime attempt performed the correct core fix (replace the `in_taxon NCBITaxon:6712` + `in_taxon NCBITaxon:6752` pair with a single `in_taxon NCBITaxon:6692` on all affected stomatogastric terms) and reserialized `uberon-edit.obo`, reproducing much of the gold PR's serialization noise. It additionally added a `property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3454" xsd:anyURI` line to every edited term — a defensible provenance convention not requested by the issue and not present in gold (blob `125b85b`, F1 0.468). The metadiff score under-represents the core fix's correctness.

## Strengths

- Core taxon-constraint repair correct and complete across all 15 affected terms (UBERON:8910001, UBERON:8910010–UBERON:8910023); correctly grounded in the issue author's Pleocyemata (NCBITaxon:6692) recommendation.
- Strong rationale in PR comment correctly explaining `RO:0002162` (`in taxon`) semantics and why two sibling-taxon assertions are contradictory.
- Reserialized with `robot convert` per SOP; legitimate overlap with gold's reserialization hunks (recall 0.812).

## Issues

- **Scope addition:** added `term_tracker_item` provenance to every edited stanza. This is a recognized OBO convention for linking edits to tracker issues and is defensible, but the issue did not ask for it and gold did not do it. Slightly lowers precision and is a minor scope-discipline note rather than an error.
- **Omission (genuine, shared by all 8 attempts):** did not add `NCBITaxon:6692` to `ncbitaxon_terms.txt` or refresh `merged_import.owl`; gold explicitly imported Pleocyemata + ancestors. Build/import incomplete without it.
- **Style vs human:** `in_taxon NCBITaxon:6692` without `! Pleocyemata` label comment. Cosmetic.
- **Metadiff caveat:** precision depressed by absent ODK-regenerated `merged_import.owl` plus reserialization differences and the extra `term_tracker_item` lines. F1 under-represents the substantive quality. See METADATA.md case-quality flag.
