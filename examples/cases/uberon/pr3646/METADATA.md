---
repo: obophenotype/uberon
issue_number: 3464
pr_number: 3646
issue_title: "Positioning 'life cycle' and 'life cycle stage' under 'process'"
issue_labels:
  - uberon-classhierarchy
issue_created_at: "2025-01-17"
issue_closed_at: "2026-01-12"
pr_author: matentzn
pr_merged_at: "2026-01-12"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 2
    deletions: 0
scoping: tightly_scoped
task_type: reclassification
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: upper-ontology
tags:
  - COB-alignment
  - life-cycle
  - upper-ontology
  - root-class
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Upper-level ontology restructuring requiring understanding of COB alignment and root class implications
---

## Context

As part of aligning Uberon with the Core Ontology for Biology (COB), "life cycle stage" and "life cycle temporary boundary" needed to be repositioned as root classes. This was an intermediate step before deprecating the "processual entity" class in a subsequent PR. The issue was open for nearly a year, indicating significant deliberation about the structural change.

## Changes Made

Added two lines to uberon-edit.obo to establish life cycle stage and life cycle temporary boundary as top-level classes. This minimal change has significant structural implications because it sets up the subsequent deprecation of processual entity.

## Resolution

Hard difficulty because changes to root-level ontology structure have cascading effects on the entire class hierarchy. The agent must understand the COB alignment strategy, know that these classes will become true roots once processual entity is deprecated, and ensure the change does not break existing reasoning. Despite the tiny diff, this required a year of discussion.
