---
repo: obophenotype/uberon
issue_number: 3003
pr_number: 3511
issue_title: "review definition of cardiac septum and its child terms"
issue_created_at: "2023-08-03"
pr_author: cmungall
pr_merged_at: "2025-04-24"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 1
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: cardiac-anatomy
tags:
  - definition-update
  - cardiac-septum
  - outflow-tract
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Definition broadening for cardiac septum requiring understanding of cardiac anatomy hierarchy and child term coverage
---

## Context

Issue #3003 noted that the definition of cardiac septum (UBERON:0002099) was too narrow, mentioning only septa between atria and ventricles. However, child terms in the hierarchy include atrioventricular septum and outflow tract septum, which the original definition did not accommodate. The issue had been open since August 2023.

## Changes Made

The PR updated the definition of UBERON:0002099 (cardiac septum) to include all septa between parts of the heart, specifically accommodating the outflow tract. This was a single line replacement in uberon-edit.obo, changing the def tag to a broader formulation that encompasses all child terms.

## Resolution

Medium difficulty. While the change is a single-line definition update, an agent would need to inspect the child terms of cardiac septum, understand that the outflow tract septum is a valid subtype, and craft a definition broad enough to cover all children without being overly vague. The nearly two-year gap between issue and resolution reflects the careful consideration needed for definitional changes to anatomical grouping terms.
