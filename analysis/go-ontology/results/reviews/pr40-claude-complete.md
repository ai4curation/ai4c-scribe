---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 40
agent: std_codex_g54
model: gpt-5.4
runtime: codex
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

gpt-5.4 / codex re-run producing the identical diff blob (`d9a1e5c`) to attempt #46. Correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups, with substantive literature review. F1=0.800 understates quality slightly. Reviewed in parallel with #46. (Note: an earlier `-claudecode-` review exists for this eval PR under a different reviewer/filename; this is the distinct `-claude-` review.)

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- Same strong RESEARCH.md as #46: PMID:12517450, PMID:11717276, PMID:21674802 reviewed; DESIGN_PATTERNS.md documenting the obsoletion precedent.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 stray comment removed — justified hygiene.
- Disciplined checklist with reasoned N/A entries (chemical-entity, taxon-constraint), prepared ISSUE_COMMENTS.md/PR_COMMENTS.md handoff artifacts.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in human PR → recall 0.727. Defensible curation.
- Obsoletion comment "is equivalent to GO:0102039" — imprecise rationale wording (over-specificity, not equivalence). Structural edit correct.
- Comment omits explicit EC 1.11.1.26 citation present in human comment. Stylistic.
- Reproducibility duplicate of #46.
