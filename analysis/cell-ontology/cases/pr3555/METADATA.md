---
repo: obophenotype/cell-ontology
issue_number: 3454
pr_number: 3555
issue_title: "[Class hierarchy] Remove CD44-high and CD122-high from CD45RO-positive memory T cells"
issue_created_at: "2025-11-20"
issue_closed_at: "2026-02-16"
pr_author: copilot-swe-agent
pr_merged_at: "2026-02-16"
pr_num_commits: 4
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 4
    deletions: 4
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: immunology
tags:
  - axiom-repair
  - marker-removal
  - CD44
  - CD122
  - memory-T-cell
  - species-specific-marker
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Marker correction requiring knowledge of species-specific expression differences between mouse and human T cells
---

## Context

CD44-high and CD122-high markers were included in the definition of CD45RO-positive memory T cells, but these markers are mouse-specific and not defining characteristics of human memory T cells. CD44 is broadly expressed across human T cell subsets (not specific to memory), and CD122-high expression is specific to mouse memory T cells. Since CD45RO is a human-specific marker, the term definition should not include mouse-specific marker assertions.

## Changes Made

Removed CD44-high and CD122-high marker assertions from the CD45RO-positive memory T cell definition in `cl-edit.owl`, with 4 lines added and 4 removed. The equal line counts reflect removing incorrect marker axioms and updating the definition text accordingly.

## Resolution

Approved on first review. Medium difficulty because correctly identifying which markers are species-specific requires understanding of comparative immunology between mouse and human T cell biology. An agent would need to recognize that combining mouse markers (CD44-high, CD122-high) with a human marker (CD45RO) is biologically inconsistent.
