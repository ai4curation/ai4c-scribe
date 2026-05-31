---
ontology: go-ontology
issue_number: 31969
pr_number: 31988
eval_repo_pr: 63
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31969
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31988
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/63
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

This is the strongest attempt in the cohort. The agent fully resolved issue #31969: all ~25 EC-driven `is_a` reparentings match the human PR #31988 exactly, all three renames were done, the requested RHEA-aligned definition rewrites were applied, and `term_tracker_item` provenance for #31969 was added to every modified term (25 links, matching the human). A line-signature comparison against the human diff shows 53/54 significant change-lines identical — the only discrepancy is a one-character notation difference in a single definition. The metadiff F1 of 0.956 slightly *under*-represents the quality here: the substance is essentially a perfect match, and the residual gap is cosmetic.

## Strengths

- Every reparenting in the issue checklist was performed correctly and matches the human: the EC 1.17 formate group (GO:0008863, GO:0047899 → GO:0016726; GO:0047111 → GO:0016725; GO:0008839 → GO:0016726), the EC 1.14 oxygenase/dioxygenase fixes (GO:0010277 → GO:0016709; GO:0050588 → GO:0016702; GO:0018570 → GO:0016708; GO:0004498/GO:0036199/GO:0032441 → GO:0016713; GO:0050616/GO:0102915 → GO:0016717), the 2-OG dioxygenase swaps (GO:0033759/GO:0045431/GO:0047594/GO:0050589 → GO:0050498; GO:0102717/GO:0106145/GO:0102394 → GO:0016706), and GO:0008762 → GO:0016628, GO:0018525 → GO:0016614, GO:0044684 → GO:0016645, GO:0033717 → GO:0016614, GO:0050607 → GO:0016616.
- Old wrong parents were correctly *removed* (25 `-is_a` / 25 `+is_a`), so no misclassification is preserved — a discriminator versus the copilot attempts that double-parented GO:0033717.
- Renamed GO:0102394 → "L-isoleucine 4-hydroxylase activity", GO:0050607 → "S-(hydroxymethyl)mycothiol dehydrogenase activity", and GO:0047081 → "3-hydroxy-2-methylpyridine-5-carboxylate monooxygenase [NAD(P)H] activity", each with the matching RHEA/EC-aligned definition rewrite.
- Added the #31969 `term_tracker_item` provenance to all 25 edited terms, exactly matching the human's provenance discipline (only this attempt, pr192, pr353, and the opencode runs did this).
- Documented methodology well: pre/post `make travis_build` validation, RESEARCH.md, checkout/checkin workflow, and an explicit rationale for removing the GO:0008875 parent on GO:0033717.

## Issues

- Did not preserve the three replaced primary labels as synonyms. The human added "3-hydroxy-2-methylpyridinecarboxylate dioxygenase [NAD(P)H] activity" (RELATED) on GO:0047081, "mycothiol-dependent formaldehyde dehydrogenase activity" (EXACT) on GO:0050607, and "4-hydroxy-L-isoleucine dehydrogenase activity" (RELATED) on GO:0102394. Dropping old labels on rename loses retrievability and is a minor curation-best-practice miss (only pr353 got this right).
- GO:0032441 definition used `2 H+` where the human PR and the issue text specified `2 H(+)`. Pure notation/style mismatch, not a substantive error.
