---
ontology: mondo
issue_number: 9940
pr_number: 10213
eval_repo_pr: 706
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
case_quality: ok
scoring_caveat: "Gold PR #10213 is the complete, sole human resolution (no companion PRs, curator-approved). However the agent config CLAUDE.md ClinGen section documents the synonym xref as empty brackets `EXACT [] {OMO:0002001=.../clingen}` (contradicting the same file's general 'never use empty brackets' rule), while the human used the GCEP affiliation URL `EXACT [https://clinicalgenome.org/affiliation/40157/]`. Agents that followed their instructions are systematically penalized on the synonym line; per-line F1 on the synonym is config-vs-gold mismatch noise. Judge attempts on substance: no attempt performed the issue-requested definition rewrite or added the human's intersection_of genus-differentia axiom."
f1: 0.4
precision: 0.333
recall: 0.5
jaccard: 0.25
outcome: partial_success
failure_modes: [over_editing, under_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent produced a diff byte-identical to pr760 (blob `d237c92`): it added the correct ClinGen preferred-label synonym to MONDO:0044205 and appended the `IAO:0000233` term-tracker for issue #9940, but it also destructively rewrote the unrelated `SDS2` abbreviation synonym from `RELATED ABBREVIATION []` to `RELATED ABBREVIATION [OMIM:617941]`. That out-of-scope edit pushes recall to 0.5 and F1 to 0.4, below the tightly-scoped twins at F1=0.5. It also omitted the issue-requested definition rewrite and the human's genus-differentia `intersection_of` axiom.

## Strengths

- Synonym line is byte-identical to the human gold, with the `[https://clinicalgenome.org/affiliation/40157/]` GCEP affiliation xref and `{OMO:0002001="https://w3id.org/information-resource-registry/clingen"}` qualifier — correctly aligned with MONDO practice over the empty-bracket config example.
- Correctly used the canonical `MONDO:0044205` (no placeholder) and *appended* the `#9940` IAO:0000233 tracker while preserving the existing `#4948` line — provenance-correct.

## Issues

- Scope violation (over-editing): the agent rewrote the pre-existing `synonym: "SDS2" RELATED ABBREVIATION []` to `[OMIM:617941]`. The issue did not request this and the human left the SDS2 synonym untouched; asserting an OMIM provenance on an unrelated synonym is a gratuitous, substantive edit a reviewer would reject. (No PR/issue comment is recorded for this run, so the agent's rationale cannot be inspected; pr760 — the byte-identical twin — explicitly justified it as cleanup.)
- Omission (explicit requirement): the issue requested a new EFL1-specific definition; the human rewrote `def` and its source. The agent left the original OMIM-only definition unchanged.
- Omission (logical axiom): the human added `intersection_of: MONDO:0009833` + `intersection_of: has_material_basis_in_germline_mutation_in HGNC:25789` to make the term a defined class. The agent did not.
- Metadiff: F1=0.4 fairly represents quality — the gap below the 0.5 twins correctly reflects the spurious SDS2 edit, not config-vs-gold synonym noise.
