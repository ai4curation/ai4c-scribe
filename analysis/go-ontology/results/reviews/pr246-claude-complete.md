---
ontology: go-ontology
issue_number: 31966
pr_number: 32003
eval_repo_pr: 246
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.889
precision: 0.889
recall: 0.889
jaccard: 0.8
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The smallest model in the cohort (gemma-4-31b) produced a substantively correct obsoletion of GO:0043713 with `replaced_by: GO:0140175` (blob `7fa9725`, F1 = 0.889), fully resolving issue #31966. The diff matches the 0.889 cluster on every required element; the only divergence from the gold is the one-sentence obsoletion comment. The 0.889 metadiff **under-represents** quality — this is a complete, mergeable edit even though the agent's narrative output was minimal.

## Strengths

- All required obsoletion metadata correct and well-formed: `obsolete` name prefix, `OBSOLETE.` def prefix retaining `[GOC:jl, PMID:16957230]`, `is_a: GO:0016616` removed, `is_obsolete: true`, `replaced_by: GO:0140175`, `term_tracker_item` for #31966 — fully conforming to the term-obsoletion skill, which is a strong result for a 31B model.
- Correct replacement target (GO:0140175) and correct stanza-level surgery with no collateral damage.
- Tightly scoped: only the GO:0043713 stanza in `go-edit.obo` changed.
- The obsoletion comment's parenthesization "(2R)-2-hydroxyacid dehydrogenase (NAD+) activity" is, if anything, slightly cleaner than other cluster members.

## Issues

- Style only: terse one-sentence obsoletion comment vs. the gold's three-sentence EC/RHEA explanation — the sole source of the 0.889 score, and consistent with the skill's short exemplar.
- Very thin process documentation: the PR/issue comments are one line each with no impact analysis or validation log. The edit is correct, but unlike the larger models there is no evidence the agent ran QC, checked for internal references, or verified annotation impact. Outcome is success on the artifact, but methodology transparency is weak.
