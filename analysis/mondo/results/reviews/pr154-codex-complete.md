---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 154
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: bulk_edit
difficulty: hard
f1: 0.003
precision: 0.002
recall: 1.0
jaccard: 0.002
outcome: failure
failure_modes: [over_editing, wrong_pattern, scope_creep]
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following .claude/skills/review-agent-pr/SKILL.md

  Source issue: https://github.com/monarch-initiative/mondo/issues/10030
  Human PR (ground truth): https://github.com/monarch-initiative/mondo/pull/10117
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-mondo/pull/154
  Agent config: ai4curation/mondo-agent-config

  Quick reference:
    gh issue view 10030 --repo monarch-initiative/mondo
    gh pr diff 10117 --repo monarch-initiative/mondo
    gh pr diff 154 --repo ai4curation/eval-ont-agent-mondo
-->

## Summary

Source PR #10117 addressed `bulk_edit` for issue #10030: Incorrect synonyms for MONDO_0001628. Human
resolution summary: Removed 5,103 lines from `src/ontology/mondo-edit.obo` with zero additions,
representing a pure cleanup operation. This is one of the largest single-PR changes in recent Mondo
history, affecting synonyms across potentially hundreds of terms. The removal was done
programmatically after careful analysis of which synonyms had uncertain provenance or semantics.
This attempt changed `src/ontology/mondo-edit.obo` and scored F1=0.003 (precision=0.002,
recall=1.0). It matched 0/0 accepted additions and 0/37 accepted deletions.

## Strengths

- The attempt has little direct normalized overlap with the accepted PR; any useful work is not captured by matching human diff lines.
- High recall indicates the agent covered most accepted changes.

## Issues

- Missing accepted changes: 0 additions and 37 deletions from the human PR were not reproduced.
- Missing accepted deletion: `synonym: "corticoadrenal insufficiency" EXACT [DOID:10493]`
- Missing accepted deletion: `synonym: "ENFL" EXACT ABBREVIATION [DOID:0060681]`
- Missing accepted deletion: `synonym: "familial isolated growth hormone deficiency" EXACT [DOID:0060870]`
- Missing accepted deletion: `synonym: "IGHD" EXACT ABBREVIATION [DOID:0060870]`
- Extra changes beyond the accepted PR: 0 additions and 8 deletions. These may be defensible only if independently justified by the issue discussion.
- Extra agent deletion: `synonym: "cellulitis and abscess" RELATED [DOID:13074]`
- Extra agent deletion: `synonym: "cellulitis and abscess of buttock" EXACT [DOID:13074, ICD9CM:682.5]`
- Extra agent deletion: `synonym: "cellulitis and abscess of face" EXACT [DOID:13074]`
- Extra agent deletion: `synonym: "cellulitis and abscess of finger" EXACT [DOID:13074]`
- Overall this is a failure because the accepted edit was largely missed or buried under substantial unrelated change.
