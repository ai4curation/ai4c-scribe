---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 738
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/mondo-agent-config@v3
case_type: new_term
difficulty: simple
case_quality: ok
f1: 0.571
precision: 0.571
recall: 0.571
jaccard: 0.400
outcome: success
failure_modes:
  - wrong_term
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

GPT-5.4 (opencode). The agent correctly created `preneoplastic lesion` as a
direct `is_a` child of MONDO:0021074 `precancerous condition`, matching the
gold PR #10111 classification and the requester's final stated preference in
issue #9781 ("make this a child term under precancerous condition rather than
pre-malignant neoplasm"). The diff is byte-identical to eval PR #684 (same blob
`51ded9b`). Metadiff F1 of 0.571 **under-represents** substantive quality — the
ceiling is set by the eval placeholder ID — but unlike the gpt-5.5 runs this
attempt also has a genuine `creator` defect. Net: a correct, well-scoped
resolution with one real metadata error. The codex review's
`partial_success` / over_editing / under_editing labels are generic
metadiff boilerplate and overstate the problems; the substantive change is
correct.

## Strengths

- **Correct parent.** `is_a: MONDO:0021074 ! precancerous condition` exactly
  matches gold and the requester's final negotiated decision; correctly avoids
  the rejected `pre-malignant neoplasm` (MONDO:0000611) and the rejected
  exact-synonym-of-`precancerous condition` option.
- **Definition substance correct.** Tracks the issue's requester-supplied
  wording ("clonal proliferation of cells that have accumulated some, but not
  all, ... molecular alterations necessary for malignant transformation ...
  intermediate stage in carcinogenesis with increased risk of progression to
  invasive neoplasia"), semantically equivalent to gold's refined phrasing.
- **Scope discipline.** Single `[Term]` stanza, one file, +8/-0; no spurious
  synonym, no collateral edits. Correct `IAO:0000233` issue link with
  `xsd:anyURI`.
- **Run-to-run determinism.** Output identical to PR #684 — desirable
  consistency for a simple new-term task.

## Issues

- **Wrong `creator` value (real error).**
  `property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3`
  attributes term authorship to a journal article DOI. `dc:creator` must be a
  curator/agent ORCID (gold uses `https://orcid.org/0000-0002-7638-4659`); a
  paper DOI here is a misattribution. This field is metadiff-normalized so it
  does not move F1, but it is a genuine curatorial defect, not a sandbox
  artifact.
- **Def xref incomplete.** Lists only `PMID:37775701, PMID:40684183`; the issue
  supplied four PMIDs and gold also leads the bracket with the requester ORCID
  `https://orcid.org/0000-0002-2336-2552`. Minor completeness gap.
- **No `is_a` provenance.** Gold annotates the `is_a` with
  `{source=...}`; this attempt omits it. Minor; defensible for a grouping term.
- ID difference (`MONDO:7770012` placeholder vs gold `MONDO:1060215`) is a
  sandbox artifact that, together with the metadiff-ignored creator field,
  fixes the F1 ceiling at 0.571 — normal under-representation for this case
  (`case_quality: ok`), not a curatorial mistake in itself.
