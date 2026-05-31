---
repo: monarch-initiative/mondo
issue_number: 9799
pr_number: 10114
issue_title: "[Obsolete]MONDO:0023124 familial pulmonary arterial hypertension leucopenia and atrial septal defect"
issue_created_at: "2025-11-28"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 9
    deletions: 4
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Term relabeling based on OMIM alignment where the original label was overly descriptive and a named syndrome exists.
case_quality: ok
case_quality_reason: sound_gold_but_external_source_alignment_limits_exact_inference
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #9799 proposed obsoleting MONDO:0023124 (familial pulmonary arterial hypertension leucopenia and atrial septal defect) because the term's only cross-reference appeared to match Dursun syndrome in OMIM. Rather than obsoleting, the curator relabeled the term to "Dursun syndrome" based on OMIM's included term designation.

## Changes Made

The PR relabeled MONDO:0023124 from the long descriptive name to "Dursun syndrome" and added associated metadata. The 9 additions include the new label, synonyms preserving the original name, and OMIM-sourced annotations. The 4 deletions remove the old label and outdated annotations. This approach preserves the term ID while improving its naming.

## Resolution

Simple difficulty because relabeling is less destructive than obsoletion and follows a clear pattern: change the rdfs:label, move the old label to a synonym, and add source annotations. The curator chose relabeling over obsoletion after verifying the OMIM alignment, which is a pragmatic decision that preserves term stability for downstream users.
