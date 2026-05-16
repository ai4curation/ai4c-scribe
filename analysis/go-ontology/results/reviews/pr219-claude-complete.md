---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 219
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.768
precision: 0.741
recall: 0.796
jaccard: 0.623
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/219
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

This attempt has the lowest metadiff F1 in the cohort (0.768), but that score badly *under*-represents the actual ontological quality. A signature-level comparison of the `is_a`/`name`/`def` changes against the human PR #31988 shows all ~25 reparentings correct (25 `-is_a` removed / 25 `+is_a` added — including correctly removing GO:0008875 on GO:0033717, which the larger copilot/sonnet runs got wrong) and all three renames done. The low line-level F1 is almost entirely explained by two non-scientific factors: it added **zero** #31969 `term_tracker_item` provenance lines (the human added 25, so ~50 lines of "expected" diff are absent on a 369-line gold diff), and ~5 definition strings have formatting drift (dash glyph, `2 H+` vs `2 H(+)`, RHEA-only vs PMID+RHEA xrefs). The reclassification reasoning — the hard part of the issue — is essentially correct.

## Strengths

- Every reparenting correct and matching the human: EC 1.17 formate cluster (GO:0008863/GO:0047899 → GO:0016726, GO:0047111 → GO:0016725, GO:0008839 → GO:0016726), EC 1.14 oxygenase/dioxygenase fixes (GO:0010277, GO:0050588, GO:0018570, GO:0032441, GO:0050616, GO:0102915), the 2-OG dioxygenase swaps (GO:0050498 ↔ GO:0016706), plus GO:0008762 → GO:0016628, GO:0018525 → GO:0016614, GO:0044684 → GO:0016645, GO:0033717 → GO:0016614, GO:0050607 → GO:0016616.
- Old wrong parents correctly removed (25/25), including GO:0008875 on GO:0033717 — a correctness discriminator versus pr504/pr425.
- All three renames correct with the requested RHEA/EC-aligned definition rewrites.
- PR comment articulates the EC-sub-subclass rationale per term group correctly (e.g. "EC class 1.17 = acting on CH or CH2 groups ≠ 1.2 acting on aldehyde or oxo group").

## Issues

- **Missed requirement (systematic, dominant score driver):** added no `term_tracker_item` "…/issues/31969" provenance to any of the 25 modified terms. Because the human applied this uniformly, the absence accounts for the bulk of the precision/recall loss and explains why F1 (0.768) sits far below the cohort despite correct reclassification.
- Did not preserve the three replaced primary labels as synonyms on GO:0047081, GO:0050607, GO:0102394 (human added them). Minor miss shared by all attempts except pr353.
- Definition-string formatting drift on ~5 defs (GO:0044684, GO:0050616, GO:0102915, GO:0032441, GO:0106145): same chemistry, different notation/xref vs the human's exact wording. Not substantive ontology errors but they compound the line-level penalty.
