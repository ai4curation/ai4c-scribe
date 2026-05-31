---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 228
agent: std_opencode_kimi
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.800
precision: 0.889
recall: 0.727
jaccard: 0.667
outcome: partial_success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: "2026-05-15"
---

## Summary

kimi-k2.6 / opencode produced the correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups, structurally matching the human gold stanza. F1=0.800 modestly understates quality. Blob `bbd4dda`, identical to attempt #227 (same model/runtime, re-run).

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, both historical tracker items (#28261, #28340) preserved.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment removed — justified hygiene discharging dangling references to the obsoleted term.
- PR comment reports pre/post `robot reason -r ELK` and obsoletion-relevant SPARQL checks passing; obo-grep confirmation that no references to GO:0008785 remain.
- Correctly defers the two experimental annotation migrations to the annotation workflow.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks absent from human PR → recall 0.727. Defensible curation.
- Obsoletion comment is weakest of the 0.800 cluster: "The reason for obsoletion is that this term is equivalent to NADH-dependent peroxiredoxin activity." Calling it "equivalent" is imprecise — the issue's rationale is over-specificity vs. known gene products, not strict equivalence (if it were equivalent, a merge rather than substrate-specificity obsoletion would be implied). Structurally correct (`replaced_by`), but the comment loses the actual rationale and omits the EC citation.
- Duplicate blob with attempt #227.
