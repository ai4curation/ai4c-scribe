---
ontology: mondo
issue_number: 9940
pr_number: 10213
eval_repo_pr: 760
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

The agent added the correct ClinGen preferred-label synonym to MONDO:0044205 and appended the `IAO:0000233` term-tracker for issue #9940 (both byte-identical to the human gold), but it also made an out-of-scope destructive edit to the unrelated `SDS2` abbreviation synonym, changing `RELATED ABBREVIATION []` to `RELATED ABBREVIATION [OMIM:617941]`. The spurious edit drives recall down to 0.5 (F1=0.4, blob `d237c92`), below the 0.5 of the tightly-scoped opencode/codex twins. Like all attempts it also omitted the issue-requested definition rewrite and the genus-differentia `intersection_of` axiom.

## Strengths

- Synonym line is byte-identical to the human gold, including the `[https://clinicalgenome.org/affiliation/40157/]` GCEP affiliation xref and the ClinGen `{OMO:0002001=...}` qualifier — the agent correctly chose the affiliation-URL form over the empty-bracket `[]` example in the config CLAUDE.md.
- Correctly used the canonical `MONDO:0044205` (no placeholder) and *appended* the `#9940` IAO:0000233 tracker while preserving the existing `#4948` line — provenance-correct.
- The PR comment honestly discloses the environment limitation (no Docker → could not run containerized `make NORM`/robot validation) rather than fabricating validation.

## Issues

- Scope violation (over-editing): the agent rewrote the pre-existing `synonym: "SDS2" RELATED ABBREVIATION []` to `[OMIM:617941]` and explicitly rationalized this as cleanup ("Replaced the empty synonym provenance on the existing abbreviation SDS2"). The issue never asked for this; the human did not touch the SDS2 synonym. Backfilling a provenance xref on an unrelated synonym is a gratuitous edit a reviewer would strip — and converting a true empty-bracket synonym to an OMIM-sourced one is a substantive provenance assertion, not formatting.
- Omission (explicit requirement): the issue requested a new EFL1-specific definition; the human rewrote `def` and its source. The agent left the original OMIM-only definition unchanged.
- Omission (logical axiom): the human added `intersection_of: MONDO:0009833` + `intersection_of: has_material_basis_in_germline_mutation_in HGNC:25789`. The agent did not promote MONDO:0044205 to a defined class.
- Metadiff: F1=0.4 is a fair representation here — the lower score vs. the 0.5 twins correctly reflects the spurious SDS2 edit penalizing recall, not config-vs-gold noise on the synonym line.
