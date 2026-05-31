---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 243
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

The agent removed exactly the 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 "tinea unguium" — a minimal, perfectly scoped resolution of the literal ask of issue #10030 (blob `b9af5d1`, byte-identical to the claude-sonnet/opus/haiku, gpt-5.4/codex, and gemma #596 runs). Metadiff F1=0.003 badly *under-represents* quality: gold PR #10117 is a 5,103-line ontology-wide synonym purge, so this correct single-term fix is structurally unscoreable against it.

## Strengths

- Correct and minimal core fix: removed precisely the 8 mis-imported DOID:13074 "cellulitis and abscess..." synonyms (bacterial soft-tissue infections wrongly attached to a fungal nail infection) and nothing else.
- Tightest possible scope discipline: zero collateral edits, no whitespace artifacts, no trailing-line changes — recall=1.0 reflects that every line it touched is a line a correct fix should touch.
- Preserved all valid nail-dermatophytosis synonyms (`dermatophytic onychia`, `dermatophytic onychomycosis`, `dermatophytosis of nail`) and every logical axiom.
- Sound rationale in the PR write-up correctly attributing the bad synonyms to the DOID:13074 import; reported using `obo-grep.pl`/`obo-checkout.pl`/`obo-checkin.pl` and `make NORM`.

## Issues

- Did not add the `IAO:0000233` issue-tracker provenance annotation that the mondo-agent-config convention favors and that the gpt-5.4/gpt-5.5 runs included. Minor process/convention gap, not a content error.
- Did not remove the parallel mis-imported `xref: ICD9:681.9 {source="DOID:13074"}`. Defensible (not explicitly requested) but a slightly less thorough cleanup than the codex/gpt-5.5 variants.
- F1/precision near zero is purely a scoring artifact of the broken gold comparison; against the issue's actual ask this is an exemplary minimal fix.
