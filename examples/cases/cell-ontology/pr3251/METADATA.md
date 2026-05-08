---
repo: obophenotype/cell-ontology
issue_number: 3243
pr_number: 3251
issue_title: "[Text and logical def] fibrocyte"
issue_created_at: "2025-08-12"
issue_closed_at: "2025-08-29"
pr_author: Caroline-99
pr_merged_at: "2025-08-29"
pr_num_commits: 8
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 10
    deletions: 7
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: connective-tissue
tags:
  - fibrocyte
  - logical-definition
  - text-definition
  - fibroblast-lineage
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Definition revision requiring domain knowledge about fibroblast-fibrocyte relationship and careful axiom construction
---

## Context

The fibrocyte term in CL needed both its textual and logical definitions revised. Fibrocytes are mature, quiescent cells derived from fibroblasts that reside in connective tissue. The existing definition was outdated or incomplete, and the logical axioms did not properly capture the cell's defining characteristics. This was part of the broader fibroblast branch improvement effort (#2097).

## Changes Made

Updated 7 lines and added 10 new lines in `cl-edit.owl` for the fibrocyte term. Changes included a revised textual definition with current literature references and updated logical axioms properly relating the fibrocyte to its developmental origin and functional characteristics.

## Resolution

Approved on first review despite taking 8 commits to finalize. Medium difficulty because revising both textual and logical definitions requires understanding the biological relationship between fibroblasts and fibrocytes, choosing correct OWL object properties for the logical definition, and ensuring consistency with related terms.
