---
ontology: uberon
issue_number: 3490
pr_number: 3585
eval_repo_pr: 607
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
itself a cell and may also have some complete cells as parts."), keeping
`[CARO:0001000]`, which resolves issue #3490 in substance. But it also
rewrote the `external_ontology_notes` curator-rationale free text — the same
over-reach as gpt-5.4 codex #81 — and split the nuance into a wordier def
rather than gold/FBbt's clean def+comment. F1=0.286 reflects the verbose
reworded def plus the changed rationale line; partial_success.

## Strengths

- Definition change is correct and on-target: removes the "does not have
  (complete) cells as a part" restriction while keeping the "primarily
  multiple cell components / not itself a cell" core. Matches issue #3490 and
  FBbt #2008 intent.
- Retained `[CARO:0001000]` def xref — provenance preserved, better than
  gpt-5.5 codex #33 which deleted it.
- Tightly scoped to UBERON:0005162 in uberon-edit.obo; no spurious term edits,
  no `term_tracker_item`/`created_by` provenance bloat (cleaner on that axis
  than #443).
- No new identifiers or mappings introduced (PR comment confirms this and it
  checks out) — avoided #443's speculative FBbt xref.

## Issues

- Scope creep / questionable edit: rewrote `external_ontology_notes` from the
  curator's FMA-vs-CARO rationale ("we go with the FMA classification rather
  than the CARO one. FMA def: '...'") to the agent's own framing about
  broader Uberon usage, deleting the original FMA def text. This overwrites
  historical editorial provenance that the issue never asked to touch and
  that gold deliberately left intact — the weakest scope decision among the
  attempts that kept the CARO xref (identical over-reach to #81).
- Style/omission vs gold: nuance inlined into a single wordier def rather
  than gold/FBbt's clean def + separate clarifying `comment:`. Defensible but
  less aligned with the canonical FBbt #2008 form gold adopted.
- Identical diff and blob (67be0cf) to PR #663 — same model/runtime,
  effectively a duplicate run.
- Net: core resolution correct and scope-clean on provenance metadata, but
  the unrequested rewrite of curator rationale free text pushes this to
  partial_success; metadiff somewhat understates def correctness while the
  rationale edit is a real scope issue.
