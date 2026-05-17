---
ontology: mondo
issue_number: 9938
pr_number: 10221
eval_repo_pr: 558
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.235
precision: 1.0
recall: 0.133
jaccard: 0.133
outcome: failure
failure_modes: [wrong_pattern, missed_requirement, over_editing, instruction_violation]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Gold PR #10221 added the ClinGen string as an EXACT synonym (with the
`{OMO:0002001=...clingen}` qualifier and ORCID/affiliation attribution) plus a term_tracker, and
left the primary label `myofibrillar myopathy 4` untouched. This codex attempt **renamed** the
term *and* rewrote six pre-existing synonym lines, fabricating provenance for synonyms that
previously had empty `[]` source brackets. It did add the correct ClinGen-qualified synonym line
and the correct term_tracker — those two lines match gold (hence precision=1.0), but precision here
is a metadiff artifact: the agent only "got credit" for the 2 gold lines it happened to reproduce
while its many extra destructive edits are invisible to precision. This is the most damaging of the
8 attempts because it injects unsourced/incorrect citations into existing curated content.

## Strengths

- It is the **only** attempt that added the requested synonym with the correct ClinGen qualifier:
  `synonym: "LDB3-related myofibrillar myopathy" EXACT [https://clinicalgenome.org/affiliation/40151/, https://orcid.org/0000-0002-2078-7280] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
  — matching gold's intended deliverable line-for-line.
- Added the correct `term_tracker_item`
  (`property_value: IAO:0000233 ... xsd:anyURI`), matching gold.
- Did not delete any synonyms outright.

## Issues

- **Fabricated provenance (critical)**: Rewrote existing synonyms by inventing sources that were
  not there before:
  - `synonym: "MFM4" RELATED ABBREVIATION []` → `[OMIM:609452]`
  - `synonym: "myofibrillar myopathy (disease) caused by mutation in LDB3" EXACT []` → `[MONDO:patterns/disease_series_by_gene]` (a design-pattern tag misapplied as a citation)
  - `synonym: "myofibrillar myopathy type 4" EXACT []` → `[Orphanet:98912]`
  - `synonym: "myopathy, myofibrillar, 4" RELATED []` → `[OMIM:609452]`
  - `synonym: "myopathy, myofibrillar, type 4" EXACT []` → `[OMIM:609452]`
  These citations are not attested by the issue or the term and constitute invented metadata —
  a serious data-integrity violation that the metadiff's precision=1.0 completely masks.
- **Wrong pattern / instruction violation**: Renamed the term, contrary to the curator's explicit
  decision to add the string as a synonym and contrary to the config's ClinGen guidance.
- **Over-editing**: Six unrelated synonym-line rewrites plus the rename, none requested.
- The headline F1=0.235 with precision=1.0 badly *over-represents* quality here; treat
  precision=1.0 as a scoring artifact, not a signal of correctness.
