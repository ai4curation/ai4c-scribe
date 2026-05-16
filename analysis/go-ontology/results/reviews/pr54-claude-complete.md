---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 54
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.800
precision: 0.889
recall: 0.727
jaccard: 0.667
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

gpt-5.5 / codex re-run producing the identical diff blob (`29a680f`) to attempt #66. Correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups, with strong reference-validation methodology. F1=0.800 understates quality slightly. Reviewed in parallel with #66.

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- Same well-formed obsoletion comment as #66 (accurate over-specificity rationale + replacement pointer).
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment removed — justified hygiene.
- Methodology: pre/post `make travis_build` passing, `linkml-reference-validator` on PMID:12517450 and PMID:11717276 (with a documented EPA-HERO fallback when NCBI returned HTTP 429), RESEARCH.md created. Good resilience under tooling failure.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in human PR → recall 0.727. Defensible curation.
- Comment omits the explicit EC 1.11.1.26 citation present in the human comment. Stylistic.
- Reproducibility duplicate of #66; no additional signal.
