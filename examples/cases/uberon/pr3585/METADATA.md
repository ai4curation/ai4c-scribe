---
repo: obophenotype/uberon
issue_number: 3490
pr_number: 3585
issue_title: "consider allowing some whole cells in a 'multi cell part structure'"
issue_labels:
  - textual definition
issue_created_at: "2025-03-14"
issue_closed_at: "2025-07-14"
pr_author: gouttegd
pr_merged_at: "2025-07-14"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 2
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: hard
scope: single_term
review_outcome: approved_first_time
domain_area: neuroanatomy
tags:
  - definition-update
  - multi-cell-part-structure
  - gray-matter
  - white-matter
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Subtle definition change requiring deep understanding of how textual definitions constrain classification of nervous system structures
---

## Context

The term "multi cell part structure" (UBERON:0005162) had a definition that excluded any structure containing whole cells. However, structures like gray matter and white matter, which are classified under this term, do contain some whole cells (e.g., neuronal cell bodies in gray matter). The overly restrictive definition was inconsistent with biological reality.

## Changes Made

Broadened the textual definition of UBERON:0005162 to allow for the presence of some complete cells within a multi cell part structure, while maintaining the core concept that such structures are primarily composed of cell parts (e.g., axons, dendrites). A minimal 2-line addition, 1-line deletion.

## Resolution

Hard difficulty despite the small diff because this involves careful reasoning about how a definition change affects the semantics of an upper-level term. The agent must understand that gray matter contains neuronal cell bodies (whole cells) alongside axons and synapses (cell parts), and that the definition must accommodate this biological reality without making the term too broad. Four months elapsed between issue filing and resolution, indicating significant deliberation.
