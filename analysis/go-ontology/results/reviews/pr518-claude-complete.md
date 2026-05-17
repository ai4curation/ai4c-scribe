---
ontology: go-ontology
issue_number: 31962
pr_number: 31970
eval_repo_pr: 518
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: medium
f1: 0.842
precision: 0.8
recall: 0.889
jaccard: 0.727
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31962
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31970
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/518
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

This is a re-run of the gemma-4-31b/opencode configuration and produced a byte-identical diff to attempt #535 (same output blob `226dc10`), so the assessment is identical. The core enzyme-mapping semantics are correct, but the agent under-edited: it omitted the SKOS qualifier on the new EC:1.14.14.24 xref, did not preserve the old GO:0030343 label as a synonym, and added no `term_tracker_item` metadata. F1 = 0.842 fairly reflects a competent-but-incomplete result; the reproducibility across #535/#518 indicates this is a stable behavior of the model, not run noise.

## Strengths

- **GO:0036441**: `xref: EC:1.1.1.358 {source="skos:exactMatch"}` added with the correct exact predicate.
- **GO:0070675**: added `EC:1.17.3.2 {source="skos:broadMatch"}` and `RHEA:68012 {source="skos:exactMatch"}`, and correctly *replaced* the def xref `[GOC:mah, GOC:pde]` with `[RHEA:68012]`, matching the gold.
- **GO:0004855**: `EC:1.17.3.2` correctly relaxed from `skos:exactMatch` to `skos:broadMatch`.
- **GO:0030343**: correctly renamed to "vitamin D 25-hydroxylase activity".

## Issues

- **Missing SKOS qualifier (GO:0030343):** `xref: EC:1.14.14.24` was added with no `{source="skos:exactMatch"}` annotation, breaking the GO EC/RHEA mapping convention and the xref→skos conversion path (cf. PR #30973).
- **Omitted synonym (GO:0030343):** the prior label `"vitamin D3 25-hydroxylase activity" EXACT []` was not retained as a synonym, unlike the gold PR.
- **No traceability metadata:** no `term_tracker_item` for #31962 on any of the four terms.
- All deviations are under-editing/omission rather than incorrect edits; the model reproduces exactly the same gaps as #535.
