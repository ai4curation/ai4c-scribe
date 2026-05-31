---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 28
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.765
precision: 0.765
recall: 0.765
jaccard: 0.619
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9771
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10102
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/28
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9771 --repo monarch-initiative/mondo
    gh pr diff 10102 --repo monarch-initiative/mondo
    gh pr diff 28 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10102 addressed `obsoletion` for issue #9771: [Obsolete] 'heart, malformation of'
(MONDO:0009327). Human resolution summary: Obsoleted MONDO:0009327 by marking it as obsolete,
removing its classification axioms, and adding appropriate replaced_by and consider annotations to
redirect users to more specific terms. The 9 additions and 10 deletions reflect the standard
obsoletion pattern: removing active axioms and adding obsoletion metadata. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.765 (precision=0.765, recall=0.765). It matched 5/9
accepted additions and 8/10 accepted deletions.

## Strengths

- Matched 13 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: obsolete heart, malformation of`
- Matched accepted addition: `xref: MEDGEN:6748 {source="MONDO:obsoleteEquivalent", source="MONDO:MEDGEN"}`
- Matched accepted addition: `xref: UMLS:C0018798 {source="MONDO:obsoleteEquivalent", source="MONDO:MEDGEN", source="MEDGEN:6748"}`
- Matched accepted addition: `is_obsolete: true`
- Matched accepted deletion: `name: heart, malformation of`
- Matched accepted deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical disease and there is currently no evidence that this term ...`
- Matched accepted deletion: `subset: obsoletion_candidate`

## Issues

- Missing accepted changes: 4 additions and 2 deletions from the human PR were not reproduced.
- Missing accepted addition: `comment: This term has been obsoleted based on the fact that it is a historical disease and there is currently no evidence that this term represent...`
- Missing accepted addition: `xref: OMIM:140500 {source="MONDO:obsoleteEquivalentObsolete"}`
- Missing accepted addition: `xref: OMIM:234750 {source="MONDO:obsoleteEquivalentObsolete"}`
- Missing accepted addition: `property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludeHistoricalDisease"}`
- Missing accepted deletion: `xref: OMIM:140500 {source="MONDO:equivalentObsolete"}`
- Missing accepted deletion: `xref: OMIM:234750 {source="MONDO:equivalentObsolete"}`
- Extra changes beyond the accepted PR: 3 additions and 1 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9771" xsd:anyURI`
- Extra agent addition: `comment: This term was obsoleted because it represents a phenotype or historical placeholder rather than a disease. See MONDO:0005267 for the broad...`
- Extra agent addition: `property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludeHistoricalDisease", source="MONDO:excludePhenotype"}`
- Extra agent deletion: `replaced_by: MONDO:0009327`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
