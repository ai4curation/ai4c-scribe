---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 100
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.938
precision: 0.914
recall: 0.964
jaccard: 0.883
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/100
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent fully resolved issue #31969. All ~25 EC-driven `is_a` reparentings match the human PR #31988 exactly (25 removed / 25 added — no misclassification preserved), the three renames were done, the RHEA-aligned definition rewrites were applied, and `term_tracker_item` provenance for #31969 was added to all 25 modified terms. The diff blob is identical to pr290 (kimi) and pr82 (gpt-5.5/opencode). The only deviations from the human are cosmetic definition-string formatting on 2 defs. F1 0.938 slightly *under*-represents the quality — substantively this is a complete and correct resolution.

## Strengths

- Every reparenting in the issue checklist is correct and matches the human: the EC 1.17 formate cluster, the EC 1.14 oxygenase/dioxygenase fixes, the GO:0050498 ↔ GO:0016706 2-OG dioxygenase swaps, plus GO:0008762 → GO:0016628, GO:0018525 → GO:0016614, GO:0044684 → GO:0016645, GO:0033717 → GO:0016614, GO:0050607 → GO:0016616.
- Old wrong parents correctly removed, including GO:0008875 on GO:0033717 (no double-parenting, unlike the copilot attempts).
- All three renames correct (GO:0102394, GO:0050607, GO:0047081) with matching RHEA/EC-aligned definition rewrites.
- Added #31969 `term_tracker_item` provenance to all 25 edited terms — matching the human's provenance discipline.
- Validated with `make travis_build` and used the checkout/checkin workflow per instructions.

## Issues

- Did not preserve the three replaced primary labels as synonyms (human added them on GO:0047081, GO:0050607, GO:0102394). Minor curation-best-practice miss shared by all attempts except pr353.
- Cosmetic definition-string deviations on the secologanin (GO:0050616) and scopoletin (GO:0106145) definitions: same chemistry, different dash glyph / retained GOC xref vs the human's exact wording. Not substantive errors.
