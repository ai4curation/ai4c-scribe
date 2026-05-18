---
ontology: uberon
issue_number: 3629
pr_number: 3630
eval_repo_pr: 579
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 1.000
precision: 1.000
recall: 1.000
jaccard: 1.000
outcome: success
failure_modes: []
case_quality: ok
case_quality_reason: gold_verbatim_issue_text_with_metadiff_scoring_artifacts
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

A second gpt-5.5/opencode run that produced the byte-identical blob (`6ba9f78`) to eval PR #639 and scored a perfect F1=1.000 / precision=1.000 / recall=1.000. It reproduces the curated gold for `UBERON:9900000 carotid artery intima-media region` exactly, including the curator-style serialization of the disjointness axiom on the partner stanza. F1 is fully representative; this is a clean, complete success and a good reproducibility signal for the gpt-5.5 runtime on this case.

## Strengths

- Identical to gold: both hunks present — the new-term stanza and the reciprocal `disjoint_from: UBERON:9900000` line inside the `UBERON:0005734` ("tunica adventitia of blood vessel") stanza. This OWL-symmetric serialization side is the discriminator that depressed every lower-scoring attempt; this run got it right.
- Canonical ID `UBERON:9900000` (not the `9900001` placeholder).
- Curator-preferred primitive shape: `is_a: UBERON:0000481` + explicit `relationship: has_part UBERON:0002522 / UBERON:0002523`, `relationship: part_of UBERON:0005396`; no `intersection_of`.
- Definition and synonym verbatim-correct with the single `[PMID:39416432]` xref.
- Complete provenance: `dc-contributor` ORCID with correct ` ! Aleix Puig-Barbé` label, `dcterms-date`, `term_tracker_item` (`xsd:anyURI`), `created_by: dragon-ai-agent`.
- Tightly scoped to `src/ontology/uberon-edit.obo` only.

## Issues

None. Bit-for-bit match with the curated gold, canonical ID, correct disjoint serialization side. Demonstrates that the gpt-5.5/opencode result on this case is stable across runs (#579 == #639).
