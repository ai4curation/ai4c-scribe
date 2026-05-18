---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 653
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
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn (CL label-comment refreshes CL:1000271/CL:0002145/CL:0002332/CL:1000223/CL:0000150, synonym reorder in UBERON:0003532) from a master-merge + ROBOT reserialization, plus reasoner-driven endocardium/synovial is_a deletions (UBERON:0001081/0009129/0002018) negotiated only in the PR comment thread. The genuine in-scope content is ~4 has_part→composed_primarily_of swaps; this attempt reproduces 3 of them with documented robot-convert validation. F1=0.190 severely under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

Functionally identical diff to sibling #594 (same blob `4cbe0a0`) but with a full validation narrative: the agent swapped `has_part CL:0000076` → `composed_primarily_of CL:0000076` (RO:0002473) on `simple squamous epithelium` (UBERON:0000487), `squamous epithelium` (UBERON:0006914), and `stratified squamous epithelium` (UBERON:0006915), exactly matching the three corresponding gold edits and resolving the issue's explicit ask. The metadiff F1 of 0.190 (recall 1.000, precision 0.105) **under-represents** quality: precision collapses only because gold PR #3494 additionally carries out-of-scope CL-label refreshes, ROBOT serialization noise, and reasoner-driven endocardium/synovial cleanup that issue #3473 never requested. Substantively this is a near-complete, correct, and well-documented solution.

## Strengths

- Correctly repaired all three squamous-branch terms (UBERON:0000487, UBERON:0006914, UBERON:0006915) with `composed_primarily_of` — the complete intended set, tied with the best codex attempts (#80/#73) and ahead of #439 (1 term), #238 (2 terms), #110 (1 term).
- Documented sound methodology in the PR comment: checked terms out/in with `obo-checkout.pl`/`obo-checkin.pl`, reserialized with `robot convert -i ... -f obo`, then ran a non-destructive `robot convert` parse-validation pass — exactly the workflow the agent config (CLAUDE.md) prescribes — and explicitly reviewed the final git diff to keep the commit focused.
- Strong rationale: notes the prior `has_part` axiom let "any epithelium containing even one squamous epithelial cell" be inferred squamous, and aligned the closely related simple/stratified subtypes together so the branch stays internally consistent.
- Tightly scoped, with no `term_tracker_item` or other extra provenance lines; the only non-axiom delta is a single benign trailing-blank-line removal at EOF in the `vessel_supplies_blood_to` typedef region.

## Issues

- Did not fix `short descending thin limb` (UBERON:0005099), the fourth `has_part CL:0000076` site gold also aligned. The agent's comment claims it "kept related squamous subtype definitions aligned" but this downstream non-squamous-named term was missed — a minor completeness gap, not an error; the issue did not name it.
- Not chargeable for omitting the reasoner-driven endocardium/synovial `is_a` removals (UBERON:0001081, UBERON:0009129, UBERON:0002018) or the CL label refreshes — these are gold's out-of-scope extras negotiated in the PR thread, not derivable from issue #3473.
