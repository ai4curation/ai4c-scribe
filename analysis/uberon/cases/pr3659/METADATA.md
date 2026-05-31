---
repo: obophenotype/uberon
issue_number: 2421
pr_number: 3659
issue_title: "multicellular organism and organism substance should be disjoint"
issue_created_at: "2022-04-15"
pr_author: matentzn
pr_merged_at: "2026-02-11"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 1
    deletions: 0
scoping: tightly_scoped
task_type: axiom_repair
difficulty: medium
scope: multi_term
review_outcome: approved_first_time
domain_area: upper-ontology
tags:
  - disjointness
  - upper-level
  - BFO-alignment
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Minimal one-line disjointness axiom addition requiring understanding of upper-level ontology design and BFO alignment
case_quality: poor
case_quality_reason: owl_serialization_placement_artifact
companion_prs: [3151]
scoring_caveat: "OBO `disjoint_from` is symmetric, so `UBERON:0000468 disjoint_from UBERON:0000463` and `UBERON:0000463 disjoint_from UBERON:0000468` are logically identical. Gold PR #3659 asserts it on the UBERON:0000463 (organism substance) stanza in uberon-edit.obo; the superseded PR #3151 and uberon member anitacaron's explicit in-issue guidance put the equivalent axiom on the UBERON:0000468 stanza in components/external-disjoints.obo. All three agent attempts produced the correct symmetric axiom (opus-4.7 in #264 is byte-identical to gold's stanza/line apart from an added {source=...} provenance qualifier; sonnet-4.5 #299 and haiku-4.5 #174 used the issue-directed external-disjoints.obo placement). Whole-file line metadiff scores F1=0.0 for all attempts purely because of file/stanza/serialization placement and a provenance annotation, not because of any logical error. F1 grossly under-represents quality; all three are substantively correct (success)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #2421 reported that UBERON:0000468 (multicellular organism) and UBERON:0000463 (organism substance) should be declared disjoint, as an organism is not a substance and vice versa. This issue had been open since April 2022, nearly four years before resolution, and an earlier PR #3151 had been superseded by this one.

## Changes Made

The PR added a single disjoint_from axiom to uberon-edit.obo, declaring multicellular organism (UBERON:0000468) disjoint from organism substance (UBERON:0000463). Despite being a one-line change, it required careful reasoning about upper-level ontology categories to ensure the disjointness assertion would not create unintended unsatisfiable classes downstream.

## Resolution

Medium difficulty despite the minimal diff. An agent would need to understand BFO-aligned upper-level ontology categories to assess whether the disjointness assertion is logically sound and would not break downstream inferences. The long gap between issue and resolution (nearly four years) reflects that this kind of foundational change requires careful deliberation. Same-day merge once submitted.

## Curation Note (data quality)

**Flagged poor by claude-opus-4.7 on 2026-05-16. Do not use the F1=0.0 scores at face value for this case.**

This is an **OWL-serialization / placement artifact** case. The requested change is a single symmetric disjointness axiom between `UBERON:0000468` (multicellular organism) and `UBERON:0000463` (organism substance). Because OBO/OWL `disjoint_from` is symmetric, there are several byte-distinct but logically identical ways to serialize it, and the issue thread itself produced *conflicting* placement guidance:

- **Gold PR #3659** (matentzn, merged 2026-02-11): `disjoint_from: UBERON:0000468 ! multicellular organism` added to the **UBERON:0000463 stanza in `src/ontology/uberon-edit.obo`**.
- **Superseded PR #3151** (ddooley, closed — not rejected on merits, just consolidated by #3659): the equivalent axiom on the **UBERON:0000468 stanza in `src/ontology/components/external-disjoints.obo`**. This placement was *explicitly directed by uberon member anitacaron in the issue* ("the disjoint file is at `src/ontology/components/external-disjoints.obo`").

All three agent attempts produced the **correct logical axiom** and are substantively `success`:

- **#264 (opus-4.7)** — byte-identical to gold's file, stanza, and line position; the *only* deviation is an added `{source="https://github.com/obophenotype/uberon/issues/2421"}` provenance qualifier (arguably an improvement over the bare gold line). F1=0.0 here is almost entirely an exact-line-match artifact caused by the provenance annotation.
- **#299 (sonnet-4.5)** and **#174 (haiku-4.5)** — identical to each other (blob `e2a9fc4`); a clean new `[Term]` stanza in `external-disjoints.obo`, i.e. the placement the uberon team directed in the issue and that PR #3151 used. Logically correct; differs from the final gold only by file/stanza convention.

Whole-file line-based metadiff cannot see symmetric-axiom equivalence or cross-file placement equivalence, so it reports F1=0.0 for all three even though none made a logical error. Downstream scoring/aggregation should treat this case as `case_quality: poor` and judge the attempts against the issue's actual ask (a valid disjointness axiom) rather than the single selected gold serialization. Companion PR: #3151.
