---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 272
agent: std_opencode_k26
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Running kimi-k2.6 under opencode, the agent obsoleted GO:0005870 "actin capping protein of dynactin complex" with `replaced_by: GO:0008290`, producing a diff functionally identical to human gold PR #31960 apart from the obsoletion `comment:` prose. F1=0.900 under-represents quality: this is a correct, complete, scope-disciplined obsoletion.

## Strengths

- Diff matches gold semantically: name prefixed "obsolete", definition prefixed "OBSOLETE." (original `[GOC:jl, PMID:18221362, PMID:18544499]` xrefs kept), both `intersection_of` axioms removed (genus `GO:0008290`, differentia `part_of GO:0005869`), `is_obsolete: true`, `replaced_by: GO:0008290`, `term_tracker_item` for #31956 added.
- Correct ontological reasoning: identifies GO:0005870 as a logical subclass of GO:0008290 defined purely by its `part_of` relationship to the dynactin complex, making GO:0008290 the appropriate direct replacement.
- Good validation: ran `robot reason -r ELK` and `robot convert` successfully; checked for residual references in `go-edit.obo`, `src/taxon_constraints`, and other OBO files; confirmed 0 EXP annotations consistent with the issue.
- Proper obo-checkout.pl / obo-checkin.pl workflow; committed only `src/ontology/go-edit.obo`.

## Issues

- Minor wording imprecision: the PR rationale and `comment:` state the term "is effectively equivalent to its parent GO:0008290". Strictly, GO:0005870 was a *specialization* (subclass) of GO:0008290, not equivalent — but for an unused term with no differentiating annotations the practical consequence (direct replacement) is the same, and the gold PR makes a similar simplification ("redundant with"). Not a defect, and not the cause of the F1 gap (which is solely the differing comment text vs gold).
