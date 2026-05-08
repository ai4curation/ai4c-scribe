---
repo: monarch-initiative/mondo
issue_number: 10030
pr_number: 10117
issue_title: "Incorrect synonyms for MONDO_0001628"
issue_labels:
  - QC
  - user request
issue_created_at: "2026-03-16"
pr_author: matentzn
pr_merged_at: "2026-04-02"
pr_num_commits: 3
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 0
    deletions: 5103
scoping: loosely_scoped
scoping_notes: Bulk removal of synonyms across many terms in the ontology.
task_type: bulk_edit
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: quality-control
tags:
  - QC
  - synonyms
  - bulk-edit
  - data-quality
  - uncertain-semantics
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large-scale QC fix removing thousands of incorrect synonyms, requiring careful validation to avoid removing valid synonyms
---

## Context

An issue was filed reporting incorrect synonyms for MONDO:0001628, which led to a broader investigation revealing that many Mondo terms had synonyms with uncertain or incorrect semantics. These problematic synonyms had been imported from external sources without adequate validation and could mislead downstream consumers of the ontology.

The lead developer (matentzn) performed a systematic review and bulk removal of synonyms that could not be confidently classified as exact, related, broad, or narrow.

## Changes Made

Removed 5,103 lines from `src/ontology/mondo-edit.obo` with zero additions, representing a pure cleanup operation. This is one of the largest single-PR changes in recent Mondo history, affecting synonyms across potentially hundreds of terms. The removal was done programmatically after careful analysis of which synonyms had uncertain provenance or semantics.

## Resolution

Hard difficulty due to the scale and risk involved. Removing over 5,000 synonym lines requires high confidence that none of them are valid. The curator needed to develop criteria for identifying problematic synonyms, validate the removal set, and ensure no valuable synonyms were lost. An agent would struggle with this task as it requires both programmatic analysis and expert judgment about synonym quality.
