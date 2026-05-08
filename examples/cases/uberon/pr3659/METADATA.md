---
repo: obophenotype/uberon
issue_number: 2421
pr_number: 3659
issue_title: "multicellular organism and organism substance should be disjoint"
issue_created_at: "2022-04-15"
pr_author: matentzn
pr_merged_at: "2026-02-11"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 0
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: upper-ontology
tags:
  - disjointness
  - upper-level
  - BFO-alignment
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minimal one-line disjointness axiom addition requiring understanding of upper-level ontology design and BFO alignment
---

## Context

Issue #2421 reported that UBERON:0000468 (multicellular organism) and UBERON:0000463 (organism substance) should be declared disjoint, as an organism is not a substance and vice versa. This issue had been open since April 2022, nearly four years before resolution, and an earlier PR #3151 had been superseded by this one.

## Changes Made

The PR added a single disjoint_from axiom to uberon-edit.obo, declaring multicellular organism (UBERON:0000468) disjoint from organism substance (UBERON:0000463). Despite being a one-line change, it required careful reasoning about upper-level ontology categories to ensure the disjointness assertion would not create unintended unsatisfiable classes downstream.

## Resolution

Medium difficulty despite the minimal diff. An agent would need to understand BFO-aligned upper-level ontology categories to assess whether the disjointness assertion is logically sound and would not break downstream inferences. The long gap between issue and resolution (nearly four years) reflects that this kind of foundational change requires careful deliberation. Same-day merge once submitted.
