---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 525
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
restrictions from the `EquivalentClasses` axioms of both CL_0001203 and CL_0001204,
and removed "CD44-high, and CD122-high" from both `IAO_0000115` definitions. This
attempt is **byte-identical to attempt #585** (same blob `83fa1bd`, same gpt-5.4 /
opencode configuration). The reported F1=0.667 (P=0.750, R=0.600) **inverts the
quality signal**: this is a known poor case (`gold_incomplete_vs_issue_caps_metadiff`)
where gold PR #3555 omitted PMID:41254224, and this attempt is penalized precisely for
being *more faithful to the issue* by adding all three requested PMIDs. Substantively a
**success**.

## Strengths

- **Core repair fully correct.** Both `RO_0015015` PR-restriction conjuncts (CD44-high
  PR_000001307, CD122-high PR_000001381) removed from the CL_0001203 and CL_0001204
  `EquivalentClasses` axioms; remaining intersection conjuncts (CL_4030046
  PR_000001380, RO_0002104 PR_000001017/PR_000001869, RO_0002162 NCBITaxon_9606,
  RO_0002353 GO_0043379) preserved intact.
- **More issue-faithful than gold.** Added all three issue-requested references
  alongside existing ones — PMID:21926977, PMID:24258910, **and PMID:41254224** —
  whereas gold omitted the third. Existing xrefs (including GO_REF:0000031,
  PMID:20146720, ISBN:0781735149, the immgen URL) preserved per the issue's "do not
  replace existing references" instruction.
- **Definition text cleaned correctly.** Both definitions end at "CD25-negative." with
  no residual mouse-marker clause, matching the issue's improved definitions.
- **Tight scope.** Single file `src/ontology/cl-edit.owl`; only the two target
  stanzas substantively changed.
- **No term_tracker_item churn.** No `IAO_0000233` link added, avoiding the further
  metadiff penalty (F1 0.600) and landing on the clean issue-compliant F1=0.667
  plateau.

## Issues

- **Benign EOF serialization artifact.** A no-op trailing-newline change at
  ~line 35622 from the editing tooling; issue-irrelevant, no ontological effect.
- **CL_0001204 definition prefixed with "A " (style).** "A CD4-positive, alpha-beta
  long-lived T cell..." vs gold's "CD4-positive...". This matches the issue's improved
  wording, so it is an issue-aligned divergence from gold rather than an error.
- **Metadiff under-represents quality.** F1=0.667 reflects the partial-gold artifact
  (precision capped at 0.750 because gold lacks PMID:41254224; recall reduced by the
  issue-compliant 3rd-PMID line), not a correctness shortfall. Note: PR #525 has no
  agent PR/issue comment captured in the attempt file (only the diff), so methodology
  narrative is inferred from the identical #585 run; the diff itself is complete and
  correct.
