---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 135
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.772
precision: 0.629
recall: 1.000
jaccard: 0.629
outcome: partial_success
failure_modes:
  - under_editing
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent performed a clean, syntactically valid obsoletion of MONDO:0023243 with `replaced_by: MONDO:0011274` and the correct `IAO:0000231 MONDO:TermsMerged` reason. However, it executed only "half" of the merge: it stripped the obsoleted stanza correctly but did **not** transfer any synonyms or xrefs onto the surviving Muenke syndrome term (MONDO:0011274). This is the exact failure pattern (obsolete-without-merge) that the curator's first PR #10087 was rejected for by reviewer @sabrinatoro before PR #10106 (the gold) re-did it as a full merge. The F1 of 0.772 (with recall=1.0, precision=0.629) over-represents quality somewhat: every line the agent wrote matches the gold (hence recall=1.0), but it omitted the entire surviving-term content-transfer half of the merge SOP.

## Strengths

- Obsoleted stanza is exactly correct and minimal: `name: obsolete glass-chapman-hockley syndrome`, `property_value: IAO:0000231 MONDO:TermsMerged`, the `IAO:0000233` issue #9798 link, `is_obsolete: true`, `replaced_by: MONDO:0011274` — byte-identical to the gold's obsoleted stanza.
- Correctly used `MONDO:TermsMerged` as the obsoletion reason (not the generic `OMO:0001000`), which is the merge-specific reason the `merge-terms` skill mandates and which the lower-scoring claude/copilot attempts got wrong.
- Correctly removed all obsoletion-tracking cruft from the obsoleted term (`subset: obsoletion_candidate`, `subset: n_of_one`, `subset: inferred_rare`, `IAO:0006012` scheduled date, GARD `seeAlso`, the long GARD definition).
- Did not create a spurious `alt_id` and left no dangling references to MONDO:0023243.

## Issues

- **Omission (the headline issue):** No content was transferred to MONDO:0011274. The gold moves the historical synonyms ("craniosynostosis - dysmorphism - brachydactyly", "craniosynostosis-dysmorphism-brachydactyly syndrome", and crucially `synonym: "glass-chapman-hockley syndrome" EXACT [PMID:20108486]`) and the `xref: Orphanet:1535 {source="...MONDO:equivalentObsolete"}` / `xref: SCTID:720814001 {source="...MONDO:equivalentObsolete"}` onto Muenke. None of this was done. A user searching "glass-chapman-hockley syndrome" would no longer resolve to Muenke after this PR — the principal reason @sabrinatoro asked for a true merge.
- **Wrong pattern:** This is effectively a pure obsoletion, the approach the curator explicitly abandoned (PR #10087) on reviewer instruction in favor of a merge. The agent's PR text even claims "direct replacement" but provides no replacement-target enrichment.
- The high F1/perfect recall is an artifact of the gold's obsoleted-stanza edits being a subset of the full change; it should not be read as "did the same work as the human."
