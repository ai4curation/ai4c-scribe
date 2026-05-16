---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 116
agent: std_opencode_gpt55
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

This run produced a byte-identical diff (blob `9a96c3b`) to attempt #135 from the same gpt-5.5/opencode configuration: a clean obsoletion of MONDO:0023243 with `replaced_by: MONDO:0011274` and `IAO:0000231 MONDO:TermsMerged`, but with **no content transferred to the surviving Muenke syndrome term** (MONDO:0011274). It is the obsolete-without-merge half of the task — the same pattern the curator's first PR #10087 was rejected for before the gold PR #10106 redid it as a full merge. F1=0.772 (recall=1.0, precision=0.629) over-represents quality: every emitted line matches gold, but the entire surviving-term enrichment half is missing.

## Strengths

- Obsoleted stanza is exactly correct: `name: obsolete glass-chapman-hockley syndrome`, `property_value: IAO:0000231 MONDO:TermsMerged`, issue #9798 `IAO:0000233` link, `is_obsolete: true`, `replaced_by: MONDO:0011274` — identical to gold's obsoleted stanza.
- Used the merge-specific obsoletion reason `MONDO:TermsMerged` rather than the generic `OMO:0001000` that the weaker claude/copilot attempts incorrectly used.
- Removed all obsoletion-tracking metadata (`subset: obsoletion_candidate`, `n_of_one`, `inferred_rare`, `IAO:0006012`, GARD `seeAlso`, GARD definition); no spurious `alt_id`; no dangling references.
- Deterministic reproducibility across runs (#116 == #135) is a positive signal for this configuration on a mechanical task.

## Issues

- **Omission:** No synonyms or xrefs transferred to MONDO:0011274. The gold moves `synonym: "glass-chapman-hockley syndrome" EXACT [PMID:20108486]`, three "craniosynostosis...brachydactyly" synonyms, and `xref: Orphanet:1535`/`xref: SCTID:720814001` (both as `MONDO:equivalentObsolete`) onto Muenke. None done; "glass-chapman-hockley syndrome" no longer resolves to Muenke post-PR.
- **Wrong pattern:** Pure obsoletion, the approach the curator abandoned (PR #10087) on reviewer @sabrinatoro's instruction to do a true merge.
- High F1/perfect recall is a metadiff artifact (gold obsoleted-stanza edits are a subset of the full change), not evidence of parity with the human.
