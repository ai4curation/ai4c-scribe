---
repo: geneontology/go-ontology
issue_number: 32018
pr_number: 32021
issue_title: "Obsoletion request: ergothioneine biosynthetic process terms"
issue_created_at: "2026-04-30"
pr_author: edwong57
pr_merged_at: "2026-05-04"
pr_num_commits: 1
files_changed:
  - path: src/taxon_constraints/only_in_taxon.tsv
    additions: 0
    deletions: 2
scoping: tightly_scoped
task_type: obsoletion
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - taxon-constraint
  - only_in_taxon
  - ergothioneine
  - cleanup
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Simple taxon constraint removal as part of term obsoletion workflow, showing that obsoletion involves cleanup across multiple files
---

## Context

Issue #32018 requested obsoletion of ergothioneine biosynthetic process terms (GO:0140479 and GO:0052704). Before these terms could be fully obsoleted, their taxon constraints in `only_in_taxon.tsv` needed to be removed. This PR handles that specific cleanup step.

## Changes Made

In `src/taxon_constraints/only_in_taxon.tsv`, two rows were removed:
- The entry for GO:0140479 (ergothioneine biosynthetic process)
- The entry for GO:0052704 (related ergothioneine term)

This is a pure deletion with no additions, reflecting the removal of constraints that are no longer meaningful for terms being obsoleted.

## Resolution

Merged directly. This is a routine cleanup step in the GO obsoletion workflow: when a term is obsoleted, its taxon constraints must also be removed since they no longer serve a purpose. The change is purely mechanical and low-risk.
