---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 54
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: simple
f1: 0.571
precision: 0.571
recall: 0.571
jaccard: 0.400
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

GPT-5.5 (opencode), second run. The produced diff is byte-identical to eval PR
#73 (same blob `a35ae63`): `preneoplastic lesion` created as a direct `is_a`
child of MONDO:0021074 `precancerous condition` with the issue's final refined
definition verbatim. Correct, well-scoped resolution matching human PR #10111;
metadiff F1 of 0.571 **under-represents** quality, with the ceiling set by the
eval placeholder ID and differing `creator` ORCID. The reproducibility across
the two runs is itself a positive signal.

## Strengths

- **Correct parent.** `is_a: MONDO:0021074 ! precancerous condition`, matching
  gold and the requester's final stated preference.
- **Definition fidelity.** Uses the issue's final refined definition text
  verbatim, matching the gold `def`.
- **`is_a` provenance present.** Annotated with
  `{source=<issue URL>, source="https://orcid.org/0000-0002-2336-2552"}`; the
  ORCID source overlaps the gold's source set.
- **Scope discipline.** Single term stanza, no spurious synonym, correct
  `IAO:0000233` issue link with `xsd:anyURI`.
- **Run-to-run determinism.** Identical output to PR #73 — desirable
  consistency for a simple new-term task.

## Issues

- **Def xref omits requester ORCID** (gold leads its def bracket with the
  ORCID; this lists only the four PMIDs). Minor completeness gap.
- **`is_a` source set differs from gold** (issue URL + ORCID vs gold's two
  PMIDs + ORCID). Defensible provenance alternative, not an error.
- ID/creator-ORCID differences from gold are sandbox artifacts that set the F1
  ceiling, not curatorial mistakes. No substantive issues; functionally
  equivalent to PR #73.
