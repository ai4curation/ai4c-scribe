---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 83
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.818
precision: 0.9
recall: 0.75
jaccard: 0.692
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/83
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 83 --repo ai4curation/eval-ont-agent-go
-->

## Summary

This run produces the byte-identical output blob (`8b01af9`) as pr104 (same model/runtime, gpt-5.5/opencode), demonstrating run-to-run determinism. The substantive assessment is therefore identical to pr104: the obsoletion and both renames are correct, but the agent rewrote the `GO:0006901` definition and **added a new logical definition** (`intersection_of: GO:0022607` + `results_in_assembly_of GO:0030120`) to that active parent term, and tagged both active terms with the obsoletion `term_tracker_item`. The metadiff (`f1: 0.818`, `precision: 0.9`, `recall: 0.75`) over-represents quality because a line-diff cannot evaluate the reasoner risk of inventing an equivalence axiom on a label-only request.

## Strengths

- **Identical to pr104**, confirming reproducibility for gpt-5.5/opencode on this case (both yield blob `8b01af9`).
- **Obsoletion is correct and complete:** `name: obsolete ...`, `def: "OBSOLETE. ..."` (original dbxrefs kept), both `intersection_of` removed, `comment`, `term_tracker_item`, `is_obsolete: true`, `replaced_by: GO:0048208`, and `created_by`/`creation_date` retained.
- **Both renames correct** with old labels restored as EXACT synonyms; `GO:0048208` restored-synonym dbxrefs `[GOC:ascb_2009, GOC:dph, GOC:tb]` match the gold.
- **Refreshed the `GO:0048208` self `is_a` comment** to `! vesicle coat assembly`.
- Documented validation: pre/post `make travis_build` passing, `obo-grep.pl` confirmation of no remaining GO:0003400 references, and an honest checklist.

## Issues

- **New logical definition added to GO:0006901 (over-editing / correctness risk — headline problem).** Adds `intersection_of: GO:0022607 ! cellular component assembly` and `intersection_of: results_in_assembly_of GO:0030120 ! vesicle coat` to a term that previously had no equivalence axiom. This is a substantive, unrequested ontological change with reasoner consequences across the vesicle-coating subtree; it should have been proposed in an issue comment. The gold and the current merged ontology have no `intersection_of` on `GO:0006901`.
- **Unrequested definition rewrite of GO:0006901** to the generic `cellular component assembly` boilerplate; the gold left the original def intact.
- **Scope creep onto active terms:** `term_tracker_item` for #31945 added to both `GO:0006901` and `GO:0048208` — the obsoletion tracker belongs only on the obsoleted term.
- **Missed the incoming-edge comment maintenance (omission):** no refresh of `GO:0016183`/`GO:0048200` `! vesicle coating` comments, both updated by the gold.

Net: `partial_success`, identical to pr104. Core task correct; the unrequested new axiom on `GO:0006901` is the highest-risk over-edit in the cohort and is not penalized proportionally by the metadiff.
