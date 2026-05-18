---
ontology: go-ontology
issue_number: 31923
pr_number: 31938
eval_repo_pr: 681
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: other
difficulty: simple
case_quality: good
f1: 0.8
precision: 0.667
recall: 1.0
jaccard: 0.667
outcome: partial_success
failure_modes:
- under_editing
- missed_requirement
reviewed_by: claude-opus-4.7
reviewed_at: '2026-05-17'
---

## Summary

The gpt-5.4/opencode run correctly removed the microtubule mechanistic gloss from the GO:0045022 `early endosome to late endosome transport` definition but did not add the `term_tracker_item` for issue #31923 that the human gold PR #31938 added as a second commit. The definition edit is byte-identical to gold; the absent tracker line is the only reason F1 is 0.800 (P=0.667, R=1.000) rather than 1.0, and the score fairly reflects "one of two required changes done." This run's diff is identical to sibling attempts #683 and #597 (same model/runtime). The codex review for this PR labels it `over_editing`, which is incorrect — recall=1.000 confirms the agent's change is a strict subset of gold, i.e. under-editing.

## Strengths

- Definition edit is exactly correct and byte-identical to gold: only the trailing `; transport occurs along microtubules and can be experimentally blocked with microtubule-depolymerizing drugs` clause was removed; leading sentence and `[ISBN:0815316194, PMID:29980602]` xrefs preserved verbatim.
- Clean scope discipline: the `intersection_of` logical-definition block (`GO:0016192`, `has_target_end_location GO:0005770`, `has_target_start_location GO:0005769`, `occurs_in GO:0005737`) and the `endosome maturation` synonym are untouched; no spurious references; no gratuitous existing-term metadata edits. A tight +1/-1 single-file patch.
- Strong, transparent methodology: explicit obo-checkout.pl/obo-checkin.pl workflow, `make travis_build` run pre- and post-edit, and a detailed checklist. The biological rationale (microtubule-dependence is not universal across taxa) precisely matches ValWood's stated reason in the issue.

## Issues

- **Missed requirement / under-editing**: the gold PR also adds `property_value: term_tracker_item "https://github.com/geneontology/go-ontology/issues/31923" xsd:anyURI` next to the existing `#26386` tracker. This attempt omitted it. The v9 config instructs linking the driving issue via `term_tracker_item`, and the curator ValWood explicitly demanded it in the issue thread ("please always add the term tracker url") — a hard curation requirement.
- The PR comment's checklist explicitly ticks "METADATA: no new term metadata needed; existing metadata preserved" — the agent consciously decided no metadata change was required, the same systematic blind spot seen in #339/#240/#203/#181 (all F1=0.800): correct visible textual edit, skipped provenance bookkeeping.
- The checklist also leaves the PR-creation and issue/PR-communication items unchecked, but the harness produced the PR and comments regardless; this is a cosmetic checklist artifact, not a substantive defect.
- No errors and no scope creep; the gap is purely completeness, hence partial_success.
