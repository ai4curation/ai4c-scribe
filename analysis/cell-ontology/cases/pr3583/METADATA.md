---
repo: obophenotype/cell-ontology
issue_number: 3521
pr_number: 3583
issue_title: "Add reference dataset and NS-Forest marker for human bipolar neuron types"
issue_created_at: "2025-12-08"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-03-16"
pr_num_commits: 3
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 13
    deletions: 0
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: neuroscience
tags:
  - annotation
  - see-also
  - reference-dataset
  - bipolar-neuron
  - retina
  - NS-Forest
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Batch addition of reference transcriptomic dataset links to 13 existing bipolar neuron terms
---

## Context

The CL practice of linking cell type terms to reference transcriptomic datasets via see_also annotations enables data-driven validation of cell type definitions. Issue #3521 requested adding see_also links to a reference transcriptomic dataset for 13 human bipolar neuron cell types in the retina, along with NS-Forest marker gene annotations that provide computational signatures for each type.

## Changes Made

Added 13 new lines to `cl-edit.owl`, one per bipolar neuron cell type, each adding a see_also annotation linking to the reference transcriptomic dataset. The terms updated include the various human retinal bipolar cell subtypes (e.g., ON bipolar cells, OFF bipolar cells, and their numbered subtypes).

## Resolution

Approved on first review in 3 commits. Simple difficulty because this is a systematic annotation addition following an established pattern -- each term receives the same type of see_also annotation pointing to the dataset, with no changes to class hierarchy or logical definitions.
