---
ontology: mondo
issue_number: 9892
pr_number: 10206
eval_repo_pr: 206
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.211
precision: 0.133
recall: 0.5
jaccard: 0.118
outcome: failure
failure_modes:
  - under_editing
  - missed_requirement
  - over_editing
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/9892
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10206
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/206
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 9892 --repo monarch-initiative/mondo
    gh pr diff 10206 --repo monarch-initiative/mondo
    gh pr diff 206 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10206 addressed `synonym_update` for issue #9892: chronic myelogenous leukemia, BCR-ABL1
positive. Human resolution summary: Relabeled MONDO:0011996 from "chronic myelogenous leukemia,
BCR-ABL1 positive" to "chronic myeloid leukemia" in `src/ontology/mondo-edit.obo`. The old label and
variations were preserved as synonyms. The 7 additions and 8 deletions reflect the label change plus
synonym adjustments across 3 commits. This attempt changed `src/ontology/mondo-edit.obo` and scored
F1=0.211 (precision=0.133, recall=0.5). It matched 1/7 accepted additions and 1/8 accepted
deletions.

## Strengths

- Matched 2 normalized human diff lines, showing direct overlap with the accepted curation.
- Matched accepted addition: `name: chronic myeloid leukemia`
- Matched accepted deletion: `name: chronic myelogenous leukemia, BCR-ABL1 positive`

## Issues

- Missing accepted changes: 6 additions and 7 deletions from the human PR were not reproduced.
- Missing accepted addition: `is_a: MONDO:0011996 {source="NCIT:C9110"} ! chronic myeloid leukemia`
- Missing accepted addition: `is_a: MONDO:0011996 {source="DOID:0060761"} ! chronic myeloid leukemia`
- Missing accepted addition: `synonym: "chronic myeloid leukemia" EXACT [DOID:8552, https://medlineplus.gov/genetics/condition/chronic-myeloid-leukemia/#synonyms, https://orcid....`
- Missing accepted addition: `synonym: "leukimia, chronic myeloid" EXACT [OMIM:608232]`
- Missing accepted addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/9892" xsd:anyURI`
- Missing accepted deletion: `is_a: MONDO:0011996 {source="NCIT:C9110"} ! chronic myelogenous leukemia, BCR-ABL1 positive`
- Missing accepted deletion: `is_a: MONDO:0011996 {source="DOID:0060761"} ! chronic myelogenous leukemia, BCR-ABL1 positive`
- Missing accepted deletion: `synonym: "chronic myeloid leukemia" EXACT [DOID:8552, NCIT:C3174, Orphanet:521]`
- Missing accepted deletion: `synonym: "leukemia, chronic myeloid" RELATED []`
- Extra changes beyond the accepted PR: 1 additions and 1 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `synonym: "chronic myelogenous leukemia, BCR-ABL1 positive" EXACT [DOID:0081088, NCIT:C3174]`
- Extra agent deletion: `synonym: "chronic myelogenous leukemia, BCR-ABL1 Positive" EXACT [DOID:0081088, NCIT:C3174]`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
