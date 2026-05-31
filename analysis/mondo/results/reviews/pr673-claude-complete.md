---
ontology: mondo
issue_number: 9933
pr_number: 10210
eval_repo_pr: 673
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/673
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

This attempt is a byte-identical replay of attempt #725 (same agent gpt-5.5/opencode,
same blob `23581f9`, same F1=0.167/P=0.125/R=0.25). The agent correctly identified
MONDO:0980992 and added the curator-requested `GINS3 Meier-Gorlin syndrome` exact synonym,
the asserted `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`
relationship, and the issue-tracker `property_value` — satisfying ValWood's literal ask.
But it OMITS both `intersection_of` equivalence axioms and uses non-pattern definition
wording, leaving the term without a proper logical disease-by-gene definition. The low F1
reflects both metadiff convention penalty and a genuine substantive gap.

## Strengths

- Correct term (MONDO:0980992) and correct gene IRI (HGNC:25851).
- Added the curator's committed `GINS3 Meier-Gorlin syndrome` exact synonym and the
  sourced asserted `relationship: has_material_basis_in_germline_mutation_in` to GINS3 —
  the minimal change needed to make the association discoverable for PomBase.
- Matched gold's `property_value: IAO:0000233 ".../issues/9933"` issue-tracker annotation.
- Tight, single-file scope with no invented synonyms or gratuitous edits.

## Issues

- Missed requirement (substantive): omits BOTH gold equivalence axioms
  `intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome` and
  `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`.
  The term ends up as an asserted subclass with a loose relationship, not a
  logically-defined `disease_series_by_gene` class — the gpt-5.4 peers and codex #570 all
  produced the equivalence axioms. This is the decisive quality gap for the gpt-5.5 runs.
- Definition uses non-pattern free text
  ("caused by homozygous or compound heterozygous mutation in the GINS3 gene")
  rather than the standardized `disease_series_by_gene` wording; needs curator rewording.
- Under-editing vs gold synonym set: missing `MGORS9` ABBREVIATION and the
  `Meier-Gorlin syndrome 9` label-synonym; GINS3 synonym sourced PMID-only (loses curator
  ORCID provenance).
- Determinism with #725 is a positive process signal, but the shared gap means the
  failure is reproducible rather than incidental.
