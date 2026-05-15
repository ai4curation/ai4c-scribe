---
repo: obophenotype/cell-ontology
issue_number: 3239
pr_number: 3245
issue_title: "remove tendon cell and otic fibrocyte from under fibrocyte"
issue_created_at: "2025-08-11"
issue_closed_at: "2025-08-19"
pr_author: Caroline-99
pr_merged_at: "2025-08-19"
pr_num_commits: 3
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 14
    deletions: 14
scoping: tightly_scoped
diff_noise: noisy
diff_noise_notes: "Protege serialization artifacts: CL_4072017/CL_4072018 declaration and stanza reordering, oboInOwl:hasDbXref comment label change. Only 2 of 5 diff hunks are real changes."
task_type: reclassification
difficulty: medium
scope: multi_term
review_outcome: multiple_rounds
domain_area: connective-tissue
tags:
  - reclassification
  - fibrocyte
  - tendon-cell
  - otic-fibrocyte
  - hierarchy-fix
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multi-term reclassification with review feedback, requiring domain knowledge about fibrocyte vs fibroblast lineage distinctions
---

## Context

Tendon cell and otic fibrocyte were incorrectly classified as children of fibrocyte in the CL hierarchy. Despite the name "otic fibrocyte," these cells are biologically distinct from true fibrocytes (which are quiescent fibroblast-derived cells). The otic fibrocytes of the spiral ligament and tendon cells needed to be moved to more appropriate parent classes.

## Changes Made

Modified 14 lines and added 14 lines in `cl-edit.owl`, changing the SubClassOf axioms for tendon cell and otic fibrocyte to remove them from under fibrocyte and place them under more appropriate parent classes. The equal addition/deletion count reflects the reclassification nature: removing old parent assertions and adding correct ones.

## Resolution

This PR went through multiple rounds of review, with changes requested before final approval. The reviewer flagged concerns about the reclassification, leading to iterative refinement. Medium difficulty because correctly reclassifying these cells requires understanding the biological distinction between fibrocytes (fibroblast-derived quiescent cells) and cells that merely have "fibrocyte" in their name due to historical convention.
