---
repo: geneontology/go-ontology
issue_number: 31963
pr_number: 32009
issue_title: "Obsolete GO:0045550 geranylgeranyl reductase activity"
issue_created_at: "2026-04-24"
pr_author: dragon-ai-agent
pr_merged_at: "2026-04-28"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 6
    deletions: 3
scoping: tightly_scoped
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - obsoletion
  - enzymes
  - geranylgeranyl
  - replaced_by
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Clean obsoletion with direct replacement, typical of enzyme term consolidation where duplicate terms exist for the same activity
---

## Context

Issue #31963 requested obsoletion of GO:0045550 "geranylgeranyl reductase activity" because it duplicates GO:0102067 "geranylgeranyl diphosphate reductase activity". The terms describe the same enzymatic reaction but GO:0102067 has the more precise name matching the EC classification.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0045550 was obsoleted with:
- `is_obsolete: true`
- `replaced_by: GO:0102067` (direct replacement for automatic annotation migration)
- Removal of logical axioms

This is the standard pattern for enzyme term consolidation where one term subsumes another.

## Resolution

Merged directly. The obsoletion was straightforward because a clear 1:1 replacement existed. Per @raymond91125's analysis in the issue, GO:0045550 and GO:0102067 describe the same reaction, and the latter has the correctly precise name. Annotations can be automatically migrated using the `replaced_by` tag.
