---
repo: obophenotype/uberon
issue_number: 3591
pr_number: 3595
issue_title: "\"carotid body\" should not be part of the cardiovascular system"
issue_labels:
  - uberon-classhierarchy
issue_created_at: "2025-08-07"
issue_closed_at: "2025-09-15"
pr_author: cmungall
pr_merged_at: "2025-09-15"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 4
    deletions: 2
scoping: tightly_scoped
task_type: reclassification
difficulty: hard
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - reclassification
  - carotid-body
  - peripheral-nervous-system
  - cardiovascular
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Reclassification requiring deep anatomical knowledge to distinguish vascular location from functional system membership
---

## Context

The carotid body was incorrectly classified as part of the cardiovascular system in Uberon. While the carotid body is located near the carotid artery bifurcation, it is functionally a peripheral chemoreceptor organ belonging to the peripheral nervous system. The issue cited PMID:32965908 supporting reclassification.

## Changes Made

Corrected the classification of the carotid body by updating its is_a parent and system membership relationships. Removed the cardiovascular system association and added peripheral nervous system membership. The definition was also updated to emphasize its sensory organ role.

## Resolution

Hard difficulty because the carotid body's anatomical location (near the carotid artery) makes it easy to misclassify as cardiovascular. An agent must understand the distinction between spatial proximity and functional system membership, and know that the carotid body is a chemoreceptor, not a vascular structure. This requires genuine anatomical domain expertise.
