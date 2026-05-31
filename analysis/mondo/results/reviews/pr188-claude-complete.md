---
ontology: mondo
issue_number: 9799
pr_number: 10114
eval_repo_pr: 188
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.519
precision: 0.538
recall: 0.5
jaccard: 0.35
outcome: partial_success
failure_modes: [wrong_pattern, over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

claude-haiku-4.5/claude got the relabel and the two xrefs right but mishandled synonym scope: it converted **all** synonyms (including the previously RELATED GARD synonyms) to `RELATED [OMIM:612541]` and introduced a new synonym, mis-attributing every one to OMIM. F1=0.519 (P=0.538, R=0.500). The score is approximately fair — the synonym-scope error and source rewrites are genuine quality problems, not metadiff artifacts.

## Strengths

- Correct relabel to `name: Dursun syndrome`.
- Added `xref: OMIM:612541 {source="MONDO:includedEntryInOMIM"}` and `xref: Orphanet:178503 {source="MONDO:equivalentObsolete"}` correctly per the issue specification.
- Removed the obsoletion `comment:`, `subset: obsoletion_candidate`, and `IAO:0006012` date.
- Kept `is_a: MONDO:0002254 ! syndromic disease` — correctly avoided the unsupported reparenting that pr443/pr134/pr115 made.

## Issues

- Wrong pattern (synonym scope): the gold kept the old descriptive label as an **EXACT** synonym (it is an exact synonym of Dursun syndrome per MeeSiing's analysis). This attempt instead set `synonym: "familial pulmonary arterial hypertension leucopenia and atrial septal defect" RELATED [OMIM:612541]` — RELATED is wrong here; the issue thread explicitly states the old label "is an exact synonym to Dursun syndrome".
- Source rewriting / over-editing: the two pre-existing GARD-sourced RELATED synonyms (`"familial PAH, leucopenia and ASD"` and `"familial pulmonary arterial hypertension, leucopenia and ASD"`) had their `[GARD:0010455]` provenance overwritten with `[OMIM:612541]`, and a new `"pulmonary arterial hypertension, leukopenia, and atrial septal defect" RELATED [OMIM:612541]` was added. Destroying existing GARD provenance is incorrect; OMIM did not supply those strings.
- Empty PR comment ("# PR Changes Summary" only) — no documented research or validation; weakest methodology transparency of the cohort.
- Omission: no `def:`, no G6PC3 logical definition. Removed the GARD `seeAlso` gold retained.
