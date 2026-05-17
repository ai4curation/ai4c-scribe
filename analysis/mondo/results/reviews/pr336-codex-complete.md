---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 336
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.343
precision: 0.415
recall: 0.293
jaccard: 0.207
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9795
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10110
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/336
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9795 --repo monarch-initiative/mondo
    gh pr diff 10110 --repo monarch-initiative/mondo
    gh pr diff 336 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10110 addressed `obsoletion` for issue #9795: [Obsolete] OMIM merges. Human resolution
summary: Merged Usher syndrome type 1J into MONDO:0012273 by obsoleting the Usher term and
transferring its cross-references and annotations to the surviving hearing loss term. The 14
additions and 28 deletions reflect that more content was removed (obsoleted stanza) than added
(transferred annotations plus obsoletion metadata). This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.343 (precision=0.415, recall=0.293). It matched 4/14
accepted additions and 13/28 accepted deletions.

## Strengths

- Matched 17 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: obsolete Usher syndrome type 1J`
- Matched accepted addition: `property_value: IAO:0000231 MONDO:TermsMerged`
- Matched accepted addition: `is_obsolete: true`
- Matched accepted addition: `replaced_by: MONDO:0012273`
- Matched accepted deletion: `name: Usher syndrome type 1J`
- Matched accepted deletion: `def: "Any Usher syndrome in which the cause of the disease is a mutation in the CIB2 gene." [MONDO:patterns/disease_series_by_gene]`
- Matched accepted deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical diseaseAfter obsoletion, this term will not have a replace...`

## Issues

- Missing accepted changes: 10 additions and 15 deletions from the human PR were not reproduced.
- Missing accepted addition: `synonym: "USH1J" EXACT ABBREVIATION [OMIM:609439]`
- Missing accepted addition: `synonym: "Usher syndrome type 1J" EXACT [OMIM:609439]`
- Missing accepted addition: `xref: DOID:0110836 {source="MONDO:equivalentObsolete"}`
- Missing accepted addition: `xref: GARD:0015863 {source="MONDO:GARD"}`
- Missing accepted addition: `xref: MEDGEN:332149 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MONDO:preferredExternal"}`
- Missing accepted deletion: `synonym: "autosomal recessive deafness 48" NARROW []`
- Missing accepted deletion: `synonym: "autosomal recessive nonsyndromic deafness 48" NARROW []`
- Missing accepted deletion: `xref: MEDGEN:332149 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}`
- Missing accepted deletion: `xref: UMLS:C1836199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:332149"}`
- Extra changes beyond the accepted PR: 25 additions and 29 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `name: obsolete cramps, familial adolescent`
- Extra agent addition: `xref: MEDGEN:347475 {source="MONDO:obsoleteEquivalent", source="MONDO:MEDGEN"}`
- Extra agent addition: `xref: UMLS:C1857533 {source="MEDGEN:347475", source="MONDO:obsoleteEquivalent", source="MONDO:MEDGEN"}`
- Extra agent addition: `property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3`
- Extra agent addition: `replaced_by: MONDO:0007402`
- Extra agent deletion: `name: cramps, familial adolescent`
- Extra agent deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical diseaseAfter obsoletion, this term will not have a replace...`
- Extra agent deletion: `xref: MEDGEN:347475 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}`
- Extra agent deletion: `xref: UMLS:C1857533 {source="MEDGEN:347475", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
