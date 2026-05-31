---
ontology: uberon
issue_number: 3629
pr_number: 3630
eval_repo_pr: 675
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: medium
f1: 0.769
precision: 0.909
recall: 0.667
jaccard: 0.625
outcome: success
failure_modes: []
case_quality: ok
case_quality_reason: gold_verbatim_issue_text_with_metadiff_scoring_artifacts
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent added `UBERON:9900000 carotid artery intima-media region` with the canonical ID and both gold hunks — including the reciprocal `disjoint_from: UBERON:9900000` on the `UBERON:0005734` stanza. Substantively this is complete and correct. The F1=0.769 (P=0.909, R=0.667) **under-represents** the quality: the recall gap is driven almost entirely by the agent additionally encoding the differentia as an equivalence (`intersection_of`), which is exactly the pre-curation form the curator (aleixpuigb) overrode by preference in commit "Remove equivalentTo" — a curator style override, not an agent error (METADATA caveat #4).

## Strengths

- Canonical ID `UBERON:9900000` matches gold (not the `9900001` placeholder).
- Both gold hunks present: the new-term stanza and the reciprocal `disjoint_from: UBERON:9900000 ! carotid artery intima-media region` line inside the `UBERON:0005734` ("tunica adventitia of blood vessel") stanza — the correct OWL serialization side that most attempts missed. This drives the high precision (0.909).
- Correct genus and issue-specified differentia: `is_a: UBERON:0000481`, `relationship: has_part UBERON:0002522` (tunica media), `relationship: has_part UBERON:0002523` (tunica intima), `relationship: part_of UBERON:0005396` (carotid artery segment) — all asserted alongside the logical definition.
- The `intersection_of` block is itself well-formed and anatomically faithful (`UBERON:0000481` genus + `part_of UBERON:0005396` + `has_part UBERON:0002522/0002523`) — arguably a stronger defined-class modeling than the curator's primitive final form.
- Full provenance: `dc-contributor` ORCID with ` ! Aleix Puig-Barbé` label, `dcterms-date`, `term_tracker_item` (`xsd:anyURI`), `created_by: dragon-ai-agent`. Methodology section documents PMID verification and a `robot convert` reserialization.

## Issues

- **Curator-overridden `intersection_of` (scoring only, not an error):** the agent added an equivalence axiom that the curator later refactored away to a primitive `is_a` + `relationship:` form. Reproducing the pre-curation shape is a defensible, arguably superior modeling choice; it lowers recall vs the post-curation gold but is not a substantive defect.
- **Spurious extra def xref:** the definition carries `[DOI:10.3389/fcvm.2024.1478600, PMID:39416432]` where the issue/gold specify only `[PMID:39416432]`. The DOI resolves to the same publication as the PMID, so this is redundant rather than wrong, but it is an unrequested addition that lowers precision slightly.
- Identical blob (`97b7311`) to eval PR #615 — consistent gpt-5.4/opencode behavior on this case.

Net: substantively complete and correct with canonical ID and both gold hunks; the F1 materially under-represents quality, with the only real divergences being a curator-overridden equivalence axiom and a redundant DOI xref.
