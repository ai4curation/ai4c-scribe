---
ontology: mondo
issue_number: 9963
pr_number: 10222
eval_repo_pr: 50
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.294
precision: 0.5
recall: 0.208
jaccard: 0.172
outcome: partial_success
failure_modes: [over_editing, scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent created the spectrum term with the correctly-qualified ClinGen synonym and re-parented both requested children, but then heavily over-edited the SCAR33 (`MONDO:0859360`) and `MONDO:0033717` stanzas — rewriting definitions, adding synonyms and logical definitions, and inserting a `MONDO:Redundant` source tag — well beyond what the issue or gold required. F1=0.294 is the lowest of the eleven; it is partly the placeholder-vs-canonical ID artifact, but here scope creep is the dominant driver and a real precision/risk problem.

## Strengths

- Correct ClinGen label; definition cites affiliation 40060 and the relevant PMIDs.
- Reproduced the gold ClinGen synonym with the `OMO:0002001="https://w3id.org/information-resource-registry/clingen"` qualifier (one of the few attempts to do so), here as `"RNU12 - related minor spliceopathy disorder"`.
- Both requested children re-parented additively; RNU12 gene axiom added to the new term and to SCAR33.
- Strong, well-documented methodology in the PR comment: consulted the analogous `RNU4ATAC spectrum disorder` precedent, verified HGNC, checked multiple PMIDs, ran `make NORM` + `robot convert`.

## Issues

- Significant scope creep on `MONDO:0859360` SCAR33: added a new `def:`, two synonyms (`"RNU12-related autosomal recessive cerebellar ataxia"`, `"SCAR33" EXACT ABBREVIATION`), an `intersection_of` logical definition, **and a `MONDO:Redundant` source tag on the existing `is_a: MONDO:0015244`** axiom. The gold only added a single `is_a` + gene axiom + issue link to SCAR33; rewriting its definition and asserting redundancy on a pre-existing parent is risky and unrequested.
- Unrequested edit to `MONDO:0033717` (congenital cerebellar ataxia due to RNU12 mutation): added `is_a: MONDO:7770747`. Defensible biologically (it is RNU12-related) but not asked for by the issue and not in the gold.
- Removed the original CDAGS `relationship: has_material_basis_in_germline_mutation_in ... {source="OMIM:603116"}` line and re-added it with an extra `PMID:34085356` source — an unnecessary modification of an existing axiom.
- Invalid provenance: `property_value: http://purl.org/dc/terms/creator doi:10.1186/s13326-024-00320-3` — a DOI (to a methods paper) is not a valid `dcterms:creator`; gold uses a curator ORCID.
- Added child disease names as `NARROW` synonyms on the umbrella term; not in gold.
- Parented under both `hereditary disease` and `syndromic disease`; gold kept only `hereditary disease`. No `IAO:0000233` issue link added to the child stanzas.
