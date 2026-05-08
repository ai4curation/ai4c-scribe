---
repo: obophenotype/cell-ontology
issue_number: 3497
pr_number: 3574
issue_title: "[NTR] Fasciacyte"
issue_created_at: "2025-11-28"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-03-13"
pr_num_commits: 8
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 12
    deletions: 0
  - path: src/ontology/components/bgo-cl-comp.owl
    additions: 2
    deletions: 2
  - path: src/ontology/components/cellxgene_subset.owl
    additions: 2
    deletions: 2
  - path: src/ontology/components/clm-cl.owl
    additions: 2
    deletions: 2
  - path: src/ontology/components/hra_subset.owl
    additions: 3
    deletions: 5
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: connective-tissue
tags:
  - NTR
  - fasciacyte
  - fascia
  - connective-tissue
  - hyaluronan
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New term for fasciacyte requiring review iteration and understanding of this recently described connective tissue cell type
---

## Context

The fasciacyte is a recently described cell type found in fascial tissue that is specialized for hyaluronan secretion, which maintains the lubrication and gliding properties of fascial layers. Issue #3497 requested a new CL term for this cell type. Fasciacytes are distinct from fibroblasts and other connective tissue cells in their morphology and functional specialization, though they share some markers with the fibroblast lineage.

## Changes Made

Added 12 new lines to `cl-edit.owl` defining the fasciacyte term with class declaration, label, textual definition referencing the hyaluronan-secreting function and fascial tissue localization, parentage under connective tissue cell, and logical axioms capturing the capable_of relationship to hyaluronan biosynthesis (GO) and part_of relationship to UBERON fascia structures. Component files received minor version updates.

## Resolution

The PR went through one round of changes_requested review before approval and merge in 8 commits. Medium difficulty because fasciacytes are a relatively new cell type classification and correctly representing their relationship to fibroblasts versus positioning them as a distinct connective tissue cell type required careful ontological modeling.
