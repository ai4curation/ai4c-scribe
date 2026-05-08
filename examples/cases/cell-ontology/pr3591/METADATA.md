---
repo: obophenotype/cell-ontology
issue_number: 3590
pr_number: 3591
issue_title: "add subset tag 'add_by_HRA'"
issue_created_at: "2026-03-14"
issue_closed_at: "2026-03-20"
pr_author: nicolevasilevsky
pr_merged_at: "2026-03-20"
pr_num_commits: 4
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 6
    deletions: 0
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: single_term
review_outcome: changes_requested
domain_area: metadata
tags:
  - subset-annotation
  - HRA
  - annotation-property
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Simple annotation property addition demonstrating subset tagging patterns used for HRA provenance tracking
---

## Context

The Human Reference Atlas (HRA) project needed a way to track which cell types were contributed through their program. A new subset annotation tag `added_by_HRA` was requested to mark terms added at HRA's request.

## Changes Made

Added a new `oboInOwl:SubsetProperty` declaration for `added_by_HRA` to `src/ontology/cl-edit.owl`. This involved declaring the annotation property and adding appropriate label and comment annotations. The change is purely additive with 6 new lines.

## Resolution

Despite being a simple change, this PR went through review: an initial review was dismissed and a subsequent approval was given. The difficulty is simple because it only requires knowing how OWL subset properties are declared in OBO-format ontologies, but it demonstrates the pattern for provenance-tracking subsets.
