---
ontology: mondo
issue_number: 9795
pr_number: 10109
case_type: obsoletion
difficulty: medium
num_agent_attempts: 0
agent_coverage: none
gold_assessment: sound
case_quality: poor
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

# Case-Level Review: PR #10109 (no agent attempts)

## Status

This is an **eval-coverage gap, not an agent failure**. As of 2026-05-15 the
case has `num_agent_attempts: 0`: no eval attempts were generated in
`ai4curation/eval-ont-agent-mondo`, and the case directory has no `attempts/`
subdirectory and no per-attempt diffs. No agent behavior can be assessed here.
This review covers the source issue, the human gold PR, and dataset readiness.

## Source Issue

[Issue #9795](https://github.com/monarch-initiative/mondo/issues/9795) —
"[Obsolete] OMIM merges" (opened 2025-11-26 by @kanems). A **batch request of
four distinct OMIM-driven merges** (full table reproduced in the pr10107
review). @MeeSiing resolved the whole issue across **four PRs**.

**This case (PR #10109) corresponds to the third table row only**: merge
"Charcot-Marie-Tooth peroneal muscular atrophy and Friedreich ataxia,
combined" (MONDO:0010553) into "Charcot-Marie-Tooth disease X-linked dominant
1" (MONDO:0010549), driven by upstream OMIM:302900 being moved/merged into
OMIM:302800. The issue text's "MONDO:0010553 → MONDO:0010549" mapping matches
the PR exactly.

## Gold PR Assessment

**Step 3a multi-PR check (decisive).** `gh search prs --repo
monarch-initiative/mondo "9795"` returns: #10107, #10108, #10109, #10110 (all
merged) and superseded #10071 (closed). The human resolution of #9795 is the
**union of #10107 + #10108 + #10109 + #10110**; PR #10109 is one of four merge
sub-steps. Scoring an agent against #10109 alone only credits the
MONDO:0010553→MONDO:0010549 merge and would crater F1 on a correct full-issue
resolution — the same `gold_pr_is_partial` pattern flagged for pr10110.

**What the human did in PR #10109 (sub-step is sound).** Two commits by
@MeeSiing: the initial merge (`e36a822`) and a follow-up "fix failed qc"
(`1af63b7`). Approved by @katiermullen ("Looks good! I approve and will
merge"), merged 2026-04-02. The QC-fix commit is consistent with Mondo's
automated checks catching an issue from the first pass (e.g., a synonym/xref
scope or sourcing violation) — a realistic difficulty signal for this case.

Final diff:

- Obsoletes MONDO:0010553: rename to "obsolete Charcot-Marie-Tooth peroneal
  muscular atrophy and Friedreich ataxia, combined", `IAO:0000231
  MONDO:TermsMerged`, `is_obsolete: true`, `replaced_by: MONDO:0010549`,
  strips active axioms (synonym, xrefs MEDGEN:337104, MESH:C564446,
  OMIM:302900 {MONDO:equivalentObsolete}, UMLS:C1844863, the `is_a`, and the
  MalaCards resource).
- Enriches target MONDO:0010549: adds synonym "Charcot-Marie-Tooth peroneal
  muscular atrophy and Friedreich ataxia, combined" EXACT [OMIM:302900];
  transfers xrefs MEDGEN:337104, MESH:C564446, OMIM:302900
  {MONDO:equivalentObsolete}, UMLS:C1844863; marks the retained
  MEDGEN/UMLS records `MONDO:preferredExternal`; tightens many loose
  `RELATED []` / bare-bracket synonyms to `EXACT [OMIM:302800]`; adds
  `IAO:0000233 .../issues/9795` provenance.

This faithfully executes the OMIM:302900→OMIM:302800 consolidation and follows
the standard Mondo merge SOP. The sub-step is **sound**.

**Note — CASE_BRIEF/METADATA minor inaccuracy (do not propagate).** The
auto-generated narrative states the merge "follow[ed] OMIM:214380's merge into
OMIM:302800." The issue and diff show the obsoleted OMIM is **OMIM:302900**
(moved to OMIM:302800), not OMIM:214380. The target/source MONDO IDs
(MONDO:0010553 → MONDO:0010549) are correct; only the OMIM source ID in the
derived prose is wrong. CASE_BRIEF is auto-generated and must not be
hand-edited; the correction is recorded in METADATA.md.

**Companion PRs:** #10107, #10108, #10110 (all merged); predecessor #10071
(closed/superseded).

## Recommendation

- **Case quality: poor (`gold_pr_is_partial`).** Gold is one of four merge
  sub-steps of a batch issue; per-PR metadiff against #10109 alone
  under-represents true performance. Judge against the issue's explicit asks
  and the union of #10107+#10108+#10109+#10110. Mirrors the pr10110 flag.
- **Coverage gap:** no agent attempts exist. Either generate attempts and
  score against the four-PR union, or treat #9795 as a single multi-merge case
  and exclude per-PR scoring of #10107–#10110.
- **Derived-data quality:** the CASE_BRIEF/METADATA OMIM source ID for this
  merge is wrong (OMIM:302900→302800, not OMIM:214380→302800). Recorded in the
  METADATA Curation Note.
