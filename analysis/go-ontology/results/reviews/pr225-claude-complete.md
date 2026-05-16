---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 225
agent: std_opencode_gem4
model: gemma-4-31b
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.727
precision: 0.889
recall: 0.615
jaccard: 0.571
outcome: partial_success
failure_modes:
  - over_editing
  - missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

gemma-4-31b / opencode produced a mostly correct obsoletion of GO:0008785 plus the two defensible comment cleanups, but **dropped the two historical term_tracker_items (#28261, #28340)** and *replaced* (rather than added) the tracker item with #31961. F1=0.727 (lowest recall of the well-formed attempts) partly reflects this provenance loss. The metadiff penalty here is appropriate and arguably still understates the provenance regression.

## Strengths

- Core obsoletion correct: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, rationale comment.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment correctly *deleted*.
- Replacement target GO:0102039 correctly identified despite the small model.
- obo-grep reference sweep performed; partial validation (timed-out travis_build, basic SPARQL checks passed) honestly disclosed.

## Issues

- Missed requirement / provenance loss: the original stanza had two `term_tracker_item`s (#28261, #28340). The diff *deletes both* and the obsolete term ends up with only the #31961 tracker item. The human gold PR explicitly *preserved* #28261 and #28340 and *added* #31961. Removing historical tracker items erases the term's provenance/history — a real regression, not just a scope difference. All higher-scoring attempts retained these.
- The obsoletion comment ("more specific than the specificity of any known gene product") is the minimal acceptable rationale; omits the replacement pointer and EC linkage. Adequate but thin.
- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in human PR (the GO:0070937 deletion is defensible hygiene).
- Net: the recall drop to 0.615 is driven mostly by the dropped tracker items, which is the appropriate penalty here (unlike the 0.762 cluster where the penalty was for benign churn).
