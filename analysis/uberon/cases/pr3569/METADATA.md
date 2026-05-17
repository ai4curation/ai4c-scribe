---
repo: obophenotype/uberon
issue_number: 3457
pr_number: 3569
issue_title: "Track the addition of VCCF vasculature terms here"
issue_created_at: "2024-12-24"
pr_author: ar-ibrahim
pr_merged_at: "2025-07-03"
pr_num_commits: 6
files_changed:
  - path: src/patterns/data/default/artery_and_arteriole_pattern.tsv
    additions: 4
    deletions: 0
  - path: src/patterns/data/default/vein_and_venule_pattern.tsv
    additions: 3
    deletions: 0
  - path: src/patterns/definitions.owl
    additions: 106
    deletions: 2
scoping: tightly_scoped
task_type: new_term
difficulty: medium
scope: multi_term
review_outcome: changes_requested
domain_area: vascular-anatomy
tags:
  - VCCF
  - vasculature
  - DOSDP-pattern
  - artery
  - vein
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Pattern-based vasculature term addition using DOSDP templates, part of a multi-PR series for VCCF integration
case_quality: poor
case_quality_reason: workflow_and_id_scheme_mismatch_plus_base_contamination
companion_prs: [3497, 3513, 3559, 3566]
scoring_caveat: "Gold PR #3569 implements the 7-term June-24-2025 tracker batch via the DOSDP pattern-data workflow (artery_and_arteriole_pattern.tsv + vein_and_venule_pattern.tsv -> regenerated src/patterns/definitions.owl) with canonical UBERON:8920049-8920055 IDs and contributor ORCID 0000-0001-6757-4744. The agent CLAUDE.md instructs the uberon-edit.obo + terms/ checkout workflow with placeholder UBERON:99xxxxx IDs. Instruction-following obo-route attempts therefore score F1=0 by construction (different file, different IDs). The obo-route attempts are additionally polluted by an identical foreign base-state hunk (seeAlso/source annotation reordering on flying-fish/hyoid/etc. terms + airway-hillock relationship reorder; blobs dda7aa8 / 7e174bf / aaf65e4). Judge attempts against the issue's June 24 batch and the union of companion PRs #3497/#3513/#3559/#3566, not the line-wise metadiff vs #3569."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

Issue #3457 tracked the addition of vasculature terms from the Vasculature Common Coordinate Framework (VCCF) into Uberon. This was the fifth PR in a series (following PRs #3497, #3513, #3559, #3566) adding batches of arterial and venous terms. Seven new terms were added in this installment.

## Changes Made

The PR added four new entries to the artery_and_arteriole_pattern.tsv and three to the vein_and_venule_pattern.tsv DOSDP pattern data files. The definitions.owl file was updated with 106 new lines containing the generated logical definitions and annotations for the new vasculature terms, linking them to their anatomical regions via supplies/drains relationships.

## Resolution

Medium difficulty. An agent would need to understand the DOSDP (Dead Simple OWL Design Patterns) framework used for systematic vasculature term creation, populate the correct pattern data TSV files with appropriate anatomical region references, and ensure the generated OWL definitions are consistent with existing vasculature terms. The six commits and multi-PR series suggest iterative review feedback across the batch import effort.

## Curation Note (data quality)

Flagged `case_quality: poor` (claude-opus-4.7, 2026-05-16).

**Workflow / ID-scheme mismatch.** Issue #3457 is a HuBMAP/VCCF tracking ticket resolved by five batched human PRs (#3497, #3513, #3559, #3566, #3569). The selected gold #3569 is a clean, self-contained sub-batch (the 7 terms in the June 24 2025 comment: lobar artery of spleen, esophageal branches of left gastric artery, posterior scrotal artery, vaginal artery, superior rectal vein, inferior rectal vein, posterior scrotal vein), so the *task* is well-defined and not "gold is partial" in the disqualifying sense. The problem is mechanism: gold #3569 edits the **DOSDP pattern-data TSVs** (`src/patterns/data/default/artery_and_arteriole_pattern.tsv`, `vein_and_venule_pattern.tsv`) and regenerates `src/patterns/definitions.owl`, assigning canonical `UBERON:8920049`–`8920055` and contributor ORCID `0000-0001-6757-4744` (Arwa Ibrahim). The agent `CLAUDE.md` in `uberon-agent-config@v3` instead prescribes the `uberon-edit.obo` + `terms/` checkout workflow and `UBERON:99xxxxx` placeholder IDs. An agent that faithfully follows its instructions therefore scores **F1 = 0 by construction** (different target file, different IDs) even when the anatomical content is correct. Only the codex attempt (#34, F1 0.626) discovered the pattern-TSV route and reused the canonical 8920xxx IDs.

**Base-state contamination.** The obo-route attempts (#323, #253, #189, #93, #71, #54; blobs `dda7aa8`/`7e174bf`/`aaf65e4`) additionally carry an identical foreign hunk unrelated to the issue: `seeAlso`/`source` annotation reordering on flying-fish wing, hyoid bone, spinal accessory nerve, manual digits, spleen marginal sinus and lateral malleolus, plus an `airway hillock` (UBERON:8910024) `part_of`/`has_part` reorder — robot-reserialization churn leaked into the eval base.

**Recommendation for scoring/aggregation.** Down-weight or exclude the line-wise metadiff vs #3569 for this case. Judge attempts against the issue's June 24 batch and the union of companion PRs #3497/#3513/#3559/#3566. The two haiku runs (#189, #93) still fail on substance (no terms created; out-of-scope harness-config edits); opus #253 fails on substance (added the wrong, already-handled April 30 lung batch); codex #34 substantively succeeds; sonnet #323 and the opencode pair #71/#54 are substantively partial successes (correct batch and anatomy, one wrong arterial parent, wrong workflow/IDs).
