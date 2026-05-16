---
ontology: go-ontology
issue_number: 31964
pr_number: 31982
eval_repo_pr: 271
agent: std_opencode_kimi26
model: kimi-k2.6
runtime: opencode
agent_config_tag: v9
case_type: axiom_repair
difficulty: medium
f1: 0.889
precision: 1.0
recall: 0.8
jaccard: 0.8
outcome: partial_success
failure_modes:
  - over_editing
  - instruction_violation
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

kimi-k2.6 / opencode got both core ontology fixes from issue #31964 correct (broadMatch removal on `GO:0052598`, reparent of `GO:0004720` from `GO:0052597` to `GO:0016641`), but mishandled the tracker provenance: instead of *adding* a `term_tracker_item` for #31964, it *overwrote* the pre-existing `#30193` tracker on **both** terms, deleting historical provenance. F1 = 0.889 (P = 1.0, R = 0.8) modestly *under*-represents the problem — the metadiff sees this as a near-miss, but the destructive replacement of an existing axiom is a real error, not just an omission.

## Strengths

- Both substantive edits are correct and match the gold: the redundant `xref: EC:1.4.3.22 {source="skos:broadMatch"}` is removed from `GO:0052598`, and `GO:0004720` is reparented to `GO:0016641` (verified to be the `EC:1.4.3.-` grouping class the issue requested).
- Preserved the orthogonal `is_a: GO:0140096` on `GO:0004720` and the EC systematic synonym / `RHEA:25625` exactMatch on `GO:0052598`.
- PR comment gives a correct biological rationale (lysyl oxidase acts on a protein-bound lysine residue, not a free diamine).

## Issues

- **Destructive edit (over_editing / instruction_violation).** On `GO:0004720` the diff replaces `property_value: term_tracker_item ".../issues/30193"` with `.../issues/31964` (single line changed, not added). On `GO:0052598` it replaces the `#30193` tracker with `#31964`, deleting that line and keeping only `#28199` + the new one. The gold PR and every F1 = 1.0 attempt *added* #31964 while keeping #28199/#30193 intact. The agent destroyed pre-existing issue provenance — a worse failure than simply omitting the tracker (cf. pr208/pr56, which omitted it but deleted nothing).
- This is why precision reads 1.0 (every changed line maps to a human-changed region) while recall is 0.8 (the additive tracker lines the human added are absent). The score therefore *understates* the severity: a curator merging this would silently lose the #30193 audit trail on two terms.
- Did not run full validation (`make travis_build` unavailable in environment); acceptable given tooling limits, but the destructive tracker edit would not have been caught by syntax-only checks anyway.
