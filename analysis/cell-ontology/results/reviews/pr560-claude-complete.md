---
ontology: cell-ontology
issue_number: 3584
pr_number: 3585
eval_repo_pr: 560
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3:.
case_type: new_term
difficulty: hard
f1: 0.639
precision: 0.639
recall: 0.639
jaccard: 0.469
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: gold_renegotiated_plus_placeholder_vs_canonical_cl_id_artifact
companion_prs: []
scoring_caveat: "Byte-identical diff to pr495 (blob 417596b, gpt-5.5/opencode). Canonical CL_9900001–CL_9900014 numbering matches gold's ID assignment so it scores F1=0.639, far above the ontologically-equivalent off-by-one attempts (pr195/pr214 ~0.26). Remaining gap is metadiff-blind provenance (term_tracker_item → #3584 vs gold #3471, differing terms:date) plus gold's review-only/out-of-scope edits the issue never specified. Judge against the issue spec, not line-level metadiff vs #3585."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: 2026-05-16
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

This is a re-run of the gpt-5.5/opencode configuration and produces a diff byte-identical to pr495 (blob 417596b): all 14 myenteric-neuron terms from issue #3584, on the canonical CL_9900001–CL_9900014 scheme that aligns with gold's numbering. F1=0.639 (highest of the gpt-5.x set) under-represents quality — the residual gap is provenance/synonym-convention noise plus gold's own renegotiated and out-of-scope edits. The accompanying PR comment documents a sound methodology including ROBOT convert + ELK satisfiability validation. Outcome graded `success` on substance (case is `poor`, see METADATA).

## Strengths

- **All 14 terms present and ID-aligned to gold** (CL_9900001 generic Dogiel II … CL_9900014 nitrergic), avoiding the off-by-one metadiff collapse that hit pr195/pr214.
- Definitions, PMID xrefs, parentage, and the two defined grouping classes (`EquivalentClasses` with `RO_0002215 some GO_0014055` / `GO_0006809`) follow the issue spec accurately, identical to pr495 (see that review for the per-term detail).
- **Documented, defensible methodology:** the PR comment explicitly records (a) running `robot reason --reasoner ELK` for satisfiability and `robot convert` for syntax, (b) the deliberate decision *not* to make "interneuron of myenteric plexus" a `SubClassOf CL_0000099` because that class is CNS-constrained (`part_of some UBERON_0001017`) and would make the enteric branch unsatisfiable under ELK — a correct, well-reasoned ontological judgment, and a more rigorous handling than blindly following the issue's requested CL_0000099 parent.
- Correctly deferred the calretinin protein-expression axiom (issue flagged it as needing a PRO import decision) rather than inventing an unresolved term — good scope discipline.
- Added the intestinofugal axon-target union restriction (`RO_0013007` over UBERON_0002262/0005479/0005480) faithfully encoding the issue's Term 4 axon-target list.
- `IAO_0000233` term_tracker_item present on every term (provenance instruction satisfied; pr143 missed this).

## Issues

- **Provenance divergence (metadiff-penalized, not a defect):** term_tracker_item → `issues/3584` vs gold's `issues/3471`; `terms:date` is run date not 2026-03-10. No ontological consequence.
- **Synonym scope/typing differs from gold:** abbreviations demoted to plain `hasRelatedSynonym` without the `OMO_0003000` synonym-type tag gold uses; a few exact/related assignments differ. Valid but house-convention misses, metadiff-visible.
- **Ontology risk inherited from the issue:** spiny Dogiel I (CL_9900009) keeps `SubClassOf CL_0008015` per Term 8; gold curators removed the analogous axiom in review for unsatisfiability. A real latent caveat, but faithful to the issue and not an agent fault. Note the agent *did* proactively guard the interneuron branch but not this one — inconsistent satisfiability hygiene, though both follow the literal issue text.
- **Label casing:** "dogiel type II neuron" lowercase vs gold's "Dogiel type II neuron". Cosmetic, metadiff-visible.
- Gold's out-of-scope edits (pre-existing `CL_4033160`; unrequested `BFO_0000050 some UBERON_0002005` on generic Dogiel II) are gold-side over-edits the agent correctly avoided; they depress apparent recall through no fault of the agent.
