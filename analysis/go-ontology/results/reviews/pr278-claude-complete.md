---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 278
agent: std_opencode_kimi26
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes:
  - over_editing
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/278
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 278 --repo ai4curation/eval-ont-agent-go
-->

## Summary

A strong attempt that ties pr344 on metadiff (`f1: 0.900`, `precision: 0.900`, `recall: 0.900`) but has a couple of real, if minor, defects the score papers over. The obsoletion and both renames are correct, but the agent (1) deleted the `created_by`/`creation_date` provenance lines from the obsoleted `GO:0003400` stanza, (2) added unrequested `term_tracker_item` properties to the two *active* renamed terms, (3) emptied the restored synonym dbxrefs, and (4) missed the stale-comment refresh on `GO:0016183`/`GO:0048200`. The metadiff over-represents quality slightly: 0.900 is generous given the lost provenance lines and the scope creep on active terms.

## Strengths

- **Core obsoletion is correct.** `GO:0003400` gets `name: obsolete ...`, `def: "OBSOLETE. ..."` (original dbxrefs kept), both `intersection_of` axioms removed, `is_obsolete: true`, `replaced_by: GO:0048208`, `term_tracker_item`, and a comment.
- **Both renames correct.** `GO:0048208` → `COPII vesicle coat assembly` and `GO:0006901` → `vesicle coat assembly`, with old labels restored as EXACT synonyms and the previously-promoted synonyms removed — matching the gold's label/synonym swap logic.
- **Updated the GO:0048208 self `is_a` comment** to `! vesicle coat assembly`, matching the gold.
- Strong, verifiable validation methodology: PR comment documents `robot convert`, `robot reason` (ELK, no unsat), `robot verify` (all SPARQL QC pass), and `robot explain`. This is more rigorous QC reporting than most attempts.

## Issues

- **Provenance loss (error).** The diff removes `created_by: dph` and `creation_date: 2009-12-17T08:38:14Z` from the obsoleted `GO:0003400` stanza. The gold PR and the `term-obsoletion` skill both explicitly retain these — historical provenance is one of the few things that *must* survive obsoletion. This is a genuine, if low-severity, regression.
- **Scope creep onto active terms.** Added `property_value: term_tracker_item "...31945..."` to both `GO:0006901` and `GO:0048208`. `term_tracker_item` is appropriate on the *obsoleted* term to record why it was deprecated; tagging two unrelated active terms with the obsoletion issue is non-standard and unrequested. The gold did not do this.
- **Weak obsoletion comment.** "The reason for obsoletion is that this term is equivalent to COPII vesicle coating (GO:0048208)" is both biologically imprecise (the term is *not* equivalent — it is a regulation term whose annotated proteins are part_of the process) and uses the now-stale old label "COPII vesicle coating". The gold's comment correctly explains the part_of relationship.
- **Missed the stale-comment maintenance (omission).** It did not refresh `is_a: GO:0006901 ! vesicle coating` → `! vesicle coat assembly` on `GO:0016183` and `GO:0048200`, both of which the gold updated. This is the recall gap shared with most attempts.
- **Restored synonym dbxrefs emptied.** `synonym: "COPII vesicle coating" EXACT []` discards attribution; the gold kept `[GOC:ascb_2009, GOC:dph, GOC:tb]`. Minor.

Net: a `success` on the central task, but the provenance deletion and active-term scope creep are concrete defects that the 0.900 metadiff does not penalize.
