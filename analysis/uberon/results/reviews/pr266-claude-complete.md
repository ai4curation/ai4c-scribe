---
ontology: uberon
issue_number: 3682
pr_number: 3683
eval_repo_pr: 266
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
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

The agent performed the requested label/exact-synonym swap on UBERON:0002346 (`neurectoderm` → `neuroectoderm`; old label demoted to `synonym: "neurectoderm" EXACT []`), updated `terminology_notes` to "we prefer neuroectoderm to neural ectoderm…", added `property_value: term_tracker_item` referencing issue #3682, and re-serialised with `robot convert` so the ~14 propagated `! neuroectoderm` label comments throughout the file match the gold PR. F1=0.917 slightly *under-represents* quality: the only deltas from gold are (a) a defensible extra `has_relational_adjective` "neurectodermal"→"neuroectodermal" consistency edit the human did not make, and (b) `xsd:anyURI` vs gold's `xsd:string` datatype on the tracker item. This is a correct, complete, well-scoped resolution.

## Strengths

- Core edit exactly matches the curator instruction in the issue ("@dragon-ai-agent please swap label and exact synonym, reference this issue"): label and EXACT synonym are swapped and the issue is referenced via `term_tracker_item`.
- Correctly reproduced the human's `terminology_notes` rewording verbatim ("we prefer neuroectoderm to neural ectoderm since placodal ectoderm is not classified here"), which the gpt-5.5/opencode runs (#69, #52) did not match (they paraphrased it).
- Ran `robot convert` reserialization, so the mechanical `! neurectoderm`→`! neuroectoderm` label-comment propagation across ~14 referencing stanzas (UBERON:0001772 iris sphincter, ciliary body, neural crest UBERON:0002342, etc.) matches gold exactly — this is why recall (0.880) is much higher than the non-reserialized attempts (#1=0.857-recall-but-precision-0.261, #6).
- Correctly identified the corresponding Cell Ontology term **CL:0000133 "neurectodermal cell"** for the requested CL follow-up, doing the search work the maintainer asked for so CL editors would not have to; the human-opened companion issue obophenotype/cell-ontology#3595 confirms CL:0000133 was exactly the right term.
- Excellent scope transparency: the PR comment explicitly enumerates what was left unchanged (def text, other synonyms, all xrefs, the CL term comment) and why other "neurectoderm" substrings in unrelated externally-sourced stanzas were deliberately not touched.

## Issues

- Extra edit not in gold: changed `property_value: has_relational_adjective "neurectodermal"` → `"neuroectodermal"`. This is a *defensible/justified* consistency edit (the relational adjective should track the new preferred label) and is arguably an improvement, but it is the principal cause of the recall gap vs the human (who left it as `neurectodermal`). Not an error.
- Used `xsd:anyURI` for the `term_tracker_item` datatype where gold used `xsd:string`. `xsd:anyURI` is more semantically correct for a URL, but it differs from the prevailing Uberon convention for this property; this is a normalization/serialization-level difference, not a substantive defect.
- The requested CL issue was not actually opened — but this is an environment constraint (remote GitHub interaction disabled in the eval), not an agent failure; the agent surfaced the full CL term list in its issue comment so the follow-up is trivially actionable.
