---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 462
agent: std_claude_son45
model: claude-sonnet-4.5
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

The agent did exactly what issue #10030 literally asked: it removed the 8 erroneous "cellulitis and abscess..." synonyms (a bacterial soft-tissue infection cluster mis-imported from DOID:13074) from MONDO:0001628 "tinea unguium", a fungal nail infection, and left all correct nail-dermatophytosis synonyms and logical axioms intact. The metadiff F1=0.003 massively *under-represents* quality: the selected gold PR #10117 is a "drastic, large-scale" 5,103-line ontology-wide synonym purge (per the curator decision in the issue thread), so a correctly scoped single-term fix is structurally capped near zero F1. The actual change is correct and clean — this is a poor evaluation case, not an agent failure.

## Strengths

- Correctly identified all 8 problematic synonyms on MONDO:0001628 and the DOID:13074 import as their common origin.
- Removed precisely the lines the issue named (buttock/face/gluteal region/trunk/upper arm) plus the conceptually identical bare "cellulitis and abscess", finger, and finger-and-toe variants — a defensible, complete reading of the issue.
- Preserved all valid synonyms (`onychomycosis`, `dermatophytic onychia`, `dermatophytosis of nail`, etc.) and untouched the `is_a`/`intersection_of`/`disease_has_infectious_agent` axioms. No collateral damage.
- Single clean hunk anchored at the tinea unguium stanza; no base-state contamination.

## Issues

- No correctness or scope errors. The change is a faithful, narrowly scoped resolution of the issue.
- Minor convention gap: did not add the `IAO:0000233` term-tracker provenance annotation linking PR back to issue #10030 (the agent config asks for this; the opencode/codex variants did add it). Style/completeness nit, not an error.
- Did not also remove the parallel erroneous `xref: ICD9:681.9 {source="DOID:13074"}` (cellulitis/abscess of unspecified digit), which the kimi/gpt-5.5 variants caught. Defensible omission given the issue is scoped to synonyms, but the xref shares the same bad provenance.
