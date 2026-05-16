---
ontology: mondo
issue_number: 9799
pr_number: 10114
eval_repo_pr: 443
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.519
precision: 0.538
recall: 0.5
jaccard: 0.35
outcome: partial_success
failure_modes: [under_editing, missed_requirement, over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9799
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10114
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/443
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9799 --repo monarch-initiative/mondo
    gh pr diff 10114 --repo monarch-initiative/mondo
    gh pr diff 443 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10114 addressed `other` for issue #9799: [Obsolete]MONDO:0023124 familial pulmonary
arterial hypertension leucopenia and atrial septal defect. Human resolution summary: The PR
relabeled MONDO:0023124 from the long descriptive name to "Dursun syndrome" and added associated
metadata. The 9 additions include the new label, synonyms preserving the original name, and
OMIM-sourced annotations. The 4 deletions remove the old label and outdated annotations. This
approach preserves the term ID while improving its naming. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.519 (precision=0.538, recall=0.5). It matched 3/9
accepted additions and 4/4 accepted deletions.

## Strengths

- Matched 7 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: Dursun syndrome`
- Matched accepted addition: `xref: OMIM:612541 {source="MONDO:includedEntryInOMIM"}`
- Matched accepted addition: `xref: Orphanet:178503 {source="MONDO:equivalentObsolete"}`
- Matched accepted deletion: `name: familial pulmonary arterial hypertension leucopenia and atrial septal defect`
- Matched accepted deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical disease and there is currently no evidence that this term ...`
- Matched accepted deletion: `subset: obsoletion_candidate`

## Issues

- Missing accepted changes: 6 additions and 0 deletions from the human PR were not reproduced.
- Missing accepted addition: `def: "A syndromic disease caused by mutation in the G6PC3 gene, characterized by familial pulmonary arterial hypertension, leukopenia, and atrial s...`
- Missing accepted addition: `synonym: "familial pulmonary arterial hypertension leucopenia and atrial septal defect" EXACT [OMIM:612541]`
- Missing accepted addition: `synonym: "familial pulmonary arterial hypertension, leucopenia, and atrial septal defect" EXACT [OMIM:612541]`
- Missing accepted addition: `intersection_of: MONDO:0002254 ! syndromic disease`
- Missing accepted addition: `intersection_of: has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/24861 ! G6PC3`
- Extra changes beyond the accepted PR: 3 additions and 4 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `def: "A severe phenotype within the spectrum of severe congenital neutropenia type 4 (SCN4) caused by homozygous mutation in the G6PC3 gene, charac...`
- Extra agent addition: `synonym: "familial pulmonary arterial hypertension leucopenia and atrial septal defect" EXACT [GARD:0010455]`
- Extra agent addition: `is_a: MONDO:0012930 {source="OMIM:612541", source="https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Expert=178503"} ! autosomal recessive severe con...`
- Extra agent deletion: `synonym: "Dursun syndrome" RELATED []`
- Extra agent deletion: `synonym: "pulmonary arterial hypertension, leukopenia, and atrial septal defect" RELATED []`
- Extra agent deletion: `is_a: MONDO:0002254 {source="https://orcid.org/0000-0002-6601-2165"} ! syndromic disease`
- Extra agent deletion: `property_value: seeAlso "https://rarediseases.info.nih.gov/diseases/10455/familial-pulmonary-arterial-hypertension-leucopenia-and-atrial-septal-def...`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
