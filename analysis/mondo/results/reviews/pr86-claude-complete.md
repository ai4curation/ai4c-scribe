---
ontology: mondo
issue_number: 9963
pr_number: 10222
eval_repo_pr: 86
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.583
precision: 0.7
recall: 0.5
jaccard: 0.412
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent correctly created the requested ClinGen spectrum term `RNU12-related minor spliceopathy disorder`, classified both requested children (`MONDO:0011287` CDAGS, `MONDO:0859360` SCAR33) under it, added the RNU12 (`HGNC:19380`) gene axiom, and used the ClinGen preferred-label synonym with the correct `OMO:0002001` ClinGen-source qualifier. F1=0.583 substantially **under-represents** the quality: the new term's `id:` line and both `is_a: <newterm>` placement lines cannot match gold because the canonical ID `MONDO:1060223` is assigned only at merge — every agent used a placeholder (`MONDO:7770747`), so ~4 of 9 gold additions are structurally unreachable. On substance this is the strongest of the eleven attempts and would need only minor curator cleanup.

## Strengths

- Correct term label matching the ClinGen-requested string, and a faithful definition citing `https://clinicalgenome.org/affiliation/40060/` and `PMID:39802771`.
- Reproduced the gold ClinGen synonym pattern almost exactly: `synonym: "RNU12-related minor spliceopathy disorder" EXACT [...clinicalgenome.../40060/...] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}` — the only attempt besides #67 and #50 to get the `OMO:0002001` qualifier right.
- Both requested children re-parented via additive `is_a` to the new term, preserving existing parents (correct per Mondo policy).
- `has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/19380` correctly placed on the new term; HGNC ID verified against existing Mondo content rather than guessed.
- Added `property_value: IAO:0000233 ".../issues/9963"` issue-tracker provenance on the new term, matching gold.
- Ran `robot convert` syntax validation; honestly reported that Docker/ODK NORM was unavailable.

## Issues

- Scope/precision: added `subset: clingen {source="MONDO:CLINGEN"}` and `subset: rare`, plus an `intersection_of` logical definition (`hereditary disease` and the RNU12 axiom). The gold term has **no** `intersection_of` and no subsets — these are extra, not wrong per se, but unrequested.
- Parented under both `hereditary disease` and `syndromic disease`; the gold kept **only** `hereditary disease` (MONDO:0003847) despite the issue requesting both — a defensible reading of the issue, but a divergence from the merged curation.
- Omission: did not add `has_material_basis_in_germline_mutation_in HGNC:19380` to the SCAR33 (`MONDO:0859360`) stanza, which the gold added because SCAR33 lacked the gene relationship; also did not add the `IAO:0000233` issue link to the two child stanzas as gold did.
- Did not add `property_value: http://purl.org/dc/terms/creator` (gold used the curator ORCID); minor provenance omission.
