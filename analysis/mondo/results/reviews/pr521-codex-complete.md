---
ontology: mondo
issue_number: 9956
pr_number: 10214
eval_repo_pr: 521
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.435
precision: 0.417
recall: 0.455
jaccard: 0.278
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9956
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10214
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/521
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9956 --repo monarch-initiative/mondo
    gh pr diff 10214 --repo monarch-initiative/mondo
    gh pr diff 521 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10214 addressed `new_term` for issue #9956: New Term Request/TSEN2-related
neurodevelopmental disorder with or without thrombotic microangiopathy. Human resolution summary:
Added new term MONDO:1060216 to `src/ontology/mondo-edit.obo`: - **ID**: MONDO:1060216 - **Name**:
TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy -
**Definition**: Comprehensive clinical description citing 8 PMIDs (PMID:18711368, PMID:20952379,
PMID:23562994, PMID:32404165, PMID:38347586, PMID:38438125, PMID:38622473) and ClinGen as source -
**Classification** (multi-parent): - i... This attempt changed `src/ontology/mondo-edit.obo` and
scored F1=0.435 (precision=0.417, recall=0.455). It matched 4/12 accepted additions and 0/0 accepted
deletions.

## Strengths

- Matched 4 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `[Term]`
- Matched accepted addition: `intersection_of: MONDO:0700092 ! neurodevelopmental disorder`
- Matched accepted addition: `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/28422 ! TSEN2`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9956" xsd:anyURI`

## Issues

- Missing accepted changes: 8 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `id: MONDO:1060216`
- Missing accepted addition: `name: TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy`
- Missing accepted addition: `def: "Any neurodevelopmental disorder in which the cause of the disease is a variation in the TSEN2 gene. This condition is associated with intelle...`
- Missing accepted addition: `synonym: "TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy" EXACT [https://clinicalgenome.org/affiliation/40069...`
- Missing accepted addition: `is_a: MONDO:0002254 {source="https://clinicalgenome.org/affiliation/40069/"} ! syndromic disease`
- Extra changes beyond the accepted PR: 7 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `id: MONDO:7770736`
- Extra agent addition: `name: TSEN2-related neurodevelopmental disorder`
- Extra agent addition: `def: "Any neurodevelopmental disorder in which the cause of the disease is a mutation in the TSEN2 gene. This condition is associated with intellec...`
- Extra agent addition: `synonym: "TSEN2-related neurodevelopmental disorder with or without thrombotic microangiopathy" EXACT [https://clinicalgenome.org/affiliation/40069/]`
- Extra agent addition: `is_a: MONDO:0700092 {source="PMID:38347586", source="PMID:38622473", source="https://clinicalgenome.org/affiliation/40069/"} ! neurodevelopmental d...`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
