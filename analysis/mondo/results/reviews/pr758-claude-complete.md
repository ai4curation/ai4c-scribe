---
ontology: mondo
issue_number: 9933
pr_number: 10210
eval_repo_pr: 758
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/758
  Agent config: ai4curation/mondo-agent-config
-->

## Summary

The agent correctly identified MONDO:0980992 and produced a clean, well-scoped
`disease_series_by_gene` model for the GINS3-Meier-Gorlin association: pattern-form
definition, both `intersection_of` equivalence axioms, the asserted sourced
`has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`
relationship, the `GINS3 Meier-Gorlin syndrome` exact synonym, and the issue-tracker
`property_value`. F1=0.429 substantially under-represents quality — the core gene-disease
logical model matches gold exactly, and ValWood's actual ask (make GINS3↔Meier-Gorlin
discoverable) is fully resolved. The metadiff penalty is mostly missing gold's extra
synonym set and a synonym-source convention difference (see METADATA `case_quality: ok`,
`scoring_caveat`). Diff is byte-identical to attempt #707 (blob `5a63382`).

## Strengths

- Correct term (MONDO:0980992) and correct gene IRI (HGNC:25851); confirmed against
  PubMed PMID:38773883 and the `disease_series_by_gene` pattern per the PR comment.
- Reproduced the gold logical definition exactly: both
  `intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome` and
  `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`,
  plus the sourced `relationship:` — the substantive heart of the gold PR and the part
  that produces the PomBase-visible gene association.
- Definition uses the exact `disease_series_by_gene` pattern wording and xrefs
  (`[MONDO:patterns/disease_series_by_gene, OMIM:621512, PMID:38773883]`).
- Added exactly the `GINS3 Meier-Gorlin syndrome` exact synonym the curator committed to
  in the issue thread; no invented synonyms (good scope discipline relative to #570).
- Consulted `src/patterns/dosdp-patterns/disease_series_by_gene.yaml` — correct
  methodology for this Mondo task type.

## Issues

- Synonym sourcing diverges from gold: `[PMID:38773883, MONDO:patterns/disease_series_by_gene]`
  instead of gold's `[https://orcid.org/0000-0001-6330-7526, PMID:38773883]`. Loses the
  curator ORCID; a provenance-convention difference, not a substantive error.
- Under-editing relative to gold's full synonym set: did not add
  `synonym: "Meier-Gorlin syndrome 9" EXACT [DOID:0051069, OMIM:621512]` or
  `synonym: "MGORS9" EXACT ABBREVIATION [OMIM:621512]`. These are pattern-enrichment
  additions the issue did not explicitly request; their absence is the main (largely
  cosmetic) metadiff loss.
- ODK `make NORM` not run (docker unavailable in the environment); only `robot convert`
  syntax check performed. The output is still well-formed, but normalization should be
  verified by a curator before merge.
