---
ontology: uberon
issue_number: 3682
pr_number: 3683
eval_repo_pr: 624
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

The agent (gpt-5.4 / opencode) is among the strongest attempts on this case. It performed
the core swap on UBERON:0002346 (`name: neuroectoderm`, `neurectoderm` demoted to
`synonym ... EXACT []`), added a `term_tracker_item` for issue #3682, **and** correctly
reserialized so that all ~14 `! neurectoderm` → `! neuroectoderm` label-comment
propagations across referencing stanzas (surface ectoderm, iris dilator/sphincter,
ciliary body, vitreous body, hypophysis, neural crest UBERON:0002342, optic vesicle,
presumptive neural plate/CNS GCI line, insect ventral ectoderm, etc.) match the gold
diff line-for-line. The blob is identical to attempt #682 (`1610295`). F1=0.909 slightly
*under-represents* quality on the mechanical-propagation dimension (that work is fully
correct), and the residual gap is real but small: the `terminology_notes` was not
reworded, leaving a self-contradiction, and the `term_tracker_item` datatype differs
from gold.

## Strengths

- Core semantic edit fully correct and exactly as the maintainer requested in the issue
  thread: label promoted to `neuroectoderm`, `neurectoderm` retained as
  `synonym: "neurectoderm" EXACT []`, issue back-referenced.
- Performed the `robot convert` reserialization, so every stale `! neurectoderm` label
  comment on UBERON:0002346 references was refreshed — matching gold on the changes that
  the lower-scoring kimi/sonnet/haiku runs missed entirely. This is the discriminating
  step on this case and the agent got it right.
- Tightly scoped: only `src/ontology/uberon-edit.obo` touched, no collateral edits to
  unrelated terms.
- Did **not** spuriously rewrite `has_relational_adjective` (gold also left it as
  `neurectodermal`), so it avoided an over-edit some runs made.

## Issues

- Under-editing: did not reword `property_value: terminology_notes` from "we prefer
  neurectoderm to neural ectoderm ..." to gold's "we prefer neuroectoderm to neural
  ectoderm ...". The stanza now contradicts its own preferred label. This ~1-line
  omission is the principal reason F1 is 0.909 rather than ~1.0 and is a genuine
  (if minor) curator-relevant defect.
- Style/datatype: emitted `term_tracker_item ... xsd:anyURI`; gold and curator
  convention use `xsd:string`. Cosmetic but a real divergence from the gold
  serialization and contributes to the residual precision loss.
- Net effect on metadiff: F1 modestly under-represents quality on the propagation work
  (correct but counted line-by-line), while the terminology-note omission is a real gap.
  Graded `partial_success` (very close to `success`) — the only substantive miss is the
  self-contradicting note.
