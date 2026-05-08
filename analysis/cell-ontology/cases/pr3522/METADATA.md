---
repo: obophenotype/cell-ontology
issue_number: 3408
pr_number: 3522
issue_title: "Update type I-IV otic fibrocytes"
issue_created_at: "2025-10-27"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-04"
pr_num_commits: 6
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 63
    deletions: 26
scoping: mostly_scoped
task_type: other
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: auditory
tags:
  - definition-update
  - otic-fibrocyte
  - spiral-ligament
  - rename
  - cochlea
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large-scale update renaming and redefining 5 otic fibrocyte types with enhanced definitions and corrected anatomy references
---

## Context

The existing type I through V otic fibrocyte terms in CL had outdated labels and sparse definitions that did not reflect current understanding of their roles in cochlear ion homeostasis. Issue #3408 requested renaming these to "spiral ligament fibrocyte type I-V" to better reflect their anatomical localization, and expanding their definitions with information about ion transport functions, spatial distribution within the spiral ligament, and marker gene expression.

## Changes Made

Extensively updated `cl-edit.owl` with 63 additions and 26 deletions affecting all five otic fibrocyte types. Each term received a renamed label (e.g., "type I otic fibrocyte" became "spiral ligament fibrocyte type I"), an expanded textual definition with literature references, and updated logical axioms linking to UBERON spiral ligament subdivisions and GO ion transport processes. The changes ensure consistency across the entire fibrocyte type series.

## Resolution

Approved on first review in 6 commits. Hard difficulty because the update required coordinating changes across 5 related terms simultaneously, ensuring consistent naming conventions, accurate anatomical placement within cochlear substructures, and correct representation of each type's distinct ion transport roles in endolymph homeostasis.
