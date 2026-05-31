---
ontology: mondo
issue_number: 9933
pr_number: 10210
eval_repo_pr: 274
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.526
precision: 0.625
recall: 0.455
jaccard: 0.357
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9933
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10210
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/274
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9933 --repo monarch-initiative/mondo
    gh pr diff 10210 --repo monarch-initiative/mondo
    gh pr diff 274 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10210 addressed `synonym_update` for issue #9933: GINS3 Meier-Gorlin syndrome. Human
resolution summary: The PR added 8 lines of synonym annotations to MONDO:0980992 in mondo-edit.obo.
These additions likely include gene-centric synonyms (e.g., "GINS3-related Meier-Gorlin syndrome")
and potentially alternate disease names referenced in the literature, each with appropriate synonym
scope and evidence annotations. This attempt changed `src/ontology/mondo-edit.obo` and scored
F1=0.526 (precision=0.625, recall=0.455). It matched 5/8 accepted additions and 0/0 accepted
deletions.

## Strengths

- Matched 5 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `synonym: "Meier-Gorlin syndrome 9" EXACT [DOID:0051069, OMIM:621512]`
- Matched accepted addition: `synonym: "MGORS9" EXACT ABBREVIATION [OMIM:621512]`
- Matched accepted addition: `intersection_of: MONDO:0016817 ! Meier-Gorlin syndrome`
- Matched accepted addition: `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851`

## Issues

- Missing accepted changes: 3 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene." [MONDO:patterns/disease_series_by_gene, OMIM:62...`
- Missing accepted addition: `synonym: "GINS3 Meier-Gorlin syndrome" EXACT [https://orcid.org/0000-0001-6330-7526, PMID:38773883]`
- Missing accepted addition: `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/25851 {source="OMIM:621512", source="PMID:38773883"}`
- Extra changes beyond the accepted PR: 6 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `def: "Any Meier-Gorlin syndrome in which the cause of the disease is a mutation in the GINS3 gene." [MONDO:patterns/disease_series_by_gene]`
- Extra agent addition: `synonym: "GINS3 Meier-Gorlin syndrome" EXACT [MONDO:design_pattern, MONDO:patterns/disease_series_by_gene]`
- Extra agent addition: `synonym: "Meier-Gorlin syndrome caused by mutation in GINS3" EXACT [MONDO:design_pattern]`
- Extra agent addition: `synonym: "Meier-Gorlin syndrome type 9" EXACT []`
- Extra agent addition: `relationship: has_characteristic HP:0000007 {source="MONDO:HPOA", source="OMIM:621512"} ! Autosomal recessive inheritance`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
