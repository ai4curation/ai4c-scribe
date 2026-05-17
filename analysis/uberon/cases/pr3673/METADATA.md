---
repo: obophenotype/uberon
issue_number: 3672
pr_number: 3673
issue_title: "add 'addedByHRA' subset tag"
issue_created_at: "2026-03-14"
issue_closed_at: "2026-03-19"
pr_author: nicolevasilevsky
pr_merged_at: "2026-03-19"
pr_num_commits: 2
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 0
scoping: tightly_scoped
task_type: other
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: metadata
tags:
  - subset-tag
  - HRA
  - metadata
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minimal metadata addition showing how subset tags are declared in the OBO header
case_quality: ok
case_quality_reason: gold_id_revised_away_from_verbatim_issue_text
scoring_caveat: "Issue #3672 proposed the camelCase ID 'addedByHRA' verbatim; the human's first commit used that form, then commit 2 ('revise subset def') changed it to snake_case 'added_by_HRA' (the merged/master form). Metadiff scores against the revised gold only. Attempts that produced a valid subsetdef using the issue's literal 'addedByHRA' (pr315, pr281, pr183) correctly score F1=0.0 on convention/wording but are valid, in-scope, functional edits — treat as partial_success, not hard failure. pr125's F1=1.0 is genuine (verified byte-identical to live obophenotype/uberon master)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The Human Reference Atlas (HRA) project needed a new subset tag "added_by_HRA" to track which terms in Uberon were contributed by HRA. This requires adding a subsetdef declaration to the OBO file header.

## Changes Made

A single line was added to the ontology header in uberon-edit.obo declaring the new subset "added_by_HRA" with a description. This is a minimal change that only modifies the file header, not any term stanzas.

## Resolution

Simple metadata addition. An agent would need to know where subset declarations go in OBO format (in the header section) and follow the existing subsetdef pattern. Approved on first review.

## Curation Note (data quality)

The case is a valid, single-PR reference (gold PR #3673 is the complete and only human resolution of issue #3672; no companion PRs; F1=1.0 for attempt pr125 was verified as genuine against live `obophenotype/uberon` master, not leakage/contamination). It is **not** a poor case.

However, there is a metadiff caveat worth recording for downstream scoring: issue #3672's body and title explicitly propose the camelCase ID **`addedByHRA`**. The human's first commit (`add subset tag`) used exactly that camelCase form; the second commit (`revise subset def`) then changed it to the snake_case **`added_by_HRA`** with the canonical description ("Classes tagged with this subset property were added on request from HuBMAP to support the HuBMAP Human Reference Atlas (HRA)."), which is what merged and is in master.

Consequently the three F1=0.0 attempts (pr315 claude-sonnet-4.5; pr281 and pr183 claude-haiku-4.5) each produced a syntactically valid, correctly placed, in-scope subsetdef that used the issue's *literal* `addedByHRA` proposal. They genuinely missed Uberon's universal snake_case subsetdef convention and the curator's revised wording (a real `wrong_pattern` quality miss), but they are functional, defensible edits — they should be scored as `partial_success`, not as hard failures, despite F1=0.0. The F1=0.0 here over-represents the failure severity. pr125 (gemma-4-31b) is a genuine clean `success`.

