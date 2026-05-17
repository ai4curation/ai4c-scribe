---
repo: test-org/test-ont
issue_number: 190
pr_number: 200
issue_title: "Reclassify baz widget"
issue_created_at: "2026-02-01"
pr_author: bob
pr_merged_at: "2026-02-20"
pr_num_commits: 4
files_changed:
  - path: src/ontology/test.obo
    additions: 5
    deletions: 3
scoping: tightly_scoped
task_type: reclassification
difficulty: hard
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-01"
rationale: Complex reclassification requiring domain knowledge
case_quality: poor
case_quality_reason: gold_leakage_base_contamination
companion_prs: [201, 202]
scoring_caveat: "Gold leaked into eval base; exclude from aggregates."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue requested reclassification of baz widget.

## Changes Made

Moved baz widget under new parent.

## Resolution

Reviewer requested changes to parent term placement.
