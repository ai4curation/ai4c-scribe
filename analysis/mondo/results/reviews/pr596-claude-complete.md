---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 596
agent: std_opencode_gemma4
model: gemma-4-31b
runtime: opencode
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
reviewed_at: 2026-05-17
---

## Summary

The agent removed exactly the 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 "tinea unguium" — a minimal, perfectly scoped resolution of the literal ask of issue #10030 (blob `b9af5d1`, byte-identical to attempt #243, the same gemma-4-31b/opencode model on a second sampled run). Metadiff F1=0.003 badly *under-represents* quality: gold PR #10117 is a 5,103-line ontology-wide synonym purge, so this correct single-term fix is structurally unscoreable against it.

## Strengths

- Correct and minimal core fix: removed precisely the 8 mis-imported DOID:13074 "cellulitis and abscess..." synonyms and nothing else; recall=1.0 reflects fully on-target edits.
- Excellent scope discipline: no collateral edits, no whitespace/EOF artifacts. Stable and reproducible — identical output to the sibling gemma run #243.
- Preserved all valid nail-dermatophytosis synonyms and every logical axiom (`is_a`/`intersection_of`/`disease_has_location UBERON:0001705`/`disease_has_infectious_agent`).
- PR write-up gives a correct, well-reasoned rationale (tinea unguium is a nail fungal infection; cellulitis/abscess of buttock/face/etc. are not synonyms) and reports ODK-script-based editing plus `make NORM`.

## Issues

- Did not add the `IAO:0000233` issue-tracker provenance annotation favored by the mondo-agent-config convention. Minor convention gap, not a content error.
- Did not remove the parallel mis-imported `xref: ICD9:681.9 {source="DOID:13074"}`; defensible omission, slightly less thorough than the codex/gpt-5.5 runs.
- Near-zero F1/precision is entirely a scoring artifact of the out-of-scope gold mega-edit; against the issue's actual ask this is an exemplary minimal fix.
