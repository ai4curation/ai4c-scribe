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
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/25870
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32008
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/254
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent produced a correct, skill-conformant obsoletion of `GO:0018581` and rename of `GO:0047074` in `go-edit.obo`, matching the gold PR's stanza edits, but did not remove the obsolete term's participant axioms from the generated OWL import. The `go-edit.obo` diff is essentially identical to the human PR; the lone substantive omission is the `imports/go-catalytic-activities-participants.owl` cleanup. F1 0.667 understates the quality of the core curation. Notably, the agent's PR comment explicitly and correctly identified that the earlier issue checklist had already been handled in prior work for #30193 — consistent with companion PR #25904 being merged before this eval base. (Metadiff vs #32008 is a fair reference; not a partial-gold case.)

## Strengths

- Correct obsoletion of `GO:0018581`: `obsolete `-prefixed name, `OBSOLETE.` definition, all four xrefs and `is_a: GO:0016702` removed, `is_obsolete: true`, `replaced_by: GO:0047074`, both `term_tracker_item` properties retained.
- Renamed `GO:0047074` to `hydroxyquinol 1,2-dioxygenase activity` and added `4-hydroxycatechol 1,2-dioxygenase activity` as an EXACT synonym — matching the human PR exactly.
- Demonstrated good situational awareness: PR comment explicitly enumerated the original issue checklist items already completed (EC qualifiers, removed EC synonyms, RHEA def, MetaCyc replacements) and correctly scoped the remaining work to obsoletion + rename. This avoided re-doing or conflicting with the prior fixes — the right judgment call.
- Checked for internal references to `GO:0018581` (none found) before obsoleting; tightly scoped diff.

## Issues

- Omission: did not remove the `GO:0018581` `owl:Class` participant block (four `RO:0000057` restrictions) from `src/ontology/imports/go-catalytic-activities-participants.owl`, which the human PR did to avoid obsolete-term reasoning artifacts. This is the sole recall gap vs the gold PR.
- The obsoletion comment ("equivalent to GO:0047074 4-hydroxycatechol 1,2-dioxygenase activity") references the pre-rename label of `GO:0047074` within the same PR that renames it, leaving a minor internal inconsistency; the human comment uses the new/EC name. Cosmetic, not an error.
