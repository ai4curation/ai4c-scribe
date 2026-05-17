---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 88
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: bulk_edit
difficulty: hard
f1: 0.003
precision: 0.002
recall: 0.8
jaccard: 0.002
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

  Source issue: https://github.com/monarch-initiative/mondo/issues/10030
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10117
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/88
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 10030 --repo monarch-initiative/mondo
    gh pr diff 10117 --repo monarch-initiative/mondo
    gh pr diff 88 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10117 addressed `bulk_edit` for issue #10030: Incorrect synonyms for MONDO_0001628. Human
resolution summary: Removed 5,103 lines from `src/ontology/mondo-edit.obo` with zero additions,
representing a pure cleanup operation. This is one of the largest single-PR changes in recent Mondo
history, affecting synonyms across potentially hundreds of terms. The removal was done
programmatically after careful analysis of which synonyms had uncertain provenance or semantics.
This attempt changed `src/ontology/mondo-edit.obo` and scored F1=0.003 (precision=0.002,
recall=0.8). It matched 0/0 accepted additions and 0/37 accepted deletions.

## Strengths

- The attempt has little direct normalized overlap with the accepted PR; any useful work is not captured by matching human diff lines.

## Issues

- Missing accepted changes: 0 additions and 37 deletions from the human PR were not reproduced.
- Missing accepted deletion: `synonym: "corticoadrenal insufficiency" EXACT [DOID:10493]`
- Missing accepted deletion: `synonym: "ENFL" EXACT ABBREVIATION [DOID:0060681]`
- Missing accepted deletion: `synonym: "familial isolated growth hormone deficiency" EXACT [DOID:0060870]`
- Missing accepted deletion: `synonym: "IGHD" EXACT ABBREVIATION [DOID:0060870]`
- Extra changes beyond the accepted PR: 1 additions and 9 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent addition: `property_value: IAO:0000233 "https://github.com/monarch-initiative/mondo/issues/10030" xsd:anyURI`
- Extra agent deletion: `synonym: "cellulitis and abscess" RELATED [DOID:13074]`
- Extra agent deletion: `synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]`
- Extra agent deletion: `synonym: "cellulitis and abscess of face" EXACT [DOID:13074]`
- Extra agent deletion: `synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
