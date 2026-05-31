---
repo: obophenotype/uberon
issue_number: 3604
pr_number: 3607
issue_title: "dGTEx terms needed in Uberon"
issue_labels:
  - new term request
issue_created_at: "2025-08-29"
issue_closed_at: "2025-09-11"
pr_author: dragon-ai-agent
pr_merged_at: "2025-09-11"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 13
    deletions: 0
scoping: mostly_scoped
scoping_notes: >-
  The issue requested multiple dGTEx terms but this PR only addresses the kidney
  interpolar region. Other terms from the same issue were handled in separate PRs.
task_type: new_term
difficulty: medium
scope: single_term
review_outcome: approved_first_time
domain_area: renal-anatomy
tags:
  - new-term
  - kidney
  - dGTEx
  - renal
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: NTR from a multi-term request showing how a single term is carved out and addressed independently
case_quality: ok
case_quality_reason: robot_convert_reserialization_churn_penalizes_instruction_following
scoring_caveat: >-
  Whole-file metadiff over-penalizes the attempt (#255/opus, F1=0.615) that
  followed the agent config's mandated `robot convert -f obo` reserialization
  step: that step refreshes `!` label comments for unrelated referenced terms
  (CL:0000649, GO:0098643) from the current import closure, adding 3 cosmetic
  hunks that crater recall to 0.471. This is NOT eval-base contamination
  (hunks appear only in #255, not #166/#287). Substantively all three attempts
  correctly add UBERON kidney interpolar region; judge on term content, not
  recall. Separately, gold #3607 used `[Wikipedia:Kidney]` as the def source
  despite the issue body explicitly pointing at NCIT:C186124, so attempts
  #287/#255 that added `xref: NCIT:C186124` are arguably more source-faithful
  than gold and should not be marked down for the resulting recall loss.
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

The dGTEx (developmental Genotype-Tissue Expression) project needed several anatomical terms added to Uberon. This PR addressed one of those terms: the kidney interpolar region, which is the central portion of the kidney between the upper and lower poles.

## Changes Made

Added UBERON:7770009 "kidney interpolar region" with synonyms ("central pole of kidney", "interpolar region of kidney"), a definition, is_a organ part classification, and part_of kidney relationship. Attribution was included via ORCID for the requesting contributor.

## Resolution

Medium difficulty because the agent must understand renal anatomy well enough to define the interpolar region correctly and place it in the partonomy. The term also needed proper contributor attribution. This was one term from a multi-term request, so the agent needed to scope appropriately.

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-16 after detailed review of all three
attempts. `case_quality: ok` (not `poor`) — the case is a legitimate,
well-scoped NTR and gold #3607 is the complete, sole resolution for this term
(no companion PRs; other dGTEx terms in issue #3604 are out of scope for this
PR by design). The flag records two scoring caveats so downstream aggregation
does not misread the F1 spread:

1. **robot-convert reserialization churn (primary).** The uberon-agent-config
   `CLAUDE.md` explicitly instructs agents to reserialize
   `src/ontology/uberon-edit.obo` with `robot convert ... -f obo` before
   committing. Attempt #255 (opus-4.7) did exactly this; the reserialization
   refreshed `!` label comments on two unrelated referenced terms
   (`CL:0000649` "prickle cell"→"spinous cell of epidermis"; `GO:0098643`
   "banded collagen fibril"→"fibrillar collagen", x2) from the current import
   closure. These 3 cosmetic comment-only hunks (IDs/axioms unchanged) drop
   #255's recall to 0.471 / F1 to 0.615. They appear ONLY in #255, not in
   #166/#287, so this is reserialization churn, not eval-base contamination.
   Net effect: whole-file metadiff most penalizes the attempt that most
   faithfully followed its documented instructions. All three attempts produce
   a substantively correct kidney interpolar region term.

2. **Gold def-source choice is weaker than two attempts.** Issue #3604's body
   explicitly states the definition "is already defined in NCIT ...
   NCIT_C186124", yet gold #3607 paraphrased and cited `[Wikipedia:Kidney]`
   with no NCIT xref. Attempts #287 and #255 added `xref: NCIT:C186124`
   (and #255 used NCIT's verbatim definition + the NCIT "Kidney, Middle"
   synonym), which is arguably more provenance-correct than gold. The recall
   loss they incur for this extra (correct) cross-reference should be read as
   an improvement over gold, not as scope creep.

Reviewer verdict per attempt: #166 (haiku, F1 0.889) success — best,
gold-equivalent; #287 (sonnet, F1 0.842) success — gold-equivalent + better
NCIT provenance; #255 (opus, F1 0.615) success substantively — most
source-faithful, F1 artifact of mandated reserialization, only minor real
issue is the missing `! Deanne Taylor` label on `dc-contributor`.
