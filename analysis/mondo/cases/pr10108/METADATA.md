---
repo: monarch-initiative/mondo
issue_number: 9795
pr_number: 10108
issue_title: "[Obsolete] OMIM merges"
issue_created_at: "2025-11-26"
pr_author: MeeSiing
pr_merged_at: "2026-04-02"
pr_num_commits: 4
files_changed:
  - path: src/ontology/mondo-edit.obo
    additions: 36
    deletions: 44
scoping: tightly_scoped
task_type: obsoletion
difficulty: medium
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-10"
rationale: Multi-step term merge that required adding a definition and recovering missing annotations, demonstrating the complexity of merging terms with rich metadata.
agent_coverage: none
agent_coverage_note: "no eval attempts generated as of 2026-05-15"
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10109, 10110]
scoring_caveat: "PR #10108 is only the HSAN-type-1B (MONDO:0011961 -> MONDO:0044720) sub-step of multi-merge issue #9795; metadiff vs #10108 alone misses the other three OMIM merges. Judge attempts against the issue and the union of #10107+#10108+#10109+#10110."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-15"
---

## Context

Issue #9795 listed multiple OMIM merges needed in Mondo. This PR merged "hereditary sensory and autonomic neuropathy type 1B" into MONDO:0044720 (cerebellar ataxia with neuropathy and bilateral vestibular areflexia syndrome). The merge followed OMIM:615490's incorporation into OMIM:614455, reflecting updated understanding that these represent the same SPTLC1-associated condition.

## Changes Made

The PR required 4 commits across multiple contributors. The first commit performed the initial merge. The second added a definition to the surviving term MONDO:0044720, which previously lacked one. The third commit recovered annotations that were accidentally lost during merging. The fourth was a merge with master by a reviewer. The 36 additions and 44 deletions reflect substantial metadata consolidation between two richly annotated neurology terms.

## Resolution

Moderate difficulty due to the iterative nature of the merge. When merging terms with complementary metadata (one has a good definition, the other has good xrefs), the curator must carefully combine both without losing information. The multiple commits show that this process benefits from review, as missing annotations were caught and restored in a follow-up commit.

## Curation Note (data quality)

Flagged `case_quality: poor` (`gold_pr_is_partial`) by claude-opus-4.7 on
2026-05-15.

Source issue #9795 ("[Obsolete] OMIM merges") is a **batch request listing
four distinct OMIM-driven term merges**, resolved by @MeeSiing across **four
separate PRs**, one per merge:

- #10107 — cramps, familial adolescent (MONDO:0009027) -> MONDO:0007402
  (per OMIM:218050 merged into OMIM:123320)
- #10108 — HSAN type 1B (MONDO:0011961) -> MONDO:0044720
  (per OMIM:608088 moved to OMIM:614575, RFC1/CANVAS) — **this case**
- #10109 — CMT + Friedreich ataxia, combined (MONDO:0010553) -> MONDO:0010549
  (per OMIM:302900 moved to OMIM:302800)
- #10110 — Usher syndrome type 1J (MONDO:0013935) -> MONDO:0012273
  (per OMIM:614869 moved to OMIM:609439)

(Predecessor PR #10071 was closed/superseded.)

The human resolution of issue #9795 is the **union of
#10107+#10108+#10109+#10110**. This case's gold (PR #10108) is only the second
merge sub-step. Per-PR metadiff/F1 against #10108 alone will under-represent
any agent that correctly resolves the whole issue. Same `gold_pr_is_partial`
pattern already flagged for companion case pr10110.

**Derived-prose ID error (do not propagate).** The auto-generated CASE_BRIEF
and the Context/Changes prose above state this merge "followed OMIM:615490's
incorporation into OMIM:614455, reflecting ... the same SPTLC1-associated
condition." This is **incorrect**. The issue and PR diff show OMIM:608088 ->
OMIM:614575, and the surviving term MONDO:0044720 is the **RFC1-associated
CANVAS** syndrome (`has_material_basis_in_germline_mutation_in ... RFC1`), not
an SPTLC1/HSAN1A entity. The MONDO IDs (MONDO:0011961 -> MONDO:0044720) and the
merge itself are correct; only the derived OMIM IDs and gene attribution in the
narrative are wrong. CASE_BRIEF is auto-generated and must not be hand-edited;
this note is the durable record of the correction.

**Coverage gap:** `num_agent_attempts: 0` — no eval attempts exist as of
2026-05-15 (no `attempts/` subdirectory). Eval-coverage gap, not an agent
failure.

**Recommendation:** exclude #10107/#10108/#10109/#10110 from per-PR aggregate
scoring of issue #9795, or generate attempts and score against the four-PR
union and the issue's explicit asks. Downstream consumers should not trust the
OMIM IDs / gene in the derived prose for this case.

Full case-level review:
`analysis/mondo/results/reviews/pr10108-claude-case-review.md`.
