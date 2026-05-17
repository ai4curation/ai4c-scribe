---
ontology: uberon
issue_number: 3682
pr_number: 3683
eval_repo_pr: 15
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
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent (gpt-5.5 via opencode, blob `15d3a90`) performed the UBERON:0002346 label/EXACT-synonym swap, reproduced the gold `terminology_notes` rewording verbatim, added `term_tracker_item` for issue #3682, updated `has_relational_adjective` to `neuroectodermal`, and reserialized with `robot convert`. It additionally attached an issue-URL provenance bracket to the demoted synonym (`synonym: "neurectoderm" EXACT [https://github.com/obophenotype/uberon/issues/3682]`), which gold did not. F1=0.875 modestly under-represents quality: the core task is correct and the terminology note matches gold verbatim; the gap is one defensible extra (`has_relational_adjective`) plus the over-eager synonym xref.

## Strengths

- Core ontological change is correct and matches the curator instruction: label/EXACT-synonym swap, issue referenced via `term_tracker_item`.
- Reproduced the human `terminology_notes` rewording verbatim ("we prefer neuroectoderm to neural ectoderm since placodal ectoderm is not classified here") — better fidelity than the paraphrasing runs #69/#52.
- Ran checkout/checkin plus `robot convert`, so the ~14 `! neuroectoderm` label-comment propagations match gold (recall 0.840).
- Correctly identified **CL:0000133 "neurectodermal cell"** as the corresponding CL follow-up term (matches human-opened obophenotype/cell-ontology#3595).

## Issues

- Mild over-editing: added `[https://github.com/obophenotype/uberon/issues/3682]` as an OBO xref/provenance bracket on `synonym: "neurectoderm" EXACT`. The issue is already linked via `term_tracker_item`; a GitHub issue URL is not a conventional synonym provenance source in Uberon, and gold did not do this. Harmless but unnecessary, and it lowers precision vs the human.
- Extra edit not in gold: `has_relational_adjective` "neurectodermal"→"neuroectodermal" — defensible consistency improvement.
- `term_tracker_item` datatype `xsd:anyURI` vs gold `xsd:string`: serialization-level convention difference.
- CL follow-up issue not opened — eval-environment restriction, not an agent failure.
