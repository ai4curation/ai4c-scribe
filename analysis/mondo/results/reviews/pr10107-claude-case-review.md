---
ontology: mondo
issue_number: 9795
pr_number: 10107
case_type: obsoletion
difficulty: medium
num_agent_attempts: 0
agent_coverage: none
gold_assessment: sound
case_quality: poor
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

# Case-Level Review: PR #10107 (no agent attempts)

## Status

This is an **eval-coverage gap, not an agent failure**. As of 2026-05-15 the
case has `num_agent_attempts: 0`: no eval attempts were generated in
`ai4curation/eval-ont-agent-mondo` for this source PR, and the case directory
has no `attempts/` subdirectory and no per-attempt diffs. Nothing about agent
behavior can be evaluated here. This review covers only the source issue, the
human gold PR, and dataset readiness.

## Source Issue

[Issue #9795](https://github.com/monarch-initiative/mondo/issues/9795) —
"[Obsolete] OMIM merges" (opened 2025-11-26 by @kanems). The issue is a
**batch request listing four distinct OMIM-driven term merges**, presented as
a table with a source Mondo term, its ID, and an upstream-OMIM justification,
plus a "Suggested term to consider" mapping for each:

| Source Mondo | Suggested target | OMIM justification |
|---|---|---|
| MONDO:0009027 cramps, familial adolescent | MONDO:0007402 | OMIM:218050 merged into OMIM:123320 (CPK, elevated serum) |
| MONDO:0011961 HSAN type 1B | MONDO:0044720 | OMIM:608088 moved to OMIM:614575 (CANVAS) |
| MONDO:0010553 CMT + Friedreich ataxia, combined | MONDO:0010549 | OMIM:302900 moved to OMIM:302800 |
| MONDO:0013935 Usher syndrome type 1J | MONDO:0012273 | OMIM:614869 moved to OMIM:609439 |

@MeeSiing committed in-thread (2026-04-01) to "create PR to merge all these
terms." She resolved the issue not with one PR but with **four separate PRs**,
one per merge.

**This case (PR #10107) corresponds to the first table row only**: merge
"cramps, familial adolescent" (MONDO:0009027) into "creatine phosphokinase,
elevated serum" (MONDO:0007402), driven by OMIM:218050 being merged upstream
into OMIM:123320.

## Gold PR Assessment

**Step 3a multi-PR check (decisive).** `gh search prs --repo
monarch-initiative/mondo "9795"` returns five PRs:

- #10107 (merged) — cramps, familial adolescent → MONDO:0007402 *(this case)*
- #10108 (merged) — HSAN type 1B → MONDO:0044720
- #10109 (merged) — CMT + Friedreich ataxia → MONDO:0010549
- #10110 (merged) — Usher syndrome type 1J → MONDO:0012273
- #10071 (closed, superseded) — "Obsolete terms based on OMIM merges"

So the human resolution of issue #9795 is the **union of #10107 + #10108 +
#10109 + #10110**. PR #10107 is exactly one of the four merge sub-steps. Any
metadiff scoring an agent against #10107 alone would only credit the
MONDO:0009027→MONDO:0007402 merge and would mark a correct, complete,
issue-wide resolution as near-zero F1 — the same `gold_pr_is_partial` pattern
already flagged for the companion case pr10110.

**What the human did in PR #10107 (the sub-step itself is sound).** Single
clean commit `c88ca0f` by @MeeSiing, approved first time by @sabrinatoro
("Looks good"), merged 2026-04-02. The diff is a textbook Mondo term-merge:

- Obsoletes MONDO:0009027: renames to "obsolete cramps, familial adolescent",
  adds `property_value: IAO:0000231 MONDO:TermsMerged`, `is_obsolete: true`,
  `replaced_by: MONDO:0007402`, drops the active synonym/xref/`is_a` axioms.
- Transfers metadata onto target MONDO:0007402: adds synonym "cramps, familial
  adolescent" EXACT [OMIM:218050]; adds xref MEDGEN:347475, xref OMIM:218050
  {source="MONDO:equivalentObsolete"}, and xref UMLS:C1857533; tightens the
  surviving term's loose `RELATED []` synonyms to `EXACT [OMIM:123320]`; adds
  the `IAO:0000233 .../issues/9795` provenance pointer.

This faithfully executes the OMIM:218050→OMIM:123320 consolidation and follows
the standard Mondo merge SOP (TermsMerged + replaced_by, xref provenance
sourced as `MONDO:equivalentObsolete`). The sub-step is **sound**.

**Companion PRs:** #10108, #10109, #10110 (all merged); predecessor #10071
(closed/superseded).

## Recommendation

- **Case quality: poor (`gold_pr_is_partial`).** The gold for this case is one
  of four merge sub-steps of a batch issue. Any metadiff/F1 computed against
  PR #10107 alone under-represents true performance and must not be used to
  score agents on issue #9795. Judge against the issue's explicit asks and the
  union of #10107+#10108+#10109+#10110. This mirrors the existing pr10110
  poor-case flag.
- **Coverage gap:** no agent attempts exist for this case. To get usable
  signal, either (a) generate attempts and score against the four-PR union, or
  (b) exclude #10107/#10108/#10109/#10110 from per-PR aggregate scoring and
  treat #9795 as a single multi-merge case.
- The CASE_BRIEF narrative for the sub-step is accurate (correct MONDO/OMIM
  IDs). No correction needed for this case's IDs.
- Metadata updated in METADATA.md (curator-only): `agent_coverage: none`,
  `case_quality: poor`, `companion_prs`, `scoring_caveat`.
