---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 378
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
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

The agent created `preneoplastic lesion` as a new term and placed it as a direct
child of MONDO:0021074 `precancerous condition`, exactly matching the human's
final ontological decision in PR #10111 and the requester's final preference in
the issue thread (`corismall`, 2026-04-01: "make this a child term under
'precancerous condition' rather than pre-malignant neoplasm"). The metadiff F1 of
0.571 substantially **under-represents** the quality: this is a correct,
well-scoped resolution. The compression is entirely attributable to (a) the
eval-environment placeholder ID `MONDO:7770012` versus the production ID
`MONDO:1060215` (a structural difference no agent can avoid in this sandbox),
and (b) a different `creator` ORCID — both metadiff-counted lines that differ
by environment, not by curatorial error.

## Strengths

- **Correct parent.** `is_a: MONDO:0021074 ! precancerous condition` matches the
  gold exactly, including resolving the issue's ontological subtlety: the
  requester explicitly rejected both the exact-synonym route and the
  `pre-malignant neoplasm` (MONDO:0000611) parent. The agent navigated this
  three-way negotiated history correctly.
- **Definition fidelity.** Used the issue's final refined definition verbatim
  ("A precancerous condition characterized by accumulation of some molecular
  alterations necessary for malignant transformation in a clonal proliferation
  of cells...") — matching the gold `def` text exactly.
- **Provenance done well.** Carried `source=` axiom annotation on the `is_a`
  (`source="https://orcid.org/0000-0002-2336-2552"`) and the
  `IAO:0000233` issue-tracker link to #9781 with correct `xsd:anyURI`
  datatype — matching the gold's datatype (contrast haiku attempts which used
  `xsd:string`).
- **Scope discipline.** Single clean term stanza, no extraneous edits, no
  spurious `synonym` line (the issue thread explicitly concluded the label
  should not be a synonym of the parent).
- The PR/issue comments accurately summarize the negotiated rationale.

## Issues

- **Def xref list incomplete (minor, metadiff-scored).** The agent's `def`
  dbxref bracket is `[PMID:37775701, PMID:39754221, PMID:40624726,
  PMID:40684183]`; the gold additionally prepends the requester ORCID
  `https://orcid.org/0000-0002-2336-2552` inside the def xref list. Omitting
  the ORCID from the def provenance is a small completeness gap, though the
  ORCID is still captured on the `is_a` axiom source.
- **ID and creator ORCID differ from gold** (`MONDO:7770012` vs
  `MONDO:1060215`; creator `0000-0002-2336-2552` vs gold's
  `0000-0002-7638-4659`). These are environment artifacts, not curatorial
  errors — the agent cannot know the production next-available ID, and using
  the requester ORCID as creator is a defensible choice in absence of an
  assigned curator. They drive the F1 ceiling but should not be held against
  the agent.
- Net: no substantive issues. This is the best attempt for the case.
