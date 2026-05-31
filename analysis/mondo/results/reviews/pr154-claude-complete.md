---
ontology: mondo
issue_number: 10030
pr_number: 10117
eval_repo_pr: 154
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: bulk_edit
difficulty: hard
f1: 0.003
precision: 0.002
recall: 1.0
jaccard: 0.002
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_pr_is_out_of_scope_mega_edit
companion_prs: []
scoring_caveat: "metadiff compares a correct 8-line single-term fix against the 5,103-line ontology-wide bulk sweep selected as gold (#10117); F1=0.003 is meaningless here. Judge against the literal ask of issue #10030."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent removed exactly the 8 erroneous "cellulitis and abscess..." synonyms from MONDO:0001628 "tinea unguium", explicitly stating it changed no parentage, definition, xrefs, or logical axioms. This is a faithful, minimal resolution of the issue's literal ask. Metadiff F1=0.003 *under-represents* quality: gold PR #10117 is a 5,103-line ontology-wide synonym purge (the curator-chosen large-scale approach), so a correctly scoped single-term fix is structurally unscoreable against it. The edit is correct and clean.

## Strengths

- Correct, minimal diff matching the issue exactly: 8 bad synonyms removed, all dermatophytosis/onychomycosis synonyms and logical axioms preserved.
- Clear, accurate rationale tying the bad synonyms to the DO-derived import and confirming they describe unrelated body sites, not fungal nail infection.
- Transparent about an environment limitation: could not run the Docker-backed `sh run.sh make NORM` normalization (no docker in runner), but did run `robot convert` syntax validation. Honest reporting of tooling constraints rather than silently skipping or faking validation.

## Issues

- No correctness or scope errors.
- Did not add the `IAO:0000233` term-tracker annotation (config convention) and did not remove the parallel suspect `xref: ICD9:681.9 {source="DOID:13074"}`. Minor completeness nits, defensible given the narrow scope.
- Could not complete the ODK normalization step due to missing Docker in the runner — an environment limitation, not an agent fault; syntax validation was still performed.
