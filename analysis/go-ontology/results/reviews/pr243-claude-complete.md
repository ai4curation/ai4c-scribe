---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 243
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
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

Running gemma-4-31b under opencode, the agent obsoleted GO:0005870 "actin capping protein of dynactin complex" with `replaced_by: GO:0008290`, producing a diff functionally identical to human gold PR #31960 except for the obsoletion `comment:` prose. F1=0.900 under-represents quality; this is a correct obsoletion. Notably, the smallest model in the cohort produced an output indistinguishable in substance from the frontier models.

## Strengths

- Diff matches gold semantically: name prefixed "obsolete", definition prefixed "OBSOLETE." (original `[GOC:jl, PMID:18221362, PMID:18544499]` xrefs preserved), both `intersection_of` axioms removed, `is_obsolete: true`, `replaced_by: GO:0008290`, and `term_tracker_item` for #31956 added.
- Correct replacement target (GO:0008290, the genus from the original logical definition) and tight scope — only the GO:0005870 stanza changed.
- Did perform the key reference check (grep for other terms referencing GO:0005870, found none) and ran a syntax validation (`make go-edit.obo-check`).

## Issues

- Thinnest methodology of the cohort: the PR comment is terse and the `comment:` text ("this term is a direct replacement by GO:0008290") is grammatically awkward and conflates the term with its replacement — it states the obsoleted term *is* a replacement rather than that it is *being replaced by* GO:0008290. Accurate enough in intent but the weakest obsoletion-comment phrasing among the 10 attempts. This is the line that differs from gold and accounts for the 0.1 F1 gap; it is a style weakness, not a correctness error.
- No explicit annotation-impact verification beyond relying on the issue's stated "0 EXP" (acceptable here, but less thorough than the claude/codex runs which independently checked).
