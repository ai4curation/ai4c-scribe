---
ontology: cell-ontology
issue_number: 3521
pr_number: 3583
eval_repo_pr: 494
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: other
difficulty: simple
f1: 0.634
precision: 1.0
recall: 0.464
jaccard: 0.464
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This is a byte-identical re-run of attempt #556 (same gpt-5.5/opencode model,
same result blob `7b7cba8`). The agent added a
`rdfs:seeAlso obo:CL_xxxx <https://celltype.info/project/544/dataset/1157>`
assertion annotated with `Annotation(rdfs:label "reference transcriptomic data
on Cell Annotation Platform")` to all 13 listed bipolar neuron terms — matching
the final merged gold's predicate and IRI syntax exactly — plus an
`obo:IAO_0000233` term-tracker annotation to issue #3521 on each. The metadiff
F1 of 0.634 (precision 1.000, recall 0.464) **under-represents quality**: all
gold lines are reproduced exactly; recall is reduced only by the 13 gold-absent
tracker extras and the documented poor-case caveat
(`gold_renegotiated_in_pr_comments`).

## Strengths

- All 13 required terms updated exactly (CL_0000748, CL_0000751, CL_4033019,
  CL_4033027–CL_4033036) — complete, no omissions.
- Selected the gold's *final* predicate and IRI syntax (`rdfs:seeAlso <...>`),
  matching post-renegotiation gold despite that form not being derivable from
  the supplied issue context; rdfs:label string is verbatim to gold.
- Reproducible: identical to #556, indicating a stable, deterministic solution
  for this systematic batch-annotation task.
- Tight scope on `cl-edit.owl`; correctly deferred NS-Forest markers (blocked
  on upstream CellMark PR #56).

## Issues

- The `obo:IAO_0000233` tracker on all 13 terms is a gold-absent extra
  (defensible standard CL provenance practice, but the sole substantive
  divergence from gold and the only cause of reduced recall).
- "Extend definition text (standard pattern)" sub-ask not addressed —
  defensible, as the gold PR also did not edit definitions and the issue gives
  no pattern example.
- F1=0.634 is a poor-case scoring artifact; substantively a clean success. See
  the case `METADATA.md` curation note.
