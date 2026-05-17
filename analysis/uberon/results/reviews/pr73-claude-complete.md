---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 73
agent: std_codex_gpt-5.5
model: gpt-5.5
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.182
precision: 0.105
recall: 0.667
jaccard: 0.100
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn (CL label-comment refreshes CL:1000271/CL:0002145/CL:0002332/CL:1000223/CL:0000150, synonym reorder in UBERON:0003532) from a master-merge + ROBOT reserialization, plus reasoner-driven endocardium/synovial is_a deletions negotiated only in the PR comment thread. The genuine in-scope content is ~4 has_part→composed_primarily_of swaps; this attempt reproduces 3 of them. F1=0.182 severely under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Functionally identical in substance to attempt #80 (gpt-5.4/codex): the agent correctly converted `has_part CL:0000076` → `composed_primarily_of CL:0000076` on all three core squamous classes — `squamous epithelium` (UBERON:0006914), `simple squamous epithelium` (UBERON:0000487), and `stratified squamous epithelium` (UBERON:0006915) — matching the three corresponding gold axiom edits exactly. Recall 0.667 reflects only the gold PR's out-of-scope label/serialization churn and reasoner-driven cleanup, not any deficiency. F1 0.182 strongly **under-represents** quality; this is among the best attempts in the cohort.

## Strengths

- All three squamous logical definitions correctly repaired with `composed_primarily_of` (RO:0002473) — the full intended in-scope fix set.
- Best-documented methodology of the cohort: PR comment reports reading `__issue_context__.json`, checking for an applicable DOSDP pattern under `src/patterns/dosdp-patterns` (correctly found none), editing via `obo-checkout.pl`/`obo-checkin.pl`, reserializing with `robot convert`, syntax-validating, *and* running ELK classification (`robot reason -i ... -r ELK`). This directly satisfies the issue's "Important to test results of change" instruction and the agent config's prescribed workflow.
- Kept the committed diff scoped to the three affected stanzas, deliberately avoiding the serialization churn that contaminated gold.

## Issues

- Added `property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3473" xsd:anyURI` on all three terms; gold did not. Defensible provenance convention but extra vs gold (minor precision-vs-gold reduction, not an error).
- Did not fix `short descending thin limb` (UBERON:0005099), the additional `has_part CL:0000076` site gold aligned. Minor completeness gap.
- Reasoner-driven endocardium/synovial `is_a` removals are not reproduced — unpredictable from the issue (they came from curator research in the PR thread), so not chargeable.
