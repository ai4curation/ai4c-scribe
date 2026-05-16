---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 381
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.842
precision: 0.8
recall: 0.889
jaccard: 0.727
outcome: success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/381
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 381 --repo ai4curation/eval-ont-agent-go
-->

## Summary

A correct, scope-disciplined sonnet-4.5/copilot run. The obsoletion and both renames are right, with full provenance retained and no scope creep. The metadiff is the lowest of the "no-error" attempts (`f1: 0.842`, `precision: 0.800`, `recall: 0.889`), but this *under*-represents quality: the precision hit is driven almost entirely by emptying the restored-synonym dbxrefs (`COPII vesicle coating EXACT []` instead of the gold's `[GOC:ascb_2009, GOC:dph, GOC:tb]`) and by missing the cosmetic incoming-edge comment refresh — both minor.

## Strengths

- **Obsoletion matches gold:** `name: obsolete ...`, `def: "OBSOLETE. ..."` (original dbxrefs kept), both `intersection_of` removed, `comment`, `term_tracker_item`, `is_obsolete: true`, `replaced_by: GO:0048208`, and `created_by: dph`/`creation_date` retained — full provenance preserved.
- **Strong obsoletion comment:** "the proteins annotated to this term are part of the COPII vesicle coating pathway itself, not upstream regulators" — biologically accurate, matches ValWood's note.
- **Both renames correct** with old labels restored as EXACT synonyms; the previously-promoted synonyms removed (matching the gold's swap logic).
- **Tight scope, no errors.** Only the three target terms touched; no definition rewrites, no spurious `term_tracker_item` on active terms, no design-pattern-file edits.
- Good process documentation: term-obsoletion skill consulted, annotation impact correctly summarized (11 EXP; SGD 8, UniProt 3), and the disputed MAPK15 annotation correctly flagged as out of scope.

## Issues

- **Restored-synonym dbxrefs emptied (minor style/precision).** `synonym: "COPII vesicle coating" EXACT []` discards the source attribution; the gold preserved `[GOC:ascb_2009, GOC:dph, GOC:tb]` (the dbxrefs of the synonym being demoted). Defensible but loses provenance, and is the main precision-lowering difference vs the gold line-diff.
- **Missed the stale-comment maintenance (omission).** No refresh of `is_a: GO:0006901 ! vesicle coating` → `! vesicle coat assembly` on `GO:0016183`/`GO:0048200`, nor `GO:0048208`'s own self-edge — all done by the gold. Cosmetic; cohort-wide omission.

Net: `success`. The 0.842 metadiff is the harshest in the no-error tier and under-represents the actual quality — the substance is correct and well-scoped; only attribution/cosmetic details differ from the gold.
