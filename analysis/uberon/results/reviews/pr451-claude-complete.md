---
ontology: uberon
issue_number: 3471
pr_number: 3472
eval_repo_pr: 451
agent: std_opencode_kimi26
model: togetherai/moonshotai/Kimi-K2.6
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: simple
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: success
failure_modes: [scope_creep]
case_quality: poor
case_quality_reason: gold_pr_is_partial
companion_prs: []
scoring_caveat: "Gold PR #3472 only added the def line and never removed the redundant `part_of UBERON:0002021 ! occipital lobe` axiom that issue #3471 explicitly asked to be removed (still present in upstream master 2026-05). This attempt added the def with the issue's verbatim wording (plus a disclosed grammar fix) AND removed the redundant axiom, so it is MORE complete than gold but is recall-penalized for the removal; the F1=0.000 (vs ~0.667 for the byte-clean cohort) is additionally driven by two extra `property_value` provenance lines. metadiff F1=0.000 strongly under-represents quality."
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

On the substance of issue #3471 this is the strongest of the three attempts and one of the best in the whole cohort: the agent installed the definition using the issue's wording essentially verbatim (with a disclosed, well-justified grammar correction "contribute" → "contributes" for subject-verb agreement with "A functional part"), kept all three issue-supplied xref sources, and correctly removed the redundant `relationship: part_of UBERON:0002021 ! occipital lobe` axiom with an accurate transitivity rationale. The metadiff F1=0.000 badly under-represents quality: it reflects (a) the known partial-gold artifact (gold #3472 never removed the redundant axiom) and (b) two extra `property_value` provenance lines the agent added. The substantive ontology work is correct and complete; the only real fault is provenance scope creep, not curation error.

## Strengths

- **Definition matches the issue's supplied text** including the colour / object-recognition / spatial-awareness content and all three sources (`ISBN:978-0-323-10027-4`, `ISSN:0072-9752`, `WikipediaVersioned:Visual_cortex&oldid=1268682728`). In contrast to #590/#648 it did not paraphrase away the requested content.
- The "contribute" → "contributes" change is a genuine improvement over both the issue text and the gold `def:` (gold preserved the grammatical error), and the agent explicitly disclosed and justified it in the PR comment as a third-person-singular agreement fix.
- Correctly removed `relationship: part_of UBERON:0002021 {source="MA"} ! occipital lobe`. The redundancy is genuine and the agent's stated reasoning is exactly right (UBERON:0022232 `part_of` UBERON:0000411 visual cortex; UBERON:0000411 `part_of` UBERON:0002021 occipital lobe; `part_of` transitivity entails the direct axiom). This is the issue-mandated work gold omitted; the agent even validated the redundancy by inspecting UBERON:0000411.
- Strong methodology disclosure: PR comment documents the checkout/checkin workflow, the redundancy validation against UBERON:0000411, and honestly flags that `robot convert` was unavailable so the file was not reserialized.

## Issues

- **Provenance scope creep.** The agent added `property_value: term_tracker_item https://github.com/obophenotype/uberon/issues/3471 xsd:anyURI` and `property_value: dcterms-date "2026-05-16T00:00:00Z" xsd:dateTime`. Neither is in gold, neither was requested, and the dcterms-date in particular is gratuitous metadata. This is the dominant precision drag and a real (if minor) deviation. The codex review's claim that the `term_tracker_item` URI is "malformed" is overstated — unquoted `xsd:anyURI` term-tracker values are an accepted Uberon convention — but the lines are still unrequested scope creep.
- The agent could not run `robot convert` (disclosed), so the OBO was not reserialized; for this minimal single-stanza edit that is low-risk and the OBO syntax is valid, but it is a deviation from the standard workflow.
- Net: outcome is `success` on substance — both explicit issue asks fully and correctly satisfied, exceeding the partial gold. The F1=0.000 must not be read as failure; the actionable lesson is provenance-metadata restraint, not ontology correctness. `scope_creep` is the only failure mode.
