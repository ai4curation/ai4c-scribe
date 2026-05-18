---
ontology: cell-ontology
issue_number: 3559
pr_number: 3564
eval_repo_pr: 491
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: synonym_update
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
  - missed_requirement
  - scope_creep
case_quality: ok
case_quality_reason: metadiff_underrepresents_substance
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added all three requested abbreviation synonyms — "WBC" to leukocyte
(CL:0000738), "RPE" to retinal pigment epithelial cell (CL:0002586), and "PBMC"
to peripheral blood mononuclear cell (CL:2000001) — each as a
`hasExactSynonym` with the issue URL as xref, plus an `obo:IAO_0000233`
issue-tracker annotation on each of the three terms. The agent diff is
identical to attempt #552 (both produce blob `01f8370`): correct terms,
correct abbreviations, correct exact scope on all three, but missing the
`oboInOwl:hasSynonymType obo:OMO_0003000` abbreviation synonym type gold
carries, using the issue URL instead of literature PMIDs (PMID:40794848 WBC,
PMID:35835183 RPE, PMID:27696124 PBMC), and adding three extra IAO_0000233
tracker annotations not in gold. Metadiff F1=0.0 under-represents substance,
which is ~70% correct.

## Strengths

- Correctly identified all three target CL terms and applied
  `oboInOwl:hasExactSynonym` scope to each, matching gold and the curator
  consensus in the issue thread (addiehl: PBMC/WBC exact; scheuerm: RPE
  appropriate for CL:0002586). RPE correctly given exact scope, unlike codex
  attempt #291 which used related scope.
- Each synonym placed in the correct term annotation block; the issue-relevant
  edit is confined to `src/ontology/cl-edit.owl`.

## Issues

- Omission (axiom shape): missing `oboInOwl:hasSynonymType obo:OMO_0003000` on
  all three synonyms. Gold uses it, the cl-agent-config CLAUDE.md demonstrates
  this exact abbreviation pattern, and the sibling gpt-5.4 attempts
  (#590/#529) did include it.
- Omission (provenance): xref is the issue URL, not the literature PMID gold
  attached to each synonym. The issue explicitly asked for "reference(s)".
- Scope creep (minor): three `obo:IAO_0000233` issue-tracker annotations (one
  per touched term) not in gold. Defensible provenance, and a
  metadiff-ignored field, but not requested and widens the diff beyond the
  synonym request.
- Trailing-newline artifact at line 35600 (serialization side effect),
  harmless.
- F1/precision/recall of 0.0 reflects the all-or-nothing line match against
  gold lines carrying PMID + OMO_0003000 annotations, not absence of useful
  work. Treat as partial_success, not failure.
