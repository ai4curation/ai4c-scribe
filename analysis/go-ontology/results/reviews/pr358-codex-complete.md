---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 358
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes:
- under_editing
- missed_requirement
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32018
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32021
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/358
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32018 --repo geneontology/go-ontology
    gh pr diff 32021 --repo geneontology/go-ontology
    gh pr diff 358 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The F1=0.0 is misleading because the agent did substantial issue-level work that belongs to the broader human resolution, not just selected PR #32021. It obsoleted GO:0052704 and GO:0140479, added the MetaCyc narrowMatch xrefs to GO:0052699, rewired active `part_of` links, and fixed GO:0052707's replacement. The attempt is incomplete and a little lossy because it missed the taxon-constraint TSV cleanup and removed existing tracker metadata from GO:0052704.

## Strengths

- Correctly identified the two child pathway variants as obsolete and replaced them with GO:0052699.
- Added `MetaCyc:PWY-7255` and `MetaCyc:PWY-7550` to the retained parent term as narrow matches.
- Rewired the two affected MF terms away from obsolete process terms.
- Updated GO:0052707's `replaced_by` value so it points to active GO:0052699.

## Issues

- Missed requirement: it did not delete the GO:0052704 and GO:0140479 rows from `src/taxon_constraints/only_in_taxon.tsv`, the accepted #32021 change.
- Metadata regression: while obsoleting GO:0052704, it removed the pre-existing `property_value` tracker for issue #11163 instead of preserving it alongside the new #32018 tracker.
- It did not add a #32018 tracker to GO:0052699 and did not update the stale GO:0052711 comment, so its cleanup is less complete than stronger attempts.
- It removed GO:0052704's broad synonym and Wikipedia xref, which may be defensible for obsoletion but is not required by the issue.
