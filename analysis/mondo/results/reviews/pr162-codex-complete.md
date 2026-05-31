---
ontology: mondo
issue_number: 9799
pr_number: 10114
eval_repo_pr: 162
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.727
precision: 0.615
recall: 0.889
jaccard: 0.571
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9799
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10114
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/162
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9799 --repo monarch-initiative/mondo
    gh pr diff 10114 --repo monarch-initiative/mondo
    gh pr diff 162 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10114 addressed `other` for issue #9799: [Obsolete]MONDO:0023124 familial pulmonary
arterial hypertension leucopenia and atrial septal defect. Human resolution summary: The PR
relabeled MONDO:0023124 from the long descriptive name to "Dursun syndrome" and added associated
metadata. The 9 additions include the new label, synonyms preserving the original name, and
OMIM-sourced annotations. The 4 deletions remove the old label and outdated annotations. This
approach preserves the term ID while improving its naming. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.727 (precision=0.615, recall=0.889). It matched 4/9
accepted additions and 4/4 accepted deletions.

## Strengths

- Matched 8 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: Dursun syndrome`
- Matched accepted addition: `synonym: "familial pulmonary arterial hypertension leucopenia and atrial septal defect" EXACT [OMIM:612541]`
- Matched accepted addition: `xref: OMIM:612541 {source="MONDO:includedEntryInOMIM"}`
- Matched accepted addition: `xref: Orphanet:178503 {source="MONDO:equivalentObsolete"}`
- Matched accepted deletion: `name: familial pulmonary arterial hypertension leucopenia and atrial septal defect`
- Matched accepted deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical disease and there is currently no evidence that this term ...`
- Matched accepted deletion: `subset: obsoletion_candidate`
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 5 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "A syndromic disease caused by mutation in the G6PC3 gene, characterized by familial pulmonary arterial hypertension, leukopenia, and atrial s...`
- Missing accepted addition: `synonym: "familial pulmonary arterial hypertension, leucopenia, and atrial septal defect" EXACT [OMIM:612541]`
- Missing accepted addition: `intersection_of: MONDO:0002254 ! syndromic disease`
- Missing accepted addition: `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/24861 ! G6PC3`
- Missing accepted addition: `relationship: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/24861 {source="OMIM:612541", source="PMID:20799326"} ! G6PC3`
- Extra changes beyond the accepted PR: 0 additions and 1 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent deletion: `property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/10455/familial-pulmonary-arterial-hypertension-leucopenia-and-atrial-septal-def...`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
