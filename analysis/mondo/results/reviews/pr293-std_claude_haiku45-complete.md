---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 293
agent: std_claude_haiku45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.600
precision: 0.514
recall: 0.720
jaccard: 0.429
outcome: failure
failure_modes:
  - wrong_pattern
  - under_editing
  - syntax_error
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This run produced a byte-identical diff (blob `dd5bee2`) to attempt #424 from the same claude-haiku-4.5/claude configuration: an obsolete-in-place with **no merge**. The full obsoleted stanza is retained on MONDO:0023243, the obsoletion reason is the generic `OMO:0001000`, and **nothing is transferred to the surviving Muenke term** (MONDO:0011274). This is the obsolete-only approach the curator's PR #10087 was rejected for by reviewer @sabrinatoro before the gold PR #10106 redid it as a true merge. F1=0.600 over-represents quality: only the obsoleted stanza was touched, and against the SOP.

## Strengths

- Correctly set `is_obsolete: true` and `replaced_by: MONDO:0011274`.
- Removed `subset: obsoletion_candidate` and the `IAO:0006012` scheduled-obsoletion date.
- Prefixed the definition with `OBSOLETE.` and added a coherent merge-rationale comment citing PMID:20108486 — adequate for a standalone obsoletion but not the required merge.
- Deterministic reproducibility with #424 (same blob) is a (weak) positive signal for configuration stability, though here it reproduces the same wrong pattern.

## Issues

- **Wrong pattern (decisive):** Pure obsoletion, not a merge. Obsoleted stanza keeps def/synonyms/xrefs; **zero edits to MONDO:0011274**. The historical label "glass-chapman-hockley syndrome" no longer resolves to Muenke — the exact problem @sabrinatoro flagged on PR #10087.
- **Wrong obsoletion reason:** `property_value: IAO:0000231 OMO:0001000` instead of the merge-specific `MONDO:TermsMerged`.
- **Fabricated qualifier (vocabulary error):** `source="MONDO:obsoleteEquivalent"` on Orphanet:1535 and SCTID:720814001; correct value is `MONDO:equivalentObsolete`.
- **Unrequested synonym scope churn:** Flipped "craniosynostosis with facial dysmorphism and brachydactyly syndrome" EXACT→RELATED and "glass chapman hockley syndrome" RELATED→EXACT with no rationale.
- **Stray creator property:** Added `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-4142-7153` to the obsoleted term — not in the SOP, unattributed ORCID guess.
