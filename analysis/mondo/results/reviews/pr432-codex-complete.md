---
ontology: mondo
issue_number: 9871
pr_number: 10201
eval_repo_pr: 432
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: other
difficulty: medium
f1: 0.385
precision: 0.268
recall: 0.682
jaccard: 0.238
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9871
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10201
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/432
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9871 --repo monarch-initiative/mondo
    gh pr diff 10201 --repo monarch-initiative/mondo
    gh pr diff 432 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10201 addressed `other` for issue #9871: MONDO:0009106 diastematomyelia. Human resolution
summary: The PR evolved from a simple xref correction into a multi-term edit across 5 commits. The
initial commit updated the Orphanet xref from 1671 to 573278. A proxy merge was fixed in the second
commit. The third commit added 3 new subtypes (MONDO:1060220-1060222) for split cord malformation
classification. The fourth and fifth commits resolved merge conflicts with master. The 59 additions
and 21 deletions reflect both th... This attempt changed `src/ontology/mondo-edit.obo` and scored
F1=0.385 (precision=0.268, recall=0.682). It matched 4/56 accepted additions and 10/21 accepted
deletions.

## Strengths

- Matched 14 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `subset: ordo_disorder {source="Orphanet:573278"}`
- Matched accepted addition: `subset: orphanet {source="Orphanet:573278"}`
- Matched accepted addition: `subset: orphanet_rare {source="Orphanet:573278"}`
- Matched accepted addition: `synonym: "diastematomyelia" EXACT [ICD10CM:Q06.2, icd11.foundation:2070601288, NCIT:C98913, OMIM:222500, Orphanet:573278]`
- Matched accepted deletion: `subset: ordo_disorder {source="Orphanet:1671"}`
- Matched accepted deletion: `subset: orphanet {source="Orphanet:1671"}`
- Matched accepted deletion: `subset: orphanet_rare {source="Orphanet:1671"}`

## Issues

- Missing accepted changes: 52 additions and 11 deletions from the human PR were not reproduced.
- Missing accepted addition: `synonym: "SCM type 1" NARROW ABBREVIATION [Orphanet:1671]`
- Missing accepted addition: `synonym: "split cord malformation" EXACT [GARD:0001851, Orphanet:573278]`
- Missing accepted addition: `synonym: "split cord malformation type 1" NARROW [Orphanet:1671]`
- Missing accepted addition: `synonym: "split spinal cord malformation" EXACT [GARD:0001851, Orphanet:573278]`
- Missing accepted addition: `synonym: "SSCM" EXACT ABBREVIATION [GARD:0001851]`
- Missing accepted deletion: `synonym: "split cord malformation" RELATED [GARD:0001851]`
- Missing accepted deletion: `synonym: "split spinal cord malformation" RELATED [GARD:0001851]`
- Missing accepted deletion: `synonym: "SSCM" RELATED ABBREVIATION [GARD:0001851]`
- Missing accepted deletion: `subset: ordo_disorder {source="Orphanet:573253"}`
- Extra changes beyond the accepted PR: 7 additions and 1 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `subset: ordo_morphological_anomaly {source="Orphanet:573278"}`
- Extra agent addition: `synonym: "SCM type 1" EXACT [Orphanet:573278]`
- Extra agent addition: `synonym: "split cord malformation type 1" EXACT [Orphanet:573278]`
- Extra agent addition: `xref: ICD10CM:Q06.2 {source="Orphanet:573278", source="MONDO:equivalentTo", source="Orphanet:573278/e", source="Orphanet:573278/specific"}`
- Extra agent addition: `xref: MedDRA:10012750 {source="Orphanet:573278", source="Orphanet:573278/e"}`
- Extra agent deletion: `subset: ordo_morphological_anomaly {source="Orphanet:1671"}`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
