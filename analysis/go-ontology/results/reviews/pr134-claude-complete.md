---
ontology: go-ontology
issue_number: 31962
pr_number: 31970
eval_repo_pr: 134
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/134
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

This gpt-5.5/opencode run produced a diff byte-identical to the gpt-5.5/codex run #126 (output blob `5cf0615`), so the substance and assessment are the same: all four issue requirements correctly met, plus two defensible extra edits. F1 = 0.818 under-represents quality — precision is 0.900 and the recall loss is from in-scope-adjacent extra work, not errors. Successful curation with mild scope creep; the cross-runtime reproducibility (#126/#134/#154) shows this is stable model behavior.

## Strengths

- **GO:0036441**: `xref: EC:1.1.1.358 {source="skos:exactMatch"}` — correct.
- **GO:0070675**: `EC:1.17.3.2 {source="skos:broadMatch"}` + `RHEA:68012 {source="skos:exactMatch"}` added; def xref replaced with `[RHEA:68012]`, matching the gold.
- **GO:0004855**: `EC:1.17.3.2` relaxed `skos:exactMatch` → `skos:broadMatch`, as requested.
- **GO:0030343**: renamed to "vitamin D 25-hydroxylase activity", old label retained as EXACT synonym, `EC:1.14.14.24 {source="skos:exactMatch"}` added.
- `term_tracker_item` for #31962 added to all four terms.

## Issues

- **Scope creep — extra def-xref change on GO:0004855:** changed the GO:0004855 def xref from `[EC:1.17.3.2]` to `[RHEA:21132]`, which was not requested and is absent from the gold. Defensible (RHEA:21132 is the exact reaction source and the EC is now broadened), but out of scope versus the issue checklist.
- **Minor style — synonym xref bracket:** on GO:0030343 the retained label is `synonym: "vitamin D3 25-hydroxylase activity" EXACT [EC:1.14.14.24]` rather than the gold's empty `[]`. Defensible but non-standard for a label-preservation synonym.
- These extra edits drive the recall penalty; nothing is biologically or syntactically wrong.
