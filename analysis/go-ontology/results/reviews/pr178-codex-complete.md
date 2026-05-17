---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 178
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.952
precision: 0.952
recall: 0.952
jaccard: 0.909
outcome: partial_success
failure_modes:
  - over_editing
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31882
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32036
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/178
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31882 --repo geneontology/go-ontology
    gh pr diff 32036 --repo geneontology/go-ontology
    gh pr diff 178 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the central obsoletion request from issue #31882: it obsoleted `GO:0097711` ciliary basal body-plasma membrane docking and `GO:1905353` ciliary transition fiber assembly, and set both to `replaced_by: GO:1905349` ciliary transition zone assembly. The metadiff F1 of 0.952 is close to the human PR because most edits match, but it slightly overstates quality: the agent did not just remove the obsolete `starts_with GO:0097711` relation from `GO:0060271`, it replaced it with a new `starts_with GO:1905349` assertion that the accepted PR did not make.


## Strengths

- Correctly identified both terms named in the final issue decision: `GO:0097711` and `GO:1905353`.
- Applied the standard obsoletion structure to both terms: `obsolete` name prefix, `OBSOLETE.` definition prefix, removal of active logical axioms and synonyms, `is_obsolete: true`, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31882" xsd:anyURI`, and `replaced_by: GO:1905349`.
- Preserved the original definition text and dbxrefs for both obsolete terms, including the PMID and GOC references on `GO:0097711` and the TermGenie/GO_REF/PMID references on `GO:1905353`.
- Removed the direct live reference to the newly obsolete `GO:0097711` from `GO:0060271` cilium assembly, so the ontology no longer has `starts_with` pointing at an obsolete term.


## Issues

- The agent over-edited `GO:0060271` by changing `relationship: starts_with GO:0097711 ! ciliary basal body-plasma membrane docking` to `relationship: starts_with GO:1905349 ! ciliary transition zone assembly`. The human PR removed the `starts_with` assertion entirely. Since `GO:0060271` already has `relationship: has_part GO:1905349`, adding a new temporal `starts_with` assertion to the replacement term is not justified by the issue and may be ontologically stronger than curator intent.
- The obsoletion comments are less specific than the accepted solution. For `GO:0097711`, the human PR cites the issue rationale from `PMID:27646273` that transition zone assembly begins with docking of the mother centriole to cytoplasmic vesicles; the agent only says the term is redundant with ciliary transition zone assembly. For `GO:1905353`, the human PR notes that the term had no annotations and is part of transition zone assembly; the agent again uses only a generic redundancy comment.
