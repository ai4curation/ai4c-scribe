---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 655
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.956
precision: 0.931
recall: 0.982
jaccard: 0.915
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/655
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent fully and correctly resolved issue #31969. All ~25 EC-driven `is_a`
reparentings match the human PR #31988 exactly (25 `-is_a` removed / 25 `+is_a`
added — no misclassification preserved), the three renames were done, the
RHEA-aligned definition rewrites were applied, and `term_tracker_item`
provenance for #31969 was added to every modified term. This is the
top-scoring attempt in the 14-run cohort (tied with pr63 at F1=0.956); it also
inserts the new `term_tracker_item` line in the same position as the human
(after the existing #30193 line), which is why it edges out the otherwise
identical-substance 0.920 blob runs. The remaining ~0.044 F1 gap is purely
cosmetic definition-string formatting, so the score very slightly
*under*-represents what is effectively a reference-quality resolution.

## Strengths

- Every reparenting in the issue checklist is correct and matches the human:
  GO:0004498/GO:0036199/GO:0032441 → GO:0016713 (EC 1.14.15.-), GO:0008762 →
  GO:0016628 (EC 1.3.1.- CH-CH), GO:0008839/GO:0008863/GO:0047899 → GO:0016726
  and GO:0047111 → GO:0016725 (EC 1.17 CH/CH2 cluster), GO:0010277 →
  GO:0016709, GO:0050588 → GO:0016702, GO:0018525 → GO:0016614, GO:0018570 →
  GO:0016708, GO:0044684 → GO:0016645, GO:0033717 → GO:0016614, GO:0050616/
  GO:0102915 → GO:0016717, and the 2-OG dioxygenase swaps
  (GO:0033759/GO:0045431/GO:0047594/GO:0050589 → GO:0050498; GO:0102717/
  GO:0106145 → GO:0016706).
- Old wrong parents correctly removed, including the GO:0008875 parent on
  GO:0033717 (replaced cleanly by GO:0016614) — avoiding the double-parenting
  error seen in the copilot attempts.
- The GO:0047081 rename to "3-hydroxy-2-methylpyridine-5-carboxylate
  monooxygenase [NAD(P)H] activity" with its matching definition rewrite was
  applied, and uniquely among the opencode runs the old label was retained as
  a RELATED synonym, matching the human's label-retrievability practice.
- RHEA-aligned definition rewrites applied for GO:0008762 (alpha-D
  stereochemistry, xref → RHEA:12248), GO:0018525 (explicit 2[4Fe-4S]-
  ferredoxin notation), GO:0044684, GO:0032441, GO:0047081, etc.
- Added #31969 `term_tracker_item` provenance to all 25 edited terms, placed in
  the same position as the human curator (after the pre-existing #30193 line).

## Issues

- A few definition strings differ from the human only in xref-bracket contents
  or notation (`2 H+` vs `2 H(+)`, retained vs dropped GOC/PMID provenance) on
  terms such as GO:0102915 and GO:0106145. Same chemistry in every case — these
  are provenance/notation style differences, not substantive errors, and
  account for the entire residual metadiff gap.
- No substantive ontology errors or omissions identified.
