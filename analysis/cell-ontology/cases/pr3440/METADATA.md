---
repo: obophenotype/cell-ontology
issue_number: 3382
pr_number: 3440
issue_title: "[Class hierarchy] Change CXCR3 property in CD8+ CXCR3+ alpha-beta regulatory T cell"
issue_created_at: "2025-10-10"
issue_closed_at: "2025-11-13"
pr_author: copilot-swe-agent
pr_merged_at: "2025-11-13"
pr_num_commits: 3
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
  - axiom-repair
  - relation-fix
  - CXCR3
  - plasma-membrane
  - T-cell
  - has_plasma_membrane_part
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minimal single-axiom fix correcting an overly generic relation to a more specific one for membrane protein annotation
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

CXCR3 is a chemokine receptor that resides on the plasma membrane. In the definition of CD8-positive CXCR3-positive alpha-beta regulatory T cell (CL:0001041), the relationship to CXCR3 was expressed using the generic `has_part` relation instead of the more specific `has_plasma_membrane_part`. This imprecision affects automated reasoning about cell surface markers.

## Changes Made

Changed a single OWL axiom in `cl-edit.owl`: replaced `has_part some CXCR3` with `has_plasma_membrane_part some CXCR3` for CL:0001041. One line added, one line removed.

## Resolution

Approved on first review. Simple difficulty because it is a single relation substitution, but it illustrates an important pattern: when annotating cell surface markers, the specific `has_plasma_membrane_part` relation should be used rather than the generic `has_part`, as this enables more precise reasoning about cell phenotypes.
