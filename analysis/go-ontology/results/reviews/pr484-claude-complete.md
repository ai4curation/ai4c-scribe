---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 484
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.929
precision: 0.897
recall: 0.963
jaccard: 0.867
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/484
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent got the hard ontological reasoning right — all ~25 EC-driven `is_a` reparentings match the human PR #31988 exactly (25 `-is_a` removed / 25 `+is_a` added, no misclassification preserved), all three renames done, and the RHEA-aligned definition rewrites applied. However it added **zero** `term_tracker_item` #31969 provenance lines, whereas the human added one to all 25 modified terms. This is a systematic missed requirement (the provenance pattern is standard GO practice and was applied uniformly by the human), which is the main reason F1 is 0.929 rather than ~0.95. The metadiff F1 is a fair reflection: the core science is correct, but a consistent metadata step was skipped.

## Strengths

- All reparentings correct and matching the human: EC 1.17 formate cluster (GO:0008863/GO:0047899 → GO:0016726, GO:0047111 → GO:0016725, GO:0008839 → GO:0016726), EC 1.14 oxygenase/dioxygenase fixes (GO:0010277 → GO:0016709, GO:0050588 → GO:0016702, GO:0018570 → GO:0016708, GO:0032441 → GO:0016713, GO:0050616/GO:0102915 → GO:0016717), the 2-OG dioxygenase swaps (GO:0033759/GO:0045431/GO:0047594/GO:0050589 → GO:0050498; GO:0102717/GO:0106145/GO:0102394 → GO:0016706), plus GO:0008762 → GO:0016628, GO:0018525 → GO:0016614, GO:0044684 → GO:0016645, GO:0033717 → GO:0016614, GO:0050607 → GO:0016616.
- Old wrong parents correctly removed, including GO:0008875 on GO:0033717 — avoiding the double-parenting error the copilot/sonnet attempts (pr504, pr425) made on this same term.
- All three renames correct (GO:0102394, GO:0050607, GO:0047081) with the requested RHEA/EC-aligned definition rewrites.
- PR comment organizes the changes by target EC parent class with clear rationale, indicating the EC→GO logic was reasoned rather than guessed.

## Issues

- **Missed requirement (systematic):** added no `term_tracker_item` "…/issues/31969" provenance to any of the 25 modified terms. The human added it to every term; this is the dominant contributor to the precision/recall gap and represents a uniformly skipped metadata step.
- Did not preserve the three replaced primary labels as synonyms on GO:0047081, GO:0050607, GO:0102394 (human added them as RELATED/EXACT). Minor curation-best-practice miss shared by all attempts except pr353.
- Minor cosmetic definition-string formatting deviations vs the human's exact wording (dash glyph / xref bracket contents). Not substantive errors.
