---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 386
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v3
case_type: bulk_edit
difficulty: hard
f1: 0.003
precision: 0.002
recall: 1.0
jaccard: 0.002
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_out_of_scope_mega_edit
companion_prs: []
scoring_caveat: "metadiff compares a correct 8-line single-term fix against the 5,103-line ontology-wide bulk sweep selected as gold (#10117); F1=0.003 is meaningless here. Judge against the literal ask of issue #10030."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is the strongest attempt on the case. The agent removed exactly the 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 "tinea unguium", correctly traced them to the DOID:13074 import, and — critically — explicitly recognized in its PR write-up that the issue thread (sabrinatoro: "We need a more drastic-large scale approach") pointed to a broader systematic sweep, deliberately scoping its PR to the one term the issue names while flagging the larger DO-import audit as follow-up. The metadiff F1=0.003 badly *under-represents* quality: gold PR #10117 *is* that drastic 5,103-line ontology-wide purge, so a correctly scoped term-level fix cannot score against it. The change itself is correct and clean.

## Strengths

- Correct, complete, well-scoped edit: all 8 bad synonyms removed, all valid synonyms and logical axioms (`is_a`, `intersection_of disease_has_location UBERON:0001705`, `disease_has_infectious_agent NCBITaxon:4751/4890`) preserved.
- Demonstrated genuine reading of the issue *discussion*, not just the title: explicitly noted the curators' large-scale-cleanup intent and consciously chose a narrow fix while documenting the scaling concern — exactly the right judgment given an agent cannot safely replicate a 5,000-line expert sweep.
- Identified the parallel suspect `xref: ICD9:681.9 {source="DOID:13074"}` and gave a defensible reason for leaving it (issue scoped to synonyms; xref-level mismatch belongs in the DO-import audit). Shows discernment rather than mechanical deletion.
- Reported syntax validation (`robot convert`) and normalization checks.

## Issues

- No correctness or scope errors.
- Did not add the `IAO:0000233` term-tracker provenance annotation (config convention); a minor completeness nit, not an error. The agent's deliberate narrow scoping is the correct call here.
