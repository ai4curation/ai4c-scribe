---
ontology: uberon
issue_number: 3490
pr_number: 3585
eval_repo_pr: 663
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: axiom_repair
difficulty: hard
case_quality: ok
case_quality_reason: metadiff_tiny_freetext_def_ceiling
f1: 0.286
precision: 0.333
recall: 0.250
jaccard: 0.167
outcome: partial_success
failure_modes: [scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent relaxed the UBERON:0005162 def to permit some whole cells ("A
structure consisting primarily of multiple cell components, but which is not
itself a cell and may also have some complete cells as parts."), kept
`[CARO:0001000]`, and resolved issue #3490 in substance. As with its sibling
run #607 it also rewrote the `external_ontology_notes` curator-rationale free
text (the #81 over-reach) and inlined the nuance into a wordier def instead of
gold/FBbt's def+comment split. F1=0.286 reflects the reworded def plus the
changed rationale line; partial_success.

## Strengths

- Definition change is correct and on-target: drops the "does not have
  (complete) cells as a part" restriction while preserving the "primarily
  multiple cell components / not itself a cell" core. Matches issue #3490 and
  FBbt #2008 intent.
- Retained `[CARO:0001000]` def xref — provenance preserved, better than
  gpt-5.5 codex #33 which deleted it.
- No new identifiers/mappings introduced and no `term_tracker_item`/
  `created_by` bloat — cleaner on provenance metadata than #443.
- Strongest documented methodology of these three: obo-checkout/checkin,
  explicit `robot convert` reserialization of uberon-edit.obo, inspected
  representative subclasses, and reviewed the exact git diff before commit —
  the robot-convert step here is a deliberate, scoped reserialization, not
  ODK-driven churn (only the one stanza changed).

## Issues

- Scope creep / questionable edit: rewrote `external_ontology_notes` from the
  curator's FMA-vs-CARO rationale ("we go with the FMA classification rather
  than the CARO one. FMA def: '...'") to the agent's own broader-usage
  framing, deleting the original FMA def text. Unrequested overwrite of
  historical editorial provenance that gold deliberately preserved — same
  over-reach as #81/#607.
- Style/omission vs gold: nuance inlined into one wordier def rather than
  gold/FBbt's clean def + separate `comment:`. Defensible but less aligned
  with the canonical FBbt #2008 form gold adopted.
- Identical diff and blob (67be0cf) to PR #607 — duplicate gpt-5.4/opencode
  run; assessments and outcome are necessarily the same.
- Net: core resolution correct and free of provenance-metadata bloat, but the
  unrequested rewrite of curator rationale free text makes this
  partial_success; metadiff understates def correctness while the rationale
  edit is a genuine scope issue.
