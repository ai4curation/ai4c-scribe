---
ontology: mondo
issue_number: 9933
pr_number: 10210
eval_repo_pr: 707
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.429
precision: 0.375
recall: 0.5
jaccard: 0.273
outcome: success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9933
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10210
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/707
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

This attempt is a byte-identical replay of attempt #758 (same agent gpt-5.4/opencode,
same blob `5a63382`, same F1=0.429/P=0.375/R=0.5). The agent correctly identified
MONDO:0980992 and produced the full `disease_series_by_gene` model: pattern definition,
both `intersection_of` equivalence axioms, the sourced
`has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`
relationship, the `GINS3 Meier-Gorlin syndrome` exact synonym, and the issue-tracker
`property_value`. F1 under-represents quality; the core logical model matches gold and
the curator's actual ask is fully resolved (see METADATA `case_quality: ok`,
`scoring_caveat`).

## Strengths

- Correct term (MONDO:0980992) and gene IRI (HGNC:25851).
- Reproduced gold's logical definition exactly: both `intersection_of` lines plus the
  sourced `relationship: has_material_basis_in_germline_mutation_in` — the substantive
  core that makes GINS3 discoverable for Meier-Gorlin syndrome (the PomBase concern in
  the issue thread).
- Definition follows the `disease_series_by_gene` pattern wording and xrefs precisely.
- Added exactly the curator-requested `GINS3 Meier-Gorlin syndrome` exact synonym with
  no invented synonyms — good scope discipline.
- Consulted the dosdp pattern file; sound methodology for this task type. Deterministic
  reproducibility vs #758 is itself a positive signal.

## Issues

- Synonym sourcing diverges from gold (`[PMID:38773883, MONDO:patterns/disease_series_by_gene]`
  vs gold's ORCID+PMID) — provenance convention, not a substantive error.
- Under-editing vs gold's pattern-enrichment synonym set: missing
  `synonym: "Meier-Gorlin syndrome 9" EXACT [DOID:0051069, OMIM:621512]` and
  `synonym: "MGORS9" EXACT ABBREVIATION [OMIM:621512]`. The issue did not explicitly
  request these; their absence is the main, largely cosmetic, metadiff loss.
- ODK `make NORM` not run (docker unavailable); only `robot convert` syntax check.
  Normalization should be curator-verified before merge.
