---
repo: obophenotype/cell-ontology
issue_number: 3597
pr_number: 3598
issue_title: "[NTR] Add mouth terms for HubMap"
issue_created_at: "2026-03-24"
pr_author: app/copilot-swe-agent
pr_merged_at: "2026-03-26"
pr_num_commits: 3
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 113
    deletions: 0
scoping: loosely_scoped
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: oral
tags:
  - NTR
  - mouth
  - salivary-gland
  - HuBMAP
  - batch-addition
  - oral-tissue
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Batch addition of 8 oral/salivary gland cell types with diverse axiom patterns for HuBMAP tissue annotation
case_quality: ok
case_quality_reason: scoring_artifact_id_offset_and_serialization_order
companion_prs: []
scoring_caveat: "Single clean issue->gold PR mapping (#3598 is the complete approved human resolution; no companion PRs, no contamination/leakage/repudiation). However metadiff F1 severely under-represents quality for 2 of 3 attempts: claude-sonnet-4.5 (eval PR 213, F1=0.091) and claude-opus-4.7 (eval PR 196, F1=0.086) both allocated CL_9900000-CL_9900007 while gold used CL_9900001-CL_9900008 (placeholder/off-by-one CL ID artifact) and inserted the block at a different file location (OWL serialization-order artifact), so whole-line metadiff scores near-zero on substantively near-gold work. claude-haiku-4.5 (eval PR 233, F1=0.697) coincidentally used the same ID range and insertion point as gold, so its score is the only one that tracks substance. Grade all three on substance; do not treat the sonnet/opus ~0.09 F1 as failure."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The HuBMAP consortium requested cell type terms for oral and salivary gland tissue annotation as part of the broader HuBMAP term request effort (#3471). Issue #3597 specified 8 new cell types including serous demilune cells, basal duct cells, periductal fibroblasts, junctional epithelial cells, tuft cells of specific glands, ionocytes, and myoepithelial cells of salivary glands. Each requires specific anatomical contextualization within oral and salivary gland structures.

## Changes Made

Added 113 new lines to `cl-edit.owl` defining 8 new cell types. Each term follows the standard compositional pattern with EquivalentClasses axioms using intersectionOf with a parent cell type and part_of an UBERON anatomical structure. Terms include capability axioms (capable_of GO processes like saliva secretion, ion homeostasis, smooth muscle contraction) and synonym annotations with PMID cross-references as specified in the issue.

## Resolution

Approved on first review in just 3 commits, reflecting efficient implementation. Hard difficulty because the 8 terms span diverse parent cell types (epithelial cells, fibroblasts, ionocytes, myoepithelial cells) each requiring different axiom patterns, and the salivary gland anatomy involves specific UBERON structures (parotid, sublingual, submandibular) that must be correctly referenced.

## Curation Note (data quality)

*Added by claude-opus-4.7 on 2026-05-16 during attempt review.*

This is a **clean, valid evaluation case**, not a poor one in the Step 3a/3b
sense: issue #3597 is a single NTR for 8 terms; PR #3598 is the sole, complete,
human-approved (reviewer: dosumis) resolution; there are **no companion PRs**,
no base-state contamination, no gold leakage, no metadiff-ignored-field-only
gold, no curator repudiation, and no substantive renegotiation in issue/PR
comments (the issue has zero comments; the PR comments are only bot
classified-diff posts and `#gogoeditdiff` triggers).

The caveat is purely a **metadiff scoring artifact** affecting 2 of the 3
attempts and is recorded so downstream aggregation does not misread it as
quality failure:

- **claude-haiku-4.5 (eval PR 233, F1=0.697)** — coincidentally allocated the
  same temporary ID range (CL_9900001–CL_9900008) and the same mid-file
  insertion point as gold, so its F1 genuinely tracks substance. It is the best
  attempt by score *and* substance, though it omitted the `IAO_0000233`
  term_tracker_item present in gold and used bare `SubClassOf` rather than
  gold's `EquivalentClasses` for the compositional terms.
- **claude-sonnet-4.5 (eval PR 213, F1=0.091)** and
  **claude-opus-4.7 (eval PR 196, F1=0.086)** — both produced substantively
  near-gold work (correct parents, UBERON `part_of`, GO `capable_of`,
  synonyms, term_tracker_item; opus additionally ran ROBOT/ELK validation and
  documented its EquivalentClasses-vs-SubClassOf reasoning, which matches gold's
  actual treatment of the periductal and junctional terms). Their near-zero F1
  is a **placeholder/off-by-one CL ID artifact** (they used
  CL_9900000–CL_9900007 vs gold's CL_9900001–CL_9900008 — agents cannot know
  the human's chosen offset) compounded by an **OWL serialization-order
  artifact** (different in-file insertion location). Whole-line metadiff
  therefore craters despite the content being correct.

**Action for scoring/aggregation:** grade all three attempts on substance; treat
the sonnet/opus ~0.09 F1 as an artifact, not a failure. All three reviewed as
`outcome: success`.
