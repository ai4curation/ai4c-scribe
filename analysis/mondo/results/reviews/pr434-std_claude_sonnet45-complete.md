---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 434
agent: std_claude_sonnet45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.500
precision: 0.400
recall: 0.667
jaccard: 0.333
outcome: failure
failure_modes:
  - wrong_pattern
  - under_editing
  - syntax_error
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The weakest of the ten attempts: a minimal obsolete-in-place that retains nearly the entire obsoleted stanza (def, comment, subsets `inferred_rare`/`n_of_one`/`rare`, all synonyms, both xrefs, and the GARD `seeAlso`) on MONDO:0023243, uses the generic `OMO:0001000` reason, and transfers **nothing** to the surviving Muenke term (MONDO:0011274). It is the obsolete-only pattern that PR #10087 was rejected for by @sabrinatoro before PR #10106 redid it as a merge — done even less completely than the haiku attempts. F1=0.500 over-represents quality.

## Strengths

- Correctly set `is_obsolete: true` and `replaced_by: MONDO:0011274`.
- Removed `subset: obsoletion_candidate` and the `IAO:0006012` scheduled-obsoletion date.
- Prefixed the definition with `OBSOLETE.` and added a coherent obsoletion comment citing PMID:20108486.
- Added `[GARD:0002479]` evidence to two previously empty-bracketed synonyms — a minor sourcing improvement (though on a term being obsoleted, where it has little value).

## Issues

- **Wrong pattern (decisive):** Pure obsoletion, not a merge, and the least-reduced obsoleted stanza of any attempt — it even keeps `subset: inferred_rare`, `subset: n_of_one`, `subset: rare` on the obsolete term. The merge-terms SOP requires the obsoleted stanza reduced to six lines and content transferred to Muenke. **Zero edits to MONDO:0011274**; the historical label does not resolve to Muenke.
- **Wrong obsoletion reason:** `property_value: IAO:0000231 OMO:0001000` instead of the merge-specific `MONDO:TermsMerged`.
- **Fabricated qualifier (vocabulary error):** `source="MONDO:obsoleteEquivalent"` on Orphanet:1535 and SCTID:720814001; correct value is `MONDO:equivalentObsolete`.
- **Omission:** No synonym or xref transferred to Muenke; `synonym: "glass-chapman-hockley syndrome"` is lost as a route to Muenke entirely.
- Retaining `is_a` parents was avoided (axioms removed) but the surrounding obsoletion is so incomplete that QC (`qc-obsoletion-reason`, deprecated-class-reference, xref-precision) would flag multiple problems.
