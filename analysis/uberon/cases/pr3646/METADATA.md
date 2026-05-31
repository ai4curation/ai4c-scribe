---
repo: obophenotype/uberon
issue_number: 3464
pr_number: 3646
issue_title: "Positioning 'life cycle' and 'life cycle stage' under 'process'"
issue_labels:
  - uberon-classhierarchy
issue_created_at: "2025-01-17"
issue_closed_at: "2026-01-12"
pr_author: matentzn
pr_merged_at: "2026-01-12"
pr_num_commits: 1
files_changed:
  - path: src/ontology/uberon-edit.obo
    additions: 2
    deletions: 0
scoping: tightly_scoped
task_type: reclassification
difficulty: hard
scope: multi_term
review_outcome: approved_first_time
domain_area: upper-ontology
tags:
  - COB-alignment
  - life-cycle
  - upper-ontology
  - root-class
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Upper-level ontology restructuring requiring understanding of COB alignment and root class implications
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [3532, 3647]
scoring_caveat: "metadiff vs #3646 only covers a deliberate intermediate step (adds two has_ontology_root_term header declarations). The substantive semantic work the issue requested — reparenting UBERON:0000104/0000105 to BFO:0000015 (process) and deprecating UBERON:0000000 (processual entity) — was done in companion PR #3647 (with prior COB-comment groundwork in #3532). All 3 attempts score F1=0 by construction; judge them against the issue and the union of #3532+#3646+#3647."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

As part of aligning Uberon with the Core Ontology for Biology (COB), "life cycle stage" and "life cycle temporary boundary" needed to be repositioned as root classes. This was an intermediate step before deprecating the "processual entity" class in a subsequent PR. The issue was open for nearly a year, indicating significant deliberation about the structural change.

## Changes Made

Added two lines to uberon-edit.obo to establish life cycle stage and life cycle temporary boundary as top-level classes. This minimal change has significant structural implications because it sets up the subsequent deprecation of processual entity.

## Resolution

Hard difficulty because changes to root-level ontology structure have cascading effects on the entire class hierarchy. The agent must understand the COB alignment strategy, know that these classes will become true roots once processual entity is deprecated, and ensure the change does not break existing reasoning. Despite the tiny diff, this required a year of discussion.

## Curation Note (data quality)

**Flagged poor: `gold_pr_is_partial`.** This is a multi-PR human resolution and the
selected gold PR is only a deliberate sub-step, so every agent scores F1=0 by
construction regardless of correctness.

Issue #3464 asks to reposition `life cycle` (UBERON:0000104) and `life cycle stage`
(UBERON:0000105) from `processual entity` (UBERON:0000000) to `process`
(`BFO:0000015`) for COB compatibility; the comment thread additionally raises
obsoleting the 4 vestigial "life cycle temporal boundary" terms
(UBERON:0035943/0035944/0035945/0035946).

The human resolved this across **three** PRs:

- **#3532** (2025-05): added the COB-alignment `comment:` and `seeAlso` COB#51 to
  UBERON:0000000 (groundwork).
- **#3646** (gold, 2026-01-12): adds only two header lines —
  `has_ontology_root_term UBERON:0000105` and `... UBERON:0035943`. The PR body
  states verbatim: *"This is an intermediate step... I am breaking the task down...
  in the next PR, I am getting rid of processual entity, which will make it so."*
  It shares **zero substantive lines** with the issue's actual ask.
- **#3647** (2026-01-23): the real work — obsoletes UBERON:0000000
  ("obsolete processual entity", `is_obsolete: true`), reparents UBERON:0000104 and
  UBERON:0000105 to `is_a: BFO:0000015 ! process`, and moves
  `life cycle temporal boundary` (UBERON:0035943) to `is_a: BFO:0000001 ! entity`.

Consequently the metadiff vs #3646 is meaningless for this issue. Judged against
the issue and the union #3532+#3646+#3647:

- **pr177 (haiku-4.5)** — best attempt; its 2 hunks reparenting UBERON:0000104/0000105
  to `BFO:0000015 ! process` are byte-identical to the corresponding hunks in
  human PR #3647. Graded `success`.
- **pr303 (sonnet-4.5)** — valid alternative mechanism: renames UBERON:0000000 in
  place to "process" with `BFO:0000015` xref + retained synonym; achieves COB
  alignment, differs from the human's obsolete-and-reparent approach. `partial_success`.
- **pr263 (opus-4.7)** — obsoletes the 4 vestigial temporal-boundary terms with good
  obsoletion hygiene and explicit scope rationale; responsive to the issue
  discussion but skips the title's primary reparenting ask. `partial_success`.

Flagged by claude-opus-4.7 on 2026-05-16.
