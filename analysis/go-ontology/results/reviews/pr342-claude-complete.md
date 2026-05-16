---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 342
agent: std_claude_opus47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.9
precision: 0.9
recall: 0.9
jaccard: 0.818
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent obsoleted GO:0005870 "actin capping protein of dynactin complex" with a direct replacement by GO:0008290, producing a diff functionally identical to human gold PR #31960. This run also matches the original real-world resolution: the source issue's gold PR #31960 was itself authored by dragon-ai-agent running claude-opus-4-7, so this attempt replicates the production solution. F1=0.900 under-represents quality — the only deviation is the obsoletion `comment:` prose.

## Strengths

- Fully correct obsoletion: name → "obsolete actin capping protein of dynactin complex", definition prefixed "OBSOLETE." with original `[GOC:jl, PMID:18221362, PMID:18544499]` provenance retained, both `intersection_of` axioms stripped, `is_obsolete: true`, `replaced_by: GO:0008290`, and `term_tracker_item` for #31956 added.
- Best rationale of the cohort: explicitly explains GO:0005870 is "the dynactin-localized pool of the F-actin capping protein complex (GO:0008290)" and that GO does not maintain separate CC terms for the same complex distinguished only by location — this is exactly the correct curatorial reasoning, and it cites the alternative modeling routes (annotation extensions, or separate annotation to GO:0005869 dynactin complex).
- Rigorous validation: ran `robot convert`, `robot reason -r ELK` (no unsat classes), and reports all 16 SPARQL QC checks passing including the relevant `replaced-by-obsolete-violation` and `obsolete-definition-violation` checks. Correctly noted that `go-idranges.txt` references the ID only for range tracking and needs no change, and correctly declined to add `created_by`/`creation_date` (edit, not new term).
- Proper obo-checkout.pl / obo-checkin.pl workflow; single-file commit; scope-disciplined.

## Issues

- None. The `comment:` wording differs from gold's but is accurate and well-justified; it is the sole reason F1 is 0.900 rather than 1.0 and reflects a normalization artifact, not a quality deficit.
