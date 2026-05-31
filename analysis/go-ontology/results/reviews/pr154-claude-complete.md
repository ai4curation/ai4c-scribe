---
ontology: go-ontology
issue_number: 31962
pr_number: 31970
eval_repo_pr: 154
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: medium
f1: 0.818
precision: 0.9
recall: 0.75
jaccard: 0.692
outcome: success
failure_modes:
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-15'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31962
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31970
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/154
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The gpt-5.5/opencode (pi) run produced a diff byte-identical to runs #126 and #134 (output blob `5cf0615`): all four issue requirements correctly satisfied plus two defensible extra edits. F1 = 0.818 under-represents the result — precision 0.900, with the recall penalty driven by extra (arguably improving) work, not errors. Successful curation with mild scope creep; the identical output across three independent runs confirms stable model behavior.

## Strengths

- **GO:0036441**: `xref: EC:1.1.1.358 {source="skos:exactMatch"}` — correct.
- **GO:0070675**: `EC:1.17.3.2 {source="skos:broadMatch"}` + `RHEA:68012 {source="skos:exactMatch"}`; def xref cleanly replaced with `[RHEA:68012]`, matching the gold.
- **GO:0004855**: `EC:1.17.3.2` relaxed `skos:exactMatch` → `skos:broadMatch`, as requested.
- **GO:0030343**: renamed to "vitamin D 25-hydroxylase activity", old label retained as EXACT synonym, `EC:1.14.14.24 {source="skos:exactMatch"}` added.
- `term_tracker_item` for #31962 added to all four terms.
- Transparent methodology: honestly reported a `runoak` dependency failure in the sandbox and fell back to verifying IDs against the local RHEA RDF and ENZYME/ExPASy; `make travis_build` passed before and after.

## Issues

- **Scope creep — extra def-xref change on GO:0004855:** changed the GO:0004855 def xref from `[EC:1.17.3.2]` to `[RHEA:21132]`, not requested and not in the gold. Defensible (mirrors the requested GO:0070675 treatment and uses the existing exact RHEA reaction) but outside the issue's checklist.
- **Minor style — synonym xref bracket:** GO:0030343 retained label written as `synonym: "vitamin D3 25-hydroxylase activity" EXACT [EC:1.14.14.24]` vs the gold's empty `[]`.
- These extras account for the recall drop; no biological or syntactic errors.
