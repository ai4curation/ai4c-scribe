---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 19
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/cl-agent-config@v3
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
definitions — the full substantive repair. Output blob (`83fa1bd`) is
identical to pr33 (same codex/gpt-5.5 config). F1 of 0.667
**under-represents** quality; the recall drop is from the issue-requested 3rd
PMID plus a benign EOF serialization artifact, not an ontological error.

## Strengths

- Both target axioms removed correctly and identically for the CD8 and CD4
  parent classes; all other differentiae preserved.
- Added all three issue-requested PMIDs (24258910, 21926977, 41254224) — more
  complete than gold's two.
- Definition texts kept close to issue verbatim wording (no spurious leading
  "A", "CD45RO and CD127-positive" preserved).
- Strong documented methodology: retrieved publication metadata/abstracts via
  Europe PMC for all three PMIDs (full text for PMID:21926977), ran
  `robot convert` and `git diff --check`.

## Issues

- **EOF serialization artifact** at line ~35622: a no-op `)` → `)` hunk adding
  a trailing newline at end of file. Tooling side-effect, issue-irrelevant,
  harmless but gratuitous churn. Not a substantive error.
- The 3rd issue-requested PMID lowers metadiff recall vs gold but is
  issue-compliant — scoring artifact, not a regression.
- Identical to pr33 (repeat run, same config) — consistent and correct, no
  independent signal.
