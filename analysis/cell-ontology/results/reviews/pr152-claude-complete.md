---
ontology: cell-ontology
issue_number: 3479
pr_number: 3526
eval_repo_pr: 152
agent: std_claude_hai45
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: axiom_repair
difficulty: medium
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

claude-haiku-4.5 (claude runtime) produced a diff that is byte-identical to
the merged gold PR #3526 for issue #3479 on `CL:4023063` (medial ganglionic
eminence derived interneuron). The F1=1.0 is genuine and accurately
represents quality — verified against `gh pr diff 3526`, the agent's hunk
(blob `3b1912a`) matches the human's hunk line-for-line, including the
revised definition text, the added `PMID:19709629` xref, and the two
`SubClassOf RO_0002292` (expresses) axioms to ncbigene/26468 (LHX6) and
ncbigene/55553 (SOX6). The smallest model in the cohort solved this case
perfectly.

## Strengths

- Exact reproduction of the gold definition revision: appended "In mice and
  humans, it expresses LHX6 and SOX6." while preserving the existing
  `DOI:10.1101/2022.10.12.511898` xref and adding `PMID:19709629` as a
  second definition xref — matching the curator's choice of supporting
  reference.
- Correct marker formalization: two `SubClassOf(obo:CL_4023063
  ObjectSomeValuesFrom(obo:RO_0002292 <http://identifiers.org/ncbigene/26468>))`
  and `.../ncbigene/55553>)` axioms, using the `expresses` relation
  (RO_0002292) and NCBIGene identifiers — exactly the gold pattern.
- Correctly resolved the gene symbols to identifiers: 26468 = LHX6,
  55553 = SOX6 (confirmed by the gold PR's gogoeditdiff bot output, which
  labels these as LHX6 and SOX6).
- Tightly scoped: only `src/ontology/cl-edit.owl` touched, only the
  `CL:4023063` block edited, no collateral edits, no EOF noise.
- Accurate PR comment correctly naming the term, gene IDs, references, and
  the RO_0002292 representation.

## Issues

- None. The diff is identical to the curator-approved gold (approved
  first-time by dosumis, a core CL maintainer). F1 is fully representative.
