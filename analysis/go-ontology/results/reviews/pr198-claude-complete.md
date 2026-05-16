---
ontology: go-ontology
issue_number: 31876
pr_number: 31953
eval_repo_pr: 198
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 1.0
precision: 1.0
recall: 1.0
jaccard: 1.0
outcome: partial_success
failure_modes:
- over_editing
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

## Summary

The claude-haiku-4.5 agent correctly obsoleted GO:0140057 "vacuole-mitochondria membrane tethering" with all required obsoletion metadata and no replacement, matching the ontological substance of the human gold PR #31953. Like the opus attempt (#333), it additionally **deleted `created_by: pg` and `creation_date: 2017-06-27T10:31:12Z`**, diverging from the human gold which retained them. The metadiff F1=1.0 over-represents quality because the normalization masks this provenance deletion; the outcome is partial_success. The diff resolves to blob `bb3b5b7`, identical to attempt #333.

## Strengths

- Correctly targeted GO:0140057; edits confined to `src/ontology/go-edit.obo`; GO:0140058 untouched.
- Full obsoletion metadata: `obsolete ` name prefix, `OBSOLETE.` def prefix with original text and `[PMID:27875684]`, obsoletion-reason `comment`, `term_tracker_item` with `xsd:anyURI`, `is_obsolete: true`.
- Removed the only logical axiom (`is_a: GO:0140056`), leaving no logical axioms.
- Correctly added no `replaced_by`/`consider` — appropriate for a term added in error.
- Impact analysis identified the remaining PomBase annotation (SPAC23H4.14, TAS) and noted it was already removed by PomBase; checked internal references and subsets.

## Issues

- **Provenance deletion (over-editing)**: removed `created_by: pg` and `creation_date: 2017-06-27T10:31:12Z`. The human gold retained both. The agent's PR comment explicitly rationalizes this ("Original creation metadata ... removed as per GO obsoletion standards"), which is an incorrect statement of GO practice — GO retains creation metadata on obsolete terms as historical provenance. The error is partly traceable to the term-obsoletion skill exemplar (GO:0000170) omitting these fields, but the human standard is to keep them.
- Self-contradiction in the PR notes: the validation checklist claims "Definition preserved" and "Historical provenance preserved" while the same comment states creation metadata was removed — the agent's reasoning about provenance was internally inconsistent.
- Metadiff F1=1.0 does not penalize the deletion, so the score over-represents fidelity relative to the provenance-preserving attempts (#456, #376, #256, etc.).
