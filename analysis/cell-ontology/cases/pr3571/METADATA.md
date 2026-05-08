---
repo: obophenotype/cell-ontology
issue_number: 3533
pr_number: 3571
issue_title: "Add articular cartilage zonal chondrocyte cell types"
issue_created_at: "2025-12-15"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-02-19"
pr_num_commits: 8
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 51
    deletions: 5
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
    additions: 898
    deletions: 20
scoping: loosely_scoped
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: skeletal
tags:
  - NTR
  - chondrocyte
  - articular-cartilage
  - zonal
  - superficial
  - deep
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multiple new chondrocyte terms for articular cartilage zones with substantial HRA subset updates
---

## Context

Articular cartilage is organized into distinct zones (superficial, middle/transitional, deep/radial) with morphologically and functionally distinct chondrocyte populations in each zone. Issue #3533 requested adding cell type terms for the zonal chondrocyte subtypes found in articular cartilage, which are important for joint biology and osteoarthritis research. These terms complement the broader chondrocyte lineage expansion effort.

## Changes Made

Added 51 new lines and removed 5 in `cl-edit.owl`, defining multiple articular cartilage zonal chondrocyte terms including superficial zone chondrocyte, middle zone chondrocyte, and deep zone chondrocyte. Each term includes appropriate parentage, textual definitions referencing zone-specific properties (e.g., flattened morphology and lubricin expression in the superficial zone), and part_of relationships to UBERON articular cartilage zone structures. The HRA subset component received a large update (898 additions) to incorporate these new terms into the Human Reference Atlas.

## Resolution

Approved on first review in 8 commits. Hard difficulty because this required defining multiple coordinated terms with zone-specific biological properties, ensuring consistent use of UBERON anatomical references for each cartilage zone, and managing the large-scale HRA subset update that accompanied the new terms.
