---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 85
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.965
precision: 0.965
recall: 0.965
jaccard: 0.932
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Independent claude review.
  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/85
-->

## Summary

The agent fully resolved issue #31916, producing a diff substantively identical to the gold PR #32024. It obsoleted the four Entner-Doudoroff variant terms with `replaced_by: GO:0061678`, obsoleted GO:0061688 with `replaced_by: GO:0006096`, and rebuilt the GO:0061678 MetaCyc xrefs as `{source="skos:narrowMatch"}` exactly as the issue specified. F1=0.965 slightly under-represents the quality: the only differences from gold are the wording of obsoletion comments and a single extra tracker line. This run is byte-equivalent in its substantive edits to the gpt-5.5/codex run (#65) and the other opencode run (#106).

## Strengths

- Correct and complete obsoletion of GO:0009255, GO:0061679, GO:0061680, GO:0061681: obsolete name/definition prefixes, `is_obsolete: true`, `replaced_by: GO:0061678`, issue #31916 `term_tracker_item`, and removal of all active axioms (`is_a`, `intersection_of`, term-level MetaCyc xrefs, the GO:0061679 RELATED synonym).
- GO:0061688 obsoleted with `replaced_by: GO:0006096`, correctly picking up the curator-agreed target from the issue thread rather than only the issue body; active glycolytic `is_a`/`intersection_of`/`starts_with` axioms removed.
- GO:0061678 mapping cleanup is exactly right: grouping-class `xref: MetaCyc:Entner-Doudoroff-Pathways` removed; all four variant IDs added with the required `{source="skos:narrowMatch"}` qualifier — the highest-risk detail in this task, done correctly.
- Pre-existing issue #28392 `term_tracker_item` and `created_by`/`creation_date` lines preserved on the obsoleted variants, matching the gold PR and avoiding collateral metadata loss.

## Issues

- Style only: obsoletion comments are generic ("represents a variant of the Entner-Doudoroff pathway that is better represented in GO-CAMs") versus the gold PR's more specific text that names GO:0061678 and MetaCyc's variant-pathway rationale. No semantic difference.
- Minor scope: an extra `property_value: term_tracker_item ".../31916"` was added to the still-active parent GO:0061678, which the human PR did not include. Harmless, and the sole cause of F1 < 1.0.
- No correctness, syntax, or completeness problems.
