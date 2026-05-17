---
ontology: uberon
issue_number: 3682
pr_number: 3683
eval_repo_pr: 14
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: synonym_update
difficulty: simple
f1: 0.917
precision: 0.957
recall: 0.880
jaccard: 0.846
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent (gpt-5.5 via the pi/opencode runtime) produced a diff byte-identical (blob `86183ac`) to the top claude-opus-4.7 run #266: it swapped the UBERON:0002346 label and EXACT synonym, updated `terminology_notes` to the gold wording, added `term_tracker_item` for issue #3682, and reserialized with `robot convert` so the ~14 propagated `! neuroectoderm` label comments match gold. F1=0.917 slightly under-represents quality; the only deviations from the human are a defensible `has_relational_adjective` consistency edit and the `xsd:anyURI` vs `xsd:string` datatype on the tracker item.

## Strengths

- Exactly satisfies the curator's instruction: label/EXACT-synonym swap with the issue referenced via `term_tracker_item`.
- Reproduced the human's `terminology_notes` rewording verbatim ("we prefer neuroectoderm to neural ectoderm since placodal ectoderm is not classified here").
- Used the `obo-checkout.pl`/`obo-checkin.pl` workflow rather than hand-editing the 220k-line OBO file, and ran `robot convert` reserialization — so the mechanical label-comment propagation across all UBERON:0002346-referencing stanzas matches gold, giving high recall (0.880).
- Correctly identified **CL:0000133 "neurectodermal cell"** (and noted its `neurectodermal cell` exact synonym) as the corresponding CL follow-up term — matching the human-opened companion issue obophenotype/cell-ontology#3595.
- Honest about the environment constraint: explicitly stated it did not open the CL issue because remote GitHub interaction was disabled, rather than fabricating an issue link.

## Issues

- Extra edit not in gold: `has_relational_adjective` "neurectodermal"→"neuroectodermal". Defensible/justified consistency improvement; main contributor to the recall gap vs the human.
- `term_tracker_item` datatype `xsd:anyURI` vs gold `xsd:string` — semantically cleaner but diverges from the prevailing Uberon convention; serialization-level, not substantive.
- The CL follow-up issue was not opened, but this is an eval-environment restriction, not an agent failure.
