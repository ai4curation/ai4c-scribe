---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 238
agent: std_claude_opus-4.7
model: claude-opus-4-7
runtime: claude
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
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn that no well-scoped agent could or should reproduce: CL label-comment refreshes from term renames (CL:1000271 'lung ciliated cell'→'lung multiciliated epithelial cell', CL:0002145, CL:0002332, CL:1000223, CL:0000150 'glandular epithelial cell'→'glandular secretory epithelial cell') and a synonym reordering in UBERON:0003532, all introduced by a `Merge branch 'master'` commit + ROBOT reserialization, plus 3 reasoner-driven is_a deletions (endocardium/synovial) that emerged only from curator research in the PR comment thread. The genuine in-scope content of the issue is ~4 has_part→composed_primarily_of swaps. F1=0.190 with recall=1.000 severely under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent correctly performed the core ontological fix requested by issue #3473: changing the genus-differentia of `squamous epithelium` (UBERON:0006914) from `has_part CL:0000076` to `composed_primarily_of CL:0000076`, and proactively applying the identical fix to `stratified squamous epithelium` (UBERON:0006915), which had the same defective pattern. Recall is 1.000 (every line the agent wrote is in the gold), so the metadiff F1 of 0.190 is entirely a precision artifact: the gold PR mixes the genuine fix with ~11 lines of out-of-scope CL-label refresh and serialization churn plus reasoner-driven cleanup that was negotiated in the PR comment thread, none of which is derivable from the issue. F1 dramatically **under-represents** the quality of this attempt.

## Strengths

- Correctly identified the precise relation swap requested in the issue (`has_part` → `composed_primarily_of` on UBERON:0006914), matching gold exactly.
- Proactively extended the fix to `stratified squamous epithelium` (UBERON:0006915), which the gold PR also fixed — a sound generalization showing genuine understanding that the defective pattern was shared across the squamous branch.
- Surgically scoped diff: exactly 2 changed lines, both correct and both present byte-identically in gold. Precision against the *issue intent* is effectively 1.0.
- The PR comment correctly diagnoses the logical flaw ("an epithelium with even a single squamous cell would be classified as a squamous epithelium") and explicitly flags that other epithelium subclasses (ciliated, columnar) share the pattern and merit a follow-up — good scope discipline (deferring rather than over-editing).

## Issues

- Did not also fix `simple squamous epithelium` (UBERON:0000487) or `short descending thin limb` (UBERON:0005099), both of which gold updated for consistency. This is a minor completeness gap — the issue named only "squamous epithelium" and the agent reasonably generalized to the direct stratified subclass but stopped short of the full branch. Codex attempts (#80/#73) that also caught UBERON:0000487 are slightly more complete here.
- The agent could not (and was not expected to) reproduce the reasoner-driven removal of dubious epithelial `is_a` assertions on endocardium of ventricle / right atrium endocardium / synovial membrane — those edits emerged only after the curator ran the reasoner and researched synovial histology in the PR thread; they are not part of the gold case's predictable scope.
- No syntax/reasoning validation evidence in the PR comment (unlike the codex attempts), though the change is trivially safe.
