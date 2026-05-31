---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 218
agent: std_claude_hai45
model: claude-haiku-4.5
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
reviewed_by: codex
reviewed_at: "2026-05-16"
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/32018
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32021
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/218
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 32018 --repo geneontology/go-ontology
    gh pr diff 32021 --repo geneontology/go-ontology
    gh pr diff 218 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent made a substantively reasonable ontology obsoletion for the two ergothioneine pathway-variant terms: `GO:0052704` and `GO:0140479` were obsoleted, replaced by `GO:0052699`, and the MetaCyc pathway mappings were moved to the parent as `narrowMatch` xrefs. The `f1=0.0` score is technically correct because the agent's diff has no overlap with the human PR, but it under-represents the biological quality of the agent's work: the human PR only removed the two stale taxon constraint rows, while the agent addressed most of the issue text. The agent still missed that taxon-constraint cleanup, so the result is incomplete.


## Strengths

- Correctly identified the two requested child process terms, `GO:0052704` (`ergothioneine biosynthesis from histidine via gamma-glutamyl-hercynylcysteine sulfoxide`) and `GO:0140479` (`ergothioneine biosynthesis from histidine via hercynylcysteine sulfoxide synthase`), as terms to obsolete.
- Correctly used `GO:0052699` (`ergothioneine biosynthetic process`) as the `replaced_by` target for both obsolete child terms, matching the issue request.
- Added `MetaCyc:PWY-7255` and `MetaCyc:PWY-7550` to `GO:0052699` with `source="skos:narrowMatch"`, which follows the issue's instruction to represent the bacterial and fungal pathway variants as narrower external pathways of the general GO process.
- Removed the obsolete terms' asserted `is_a` links and added `is_obsolete: true`, obsolete-prefixed labels/definitions, explanatory comments, and tracker links to issue `#32018`.
- Rewired internal `part_of` references from the now-obsolete processes to the parent process: `GO:0044875` was changed from `part_of GO:0052704` to `part_of GO:0052699`, and `GO:0061686` was changed from `part_of GO:0140479` to `part_of GO:0052699`.


## Issues

- The agent missed the actual human PR change: removing the two rows for `GO:0052704` and `GO:0140479` from `src/taxon_constraints/only_in_taxon.tsv`. Leaving `only_in_taxon` constraints for obsolete terms is stale ancillary data and is exactly what the accepted PR cleaned up.
- The agent's PR changed only `src/ontology/go-edit.obo`, so the diff does not include the curated repository's taxon-constraint maintenance even though the source issue explicitly noted that `GO:0052704` was only in bacteria and `GO:0140479` was only in fungi.
- The agent's scope is broader than the human PR, but most of that extra scope is justified by the issue text rather than gratuitous over-editing. The main quality problem is incompleteness, not a wrong target term or bad replacement choice.
