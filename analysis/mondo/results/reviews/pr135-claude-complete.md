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
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
outcome: partial_success
failure_modes: [under_editing, missed_requirement]
---

## Summary

Replicate run of the same gpt-5.5/opencode configuration as eval PR #116 — the diff is byte-identical (blob `9a96c3b`, F1=0.772). The agent obsoleted MONDO:0023243 correctly at the stanza level (`name: obsolete glass-chapman-hockley syndrome`, `IAO:0000231 MONDO:TermsMerged`, issue link, `is_obsolete: true`, `replaced_by: MONDO:0011274`) but **transferred no content to the surviving Muenke syndrome term MONDO:0011274**. This reproduces the obsolete-only pattern reviewer @sabrinatoro **repudiated** in the curator's first attempt #10087, requiring a true merge. The joint-highest F1=0.772 is a metadiff artefact (only the obsolete-stanza hunk is touched, no extra lines, so recall=1.0 on that hunk) and badly over-represents completeness.

## Strengths

- Obsolete stanza is exactly correct and byte-identical to gold's obsolete hunk: correct merge-specific `IAO:0000231 MONDO:TermsMerged` reason, correct `replaced_by: MONDO:0011274`, def/comment/subsets/is_a/scheduled-date all stripped.
- No fabricated `MONDO:obsoleteEquivalent` qualifier and no `OMO:0001000` mis-reason — clean within the (incomplete) scope attempted.
- Deterministic reproducibility with #116 is itself a positive signal for this configuration.

## Issues

- **Missed requirement (core defect):** identical to #116 — no synonyms or xrefs (glass-chapman-hockley labels, craniosynostosis-dysmorphism-brachydactyly synonyms, Orphanet:1535, SCTID:720814001) transferred to MONDO:0011274. The historical→Muenke lexical bridge is lost, exactly the data-loss objection @sabrinatoro raised against #10087.
- **Under-editing:** reproduced the *abandoned* human approach rather than the *approved* merge. Would require the same curator correction #10087 received.
- The F1 ranking is misleading relative to the full-merge attempts (#100/#165/#375), which did substantially more correct work. Judge substance: this is materially less complete than those.

Net: partial success — clean obsoletion, merge half missing; reproduces a repudiated pattern. Same assessment as #116.
