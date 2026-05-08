---
repo: monarch-initiative/mondo
issue_number: 9703
pr_number: 9770
issue_title: "Updates to Gene-Disease Classifications and Inheritance Patterns for Porphyria Disease Entities - ClinGen EIM group"
issue_labels:
  - New term request
  - user request
issue_created_at: "2025-10-29"
pr_author: sabrinatoro
pr_merged_at: "2025-11-20"
pr_num_commits: 7
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 60
    deletions: 9
  - path: src/ontology/Makefile
    additions: 1
    deletions: 1
  - path: src/sparql/qc/general/qc-definition-containing-underscore.sparql
    additions: 5
    deletions: 0
scoping: tightly_scoped
scoping_notes: Changes focused on porphyria disease branch with minor supporting infrastructure changes.
task_type: reclassification
difficulty: hard
scope: multi_term
review_outcome: changes_requested
domain_area: rare-disease
tags:
  - porphyria
  - ClinGen
  - gene-disease
  - inheritance-pattern
  - reclassification
  - new-terms
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex multi-term restructure of porphyria branch driven by ClinGen expert review requiring new terms, relabeling, and inheritance updates
---

## Context

The ClinGen Errors of Inborn Metabolism (EIM) group requested comprehensive updates to porphyria disease entities in Mondo. This included new gene-disease classifications, updated inheritance patterns, new labels, and new child terms. The changes were coordinated via a shared spreadsheet tracking all required updates across the porphyria disease branch.

Porphyrias are a group of metabolic disorders caused by enzyme deficiencies in the heme biosynthesis pathway. Accurate classification requires understanding both the biochemical pathway and the clinical presentations, which differ between acute and cutaneous forms.

## Changes Made

The PR made 60 additions and 9 deletions across `src/ontology/mondo-edit.obo`, involving new labels, new terms, updated inheritance annotations, and restructured classification for multiple porphyria entities. A minor Makefile update and a new SPARQL QC query for detecting underscores in definitions were also included. The 7 commits reflect an iterative curation process responding to expert review feedback.

## Resolution

Hard difficulty because the porphyria branch restructure required coordinating multiple types of changes (new terms, relabeling, inheritance updates, reclassification) across several related terms while maintaining consistency with ClinGen's expert classifications. An agent would need to interpret the spreadsheet-based requirements and apply domain-specific knowledge about porphyria subtypes.
