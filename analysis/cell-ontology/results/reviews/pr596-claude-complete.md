---
ontology: cell-ontology
issue_number: 3590
pr_number: 3591
eval_repo_pr: 596
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: other
difficulty: simple
f1: 0.000
precision: 0.000
recall: 0.000
jaccard: 0.000
outcome: partial_success
failure_modes:
  - wrong_term
  - over_editing
case_quality: poor
case_quality_reason: gold_renegotiated_in_pr_comments
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent built a complete, well-formed subset property — `Declaration` correctly ordered after `cl:BDS_subset`, header comment, `terms:date`, `rdfs:comment`, `rdfs:label`, an issue provenance link, and the defining `SubAnnotationPropertyOf(cl:add_by_HRA oboInOwl:SubsetProperty)`. Its only substantive defect is the typo'd name `add_by_HRA` taken verbatim from the issue (human silently corrected to `added_by_HRA`). This is the best-implemented of the five gpt attempts on this case; metadiff F1=0.000 is driven entirely by the name-token mismatch plus the unobservable post-submission comment renegotiation, so F1 badly under-represents quality (`poor`-flagged case).

## Strengths

- Correct subset-tag mechanism: valid `Declaration` plus `SubAnnotationPropertyOf(... oboInOwl:SubsetProperty)` — the canonical CL pattern (`cl:BDS_subset`, `cl:added_for_HCA`).
- Declaration correctly ordered: placed after `cl:BDS_subset` and before `cl:added_for_HCA`, exactly matching the gold's alphabetical position — the only one of these five attempts to get declaration ordering right (pr558/pr498/pr286 all mis-ordered it).
- Self-documenting and provenance-aware: added an accurate `rdfs:comment` plus `AnnotationAssertion(obo:IAO_0000233 cl:add_by_HRA <.../issues/3590>)` tying the property to its originating issue — defensible, arguably good provenance practice.
- Sound methodology: validated with `robot convert`, reviewed the diff, and explicitly reasoned that no term assignments were requested (the issue's spreadsheet follow-up is a separate future task) — correctly scoped the change.

## Issues

- Wrong name token (root cause of F1=0): used `cl:add_by_HRA` verbatim from the typo'd issue text instead of normalizing to `added_by_HRA` per the in-repo `added_for_HCA` convention. This is the single defect separating it from a high-quality solution.
- Scope (over_editing): extra `rdfs:label`, `terms:date` (fabricated `2026-05-17` timestamp), and `IAO_0000233` assertions that the gold does not include — gold deliberately adds no `rdfs:label` per CL subset-property convention. The provenance link is the most defensible of these extras.
- Comment wording differs from the merged text, which was dictated by reviewer @dosumis post-submission and is unknowable a priori (see Curation Note).
- Net: F1=0.000 severely under-represents quality. Mechanism, ordering, and scoping reasoning are all correct; only the typo-driven identifier token is wrong. Graded `partial_success` (a near-success gated solely by an unobservable typo correction).
