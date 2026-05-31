---
ontology: uberon
issue_number: 3682
pr_number: 3683
eval_repo_pr: 9
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v2
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

The agent (gpt-5.5 via the codex runtime, config v2) produced a diff byte-identical (blob `86183ac`) to the top runs #266 and #14: label/EXACT-synonym swap on UBERON:0002346, gold-matching `terminology_notes` rewording, `term_tracker_item` for issue #3682, and `robot convert` reserialization propagating the ~14 `! neuroectoderm` label comments. F1=0.917 slightly under-represents quality; the only deviations from gold are the defensible `has_relational_adjective` consistency edit and `xsd:anyURI` vs `xsd:string` on the tracker item.

## Strengths

- Core ontological change exactly matches the curator instruction in issue #3682 (swap label and exact synonym, reference the issue).
- Reproduced the human `terminology_notes` rewording verbatim.
- Documented a sound methodology in the PR comment: read the imported issue context, inspected the UBERON:0002346 stanza and all ID mentions with `obo-grep.pl`, checked the parent `UBERON:0000923 ! germ layer` for consistency (correctly concluding no hierarchy change was needed), used checkout/checkin, ran `robot convert`, and ran `git diff --check`.
- Correctly identified **CL:0000133 "neurectodermal cell"** as the corresponding CL follow-up term (matches human-opened obophenotype/cell-ontology#3595) and was transparent that the CL issue could not be opened from the local eval checkout.

## Issues

- Extra edit not in gold: `has_relational_adjective` "neurectodermal"→"neuroectodermal" — defensible/justified consistency improvement; principal source of the recall gap vs the human.
- `term_tracker_item` datatype `xsd:anyURI` vs gold `xsd:string`: serialization-level convention difference, not a substantive defect.
- CL follow-up issue not opened — eval-environment restriction, not an agent failure.
