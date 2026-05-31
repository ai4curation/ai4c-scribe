---
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10107
issue_title: "[Obsolete] OMIM merges"
issue_created_at: "2025-11-26"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 1
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 11
    deletions: 12
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Clean single-commit term merge following OMIM's upstream consolidation of two muscle-related phenotype entries.
agent_coverage: none
agent_coverage_note: "no eval attempts generated as of 2026-05-15"
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10108, 10109, 10110]
scoring_caveat: "PR #10107 is only the cramps-familial-adolescent (MONDO:0009027 -> MONDO:0007402) sub-step of multi-merge issue #9795; metadiff vs #10107 alone misses the other three OMIM merges. Judge attempts against the issue and the union of #10107+#10108+#10109+#10110."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9795 listed multiple OMIM merges needed in Mondo. This PR merged "cramps, familial adolescent" (MONDO:0009027) into MONDO:0007402 (creatine phosphokinase, elevated serum), following OMIM:218050's merge into OMIM:123320. The OMIM merge reflects that familial adolescent cramps and elevated serum CPK represent the same underlying condition.

## Changes Made

The PR merged MONDO:0009027 into MONDO:0007402 in a single clean commit. The 11 additions and 12 deletions represent the standard merge pattern: obsoleting the source term with replaced_by annotation, transferring synonyms and cross-references to the target term, and removing the source term's classification axioms. The near-equal additions and deletions indicate a straightforward metadata transfer.

## Resolution

Moderate difficulty because term merges always require judgment about which metadata to preserve and how to annotate the merge. However, this specific case was clean because the OMIM upstream merge provides clear justification and the terms had minimal conflicting annotations. An agent could handle this given clear merge SOPs and the ability to identify the source/target terms correctly.

## Curation Note (data quality)

Flagged `case_quality: poor` (`gold_pr_is_partial`) by claude-opus-4.7 on
2026-05-15.

Source issue #9795 ("[Obsolete] OMIM merges") is a **batch request listing
four distinct OMIM-driven term merges**. The curator (@MeeSiing) resolved it
across **four separate PRs**, one per merge:

- #10107 — cramps, familial adolescent (MONDO:0009027) -> MONDO:0007402
  (per OMIM:218050 merged into OMIM:123320) — **this case**
- #10108 — HSAN type 1B (MONDO:0011961) -> MONDO:0044720
  (per OMIM:608088 moved to OMIM:614575, RFC1/CANVAS)
- #10109 — CMT + Friedreich ataxia, combined (MONDO:0010553) -> MONDO:0010549
  (per OMIM:302900 moved to OMIM:302800)
- #10110 — Usher syndrome type 1J (MONDO:0013935) -> MONDO:0012273
  (per OMIM:614869 moved to OMIM:609439)

(Predecessor PR #10071 "Obsolete terms based on OMIM merges" was
closed/superseded.)

The human resolution of issue #9795 is therefore the **union of
#10107+#10108+#10109+#10110**. This case's gold (PR #10107) is only the first
merge sub-step. Per-PR metadiff/F1 computed against #10107 alone will
under-represent any agent that correctly resolves the whole issue, and would
score a complete, correct full-issue resolution as near-zero F1. Same
`gold_pr_is_partial` pattern already flagged for companion case pr10110.

**Coverage gap:** `num_agent_attempts: 0` — no eval attempts exist for this
case as of 2026-05-15 (no `attempts/` subdirectory). This is an eval-coverage
gap, not an agent failure; no agent behavior could be assessed.

**Recommendation:** exclude #10107/#10108/#10109/#10110 from per-PR aggregate
scoring of issue #9795, or generate attempts and score against the four-PR
union and the issue's explicit asks. The CASE_BRIEF MONDO/OMIM IDs for *this*
sub-step (#10107) are accurate; no ID correction needed for this case (see
pr10108/pr10109 Curation Notes for derived-prose ID errors in those cases).

Full case-level review:
`analysis/mondo/results/reviews/pr10107-claude-case-review.md`.
