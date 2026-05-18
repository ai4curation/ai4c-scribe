---
ontology: mondo
issue_number: 9781
pr_number: 10111
eval_repo_pr: 684
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

GPT-5.4 (opencode), companion run to eval PR #738 — the diff is byte-identical
(same blob `51ded9b`). The agent correctly created `preneoplastic lesion` as a
direct `is_a` child of MONDO:0021074 `precancerous condition`, matching gold PR
#10111 and the requester's final decision in issue #9781 (child of
`precancerous condition`, not `pre-malignant neoplasm`, not an exact synonym).
Metadiff F1 of 0.571 **under-represents** the substantive quality (ceiling set
by the eval placeholder ID), but the attempt carries one genuine `creator`
metadata defect. Net: correct, well-scoped resolution with a real attribution
error. The codex review's `partial_success` / over_editing / under_editing
verdict is generic metadiff boilerplate and overstates the issues.

## Strengths

- **Correct parent.** `is_a: MONDO:0021074 ! precancerous condition` matches
  gold and the requester's final negotiated outcome; correctly avoids the
  rejected `pre-malignant neoplasm` (MONDO:0000611) and the rejected
  exact-synonym option.
- **Definition substance correct.** Uses the requester-supplied wording
  ("clonal proliferation of cells that have accumulated some, but not all, ...
  molecular alterations necessary for malignant transformation ... increased
  risk of progression to invasive neoplasia"), semantically equivalent to
  gold's refined definition.
- **Scope discipline.** Single `[Term]` stanza, one file, +8/-0; no spurious
  synonym; correct `IAO:0000233` issue link with `xsd:anyURI`.
- **Determinism.** Identical to PR #738 — good reproducibility for a simple
  new-term task.

## Issues

- **Wrong `creator` value (real error).**
  `property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3`
  uses a journal-article DOI where a curator/agent ORCID is required (gold:
  `https://orcid.org/0000-0002-7638-4659`). Misattribution; metadiff-ignored
  so F1-neutral, but a genuine curatorial defect rather than a sandbox
  artifact.
- **Def xref incomplete.** Only `PMID:37775701, PMID:40684183`; the issue
  supplied four PMIDs and gold also leads with the requester ORCID
  `https://orcid.org/0000-0002-2336-2552`. Minor completeness gap.
- **No `is_a` provenance.** Gold annotates `is_a` with `{source=...}`; omitted
  here. Minor.
- Placeholder ID (`MONDO:7770012` vs gold `MONDO:1060215`) plus the
  metadiff-ignored creator field set the F1 ceiling at 0.571 — normal
  under-representation for `case_quality: ok`, not itself a mistake.
