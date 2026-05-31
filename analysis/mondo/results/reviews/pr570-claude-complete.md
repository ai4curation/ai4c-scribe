---
ontology: mondo
issue_number: 9933
pr_number: 10210
eval_repo_pr: 570
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.667
precision: 0.75
recall: 0.6
jaccard: 0.5
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-17"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9933
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10210
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/570
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

This is the strongest of the 11 attempts on issue #9933 (associate GINS3 with Meier-Gorlin
syndrome). The agent correctly identified MONDO:0980992 and built out the full
`disease_series_by_gene` model: gene-pattern definition, the asserted
`has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`
relationship, both `intersection_of` equivalence axioms, the `GINS3 Meier-Gorlin syndrome`
exact synonym, `MGORS9` abbreviation, and the issue-tracker `property_value`. F1=0.667
under-represents quality: it fully resolves the curator's actual ask (ValWood needed the
GINS3↔Meier-Gorlin link discoverable for PomBase) and matches the gold substance; the gap
is mostly synonym-source convention and one extra defensible axiom (see METADATA
`case_quality: ok`, `scoring_caveat`).

## Strengths

- Correct term selection (MONDO:0980992) and correct gene IRI (HGNC:25851), verified
  against NCBI Gene / HGNC per the PR comment.
- Reproduced the gold logical model verbatim in substance: both
  `intersection_of: MONDO:0016817` and
  `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`,
  plus the sourced `relationship:` line — this is what makes the term a proper
  logically-defined disease-by-gene class and what makes GINS3 surface for PomBase.
- Definition follows the `disease_series_by_gene` pattern wording exactly, with the
  expected `[MONDO:patterns/disease_series_by_gene, OMIM:621512, PMID:38773883]` xrefs.
- Added `MGORS9` EXACT ABBREVIATION and the `GINS3 Meier-Gorlin syndrome` exact synonym
  (the specific synonym the curator committed to in the issue thread).
- Ran ODK `make NORM` (not just `robot convert`), the correct Mondo normalization step;
  most opencode peers skipped this for lack of docker.

## Issues

- Synonym sourcing diverges from gold: the `GINS3 Meier-Gorlin syndrome` synonym is
  sourced `[MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]` rather than the
  gold's `[https://orcid.org/0000-0001-6330-7526, PMID:38773883]`. Substantively present
  but loses the curator ORCID and PMID provenance. This is the main metadiff penalty and
  is a convention difference, not an error.
- Did not add the gold's `synonym: "Meier-Gorlin syndrome 9" EXACT [DOID:0051069, OMIM:621512]`
  (label-as-synonym with cross-DB sourcing). Minor omission.
- Over-editing: two invented synonyms not in gold
  (`Meier-Gorlin syndrome caused by mutation in GINS3`, `Meier-Gorlin syndrome type 9`)
  and an extra `relationship: has_characteristic HP:0000007 ! Autosomal recessive inheritance`.
  The inheritance relationship is biologically defensible for MGORS9 but was not requested
  and is the only material scope concern.
