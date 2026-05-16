---
ontology: mondo
issue_number: 9795
pr_number: 10110
eval_repo_pr: 296
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.392
precision: 0.488
recall: 0.328
jaccard: 0.244
outcome: partial_success
failure_modes: [wrong_pattern, missed_requirement]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: [10107, 10108, 10109]
scoring_caveat: "Gold PR #10110 covers only the Usher 1J sub-step of a four-merge issue resolved across #10107/#10108/#10109/#10110. Recall floored for every attempt; F1 under-represents scope coverage — but for this attempt the low precision reflects real pattern errors, not just the harness."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Poor evaluation case (multi-PR partial gold), but unlike the codex/opencode/opus runs this attempt also has genuine quality problems. haiku-4.5 obsoleted all four requested terms with correct `replaced_by` targets, but it did **not** perform the merge correctly: it left the obsoleted terms' synonyms and xrefs on the obsolete stanzas (only flipping `MONDO:equivalentTo`→`MONDO:equivalentObsolete`) and transferred **nothing** to the surviving terms. The result is an incomplete "merge" — the surviving terms (MONDO:0007402, MONDO:0044720, MONDO:0010549, MONDO:0012273) gain none of the merged concept's metadata. F1=0.392 partly reflects the partial-gold harness, but the low precision=0.488 reflects real pattern divergence from how MONDO does term merges.

## Strengths

- Correctly identified all four merge pairs and applied `is_obsolete: true` + `replaced_by:` + `IAO:0000231 MONDO:TermsMerged` + the issue link, with the `obsolete ...` name prefix.
- Removed logical axioms (`is_a`, `relationship`) and the `obsoletion_candidate` subset / scheduled-obsoletion date from the obsoleted stanzas.

## Issues

- **Wrong merge pattern (core defect)**: a MONDO "TermsMerged" obsoletion is supposed to transfer the merged concept's synonyms/xrefs/subsets onto the *surviving* term so external mappings are preserved. This attempt instead retained synonyms and xrefs on the *obsolete* stanza and made no edits to any surviving term. After this change, e.g. MONDO:0007402 still lacks the `cramps, familial adolescent` synonym and the OMIM:218050/MEDGEN:347475/UMLS:C1857533 xrefs that the human (#10107) moved onto it. This loses the merge's entire point.
- Indiscriminately rewrote almost every xref source on the obsolete stanzas to `MONDO:equivalentObsolete` (DOID, MEDGEN, MESH, Orphanet, SCTID, UMLS) — over-broad and not how the human handled these.
- Did not reproduce any of the human's MONDO:0012273-specific edits (`MONDO:preferredExternal`, NARROW-synonym deletions, transferred OMIM-evidenced synonyms).
- Did not engage the syndromic-vs-nonsyndromic judgment that defines the case difficulty (no curator-review note, no parent reasoning) because it never touched the survivors.
