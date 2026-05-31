---
ontology: mondo
issue_number: 9940
pr_number: 10213
eval_repo_pr: 672
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

The agent produced a diff byte-identical to pr729/pr554 (blob `5ab3104`): it added the ClinGen preferred-label synonym to MONDO:0044205 and appended an `IAO:0000233` term-tracker for issue #9940 while retaining the existing #4948 tracker. Both lines match the human gold exactly, giving recall=1.0 and F1=0.5. It did not rewrite the definition (an explicit issue request) and did not add the human's genus-differentia `intersection_of` axiom; the metadiff slightly *over*-represents quality relative to the issue's full ask.

## Strengths

- Synonym line is byte-identical to the human gold, including the `[https://clinicalgenome.org/affiliation/40157/]` GCEP affiliation xref and the `{OMO:0002001="https://w3id.org/information-resource-registry/clingen"}` qualifier. The agent chose the affiliation-URL form rather than the empty-bracket `[]` example documented in the config CLAUDE.md ClinGen section — correctly aligning with MONDO practice.
- Correctly used the canonical `MONDO:0044205` (no placeholder) and *appended* the `#9940` IAO:0000233 tracker while preserving the pre-existing `#4948` line — provenance-correct.
- Tightly scoped: no spurious edits, no syntax errors. Precision is depressed only by omitted human lines.

## Issues

- Omission (explicit requirement): the issue requested a new EFL1-specific definition; the human rewrote the `def` and its source. The agent left the original OMIM-only definition (`def: "Shwachman-Diamond syndrome-2 (SDS2) is characterized by..." [OMIM:617941]`) unchanged.
- Omission (logical axiom): the human added `intersection_of: MONDO:0009833` + `intersection_of: has_material_basis_in_germline_mutation_in HGNC:25789` to make the term a defined class. The agent did not promote the term.
- Metadiff caveat: F1=0.5 over-credits slightly here — the 2 missed changes (definition rewrite, equivalence axiom) are the higher-value ones. Note this attempt provides no PR/issue comment (diff-only record), so methodology beyond the diff cannot be assessed.
