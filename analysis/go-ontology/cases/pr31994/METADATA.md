---
repo: geneontology/go-ontology
issue_number: 31948
pr_number: 31994
issue_title: "Obsoletion request: glycoprotein cargo receptor activity"
issue_created_at: "2026-04-22"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 6
    deletions: 5
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - obsoletion
  - vesicle-mediated-transport
  - cargo-receptor
  - replaced_by
  - modeling-error
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Obsoletion of a term that was conceptually flawed, demonstrating ontological reasoning about when a subclass distinction is unhelpful
case_quality: good
case_quality_reason: single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #31948 flagged GO:7770028 "glycoprotein cargo receptor activity" for obsoletion. The term was added in error because most vesicle cargo proteins are glycoproteins, making "glycoprotein cargo receptor" an uninformative specialization of "cargo receptor activity" (GO:0038024). Classifying cargo receptors by whether their substrate happens to be glycosylated introduces an unhelpful and non-orthogonal axis of classification.

## Changes Made

In `src/ontology/go-edit.obo`, GO:7770028 was obsoleted:
- Marked `is_obsolete: true`
- Added `replaced_by: GO:0038024` (cargo receptor activity)
- Removed logical axioms
- Obsoletion reason documented in the comment field

## Resolution

Merged directly. The ontological argument was clear: the glycoprotein distinction does not represent a meaningful functional difference in receptor mechanism. This is a good example of quality control catching a term that, while technically valid biologically, creates a misleading classification axis.
