---
repo: obophenotype/cell-ontology
issue_number: 3239
pr_number: 3245
issue_title: "remove tendon cell and otic fibrocyte from under fibrocyte"
issue_created_at: "2025-08-11"
issue_closed_at: "2025-08-19"
pr_author: Caroline-99
pr_merged_at: "2025-08-19"
pr_num_commits: 3
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 14
    deletions: 14
scoping: tightly_scoped
diff_noise: noisy
diff_noise_notes: "Protege serialization artifacts: CL_4072017/CL_4072018 declaration and stanza reordering, oboInOwl:hasDbXref comment label change. Only 2 of 5 diff hunks are real changes."
task_type: reclassification
difficulty: medium
scope: multi_term
review_outcome: multiple_rounds
domain_area: connective-tissue
tags:
  - reclassification
  - fibrocyte
  - tendon-cell
  - otic-fibrocyte
  - hierarchy-fix
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Multi-term reclassification with review feedback, requiring domain knowledge about fibrocyte vs fibroblast lineage distinctions
case_quality: poor
case_quality_reason: gold_incomplete_plus_serialization_noise
companion_prs: []
scoring_caveat: "Gold PR #3245 is the only PR for issue #3239, but it is an INCOMPLETE and NOISY reference: (a) it omits the two otic fibrocyte synonyms the issue explicitly requested (cochlear fibrocyte PMID:31866825, spiral ligament fibrocyte PMID:33193034) — deferred to issue #3246; (b) it adds an unrequested PMID:37894875 to the tendon cell def xref; (c) it leaves the stale inferred SubClassOf(CL_0000388 CL_0000135) pointing at the old fibrocyte parent; (d) 3 of its 5 diff hunks are pure Protege serialization noise (CL_4072017/CL_4072018 declaration+stanza reorder, hasDbXref comment-label change) that agents working from a normalized base cannot and should not reproduce. Net effect: metadiff F1 (0.24–0.41 across all 8 attempts) systematically UNDER-represents agent quality. Judge attempts against the issue text, not the line-level metadiff."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Tendon cell and otic fibrocyte were incorrectly classified as children of fibrocyte in the CL hierarchy. Despite the name "otic fibrocyte," these cells are biologically distinct from true fibrocytes (which are quiescent fibroblast-derived cells). The otic fibrocytes of the spiral ligament and tendon cells needed to be moved to more appropriate parent classes.

## Changes Made

Modified 14 lines and added 14 lines in `cl-edit.owl`, changing the SubClassOf axioms for tendon cell and otic fibrocyte to remove them from under fibrocyte and place them under more appropriate parent classes. The equal addition/deletion count reflects the reclassification nature: removing old parent assertions and adding correct ones.

## Resolution

This PR went through multiple rounds of review, with changes requested before final approval. The reviewer flagged concerns about the reclassification, leading to iterative refinement. Medium difficulty because correctly reclassifying these cells requires understanding the biological distinction between fibrocytes (fibroblast-derived quiescent cells) and cells that merely have "fibrocyte" in their name due to historical convention.

## Curation Note (data quality)

Flagged `case_quality: poor` on 2026-05-16 (claude-opus-4.7) after detailed
review of all 8 attempts against issue #3239 and gold PR #3245.

PR #3245 is the *only* PR resolving issue #3239 (companion-PR search confirms
no other PR references #3239; PRs #3409/#3410/#3522 are the explicitly
deferred "separate ticket" work and belong to issue #3246, out of scope
here). However the gold reference is both **incomplete** and **noisy**:

1. **Gold under-resolves the issue.** Issue #3239 explicitly asks for two
   otic fibrocyte synonyms — "cochlear fibrocyte" (PMID:31866825) and
   "spiral ligament fibrocyte" (PMID:33193034). The merged gold PR adds
   *neither*; the curator deferred synonym/relabel work to issue #3246.
   All 8 attempts correctly followed the issue and added these synonyms,
   so they are penalized by metadiff for *correctly* doing what the issue
   asked.
2. **Gold has an out-of-scope extra edit.** Gold adds PMID:37894875 (a 2023
   tendon-aging review) to the tendon cell definition xref and substantially
   rewords the definition prose — neither requested by the issue. This caps
   well-scoped agents below 1.0 on precision.
3. **Gold leaves a stale axiom.** Gold retargets only the
   `EquivalentClasses` for tendon cell to fibroblast (CL_0000057) but leaves
   `SubClassOf(Annotation(is_inferred "true") CL_0000388 CL_0000135)` still
   pointing at fibrocyte. Agents that fixed this (pr86, pr55, pr37, pr79,
   pr171) are *more* internally consistent than gold yet score lower.
4. **Serialization noise dominates the diff.** 3 of gold's 5 hunks are pure
   Protege artifacts (CL_4072017/CL_4072018 declaration + stanza reorder, and
   an `oboInOwl:hasDbXref` comment-label change "database_cross_reference" →
   "has cross-reference"). Agents editing a normalized base file cannot and
   should not reproduce these, structurally capping recall.

Consequence: every attempt scores F1 in a compressed 0.24–0.41 band that
**systematically under-represents** quality. The substantive reclassification
work (tendon cell → fibroblast; otic fibrocyte → mesenchymal cell CL_0008019)
was done correctly by all 8 attempts. The strongest attempts on substance
(pr86 haiku-4.5, pr55/pr37 gpt-5.5 opencode, pr171 opus-4.7) are *more*
complete and internally consistent than the gold itself. Downstream scoring
should down-weight or exclude this case, or re-score against the issue text
rather than the line-level metadiff. No gold leakage / bot-commit / placeholder
artifact was found — gold commits are genuine human work by Caroline-99 with
RiveraAndrea83 review.
