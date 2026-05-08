---
repo: obophenotype/uberon
issue_number: 3602
pr_number: 3603
issue_title: "NTR: occlusal surface of tooth"
issue_labels:
  - new term request
issue_created_at: "2025-08-28"
issue_closed_at: "2025-09-02"
pr_author: dragon-ai-agent
pr_merged_at: "2025-09-02"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 9
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: dental-anatomy
tags:
  - new-term
  - tooth
  - dental-anatomy
  - surface-structure
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Simple NTR with clear parent term and straightforward anatomical definition
---

## Context

A new term request was filed for "occlusal surface of tooth," the biting or chewing surface where upper and lower teeth meet. The parent term "tooth surface structure" (UBERON:8600148) already existed, making classification straightforward.

## Changes Made

Added UBERON:8600149 for "occlusal surface of tooth" as a subclass of tooth surface structure. Included an exact synonym ("occlusal surface"), a definition referencing a dental education source, and appropriate relationships.

## Resolution

Simple difficulty because the parent class already existed and the anatomical concept is well-defined. An agent needs to follow the standard NTR pattern: create a new term stanza, place it under the correct parent, add a definition with reference, and include synonyms. Approved on first review.
