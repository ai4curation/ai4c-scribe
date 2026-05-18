---
ontology: mondo
issue_number: 9940
pr_number: 10213
eval_repo_pr: 729
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
case_quality: ok
scoring_caveat: "Gold PR #10213 is the complete, sole human resolution (no companion PRs, curator-approved). However the agent config CLAUDE.md ClinGen section documents the synonym xref as empty brackets `EXACT [] {OMO:0002001=.../clingen}` (contradicting the same file's general 'never use empty brackets' rule), while the human used the GCEP affiliation URL `EXACT [https://clinicalgenome.org/affiliation/40157/]`. Agents that followed their instructions are systematically penalized on the synonym line; per-line F1 on the synonym is config-vs-gold mismatch noise. Judge attempts on substance: no attempt performed the issue-requested definition rewrite or added the human's intersection_of genus-differentia axiom."
f1: 0.5
precision: 0.333
recall: 1.0
jaccard: 0.333
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added the ClinGen preferred-label synonym to MONDO:0044205 and appended an `IAO:0000233` term-tracker for issue #9940, leaving the existing #4948 tracker intact. Both edits are byte-identical to the corresponding human gold lines, giving recall=1.0 over the lines it produced (F1=0.5). It did not rewrite the definition (an explicit issue ask) and did not add the genus-differentia `intersection_of` axiom the human added, so F1=0.5 slightly *over*-represents quality relative to the issue's full ask while still placing this among the best attempts.

## Strengths

- Synonym line matches the human gold exactly: `synonym: "EFL1-related Shwachman-Diamond syndrome" EXACT [https://clinicalgenome.org/affiliation/40157/] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`. Notably, the agent independently chose the CAYA GCEP affiliation URL the human used instead of the empty-bracket `[]` form documented in the agent config CLAUDE.md ClinGen section — it followed MONDO practice over the contradictory config example.
- Correctly targeted the canonical `MONDO:0044205` (no placeholder artifact) and correctly *appended* `property_value: IAO:0000233 ".../issues/9940" xsd:anyURI` while preserving the pre-existing `#4948` tracker — provenance-correct, unlike the destructive overwrite seen in pr429.
- Tightly scoped: every changed line is also a line the human changed; precision is depressed only by omitted lines, not spurious edits. No over-editing, no syntax errors. The PR comment documents `make NORM` + `robot convert` validation.

## Issues

- Omission (explicit requirement): the issue requested a new definition ("An autosomal recessive syndrome characterized by exocrine pancreatic dysfunction, hematopoietic abnormalities, short stature, and metaphyseal dysplasia and caused by pathogenic variants in the EFL1 gene"). The human rewrote the def to "Any Shwachman-Diamond syndrome in which the cause of the disease is a variation on the EFL1 gene..." with source `[https://clinicalgenome.org/affiliation/40157/, OMIM:617941]`. The agent left the old OMIM-only definition untouched.
- Omission (logical axiom): the human added `intersection_of: MONDO:0009833` + `intersection_of: has_material_basis_in_germline_mutation_in HGNC:25789`, promoting MONDO:0044205 to a defined class under the disease-by-gene pattern. The agent kept only the pre-existing `is_a`/`relationship` assertion.
- Metadiff caveat: F1=0.5 does not under-count here; if anything it slightly over-credits, since the 2 missed semantic changes (definition rewrite, equivalence axiom) are the higher-value ones.
