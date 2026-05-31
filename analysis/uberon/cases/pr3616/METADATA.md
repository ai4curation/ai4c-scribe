---
repo: obophenotype/uberon
issue_number: 3613
pr_number: 3616
issue_title: "Typos in labels of UBERON:0009548 and UBERON:0009549"
issue_created_at: "2025-09-30"
issue_closed_at: "2025-11-03"
pr_author: dragon-ai-agent
pr_merged_at: "2025-11-03"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 2
    deletions: 2
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: hepatic-anatomy
tags:
  - typo-fix
  - label-correction
  - hepatic-sinusoid
  - liver
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Straightforward typo correction in two term labels, testing basic text editing in OBO format
case_quality: good
case_quality_reason: single_complete_label_typo_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Two hepatic sinusoid terms had typos in their labels: "hepatic sinusoid of left of lobe of liver" and "hepatic sinusoid of right of lobe of liver" each contained an extra "of" making the labels grammatically incorrect.

## Changes Made

Fixed the labels for UBERON:0009548 and UBERON:0009549 by removing the redundant "of" from each label. Changed "left of lobe" to "left lobe" and "right of lobe" to "right lobe" respectively. Two lines changed, two lines added.

## Resolution

Simple difficulty. The fix is a mechanical text correction in two term labels. An agent needs to locate the terms by ID and fix the obvious grammatical error. No domain knowledge is required beyond basic English grammar.
