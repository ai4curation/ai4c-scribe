---
repo: geneontology/go-ontology
issue_number: 31985
pr_number: 31986
issue_title: "GO:0102177 24-methylenelophenol methyl oxidase activity"
issue_created_at: "2026-04-27"
pr_author: sjm41
pr_merged_at: "2026-04-27"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 7
    deletions: 5
scoping: tightly_scoped
task_type: reclassification
difficulty: hard
scope: single_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - enzymes
  - EC-realignment
  - RHEA-xref
  - MetaCyc-xref
  - sterol-biosynthesis
  - parent-change
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Complex enzyme term realignment requiring cross-database reconciliation of EC, RHEA, and MetaCyc identifiers with GO classification
case_quality: good
case_quality_reason: hard_but_clean_single_complete_gold_pr
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #31985 identified that GO:0102177 carried an `xref: EC:1.14.18.11` (plant 4-alpha-monomethylsterol monooxygenase) but its name, definition, RHEA cross-reference, MetaCyc cross-reference, and parent term all described a different reaction (an NADH-dependent partial reaction). All five fields needed realignment to match the actual EC:1.14.18.11 reaction.

## Changes Made

In `src/ontology/go-edit.obo`, GO:0102177 was comprehensively realigned:
- Name updated to match EC:1.14.18.11 nomenclature
- Definition rewritten to describe the correct reaction
- RHEA cross-reference corrected
- MetaCyc cross-reference corrected
- Parent `is_a` relationship changed to the appropriate oxidase parent
- Net +2 lines reflecting addition of previously missing xrefs

## Resolution

Merged same-day by the reporting curator (@sjm41). This is a technically demanding correction because it requires reconciling multiple external database identifiers (EC, RHEA, MetaCyc) with the GO term hierarchy to ensure all five aspects of the term (name, def, xrefs, parent) describe the same biochemical reaction.
