---
repo: obophenotype/uberon
issue_number: 3414
pr_number: 3499
issue_title: "NTR: broad ligament regions supporting fallopian tube & tissue layer addition"
issue_created_at: "2024-11-08"
pr_author: aleixpuigb
pr_merged_at: "2025-04-04"
pr_num_commits: 6
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 83
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: changes_requested
domain_area: reproductive-anatomy
tags:
  - new-term-request
  - fallopian-tube
  - myosalpinx
  - tissue-layers
  - cardinal-regions
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex multi-term addition creating a systematic set of tissue layer and regional subdivision terms for fallopian tube anatomy
---

## Context

Issue #3414 requested new terms for the myosalpinx (muscle layer of the fallopian tube), fallopian tube epithelium, and four cardinal regional subdivisions (superior, inferior, mesosalpinx-proximal, antimesosalpinx-proximal) for each tissue layer. This systematic decomposition supports detailed anatomical mapping of the fallopian tube.

## Changes Made

The PR added 83 lines to uberon-edit.obo, creating terms for myosalpinx, fallopian tube epithelium, and eight regional subdivision terms (four regions for each of the two tissue layers). Each term includes a definition, is_a classification, part_of relationships to the parent fallopian tube structure, and appropriate cross-references. Six commits indicate iterative development with review feedback.

## Resolution

Hard difficulty. An agent would need to understand the systematic naming convention for cardinal regions of tubular organs, correctly model the part_of relationships between tissue layers and their regional subdivisions, and ensure consistency across the set of ten new terms. The six commits and five-month timeline from issue to merge suggest substantive review feedback was incorporated.
