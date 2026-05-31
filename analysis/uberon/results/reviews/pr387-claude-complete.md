---
ontology: uberon
issue_number: 3602
pr_number: 3603
eval_repo_pr: 387
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: simple
case_quality: good
f1: 0.923
precision: 1.000
recall: 0.857
jaccard: 0.857
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/codex added `UBERON:8600149` "occlusal surface of tooth" as a
subclass of `UBERON:8600148` "tooth surface structure", reproducing the gold
PR #3603 term stanza essentially line-for-line: same ID, name, definition
with *both* issue cross-references (`dentaleducationhub.com` + HL7
`CodeSystem-FDI-surface.html`), EXACT synonym `"occlusal surface"` with the
dentaleducationhub reference, correct `is_a` parent, and wdduncan's requester
ORCID `0000-0001-9625-1899`. Metadiff F1=0.923 (P=1.000, R=0.857)
**under-represents** quality: precision is perfect and the only recall gap is
the two CLAUDE.md-mandated metadata lines (`term_tracker_item`,
`created_by`). Notably this codex run produced a *cleaner* diff than the
opencode siblings (#609/#668) — no trailing-newline churn, because `robot`
was unavailable and the agent honestly disclosed it. Clean `success`.

## Strengths

- **Term content matches gold exactly**: id `UBERON:8600149`, name, full def
  text, *both* def xrefs, EXACT synonym `"occlusal surface"` with the
  dentaleducationhub reference, `is_a: UBERON:8600148 ! tooth surface
  structure`, and `relationship: dc-contributor
  https://orcid.org/0000-0001-9625-1899` — the exact ORCID the gold uses.
- **No serialization churn**: the diff is a single clean term-stanza
  insertion with zero collateral edits — the tightest scope of all attempts
  in this case.
- **Honest environment disclosure**: explicitly reported that `robot` was
  not installed (`robot: command not found`) so the prescribed
  reserialization step could not run, rather than silently skipping it or
  fabricating success. Good methodology under a tooling limitation.
- **Followed CLAUDE.md metadata guidance**: added `term_tracker_item`
  pointing at issue #3602 and `created_by: dragon-ai-agent`, both required
  by the agent config (absent from the minimal gold, hence the recall dip).
- **Sound verification**: PR comment documents parent-existence check,
  ID-availability check, sibling-pattern alignment, and diff scope check.

## Issues

- **No genuine ontological issues.** The entire F1 gap is the two
  CLAUDE.md-required metadata lines that the minimal gold stanza omits;
  substantively the term is correct, complete, and well-formed. The missed
  `robot convert` step is a documented environment limitation, not an agent
  fault, and produced no defect here.
