---
repo: obophenotype/cell-ontology
issue_number: 3353
pr_number: 3354
issue_title: "[Text def] Create human specific term for chandelier Pvalb GABAergic neuron"
issue_created_at: "2025-09-29"
issue_closed_at: "2025-10-01"
pr_author: RiveraAndrea83
pr_merged_at: "2025-10-01"
pr_num_commits: 7
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 23
    deletions: 4
  - path: src/ontology/components/clm-cl.owl
    additions: 2
    deletions: 17
scoping: mostly_scoped
scoping_notes: >-
  Primary change is the new human-specific term, but also includes cleanup of the
  clm-cl.owl component file.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: neuroscience
tags:
  - neuron
  - chandelier-cell
  - parvalbumin
  - GABAergic
  - human-specific
  - taxon-specific
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Species-specific neuron term requiring understanding of taxon-specific classification patterns and GABAergic interneuron subtypes
---

## Context

The Allen Brain Cell Atlas and other human brain atlases distinguish human-specific subtypes of GABAergic interneurons. Chandelier cells are a morphologically distinct type of parvalbumin-positive (Pvalb+) GABAergic interneuron that forms characteristic axo-axonic synapses. A human-specific term was needed to support human brain cell-type annotation.

## Changes Made

Added a new human-specific term for chandelier Pvalb GABAergic interneuron to `cl-edit.owl` with 23 lines added and 4 modified. The term includes appropriate parentage under the species-neutral chandelier cell, a taxon constraint for Homo sapiens, and molecular marker annotations. Also cleaned up the `clm-cl.owl` component file (removing 17 lines, adding 2).

## Resolution

Medium difficulty because creating species-specific neuron subtypes requires understanding the CL pattern for taxon-specific terms, including: proper parentage under the species-neutral type, correct taxon constraint assertions, and appropriate marker annotations based on transcriptomic evidence. The component file changes add additional complexity.
