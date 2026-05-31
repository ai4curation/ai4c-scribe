---
ontology: mondo
issue_number: 9798
pr_number: 10106
eval_repo_pr: 335
agent: std_copilot_son45
model: claude-sonnet-4.5
runtime: copilot
agent_config_tag: v3
case_type: obsoletion
difficulty: medium
f1: 0.561
precision: 0.457
recall: 0.727
jaccard: 0.390
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
outcome: failure
failure_modes: [wrong_pattern, under_editing, missed_requirement, syntax_error]
---

## Summary

A well-researched but mechanically wrong obsoletion. The PR comment is the most thorough in the set (it correctly traces the Glass et al. 1994 family to the FGFR3 P250R mutation of Muenke syndrome), but the actual edit is a plain **obsoletion in place** with no content transferred to MONDO:0011274 — reproducing the obsolete-only pattern reviewer @sabrinatoro **repudiated** in the curator's first attempt #10087. It uses the generic `OMO:0001000` reason instead of `MONDO:TermsMerged`, fabricates the invalid `MONDO:obsoleteEquivalent` qualifier, drops a real provenance source from the Orphanet xref, and rewrote the def with possibly inaccurate citations. F1=0.561. Failure.

## Strengths

- Genuinely strong literature methodology in the PR narrative: identified PMC5051481 and the FGFR3 P250R linkage and articulated a coherent obsoletion rationale.
- Correctly set `is_obsolete: true` and `replaced_by: MONDO:0011274`.
- Removed `subset: obsoletion_candidate`, all `is_a` axioms, and the scheduled-obsoletion date — appropriate for an obsoleted class.

## Issues

- **Wrong pattern (decisive):** obsoletion, not merge. Nothing transferred to Muenke MONDO:0011274; the historical synonyms/xrefs are stranded on the obsolete term. This is exactly the approach @sabrinatoro rejected in #10087, requiring a full merge instead.
- **Wrong obsoletion reason:** `IAO:0000231 OMO:0001000` instead of gold's merge-specific `MONDO:TermsMerged`.
- **Fabricated qualifier:** `xref: Orphanet:1535 {source="MONDO:obsoleteEquivalent"}` — invalid token (correct: `MONDO:equivalentObsolete`); the agent additionally **dropped the real `source="GARD:0002479"` provenance** that gold preserves on this xref.
- **Definition rewrite with shaky citations:** replaced the GARD-sourced def with a new one citing `[PMC:PMC5051481, PMID:7981856]`; the PR comment's own reference list mislabels PMC5051481 as a *cleidocranial dysplasia / RUNX2* paper, indicating the cited support is not reliably tied to the new def text. Gold simply removes the def in the merge — a cleaner outcome.
- **Citation/ORCID confusion:** the PR comment claims ORCID `0000-0001-5208-3432` while the diff writes `0000-0001-5208-3432` as a `dc:creator` on the obsolete stanza (gold adds no such property); an unrelated `0000-0002-4142-7153` appears in the surrounding Muenke context. Adds noise to an already out-of-scope edit.

Net: failure — strong prose, wrong mechanics; reproduces the repudiated #10087 obsolete-only pattern with an invalid qualifier and lost provenance.
