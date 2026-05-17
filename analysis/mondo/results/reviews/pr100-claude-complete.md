---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 100
agent: std_codex_g55
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
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

This is the strongest substantive attempt in the set. The agent correctly recognized that issue #9798 required a full term **merge** (not a bare obsoletion) and executed the canonical Mondo `merge-terms` SOP: it reduced MONDO:0023243 to a clean obsolete stanza (`name: obsolete ...`, `IAO:0000231 MONDO:TermsMerged`, issue link, `is_obsolete: true`, `replaced_by: MONDO:0011274`) **and** transferred the historical synonyms plus both legacy xrefs onto the surviving Muenke syndrome term MONDO:0011274. This matches the curator's reviewer-approved approach (gold #10106) and avoids the obsolete-only pattern that reviewer @sabrinatoro repudiated in the curator's first attempt #10087. F1=0.765 under-represents the quality here: the missed lines are gold's *incidental, issue-unrelated* Muenke cleanups, not the merge itself.

## Strengths

- Correctly inferred the merge intent from issue context (SNOMED retirement, Orphanet 1535→Muenke equivalence, PMID:20108486) — the same judgment the curator and reviewer ultimately required.
- Obsolete stanza is exactly correct: uses the merge-specific `IAO:0000231 MONDO:TermsMerged` (not the generic `OMO:0001000` that four lower-tier attempts wrongly used), keeps `replaced_by: MONDO:0011274`, and strips def/comment/subsets/is_a/scheduled-obsoletion-date — byte-identical to gold's obsolete hunk.
- Transferred `xref: Orphanet:1535 {source="GARD:0002479", source="MONDO:equivalentObsolete"}` with the correct `MONDO:equivalentObsolete` qualifier (not the fabricated `MONDO:obsoleteEquivalent`).
- Also transferred `xref: SCTID:720814001 {source="MONDO:equivalentObsolete"}` matching gold exactly — gold deliberately retains the retired SNOMED concept as an obsolete-equivalent record.
- Transferred all four craniosynostosis synonyms and added the issue-tracker `IAO:0000233` link to Muenke.

## Issues

- **Scope/over-editing (minor):** added `synonym: "glass chapman hockley syndrome" RELATED [...]` (the owltools-injected unspaced variant) to Muenke; gold drops this artefact and keeps only the hyphenated `glass-chapman-hockley syndrome`. The agent also keeps `synonym: "Muenke nonsyndromic coronal craniosynostosis" RELATED [MEDGEN:355217]` (adding an evidence code) whereas gold *deletes* that synonym — an incidental gold cleanup the agent had no way to know about from the issue.
- **Synonym scope/evidence differences (defensible, not errors):** kept transferred synonyms at `RELATED` and cited `[GARD:0002479, PMID:20108486]`; gold promotes them to `EXACT` and cites `[GARD:0002479]` / `[Orphanet:1535]`. Both are reasonable curatorial choices; gold's scope promotion is not derivable from the issue.
- **Missed incidental gold edits (not the agent's fault):** did not reproduce gold's issue-unrelated `subset: inferred_rare` addition or the `MNKES` RELATED→EXACT ABBREVIATION change on Muenke. These cap F1 below 1.0 for any well-scoped agent and should not count against this attempt.

Net: a correct, mergeable full-merge solution. The metadiff under-represents quality; treat as success.
