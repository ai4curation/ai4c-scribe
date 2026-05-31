---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 46
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

gpt-5.4 / codex produced a correct standard obsoletion of GO:0008785 plus the two defensible cross-reference cleanups, with the most substantive literature review of the codex attempts (three issue-cited PMIDs reviewed). F1=0.800 understates quality slightly. Blob `d9a1e5c`, identical to attempt #40 (same model/runtime, re-run).

## Strengths

- Correct, complete obsoletion: obsolete name prefix, `OBSOLETE.` def prefix, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, #31961 tracker item, historical tracker items preserved.
- Strongest research methodology in the codex set: RESEARCH.md reviews PMID:12517450 (peroxiredoxin mechanism), PMID:11717276 (E. coli Ahp peroxide scavenging), and PMID:21674802 (Pseudomonas AhpC as a 2-Cys peroxiredoxin) — biologically grounds the substrate-specificity argument rather than just restating the issue.
- GO:0009321 comment rewired to GO:0102039; GO:0070937 spurious comment removed with a clear rationale that it is "stray and unrelated."
- Honest disclosure of NCBI HTTP 429 and the OAK import failure, with documented Europe PMC fallback for PMID metadata.

## Issues

- Scope/over-editing (metadiff-only): GO:0009321/GO:0070937 hunks not in human PR → recall 0.727. Defensible curation.
- Obsoletion comment says the term "is equivalent to GO:0102039" — same imprecision flagged elsewhere: the rationale is over-specificity vs. gene products, not strict equivalence. Wording nit; the structural `replaced_by` edit is correct.
- Comment omits the explicit EC 1.11.1.26 citation present in the human comment. Stylistic.
- Duplicate blob with attempt #40.
