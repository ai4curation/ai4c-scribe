---
repo: monarch-initiative/mondo
issue_number: 9855
pr_number: 10115
issue_title: "Request for new term PADI6-related oocyte/zygote/embryo maturation arrest 16 and maternal-effect disorder"
issue_created_at: "2026-01-02"
pr_author: katiermullen
pr_merged_at: "2026-04-02"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 19
    deletions: 11
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: New term request that required merging information from a previously obsoleted term, demonstrating knowledge of obsoletion recovery patterns.
case_quality: ok
case_quality_reason: sound_gold_but_requires_obsoleted_term_recovery
quality_flagged_by: codex
quality_flagged_at: "2026-05-17"
---

## Context

Issue #9855 requested a new term for "PADI6-related oocyte/zygote/embryo maturation arrest 16 and maternal-effect disorder". The curator discovered that this concept overlapped with the previously obsoleted MONDO:0014978, which had been deprecated but contained relevant metadata (synonyms, xrefs, definitions) that should be preserved in the new term.

## Changes Made

The PR created the new term while incorporating metadata from obsoleted MONDO:0014978. The 19 additions include the new term stanza with label, definition, synonyms (including "oocyte/zygote/embryo maturation arrest 16" and "PREIMPLANTATION EMBRYONIC LETHALITY 2"), parent classification, and cross-references. The 11 deletions likely reflect updating the obsoleted term's replaced_by annotation to point to the new term.

## Resolution

Moderate difficulty because it requires recognizing the relationship between a new term request and an existing obsoleted term. The curator noted this overlap in the PR description and merged information appropriately. An agent would need to search for related obsoleted terms when creating new terms and reconcile their metadata, which requires understanding of the obsoletion/replacement workflow.
