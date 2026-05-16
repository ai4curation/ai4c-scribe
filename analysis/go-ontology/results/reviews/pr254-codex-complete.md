---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 254
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.667
precision: 0.519
recall: 0.933
jaccard: 0.5
outcome: partial_success
failure_modes:
- under_editing
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/254
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 25870 --repo geneontology/go-ontology
    gh pr diff 32008 --repo geneontology/go-ontology
    gh pr diff 254 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly made the main `go-edit.obo` changes for issue #25870: it obsoleted `GO:0018581`, used `GO:0047074` as the replacement, renamed `GO:0047074` to `hydroxyquinol 1,2-dioxygenase activity`, and preserved the old `GO:0047074` label as an exact synonym. The main omission is that it did not remove the `GO:0018581` reaction-participant axioms from `imports/go-catalytic-activities-participants.owl`, which the human PR did to avoid obsolete-term reasoning artifacts. This is a partial success because the core ontology stanza edits are correct but import cleanup is missing.


## Strengths

- Correctly changed `GO:0018581` to an obsolete term with `OBSOLETE.` definition, `is_obsolete: true`, and `replaced_by: GO:0047074`.
- Removed active xrefs and the asserted oxidoreductase parent from the obsolete `GO:0018581` stanza.
- Correctly renamed `GO:0047074` to `hydroxyquinol 1,2-dioxygenase activity`, matching EC:1.13.11.37.
- Added `synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []` to preserve the former `GO:0047074` label.
- Kept the main edit tightly scoped to the two relevant GO terms.


## Issues

- Missed the generated import cleanup: the human PR removed `GO:0018581` participant restrictions from `src/ontology/imports/go-catalytic-activities-participants.owl` because the term is now obsolete.
- Without that cleanup, the obsolete term may still carry generated reaction participant axioms in the import artifacts until regeneration.
- The obsoletion comment is somewhat shorter than the human PR's rationale, but it captures the key sub-reaction/complete-reaction distinction.
