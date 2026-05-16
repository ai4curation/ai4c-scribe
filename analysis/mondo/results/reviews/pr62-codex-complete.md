---
ontology: mondo
issue_number: 9842
pr_number: 10158
eval_repo_pr: 62
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.921
precision: 0.906
recall: 0.935
jaccard: 0.853
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9842
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10158
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/62
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9842 --repo monarch-initiative/mondo
    gh pr diff 10158 --repo monarch-initiative/mondo
    gh pr diff 62 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10158 addressed `obsoletion` for issue #9842: [Merge]Extraoral halitosis due to
methanethiol oxidase deficiency & Autosomal recessive extra-oral halitosis. Human resolution
summary: Merged MONDO:0034186 into MONDO:0029144 by obsoleting the former and transferring its
cross-references, synonyms, and other annotations to the surviving term. The 16 additions and 16
deletions reflect the balanced nature of a merge operation: removing one stanza while enriching the
other. This attempt changed `src/ontology/mondo-edit.obo` and scored F1=0.921 (precision=0.906,
recall=0.935). It matched 15/16 accepted additions and 14/16 accepted deletions.

## Strengths

- Matched 29 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `subset: gard_rare {source="GARD:0017996", source="MONDO:GARD"}`
- Matched accepted addition: `subset: nord_rare {source="MONDO:NORD"}`
- Matched accepted addition: `subset: ordo_disorder {source="Orphanet:562538"}`
- Matched accepted addition: `subset: orphanet {source="Orphanet:562538"}`
- Matched accepted deletion: `name: autosomal recessive extra-oral halitosis`
- Matched accepted deletion: `comment: This term is scheduled to be merged with MONDO:0029144 Extraoral halitosis due to methanethiol oxidase deficiency, based on the fact that ...`
- Matched accepted deletion: `subset: gard_rare {source="GARD:0017996", source="MONDO:GARD"}`
- High precision indicates the agent mostly edited within the accepted change surface.
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 1 additions and 2 deletions from the human PR were not reproduced.
- Missing accepted addition: `relationship: has_characteristic HP:0000007 ! Autosomal recessive inheritance`
- Missing accepted deletion: `synonym: "EHMTO" RELATED ABBREVIATION []`
- Missing accepted deletion: `synonym: "extraoral halitosis due to MTO deficiency" EXACT []`
- Extra changes beyond the accepted PR: 1 additions and 1 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `relationship: has_characteristic HP:0000007 {source="Orphanet:562538"} ! Autosomal recessive inheritance`
- Extra agent deletion: `is_a: MONDO:0003847 {source="https://orcid.org/0000-0001-5208-3432"} ! hereditary disease`
- Overall this is a successful attempt; any differences above are minor relative to the requested curation.
