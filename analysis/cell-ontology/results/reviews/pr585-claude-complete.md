---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 585
agent: std_opencode_gpt54
model: openai/gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.667
precision: 0.750
recall: 0.600
jaccard: 0.500
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_incomplete_vs_issue_caps_metadiff
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly and completely performed the core axiom repair requested in
issue #3454: it removed the mouse-specific CD44-high (`ObjectSomeValuesFrom(obo:RO_0015015
obo:PR_000001307)`) and CD122-high (`ObjectSomeValuesFrom(obo:RO_0015015 obo:PR_000001381)`)
restrictions from the `EquivalentClasses` axioms of both CL_0001203 (CD8-positive,
alpha-beta memory T cell, CD45RO-positive) and CL_0001204 (CD4-positive, alpha-beta
memory T cell, CD45RO-positive), and removed "CD44-high, and CD122-high" from both
`IAO_0000115` definitions. The reported F1=0.667 (P=0.750, R=0.600) **inverts the
quality signal**: this is a known poor case (`gold_incomplete_vs_issue_caps_metadiff`)
where gold PR #3555 omitted PMID:41254224, and this attempt is penalized precisely for
being *more faithful to the issue* by adding all three requested PMIDs. Substantively a
**success**.

## Strengths

- **Core repair fully correct.** Both `RO_0015015` PR-restriction conjuncts (CD44-high
  PR_000001307, CD122-high PR_000001381) removed from CL_0001203 and CL_0001204
  `EquivalentClasses` axioms; the remaining intersection (CL_4030046 PR_000001380,
  RO_0002104 PR_000001017/PR_000001869, RO_0002162 NCBITaxon_9606, RO_0002353
  GO_0043379) is left intact and correct.
- **More issue-faithful than gold.** Added all three references the issue explicitly
  requested "along existing ones" — PMID:21926977, PMID:24258910, **and
  PMID:41254224** (the "Guidelines for T cell nomenclature" paper the issue flagged
  for its Table 4 marker list). Gold omitted the third; this attempt complied with the
  issue text. Existing xrefs (GOC:tfm, GO_REF:0000031, PMID:20146720 for CL_0001203;
  GOC:add, GOC:tfm, GO_REF:0000031, ISBN:0781735149, immgen URL for CL_0001204) were
  preserved, exactly as instructed ("do not replace existing references").
- **Definition text cleaned correctly.** Both definitions now terminate at
  "CD25-negative." with no residual mouse-marker clause, matching the issue's improved
  definitions.
- **Tight scope.** Only `src/ontology/cl-edit.owl` touched; only the two target
  stanzas changed. The agent self-reported running `git diff --check` and verifying
  the diff was limited to the two class stanzas.
- **No term_tracker_item churn.** Did not add an `IAO_0000233` link, so it avoids the
  further metadiff penalty (F1 0.600) seen on config-compliant attempts; result is the
  clean F1=0.667 plateau driven solely by the issue-compliant 3rd PMID.

## Issues

- **Benign EOF serialization artifact.** A no-op trailing-newline change at
  ~line 35622 (`)` with "No newline at end of file" → `)` plus newline) from the
  editing tooling. Issue-irrelevant churn that whole-file metadiff can over-weight; no
  ontological effect.
- **CL_0001204 definition prefixed with "A " (style).** The agent rewrote the
  CL_0001204 definition opening as "A CD4-positive, alpha-beta long-lived T cell...",
  whereas gold retained "CD4-positive, alpha-beta long-lived T cell...". This actually
  matches the issue's improved-definition wording ("A CD4-positive, alpha-beta
  long-lived T cell..."), so it is a defensible, issue-aligned divergence from gold,
  not an error.
- **Metadiff under-represents quality.** F1=0.667 reflects the partial-gold artifact
  (precision capped at 0.750 because gold lacks PMID:41254224; recall reduced by the
  issue-compliant 3rd-PMID line), not any correctness shortfall. Judge against the
  issue text and the union of the two axiom removals + both definition edits + three
  PMIDs — all of which this attempt satisfied.
