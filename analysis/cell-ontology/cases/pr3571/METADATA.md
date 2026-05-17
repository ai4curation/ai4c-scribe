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
case_quality: poor
case_quality_reason: odk_regenerated_file_domination
companion_prs: []
scoring_caveat: "Gold PR #3571 bundles ~9000 lines of ODK pipeline-regenerated artifacts (merged_import.owl +920/-5186, hra_subset.owl +898/-20, cellxgene_subset.tsv +959/-959, six component version-date bumps) on top of a genuine ~46-line hand edit in cl-edit.owl. Whole-file metadiff therefore scores every attempt at F1~=0.002-0.005 even when the substantive new-term work is essentially correct. Judge attempts against the issue and gold's cl-edit.owl term block only, NOT the reported F1."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Articular cartilage is organized into distinct zones (superficial, middle/transitional, deep/radial) with morphologically and functionally distinct chondrocyte populations in each zone. Issue #3533 requested adding cell type terms for the zonal chondrocyte subtypes found in articular cartilage, which are important for joint biology and osteoarthritis research. These terms complement the broader chondrocyte lineage expansion effort.

## Changes Made

Added 51 new lines and removed 5 in `cl-edit.owl`, defining multiple articular cartilage zonal chondrocyte terms including superficial zone chondrocyte, middle zone chondrocyte, and deep zone chondrocyte. Each term includes appropriate parentage, textual definitions referencing zone-specific properties (e.g., flattened morphology and lubricin expression in the superficial zone), and part_of relationships to UBERON articular cartilage zone structures. The HRA subset component received a large update (898 additions) to incorporate these new terms into the Human Reference Atlas.

## Resolution

Approved on first review in 8 commits. Hard difficulty because this required defining multiple coordinated terms with zone-specific biological properties, ensuring consistent use of UBERON anatomical references for each cartilage zone, and managing the large-scale HRA subset update that accompanied the new terms.

## Curation Note (data quality)

**Flagged poor: ODK build-regenerated-file domination.** `quality_flagged_by: claude-opus-4.7`, `quality_flagged_at: 2026-05-16`.

The genuine, hand-authored content of gold PR #3571 is confined to ~46 lines in `src/ontology/cl-edit.owl`: four new classes `CL_9900000`–`CL_9900003` (superficial / middle / deep / calcified zone articular chondrocyte) as `SubClassOf CL_1001607`, plus a handful of new GO/PR `Declaration`s, three GO `expresses`/equivalence swaps, and two synonym-annotation-property label fixes. Everything else in the PR is ODK release-pipeline output that an issue-scoped agent cannot and should not reproduce:

- `src/ontology/imports/merged_import.owl`: +920 / **-5186** (regenerated import module)
- `src/ontology/components/hra_subset.owl`: +898 / -20 (regenerated HRA subset, incl. unrelated `RO_0002175`/NCBITaxon blocks for `CL_0000067` etc.)
- `src/templates/cellxgene_subset.tsv`: +959 / -959 (pure regeneration/reordering)
- Six component files (`bgo-cl-comp.owl`, `cellxgene_subset.owl`, `clm-cl.owl`, `hra_subset.owl`, `wmbo-cl-comp.owl`, `definitions.owl`) with only `versionIRI`/`versionInfo` date bumps (2025-12-17 / 2025-10-29 → 2026-02-19)
- `imports/go_terms.txt` (+4), `imports/pr_terms.txt` (+2/-1)

Whole-file metadiff divides each agent's correct ~40-line term block by this ~9000-line regenerated denominator, yielding artificial F1 of 0.002–0.005 for all four attempts despite all four substantively resolving the issue. The case is **not** curator-repudiated and **not** multi-PR: search confirms #3571 is the sole PR for issue #3533, and curator @RiveraAndrea83 (MEMBER) explicitly confirmed in the issue thread that the terms were added to the correct parent. The issue itself contained an erroneous parent ID (`CL:0002557` = "fibroblast of pulmonary artery"); all four agents correctly resolved it to `CL_1001607`, matching gold and the curator's confirmation.

**Scoring guidance:** exclude or heavily down-weight the reported F1/precision/recall/jaccard for this case. Evaluate attempts against the issue text and gold's `cl-edit.owl` term block only. Substantive ranking: pr193 (opus-4.7) ≈ pr205 (sonnet-4.5) > pr244 (copilot/sonnet-4.5) ≈ pr142 (haiku-4.5); the latter two used a one-position ID offset (`CL_9900001`–`CL_9900004`) and weaker synonym coverage, but all four are functionally successful.
