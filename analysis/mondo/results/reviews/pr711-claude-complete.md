---
ontology: mondo
issue_number: 9963
pr_number: 10222
eval_repo_pr: 711
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.667
precision: 0.7
recall: 0.636
jaccard: 0.5
case_quality: poor
case_quality_reason: placeholder_id_artifact
companion_prs: []
scoring_caveat: "Gold #10222 is the complete, clean single-PR human resolution; but the new term's canonical ID MONDO:1060223 is minted only at merge, so the agent's placeholder (MONDO:7770747) makes the gold id: line and the two is_a placement lines structurally unmatchable for every attempt. metadiff F1 systematically UNDER-represents quality; judge on substance vs the issue + gold facts."
outcome: success
failure_modes: [over_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This is a re-run of the same gpt-5.4/opencode configuration as eval PR #765 and produces a **byte-identical diff** (same blob `84b2154`, F1=0.667 — the top score of the thirteen attempts). The agent correctly created the ClinGen spectrum term `RNU12-related minor spliceopathy disorder`, re-parented both requested children (`MONDO:0011287` CDAGS, `MONDO:0859360` SCAR33) additively, added the RNU12 (`http://identifiers.org/hgnc/19380`) gene axiom, and included `IAO:0000233` issue provenance. F1=0.667 **under-represents** quality for the structural placeholder-ID reason (canonical `MONDO:1060223` minted only at merge; agent used `MONDO:7770747`, so the `id:` and two `is_a` placement lines are unmatchable). Substantively one of the strongest attempts; the chief gap is the missing ClinGen `OMO:0002001` synonym.

## Strengths

- Correct term label matching the ClinGen-requested string; faithful definition capturing the CDAGS + SCAR33 spectrum with affiliation 40060 provenance.
- Recognized the peer-reviewed update of the issue's `PMID:39802771` and cited `PMID:40975062` — a defensible methodological improvement (lowers metadiff recall vs the gold's preprint PMID, but is good practice).
- Both requested children (`MONDO:0011287`, `MONDO:0859360`) re-parented via additive `is_a`, preserving existing parents — correct Mondo practice, matching gold substance.
- Correct RNU12 gene axiom `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19380` on the new term; HGNC ID verified against existing Mondo content.
- `property_value: IAO:0000233 ".../issues/9963"` issue provenance on the new term, matching gold.

## Issues

- Omission: no ClinGen EXACT synonym with the `OMO:0002001="https://w3id.org/information-resource-registry/clingen"` source qualifier (present in gold and in the stronger gpt-5.5 attempts #86/#67/#50) — the most material substantive gap.
- Over-editing (low risk): added a free-text `comment:` paragraph restating the spectrum, not present in the issue or gold.
- Scope divergence: parented under both `hereditary disease` (MONDO:0003847) and `syndromic disease` (MONDO:0002254); gold kept only `hereditary disease`. Defensible per the issue text but divergent from merged curation, lowering recall.
- Invalid provenance: `property_value: http://purl.org/dc/terms/creator https://ai4curation.github.io/aidocs/reference/clients/claude-code/` — a tool doc URL is not a valid `dcterms:creator`; gold uses a curator ORCID.
- Omissions vs gold on child stanzas: no `has_material_basis_in_germline_mutation_in HGNC:19380` added to SCAR33 (`MONDO:0859360`) where gold added it; no `IAO:0000233` issue link on the two child stanzas.
- No new poor-case signal beyond the established `placeholder_id_artifact` flag: this re-run is deterministic and identical to #765, confirming reproducibility rather than revealing a new data-quality problem.
