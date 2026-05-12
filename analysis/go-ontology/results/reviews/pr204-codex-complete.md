---
ontology: go-ontology
issue_number: 31916
pr_number: 32024
eval_repo_pr: 204
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.887
precision: 0.895
recall: 0.879
jaccard: 0.797
outcome: partial_success
failure_modes:
  - missed_requirement
  - wrong_pattern
  - over_editing
reviewed_by: gpt-5.5
reviewed_at: 2026-05-11
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31916
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32024
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/204
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31916 --repo geneontology/go-ontology
    gh pr diff 32024 --repo geneontology/go-ontology
    gh pr diff 204 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent mostly solved issue #31916: it obsoleted the Entner-Doudoroff pathway variant terms, used the expected replacement targets, and also matched the human PR's obsoletion of `GO:0061688`. The `F1=0.887` score is a fair signal of a close but imperfect match: the core obsoletion edits are present, but the parent `GO:0061678` mappings were added as plain MetaCyc xrefs rather than `skos:narrowMatch` xrefs, and several existing metadata lines were dropped.


## Strengths

- Correctly obsoleted `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681`, the Entner-Doudoroff pathway variants identified in the issue, with obsolete names, `OBSOLETE.` definitions, `is_obsolete: true`, issue #31916 tracker items, and `replaced_by: GO:0061678`.
- Correctly removed active logical structure from those obsolete variant terms, including `is_a` parents, `intersection_of` axioms, old direct MetaCyc xrefs, and the obsolete-term synonyms where applicable.
- Correctly removed `MetaCyc:Entner-Doudoroff-Pathways` from the active parent `GO:0061678` and added the four individual MetaCyc variant IDs requested by the issue: `MetaCyc:PWY-8004`, `MetaCyc:NPGLUCAT-PWY`, `MetaCyc:PWY-2221`, and `MetaCyc:ENTNER-DOUDOROFF-PWY`.
- Matched the human PR's additional obsoletion of `GO:0061688 glycolytic process via Entner-Doudoroff Pathway`, including stripping the active glycolysis/start axioms and using `replaced_by: GO:0006096`.


## Issues

- The most important issue is the mapping pattern on `GO:0061678`: the issue explicitly requested the individual MetaCyc IDs as `narrowMatch` xrefs, and the human PR encoded them as `xref: MetaCyc:... {source="skos:narrowMatch"}`. The agent added the same four IDs only as plain `xref` lines, so the intended SKOS mapping semantics are missing.
- The agent over-edited provenance metadata on obsolete terms. It removed `created_by` and `creation_date` from `GO:0061679`, `GO:0061680`, `GO:0061681`, and `GO:0061688`, while the human PR preserved those historical metadata lines.
- The agent also removed the pre-existing `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/28392"` from `GO:0061680`. That was unrelated to issue #31916 and should have been retained.
- The obsolete comments are acceptable but less precise than the human PR's comments. In particular, the human text explicitly ties the obsoletion of `GO:0009255`, `GO:0061679`, `GO:0061680`, and `GO:0061681` to MetaCyc variant pathways and GO-CAM representation, and gives a more specific annotation rationale for `GO:0061688`.
