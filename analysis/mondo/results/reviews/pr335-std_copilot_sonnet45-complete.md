---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 335
agent: std_copilot_sonnet45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.561
precision: 0.457
recall: 0.727
jaccard: 0.390
outcome: failure
failure_modes:
  - wrong_pattern
  - under_editing
  - syntax_error
  - wrong_term
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

An obsolete-in-place with **no merge**, plus fabricated/incorrect provenance. The agent kept the obsoleted stanza, used the generic `OMO:0001000` reason, transferred **nothing** to Muenke (MONDO:0011274), invented an xref qualifier, attached an ORCID it had no basis for, and rewrote the definition with a mis-attributed citation. This reproduces the rejected obsolete-only pattern of PR #10087 (which @sabrinatoro asked the curator to redo as a merge in PR #10106), with extra accuracy problems. F1=0.561 over-represents quality.

## Strengths

- Correctly set `is_obsolete: true` and `replaced_by: MONDO:0011274`.
- Removed `subset: obsoletion_candidate`, the `IAO:0006012` scheduled date, and the `is_a` axioms from the obsoleted term.
- The PR writeup correctly identifies the underlying science (Glass et al. 1994 family later found to carry the FGFR3 P250R mutation = Muenke syndrome).

## Issues

- **Wrong pattern (decisive):** Pure obsoletion; the obsoleted stanza keeps def/synonyms/xrefs and **no content is transferred to MONDO:0011274**. The historical label does not resolve to Muenke post-PR — the exact defect that caused PR #10087 to be redone as a merge.
- **Wrong obsoletion reason:** `property_value: IAO:0000231 OMO:0001000` instead of the merge-specific `MONDO:TermsMerged`.
- **Fabricated qualifier (vocabulary error):** `source="MONDO:obsoleteEquivalent"` on Orphanet:1535 and SCTID:720814001; correct value is `MONDO:equivalentObsolete`. It also stripped the legitimate `source="GARD:0002479"` from the Orphanet:1535 xref.
- **Unbased ORCID attribution:** Added `property_value: http://purl.org/dc/terms/creator https://orcid.org/0000-0001-5208-3432` — an ORCID the agent had no basis to assign as creator of this obsoletion (the issue provides no ORCID; the PR text even cites a *different* ORCID, 0000-0001-5208-3432 vs the 0000-0002-4142-7153 elsewhere — internally inconsistent).
- **Mis-attributed citation (wrong_term):** Rewrote the definition with reference `[PMC:PMC5051481, PMID:7981856]`. PMC5051481 in the diff is paired with a "Cleidocranial dysplasia / RUNX2 mutations" citation in the PR's reference list — an unrelated paper; the issue's supporting article is PMID:20108486 / PMC5051481 for the Glass→Muenke merge. The reference handling is muddled and partly wrong.
- **Omission:** No synonym ("glass-chapman-hockley syndrome") or xref transferred to Muenke.
