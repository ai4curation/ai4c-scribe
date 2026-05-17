---
ontology: mondo
issue_number: 9771
pr_number: 10102
eval_repo_pr: 19
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: simple
f1: 0.562
precision: 0.529
recall: 0.6
jaccard: 0.391
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/19
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9771 --repo monarch-initiative/mondo
    gh pr diff 10102 --repo monarch-initiative/mondo
    gh pr diff 19 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10102 addressed `obsoletion` for issue #9771: [Obsolete] 'heart, malformation of'
(MONDO:0009327). Human resolution summary: Obsoleted MONDO:0009327 by marking it as obsolete,
removing its classification axioms, and adding appropriate replaced_by and consider annotations to
redirect users to more specific terms. The 9 additions and 10 deletions reflect the standard
obsoletion pattern: removing active axioms and adding obsoletion metadata. This attempt changed
`src/ontology/mondo-edit.obo` and scored F1=0.562 (precision=0.529, recall=0.6). It matched 3/9
accepted additions and 6/10 accepted deletions.

## Strengths

- Matched 9 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: obsolete heart, malformation of`
- Matched accepted addition: `is_obsolete: true`
- Matched accepted addition: `consider: MONDO:0005267`
- Matched accepted deletion: `name: heart, malformation of`
- Matched accepted deletion: `comment: This term is scheduled for obsoletion based on the fact that it is a historical disease and there is currently no evidence that this term ...`
- Matched accepted deletion: `subset: obsoletion_candidate`

## Issues

- Missing accepted changes: 6 additions and 4 deletions from the human PR were not reproduced.
- Missing accepted addition: `comment: This term has been obsoleted based on the fact that it is a historical disease and there is currently no evidence that this term represent...`
- Missing accepted addition: `xref: MEDGEN:6748 {source="MONDO:obsoleteEquivalent", source="MONDO:MEDGEN"}`
- Missing accepted addition: `xref: OMIM:140500 {source="MONDO:obsoleteEquivalentObsolete"}`
- Missing accepted addition: `xref: OMIM:234750 {source="MONDO:obsoleteEquivalentObsolete"}`
- Missing accepted addition: `xref: UMLS:C0018798 {source="MONDO:obsoleteEquivalent", source="MONDO:MEDGEN", source="MEDGEN:6748"}`
- Missing accepted deletion: `xref: MEDGEN:6748 {source="MONDO:equivalentTo", source="MONDO:MEDGEN"}`
- Missing accepted deletion: `xref: OMIM:140500 {source="MONDO:equivalentObsolete"}`
- Missing accepted deletion: `xref: OMIM:234750 {source="MONDO:equivalentObsolete"}`
- Missing accepted deletion: `xref: UMLS:C0018798 {source="MONDO:equivalentTo", source="MONDO:MEDGEN", source="MEDGEN:6748"}`
- Extra changes beyond the accepted PR: 2 additions and 4 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `comment: Reason of obsoletion: out of scope - MONDO:excludePhenotype. Term to consider: heart disorder-MONDO:0005267`
- Extra agent addition: `property_value: IAO:0000231 OMO:0001000 {source="MONDO:excludePhenotype"}`
- Extra agent deletion: `replaced_by: MONDO:0009327`
- Extra agent deletion: `subset: gard_rare {source="GARD:0024658", source="MONDO:GARD"}`
- Extra agent deletion: `subset: nord_rare {source="MONDO:NORD"}`
- Extra agent deletion: `subset: rare`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
