---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 40
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.8
precision: 0.889
recall: 0.727
jaccard: 0.667
outcome: partial_success
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/40
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 40 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly obsoleted `GO:0008785 alkyl hydroperoxide reductase activity` and added `replaced_by: GO:0102039`, matching the core request in issue #31961. However, it also edited free-text comments on `GO:0009321` and `GO:0070937`; those same comment edits were present in the initial human PR but were explicitly reverted after maintainer feedback, leaving the accepted human solution scoped only to `GO:0008785`. The metadiff F1 of 0.8 is a fair signal: the main ontology change is right, but the extra edits lower precision of the delivered PR.


## Strengths

- Correctly converted `GO:0008785` to an obsolete term by prefixing the name with `obsolete`, prefixing the definition with `OBSOLETE.`, removing the asserted `is_a: GO:0016668`, adding `is_obsolete: true`, and adding `replaced_by: GO:0102039`.
- Added the requested issue tracker link for `GO:0008785` with `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31961" xsd:anyURI`.
- Chose the right replacement term, `GO:0102039 NADH-dependent peroxiredoxin activity`, consistent with the issue's rationale that `GO:0008785` was a substrate-specific version of that EC/RHEA-supported activity.
- Included a biologically relevant obsoletion comment explaining that `GO:0008785` was more specific than known gene product specificity and equivalent in practice to `GO:0102039`.


## Issues

- Over-edited outside the requested obsoletion by changing the `GO:0009321 alkyl hydroperoxide reductase complex` comment to point to `GO:0102039`. This is defensible as cleanup, but the human PR review explicitly requested not changing comments in other terms, and the accepted PR reverted this edit.
- Removed a free-text comment from `GO:0070937 CRD-mediated mRNA stability complex` because it appeared to be a stale copy/paste reference to `GO:0008785`. That may be a real cleanup, but it was outside the issue scope and was also reverted from the accepted human PR.
- The obsoletion comment differs from the accepted human PR's final wording. The agent's longer comment is not syntactically wrong, but the extra EC/synonym rationale is more verbose than the final accepted edit and contributes to the line-level mismatch.
