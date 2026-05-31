---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 252
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.634
precision: 0.481
recall: 0.929
jaccard: 0.464
outcome: partial_success
failure_modes:
- under_editing
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/252
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The smallest-model attempt got the biological direction right — obsoleting `GO:0018581` with `replaced_by: GO:0047074` and renaming `GO:0047074` to the EC accepted name — but missed the same two items as the haiku attempt: the EXACT synonym preserving the former `GO:0047074` label, and the generated OWL import cleanup. The obsoletion mechanics are skill-conformant; the patch is incomplete and the rationale comment is the tersest of the set. F1 0.634 is a fair reflection of two genuine omissions. (Eval base already incorporates companion PR #25904; metadiff vs #32008 is a fair reference, not a partial-gold case.)

## Strengths

- Correct obsoletion of `GO:0018581`: `obsolete `-prefixed name, `OBSOLETE.` definition, all four xrefs and `is_a: GO:0016702` removed, `is_obsolete: true`, `replaced_by: GO:0047074`, both `term_tracker_item` properties retained.
- Renamed `GO:0047074` to `hydroxyquinol 1,2-dioxygenase activity`, matching the EC:1.13.11.37 accepted name and the human PR's intent.
- Stayed tightly scoped — no unrelated terms or files touched.

## Issues

- Omission: did not add `synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []` to `GO:0047074`, so the displaced former label is not preserved for searchability — a real data-quality miss for a rename.
- Omission: did not remove the obsolete `GO:0018581` participant `owl:Class` block from `src/ontology/imports/go-catalytic-activities-participants.owl`.
- The obsoletion comment ("The reason for obsoletion is that this term is equivalent to GO:0047074") is the least informative of any attempt — it states equivalence but omits the sub-reaction/non-enzymatic-second-step rationale that justifies it. Minimal but technically valid provenance.
- PR/issue comments are bare bullet lists with no methodology, impact analysis, or validation evidence.
