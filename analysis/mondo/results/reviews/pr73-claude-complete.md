---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 73
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

GPT-5.5 (opencode) created `preneoplastic lesion` as a direct `is_a` child of
MONDO:0021074 `precancerous condition`, using the issue's final refined
definition verbatim. The ontological decision matches human PR #10111 and the
requester's final preference. This is a correct, well-scoped resolution; the
metadiff F1 of 0.571 **under-represents** quality, with the ceiling driven by
the eval placeholder ID and a differing `creator` ORCID line.

## Strengths

- **Correct parent.** `is_a: MONDO:0021074 ! precancerous condition`, matching
  gold; the PR rationale correctly explains why neither exact-synonym nor
  `pre-malignant neoplasm` was appropriate.
- **Definition fidelity.** Issue's final definition text used verbatim,
  matching the gold `def` string.
- **Richer `is_a` provenance than most attempts.** Annotates the parent axiom
  with `{source="https://github.com/monarch-initiative/mondo/issues/9781",
  source="https://orcid.org/0000-0002-2336-2552"}`. This overlaps partially
  with the gold's `source=` set (gold uses two PMIDs + the ORCID); the ORCID
  source matches.
- **Scope discipline.** Single term stanza, no synonym line, correct
  `IAO:0000233` link to #9781 with `xsd:anyURI`.
- **Honest methodology disclosure.** PR comment transparently notes `aurelian`
  was unavailable and ODK/Docker was unavailable so `make NORM` could not run —
  good provenance honesty rather than false claims.

## Issues

- **Def xref omits requester ORCID.** Gold's def bracket leads with
  `https://orcid.org/0000-0002-2336-2552`; this attempt lists only the four
  PMIDs. Minor completeness gap (the ORCID is captured on the `is_a` source
  instead).
- **`is_a` source set differs from gold.** Gold uses
  `{source="PMID:37775701", source="PMID:40684183", source=<ORCID>}`; this uses
  the issue URL + ORCID. Defensible alternative provenance, not an error.
- **Normalization not applied** (ODK unavailable in environment). The serialized
  stanza is still syntactically valid OBO; this is an environment limitation,
  not agent fault.
- ID/creator-ORCID differences from gold are sandbox artifacts driving the F1
  ceiling, not curatorial errors. No substantive issues.
