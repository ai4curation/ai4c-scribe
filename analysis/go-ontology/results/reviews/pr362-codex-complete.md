---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 362
agent: std_gemini_flash
model: gemini-2.5-flash
runtime: gemini
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.308
precision: 0.222
recall: 0.5
jaccard: 0.182
outcome: failure
failure_modes:
- under_editing
- missed_requirement
- wrong_pattern
- scope_creep
reviewed_by: gpt-5.5
reviewed_at: '2026-05-16'
---

<!-- Review this eval run following analysis/instructions/review-agent-eval.md

  Source issue: https://github.com/geneontology/go-ontology/issues/31961
  Human PR (ground truth): https://github.com/geneontology/go-ontology/pull/32015
  Agent PR (eval): https://github.com/ai4curation/eval-ont-agent-go/pull/362
  Agent config: ai4curation/go-ontology-agent-config

  Quick reference:
    gh issue view 31961 --repo geneontology/go-ontology
    gh pr diff 32015 --repo geneontology/go-ontology
    gh pr diff 362 --repo ai4curation/eval-ont-agent-go
-->

## Summary

The agent identified GO:0102039 as the intended replacement, but it did not perform a valid GO obsoletion for GO:0008785. It left the active name and definition in place, retained the active `is_a` parent, omitted the issue tracker link, and added a reverse `consider: GO:0008785` on GO:0102039. The 0.308 metadiff score reflects a real failure rather than just wording differences.

## Strengths

- Found the correct replacement target, GO:0102039 NADH-dependent peroxiredoxin activity.
- Added `is_obsolete: true` and `replaced_by: GO:0102039` to GO:0008785.
- Added a brief comment indicating that the term was too specific for known gene products.

## Issues

- Missing required obsoletion mechanics: the name was not prefixed with `obsolete`, the definition was not prefixed with `OBSOLETE.`, and the active `is_a: GO:0016668` relationship was not removed.
- Missing provenance: the attempt did not add `property_value: term_tracker_item` for issue 31961.
- Wrong pattern: it added `consider: GO:0008785` to GO:0102039, pointing the valid replacement term back at the newly obsolete term.
- The patch does not update or remove the stale textual references handled in other attempts, but more importantly the target term itself is left in an internally inconsistent obsolete state.
