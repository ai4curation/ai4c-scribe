---
repo: geneontology/go-ontology
issue_number: 27880
pr_number: 27886
issue_title: "Obsolete redundant term"
issue_labels:
  - obsoletion
issue_created_at: "2025-08-10"
issue_closed_at: "2025-08-12"
pr_author: pgaudet
pr_merged_at: "2025-08-12"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 4
    deletions: 8
scoping: tightly_scoped
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - redundancy
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Simple obsoletion with clear replacement term, approved without changes
---

## Context

Term was flagged as redundant with an existing parent term.

## Resolution

Author obsoleted the term and added a replaced_by annotation. Approved on first review.
