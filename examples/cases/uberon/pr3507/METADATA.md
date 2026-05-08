---
repo: obophenotype/uberon
issue_number: 3446
pr_number: 3507
issue_title: "NTR: medial prefrontal cortex"
issue_created_at: "2024-12-13"
pr_author: cmungall
pr_merged_at: "2025-04-24"
pr_num_commits: 4
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 11
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - new-term-request
  - brain
  - prefrontal-cortex
  - SCORCH
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New neuroanatomical term addition requiring correct placement in the cortical hierarchy and proper definition
---

## Context

Issue #3446 was a new term request for medial prefrontal cortex, a brain region important in neuroscience research for decision-making, social cognition, and emotional regulation. The request came as part of the SCORCH project's efforts to improve neuroanatomical coverage in Uberon.

## Changes Made

The PR added a new term stanza (11 lines) to src/ontology/uberon-edit.obo for medial prefrontal cortex, including a text definition, is_a placement under the prefrontal cortex hierarchy, appropriate cross-references, and contributor attribution. Four commits suggest iterative refinement of the term's definition or placement.

## Resolution

Medium difficulty. An agent would need to understand cortical neuroanatomy sufficiently to place the medial prefrontal cortex correctly in the hierarchy (as a subtype of prefrontal cortex, which is part of the frontal cortex), write an accurate definition that distinguishes it from adjacent regions, and include appropriate database cross-references.
