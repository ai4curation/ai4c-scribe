---
ontology: go-ontology
issue_number: 31948
pr_number: 31994
eval_repo_pr: 270
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: medium
f1: 0.842
precision: 0.8
recall: 0.889
jaccard: 0.727
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31948
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31994
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/270
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31948 --repo geneontology/go-ontology
    gh pr diff 31994 --repo geneontology/go-ontology
    gh pr diff 270 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:7770028` glycoprotein cargo receptor activity and pointed it to `GO:0038024` cargo receptor activity, which is the substance of issue #31948 and human PR #31994. The term is renamed with the `obsolete` prefix, the definition is prefixed with `OBSOLETE.`, the active `is_a` is removed, `is_obsolete: true` is added, and `replaced_by: GO:0038024` is present. Remaining differences are minor metadata/comment differences rather than biological or structural errors.


## Strengths

- Correctly targeted `GO:7770028`, the only term in scope.
- Correctly added `is_obsolete: true` and `replaced_by: GO:0038024`.
- Correctly removed the active parent `is_a: GO:0038024` from the obsolete term.
- Preserved the original definition text under the `OBSOLETE.` prefix and retained the PMID evidence.
- Added the current issue tracker for #31948.
- Kept the change narrowly scoped to `src/ontology/go-edit.obo` and did not introduce unrelated edits.


## Issues

- The obsoletion comment is less detailed than the human PR's explanation. The accepted PR explicitly states that most vesicle cargo are glycoproteins and that cargo receptor activities should be organized by transport domain, with substrates captured via `has_input`.
- Minor metadata differences remain relative to the human PR, such as whether the older tracker for issue #31038 or the original `created_by` line is retained. These are not core ontology errors but differ from the accepted cleanup.
- No wrong replacement, missing obsoletion marker, syntax error, or scope creep was found.
