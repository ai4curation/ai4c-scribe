---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 227
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

Bit-for-bit duplicate of attempt #228 (blob `bbd4dda`, same kimi-k2.6 / opencode, re-run); only the diff is captured here, no PR/issue narrative. Correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups. F1=0.800 modestly understates quality. Reviewed in parallel with #228.

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, both historical tracker items preserved.
- GO:0102039 is the correct replacement (matches human gold and the issue's EC:1.11.1.26 reasoning).
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment removed — justified hygiene.
- OBO syntax clean; would pass the obsoletion QC checks.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in human PR → recall 0.727. Defensible curation.
- Same comment-quality weakness as #228: "this term is equivalent to NADH-dependent peroxiredoxin activity" is an imprecise rationale (over-specificity, not equivalence) and omits the EC citation. Wording nit, not a data error.
- Reproducibility duplicate of #228; no additional signal.
