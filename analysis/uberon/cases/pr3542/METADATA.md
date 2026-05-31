---
repo: obophenotype/uberon
issue_number: 3495
pr_number: 3542
issue_title: "epithelium and lamina propria for GI tract"
issue_labels:
  - new term request
  - high-priority
  - GutCellAtlas
issue_created_at: "2025-03-18"
issue_closed_at: "2025-05-27"
pr_author: cmungall
pr_merged_at: "2025-05-27"
pr_num_commits: 5
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 88
    deletions: 9
scoping: mostly_scoped
scoping_notes: >-
  The issue requested both epithelium and lamina propria terms for GI tract segments.
  This PR addresses the lamina propria portion; epithelium terms were in a separate PR.
task_type: new_term
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: gastrointestinal-anatomy
tags:
  - new-term
  - lamina-propria
  - GI-tract
  - GutCellAtlas
  - batch-NTR
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Large batch NTR following a compositional pattern across seven gut segments, requiring consistent axiom construction
case_quality: poor
case_quality_reason: placeholder_id_artifact_plus_reserialization_churn
companion_prs: [3541]
scoring_caveat: >-
  Issue #3495 was resolved by two human PRs: #3541 (4 colon epithelium terms)
  and #3542 (7 lamina propria terms, the gold here). Gold #3542 is correctly
  scoped to the lamina-propria sub-task per @dosumis (issue-comment-2896247830),
  so attempts that ALSO add epithelium terms are doing companion PR #3541's
  work. Beyond that, metadiff F1 systematically under-represents quality for
  three case-wide reasons: (1) every agent used a placeholder ID range
  (UBERON:99xxxxx / 77xxxxx / 8600051-57) whereas gold uses canonical
  UBERON:8600134-140 — a pure unpredictable ID artifact; (2) gold #3542
  contains ~9 lines of robot-convert reserialization churn (annotation-attr
  reordering, `property_value: seeAlso` repositioning) from @dosumis's
  "reserialised" commit, unrelated to the issue; (3) the ORCID definition
  dbxref + dcterms-date requirement only arrived in a late issue comment
  (2913353220, 2025-05-27) after most runs. Judge attempts on substance:
  seven lamina propria terms with genus UBERON:0000030, correct part_of
  targets, the requested definition pattern, and NO duplicated asserted
  part_of (per @dosumis) — not on the line-level metadiff.
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The Gut Cell Atlas project needed lamina propria terms for seven gut segments (ascending colon, descending colon, sigmoid colon, transverse colon, stomach, caecum, and rectum). Each term follows a compositional pattern: "The lamina propria that underlies the epithelial lining of the {gut segment}."

## Changes Made

Added seven new lamina propria terms to uberon-edit.obo with 88 lines of additions. Each term included a definition following the compositional pattern, appropriate synonyms, is_a classification under lamina propria, and part_of relationships to the specific gut segment. Some existing term stanzas were also updated (9 deletions).

## Resolution

Hard difficulty due to the scale and consistency requirements. The agent must create seven parallel term stanzas, each following the same compositional pattern but with segment-specific relationships. It must correctly identify the parent lamina propria class, use the right part_of targets for each colon region, and ensure no inconsistencies across the batch. This was a high-priority request from an external project.

## Curation Note (data quality)

Flagged `case_quality: poor` for **metadiff scoring purposes only** — the gold
PR #3542 is itself correct and well-scoped; the problem is that line-level
metadiff systematically under-represents agent quality on this case.

**Multi-PR resolution.** Issue #3495 asked for both epithelium and lamina
propria terms. The human resolved it with two PRs: **#3541** (4 colon
epithelium terms) and **#3542** (7 lamina propria terms — the gold for this
case). @dosumis's issue-comment-2896247830 explicitly scopes the lamina
propria request that PR #3542 fulfils. Agents that *also* added the four colon
epithelium terms (pr67, pr50, pr99, pr31) are reproducing companion PR #3541's
deliverable, which legitimately answers the issue but is out of scope for the
#3542 gold and is therefore penalised by metadiff as scope creep. The
well-scoped lamina-propria-only attempts are pr247 (claude-opus-4.7), pr82
(gpt-5.4 codex), and pr317 (claude-sonnet-4.5).

**Three case-wide metadiff distortions** (independent of agent quality):

1. **Placeholder-vs-canonical ID artifact.** Gold uses UBERON:8600134-140.
   Every agent used an unpredictable placeholder range (UBERON:9900001-7,
   UBERON:9900000-10, UBERON:7700001-11, or UBERON:8600051-57) per the
   project's documented placeholder convention. The agent cannot predict the
   canonical IDs the curator will assign; this alone caps F1 well below 1.0
   for every attempt.
2. **robot-convert reserialization churn.** Gold #3542 carries ~9 lines of
   non-issue churn from @dosumis's "reserialised" commit: annotation-attribute
   reordering (`{source=, seeAlso=}` → `{seeAlso=, source=}`) on unrelated
   terms (UBERON:0001638, UBERON:0012260/61/62, etc.) and the
   `property_value: seeAlso "...COB/issues/51"` line moved below the
   `relationship:` block on UBERON:0000003. Agents that ran `robot convert`
   (pr67/pr50/pr82/pr31) incidentally reproduce only the first `seeAlso` hunk;
   agents that did not (pr247/pr317/pr99) reproduce none. Either way this is
   serialization noise, not issue content.
3. **Late-arriving requirement.** The ORCID definition dbxref
   (`https://orcid.org/0000-0003-4389-9821`) and the
   `dcterms-date "2025-05-27T17:07:22Z"` only appeared in
   issue-comment-2913353220 (2025-05-27), after most agent runs. Attempts
   could not have known to use them, and the gold's own sigmoid-colon dbxref
   carries a human typo (`...4389-98219`, an extra "9") that persisted to
   master.

**Net.** Judge attempts on substance — seven lamina propria terms with genus
UBERON:0000030, correct segment-specific part_of targets
(UBERON:0001156/0001157/0001158/0001159/0000945/0001153/0001052), the
requested definition pattern, both synonym forms, and NO duplicated asserted
`relationship: part_of` (per @dosumis) — not on the compressed metadiff F1.
pr247 (F1 0.695) is substantively a clean success despite scoring < 0.7.
