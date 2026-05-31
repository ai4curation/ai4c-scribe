---
ontology: cell-ontology
issue_number: 3332
pr_number: 3333
eval_repo_pr: 42
agent: std_opencode_g55
model: openai/gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: bulk_edit
difficulty: medium
f1: 0.414
precision: 0.300
recall: 0.667
jaccard: 0.261
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_out_of_scope_reserialization_artifact
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

A second gpt-5.5/opencode run, producing a diff byte-identical to attempts #60
and #93 (blob `2d1b484`): all redundant imported-AP `rdfs:label` axioms and
their empty section headers removed, including the `uberon:HUMAN_PREFERRED` /
`LATIN` / `PLURAL` labels (their `SubAnnotationPropertyOf` axioms kept) and
`rdfs:label rdfs:seeAlso`. The F1 of 0.414 (P=0.300, R=0.667)
**under-represents** the quality: ~60% of the gold diff is an unrelated
one-time re-serialization side-effect no agent could reproduce. On substance
this is a success and demonstrates run-to-run determinism for this model.

## Strengths

- Correct, complete removal of the redundant imported IAO/oboInOwl AP labels,
  including the motivating `oboInOwl:hasDbXref` example.
- Preserved the two CL-meaningful `rdfs:seeAlso` axioms and all CL-native
  subset-property labels; kept structural `SubAnnotationPropertyOf` axioms.
- PR narrative documents reading the issue context and validating with
  `robot convert`; signed per config convention ("GitHub Copilot").
- Reproducible: identical output to the sibling opencode run (#60), indicating
  stable behavior rather than lucky sampling.

## Issues

- Same ambiguous edge-case call as #60/#93: the `uberon:*` synonym
  type-property labels were removed. Defensible under a maximalist reading;
  the Opus attempt's URI-based argument for keeping them is also valid. Not a
  clear error.
- Only true gap vs. gold is the gold's incidental class-block re-serialization
  (relocating misplaced `CL_4072027` / `CL_7770002` / `CL_7770005`), an
  explicitly out-of-scope side-effect of fixing a prior AI PR per the gold PR
  author. Not counted against the agent.
