---
repo: obophenotype/uberon
issue_number: 3682
pr_number: 3683
issue_title: "UBERON:0002346 \"neurectoderm\" vs \"neuroectoderm\""
issue_created_at: "2026-03-24"
issue_closed_at: "2026-04-23"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-23"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 18
    deletions: 17
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: developmental-anatomy
tags:
  - label-swap
  - neuroectoderm
  - synonym
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Clean label/synonym swap requiring understanding of preferred naming conventions in developmental biology
case_quality: good
case_quality_reason: single_complete_label_synonym_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

The issue reported that UBERON:0002346 used "neurectoderm" as the preferred label, while the more widely accepted term in modern developmental biology is "neuroectoderm." The existing label was moved to an exact synonym and the preferred label was updated.

## Changes Made

The PR swapped the preferred label of UBERON:0002346 from "neurectoderm" to "neuroectoderm" and demoted the old label to an exact synonym. A terminology note was added explaining the rationale, and a term_tracker_item was added referencing the issue.

## Resolution

This is a straightforward label/synonym swap affecting a single term stanza. An agent would need to understand the OBO format for label and synonym lines, and know that both forms are valid but "neuroectoderm" is preferred in current usage. Approved on first review.
