---
ontology: cell-ontology
issue_number: 3559
pr_number: 3564
eval_repo_pr: 552
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
issue-tracker annotation on each of the three terms. Correct terms, correct
abbreviations, correct exact scope. Two gaps relative to gold: it omits the
`oboInOwl:hasSynonymType obo:OMO_0003000` abbreviation synonym type that gold
(and pr590/pr529/pr291) carries, and it uses the issue URL rather than the
literature PMIDs gold cites (PMID:40794848 WBC, PMID:35835183 RPE,
PMID:27696124 PBMC). It also adds three extra IAO_0000233 tracker annotations
not in gold. Metadiff F1=0.0 under-represents substance, which is ~70% correct.

## Strengths

- Correctly identified all three target CL terms and used
  `oboInOwl:hasExactSynonym` scope on all three, matching gold and the curator
  consensus (addiehl: PBMC/WBC exact; scheuerm: RPE appropriate for
  CL:0002586). RPE correctly given exact scope, unlike codex attempt #291.
- Each synonym placed in the correct term annotation block.
- Good methodology documentation: PR comment records checking existing
  stanzas for duplicates, running `robot convert`, and `git diff --check`.

## Issues

- Omission (axiom shape): missing `oboInOwl:hasSynonymType obo:OMO_0003000`
  on all three synonyms. Gold uses it, the cl-agent-config CLAUDE.md
  demonstrates exactly this abbreviation pattern, and the sibling gpt-5.4
  attempts (#590/#529) did include it — so this attempt is a step behind on
  the key abbreviation-typing detail.
- Omission (provenance): xref is the issue URL, not the literature PMID gold
  attached to each synonym. The issue explicitly asked for "reference(s)";
  the issue URL is weaker provenance than a citation.
- Scope creep (minor): adds three `obo:IAO_0000233` issue-tracker annotations
  (one per touched term) that gold does not. These are a defensible
  provenance gesture and a metadiff-ignored field, but they were not asked
  for and slightly widen the diff beyond the synonym request.
- Trailing-newline artifact at line 35600 (serialization side effect),
  harmless.
- F1/precision/recall of 0.0 reflects the all-or-nothing line match against
  gold lines carrying PMID + OMO_0003000 annotations, not absence of useful
  work. Treat as partial_success, not failure.
