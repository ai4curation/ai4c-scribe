---
ontology: mondo
issue_number: 9933
pr_number: 10210
eval_repo_pr: 725
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.167
precision: 0.125
recall: 0.25
jaccard: 0.091
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9933
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10210
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/725
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

The agent correctly identified MONDO:0980992 and added the curator-requested
`GINS3 Meier-Gorlin syndrome` exact synonym plus an asserted
`has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`
relationship and the issue-tracker `property_value`. This satisfies ValWood's literal
ask (a discoverable GINS3↔Meier-Gorlin association). However it is materially weaker than
the gpt-5.4 attempts: it OMITS both `intersection_of` equivalence axioms, so the term is
not a logically-defined disease-by-gene class, and the definition uses non-pattern
wording. F1=0.167 partly reflects metadiff convention penalties but here also a real
substantive gap. Diff is byte-identical to attempt #673 (blob `23581f9`).

## Strengths

- Correct term selection (MONDO:0980992) and correct gene IRI (HGNC:25851), verified
  against the HGNC REST endpoint and PubMed PMID:38773883 per the PR comment.
- Added the specific `synonym: "GINS3 Meier-Gorlin syndrome" EXACT` the curator committed
  to in the issue thread, and the asserted sourced
  `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="OMIM:621512", source="PMID:38773883"}`
  — this is what makes the gene association queryable for PomBase, the issue's core need.
- Added the `property_value: IAO:0000233 ".../issues/9933"` issue-tracker annotation
  matching gold.
- Tight scope: one file, no invented synonyms, no gratuitous edits.

## Issues

- Missed requirement (substantive, not cosmetic): omits BOTH gold equivalence axioms
  `intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome` and
  `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`.
  Without the logical definition the term is only an asserted subclass with a loose
  relationship, not a proper `disease_series_by_gene` class — the gpt-5.4 peers (#758/#707)
  and codex #570 all got this right; this is the key quality differentiator.
- Definition diverges from the `disease_series_by_gene` pattern: free-text
  "caused by homozygous or compound heterozygous mutation in the GINS3 gene"
  `[OMIM:621512, PMID:38773883]` instead of the standardized
  "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene"
  `[MONDO:patterns/disease_series_by_gene, ...]`. Would need curator rewording.
- Under-editing vs gold's synonym set: missing `MGORS9` ABBREVIATION and the
  `Meier-Gorlin syndrome 9` label-synonym; and the GINS3 synonym is sourced PMID-only,
  losing the curator ORCID provenance.
- ODK `make NORM` not run (docker unavailable); only `robot convert` syntax check.
