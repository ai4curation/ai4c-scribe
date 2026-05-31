---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 38
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v8
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

gpt-5.5 / codex (v8) produced a correct core obsoletion of GO:0008785 plus the two defensible comment cleanups, and the same extra (largely redundant) GO:0102039 synonym + tracker-item edits as the 0.762 opencode runs. F1=0.762; recall drop is a fair penalty for the GO:0102039 churn. Has the most rigorous annotation-impact verification of any attempt in the case. Blob `ae96d5d`.

## Strengths

- Correct, complete core obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment correctly *deleted*.
- Best annotation-impact verification in the set: when the OAK `Format.JSON` AttributeError blocked `runoak ... associations`, the agent fell back to querying the GO public Solr endpoint and independently recovered all 3 direct annotations (EcoliWiki AhpF IGI PMID:11717276, PseudoCAP PA3529 IDA PMID:21674802, CGD AHP1 ISS PMID:14555484) — exceeding the issue's own listing. Excellent failure-recovery methodology.
- RESEARCH.md SUPPORT excerpts validated with linkml-reference-validator; pre/post `make travis_build` passing; honest note that pre-existing RHEA warnings were not introduced by this change.

## Issues

- Over-editing: added the redundant `synonym: "alkyl hydroperoxide reductase activity" EXACT []` to GO:0102039 (already has `alkylhydroperoxide reductase activity` EXACT) and a non-standard #31961 `term_tracker_item` on the replacement term. Not clearly beneficial; absent from the human PR. Fairly penalized in recall — the strong methodology does not offset the unnecessary edits to an active term.
- Comment ("describes an over-specific substrate-specific reaction ...") is accurate but, like the cluster, omits the explicit EC 1.11.1.26 citation. Stylistic.
