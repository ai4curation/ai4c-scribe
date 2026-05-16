---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 100
agent: std_codex_gpt55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.765
precision: 0.743
recall: 0.788
jaccard: 0.619
outcome: success
failure_modes:
  - over_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is the strongest substantive result of the ten attempts. The agent performed a genuine full **merge** of MONDO:0023243 into MONDO:0011274 (Muenke syndrome): the obsoleted stanza is reduced exactly per the merge SOP, and the historical synonyms and the Orphanet:1535 / SCTID:720814001 xrefs are correctly transferred onto Muenke as `MONDO:equivalentObsolete`. It matches the curator-endorsed merge approach (PR #10106) rather than the rejected obsolete-only approach (PR #10087). F1=0.765 (precision=0.743, recall=0.788) materially **under-represents** quality here — the deltas from gold are defensible evidence/scope choices and a couple of owltools-mechanical artifacts, not errors.

## Strengths

- Correct merge execution: obsoleted stanza reduced to `name: obsolete glass-chapman-hockley syndrome`, `IAO:0000231 MONDO:TermsMerged`, issue #9798 link, `is_obsolete: true`, `replaced_by: MONDO:0011274` — exactly as gold.
- Transferred all four "craniosynostosis...brachydactyly" historical synonyms plus `synonym: "glass-chapman-hockley syndrome" EXACT [GARD:0002479, PMID:20108486]` onto Muenke, so the historical label still resolves to Muenke post-merge (the core point @sabrinatoro insisted on).
- Transferred both `xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}` and `xref: SCTID:720814001 {source="MONDO:equivalentObsolete"}` — and notably **kept SCTID:720814001**, matching gold. Several other strong attempts (opus #375, gpt-5.5/opencode) dropped this xref; this agent got it right.
- Added the `IAO:0000233` issue #9798 provenance to Muenke (matches gold).
- Used `MONDO:equivalentObsolete` (correct existing-vocabulary qualifier), not the invented `MONDO:obsoleteEquivalent` that the kimi/haiku/sonnet attempts fabricated.

## Issues

- **Scope/over-edit:** The agent re-evidenced an unrelated pre-existing synonym, changing `synonym: "Muenke nonsyndromic coronal craniosynostosis" RELATED []` to `... RELATED [MEDGEN:355217]`. This synonym was not part of the merge; adding an MEDGEN source to it is an unrequested edit (gold instead *deletes* this synonym, itself a gold-side over-edit not asked for by the issue). Both diverge from the issue scope; neither is clearly wrong.
- **Style/scope difference:** The transferred synonyms are kept at `RELATED` scope (mirroring the obsoleted term), whereas gold promotes them to `EXACT`. Both are defensible; the source term itself had them as RELATED, so the agent's choice is the more conservative and arguably more faithful one.
- **Evidence difference:** Agent cites `[GARD:0002479, PMID:20108486]` on "glass-chapman-hockley syndrome"; gold cites only `[PMID:20108486]`. The agent's is a superset and well-sourced — a near-trivial metadiff penalty.
- Did not replicate gold's incidental, issue-unrelated cleanups (`MNKES` RELATED→EXACT ABBREVIATION; deletion of "Muenke nonsyndromic coronal craniosynostosis"; addition of `subset: inferred_rare`). These are gold over-edits, so omitting them is correct scope discipline, but they cost recall under metadiff.
