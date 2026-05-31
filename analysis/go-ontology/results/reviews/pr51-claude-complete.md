---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 51
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.762
precision: 0.889
recall: 0.667
jaccard: 0.615
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

gpt-5.4 / opencode produced a correct core obsoletion of GO:0008785 plus the two defensible comment cleanups, and additionally modified the *replacement* term GO:0102039 (added an EXACT synonym and a #31961 tracker item). F1=0.762 (lower recall than the 0.800 cluster) reflects the extra GO:0102039 hunk. The synonym addition is largely redundant; the score difference here is a fair penalty. Blob `e255e07`, identical to attempt #50.

## Strengths

- Correct, complete core obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment correctly *deleted* (correct action).
- Substantive validation: pre/post `make travis_build` passing, PMID:11717276 and PMID:21674802 validated with linkml-reference-validator, honest disclosure of the OAK import failure with documented fallback.
- The intent behind the GO:0102039 synonym ("preserve the previous label as searchable") is reasonable curatorial thinking.

## Issues

- Over-editing: added `synonym: "alkyl hydroperoxide reductase activity" EXACT []` to GO:0102039. This is essentially redundant — GO:0102039 already carries `synonym: "alkylhydroperoxide reductase activity" EXACT []` (only a space differs). GO synonym practice generally does not add near-duplicate spacing variants of an existing EXACT synonym; this is unnecessary churn on an active term.
- Over-editing: added a `term_tracker_item` for #31961 to GO:0102039. Tracker items document the issue's effect on the *obsoleted* term; attaching the obsoletion issue to the replacement term is non-standard (the human PR did not).
- These two GO:0102039 edits are why recall drops to 0.667 vs. the 0.800 cluster; unlike the GO:0009321/GO:0070937 hygiene, they are not clearly beneficial. Fair metadiff penalty.
- Duplicate blob with attempt #50.
