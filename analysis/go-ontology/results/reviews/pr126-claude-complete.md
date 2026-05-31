---
ontology: go-ontology
issue_number: 31962
pr_number: 31970
eval_repo_pr: 126
agent: std_codex_g55
model: gpt-5.5
runtime: codex
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
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/126
  Agent config: ai4curation/go-ontology-agent-config
-->

## Summary

The gpt-5.5/codex attempt correctly satisfied all four issue requirements and additionally made two defensible extra edits (output blob `5cf0615`, shared with the opencode runs #134/#154). The F1 = 0.818 *under-represents* the quality: precision is 0.900 and the recall penalty comes almost entirely from extra edits that are arguably improvements, not from anything wrong. This is a substantively successful curation with mild scope creep.

## Strengths

- **GO:0036441**: `xref: EC:1.1.1.358 {source="skos:exactMatch"}` — correct.
- **GO:0070675**: `EC:1.17.3.2 {source="skos:broadMatch"}` + `RHEA:68012 {source="skos:exactMatch"}` added; def xref cleanly replaced with `[RHEA:68012]`, matching the gold's handling of "use as def xref".
- **GO:0004855**: `EC:1.17.3.2` relaxed from `skos:exactMatch` to `skos:broadMatch`, as requested.
- **GO:0030343**: renamed to "vitamin D 25-hydroxylase activity", old label retained as an EXACT synonym, `EC:1.14.14.24 {source="skos:exactMatch"}` added.
- `term_tracker_item` for #31962 added to all four terms.
- Strong, transparent methodology: documented EC/RHEA verification in `RESEARCH.md` and precedent in `DESIGN_PATTERNS.md`, applied `/mapping` and `/reaction` skills, and ran `make travis_build` before and after (passed both).

## Issues

- **Scope creep — extra def-xref change on GO:0004855:** the agent also changed the GO:0004855 definition xref from `[EC:1.17.3.2]` to `[RHEA:21132]`. This was *not* requested by the issue and is not in the gold PR. It is a defensible improvement (RHEA:21132 is already the exactMatch for the xanthine→urate reaction and is a better reaction-provenance source than the now-broadened EC), and it parallels the explicitly-requested change on GO:0070675 — but it is out-of-scope relative to the issue's checklist and the human's deliberately tighter edit.
- **Minor style — synonym xref bracket:** on GO:0030343 the retained old label was written `synonym: "vitamin D3 25-hydroxylase activity" EXACT [EC:1.14.14.24]` rather than the gold's empty `[]`. Attaching the EC ID as the synonym's provenance is defensible but differs from the human's form and from GO's usual convention of leaving the empty bracket for a label-preservation synonym.
- These account for the recall drop (agent did more than the human). Nothing the agent did is biologically or syntactically wrong.
