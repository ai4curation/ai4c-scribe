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
case_quality: poor
case_quality_reason: gold_pr_is_out_of_scope_mega_edit
companion_prs: []
scoring_caveat: "metadiff scores every attempt against gold PR #10117, a 5,103-line ontology-wide synonym purge, while issue #10030 asks only to fix the synonyms on a single term (MONDO:0001628). Well-scoped, correct single-term fixes are capped at F1≈0.003 by construction. Judge attempts against the literal ask of issue #10030, not against #10117."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

An issue was filed reporting incorrect synonyms for MONDO:0001628, which led to a broader investigation revealing that many Mondo terms had synonyms with uncertain or incorrect semantics. These problematic synonyms had been imported from external sources without adequate validation and could mislead downstream consumers of the ontology.

The lead developer (matentzn) performed a systematic review and bulk removal of synonyms that could not be confidently classified as exact, related, broad, or narrow.

## Changes Made

Removed 5,103 lines from `src/ontology/mondo-edit.obo` with zero additions, representing a pure cleanup operation. This is one of the largest single-PR changes in recent Mondo history, affecting synonyms across potentially hundreds of terms. The removal was done programmatically after careful analysis of which synonyms had uncertain provenance or semantics.

## Resolution

Hard difficulty due to the scale and risk involved. Removing over 5,000 synonym lines requires high confidence that none of them are valid. The curator needed to develop criteria for identifying problematic synonyms, validate the removal set, and ensure no valuable synonyms were lost. An agent would struggle with this task as it requires both programmatic analysis and expert judgment about synonym quality.

## Curation Note (data quality)

**This is a poor evaluation case (`case_quality: poor`, reason `gold_pr_is_out_of_scope_mega_edit`).** Flagged by claude-opus-4.7 on 2026-05-15 during attempt review.

**The issue vs. the gold PR are not scope-matched.** Issue #10030 ("Incorrect synonyms for MONDO_0001628") reports a single, specific defect: the term MONDO:0001628 "tinea unguium" (a fungal nail infection) carries 8 erroneous "cellulitis and abscess..." synonyms (bacterial soft-tissue infections at unrelated body sites) mis-imported from DOID:13074. In the issue thread the curators (matentzn, sabrinatoro) decided against fixing it one-by-one and opted for "a more drastic-large scale approach."

The selected gold PR #10117 ("Remove synonyms with uncertain semantics") *is* that drastic approach: it deletes **5,103 synonym lines with zero additions across hundreds of unrelated terms** ontology-wide (corticoadrenal insufficiency, growth hormone deficiency, spotted fevers, multiple sclerosis, Jaccoud syndrome, etc.). Within it, the 8 tinea-unguium synonyms are removed — but so are thousands of unrelated lines, and even two *valid* tinea-unguium synonyms (`dermatophytic onychomycosis`, `onychomycosis due to dermatophyte`) are swept out as collateral.

**Scoring consequence.** Whole-diff metadiff compares each attempt's correct ~8–10-line single-term fix against this 5,103-line ontology-wide sweep. Every one of the 8 attempts is therefore capped at F1≈0.003 by construction, regardless of quality. This is the Step 3b "gold has an out-of-scope mega-edit" signature: F1 is uniformly near-zero across all attempts, including no-op-equivalent runs.

**Judging the attempts.** Against the *literal ask of issue #10030*, all 8 attempts succeed: each correctly removes exactly the 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 and preserves the valid nail-dermatophytosis synonyms and all logical axioms. The opencode/codex variants (kimi-k2.6, gpt-5.5 ×3) additionally and defensibly remove the parallel mis-imported `xref: ICD9:681.9 {source="DOID:13074"}` and add an `IAO:0000233` issue-tracker provenance annotation per the mondo-agent-config convention. The claude-opus-4.7 run additionally shows the best judgment by explicitly recognizing the curators' large-scale-cleanup intent and consciously scoping its PR narrowly while flagging the broader DO-import audit as follow-up.

No companion PRs exist (`gh search prs --repo monarch-initiative/mondo "10030"` returns only #10117); the issue was resolved by the single ontology-wide PR. Downstream aggregation should down-weight or exclude this case, or re-score attempts against the issue's narrow ask rather than the metadiff vs. #10117.
