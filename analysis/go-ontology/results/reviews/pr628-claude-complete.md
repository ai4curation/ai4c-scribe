---
ontology: go-ontology
issue_number: 32044
pr_number: 32054
eval_repo_pr: 628
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: new_term
difficulty: medium
case_quality: poor
case_quality_reason: gold_pr_has_out_of_scope_extra_edit
f1: 0.667
precision: 0.583
recall: 0.778
jaccard: 0.500
outcome: partial_success
failure_modes:
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This run (gpt-5.4/opencode) produced a diff byte-identical to attempt #678 (blob
`2c84b46`): it created `GO:7770074 protein O-linked glycosylation via
N-acetylglucosamine` as a single `is_a: GO:0006493` child with PMID:35536957, the
two requested EXACT synonyms, and the #32044 tracker — and nothing else, exactly the
issue's explicit ask. The lone substantive blemish is the definition paraphrase
("…**starting with** the covalent linkage of a single N-acetylglucosamine…"), which
connotes chain initiation and reads awkwardly against the no-elongation clause.
F1 = 0.667 under-represents quality (the recall gap is the gold's out-of-scope
`GO:0016266` rename), but the definition drift keeps this at `partial_success`.

## Strengths

- Verbatim-correct structural fields: ID `GO:7770074`, label,
  `biological_process` namespace, single `is_a: GO:0006493` parent, PMID:35536957,
  #32044 `term_tracker_item`.
- Tight scope discipline — only the requested new term was added; no edits to
  siblings or unrelated terms.
- Retained the "not elongated into a larger oligosaccharide chain" distinction that
  separates O-GlcNAc from GalNAc-initiated (GO:0016266) mucin-type O-glycosylation.
- Declined to add a CHEBI `intersection_of`, consistent with sibling-term precedent
  under `GO:0006493`.

## Issues

- **Definition drift (content):** Issue/gold reads "…a glycoprotein biosynthetic
  process **in which** a single N-acetylglucosamine is covalently linked…"; the
  agent wrote "…**starting with** the covalent linkage…", the same paraphrase fault
  flagged for #539/#552/#678. "Starting with" implies an initiating step of a longer
  build-up, contradicting the single-sugar/no-elongation semantics. The exact text
  was supplied verbatim in an issue comment.
- **Style (trivial):** Second synonym `protein O-linked-N-acetylglucosaminylation`
  (extra hyphen) vs. issue/gold `protein O-linked N-acetylglucosaminylation`.
  Cosmetic only.
- **Scope (not a fault):** Did not perform the gold's unsolicited `GO:0016266`
  GalNAc spelling harmonization; outside #32044's explicit ask and the sole reason
  recall < 1.0, not a true omission.
- **Note:** Identical to #678 — same model/runtime, same blob `2c84b46`; treat as a
  reproducibility duplicate.
