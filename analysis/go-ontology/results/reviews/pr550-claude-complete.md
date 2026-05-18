---
ontology: go-ontology
issue_number: 25870
pr_number: 32008
eval_repo_pr: 550
agent: std_codex_g54
model: gpt-5.4
runtime: codex
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
- missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-17'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/550
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent produced a correct, skill-conformant obsoletion of `GO:0018581` and
rename of `GO:0047074` in `go-edit.obo` that — unlike the opencode attempts —
correctly adds the EXACT synonym preserving the prior `GO:0047074` label,
exactly matching the gold `go-edit.obo` stanza edits. Its sole substantive
omission is the `imports/go-catalytic-activities-participants.owl` cleanup: the
agent did not remove the obsolete term's participant axiom block, so the
reasoner would still infer `RO:0000057` restrictions on an obsolete class. F1
0.667 (precision 0.519 / recall 0.933) understates the quality of the core
curation: the precision penalty is structural — the agent matched the gold's
`go-edit.obo` block well but produced none of the gold's 31-line `.owl`
deletions, so the diffs only partially align. The eval base already includes
companion PR #25904, so metadiff vs #32008 is a sound reference and this is not a
partial-gold case.

## Strengths

- Correct, complete obsoletion of `GO:0018581`: `obsolete `-prefixed name,
  `OBSOLETE.` definition, all four xrefs (`EC:1.13.11.37`, `MetaCyc:RXN-17556`,
  `RHEA:19441`, `UM-BBD_reactionID:r0232`) and `is_a: GO:0016702` removed,
  `is_obsolete: true`, `replaced_by: GO:0047074`, both `term_tracker_item`
  provenance properties retained — matching gold exactly.
- Renamed `GO:0047074` to the EC:1.13.11.37 accepted label
  `hydroxyquinol 1,2-dioxygenase activity` AND added
  `synonym: "4-hydroxycatechol 1,2-dioxygenase activity" EXACT []` — the full
  rename + synonym preservation the opencode attempts (#586, #662) missed. This
  is the most accurate `go-edit.obo` reproduction of the three reviewed here.
- Strong methodology and scope discipline: PR comment documents term-obsoletion,
  reaction, and mapping skill consultation, confirms zero direct annotations to
  migrate for `GO:0018581`, and a RESEARCH.md checking `EC:1.13.11.37`,
  `RHEA:19441`, `RHEA:35595`. Tightly scoped to the single edit file.

## Issues

- Omission (`under_editing` / `missed_requirement`): did not remove the
  four-restriction `GO_0018581` `owl:Class` participant block (`RO:0000057` to
  CHEBI:15378/15379/16971/58139) from
  `src/ontology/imports/go-catalytic-activities-participants.owl`. The human PR
  performed this deletion precisely to stop the reasoner inferring participant
  restrictions on an obsolete term — the explicit rationale the gold author gave
  on the issue thread. This is the only substantive gap and the dominant driver
  of the depressed F1.
- The agent's checklist notes incomplete local validation (`robot` absent,
  `make travis_build` failed on missing `amm`); plausibly why the generated OWL
  import side-effect was not detected. The core OBO edit remains valid and
  curator-ready, but a reasoner pass would have surfaced the missing cleanup.
