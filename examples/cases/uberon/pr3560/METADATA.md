---
repo: obophenotype/uberon
issue_number: 3447
pr_number: 3560
issue_title: "question on parentage of 'dorsolateral prefrontal cortex'"
issue_created_at: "2024-12-13"
issue_closed_at: "2025-06-16"
pr_author: dragon-ai-agent
pr_merged_at: "2025-06-16"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: reclassification
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - reclassification
  - prefrontal-cortex
  - brain-anatomy
  - partonomy
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Partonomy correction requiring neuroanatomical knowledge about cortical region organization
---

## Context

The dorsolateral prefrontal cortex (UBERON:0009834) was incorrectly modeled as part_of the cerebral cortex directly, rather than being part_of the prefrontal cortex (UBERON:0000451). This skipped an intermediate level in the anatomical hierarchy.

## Changes Made

Changed the part_of relationship for dorsolateral prefrontal cortex from cerebral cortex to prefrontal cortex. A single line was modified in the term stanza. This correctly reflects that the dorsolateral prefrontal cortex is a subregion of the prefrontal cortex, which itself is part of the cerebral cortex.

## Resolution

Medium difficulty because the agent must understand brain regional organization well enough to know that the dorsolateral prefrontal cortex should be placed under the prefrontal cortex rather than directly under the broader cerebral cortex. The issue was open for six months before resolution, suggesting the fix required some deliberation.
