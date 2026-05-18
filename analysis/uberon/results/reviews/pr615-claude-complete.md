---
ontology: uberon
issue_number: 3629
pr_number: 3630
eval_repo_pr: 615
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

A second gpt-5.4/opencode run producing the byte-identical blob (`97b7311`) to eval PR #675, with the same F1=0.769 (P=0.909, R=0.667). It adds `UBERON:9900000 carotid artery intima-media region` with the canonical ID and both gold hunks (including the reciprocal disjoint on the `UBERON:0005734` stanza). Substantively complete and correct; the recall gap is the curator-overridden `intersection_of` equivalence axiom plus a redundant DOI def xref — F1 **under-represents** quality (METADATA caveat #4).

## Strengths

- Canonical ID `UBERON:9900000` matches gold (not the `9900001` placeholder).
- Both gold hunks present: new-term stanza plus the reciprocal `disjoint_from: UBERON:9900000` line inside the `UBERON:0005734` ("tunica adventitia of blood vessel") stanza — the correct OWL serialization side, driving the 0.909 precision.
- Correct genus + issue-specified asserted differentia: `is_a: UBERON:0000481`, `relationship: has_part UBERON:0002522` (tunica media), `relationship: has_part UBERON:0002523` (tunica intima), `relationship: part_of UBERON:0005396` (carotid artery segment).
- The `intersection_of` block is well-formed and anatomically faithful — a defensible, arguably stronger defined-class model.
- Full provenance: `dc-contributor` ORCID with ` ! Aleix Puig-Barbé` label, `dcterms-date`, `term_tracker_item` (`xsd:anyURI`), `created_by: dragon-ai-agent`.

## Issues

- **Curator-overridden `intersection_of` (scoring only):** the equivalence axiom matches the pre-curation dragon-ai form that the curator refactored away in "Remove equivalentTo". Defensible modeling; lowers recall vs post-curation gold but not a substantive error.
- **Redundant def xref:** `[DOI:10.3389/fcvm.2024.1478600, PMID:39416432]` vs the issue/gold's `[PMID:39416432]` only. Same publication; unrequested but not wrong.
- Identical blob (`97b7311`) to eval PR #675 — reproducible gpt-5.4/opencode behavior on this case.

Net: substantively complete and correct with the canonical ID and both gold hunks; F1 under-represents quality. Graded `success`, consistent with #675.
