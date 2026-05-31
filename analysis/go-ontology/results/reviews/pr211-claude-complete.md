---
ontology: go-ontology
issue_number: 31945
pr_number: 32013
eval_repo_pr: 211
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.895
precision: 0.85
recall: 0.944
jaccard: 0.81
outcome: success
failure_modes:
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31945
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32013
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/211
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31945 --repo geneontology/go-ontology
    gh pr diff 32013 --repo geneontology/go-ontology
    gh pr diff 211 --repo ai4curation/eval-ont-agent-go
-->

## Summary

A solid haiku-4.5 run that gets the substance right (`f1: 0.895`, `precision: 0.850`, `recall: 0.944`). The obsoletion and both renames are correct with full provenance retained and exact-match restored-synonym dbxrefs. Two minor issues: the obsoletion metadata is ordered unusually (`is_obsolete`/`replaced_by` placed *after* `created_by`/`creation_date` rather than before), and it missed the stale-comment refresh on the incoming `is_a` edges. The score fairly represents a successful solution with one cosmetic omission shared across most of the cohort.

## Strengths

- **Obsoletion content matches gold:** `name: obsolete ...`, `def: "OBSOLETE. ..."` (dbxrefs preserved), both `intersection_of` removed, `comment`, `term_tracker_item`, `is_obsolete: true`, `replaced_by: GO:0048208`. Provenance (`created_by: dph`, `creation_date`) retained per the `term-obsoletion` skill.
- **Both renames correct** with old labels restored as EXACT synonyms; `GO:0048208` restored-synonym dbxrefs `[GOC:ascb_2009, GOC:dph, GOC:tb]` match the gold exactly.
- **Good obsoletion rationale in the PR comment** identifying the annotated proteins (SAR1A, PREB) as structural coat components rather than regulators — biologically accurate and aligned with ValWood's note. (The in-file `comment` itself is terser: "the data can be accurately described using COPII vesicle coat assembly (GO:0048208)" — acceptable.)
- Strong haiku showing for a medium-difficulty reclassification: tight scope, no errors, no scope creep onto active terms, sensible annotation-impact analysis.

## Issues

- **Obsoletion metadata ordering (style/minor).** The diff appends `is_obsolete: true` and `replaced_by: GO:0048208` *after* the `created_by`/`creation_date` block, whereas the gold and the skill exemplar place obsoletion tags before the provenance tags. OBO is order-insensitive for parsing so this is not an error, but it diverges from house style and from the gold's stanza layout (and contributes to the precision gap vs the line-diff).
- **Missed the stale-comment maintenance (omission).** No refresh of `is_a: GO:0006901 ! vesicle coating` → `! vesicle coat assembly` on `GO:0016183`/`GO:0048200`, nor on `GO:0048208`'s own self-edge — all done by the gold. Cosmetic, but it is the recall gap and the single thing separating this from pr344.

Net: a `success`. The metadiff fairly reflects a correct solution with a cosmetic ordering quirk and the cohort-wide comment omission.
