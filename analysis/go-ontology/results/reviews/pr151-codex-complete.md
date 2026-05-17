---
ontology: go-ontology
issue_number: 31956
pr_number: 31960
eval_repo_pr: 151
agent: std_opencode_g55
model: gpt-5.5
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
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31956
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/31960
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/151
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31956 --repo geneontology/go-ontology
    gh pr diff 31960 --repo geneontology/go-ontology
    gh pr diff 151 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent correctly handled the requested obsoletion of `GO:0005870` `actin capping protein of dynactin complex`, with direct replacement by `GO:0008290` `F-actin capping protein complex`. The metadiff F1 of 0.9 slightly under-represents the quality of the run: the agent made the same substantive ontology edits as the human PR, and the only meaningful difference is the wording of the obsolete-term comment.


## Strengths

- Correctly converted `GO:0005870` into an obsolete term by renaming it to `obsolete actin capping protein of dynactin complex`, adding `is_obsolete: true`, and prefixing the existing definition with `OBSOLETE.` while preserving the original `GOC:jl`, `PMID:18221362`, and `PMID:18544499` definition xrefs.
- Added the requested direct replacement, `replaced_by: GO:0008290`, matching the issue's specified replacement term `F-actin capping protein complex`.
- Removed the active logical definition from the obsolete stanza, including `intersection_of: GO:0008290 ! F-actin capping protein complex` and `intersection_of: part_of GO:0005869 ! dynactin complex`, so the obsolete term no longer classifies as an active cellular-component class.
- Added the correct tracker metadata, `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31956" xsd:anyURI`.
- Kept the edit tightly scoped to `GO:0005870` in `src/ontology/go-edit.obo`; there were no unrelated ontology changes.
- The agent's PR notes show appropriate checks for this simple obsoletion: it verified the target and replacement terms, checked for GO-internal usages of `GO:0005870`, and reported post-edit validation.


## Issues

- Minor comment wording issue: the agent wrote `The reason for obsoletion is that this term is equivalent to F-actin capping protein complex.`, while the human PR used the more cautious wording that `GO:0005870` is redundant with `GO:0008290` and annotations can be migrated. Because the original logical definition was `GO:0008290` plus `part_of GO:0005869` `dynactin complex`, saying it is strictly "equivalent to" `GO:0008290` overstates the relationship slightly. This is a style/precision issue in the explanatory comment, not a substantive failure of the obsoletion.
- No wrong term, missing replacement, syntax error, or scope creep was found.
