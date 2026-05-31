---
repo: obophenotype/cell-ontology
issue_number: 3550
pr_number: 3563
issue_title: "Move Lugaro (species neutral) under PLI, in line with WMB classification"
issue_created_at: "2026-01-07"
issue_closed_at: "2026-02-19"
pr_author: copilot-swe-agent
pr_merged_at: "2026-02-19"
pr_num_commits: 9
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 8
    deletions: 5
scoping: tightly_scoped
task_type: reclassification
difficulty: medium
scope: single_term
review_outcome: changes_requested
domain_area: neuroscience
tags:
  - reclassification
  - Lugaro-cell
  - Purkinje-layer
  - interneuron
  - cerebellar
  - WMB
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Reclassification with reviewer-requested changes, demonstrating iterative agent-reviewer interaction on hierarchy decisions
case_quality: poor
case_quality_reason: gold_build_regenerated_noise
companion_prs: []
scoring_caveat: "Gold PR #3563 diff is dominated by non-issue noise: 3 unrelated build-regenerated GO Declaration lines (GO_0002288, GO_0070999, GO_1904320) and 3 OWL serialization-order annotation-property header comment relabelings (hasDbXref/hasExactSynonym/hasNarrowSynonym). Only ~4 of ~13 gold-changed lines are issue-relevant (the CL_0011006 SubClassOf reparent + the soma-location UBERON_0002956->UBERON_0002979 change). Metadiff precision is structurally capped at 0.154 for all attempts; F1 ~0.25-0.27 severely under-represents quality. Judge attempts against the issue ask + the issue-relevant SubClassOf hunk only."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Lugaro cell (CL:0011006) was classified under the generic interneuron class (CL:0000099), but the Whole Mouse Brain (WMB) atlas and literature support classifying it as a Purkinje layer interneuron (PLI). This reclassification aligns the cell ontology with current neuroscience classification standards.

## Changes Made

Modified `cl-edit.owl` with 8 additions and 5 deletions. The primary change replaces the SubClassOf axiom from generic interneuron to Purkinje layer interneuron. Additional changes include updating the definition to reference the Purkinje layer location and adding supporting literature references.

## Resolution

The PR received a CHANGES_REQUESTED review before being approved on a second round. The reviewer (dosumis) requested adjustments to the reclassification, demonstrating the kind of iterative refinement common when agents propose hierarchy changes that require expert neuroscience knowledge. Medium difficulty due to the need to understand cerebellar cortex layer organization and interneuron classification systems.

## Curation Note (data quality)

`quality_flagged_by: claude-opus-4.7` · `quality_flagged_at: 2026-05-16`

This is a **poor evaluation case** for metadiff scoring (`case_quality: poor`,
`case_quality_reason: gold_build_regenerated_noise`). Inspection of gold PR
#3563's final diff shows it is dominated by changes unrelated to the issue:

1. **ODK/build-regenerated noise** — three spurious `Declaration(Class(...))`
   lines for unrelated GO classes (`GO_0002288`, `GO_0070999`, `GO_1904320`).
   The PR's own auto-generated "unreasoned" gogoeditdiff comment lists these GO
   classes as anomalously "Added", and reviewer **dosumis** explicitly
   commented on the PR: *"Diff weirdness may be artefact of update issues?
   Might need to reserialise master + branch versions of edit file."* No agent
   could or should reproduce these.
2. **OWL serialization-order artifact** — three annotation-property header
   comment relabelings (`hasDbXref`, `hasExactSynonym`, `hasNarrowSynonym`:
   e.g. `database_cross_reference` → `has cross-reference`), unrelated to
   Lugaro cell and produced by ROBOT re-serialization of `cl-edit.owl`.

Only ~4 of the gold's ~13 changed lines are issue-relevant: the
`CL_0011006 SubClassOf CL_0000099 → CL_4072102` reparent and the
`has soma location` change `UBERON_0002956 (granular layer) → UBERON_0002979
(Purkinje cell layer)`. Because metadiff scores against the whole gold diff,
precision is structurally capped at 0.154 for **every** attempt regardless of
correctness, and F1 (~0.25–0.27) severely under-represents agent quality.

Additionally, the soma-location refinement only entered the gold via the PR
**review thread** (dosumis CHANGES_REQUESTED: add `has soma location some
UBERON_0002979` and let the reasoner classify). Agents were given only the
issue body + curator comment (which asked for the direct reparent to
CL:4072102), not the review thread, so the missed soma-location update is a
defensible omission rather than an agent failure.

All three attempts (#209 sonnet-4.5, #148 haiku-4.5, #275 opus-4.7) correctly
made the primary requested reparent with clean, well-scoped edits and should
be judged against the issue's actual ask, not the contaminated metadiff.
