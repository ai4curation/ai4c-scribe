---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 464
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.879
precision: 0.895
recall: 0.864
jaccard: 0.785
outcome: partial_success
failure_modes:
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/464
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The agent correctly obsoleted all five terms with the right replacement targets and stripped logical axioms appropriately, so the obsoletion core of issue #31916 is solid. However, it encoded the new MetaCyc mappings on `GO:0061678` with the wrong xref qualifier syntax (`{skos:narrowMatch="MetaCyc:..."}` instead of the project-standard `{source="skos:narrowMatch"}`), which is a genuine pattern error not just a stylistic difference. `F1=0.879` is a fair reflection: the change is mostly right but the parent-term mapping is malformed relative to GO convention.

## Strengths

- Obsoleted all four ED variant terms (`GO:0009255`, `GO:0061679`, `GO:0061680`, `GO:0061681`) with `replaced_by: GO:0061678`, and `GO:0061688` with `replaced_by: GO:0006096` — correct targets matching the human PR and the issue directive.
- Conventional obsoletion per term: `obsolete ` name prefix, `OBSOLETE.` def prefix, `is_obsolete: true`, removal of `is_a`/`intersection_of`/`relationship`/`xref`/`synonym` axioms, and a `term_tracker_item` for #31916.
- Preserved historical provenance correctly: `created_by`/`creation_date` retained on all obsoleted terms (better than the kimi/opencode and haiku attempts on this case).
- Removed the grouping-class xref `MetaCyc:Entner-Doudoroff-Pathways` from `GO:0061678` and added the four requested variant pathway IDs, satisfying the issue body's mapping request at the content level.
- Reasonable methodology: explicit annotation-impact analysis (4 EXP on `GO:0009255`, 10 IEA on `GO:0061688`), `/term-obsoletion` skill used, and the CGD/PomBase mismatch flagged — though the agent noted full `make travis_build` could not run due to a missing `amm` dependency in the eval environment.

## Issues

- **Wrong mapping pattern (failure_mode: wrong_pattern):** the four new xrefs on `GO:0061678` are written as `xref: MetaCyc:PWY-8004 {skos:narrowMatch="MetaCyc:PWY-8004"}` etc. The established GO convention — used by the human PR and by ~4600 existing xrefs in `go-edit.obo` — is `xref: MetaCyc:PWY-8004 {source="skos:narrowMatch"}`. The `{skos:narrowMatch="..."}` form appears zero times in the ontology. This produces a non-standard trailing qualifier with a redundant self-referential value and would not encode the intended SKOS mapping semantics correctly. This is the dominant cause of the precision/recall gap.
- Omission (minor): the pre-existing `property_value: term_tracker_item ".../issues/28392"` on `GO:0061680` was dropped; the human PR retained it.
- Style-only: per-term obsoletion comments are slightly less specific than the human PR's (they reference GO-CAMs but not the MetaCyc "variant pathways" framing for every term). Not a defect.
