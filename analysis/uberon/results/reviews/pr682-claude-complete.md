---
ontology: uberon
issue_number: 3682
pr_number: 3683
eval_repo_pr: 682
agent: std_opencode_gpt54
model: openai/gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: synonym_update
difficulty: simple
case_quality: good
f1: 0.909
precision: 0.870
recall: 0.952
jaccard: 0.833
outcome: partial_success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent (gpt-5.4 / opencode) produced a near-gold result and is tied with attempt #624
as the strongest non-Opus run on this case (identical blob `1610295`). It performed the
core swap on UBERON:0002346 (`name: neuroectoderm`; `neurectoderm` demoted to
`synonym ... EXACT []`), added a `term_tracker_item` for issue #3682, and correctly
reserialized so all ~14 `! neurectoderm` → `! neuroectoderm` label-comment propagations
across referencing stanzas match the gold diff. The PR comment shows good methodology:
it explicitly describes the checkout → edit → check-in → `robot convert` reserialization
workflow, verifies the stanza with `obo-grep.pl`, confirms only one file changed, and
proactively reports CL:0000133 "neurectodermal cell" for the requested cell-ontology
follow-up. F1=0.909 slightly *under-represents* quality on the propagation work; the one
real residual gap is the un-reworded, now self-contradicting `terminology_notes`.

## Strengths

- Core semantic edit fully correct: label promoted to `neuroectoderm`, `neurectoderm`
  retained as `synonym: "neurectoderm" EXACT []`, issue back-referenced via
  `term_tracker_item` — exactly the maintainer's request.
- Reserialized with `robot convert`, refreshing every stale `! neurectoderm` label
  comment on UBERON:0002346 references (iris muscles, ciliary body, vitreous body,
  hypophysis, neural crest UBERON:0002342, optic vesicle, presumptive structures GCI
  line, insect ventral ectoderm primordium). This is the discriminating step the
  lower-scoring runs missed; this attempt got it right.
- Strong, transparent methodology in the PR comment: documented the ODK term
  checkout/check-in workflow, ran `obo-grep.pl` verification before and after, and
  confirmed the diff is confined to `src/ontology/uberon-edit.obo`.
- Correctly identified **CL:0000133 "neurectodermal cell"** for the CL follow-up
  (matches human-opened obophenotype/cell-ontology#3595); not filing it is an
  eval-environment scope restriction, not a failure.
- Avoided the spurious `has_relational_adjective` rewrite (gold left it as
  `neurectodermal`), so no over-edit on that line.

## Issues

- Under-editing: the `property_value: terminology_notes` line was left as "we prefer
  neurectoderm to neural ectoderm ..." rather than reworded to gold's "we prefer
  neuroectoderm to neural ectoderm ...". The stanza now contradicts its own preferred
  label — a genuine, curator-relevant defect and the main reason F1 is 0.909 not ~1.0.
- Style/datatype: `term_tracker_item ... xsd:anyURI` vs gold/convention `xsd:string`.
  Cosmetic divergence from the gold serialization contributing to the residual
  precision loss.
- Net effect on metadiff: F1 modestly under-represents the (correct) propagation work
  while the terminology-note omission is a real gap. Graded `partial_success`, very
  close to `success`; the only substantive miss is the self-contradicting note.
