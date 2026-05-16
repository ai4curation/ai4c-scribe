---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 247
agent: std_opencode_kimik26
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.621
precision: 0.514
recall: 0.783
jaccard: 0.450
outcome: partial_success
failure_modes:
  - wrong_pattern
  - under_editing
  - syntax_error
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent produced an inconsistent half-merge: it set the obsoletion mechanics correctly (`is_obsolete: true`, `replaced_by: MONDO:0011274`, `IAO:0000231 MONDO:TermsMerged`) and added three synonyms to Muenke, but **left the bulk of the obsoleted stanza intact** (all five original synonyms plus both xrefs remain on MONDO:0023243), which violates the merge SOP requiring the obsoleted stanza to be reduced to six allowed lines. It also invented a non-existent xref qualifier. F1=0.621 roughly tracks the mixed quality; it neither matches the rejected obsolete-only approach (PR #10087) nor the endorsed full merge (PR #10106) cleanly.

## Strengths

- Correct obsoletion core: `is_obsolete: true`, `replaced_by: MONDO:0011274`, `property_value: IAO:0000231 MONDO:TermsMerged` (the merge-specific reason, not generic `OMO:0001000`).
- Removed the obsoletion-tracking subsets (`obsoletion_candidate`, `n_of_one`, `inferred_rare`), the `IAO:0006012` scheduled date, GARD `seeAlso`, and the long GARD definition from the obsoleted term.
- Did transfer three historical synonyms ("craniosynostosis - dysmorphism - brachydactyly", "craniosynostosis with facial dysmorphism and brachydactyly syndrome", "craniosynostosis-dysmorphism-brachydactyly syndrome") to Muenke, and added the issue #9798 `IAO:0000233` provenance.

## Issues

- **Wrong pattern / incomplete reduction:** The obsoleted MONDO:0023243 stanza still contains five `synonym:` lines and two `xref:` lines. Per the `merge-terms` SOP the obsoleted stanza must be reduced to id/name/`MONDO:TermsMerged`/issue link/`is_obsolete`/`replaced_by` only. Leaving synonyms/xrefs on an obsolete term is exactly what the SOP's Step 4 forbids and triggers QC failures.
- **Fabricated qualifier (effective syntax/vocabulary error):** Changed the xref source qualifier to `source="MONDO:obsoleteEquivalent"` on both Orphanet:1535 and SCTID:720814001. The correct, existing Mondo qualifier is `MONDO:equivalentObsolete` (as in gold and in the top attempts). `MONDO:obsoleteEquivalent` is not a recognized value — this will fail `qc-xref-without-precision`-style checks.
- **Omission:** Did not transfer the principal `synonym: "glass-chapman-hockley syndrome"` (the historical label the merge exists to preserve) to Muenke, nor did it transfer the xrefs to Muenke (they were left, mis-qualified, on the obsoleted term). The lexical resolution goal of the merge is not met.
- **Wrong evidence:** Synonyms added to Muenke are evidenced `[PMID:20108486]` only, dropping the GARD:0002479 provenance the source synonyms carried; defensible but lossy.
