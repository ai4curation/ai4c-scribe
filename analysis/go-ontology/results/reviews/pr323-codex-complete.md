---
ontology: go-ontology
issue_number: 31601
pr_number: 32007
eval_repo_pr: 323
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: failure
failure_modes:
- under_editing
- wrong_term
- missed_requirement
- scope_creep
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31601
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32007
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/323
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31601 --repo geneontology/go-ontology
    gh pr diff 32007 --repo geneontology/go-ontology
    gh pr diff 323 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent did not address issue #31601 or the accepted human PR #32007. The required change was a definition revision for `GO:0140597` protein carrier activity, replacing the older "Binding to and carrying..." wording with the parent-aligned "Directly binding..." definition. Instead, the agent only changed the unrelated `GO:0102067` geranylgeranyl diphosphate reductase activity definition from issue #31963, so the metadiff F1 of 0.0 accurately reflects a complete miss for this case.


## Strengths

- The submitted ontology diff is small and syntactically plausible as an OBO definition update.
- The `GO:0102067` definition change itself matches a real accepted change in the GO history, specifically the issue #31963 / PR #32006 geranylgeranyl reductase cleanup.
- No broad restructuring, new IDs, or large unrelated ontology rewrites were introduced.


## Issues

- The agent never edited the target term for this case, `GO:0140597` protein carrier activity. It left the old definition unchanged instead of applying the accepted wording: `Directly binding to a protein and delivering it either to an acceptor molecule or to a specific location.`
- The only changed term, `GO:0102067`, is unrelated to issue #31601 and human PR #32007. That edit belongs to the separate geranylgeranyl reductase issue #31963 / PR #32006.
- The attempt also did not address the issue's surrounding context about `GO:0140309` unfolded protein holdase activity. For the final human PR #32007, no additional `GO:0140309` change was needed because it had already been handled earlier, but the agent still should have recognized the protein-carrier follow-up request.
- This is not a harmless low-recall attempt: it is a wrong-target patch. Merging it as a response to #31601 would leave the requested definition fix undone while importing an unrelated ontology change.
