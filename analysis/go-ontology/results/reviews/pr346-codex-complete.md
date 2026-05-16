---
ontology: go-ontology
issue_number: 31935
pr_number: 31946
eval_repo_pr: 346
agent: std_claude_op47
model: claude-opus-4.7
runtime: claude
agent_config_tag: v9
case_type: reclassification
difficulty: medium
f1: 0.87
precision: 1.0
recall: 0.769
jaccard: 0.769
outcome: success
failure_modes: []
reviewed_by: gpt-5.5
reviewed_at: 2026-05-16
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31935
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31946
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/346
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31935 --repo geneontology/go-ontology
    gh pr diff 31946 --repo geneontology/go-ontology
    gh pr diff 346 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully made the requested reclassification and associated label, definition, synonym, and tracker updates. It replaced the transporter-complex parent with `GO:0062137 ! cargo receptor complex`, which is the core ontological requirement. The lower recall score mainly reflects final-diff details around synonym ordering and retention, not a failure of the biological model.

## Strengths

- Correctly replaced the old transporter-complex parent rather than adding a second parent.
- Correctly renamed the term and made the minimal genus edit in the definition.
- Correctly added the new cargo receptor EXACT synonym and the issue #31935 tracker.
- Correctly kept the existing transport participation relationship without adding unnecessary logical axioms.
- The PR explanation gives a sound rationale for using the cargo receptor complex parent.

## Issues

- No substantive issues. The agent retained `retrograde transporter complex, Golgi to endoplasmic reticulum` as a BROAD synonym, which differs from the final human PR after review feedback but is a reasonable single-pass result.
