---
ontology: go-ontology
issue_number: 31961
pr_number: 32015
eval_repo_pr: 498
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
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

The agent produced a textbook obsoletion of GO:0008785 that is structurally identical to the human gold PR #32015 for the core stanza, and additionally rewired the two in-ontology comment cross-references that pointed at the now-obsolete term. The metadiff F1=0.800 slightly *understates* quality: the two extra hunks (GO:0009321, GO:0070937) are defensible ontology hygiene that the human PR omitted, not erroneous edits. Blob `c2f046b`, shared with attempt #437.

## Strengths

- Correct standard obsoletion pattern on GO:0008785: name → `obsolete alkyl hydroperoxide reductase activity`, `def` prefixed `OBSOLETE.`, `is_a: GO:0016668` removed, `is_obsolete: true`, `replaced_by: GO:0102039`, plus a rationale comment.
- Correctly identified GO:0102039 as the replacement via the EC:1.11.1.26 / Expasy synonym chain — exactly the human's reasoning.
- Added `term_tracker_item` for #31961 while preserving the two historical tracker items (#28261, #28340) — matches the human PR's provenance handling.
- Rewired GO:0009321 (alkyl hydroperoxide reductase complex) `comment` from GO:0008785 to GO:0102039: a correct active-term reference that prevents a dangling pointer to an obsolete term.
- Removed the spurious GO:0070937 (CRD-mediated mRNA stability complex) `comment` referencing GO:0008785 — a genuine pre-existing copy/paste artifact (the two terms are biologically unrelated). This is justified cleanup.
- PR comment includes a correct annotation-impact analysis (3 annotations, EcoliWiki/PseudoCAP/CGD) and correctly defers annotation migration to go-annotation#6396.

## Issues

- Scope: the GO:0009321/GO:0070937 edits go beyond the human PR's single-stanza change, lowering metadiff recall to 0.727. These are defensible (they discharge references to the obsoleted term) but were not strictly required by the issue and constitute the only "failure mode" here — over-editing in the metadiff sense, not a curation error.
- Obsoletion comment is adequate but terser than the human's; it omits the explicit EC 1.11.1.26 / Expasy citation that the human comment carries. Stylistic, not incorrect.
- No substantive errors; OBO syntax is clean and would pass the obsoletion QC checks.
