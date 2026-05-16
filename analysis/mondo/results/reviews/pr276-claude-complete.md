---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 276
agent: std_opencode_kimi
model: kimi-k2.6
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

Kimi-K2.6 created `preneoplastic lesion` as a direct `is_a` child of
MONDO:0021074 `precancerous condition` with the issue's final refined
definition verbatim. This is a correct, well-scoped resolution that matches the
human's PR #10111 ontologically and follows the negotiated outcome in the issue
thread. The metadiff F1 of 0.571 **under-represents** quality; the ceiling is
driven by the eval placeholder ID (`MONDO:7770012` vs production
`MONDO:1060215`) and a differing `creator` ORCID, neither of which is a
curatorial error.

## Strengths

- **Correct parent and ontological reasoning.** The PR comment explicitly and
  correctly reconstructs the issue negotiation: not an exact synonym of
  `precancerous condition` (because CHIP would then wrongly be a preneoplastic
  lesion), and not under `pre-malignant neoplasm` (MONDO:0000611) because the
  concept is pre-neoplasm. Resolves to `is_a: MONDO:0021074`, matching gold.
- **Definition fidelity.** Uses the issue's final refined definition text
  exactly, matching the gold `def` string.
- **Clean scope.** Single term stanza; no synonym line (correctly, since the
  thread concluded the label should not be a synonym); `IAO:0000233` link to
  #9781 with correct `xsd:anyURI` datatype.
- **Documented validation.** PR comment reports `make NORM` and
  `robot convert` syntax validation were run.

## Issues

- **`is_a` lacks `source=` axiom annotations.** The gold annotates the `is_a`
  with `{source="PMID:37775701", source="PMID:40684183",
  source="https://orcid.org/0000-0002-2336-2552"}`; this attempt has a bare
  `is_a: MONDO:0021074 ! precancerous condition`. Minor provenance omission;
  the parent assertion itself is correct.
- **Def xref omits requester ORCID.** Gold's def bracket leads with
  `https://orcid.org/0000-0002-2336-2552`; this attempt lists only the four
  PMIDs. Small completeness gap.
- **creator ORCID differs from gold** (`0000-0001-5208-3432`, the model's
  configured curator identity, vs gold `0000-0002-7638-4659`). Environment
  artifact, not an error; contributes to the F1 ceiling but should not be held
  against the agent.
- ID `MONDO:7770012` vs production `MONDO:1060215` — unavoidable sandbox
  artifact. No substantive curatorial issues.
