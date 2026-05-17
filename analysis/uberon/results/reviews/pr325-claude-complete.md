---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 325
agent: std_claude_haiku-4.5
model: claude-haiku-4-5-20251001
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.174
precision: 0.105
recall: 0.500
jaccard: 0.095
outcome: success
failure_modes: [under_editing]
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn (CL label-comment refreshes CL:1000271/CL:0002145/CL:0002332/CL:1000223/CL:0000150, synonym reorder in UBERON:0003532) from a master-merge + ROBOT reserialization, plus reasoner-driven endocardium/synovial is_a deletions negotiated only in the PR comment thread. Genuine in-scope content is ~4 has_part→composed_primarily_of swaps; this attempt reproduces 1. F1=0.174 under-represents the correctness of the change made."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This attempt produces an identical diff to attempt #375 (same model claude-haiku-4.5, same blob `1fd45d6`): a correct `has_part CL:0000076` → `composed_primarily_of CL:0000076` swap on `squamous epithelium` (UBERON:0006914) plus an aligned text-definition rewrite, with no propagation to related squamous terms. The attempt file contains only the diff (no PR/issue comment captured). The substantive axiom fix is correct; F1 0.174 is depressed by gold's out-of-scope churn and **under-represents** the in-scope correctness, but the attempt is incomplete vs the cohort best.

## Strengths

- Core logical-definition repair on UBERON:0006914 is exactly correct and matches gold (`composed_primarily_of`, RO:0002473, CL:0000076).
- Text-definition rewrite ("An epithelium that is primarily composed of squamous epithelial cells.") is biologically accurate and replaces a misleading "most superficial layer" gloss — a legitimate, if unrequested, alignment improvement.
- Minimal, clean diff: one stanza, no serialization/provenance noise.

## Issues

- Under-editing: only UBERON:0006914 fixed; `simple squamous epithelium` (UBERON:0000487) and `stratified squamous epithelium` (UBERON:0006915) — also fixed in gold and by the codex attempts — left with the defective `has_part` pattern.
- Text-definition change is extra vs gold and not requested by the issue; defensible but a stylistic deviation, not the required fix.
- No PR comment / methodology evidence captured in the attempt file; no reasoner-testing report despite the issue's explicit "test results of change" instruction.
- Functionally a duplicate run of #375 — no independent signal.
