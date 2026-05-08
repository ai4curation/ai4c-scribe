---
repo: monarch-initiative/mondo
issue_number: 9707
pr_number: 9745
issue_title: "Mondo request for SCN5A disease entity for ClinGen"
issue_labels:
  - New term request
  - user request
issue_created_at: "2025-10-30"
pr_author: katiermullen
pr_merged_at: "2025-11-12"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 40
    deletions: 1
scoping: tightly_scoped
scoping_notes: Adds two new terms and reclassifies a related existing term.
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: cardiac-disease
tags:
  - gene-disease
  - SCN5A
  - cardiac
  - ClinGen
  - cardiac-conduction
  - reclassification
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multi-term addition with reclassification requiring cardiac disease domain knowledge and ClinGen coordination
---

## Context

ClinGen requested new SCN5A-related disease entities for their gene curation workflow. SCN5A encodes a sodium channel subunit critical for cardiac conduction, and mutations cause a spectrum of cardiac rhythm disorders including Brugada syndrome, long QT syndrome type 3, and conduction defects. The request required creating two new gene-disease terms and adding child terms as specified in the detailed issue discussion.

Additionally, the existing term "atrioventricular dissociation" needed reclassification from its hereditary parent to "cardiac conduction defect" because the condition is not necessarily hereditary.

## Changes Made

Added two new SCN5A-related disease terms to `src/ontology/mondo-edit.obo` with associated child terms (40 additions), and reclassified "atrioventricular dissociation" by updating its parent (1 deletion to remove the old parent). The 2 commits reflect the new term additions and the parent reclassification as separate logical changes.

## Resolution

Hard difficulty because the PR involves multiple coordinated changes: creating two new gene-disease terms, adding their children, and correcting the classification of an existing term. An agent would need to understand the SCN5A channelopathy spectrum, determine correct parent classes for each new term, and recognize that the existing atrioventricular dissociation term was incorrectly classified as hereditary.
