---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 406
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/406
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent correctly obsoleted `GO:0018581` and renamed `GO:0047074`, but it omitted two pieces of the human PR: the EXACT synonym preserving the former `GO:0047074` label, and the generated OWL import cleanup. The obsoletion mechanics are skill-conformant and the biological direction is right, but the patch is the most incomplete of the claude-runtime attempts. F1 0.634 is roughly fair given two distinct omissions. (Eval base already incorporates companion PR #25904; metadiff vs #32008 is a fair reference, not a partial-gold case.)

## Strengths

- Correct obsoletion of `GO:0018581`: `obsolete `-prefixed name, `OBSOLETE.` definition, all four xrefs and `is_a: GO:0016702` removed, `is_obsolete: true`, `replaced_by: GO:0047074`, both `term_tracker_item` properties retained.
- Renamed `GO:0047074` to the EC accepted name `hydroxyquinol 1,2-dioxygenase activity`.
- Obsoletion comment captures the sub-reaction rationale and even cross-references the GO:0047074 rename, giving useful provenance.

## Issues

- Omission: did not add `synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []` to `GO:0047074`. The human PR (and the better-scoring attempts) preserved the displaced primary label as an EXACT synonym so the term remains discoverable under its former name; losing it degrades searchability and is a real data-quality miss for a rename.
- Omission: did not remove the obsolete `GO:0018581` participant `owl:Class` block from `src/ontology/imports/go-catalytic-activities-participants.owl`.
- Methodology is thinly documented: the issue/PR comments are a brief status update with no impact analysis or validation evidence, weaker than the sonnet/opus claude attempts on the same case.
