---
repo: obophenotype/cell-ontology
issue_number: 3460
pr_number: 3508
issue_title: "NTR - Prehypertrophic chondrocyte (preHTCs)"
issue_created_at: "2025-11-20"
pr_author: app/copilot-swe-agent
pr_merged_at: "2025-12-15"
pr_num_commits: 7
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 10
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: skeletal
tags:
  - NTR
  - chondrocyte
  - prehypertrophic
  - growth-plate
  - cartilage
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for prehypertrophic chondrocyte stage in the chondrocyte maturation sequence within the growth plate
---

## Context

A new term was requested for the prehypertrophic chondrocyte (preHTC), a distinct stage in the chondrocyte maturation sequence within the growth plate. Prehypertrophic chondrocytes are located between the proliferative zone and the hypertrophic zone and are characterized by exit from the cell cycle and the onset of Indian hedgehog (Ihh) expression. This term complements the existing hypertrophic chondrocyte (CL:0000743) and the newly added terms for the chondrocyte lineage.

## Changes Made

Added 10 new lines to `cl-edit.owl` defining the prehypertrophic chondrocyte with class declaration, label, textual definition referencing the growth plate zonal organization, subClassOf axiom under chondrocyte, and logical axioms capturing the cell's anatomical location and developmental stage markers.

## Resolution

Approved on first review after 7 commits. Medium difficulty because correctly positioning this cell type requires understanding the spatial and temporal sequence of chondrocyte maturation in endochondral ossification: resting -> proliferative -> prehypertrophic -> hypertrophic.
