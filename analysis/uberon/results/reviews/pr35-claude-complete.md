---
ontology: uberon
issue_number: 3454
pr_number: 3455
eval_repo_pr: 35
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

Functionally identical to pr53 (same opencode runtime / gpt-5.5), producing a byte-identical diff (blob `125b85b`, F1 0.468). It correctly replaced the contradictory Astacidea + Brachyura `in_taxon` pair with a single `in_taxon NCBITaxon:6692` (Pleocyemata) on all affected stomatogastric terms, reserialized `uberon-edit.obo`, and added a `term_tracker_item` provenance property to every edited term. The PR comment additionally reports running ELK reasoning validation (`robot reason --reasoner ELK`) successfully. The metadiff score under-represents the core fix's correctness.

## Strengths

- Core taxon-constraint repair correct and complete across all 15 affected terms; correctly grounded in the issue's explicit Pleocyemata (NCBITaxon:6692) recommendation, with NCBI Taxonomy/BioRegistry verification documented.
- Best-documented methodology of the codex/opencode group: includes an explicit ELK reasoning pass to confirm the edit does not introduce an inconsistency — directly the right validation for a taxon-constraint repair.
- Reserialized per SOP; legitimate overlap with gold's reserialization hunks (recall 0.812). No spurious ontological edits to definitions/synonyms/hierarchy.

## Issues

- **Scope addition:** `term_tracker_item` provenance added to every edited stanza — defensible OBO convention, not requested by the issue, not in gold. Minor precision cost; scope-discipline note, not an error.
- **Omission (genuine, shared by all 8 attempts):** did not add `NCBITaxon:6692` to `ncbitaxon_terms.txt` or refresh `merged_import.owl`. Gold explicitly imported Pleocyemata + ancestors; import/build incomplete without it.
- **Style vs human:** `in_taxon NCBITaxon:6692` without `! Pleocyemata` label comment. Cosmetic.
- **Metadiff caveat:** precision depressed by the absent ODK-regenerated `merged_import.owl`, reserialization-order differences, and the extra `term_tracker_item` lines — not by wrong edits. F1 under-represents quality. See METADATA.md case-quality flag.
