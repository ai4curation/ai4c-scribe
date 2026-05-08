---
repo: monarch-initiative/mondo
issue_number: 9892
pr_number: 10206
issue_title: "chronic myelogenous leukemia, BCR-ABL1 positive"
issue_labels:
  - relabel term
  - user request
issue_created_at: "2026-01-22"
pr_author: MeeSiing
pr_merged_at: "2026-04-30"
pr_num_commits: 3
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 7
    deletions: 8
scoping: tightly_scoped
scoping_notes: Changes limited to relabeling one term and updating its synonyms.
task_type: synonym_update
difficulty: easy
scope: single_term
review_outcome: approved_with_revisions
domain_area: oncology
tags:
  - relabel
  - leukemia
  - BCR-ABL1
  - OMIM
  - nomenclature
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Label update requiring judgment about naming conventions and alignment with OMIM nomenclature
---

## Context

A request was made to relabel MONDO:0011996 to "chronic myeloid leukemia" to better align with OMIM's naming ("leukemia, chronic myeloid"). The existing label "chronic myelogenous leukemia, BCR-ABL1 positive" was considered overly specific for the primary label, as the BCR-ABL1 qualifier could be captured as a synonym instead.

The PR involved some discussion about how strictly Mondo should follow OMIM naming conventions, reflected in the 3 commits needed to finalize the label.

## Changes Made

Relabeled MONDO:0011996 from "chronic myelogenous leukemia, BCR-ABL1 positive" to "chronic myeloid leukemia" in `src/ontology/mondo-edit.obo`. The old label and variations were preserved as synonyms. The 7 additions and 8 deletions reflect the label change plus synonym adjustments across 3 commits.

## Resolution

Easy difficulty overall, though it required a minor judgment call about naming conventions. The multiple commits suggest some back-and-forth about the exact label wording. An agent would need to understand Mondo's relationship with OMIM naming and when to simplify versus preserve qualifier terms.
