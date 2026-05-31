---
repo: obophenotype/cell-ontology
issue_number: 3379
pr_number: 3444
issue_title: "[Class hierarchy] CD4+ CD11b+ dendritic cell [CL_0000999]: Change parent to CD11b+ DC"
issue_created_at: "2025-10-10"
issue_closed_at: "2025-11-18"
pr_author: copilot-swe-agent
pr_merged_at: "2025-11-18"
pr_num_commits: 9
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: reclassification
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - reclassification
  - dendritic-cell
  - CD11b
  - CD4
  - equivalence-axiom
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Single-axiom reclassification changing the genus class in an equivalence axiom for a dendritic cell subtype
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

CD4-positive CD11b-positive dendritic cell (CL:0000999) had its EquivalentClasses axiom using conventional dendritic cell (CL:0000990) as the genus class. Since this cell type is specifically a CD11b-positive subset, the more appropriate genus is CD11b-positive dendritic cell (CL:0002465), which is itself a subclass of conventional DC.

## Changes Made

Changed a single line in the EquivalentClasses axiom in `cl-edit.owl`: replaced the genus class from CL:0000990 (conventional dendritic cell) to CL:0002465 (CD11b-positive dendritic cell). This makes the logical definition more precise without changing the inferred classification.

## Resolution

Approved on first review. Simple difficulty because it is a single axiom change, but the 9 commits suggest the agent explored multiple approaches before settling on the correct fix. This case demonstrates how equivalence axiom genus classes should be as specific as possible in OWL ontologies.
