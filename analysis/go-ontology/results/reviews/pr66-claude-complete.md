---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 66
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v9
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

gpt-5.5 / codex produced a correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups, with a thorough validation and reference-checking story. F1=0.800 understates quality slightly. Blob `29a680f`, identical to attempt #54 (same model/runtime, re-run).

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- Obsoletion comment is well-formed and accurate: "more specific than the specificity of any known gene product. It has been replaced by GO:0102039 NADH-dependent peroxiredoxin activity."
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment removed — justified hygiene.
- Strong methodology: pre/post `make travis_build` passing, `git diff --check` whitespace check, `linkml-reference-validator` run on PMID:12517450, RESEARCH.md/DESIGN_PATTERNS.md produced. Honest disclosure of the OAK/LinkML `Format.JSON` AttributeError blocking the amigo association lookup, with a documented fallback to the issue-supplied annotation summary — good failure transparency.
- Disciplined checklist with reasoned N/A entries (chemical-entity, taxon-constraint, mapping).

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in human PR → recall 0.727. Defensible curation.
- Comment omits the explicit EC 1.11.1.26 / Expasy linkage that the human comment carries (it is in the PR body instead). Stylistic.
- Duplicate blob with attempt #54.
