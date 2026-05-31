---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 173
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.64
precision: 0.667
recall: 0.615
jaccard: 0.471
outcome: success
failure_modes: [under_editing]
case_quality: poor
case_quality_reason: gold_id_range_unmatchable
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.4/codex produced a high-quality, correctly-modeled new term for STARI that is substantively equivalent to (and arguably better-cited than) the gold PR #10126. It is the best of the nine attempts (F1 0.64). The metadiff **substantially under-represents** quality: the dominant penalty is that the gold curator assigned `MONDO:1010205` while the agent followed its explicit config instruction ("New terms start MONDO:777xxxx") and used `MONDO:7770018`, forcing a different `id:` line and a different file-insertion locus (anchored near `MONDO:7770011`/`infectious discitis` vs. the gold's anchor near `MONDO:1010206`). No agent could have matched this ID by construction.

## Strengths

- Correct parent `is_a: MONDO:0025294` (tick-borne infectious disease), exactly as requested in the issue.
- Included the `relationship: transmitted_by NCBITaxon:6943 ! Amblyomma americanum` axiom — this is in the gold and is the single most discriminating modeling element; only 5 of 9 attempts captured it.
- Correctly used the `SCTID:` prefix for SNOMED (issue wrote `SNOMED:444100007`), matching the Mondo repo convention; both xrefs correctly qualified `{source="MONDO:equivalentTo"}`.
- Both requested synonyms present with correct scopes: `"Masters disease" EXACT`, `"STARI" EXACT ABBREVIATION`.
- Strong, defensible methodology documented in the PR comment: confirmed parent exists, duplicate-checked label/synonyms, ran `robot convert` syntax validation and `make NORM`. Honestly flagged that it could not verify `PMID:40267428` and conservatively excluded it — a reasonable, transparent judgment call (the gold did retain it, so this is a minor under-edit).
- Correct provenance scaffolding: `dcterms:creator` ORCID and `IAO:0000233` term_tracker_item pointing at issue 9873.

## Issues

- **Omission (minor)**: dropped `PMID:40267428` from the definition reference list out of an inability to verify it; the gold retained all three PMIDs. Conservative but slightly incomplete.
- **Style/extra**: added `subset: ncit {source="NCIT:C128427"}`, which the gold did not include. This is defensible (Mondo does use the `ncit` subset for NCIT-sourced terms) but is an extra not in the issue or gold, costing precision.
- **Definition wording** differs from the curator's final rewrite ("...transmitted by the lone star tick... erythema migrans–like rash with or without mild constitutional symptoms"). The agent's wording is scientifically accurate; the curator's exact phrasing only emerged through a CHANGES_REQUESTED review round the agent had no access to. Not a quality defect.
- **Creator ORCID**: agent used the submitter ORCID `0000-0001-5705-7831`; the gold used the curator's own ORCID `0000-0002-5002-8648`. This is house convention the agent could not infer from the issue and is metadiff-invisible relative to substance.
- These ID/locus/wording mismatches are why F1 is 0.64 rather than ~1.0; the substantive ontological content is essentially complete and correct.
