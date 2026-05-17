---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 424
agent: std_claude_hai45
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

The agent performed an obsolete-in-place with **no merge**: it kept the full obsoleted stanza (definition, synonyms, xrefs) on MONDO:0023243, used the generic obsoletion reason `OMO:0001000` instead of `MONDO:TermsMerged`, and transferred **nothing** to the surviving Muenke term (MONDO:0011274). This is precisely the obsolete-only approach the curator's PR #10087 was rejected for by reviewer @sabrinatoro before PR #10106 redid it as a true merge. F1=0.600 over-represents quality — the agent only touched the obsoleted stanza and did so against the SOP. (This run's diff is byte-identical, blob `dd5bee2`, to attempt #293 from the same haiku/claude configuration.)

## Strengths

- Correctly set `is_obsolete: true` and `replaced_by: MONDO:0011274`.
- Removed the `subset: obsoletion_candidate` and the `IAO:0006012` scheduled-obsoletion date.
- Prefixed the definition with `OBSOLETE.` and added a merge-rationale comment citing PMID:20108486 — internally coherent for a standalone obsoletion.

## Issues

- **Wrong pattern (decisive):** This is a pure obsoletion, not a merge. The merge-terms SOP (and the reviewer's explicit instruction on PR #10087) require the obsoleted stanza to be reduced to six lines and the content transferred to Muenke. The agent did the opposite — it kept def/synonyms/xrefs on the obsoleted term and made **zero edits to MONDO:0011274**. "glass-chapman-hockley syndrome" no longer resolves to Muenke.
- **Wrong obsoletion reason:** Used `property_value: IAO:0000231 OMO:0001000` (generic "obsolete") instead of the merge-specific `MONDO:TermsMerged` the SOP mandates for term merges. Will fail `qc-obsoletion-reason`-style expectations for a `replaced_by` merge.
- **Fabricated qualifier (vocabulary error):** Changed xref sources to `source="MONDO:obsoleteEquivalent"` on Orphanet:1535 and SCTID:720814001. The correct existing qualifier is `MONDO:equivalentObsolete`; `MONDO:obsoleteEquivalent` is not a recognized value.
- **Unrequested edits to retained synonyms:** Flipped `synonym: "craniosynostosis with facial dysmorphism and brachydactyly syndrome"` from EXACT to RELATED and `synonym: "glass chapman hockley syndrome"` from RELATED to EXACT, with no sourcing rationale — gratuitous scope churn on a term being obsoleted.
- **Stray creator property:** Added `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0002-4142-7153` to the obsoleted term; not part of the SOP and an unattributed ORCID guess.
