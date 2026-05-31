---
ontology: mondo
issue_number: 9795
pr_number: 10108
case_type: obsoletion
difficulty: medium
num_agent_attempts: 0
agent_coverage: none
gold_assessment: sound
case_quality: poor
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

# Case-Level Review: PR #10108 (no agent attempts)

## Status

This is an **eval-coverage gap, not an agent failure**. As of 2026-05-15 the
case has `num_agent_attempts: 0`: no eval attempts were generated in
`ai4curation/eval-ont-agent-mondo`, and the case directory has no `attempts/`
subdirectory and no per-attempt diffs. No agent behavior can be assessed here.
This review covers the source issue, the human gold PR, and dataset readiness.

## Source Issue

[Issue #9795](https://github.com/monarch-initiative/mondo/issues/9795) —
"[Obsolete] OMIM merges" (opened 2025-11-26 by @kanems). A **batch request of
four distinct OMIM-driven merges** (full table reproduced in the pr10107 and
pr10109 reviews). @MeeSiing resolved the whole issue across **four PRs**.

**This case (PR #10108) corresponds to the second table row only**: merge
"hereditary sensory and autonomic neuropathy type 1B" (MONDO:0011961) into
"cerebellar ataxia with neuropathy and bilateral vestibular areflexia
syndrome / CANVAS" (MONDO:0044720), driven by the upstream OMIM consolidation
(OMIM:608088 → OMIM:614575). The issue text's "MONDO:0011961 → MONDO:0044720"
mapping matches the PR exactly.

## Gold PR Assessment

**Step 3a multi-PR check (decisive).** `gh search prs --repo
monarch-initiative/mondo "9795"` returns: #10107, #10108, #10109, #10110 (all
merged) and superseded #10071 (closed). The human resolution of #9795 is the
**union of #10107 + #10108 + #10109 + #10110**; PR #10108 is one of four merge
sub-steps. Scoring an agent against #10108 alone only credits the
MONDO:0011961→MONDO:0044720 merge and would crater F1 on a correct full-issue
resolution — the same `gold_pr_is_partial` pattern flagged for pr10110.

**What the human did in PR #10108 (sub-step is sound, but iterative).** Four
commits by @MeeSiing plus a master-merge by reviewer @sabrinatoro. Review
history is informative: @sabrinatoro first issued **CHANGES_REQUESTED**
("There is a lot of information that wasn't moved to the term that was kept"),
@MeeSiing replied "I overlooked those and have added them back," and Sabrina
then **APPROVED**. Merged 2026-04-02.

Final diff:

- Obsoletes MONDO:0011961: rename to "obsolete hereditary sensory and
  autonomic neuropathy type 1B", `IAO:0000231 MONDO:TermsMerged`,
  `is_obsolete: true`, `replaced_by: MONDO:0044720`, strips active axioms
  (def, ~10 subsets, ~9 synonyms, ~11 xrefs incl. OMIM:608088, two `is_a`).
- Enriches target MONDO:0044720: **adds a full textual definition** (the
  surviving CANVAS term previously lacked one) cited to [OMIM:614575,
  Orphanet:504476]; transfers the HSAN1B synonyms, xrefs (DOID:0070148,
  GARD:0016958, ICD10CM:G60.8, MEDGEN:330880, MESH:C564296, OMIM:608088
  {MONDO:equivalentObsolete}, Orphanet:139564, SCTID:717825008,
  UMLS:C1842586), the two HSAN `is_a` parents, and provenance pointers
  including `IAO:0000233 .../issues/9795`.

This is a substantively richer merge than #10107 (two heavily annotated
neurology terms with complementary metadata: one had the good xref/synonym set,
the other needed a definition). The CHANGES_REQUESTED → fix → APPROVED cycle
shows the human's first pass *did* drop annotations and they were recovered on
review — a realistic difficulty signal. The final merged state is **sound**.

**Note — CASE_BRIEF/METADATA factual error (do not propagate).** The
auto-generated CASE_BRIEF and METADATA narrative state the merge "followed
OMIM:615490's incorporation into OMIM:614455, reflecting ... the same
SPTLC1-associated condition." This is **wrong**: the issue and diff show
OMIM:608088 → OMIM:614575, and the surviving term MONDO:0044720 is the
RFC1-associated CANVAS syndrome (`has_material_basis_in_germline_mutation_in
... RFC1`), not an SPTLC1 condition. SPTLC1/HSAN1A is a different entity. The
sub-step itself is correct; only the derived prose is inaccurate. CASE_BRIEF
is auto-generated and must not be hand-edited; the correction is recorded in
METADATA.md.

**Companion PRs:** #10107, #10109, #10110 (all merged); predecessor #10071
(closed/superseded).

## Recommendation

- **Case quality: poor (`gold_pr_is_partial`).** Gold is one of four merge
  sub-steps of a batch issue; per-PR metadiff against #10108 alone
  under-represents true performance. Judge against the issue's explicit asks
  and the union of #10107+#10108+#10109+#10110. Mirrors the pr10110 flag.
- **Coverage gap:** no agent attempts exist. Either generate attempts and
  score against the four-PR union, or treat #9795 as a single multi-merge case
  and exclude per-PR scoring of #10107–#10110.
- **Derived-data quality:** the CASE_BRIEF/METADATA OMIM IDs and gene for this
  merge are wrong (OMIM:608088→614575, RFC1/CANVAS — not OMIM:615490→614455 /
  SPTLC1). Recorded in the METADATA Curation Note so downstream consumers do
  not trust the derived prose.
