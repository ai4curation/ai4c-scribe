---
ontology: mondo
issue_number: 9873
pr_number: 10126
eval_repo_pr: 40
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.4
precision: 0.417
recall: 0.385
jaccard: 0.25
outcome: success
failure_modes: [over_editing]
case_quality: poor
case_quality_reason: gold_id_range_unmatchable
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

gpt-5.5/codex produced a substantively complete and correct STARI term — correct parent, both synonyms, both xrefs with the canonical `SCTID:` prefix, and the `transmitted_by NCBITaxon:6943` vector axiom present in the gold. It scores the lowest F1 (0.40) of the cohort, but this **drastically under-represents** quality: the penalty is driven by the unmatchable `MONDO:1010205` vs `MONDO:7770018` ID/locus (case flagged poor) plus some scope creep (extra `subset: ncit`, NCIT/SCTID stuffed into definition and synonym source lists) that diverges line-wise from the gold without harming the ontology.

## Strengths

- Substantively equivalent to the gold core modeling: correct parent `is_a: MONDO:0025294` (with multi-source annotation matching the gold's annotation style), `transmitted_by NCBITaxon:6943 ! Amblyomma americanum` axiom present with PMID sources, both synonyms with correct scopes, both xrefs qualified `{source="MONDO:equivalentTo"}`.
- Canonical `SCTID:444100007` used in place of the issue's `SNOMED:444100007`.
- Definition accurate and retained all three PMIDs.
- Correct provenance: submitter ORCID creator, `IAO:0000233` term_tracker_item to issue 9873.

## Issues

- **Scope creep (precision-reducing, mostly harmless)**: added `subset: ncit {source="NCIT:C128427"}` (also seen in #173) — defensible since Mondo does use the `ncit` subset, but not in the gold and not requested. Additionally added `NCIT:C128427` into the definition reference bracket and `SCTID:444100007` into both synonym source lists. None of these are erroneous, but they are gratuitous source-stuffing not present in the gold and inflate line divergence (over_editing).
- **No substantive ontological errors.** The disease is correctly modeled.
- **Style**: definition wording differs from the curator's post-review rewrite (unavailable to the agent); not a defect.
- **Methodology note**: the PR comment is a brief bullet list with no documented validation steps (no mention of `robot convert`, `make NORM`, or duplicate-checking) — thinner than the opencode/opus attempts, though the output itself is sound.
- F1 0.40 is overwhelmingly a metadiff artifact (ID range + insertion locus + source-stuffing); on substance this is a success, not the worst attempt despite the lowest score.
