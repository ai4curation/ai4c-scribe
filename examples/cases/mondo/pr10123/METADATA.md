---
repo: monarch-initiative/mondo
issue_number: 9877
pr_number: 10123
issue_title: "GPR161-related medulloblastoma predisposition"
issue_labels:
  - New term request
  - user request
issue_created_at: "2026-01-14"
pr_author: katiermullen
pr_merged_at: "2026-04-06"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 10
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds exactly one new disease term with no unrelated changes.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: cancer-predisposition
tags:
  - gene-disease
  - GPR161
  - medulloblastoma
  - cancer-predisposition
  - ClinGen
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New cancer predisposition term requiring correct classification under both cancer and predisposition hierarchies
---

## Context

A new term request was filed for GPR161-related medulloblastoma predisposition. GPR161 is a G protein-coupled receptor involved in the Hedgehog signaling pathway, and germline mutations predispose to medulloblastoma, a common pediatric brain tumor. This term captures the genetic predisposition rather than the cancer itself, requiring careful placement in the ontology hierarchy.

## Changes Made

Added a new term stanza to `src/ontology/mondo-edit.obo` with 10 lines. The term includes a definition, gene-disease logical axioms linking to GPR161, and classification under the cancer predisposition hierarchy. The compact size reflects a well-structured new term following established patterns.

## Resolution

Medium difficulty because cancer predisposition terms require dual classification: they must be linked to both the cancer type (medulloblastoma) and the predisposition concept, while also encoding the causal gene relationship. An agent needs to understand the distinction between a cancer and a predisposition to cancer and apply the correct Mondo pattern.
