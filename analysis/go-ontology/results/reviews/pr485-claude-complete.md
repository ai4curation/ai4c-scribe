---
ontology: go-ontology
issue_number: 32018
pr_number: 32021
eval_repo_pr: 485
agent: std_claude_cs45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v9
case_type: obsoletion
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: partial_success
failure_modes: [missed_requirement, wrong_pattern]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [32023, 32069]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

<!-- Re-reviewed against issue #32018 + union of human PRs #32021 + #32023 + #32069.
  Gold PR #32021 only covers the taxon-constraint sub-step; metadiff F1=0.0 is not
  meaningful for this case (see cases/pr32021/METADATA.md, case_quality: poor). -->

## Summary

The agent did a substantively correct and thoroughly documented full obsoletion of `GO:0052704` and `GO:0140479` (replaced by `GO:0052699`), added both MetaCyc `narrowMatch` xrefs + trackers to the parent, rewired the two dependent MF `part_of` links, and fixed the `GO:0052707` redirect — reproducing the go-edit.obo content of human PRs #32023 + #32069. F1=0.0 is a gold-selection artifact. The substantive gap is the untouched `only_in_taxon.tsv` (the actual gold PR), compounded by an explicit but incorrect "no synonyms on obsolete terms" rationale used to strip metadata.

## Strengths

- Correct, complete go-edit.obo obsoletion of both terms with full metadata (obsolete name/def, comment, `is_obsolete`, `replaced_by: GO:0052699`, #32018 tracker).
- MetaCyc `PWY-7255`/`PWY-7550` `narrowMatch` xrefs + tracker on `GO:0052699`; `GO:0044875` and the hercynylcysteine MF `part_of` rewired; `GO:0052707` `replaced_by` corrected to `GO:0052699` — all matching the human #32023/#32069 work.
- Strong methodology and communication: documented research/impact analysis (4 EXP on `GO:0052704`, 0 on `GO:0140479`), MetaCyc mapping rationale, and an explicit checklist.

## Issues

- **Omission (missed_requirement):** did not remove the two rows from `src/taxon_constraints/only_in_taxon.tsv` — the literal gold PR #32021 and a required CI precondition for obsoleting these taxon-constrained terms.
- **Wrong pattern (minor):** stripped the `BROAD` synonym and `Wikipedia:Ergothioneine` xref from `GO:0052704`, explicitly justified in the checklist as "No synonyms on obsolete terms (as per GO best practice)." That is an over-generalization — human PR #32069 deliberately kept both. The confident but incorrect rationale is more concerning than the edit itself.
- **Style:** the PR comment is very long with several uncommitted analysis docs; thorough but heavier than necessary for a routine obsoletion.
