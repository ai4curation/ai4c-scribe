---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 41
agent: std_opencode_g55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.167
precision: 0.105
recall: 0.400
jaccard: 0.091
outcome: success
failure_modes: [under_editing]
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn (CL label-comment refreshes CL:1000271/CL:0002145/CL:0002332/CL:1000223/CL:0000150, synonym reorder in UBERON:0003532) from a master-merge + ROBOT reserialization, plus reasoner-driven endocardium/synovial is_a deletions negotiated only in the PR comment thread. Genuine in-scope content is ~4 has_part→composed_primarily_of swaps; this attempt's diff reproduces 1, though the PR comment claims 3. F1=0.167 under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

Same model/blob as attempt #59 (`a415c02`): the captured diff fixes only `squamous epithelium` (UBERON:0006914) — `has_part CL:0000076` → `composed_primarily_of CL:0000076` (matches gold) — plus a text-definition rewrite and a `term_tracker_item` property. Notably, the PR comment *claims* it also updated `simple squamous epithelium` (UBERON:0000487) and `stratified squamous epithelium` (UBERON:0006915), but the committed diff for this eval PR shows only the UBERON:0006914 stanza. The core axiom fix is correct; F1 0.167 is depressed by gold's out-of-scope churn and **under-represents** the in-scope correctness.

## Strengths

- Core logical-definition repair on UBERON:0006914 is exactly correct (`composed_primarily_of`, RO:0002473, CL:0000076), matching gold.
- Text-definition rewrite is biologically accurate and improves the prior misleading gloss.
- Reported methodology is thorough: PR comment claims ELK reasoning plus a query confirming `simple/stratified squamous epithelium` still classify under `squamous epithelium` while `short descending thin limb` no longer does — exactly the kind of "test results of change" verification the issue asks for.

## Issues

- Comment/diff mismatch: the PR comment asserts UBERON:0000487 and UBERON:0006915 were also updated, but the captured agent diff contains only the UBERON:0006914 stanza. Either the other edits were lost in commit/serialization or the comment over-claims. Effective completeness is under-editing (one term) regardless.
- Under-editing relative to gold and the codex attempts, which fixed all three squamous classes.
- Text-definition rewrite and `term_tracker_item` are extra vs gold and unrequested by the issue; defensible but reduce precision against gold.
- Reasoner-driven endocardium/synovial cleanup not reproduced — unpredictable from the issue, not chargeable.
