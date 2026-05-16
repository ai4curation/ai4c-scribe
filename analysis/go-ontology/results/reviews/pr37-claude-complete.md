---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 37
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v8-noskills
case_type: obsoletion
difficulty: simple
f1: 0.800
precision: 0.889
recall: 0.727
jaccard: 0.667
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

gpt-5.4 / codex on the `v8-noskills` config still produced a correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups. F1=0.800 understates quality slightly. Blob `7960fbb`. Notably this matches the skill-enabled configs' output exactly, indicating the obsoletion task is solvable without the specialized skill files.

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- Obsoletion comment is accurate and concise: "obsoleted because it represents a substrate-specific instance of NADH-dependent peroxiredoxin activity" — correctly captures the over-specificity rationale.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 stray comment removed with the explicit point that this "prevents an obsolete-term reference from remaining in the ontology" — exactly the right justification.
- Pre/post `make travis_build` passing, including the obsoletion-specific SPARQL checks (`replacedby-obsolete-violation`, `replacedby-namespace-violation`, `obsolete-reference-violation`).
- Cross-config evidence: the noskills config reaches the same correct answer as the v9 skill-enabled runs — useful negative result for this simple task type.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in human PR → recall 0.727. Defensible curation.
- Comment omits the explicit EC 1.11.1.26 citation present in the human comment. Stylistic.
- No substantive errors.
