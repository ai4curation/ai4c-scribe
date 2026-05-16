---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 104
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/104
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 104 --repo ai4curation/eval-ont-agent-go
-->

## Summary

This run produces the same output blob (`8b01af9`) as pr83 (same model/runtime, gpt-5.5/opencode). The obsoletion and both renames are correct, but the agent made two unrequested substantive changes to active terms: it **rewrote the `GO:0006901` definition** to a generic `cellular component assembly` template *and added a brand-new logical definition* (`intersection_of: GO:0022607 ! cellular component assembly` + `intersection_of: results_in_assembly_of GO:0030120 ! vesicle coat`), and it tagged both `GO:0006901` and `GO:0048208` with `term_tracker_item` for the obsoletion issue. The metadiff (`f1: 0.818`, `precision: 0.9`, `recall: 0.75`) over-represents quality: introducing a new logical axiom on a heavily-used term from a label-only request is a real scope/correctness risk that a line-diff cannot evaluate.

## Strengths

- **Obsoletion is correct and complete:** `name: obsolete ...`, `def: "OBSOLETE. ..."` (original dbxrefs kept), both `intersection_of` removed, `comment`, `term_tracker_item`, `is_obsolete: true`, `replaced_by: GO:0048208`, and `created_by: dph`/`creation_date` retained.
- **Both renames correct** with old labels restored as EXACT synonyms; `GO:0048208` restored-synonym dbxrefs `[GOC:ascb_2009, GOC:dph, GOC:tb]` match the gold.
- **Refreshed the `GO:0048208` self `is_a: GO:0006901 ! vesicle coat assembly` comment** — most attempts missed this.
- Reasonable validation reporting (pre/post `make travis_build`).

## Issues

- **New logical definition added to GO:0006901 (over-editing / correctness risk — headline problem).** The agent added `intersection_of: GO:0022607 ! cellular component assembly` and `intersection_of: results_in_assembly_of GO:0030120 ! vesicle coat` to `GO:0006901`, which previously had *no* logical definition. The issue requested only a label change. Adding an equivalence axiom to a parent term used across the vesicle-coating branch is a substantive ontological change with reasoner consequences (it would force all `vesicle coat assembly` subclasses into the `cellular component assembly` hierarchy) and should be proposed in an issue comment, not committed unilaterally. The gold did not do this; the current merged ontology confirms `GO:0006901` has no `intersection_of`.
- **Unrequested definition rewrite.** `GO:0006901`'s def changed from "A protein coat is added to the vesicle to form the proper shape ..." to the generic template "The aggregation, arrangement and bonding together of a set of components to form a vesicle coat." Unrequested; the gold left it untouched.
- **Scope creep onto active terms:** `term_tracker_item` for issue #31945 added to both `GO:0006901` and `GO:0048208`. The obsoletion tracker belongs on the obsoleted term, not on two unrelated active terms.
- **Missed the incoming-edge comment maintenance (omission):** no refresh of `GO:0016183`/`GO:0048200` `! vesicle coating` comments, both done by the gold.
- Agent footer mislabels the runtime as "pi agent" in the PR comment while the harness metadata records `opencode`/`openai/gpt-5.5` — minor reporting inconsistency.

Net: `partial_success`. The core obsoletion+rename is right, but inventing a new logical definition on `GO:0006901` from a label-only request is the most consequential over-edit in the cohort, and the metadiff does not capture its risk.
