---
repo: obophenotype/cell-ontology
issue_number: 3010
pr_number: 3225
issue_title: "[Obsolete] structural cell"
issue_created_at: "2024-11-01"
pr_author: Caroline-99
pr_merged_at: "2025-08-07"
pr_num_commits: 2
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 9
    deletions: 7
scoping: loosely_scoped
scoping_notes: "PR obsoletes CL:0000293 and also rewires two dependent classes (scleral cell, choroidal cell) to point to CL:0000000 instead. Multiple conceptual operations in one PR."
eval_suitability: unusable
eval_suitability_notes: "PR was auto-linked to issue #3224 (skos:prefLabel import bug) but actually addresses issue #3010 (obsolete structural cell). Agent given #3224 cannot produce the expected diff."
task_type: obsoletion
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: ontology-maintenance
tags:
  - obsoletion
  - structural-cell
  - cascade-fix
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Obsoletion with cascading fixes to dependent terms. Agent must understand that obsoleting a term requires also rewiring all classes that reference it.
---

## Context

Issue #3010 requested obsoleting CL:0000293 "structural cell" — a grouping term with only two subclasses that was deemed unsustainable. Note: the PR was automatically linked to issue #3224 (a `skos:prefLabel` import bug from MBAO) but the actual work is driven by #3010, as evidenced by the `IAO:0000233` tracking annotation in the diff.

## Changes Made

Modified `cl-edit.owl` with 9 additions and 7 deletions across three classes:

1. **CL:0000293 (structural cell)**: obsoleted — added deprecated flag, "OBSOLETE" prefix to definition, obsoletion reason comment, tracking issue link
2. **CL:0000347 (scleral cell)**: rewired equivalence axiom from `CL_0000293` to `CL_0000000` (cell)
3. **CL:0000348 (choroidal cell)**: rewired equivalence axiom from `CL_0000293` to `CL_0000000`, updated definition to remove "structural cell" reference

## Resolution

Approved on first review. Hard difficulty because the agent must understand the obsoletion cascade: you cannot just deprecate a term — you must also find and fix all downstream references. The two dependent classes needed their logical definitions rewritten to point to a new parent. All three agent attempts scored 0.0 F1, confirming this is genuinely difficult.
