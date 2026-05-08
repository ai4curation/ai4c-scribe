---
repo: obophenotype/uberon
issue_number: 3583
pr_number: 3588
issue_title: "New terms for tooth surfaces"
issue_labels:
  - new term request
issue_created_at: "2025-07-11"
issue_closed_at: "2025-08-05"
pr_author: aleixpuigb
pr_merged_at: "2025-08-05"
pr_num_commits: 5
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 75
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: dental-anatomy
tags:
  - new-term
  - tooth-surfaces
  - dental-anatomy
  - batch-NTR
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multi-term NTR batch requiring consistent modeling of a set of related dental anatomy terms
---

## Context

A request was made to add multiple new terms for tooth surfaces to Uberon. Dental anatomy uses specific terminology for the different surfaces of a tooth (mesial, distal, buccal, lingual, etc.), and these were needed for downstream annotation projects.

## Changes Made

Added approximately 7-8 new tooth surface terms with 75 lines of additions to uberon-edit.obo. Each term followed a consistent pattern with definitions, synonyms, parent class (tooth surface structure), and relationships. The 5 commits suggest iterative refinement of the batch.

## Resolution

Medium difficulty because while each individual term follows a standard pattern, the agent must consistently apply the same modeling approach across multiple terms, ensure no duplication, and get the dental anatomy right for each surface type. The batch nature makes it more complex than a single NTR.
