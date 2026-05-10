---
repo: geneontology/go-ontology
issue_number: 31965
pr_number: 31979
issue_title: "protoporphyrinogen oxidase activity terms"
issue_created_at: "2026-04-24"
pr_author: sjm41
pr_merged_at: "2026-04-27"
pr_num_commits: 1
files_changed:
  - path: src/ontology/go-edit.obo
    additions: 5
    deletions: 2
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: molecular_function
tags:
  - naming-convention
  - enzymes
  - protoporphyrinogen
  - review-followup
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Follow-up rename implementing reviewer feedback on naming conventions, demonstrating the iterative review process for enzyme terms
---

## Context

Issue #31965 identified problems with the protoporphyrinogen oxidase activity term hierarchy. The initial refactoring was done in PR #31971. During review, @pgaudet requested that the two child terms use the standard GO naming pattern "X as acceptor" rather than the names chosen in the initial PR. This follow-up implements that naming convention fix.

## Changes Made

In `src/ontology/go-edit.obo`, two child terms of the protoporphyrinogen oxidase hierarchy were renamed:
- GO:0004729: renamed from "oxygen-dependent protoporphyrinogen oxidase activity" to "protoporphyrinogen oxidase activity, oxygen as acceptor"
- The second child term was similarly renamed to follow the "X as acceptor" pattern

The old labels were retained as synonyms (+5 additions vs -2 deletions reflects the added synonym lines).

## Resolution

Merged directly as a straightforward naming convention application. The "X as acceptor" pattern is well-established in GO for distinguishing enzyme activities by their electron acceptor, and applying it here ensures consistency with hundreds of other similarly-named terms.
