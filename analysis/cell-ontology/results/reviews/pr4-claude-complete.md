---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 4
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v2
case_type: axiom_repair
difficulty: medium
f1: 0.667
precision: 0.750
recall: 0.600
jaccard: 0.500
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly removed the CD44-high (`RO_0015015 PR_000001307`) and
CD122-high (`RO_0015015 PR_000001381`) restrictions from the EquivalentClasses
axioms of CL_0001203 and CL_0001204 and removed the marker text from both
definitions — the complete substantive repair. This run used the older
`cl-agent-config@v2` and gpt-5.4. F1 of 0.667 **under-represents** quality;
the recall drop is from the issue-requested 3rd PMID plus a benign EOF
serialization artifact, not an ontological error.

## Strengths

- Both target axioms removed correctly and identically for the CD8 and CD4
  parent classes; all other differentiae preserved.
- Added all three issue-requested PMIDs (24258910, 21926977, 41254224) — more
  complete than gold's two.
- Good methodology narrative: cross-checked the added PMIDs against PubMed/PMC,
  correctly identified the paper titles (e.g. PMID:41254224 = "Guidelines for
  T cell nomenclature", PMID:24258910 = "The who's who of T-cell
  differentiation"), noted consistency with existing child terms, ran
  `robot convert`.

## Issues

- Text deviation: changed "indicated by being CD45RO and CD127-positive" to
  "CD45RO-positive and CD127-positive" for CL_0001203, and added a leading "A"
  to the CL_0001204 definition. Both diverge from the issue's verbatim
  proposed text and from gold. Reasonable copy-edits but lower text-match
  precision.
- **EOF serialization artifact** at line ~35622 (no-op `)` → `)` trailing
  newline). Tooling side-effect, issue-irrelevant, harmless churn.
- The 3rd issue-requested PMID lowers metadiff recall vs gold but is
  issue-compliant — scoring artifact, not a regression.
