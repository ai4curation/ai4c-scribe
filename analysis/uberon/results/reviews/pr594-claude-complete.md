---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 594
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.190
precision: 0.105
recall: 1.000
jaccard: 0.105
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn (CL label-comment refreshes CL:1000271/CL:0002145/CL:0002332/CL:1000223/CL:0000150, synonym reorder in UBERON:0003532) from a master-merge + ROBOT reserialization, plus reasoner-driven endocardium/synovial is_a deletions (UBERON:0001081/0009129/0002018) negotiated only in the PR comment thread. The genuine in-scope content is ~4 has_part→composed_primarily_of swaps; this attempt reproduces 3 of them with no spurious edits. F1=0.190 severely under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

A clean, well-scoped solve of the substantive ontology task: the agent swapped `has_part CL:0000076` → `composed_primarily_of CL:0000076` (RO:0002473) on all three core squamous classes — `simple squamous epithelium` (UBERON:0000487), `squamous epithelium` (UBERON:0006914), and `stratified squamous epithelium` (UBERON:0006915) — exactly matching the corresponding gold edits and addressing the issue's explicit ask. The metadiff F1 of 0.190 (recall 1.000, precision 0.105) badly **under-represents** the result: precision is crushed only because gold PR #3494 additionally swept up out-of-scope CL-label churn, ROBOT serialization noise, and reasoner-driven endocardium/synovial cleanup that the issue never requested and that no agent could derive from issue #3473 alone. On the issue's actual intent this is essentially a complete and correct solution.

## Strengths

- Correctly repaired all three squamous-branch terms (UBERON:0000487, UBERON:0006914, UBERON:0006915) with the right relation `composed_primarily_of` — the full set of squamous logical-definition repairs the issue intended, more complete than the kimi attempt (#439, 1 term), the Opus attempt (#238, 2 terms), and the gemma attempt (#110, 1 term), and matching the strongest codex attempts (#80/#73, 3 terms).
- Tightly scoped: the only change beyond the three axiom swaps is a single trailing-blank-line removal at EOF in the `vessel_supplies_blood_to` typedef region — a benign serialization side-effect, not a semantic edit.
- Did **not** add a `term_tracker_item` property_value (unlike #439/#80), keeping the diff strictly to the requested logical-definition change and avoiding even harmless extra provenance lines.
- Avoided the gold PR's own out-of-scope label/serialization churn — the correct discipline, and the opposite of what produced gold's noise.

## Issues

- Did not fix `short descending thin limb` (UBERON:0005099), the one other `has_part CL:0000076` site gold also aligned to `composed_primarily_of`. Minor completeness gap: the issue did not name this term and finding it requires noticing the downstream `has_part` usage during the "test results / fix and align" step. Recall against gold is still 1.000 only because metadiff normalization collapses the squamous-branch lines; substantively this is a small omission, not an error.
- Could not (and is not chargeable for) reproducing the reasoner-driven endocardium/synovial `is_a` removals (UBERON:0001081, UBERON:0009129, UBERON:0002018) negotiated in the PR comment thread, nor the CL label refreshes — these are gold's out-of-scope extras, not agent failures.
- No agent PR/issue comment was captured for this run, so the validation methodology cannot be confirmed for #594 specifically; the identical-blob sibling #653 documents `obo-checkout.pl`/`obo-checkin.pl` + `robot convert` parse validation, so the same process was almost certainly followed here.
