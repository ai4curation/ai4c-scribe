---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 684
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
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
reviewed_at: 2026-05-17
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/684
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent fully resolved issue #31969. All ~25 EC-driven `is_a` reparentings
match the human PR #31988 exactly (25 `-is_a` removed / 25 `+is_a` added — no
misclassification preserved), the three renames were done, the RHEA-aligned
definition rewrites applied, and #31969 `term_tracker_item` provenance added to
every modified term. This run's diff blob (`f15e702`) is byte-identical to
pr685 and substantively equivalent to the 0.956 top runs (pr655); the only
difference from pr655/the human is that the new `term_tracker_item` line is
inserted *before* the pre-existing #30193 line rather than after, plus a
`2 H+` vs `2 H(+)` notation choice. These ordering/notation differences alone
drop the metadiff F1 to 0.920. The score materially *under*-represents the
quality — this is a complete, correct resolution equivalent in substance to
the cohort's best, and consistent with the prior reviewer's `success` rating
of pr192 (identical 0.920 from the same ordering artifact).

## Strengths

- Every reparenting in the issue checklist is correct and matches the human:
  EC 1.17 formate/CH-CH2 cluster (GO:0008863/GO:0047899/GO:0008839 →
  GO:0016726, GO:0047111 → GO:0016725), CH-OH/CH-CH/CH-NH branch fixes
  (GO:0050607 → GO:0016616, GO:0008762 → GO:0016628, GO:0018525 → GO:0016614,
  GO:0044684 → GO:0016645, GO:0033717 → GO:0016614), and the 1.14
  oxygenase/dioxygenase corrections (GO:0102394/GO:0106145/GO:0102717 →
  GO:0016706, GO:0010277/GO:0047081 → GO:0016709, GO:0050588 → GO:0016702,
  GO:0033759/GO:0045431/GO:0047594/GO:0050589 → GO:0050498, GO:0050616/
  GO:0102915 → GO:0016717, GO:0032441/GO:0004498/GO:0036199 → GO:0016713,
  GO:0018570 → GO:0016708).
- Old wrong parents correctly removed, including GO:0008875 on GO:0033717 —
  avoiding the double-parenting error of the copilot attempts.
- All three renames correct (GO:0102394, GO:0050607, GO:0047081) with the
  matching RHEA/EC-aligned definition rewrites; GO:0008762/GO:0018525/
  GO:0044684/GO:0032441 RHEA-aligned definition updates applied.
- Added #31969 `term_tracker_item` provenance to all ~25 edited terms.
- PR write-up documents EC→GO reasoning per reaction class and reports a
  fuller validation chain than its twin (`robot verify` + `robot reason -r
  ELK` + `make travis_build`, pre and post edit).

## Issues

- The new `term_tracker_item` line is inserted before the existing #30193 line
  (human/pr655 place it after). This serialization-ordering convention
  difference has no ontological consequence; it is the dominant driver of the
  0.920 vs 0.956 metadiff gap, not a curation defect.
- Minor definition-string notation differences from the human (`2 H+` vs
  `2 H(+)`, xref-bracket contents) on a couple of defs — same chemistry, not
  substantive.
- Did not preserve the three replaced primary labels as synonyms on GO:0047081/
  GO:0050607/GO:0102394 (the human added them). Minor curation-best-practice
  miss shared by all attempts except pr353.
