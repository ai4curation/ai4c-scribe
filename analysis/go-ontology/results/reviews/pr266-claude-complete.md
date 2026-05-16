---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 266
agent: std_opencode_gemma431b
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: reclassification
difficulty: hard
f1: 0.867
precision: 0.845
recall: 0.891
jaccard: 0.766
outcome: partial_success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/266
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

A strong result for the smallest model in the cohort. All ~25 EC-driven `is_a` reparentings match the human PR #31988 exactly (25 `-is_a` removed / 25 `+is_a` added — including correctly removing GO:0008875 on GO:0033717, which the larger copilot/sonnet runs got wrong), all three renames done, and the RHEA-aligned definition rewrites applied. The 0.867 F1 is driven by two non-scientific factors: it added **zero** #31969 `term_tracker_item` provenance lines (human added 25), and several definition strings have formatting drift vs the human's exact wording. The core ontological reasoning is essentially correct, so the metadiff F1 *under*-represents the substantive quality of the reclassification work.

## Strengths

- Every reparenting correct and matching the human: EC 1.17 formate cluster (GO:0008863/GO:0047899 → GO:0016726, GO:0047111 → GO:0016725, GO:0008839 → GO:0016726), EC 1.14 oxygenase/dioxygenase fixes (GO:0010277 → GO:0016709, GO:0050588 → GO:0016702, GO:0032441, GO:0050616, GO:0102915), the 2-OG dioxygenase swaps (GO:0033759/GO:0045431/GO:0047594/GO:0050589 → GO:0050498; GO:0102717/GO:0106145/GO:0102394 → GO:0016706), plus GO:0008762 → GO:0016628, GO:0018525 → GO:0016614, GO:0044684 → GO:0016645, GO:0033717 → GO:0016614, GO:0050607 → GO:0016616.
- Old wrong parents correctly removed (25/25), including GO:0008875 on GO:0033717 — a discriminator versus the copilot attempts that double-parented this term.
- All three renames correct with the requested RHEA/EC-aligned definition rewrites and updated def xrefs (RHEA:28502, RHEA:12248, RHEA:42804, RHEA:32115, RHEA:20585).
- Clear, accurate per-term summary in the PR comment.

## Issues

- **Missed requirement (systematic):** added no `term_tracker_item` "…/issues/31969" provenance to any of the 25 modified terms; the human added it uniformly.
- Did not preserve the three replaced primary labels as synonyms on GO:0047081, GO:0050607, GO:0102394 (human added them). Minor miss shared by all attempts except pr353.
- Definition-string formatting drift on several terms (dihydromethanopterin GO:0044684, secologanin GO:0050616, scopoletin GO:0106145): same chemistry but different dash glyph / xref bracket contents vs the human's exact wording. Not substantive errors but contribute to the lower line-level F1.
