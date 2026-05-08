---
repo: obophenotype/cell-ontology
issue_number: 2967
pr_number: 3309
issue_title: "T follicular helper cell logical definition using obsolete term"
issue_created_at: "2025-02-13"
issue_closed_at: "2025-09-09"
pr_author: gouttegd
pr_merged_at: "2025-09-09"
pr_num_commits: 1
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - logical-definition
  - obsolete-term
  - GO-reference
  - T-cell
  - follicular-helper
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minimal single-line fix replacing an obsolete GO term reference in a logical definition
---

## Context

The logical definition of T follicular helper cell referenced a deprecated GO class. When GO obsoletes a term, downstream ontologies that use it in logical axioms must update their references to the replacement term. This is a common maintenance task in the OBO ecosystem.

## Changes Made

Changed a single GO term reference in `cl-edit.owl`, replacing the obsolete GO class with its active replacement in the logical definition of T follicular helper cell. One line added, one line removed.

## Resolution

Approved on first review in a single commit. Simple difficulty because the fix is mechanical: identify the obsolete term, find its replacement, and update the reference. However, this case illustrates an important pattern for agents working with OBO ontologies: they must be able to detect and resolve obsolete cross-ontology references.
