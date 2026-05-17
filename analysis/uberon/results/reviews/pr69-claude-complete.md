---
ontology: uberon
issue_number: 3682
pr_number: 3683
eval_repo_pr: 69
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: synonym_update
difficulty: simple
f1: 0.875
precision: 0.913
recall: 0.840
jaccard: 0.778
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent (gpt-5.5 via pi/opencode) performed the requested UBERON:0002346 label/EXACT-synonym swap, added `term_tracker_item` for issue #3682, updated `has_relational_adjective` to `neuroectodermal`, and reserialized with `robot convert` (blob `2e42dc7`, identical to run #52). It differs from the top group only in that it **paraphrased** `terminology_notes` ("neuroectoderm is preferred over neurectoderm; this class excludes placodal ectoderm, which is not classified here") instead of using the gold wording. F1=0.875 slightly *under-represents* quality: the paraphrase preserves the same substantive content (placodal ectoderm excluded), so this is a stylistic free-text difference, not an omission or error.

## Strengths

- Core ontological change is correct and matches the curator instruction: label/EXACT-synonym swap, issue referenced via `term_tracker_item`.
- Crucially, **retained** the substantive content of `terminology_notes` (placodal ectoderm is deliberately excluded) — unlike run #13 which deleted the note entirely. The reworded note is arguably clearer than the original.
- Ran the checkout/checkin workflow plus `robot convert`, so the ~14 mechanical `! neuroectoderm` label-comment propagations match gold (recall 0.840).
- Correctly identified **CL:0000133 "neurectodermal cell"** as the corresponding CL follow-up term (matches human-opened obophenotype/cell-ontology#3595).

## Issues

- Style divergence: `terminology_notes` was paraphrased rather than minimally edited as the human did. Substantively equivalent, but the free-text wording difference is the main reason F1 (0.875) is below the verbatim-match group (0.917). This is normal metadiff under-representation, not a defect.
- Extra edit not in gold: `has_relational_adjective` "neurectodermal"→"neuroectodermal" — defensible consistency improvement.
- `term_tracker_item` datatype `xsd:anyURI` vs gold `xsd:string`: serialization-level convention difference.
- CL follow-up issue not opened — eval-environment restriction, not an agent failure.
