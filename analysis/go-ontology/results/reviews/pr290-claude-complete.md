---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 290
agent: std_opencode_kimi
model: kimi-k2.6
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/290
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent fully resolved issue #31969. All ~25 EC-driven `is_a` reparentings match the human PR #31988 exactly (25 `-is_a` removed / 25 `+is_a` added — no misclassification preserved), the three renames were done, the RHEA-aligned definition rewrites were applied, and `term_tracker_item` provenance for #31969 was added to all 25 modified terms. Its diff blob is identical to the gpt-5.5/opencode runs (pr100, pr82). The only deviations from the human are cosmetic definition-string formatting on 2 defs. F1 0.938 slightly *under*-represents the substantive quality, which is essentially a complete and correct resolution.

## Strengths

- Every reparenting in the issue checklist is correct and matches the human: EC 1.17 formate cluster (GO:0008863/GO:0047899 → GO:0016726, GO:0047111 → GO:0016725, GO:0008839 → GO:0016726), EC 1.14 oxygenase/dioxygenase fixes (GO:0010277 → GO:0016709, GO:0050588 → GO:0016702, GO:0018570 → GO:0016708, GO:0004498/GO:0036199/GO:0032441 → GO:0016713, GO:0050616/GO:0102915 → GO:0016717), the 2-OG dioxygenase swaps (GO:0033759/GO:0045431/GO:0047594/GO:0050589 → GO:0050498; GO:0102717/GO:0106145/GO:0102394 → GO:0016706), plus GO:0008762 → GO:0016628, GO:0018525 → GO:0016614, GO:0044684 → GO:0016645, GO:0033717 → GO:0016614, GO:0050607 → GO:0016616.
- Old wrong parents correctly removed, including GO:0008875 on GO:0033717 — avoiding the double-parenting error seen in the copilot attempts.
- All three renames correct (GO:0102394, GO:0050607, GO:0047081) with the matching RHEA/EC-aligned definition rewrites.
- Added #31969 `term_tracker_item` provenance to all 25 edited terms — matching the human's provenance discipline.
- PR comment includes a clear old-parent → new-parent table with EC-mismatch rationale per term.

## Issues

- Did not preserve the three replaced primary labels as synonyms (human added them as RELATED/EXACT synonyms on GO:0047081, GO:0050607, GO:0102394). Minor curation-best-practice miss shared by all attempts except pr353.
- Cosmetic definition-string deviations on the secologanin (GO:0050616) and scopoletin (GO:0106145) definitions: same chemistry, different dash glyph and retained GOC xref vs the human's exact text. Not substantive errors.
