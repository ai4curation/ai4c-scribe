---
repo: monarch-initiative/mondo
issue_number: 9937
pr_number: 10112
issue_title: "NTR/KY"
issue_labels:
  - New term request
  - user request
issue_created_at: "2026-02-11"
pr_author: katiermullen
pr_merged_at: "2026-04-02"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 15
    deletions: 0
scoping: tightly_scoped
scoping_notes: PR adds exactly one new disease term stanza.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: rare-disease
tags:
  - gene-disease
  - KY
  - neuromyopathy
  - ClinGen
  - muscular-disease
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: New gene-disease term for a rare neuromyopathy requiring correct classification and logical axioms
case_quality: ok
case_quality_reason: sound_gold_but_gene_disease_new_term_scores_sensitive_to_pattern_details
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

A new term request was filed for KY-related neuromyopathy. The KY gene (kyphoscoliosis peptidase) is involved in muscle development and maintenance, and mutations cause a rare neuromyopathy phenotype. The request came through ClinGen's gene-disease curation workflow.

## Changes Made

Added a new term stanza to `src/ontology/mondo-edit.obo` with 15 lines. The term includes a definition, gene-disease logical axioms linking the disease to KY via germline mutation, classification under the neuromyopathy hierarchy, and appropriate ClinGen provenance annotations.

## Resolution

Medium difficulty as it follows the standard gene-disease new term pattern but requires determining the correct parent class (neuromyopathy vs myopathy vs neuropathy) based on the clinical phenotype. An agent would need to understand that neuromyopathy affects both nerve and muscle and classify accordingly.
