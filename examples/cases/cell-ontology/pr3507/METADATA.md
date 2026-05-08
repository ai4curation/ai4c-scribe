---
repo: obophenotype/cell-ontology
issue_number: 3506
pr_number: 3507
issue_title: "hypertrophic chondrocyte - link to Uberon and improve definition"
issue_created_at: "2025-12-03"
pr_author: app/copilot-swe-agent
pr_merged_at: "2025-12-12"
pr_num_commits: 10
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 8
    deletions: 3
  - path: src/ontology/components/2DFTU_HRA_illustrations.owl
    additions: 2
    deletions: 2
  - path: src/ontology/components/PNS_neurons.owl
    additions: 2
    deletions: 2
  - path: src/ontology/components/bgo-cl-comp.owl
    additions: 2
    deletions: 2
  - path: src/ontology/components/cellxgene_subset.owl
    additions: 2
    deletions: 2
scoping: mostly_scoped
task_type: other
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: skeletal
tags:
  - definition-update
  - chondrocyte
  - UBERON-link
  - GO-link
  - hypertrophic
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Definition improvement for hypertrophic chondrocyte requiring removal of inaccurate claim and addition of cross-ontology links
---

## Context

The existing definition of hypertrophic chondrocyte (CL:0000743) described it as "terminally differentiated," which is now known to be inaccurate -- hypertrophic chondrocytes can transdifferentiate into osteoblasts and osteocytes. Issue #3506 requested removing this claim, improving the textual definition, and adding links to relevant UBERON anatomical structures and GO biological processes.

## Changes Made

Updated `cl-edit.owl` with a revised textual definition for CL:0000743 that removes the "terminally differentiated" language, adds part_of links to UBERON growth plate structures, and adds capable_of links to relevant GO processes like chondrocyte hypertrophy. Component files were also updated with version bumps. The change touched 13 files total, though most were minor version updates in component OWL files.

## Resolution

Approved on first review after 10 commits of refinement. Medium difficulty because the change required understanding current research on chondrocyte transdifferentiation and selecting the appropriate UBERON and GO terms to cross-reference, while ensuring the updated definition accurately reflects the cell's biology without overclaiming.
