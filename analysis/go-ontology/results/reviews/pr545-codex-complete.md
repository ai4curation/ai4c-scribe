---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 545
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.881
precision: 0.963
recall: 0.812
jaccard: 0.788
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/545
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 25870 --repo geneontology/go-ontology
    gh pr diff 32008 --repo geneontology/go-ontology
    gh pr diff 545 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly implemented the substantive resolution for issue #25870: `GO:0018581` was obsoleted with `replaced_by: GO:0047074`, `GO:0047074` was renamed to `hydroxyquinol 1,2-dioxygenase activity`, and the obsolete term's reaction-participant axioms were removed from generated import artifacts. The metadiff F1 of 0.881 reflects mostly minor differences: a shorter obsoletion comment, a source qualifier on `MetaCyc:RXN-10137`, and an extra `.obo` import cleanup in addition to the human PR's `.owl` cleanup. This is a successful attempt with small style/provenance differences.


## Strengths

- Correctly obsoleted `GO:0018581`, removed its active EC/MetaCyc/RHEA/UM-BBD xrefs and asserted parent, added `is_obsolete: true`, and added `replaced_by: GO:0047074`.
- Correctly renamed `GO:0047074` to the EC accepted label `hydroxyquinol 1,2-dioxygenase activity`.
- Preserved the old `GO:0047074` label as an exact synonym.
- Removed the `GO:0018581` reaction-participant axioms from `go-catalytic-activities-participants.owl`, preventing an obsolete term from retaining imported participant restrictions.
- The extra cleanup in `go-catalytic-activities-participants.obo` is consistent with the same generated import content and is not biologically harmful.


## Issues

- The obsoletion comment is less precise than the human PR's comment; it says only that `GO:0018581` represents a sub-reaction, while the human PR explicitly explains the non-enzymatic conversion step and equivalence to `GO:0047074`.
- The agent changed `MetaCyc:RXN-10137` on `GO:0047074` to include `{source="skos:narrowMatch"}`. The human PR did not alter that xref, so this extra assertion should be curator-reviewed.
- No wrong replacement, missing obsoletion metadata, or serious scope problem was found.
