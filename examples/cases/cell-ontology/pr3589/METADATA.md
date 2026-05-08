---
repo: obophenotype/cell-ontology
issue_number: 3588
pr_number: 3589
issue_title: "Prevent contributors from relabelling imported annotation properties"
issue_created_at: "2026-03-13"
issue_closed_at: "2026-03-17"
pr_author: gouttegd
pr_merged_at: "2026-03-17"
pr_num_commits: 3
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 0
    deletions: 24
  - path: src/ontology/cl.Makefile
    additions: 7
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: build-infrastructure
tags:
  - annotation-properties
  - import-management
  - Makefile
  - recurring-issue
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Recurring cleanup issue requiring both ontology edits and build system changes to prevent future regressions
---

## Context

Contributors had repeatedly re-added `rdfs:label` annotations to imported annotation properties (like `oboInOwl:hasDbXref`, `oboInOwl:hasExactSynonym`) in the edit file. These labels are already defined in the merged imports and having duplicates in the edit file causes confusion. This was the third time this cleanup had to be performed (see also PRs #3547 and #3333).

## Changes Made

Removed 24 lines of redundant annotation property labels from `cl-edit.owl`. Added a SPARQL-based check to `cl.Makefile` that will detect and flag any future re-introduction of these labels during the build process, preventing regression.

## Resolution

Approved on first review. The medium difficulty reflects the need to understand both the OWL import chain (why these labels are redundant) and to implement a build-system guard. An agent would need to modify both the ontology file and the Makefile, understanding the relationship between them.
