---
repo: monarch-initiative/mondo
issue_number: 9861
pr_number: 10113
issue_title: "[NTR/gene] Hyperinsulinemic hypoglycemia, familial 3"
issue_created_at: "2026-01-07"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 6
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 13
    deletions: 6
scoping: tightly_scoped
scoping_notes: PR relabels an existing term and updates its classification and synonyms based on user request.
task_type: other
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: metabolic-disease
tags:
  - relabel
  - gene-disease
  - GCK
  - hyperinsulinism
  - OMIM
  - familial-hyperinsulinism
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Term relabeling with review iteration on classification, requiring confirmation that existing OMIM term matches the user request
---

## Context

A user requested a new gene-disease term for "hyperinsulinemic hypoglycemia, familial 3" (GCK-related hyperinsulinism) under issue #9861. During curation, it was determined that the existing term MONDO:0011236 already represented this disease but carried an outdated label. Rather than creating a duplicate, the curator updated the label and synonyms of the existing term. The PR also replaced an earlier failed attempt (PR #10090) that had git conflicts.

## Changes Made

The PR modified MONDO:0011236 in `src/ontology/mondo-edit.obo` with 13 additions and 6 deletions across 6 commits. Changes included updating the rdfs:label to "hyperinsulinemic hypoglycemia, familial, 3", adding "GCK-related hyperinsulinism" as an exact synonym, and adjusting the classification under MONDO:0017182 "familial hyperinsulinism." The multiple commits reflect both the review iteration (a CHANGES_REQUESTED review asking about classification) and the recreation of the PR after rebasing issues.

## Resolution

Medium difficulty because the curator needed to recognize that an existing term matched the new term request rather than creating a duplicate. The review process involved a classification question from the reviewer, requiring the contributor to confirm that the OMIM entry and the requested term were the same concept. An agent would need to search for existing terms before creating new ones and handle reviewer questions about hierarchical placement.
