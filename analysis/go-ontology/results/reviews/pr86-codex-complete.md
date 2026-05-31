---
ontology: go-ontology
issue_number: 31882
pr_number: 32036
eval_repo_pr: 86
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.964
precision: 0.952
recall: 0.976
jaccard: 0.93
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31882
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32036
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/86
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31882 --repo geneontology/go-ontology
    gh pr diff 32036 --repo geneontology/go-ontology
    gh pr diff 86 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent successfully implemented the final decision from geneontology/go-ontology#31882: obsolete `GO:0097711` ciliary basal body-plasma membrane docking and `GO:1905353` ciliary transition fiber assembly, with both terms `replaced_by: GO:1905349` ciliary transition zone assembly. It also removed the live `starts_with GO:0097711` relationship from `GO:0060271` cilium assembly. The metadiff F1 of 0.964 is a fair high score: the core ontology edits match the human PR, with only minor metadata/comment wording differences.

## Strengths

- Correctly handled both terms named in the issue's final decision, not just the original `GO:0097711` term from the issue title.
- Applied the standard obsoletion structure to `GO:0097711` and `GO:1905353`: `obsolete` name prefix, `OBSOLETE.` definition prefix, `is_obsolete: true`, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31882" xsd:anyURI`, and `replaced_by: GO:1905349`.
- Removed active classification and logical structure from the obsolete terms, including `GO:0097711`'s `is_a: GO:0140056` and `part_of GO:0060271`, and `GO:1905353`'s `intersection_of` axioms to `GO:0022607` and `GO:0097539`.
- Removed `relationship: starts_with GO:0097711` from `GO:0060271` cilium assembly, matching the human PR and avoiding a live relationship to an obsolete biological process term.
- Preserved the original definition text and definition xrefs on both obsolete terms while dropping the active synonyms, relationships, and equivalence axioms that should not remain on obsolete terms.


## Issues

- No substantive correctness or completeness problems. The agent made the requested obsoletions and used the correct replacement target, `GO:1905349`.
- Minor metadata/style mismatch: the accepted human PR removed the existing `created_by: pr` and `creation_date` lines from both obsolete stanzas, while the agent left them on `GO:0097711` and `GO:1905353`. This does not change the replacement semantics, but it differs from the accepted obsoletion cleanup.
- Minor comment weakness: the agent's obsoletion comments are less specific than the human PR. For `GO:0097711`, the human comment names `GO:1905349` and cites the `PMID:27646273` rationale that transition zone assembly encompasses the docking step; the agent only says the term is redundant with ciliary transition zone assembly. For `GO:1905353`, the human comment notes that transition fiber assembly is part of transition zone assembly and had no annotations; the agent uses only a generic redundancy comment.
