---
repo: geneontology/go-ontology
issue_number: 31965
pr_number: 31971
issue_title: "protoporphyrinogen oxidase activity terms"
issue_created_at: "2026-04-24"
pr_author: sjm41
pr_merged_at: "2026-04-24"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 10
    deletions: 5
scoping: tightly_scoped
task_type: reclassification
difficulty: hard
scope: multi_term
review_outcome: changes_requested
domain_area: molecular_function
tags:
  - enzymes
  - EC-alignment
  - RHEA-xref
  - protoporphyrinogen
  - hierarchy-refactor
  - definition-update
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Complex enzyme hierarchy refactoring requiring reconciliation of EC/RHEA entries with GO term definitions and parent-child relationships
---

## Context

Issue #31965 identified that the protoporphyrinogen oxidase activity sub-hierarchy had incorrect mappings: the parent term GO:0070818 and its children did not correctly correspond to their EC and RHEA cross-references. Each term needed its definition, xrefs, and parent relationships realigned to match the actual biochemical reactions catalogued in EC/RHEA.

## Changes Made

In `src/ontology/go-edit.obo`, the protoporphyrinogen oxidase hierarchy was refactored:
- GO:0070818 (parent): Definition updated to include 3x stoichiometry matching RHEA:64720
- Child terms: EC and RHEA xrefs corrected to point to the right reactions
- Definitions rewritten to accurately describe each specific reaction variant
- Parent-child relationships verified against the reaction specificity hierarchy

Net +5 lines reflecting additional xrefs and expanded definitions.

## Resolution

The PR was merged same-day but received review feedback from @pgaudet requesting that child term names follow the standard "X as acceptor" naming pattern. This was addressed in follow-up PR #31979. This case demonstrates how enzyme term refactoring often requires multiple rounds: first the biochemical content is corrected, then naming conventions are applied.
