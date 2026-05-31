---
ontology: mondo
issue_number: 9799
pr_number: 10114
eval_repo_pr: 115
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.483
precision: 0.538
recall: 0.438
jaccard: 0.318
outcome: partial_success
failure_modes: [over_editing, wrong_pattern, scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is a duplicate run of the same agent/config as pr134 (gpt-5.5/opencode) and produced a byte-identical diff (same blob `20f8590`); the PR-comment narrative differs slightly but the ontology change is the same. Assessment matches pr134: correct relabel and xrefs, but over-engineered with an extra `is_a: MONDO:0012930`, an incomplete G6PC3 logical pattern, an unrequested #5507 tracker, and extra synonyms. F1=0.483 (P=0.538, R=0.438) — roughly fair given the real over-editing.

## Strengths

- Correct relabel to `name: Dursun syndrome`; removed obsoletion `comment:`, `subset: obsoletion_candidate`, and `IAO:0006012`.
- Added `xref: OMIM:612541 {source="MONDO:includedEntryInOMIM"}` and `xref: Orphanet:178503 {source="MONDO:equivalentObsolete"}` correctly per the issue.
- Documented good verification (MedGen, PubMed, GeneReviews, OLS/ORDO API; `obo-checkout.pl`/`obo-checkin.pl`; `robot convert`). The G6PC3 biology is correct.

## Issues

- Same as pr134 (identical diff): incomplete logical pattern (`relationship: has_material_basis_in_germline_mutation_in HGNC:24861` with no `intersection_of` pair), redundant/unsupported `is_a: MONDO:0012930` added on top of the retained MONDO:0002254 (gold kept only MONDO:0002254), and an unrequested second `IAO:0000233` tracker to issue #5507.
- The PR comment claims `Orphanet:178503` was added as `MONDO:obsoleteEquivalent`, but the actual diff correctly uses `MONDO:equivalentObsolete` — the prose is internally inconsistent with the (correct) diff; minor but indicates loose self-reporting.
- Over-editing of synonyms relative to gold; removed the GARD `seeAlso` gold retained. `make NORM` could not run (no Docker; disclosed).
- Duplicate-run consistency with pr134 is a positive signal for determinism but does not change the substantive over-scoping verdict.
