---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 192
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.92
precision: 0.897
recall: 0.945
jaccard: 0.852
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/192
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent fully resolved issue #31969: all ~25 EC-driven `is_a` reparentings match the human PR #31988 exactly (25 removed / 25 added — no misclassification preserved), all three renames done, the RHEA-aligned definition rewrites applied, and #31969 `term_tracker_item` provenance added to all 25 modified terms. The reparenting and provenance — the substance of the issue — are essentially perfect. The 0.92 F1 is driven entirely by definition-string formatting choices on 3 defs (xref bracket contents and dash/notation), which slightly *under*-represents the actual quality.

## Strengths

- Every reparenting correct and matching the human, with the EC→GO logic explicitly explained in the PR comment grouped by reaction class (EC 1.17.* CH/CH2, EC 1.14.20.* → GO:0050498, EC 1.5.99.* → GO:0016645, etc.).
- Old wrong parents correctly removed, including GO:0008875 on GO:0033717 — avoiding the double-parenting error of the copilot attempts.
- All three renames correct (GO:0102394, GO:0050607, GO:0047081) with the matching RHEA/EC-aligned definition rewrites.
- Added #31969 `term_tracker_item` provenance to all 25 edited terms — matching the human's provenance discipline (one of the minority of attempts that did this).
- The PR write-up demonstrates genuine domain reasoning, e.g. justifying GO:0102915's expanded definition (also catalyzes (+)-sesamin formation) from the existing PMID-backed description.

## Issues

- Definition-xref deviations from the human's exact wording: for GO:0106145 (scopoletin) the agent used `[RHEA:57848]` alone whereas the human kept `[PMID:29361149, PMID:29581584, RHEA:57848]`; similarly minor xref differences on GO:0102915 and GO:0032441 (`2 H+` vs `2 H(+)`). Same chemistry in each case — these are provenance/notation style differences, not substantive errors, but they reduce fidelity to the requested RHEA wording and the existing publication support.
- Did not preserve the three replaced primary labels as synonyms on GO:0047081, GO:0050607, GO:0102394 (human added them). Minor curation-best-practice miss shared by all attempts except pr353.
