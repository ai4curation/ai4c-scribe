---
repo: monarch-initiative/mondo
issue_number: 9826
pr_number: 10142
issue_title: "[Merge] short-rib thoracic dysplasia 22 without polydactyly & thoracic dysostosis, isolated"
issue_created_at: "2025-12-11"
pr_author: MeeSiing
pr_merged_at: "2026-04-08"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 13
    deletions: 9
scoping: tightly_scoped
scoping_notes: PR merges one term into another with standard obsoletion of the source term.
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: skeletal-disease
tags:
  - merge
  - OMIM
  - skeletal-dysplasia
  - thoracic-dysostosis
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Straightforward term merge following an OMIM consolidation of two skeletal dysplasia entries
---

## Context

MONDO:0008549 "thoracic dysostosis, isolated" and MONDO:0979242 "short-rib thoracic dysplasia 22 without polydactyly" were identified as representing the same disease entity after OMIM merged entry 187750 into 621260. A user request (issue #9826) flagged this redundancy and provided the OMIM provenance for the merge. The task required consolidating the two Mondo terms and obsoleting the duplicate.

## Changes Made

The PR obsoleted MONDO:0008549 and merged its metadata into MONDO:0979242. The 13 additions include obsoletion annotations on the source term (replaced_by pointing to MONDO:0979242) and an added definition for the surviving term. The 9 deletions remove the active classification axioms and synonyms from the obsoleted term. All changes are confined to `src/ontology/mondo-edit.obo`.

## Resolution

Simple difficulty because term merges following OMIM consolidations are well-documented in the Mondo SOP. The curator needs to mark the source term as obsolete, transfer relevant metadata (synonyms, cross-references) to the target term, and add a replaced_by annotation. An agent should be able to handle this given the OMIM provenance and the standard merge pattern.
