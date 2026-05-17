---
repo: obophenotype/uberon
issue_number: 3583
pr_number: 3588
issue_title: "New terms for tooth surfaces"
issue_labels:
  - new term request
issue_created_at: "2025-07-11"
issue_closed_at: "2025-08-05"
pr_author: aleixpuigb
pr_merged_at: "2025-08-05"
pr_num_commits: 5
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 75
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: dental-anatomy
tags:
  - new-term
  - tooth-surfaces
  - dental-anatomy
  - batch-NTR
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multi-term NTR batch requiring consistent modeling of a set of related dental anatomy terms
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
companion_prs: []
scoring_caveat: "Metadiff vs gold PR #3588 is misleading. The gold's defining design — an intermediate grouping class UBERON:8600148 'tooth surface structure' (logical def: surface structure AND part_of calcareous tooth) with all tooth-surface terms reparented under it, and the consequent 'A tooth surface structure that...' definition wording — was negotiated by reviewer @wdduncan during PR review (comments from 2025-08-02 onward), NOT present in issue #3583. The issue requested parent = surface structure (UBERON:0003102) directly and only 5 terms. Agents work from the issue + issue comments and cannot reproduce PR-review-derived structure. F1 is further depressed by the standard placeholder-vs-canonical UBERON ID artifact (agents emit UBERON:99xxxxx; gold uses UBERON:86001xx), which zeroes line-level metadiff on every id/is_a/intersection_of line. Judge attempts against the issue text + issue comments, not the renegotiated gold."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

A request was made to add multiple new terms for tooth surfaces to Uberon. Dental anatomy uses specific terminology for the different surfaces of a tooth (mesial, distal, buccal, lingual, etc.), and these were needed for downstream annotation projects.

## Changes Made

Added approximately 7-8 new tooth surface terms with 75 lines of additions to uberon-edit.obo. Each term followed a consistent pattern with definitions, synonyms, parent class (tooth surface structure), and relationships. The 5 commits suggest iterative refinement of the batch.

## Resolution

Medium difficulty because while each individual term follows a standard pattern, the agent must consistently apply the same modeling approach across multiple terms, ensure no duplication, and get the dental anatomy right for each surface type. The batch nature makes it more complex than a single NTR.

## Curation Note (data quality)

**Flagged `case_quality: poor` — `gold_renegotiated_in_pr_comments` (claude-opus-4.7, 2026-05-16).**

The gold PR #3588 is a faithful, single self-contained PR that resolves issue #3583, but it is a **poor metadiff reference** because the human solution was substantially renegotiated *during PR review*, beyond anything the agent could see:

- **Issue #3583 asked for**: 5 terms (distal, incisal, labial, lingual, mesial); definitions in the form "A tooth surface that…"; parent term **`surface structure` (UBERON:0003102)** directly; ORCID 0000-0001-6677-8489.
- **Issue comments added**: discussion that `facial surface` should parent `labial`/`buccal`, and the clinical "F for facial" shorthand (so a `facial`↔`labial` synonym is warranted). Agents legitimately had this.
- **Introduced only in PR review (not visible to agents)**: reviewer @wdduncan (PR comment 2025-08-02) proposed creating a new intermediate grouping class **`tooth surface structure` (UBERON:8600148)**, `is_a surface structure` + `part_of calcareous tooth`, with `synonym "tooth surface" EXACT`, and reparenting every surface term under it. A multi-round label/definition debate followed ("tooth surface" vs "tooth surface structure", whether surfaces are 2D or 3D, adding a buccal-mucosa gloss). The final gold definitions read "A tooth surface **structure** that…" purely because of this review thread. This is the single biggest structural feature of the gold diff and is unreachable from the issue.

Consequently every agent attempt scores low F1 (~0.36–0.38) by construction. The two attempts are in fact substantively strong: both produced the 5 requested terms with near-verbatim definitions, correctly synthesised the facial/labial/buccal hierarchy from the issue comments, attached `part_of calcareous tooth`, and used the correct contributor ORCID. Attempt #318 (sonnet-4.5) even used the literally-requested `surface structure` parent and added `occlusal` (later independently added by humans in PRs #3603/#3633 as UBERON:8600149, vindicating the instinct). The low F1 is driven by (a) the PR-review-only `tooth surface structure` superclass and definition rewording, and (b) the standard placeholder-vs-canonical UBERON ID artifact (UBERON:99xxxxx vs UBERON:86001xx). Downstream scoring should exclude or heavily down-weight this case, or re-score attempts against the issue + issue comments rather than the renegotiated gold.

No companion PRs are needed to reconstruct the issue resolution (PR #3588 alone fully resolved #3583); `companion_prs` is empty. The later occlusal PRs (#3603, #3632, #3633) are independent follow-ups for a different surface and are not part of this issue's resolution.
