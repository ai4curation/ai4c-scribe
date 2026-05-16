---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 183
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.864
precision: 0.95
recall: 0.792
jaccard: 0.76
outcome: partial_success
failure_modes:
  - over_editing
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/183
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 183 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:0003400` and renamed both `GO:0048208` and `GO:0006901`, and it was the only non-opus attempt besides pr61 to refresh the GO:0048208 self `is_a` comment. However, it made an unrequested and biologically questionable change: it **rewrote the definitions** of both active terms `GO:0006901` and `GO:0048208` to a generic "aggregation, arrangement and bonding together of a set of components ..." `cellular component assembly` boilerplate. The issue asked only for a label change, not a definition rewrite. The metadiff (`f1: 0.864`, `precision: 0.95`, `recall: 0.792`) over-represents quality on precision (the def rewrites are scored as matching the surrounding context) and the failure modes are over-editing plus the cohort-wide comment omission.

## Strengths

- **Obsoletion is correct and complete:** `name: obsolete ...`, `def: "OBSOLETE. ..."` (original dbxrefs kept), both `intersection_of` removed, `comment`, `term_tracker_item`, `is_obsolete: true`, `replaced_by: GO:0048208`, and `created_by`/`creation_date` retained.
- **Both renames correct** with old labels restored as EXACT synonyms; the `GO:0048208` restored-synonym dbxrefs `[GOC:ascb_2009, GOC:dph, GOC:tb]` match the gold.
- **Refreshed the `GO:0048208` self `is_a: GO:0006901 ! vesicle coat assembly` comment** — most attempts missed this.
- Sound process: documented `term-obsoletion` and `design-pattern` workflow use, `obo-checkout.pl`/`obo-checkin.pl`, and `make travis_build` passing. Honest disclosure that `runoak` was unavailable and it fell back to the issue-provided annotation summary.

## Issues

- **Unrequested definition rewrites (over-editing, the headline problem).** The agent replaced `GO:0006901`'s def ("A protein coat is added to the vesicle to form the proper shape ...") and `GO:0048208`'s def ("The addition of COPII proteins and adaptor proteins to ER membranes ...") with a templated "The aggregation, arrangement and bonding together of a set of components to form a [...] coat." The issue (and ValWood's comment) requested *only* a label change. The gold PR left both definitions untouched. While the new wording aligns with the `cellular component assembly` design pattern, this is a substantive, unrequested semantic edit on two heavily-annotated active terms and exactly the kind of scope expansion that should be raised in an issue comment, not committed unilaterally. The original `GO:0048208` def also names the specific COPII/adaptor-protein biology, which the generic replacement discards.
- **Missed the stale-comment maintenance on incoming edges (omission).** No refresh of `is_a: GO:0006901 ! vesicle coating` → `! vesicle coat assembly` on `GO:0016183`/`GO:0048200`, both updated by the gold.
- The PR comment frames the def rewrite as "Updated the definition ... so the lexical layer matches the requested terminology," which mischaracterizes the issue's ask (it requested a label, not a def) and understates that this is an unrequested change.

Net: `partial_success` — the central obsoletion+rename is correct, but the unrequested twin definition rewrites on active terms are a real scope/correctness concern that the high precision metric masks.
