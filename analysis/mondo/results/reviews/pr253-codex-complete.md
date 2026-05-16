---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 253
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.398
precision: 0.854
recall: 0.259
jaccard: 0.248
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9795
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10110
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/253
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9795 --repo monarch-initiative/mondo
    gh pr diff 10110 --repo monarch-initiative/mondo
    gh pr diff 253 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10110 addressed `obsoletion` for issue #9795: [Obsolete] OMIM merges. Human resolution
summary: Merged Usher syndrome type 1J into MONDO:0012273 by obsoleting the Usher term and
transferring its cross-references and annotations to the surviving hearing loss term. The 14
additions and 28 deletions reflect that more content was removed (obsoleted stanza) than added
(transferred annotations plus obsoletion metadata). This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.398 (precision=0.854, recall=0.259). It matched 10/14
accepted additions and 24/28 accepted deletions.

## Strengths

- Matched 34 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `xref: DOID:0110836 {source="MONDO:equivalentObsolete"}`
- Matched accepted addition: `xref: GARD:0015863 {source="MONDO:GARD"}`
- Matched accepted addition: `xref: MEDGEN:766858 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}`
- Matched accepted addition: `xref: OMIM:614869 {source="MONDO:equivalentObsolete", source="DOID:0110836"}`
- Matched accepted deletion: `name: Usher syndrome type 1J`
- Matched accepted deletion: `def: "Any Usher syndrome in which the cause of the disease is a mutation in the CIB2 gene." [MONDO:patterns/disease_series_by_gene]`
- Matched accepted deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical diseaseAfter obsoletion, this term will not have a replace...`
- High precision indicates the agent mostly edited within the accepted change surface.

## Issues

- Missing accepted changes: 4 additions and 4 deletions from the human PR were not reproduced.
- Missing accepted addition: `synonym: "USH1J" EXACT ABBREVIATION [OMIM:609439]`
- Missing accepted addition: `synonym: "Usher syndrome type 1J" EXACT [OMIM:609439]`
- Missing accepted addition: `xref: MEDGEN:332149 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MONDO:preferredExternal"}`
- Missing accepted addition: `xref: UMLS:C1836199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:332149", source="MONDO:preferredExternal"}`
- Missing accepted deletion: `synonym: "autosomal recessive deafness 48" NARROW []`
- Missing accepted deletion: `synonym: "autosomal recessive nonsyndromic deafness 48" NARROW []`
- Missing accepted deletion: `xref: MEDGEN:332149 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}`
- Missing accepted deletion: `xref: UMLS:C1836199 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:332149"}`
- Extra changes beyond the accepted PR: 65 additions and 58 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `synonym: "cramps, familial adolescent" EXACT [OMIM:218050]`
- Extra agent addition: `xref: MEDGEN:347475 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}`
- Extra agent addition: `xref: OMIM:218050 {source="MONDO:equivalentObsolete"}`
- Extra agent addition: `xref: UMLS:C1857533 {source="MEDGEN:347475", source="MONDO:equivalentTo", source="MONDO:MEDGEN"}`
- Extra agent addition: `is_a: MONDO:0003847 {source="OMIM:123320/inferred", source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease`
- Extra agent deletion: `is_a: MONDO:0003847 {source="OMIM:123320/inferred"} ! hereditary disease`
- Extra agent deletion: `name: cramps, familial adolescent`
- Extra agent deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical diseaseAfter obsoletion, this term will not have a replace...`
- Extra agent deletion: `synonym: "cramps, familial adolescent" EXACT []`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
