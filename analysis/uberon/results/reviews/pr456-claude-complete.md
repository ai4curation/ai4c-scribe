---
ontology: uberon
issue_number: 3682
pr_number: 3683
eval_repo_pr: 456
agent: std_opencode_kimik26
model: togetherai/moonshotai/Kimi-K2.6
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: synonym_update
difficulty: simple
case_quality: good
f1: 0.286
precision: 0.174
recall: 0.800
jaccard: 0.167
outcome: partial_success
failure_modes:
  - missed_requirement
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent (kimi-k2.6 / opencode, iteration 1) performed the *core* semantic edit on the
UBERON:0002346 stanza correctly — `name` swapped to `neuroectoderm`, `neurectoderm`
demoted to `synonym ... EXACT []`, and a `term_tracker_item` added for issue #3682 — but
it did **not** reserialize with `robot convert`, so the ~14 mechanical
`! neurectoderm` → `! neuroectoderm` label-comment propagations across referencing
stanzas (surface ectoderm UBERON:0000076-area, iris dilator/sphincter, ciliary body
UBERON:0002295, vitreous body, hypophysis, neural crest UBERON:0002342, optic vesicle,
etc.) are entirely absent. It also left the `terminology_notes` unchanged so it still
reads "we prefer neurectoderm to neural ectoderm", now directly contradicting the new
label. F1=0.286 (precision 0.174) heavily *over-penalizes* relative to the substantive
ontological correctness of the central edit — this is mostly a `robot convert`
reserialization artifact — but it also reflects two genuine gaps (stale propagated
comments and the self-contradicting note) that a curator would reject on review.

## Strengths

- The semantically load-bearing changes are all correct: `name: neuroectoderm`,
  `neurectoderm` demoted to `synonym: "neurectoderm" EXACT []`, issue referenced via
  `term_tracker_item`. This is exactly what the maintainer asked for in the issue thread
  ("please swap label and exact synonym, reference this issue").
- Tightly scoped to the single intended stanza; no spurious edits to unrelated terms.
- Correctly identified **CL:0000133 "neurectodermal cell"** as the candidate for the
  requested cell-ontology follow-up and surfaced it in the comment — matching the
  human-opened obophenotype/cell-ontology#3595. The "did not open the CL issue" note is
  an eval-environment scope restriction, not an agent failure.

## Issues

- Missed requirement (completeness): no `robot convert` reserialization, leaving ~14
  stale `! neurectoderm` label comments on UBERON:0002346 references throughout
  uberon-edit.obo. These are auto-generated comments so the asserted ontology is
  correct, but the gold PR (and the high-scoring gpt-5.4 runs) refreshed them; the
  diff is therefore materially incomplete versus the human resolution. This is the
  dominant cause of the low F1/precision.
- Under-editing: the `property_value: terminology_notes "we prefer neurectoderm to
  neural ectoderm ..."` line was left intact. Gold reworded it to "we prefer
  neuroectoderm to neural ectoderm ..."; leaving the old wording produces a stanza
  that contradicts its own preferred label — a real defect, not a metadiff artifact.
- Style/datatype: used `term_tracker_item ... xsd:anyURI` whereas gold and curator
  convention use `xsd:string`; also placed the property between the synonym block and
  the xref block rather than adjacent to the other `property_value` lines near the
  terminology note. Minor, but it diverges from house style and the gold serialization.
- Net effect on metadiff: F1 strongly over-represents failure (the central content is
  correct and the propagation gap is auto-generated comment churn), but two substantive
  omissions remain, so this is graded `partial_success` rather than `success`.
