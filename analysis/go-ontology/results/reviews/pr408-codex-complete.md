---
ontology: go-ontology
issue_number: 32044
pr_number: 32054
eval_repo_pr: 408
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.762
precision: 0.667
recall: 0.889
jaccard: 0.615
outcome: partial_success
failure_modes:
- under_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32044
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32054
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/408
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32044 --repo geneontology/go-ontology
    gh pr diff 32054 --repo geneontology/go-ontology
    gh pr diff 408 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent added the requested new biological process term `GO:7770074` protein O-linked glycosylation via N-acetylglucosamine with the correct parent, definition, PMID, issue tracker, and the two expected exact synonyms. The main miss is that human PR #32054 also harmonized the sibling `GO:0016266` label from `N-acetyl-galactosamine` to `N-acetylgalactosamine`, added the old hyphenated label as an exact synonym, and added the issue tracker there. The metadiff score is therefore moderately below 1.0, but the core new-term request is successfully handled.


## Strengths

- Correctly minted `GO:7770074` with the requested label `protein O-linked glycosylation via N-acetylglucosamine`.
- Used the exact requested definition, including the beta-glycosidic bond, serine/threonine side chain, and the fact that the sugar is not elongated into a larger oligosaccharide chain.
- Added the requested parent `GO:0006493` protein O-linked glycosylation.
- Added the issue tracker for #32044 and the expected PMID `35536957`.
- Added the two main exact synonyms: `protein O-linked GlcNAcylation` and an N-acetylglucosaminylation synonym.
- Did not touch unrelated ontology branches or overwrite existing terms.


## Issues

- Missed the sibling-term cleanup on `GO:0016266`: the human PR changed `N-acetyl-galactosamine` to `N-acetylgalactosamine`, preserved the old label as an exact synonym, and added a tracker for #32044.
- The N-acetylglucosaminylation synonym uses the hyphenated form `protein O-linked-N-acetylglucosaminylation`, while the human PR used `protein O-linked N-acetylglucosaminylation`. This is a small wording/style mismatch rather than a core modeling error.
- `created_by` and `creation_date` differ from the human PR, reflecting the agent run rather than the original curator metadata.
