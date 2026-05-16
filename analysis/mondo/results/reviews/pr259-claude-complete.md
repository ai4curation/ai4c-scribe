---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 259
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: simple
f1: 0.533
precision: 0.571
recall: 0.500
jaccard: 0.364
outcome: partial_success
failure_modes: [over_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Gemma-4-31b created `preneoplastic lesion` as an `is_a` child of MONDO:0021074
`precancerous condition` with the issue's final refined definition verbatim —
the correct ontological decision. However it added a redundant
`synonym: "preneoplastic lesion" EXACT` line whose string is identical to the
`name`, and used a malformed axiom source `source="MONDO:issue_9781"`. The core
term is correct but these defects make it a partial success. F1 of 0.533
roughly tracks the mixed quality (a correct term plus a junk synonym line).

## Strengths

- **Correct parent.** `is_a: MONDO:0021074 ! precancerous condition` matches
  gold and the requester's final preference; PR rationale correctly states the
  concept occurs before neoplasm formation so `pre-malignant neoplasm` is
  inappropriate.
- **Definition fidelity.** Uses the issue's final refined definition text
  verbatim, matching the gold `def` string (PMID order differs but the same
  four PMIDs are present).
- Correct `IAO:0000233` issue-tracker link to #9781 with `xsd:anyURI`.

## Issues

- **Redundant self-synonym (wrong pattern / over-editing).** Adds
  `synonym: "preneoplastic lesion" EXACT [...]` — a string identical to the
  term `name`. A label-equals-synonym entry is meaningless noise and is not
  standard MONDO practice; the gold has no synonym. The issue thread explicitly
  concluded the label should NOT be handled as a synonym, so this also runs
  contrary to the negotiated outcome.
- **Malformed axiom source.** `is_a: MONDO:0021074 {source="MONDO:issue_9781"}`
  — `MONDO:issue_9781` is not a valid CURIE/identifier. The gold uses proper
  `source="PMID:..."` / ORCID values. This is an invalid annotation value.
- **Def xref omits requester ORCID** (gold leads its def bracket with the
  ORCID). Minor relative to the above.
- ID/creator-ORCID differences are sandbox artifacts; the substantive problems
  here are the junk synonym and the malformed source value.
