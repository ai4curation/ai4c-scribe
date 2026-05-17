---
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10109
issue_title: "[Obsolete] OMIM merges"
issue_created_at: "2025-11-26"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 2
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 20
    deletions: 21
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Complex neurology term merge requiring QC fix, reflecting the challenge of merging terms with overlapping but distinct clinical phenotypes.
agent_coverage: none
agent_coverage_note: "no eval attempts generated as of 2026-05-15"
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10110]
scoring_caveat: "PR #10109 is only the CMT+Friedreich-ataxia (MONDO:0010553 -> MONDO:0010549) sub-step of multi-merge issue #9795; metadiff vs #10109 alone misses the other three OMIM merges. Judge attempts against the issue and the union of #10107+#10108+#10109+#10110."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9795 identified several OMIM entries that had been merged upstream and needed corresponding merges in Mondo. This PR specifically merged "Charcot-Marie-Tooth peroneal muscular atrophy and Friedreich ataxia, combined" into MONDO:0010549, following OMIM:214380's merge into OMIM:302800. The conditions share overlapping neuropathy features but were historically maintained as separate entries.

## Changes Made

The PR required 2 commits: the initial merge operation and a subsequent QC fix. The merge obsoleted one term and transferred its metadata (synonyms, xrefs, definitions) to MONDO:0010549. The 20 additions and 21 deletions reflect the standard merge pattern: adding replaced_by annotations, transferring cross-references, and removing the obsoleted term's active axioms. The QC failure in the first commit likely involved a missing annotation or invalid axiom pattern that automated checks caught.

## Resolution

Moderate difficulty because neurology term merges require understanding whether two clinical presentations truly represent the same underlying disease entity. The OMIM merge provides strong evidence, but the curator must still correctly execute the merge procedure and handle any QC issues that arise from combining annotation sets from different provenance sources.

## Curation Note (data quality)

Flagged `case_quality: poor` (`gold_pr_is_partial`) by claude-opus-4.7 on
2026-05-15.

Source issue #9795 ("[Obsolete] OMIM merges") is a **batch request listing
four distinct OMIM-driven term merges**, resolved by @MeeSiing across **four
separate PRs**, one per merge:

- #10107 — cramps, familial adolescent (MONDO:0009027) -> MONDO:0007402
  (per OMIM:218050 merged into OMIM:123320)
- #10108 — HSAN type 1B (MONDO:0011961) -> MONDO:0044720
  (per OMIM:608088 moved to OMIM:614575, RFC1/CANVAS)
- #10109 — CMT + Friedreich ataxia, combined (MONDO:0010553) -> MONDO:0010549
  (per OMIM:302900 moved to OMIM:302800) — **this case**
- #10110 — Usher syndrome type 1J (MONDO:0013935) -> MONDO:0012273
  (per OMIM:614869 moved to OMIM:609439)

(Predecessor PR #10071 was closed/superseded.)

The human resolution of issue #9795 is the **union of
#10107+#10108+#10109+#10110**. This case's gold (PR #10109) is only the third
merge sub-step. Per-PR metadiff/F1 against #10109 alone will under-represent
any agent that correctly resolves the whole issue. Same `gold_pr_is_partial`
pattern already flagged for companion case pr10110.

**Derived-prose ID error (do not propagate).** The auto-generated CASE_BRIEF
and the Context/Changes prose above state this merge "follow[ed] OMIM:214380's
merge into OMIM:302800." The issue and PR diff show the obsoleted upstream
entry is **OMIM:302900** (moved to OMIM:302800), not OMIM:214380. The MONDO IDs
(MONDO:0010553 -> MONDO:0010549) and the merge itself are correct; only the
OMIM source ID in the derived narrative is wrong. CASE_BRIEF is auto-generated
and must not be hand-edited; this note is the durable record of the correction.

**Coverage gap:** `num_agent_attempts: 0` — no eval attempts exist as of
2026-05-15 (no `attempts/` subdirectory). Eval-coverage gap, not an agent
failure.

**Recommendation:** exclude #10107/#10108/#10109/#10110 from per-PR aggregate
scoring of issue #9795, or generate attempts and score against the four-PR
union and the issue's explicit asks. Downstream consumers should not trust the
OMIM source ID in the derived prose for this case.

Full case-level review:
`analysis/mondo/results/reviews/pr10109-claude-case-review.md`.
