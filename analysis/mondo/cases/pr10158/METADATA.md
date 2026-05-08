---
repo: monarch-initiative/mondo
issue_number: 9842
pr_number: 10158
issue_title: "[Merge]Extraoral halitosis due to methanethiol oxidase deficiency & Autosomal recessive extra-oral halitosis"
issue_labels:
  - merge
  - on list
  - user request
issue_created_at: "2025-12-19"
pr_author: MeeSiing
pr_merged_at: "2026-04-17"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 16
    deletions: 16
scoping: tightly_scoped
scoping_notes: Changes are limited to merging two related term stanzas into one.
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: rare-disease
tags:
  - merge
  - obsoletion
  - halitosis
  - SELENBP1
  - metabolic-disorder
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Term merge requiring cross-reference analysis to confirm two Mondo terms represent the same disease entity
---

## Context

Two Mondo terms were identified as representing the same disease: MONDO:0034186 (autosomal recessive extra-oral halitosis) and MONDO:0029144 (extraoral halitosis due to methanethiol oxidase deficiency). The Orphanet cross-reference for the former mapped to the same OMIM entry as the latter, confirming they describe the same condition caused by SELENBP1 mutations.

Term merges are a common curation task in Mondo when duplicate entries are discovered through cross-reference analysis with external databases like Orphanet and OMIM.

## Changes Made

Merged MONDO:0034186 into MONDO:0029144 by obsoleting the former and transferring its cross-references, synonyms, and other annotations to the surviving term. The 16 additions and 16 deletions reflect the balanced nature of a merge operation: removing one stanza while enriching the other.

## Resolution

Medium difficulty because the curator must verify that the two terms genuinely represent the same entity by analyzing Orphanet-OMIM cross-reference chains, then execute the merge following Mondo's established obsoletion pattern (adding replaced_by, marking as obsolete, transferring annotations).
