---
repo: obophenotype/cell-ontology
issue_number: 3333
pr_number: 3547
issue_title: "Dont relabel imported annotation properties"
issue_created_at: "2025-09-16"
issue_closed_at: "2025-12-22"
pr_author: gouttegd
pr_merged_at: "2025-12-22"
pr_num_commits: 1
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 0
    deletions: 24
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: ontology-maintenance
tags:
  - annotation-properties
  - import-management
  - cleanup
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Purely subtractive cleanup removing redundant annotation property labels from the edit file
---

## Context

This is the second occurrence of the recurring issue where imported annotation properties (oboInOwl:hasDbXref, oboInOwl:hasExactSynonym, etc.) accumulate redundant `rdfs:label` annotations in the edit file. These labels already exist in the merged imports and their presence in the edit file is confusing and unnecessary. The issue was originally fixed in PR #3333 but the labels crept back in.

## Changes Made

Removed 24 lines of redundant `rdfs:label` annotations for imported annotation properties from `cl-edit.owl`. This is a purely subtractive change with no additions.

## Resolution

Approved on first review in a single commit. Simple difficulty because the fix is purely mechanical deletion, but it demonstrates an important maintenance pattern: understanding which annotations belong in the edit file versus the imports. An agent would need to understand OWL import chains to know which labels are redundant.
