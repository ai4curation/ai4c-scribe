---
ontology: mondo
issue_number: 9892
pr_number: 10206
eval_repo_pr: 488
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.769
precision: 0.667
recall: 0.909
jaccard: 0.625
outcome: partial_success
failure_modes: [over_editing]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9892
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10206
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/488
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9892 --repo monarch-initiative/mondo
    gh pr diff 10206 --repo monarch-initiative/mondo
    gh pr diff 488 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10206 addressed `synonym_update` for issue #9892: chronic myelogenous leukemia, BCR-ABL1
positive. Human resolution summary: Relabeled MONDO:0011996 from "chronic myelogenous leukemia,
BCR-ABL1 positive" to "chronic myeloid leukemia" in `src/ontology/mondo-edit.obo`. The old label and
variations were preserved as synonyms. The 7 additions and 8 deletions reflect the label change plus
synonym adjustments across 3 commits. This attempt changed `src/ontology/mondo-edit.obo` and scored
F1=0.769 (precision=0.667, recall=0.909). It matched 5/7 accepted additions and 5/8 accepted
deletions.

## Strengths

- Matched 10 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `is_a: MONDO:0011996 {source="NCIT:C9110"} ! chronic myeloid leukemia`
- Matched accepted addition: `is_a: MONDO:0011996 {source="DOID:0060761"} ! chronic myeloid leukemia`
- Matched accepted addition: `name: chronic myeloid leukemia`
- Matched accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9892" xsd:anyURI`
- Matched accepted deletion: `is_a: MONDO:0011996 {source="NCIT:C9110"} ! chronic myelogenous leukemia, BCR-ABL1 positive`
- Matched accepted deletion: `is_a: MONDO:0011996 {source="DOID:0060761"} ! chronic myelogenous leukemia, BCR-ABL1 positive`
- Matched accepted deletion: `name: chronic myelogenous leukemia, BCR-ABL1 positive`
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 2 additions and 3 deletions from the human PR were not reproduced.
- Missing accepted addition: `synonym: "chronic myeloid leukemia" EXACT [DOID:8552, https://medlineplus.gov/genetics/condition/chronic-myeloid-leukemia/#synonyms, https://orcid....`
- Missing accepted addition: `synonym: "leukimia, chronic myeloid" EXACT [OMIM:608232]`
- Missing accepted deletion: `synonym: "leukemia, chronic myeloid" RELATED []`
- Missing accepted deletion: `synonym: "leukemia, chronic myeloid, Philadelphia chromosome positive, somatic" EXACT []`
- Missing accepted deletion: `synonym: "leukemia, Philadelphia chromosome-positive, resistant to imatinib, Somatic mutation" EXACT []`
- Extra changes beyond the accepted PR: 1 additions and 0 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `synonym: "chronic myelogenous leukemia, BCR-ABL1 positive" EXACT [DOID:0081088, NCIT:C3174]`
- Overall this is a partial success: the attempt captures some intended curation but would still need curator correction before merge.
