---
repo: obophenotype/uberon
issue_number: 3618
pr_number: 3620
issue_title: "sixth lumbar dorsal root ganglion"
issue_labels:
  - new term request
issue_created_at: "2025-10-31"
issue_closed_at: "2025-11-03"
pr_author: dragon-ai-agent
pr_merged_at: "2025-11-03"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 13
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - new-term
  - dorsal-root-ganglion
  - spinal-anatomy
  - nervous-system
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: NTR following an existing series pattern (L1-L5 ganglia already exist), requiring positional anatomy knowledge
---

## Context

A new term was requested for the sixth lumbar dorsal root ganglion. Uberon already had terms for L1 through L5 dorsal root ganglia, so this request extended the series for species with six lumbar vertebrae.

## Changes Made

Added UBERON:9900001 for "sixth lumbar dorsal root ganglion" with synonyms (L6 dorsal root ganglion, sixth lumbar spinal ganglion), a definition, and relationships following the pattern established by the existing L1-L5 terms. The term was placed as part_of the appropriate spinal segment.

## Resolution

Medium difficulty because the agent must identify and follow the existing naming and axiom pattern for the L1-L5 series. It needs to understand that different species have different numbers of lumbar vertebrae and that the term must be modeled consistently with its siblings in the series.
