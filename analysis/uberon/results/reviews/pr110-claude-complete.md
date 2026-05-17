---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 110
agent: std_opencode_gemma4-31b
model: togetherai/google/gemma-4-31B-it
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.190
precision: 0.105
recall: 1.000
jaccard: 0.105
outcome: success
failure_modes: [under_editing]
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn (CL label-comment refreshes CL:1000271/CL:0002145/CL:0002332/CL:1000223/CL:0000150, synonym reorder in UBERON:0003532) from a master-merge + ROBOT reserialization, plus reasoner-driven endocardium/synovial is_a deletions negotiated only in the PR comment thread. The genuine in-scope content is ~4 has_part→composed_primarily_of swaps. F1=0.190 with recall=1.000 severely under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent made exactly the single change the issue's headline requested: `has_part CL:0000076` → `composed_primarily_of CL:0000076` on `squamous epithelium` (UBERON:0006914), which is byte-identical to the corresponding gold line (recall 1.000). It did not generalize the fix to any related term. The metadiff F1 of 0.190 is a pure precision artifact of the gold PR's out-of-scope churn and **under-represents** the correctness of the one change made, though the attempt is the least complete of the cohort.

## Strengths

- The single edit is exactly correct and matches gold: the core ontological repair the issue asked for, on the right term (UBERON:0006914) with the right relation (`composed_primarily_of`, RO:0002473) and the right filler (CL:0000076).
- Clean, minimal diff with no spurious metadata, provenance, or serialization noise — no precision-against-intent problems.
- PR comment correctly states the rationale (single squamous cell should not make an epithelium squamous) and claims verification via `obo-grep.pl` and a check that `composed_primarily_of` is an existing relation.

## Issues

- Under-editing: unlike the Opus (#238) and codex (#80/#73) attempts, this run fixed only UBERON:0006914 and did not propagate the identical defect fix to `stratified squamous epithelium` (UBERON:0006915), `simple squamous epithelium` (UBERON:0000487), or `short descending thin limb` (UBERON:0005099), all of which gold updated. The issue explicitly says "Important to test results of change and fix/align", which signals the need to propagate to subclasses; this was not done.
- No evidence of reasoner testing despite the issue's explicit "test results of change" instruction.
- Could not reproduce the reasoner-driven endocardium/synovial cleanup, but that is unpredictable from the issue and not chargeable to the agent.
