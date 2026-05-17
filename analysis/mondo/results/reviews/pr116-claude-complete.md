---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 116
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
failure_modes: [under_editing, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The agent obsoleted MONDO:0023243 correctly at the stanza level — `name: obsolete glass-chapman-hockley syndrome`, `IAO:0000231 MONDO:TermsMerged`, issue link, `is_obsolete: true`, `replaced_by: MONDO:0011274` — but **did not transfer any content to the surviving Muenke syndrome term MONDO:0011274**. The diff touches only the obsoleted stanza. This is precisely the pattern reviewer @sabrinatoro **repudiated** in the curator's first attempt #10087 ("If the term is the same as the other one, then it should be merged. In this case, follow the merge procedure"). The headline F1=0.772 (the joint-highest in the set) is a metadiff artefact: because the agent made only the obsolete-stanza changes and no extra lines, recall on that hunk is 1.0 and precision is moderate, even though half the required curation (the synonym/xref transfer to Muenke) is entirely missing.

## Strengths

- Obsolete stanza is exactly correct and byte-identical to gold's obsolete hunk: correct `MONDO:TermsMerged` reason (not the erroneous `OMO:0001000`), correct `replaced_by: MONDO:0011274`, removal of def/comment/subsets/is_a/scheduled-obsoletion date.
- No fabricated `MONDO:obsoleteEquivalent` qualifier, no spurious extra edits — clean and conservative within the scope it attempted.
- Recognized the issue's `replaced_by` (rather than weaker "consider") was warranted given the Orphanet/PMID equivalence evidence.

## Issues

- **Missed requirement (the core defect):** no synonyms or xrefs transferred to MONDO:0011274. The historical labels "glass-chapman-hockley syndrome" and the craniosynostosis-dysmorphism-brachydactyly synonyms, plus the Orphanet:1535 / SCTID:720814001 legacy xrefs, are simply lost — exactly the data-loss objection @sabrinatoro raised against #10087. A `replaced_by` with no synonym/xref transfer leaves no lexical bridge from the historical labels to Muenke.
- **Under-editing:** the agent reproduced the *abandoned* human approach, not the *approved* one. Despite the high F1, this would require the same curator correction that #10087 received.
- The high F1 ranking is misleading: #100/#165/#375 did substantially more correct work (the full merge) yet score lower because their (correct) Muenke additions diverge from gold's incidental cleanups. Judge substance, not F1: this attempt is materially less complete than those.

Net: partial success — clean obsoletion but the merge half is missing, reproducing a repudiated pattern.
