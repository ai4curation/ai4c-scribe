---
ontology: cell-ontology
issue_number: 3454
pr_number: 3555
eval_repo_pr: 18
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 0.600
precision: 0.750
recall: 0.500
jaccard: 0.429
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly removed the CD44-high (`RO_0015015 PR_000001307`) and
CD122-high (`RO_0015015 PR_000001381`) restrictions from the EquivalentClasses
axioms of CL_0001203 and CL_0001204 and removed the marker text from both
definitions — the full substantive repair. F1 of 0.600 is the lowest on the
case but **under-represents** quality: the recall drop is entirely from
defensible/instruction-following extras (3rd issue-requested PMID,
`term_tracker_item`) plus a benign EOF artifact — not from any ontological
error.

## Strengths

- Both target axioms removed correctly and identically for the CD8 and CD4
  parent classes; all other differentiae preserved (parents, CD25, CD45RO,
  CD127, in-taxon, GO_0043379).
- Added all three issue-requested PMIDs (24258910, 21926977, 41254224) — more
  complete than gold's two.
- Added `term_tracker_item` (IAO_0000233 → issue #3454) per config guidance.
- Checked DOSDP patterns (correctly found none applicable), validated with
  `robot convert`; documented checklist.

## Issues

- **Annotation placement**: the `IAO_0000233` term_tracker_item is inserted
  *between* the last `hasExactSynonym` and the `rdfs:label` line, rather than
  grouped with the definition/metadata block as in the cleaner sibling
  attempts (pr70/pr50/pr16 place it right after the definition). Functionally
  equivalent in OWL but stylistically off; this scattered placement is part of
  why metadiff recall is lower (0.500) than the other term_tracker attempts.
- **EOF serialization artifact** at line ~35624 (no-op `)` → `)` trailing
  newline). Tooling side-effect, issue-irrelevant, harmless churn.
- Leading "A" added to CL_0001204 definition (diverges from issue verbatim
  text and gold). Cosmetic.
- The 3rd PMID + term_tracker depress metadiff recall vs gold but are
  defensible/instruction-following — scoring artifact, not a regression. The
  ontological substance is equivalent to the higher-scoring attempts.
