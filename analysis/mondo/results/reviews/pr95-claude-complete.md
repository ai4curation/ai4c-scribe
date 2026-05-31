---
ontology: mondo
issue_number: 9799
pr_number: 10114
eval_repo_pr: 95
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.462
precision: 0.462
recall: 0.462
jaccard: 0.3
outcome: partial_success
failure_modes: [over_editing, wrong_term]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5/codex got the core relabel and the OMIM xref right but introduced the lowest-quality enrichments of the cohort: a self-referential `synonym: "Dursun syndrome" EXACT` on the term now *named* Dursun syndrome, a malformed double-`source` qualifier on the Orphanet xref, and a non-standard `MONDO:obsoleteEquivalent` qualifier instead of the issue-specified `MONDO:equivalentObsolete`. F1=0.462 (P=0.462, R=0.462), lowest of the 10. The score is broadly fair; this attempt has genuine pattern/qualifier errors, not just metadiff under-representation.

## Strengths

- Correct relabel to `name: Dursun syndrome`; removed obsoletion `comment:`, `subset: obsoletion_candidate`, and `IAO:0006012`.
- Added `xref: OMIM:612541 {source="MONDO:includedEntryInOMIM"}` correctly per the issue.
- Correctly kept `is_a: MONDO:0002254 ! syndromic disease` and explicitly declined to add a G6PC3 equivalence axiom, reasoning that the issue centered on an OMIM *included* entry rather than asserting a new gene-defined equivalent class — a defensible conservative judgment that avoided pr443/pr134's reparenting error.
- Documented research (OMIM metadata, Orphanet page, PMID:19011569) and ran `robot convert` + `git diff --check`.

## Issues

- Wrong qualifier: `xref: Orphanet:178503 {source="MONDO:obsoleteEquivalent", source="OMIM:612541"}`. The issue explicitly specified `MONDO:equivalentObsolete` (MeeSiing, confirmed by kanems). `MONDO:obsoleteEquivalent` is a fabricated/inverted qualifier name, and the second `source="OMIM:612541"` on the same xref is a malformed/duplicated qualifier (an Orphanet xref should not carry an OMIM source) — a likely syntax/QC problem.
- Wrong term content: added `synonym: "Dursun syndrome" EXACT [OMIM:612541, Orphanet:178503]` — a synonym identical to the new primary label, which Mondo QC flags as a redundant self-synonym. Gold did not do this.
- Over-editing: added several extra EXACT synonyms (`PMID:19011569`/`Orphanet:178503`-sourced) and a bare-PMID definition `[PMID:19011569]`; gold's definition was sourced `[OMIM:612541, PMID:20799326]`. The extra synonyms and the redundant self-synonym lower precision symmetrically with recall.
- Removed the GARD `seeAlso` gold retained. `make NORM` could not run (no Docker; disclosed).
