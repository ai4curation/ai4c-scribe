---
repo: monarch-initiative/mondo
issue_number: 9859
pr_number: 10219
issue_title: "primary hypophysitis synonyms"
issue_labels:
  - synonym
  - user request
issue_created_at: "2026-01-06"
pr_author: MeeSiing
pr_merged_at: "2026-05-04"
pr_num_commits: 6
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 45
    deletions: 18
scoping: tightly_scoped
scoping_notes: All changes are within the hypophysitis branch of the ontology, restructuring subtypes.
task_type: reclassification
difficulty: hard
scope: multi_term
review_outcome: changes_requested
domain_area: rare-disease
tags:
  - hypophysitis
  - reclassification
  - hierarchy-restructure
  - autoimmune
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Complex hierarchy restructure requiring domain knowledge about hypophysitis subtypes and careful reclassification
case_quality: poor
case_quality_reason: placeholder_id_and_strategy_artifact_deflates_f1
companion_prs: []
scoring_caveat: "Single gold PR (#10219) fully resolves the issue (no companion PRs), but metadiff F1 systematically under-represents quality for every attempt. The maintainer chose to *relabel* the existing MONDO:0019835 to 'lymphocytic hypophysitis'; most agents instead created a NEW lymphocytic hypophysitis term with a placeholder ID (MONDO:7770747). Both are defensible models of the same biology, but the relabel-vs-create-child fork plus the placeholder-vs-canonical ID guarantees a near-total line/ID mismatch on the core change. Judge attempts against the issue text + the MeeSiing/galyea123 comment plan, not the line-level metadiff. Several low-F1 attempts (e.g. #166 R=1.0, #320/#190 R=1.0) have degenerate recall from tiny diffs."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

A user request was filed to update synonyms for primary hypophysitis. However, the resolution required a broader restructuring of the hypophysitis branch. The existing classification conflated primary vs secondary hypophysitis with histological subtypes (lymphocytic, granulomatous, etc.), making the hierarchy confusing.

The issue required domain expertise to determine that histological and anatomical subtypes should be classified as children of hypophysitis rather than maintaining the primary/secondary distinction, which is clinically less useful for classification purposes.

## Changes Made

The PR relabeled MONDO:0019835 to "lymphocytic hypophysitis" and restructured all histological and anatomical subtypes as child terms under the main hypophysitis term. With 6 commits, 45 additions and 18 deletions, this involved modifying multiple term stanzas to correct parent-child relationships and update labels.

## Resolution

This is a hard case because it requires understanding the clinical distinction between primary/secondary hypophysitis and histological subtypes, then making a judgment call about how best to restructure the hierarchy. An agent would need domain knowledge about hypophysitis classification and the ability to reorganize multiple related terms consistently while preserving cross-references.

## Curation Note (data quality)

Flagged `case_quality: poor` by claude-opus-4.7 on 2026-05-15.

The single gold PR (#10219) *is* the whole human resolution — `gh search prs`
on both "9859" and "hypophysitis" returns only #10219, so this is NOT a
partial/multi-PR case (no companion PRs). The agent commits are genuine
agent-authored work (github-actions bot + model author), not leaked gold, and
no attempt scores F1≈1.0 (max 0.259), so there is no gold-leakage artifact.

The case is poor because the metadiff F1 **systematically under-represents
agent quality** for two compounding reasons:

1. **Relabel-vs-create-child modeling fork.** The maintainer (MeeSiing,
   2026-05-01 comment) explicitly chose to *relabel* the existing
   MONDO:0019835 from "primary hypophysitis" to "lymphocytic hypophysitis"
   and add "primary hypophysitis" as a RELATED synonym, putting all subtypes
   directly under MONDO:0021156 hypophysitis. Most agents instead created a
   *new* lymphocytic hypophysitis term as a child of the unchanged
   MONDO:0019835 "primary hypophysitis" grouping. Both faithfully model the
   biology described in the issue and galyea123's classification comment;
   the choice was resolved by maintainer fiat in issue comments, not by
   ontological necessity.

2. **Placeholder-vs-canonical ID artifact.** Agents that created a new term
   assigned the placeholder ID `MONDO:7770747`, which is never reconciled to
   a canonical ID, while the gold reuses the existing `MONDO:0019835`. Every
   new-term line and every reparent line (`is_a: MONDO:7770747 ...`) is then
   scored as a mismatched "extra" edit, capping precision near 0.05–0.17 for
   even the most substantively correct attempts (#459, #280, #45).

Additionally, the lowest-F1 attempts (#166, #320, #190) have **degenerate
recall=1.0** because their diffs are only 1–2 lines, so they cannot contain a
mismatch — recall here is a metadiff degeneracy, not completeness.

Downstream scoring/aggregation should down-weight or exclude line-level
metadiff for this case and judge attempts against the issue text plus the
MeeSiing/galyea123 comment plan. Substantive ranking of the attempts:
#459 (sonnet-4.5, most complete restructure incl. reparenting) >
#45 (gpt-5.5 codex, careful xref relocation) ≈ #280 (kimi, clean minimal
create) > #550/#401 (opus, NARROW + explanatory comment, no structure) >
#85/#65 (gpt-5.5 NARROW only) > #166 (one synonym del + annotation) >
#320/#190 (one synonym del only). All are partial — none reproduced the
full restructure (new MONDO:1060217–1060219 subtype terms, definition
backfill on MONDO:0016534/0019838/0019839/0957423, MONDO:0021156 cleanup).
