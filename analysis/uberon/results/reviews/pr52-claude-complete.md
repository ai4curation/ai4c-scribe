---
ontology: uberon
issue_number: 3682
pr_number: 3683
eval_repo_pr: 52
agent: std_opencode_g55
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

The agent (gpt-5.5 via opencode) produced a diff byte-identical (blob `2e42dc7`) to run #69: UBERON:0002346 label/EXACT-synonym swap, `term_tracker_item` for issue #3682, `has_relational_adjective` updated to `neuroectodermal`, `robot convert` reserialization propagating the `! neuroectoderm` label comments, and a **paraphrased** `terminology_notes` ("neuroectoderm is preferred over neurectoderm; this class excludes placodal ectoderm, which is not classified here"). F1=0.875 slightly under-represents quality: the paraphrase preserves the same substantive content as gold, so the gap is a free-text wording difference, not an omission or error.

## Strengths

- Core ontological change is correct and matches the curator instruction: label/EXACT-synonym swap with the issue referenced via `term_tracker_item`.
- Retained the substantive `terminology_notes` content (placodal ectoderm excluded) — better than run #13's outright deletion.
- Thorough documented validation: read `__issue_context__.json`, inspected the stanza and references with `obo-grep.pl`, used checkout/checkin, ran `robot convert` plus a separate validation conversion to `/tmp`, ran `git diff --check`, and confirmed parents `UBERON:0000923`/`UBERON:0000924` exist.
- Correctly identified **CL:0000133 "neurectodermal cell"** as the corresponding CL follow-up term (matches human-opened obophenotype/cell-ontology#3595) and was explicit that the CL issue could not be opened due to the no-remote-interaction instruction.

## Issues

- Style divergence: `terminology_notes` paraphrased rather than minimally edited. Substantively equivalent; main reason F1 (0.875) is below the verbatim-match group. Normal metadiff under-representation, not a defect.
- Extra edit not in gold: `has_relational_adjective` "neurectodermal"→"neuroectodermal" — defensible consistency improvement.
- `term_tracker_item` datatype `xsd:anyURI` vs gold `xsd:string`: serialization-level convention difference.
- CL follow-up issue not opened — eval-environment restriction, not an agent failure.
