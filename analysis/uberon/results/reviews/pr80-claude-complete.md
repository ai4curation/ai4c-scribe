---
ontology: uberon
issue_number: 3473
pr_number: 3494
eval_repo_pr: 80
agent: std_codex_g54
model: gpt-5.4
runtime: codex
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.182
precision: 0.105
recall: 0.667
jaccard: 0.100
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_has_out_of_scope_extra_edits
companion_prs: []
scoring_caveat: "metadiff vs #3494 is dominated by ~11 lines of issue-irrelevant churn (CL label-comment refreshes CL:1000271/CL:0002145/CL:0002332/CL:1000223/CL:0000150, synonym reorder in UBERON:0003532) from a master-merge + ROBOT reserialization, plus reasoner-driven endocardium/synovial is_a deletions negotiated only in the PR comment thread. The genuine in-scope content is ~4 has_part→composed_primarily_of swaps; this attempt reproduces 3 of them. F1=0.182 severely under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The strongest attempt in the cohort on the substantive ontology axioms: the agent correctly swapped `has_part CL:0000076` → `composed_primarily_of CL:0000076` on all three core squamous classes — `squamous epithelium` (UBERON:0006914), `simple squamous epithelium` (UBERON:0000487), and `stratified squamous epithelium` (UBERON:0006915) — exactly matching the three corresponding gold edits. Recall is 0.667 only because the gold PR additionally swept up out-of-scope CL-label churn, serialization noise, and reasoner-driven endocardium/synovial cleanup the issue never asked for. The F1 of 0.182 badly **under-represents** the quality; on the issue's actual intent this is essentially a complete and correct solution.

## Strengths

- Correctly fixed all three squamous-branch terms (UBERON:0006914, UBERON:0000487, UBERON:0006915) with the right relation `composed_primarily_of` (RO:0002473) — the full set of squamous logical-definition repairs the issue intended, more complete than the Opus (#238, 2 terms) and gemma (#110, 1 term) attempts.
- Used the prescribed `obo-checkout.pl`/`obo-checkin.pl` workflow and reserialized with `robot convert`, then ran a non-destructive `robot convert` syntax check — exactly the methodology the agent config (CLAUDE.md) prescribes.
- Explicitly trimmed incidental label/serialization churn from the reserialization step so the final diff stayed scoped — the correct discipline, and notably the *opposite* of what produced gold's noise.
- Sound rationale in the PR comment: notes the old pattern was satisfiable by "even a small number of squamous epithelial cells" and that `composed_primarily_of` is an established Uberon composition relation.

## Issues

- Added `property_value: term_tracker_item "https://github.com/obophenotype/uberon/issues/3473" xsd:anyURI` to all three terms. Gold did not add these. This is a defensible provenance convention (and harmless), but it is extra relative to gold and contributes nothing the issue requested; it slightly lowers precision against gold. Not an error.
- Final hunk removes a single trailing blank line at EOF (`vessel_supplies_blood_to` typedef region) — a benign serialization side-effect, not a semantic change.
- Did not fix `short descending thin limb` (UBERON:0005099), the one other `has_part CL:0000076` site gold aligned. Minor completeness gap; the issue did not name it and it requires noticing the downstream `has_part` usage.
- Did not (and could not, from the issue alone) reproduce the reasoner-driven endocardium/synovial `is_a` removals negotiated in the PR thread — not chargeable.
