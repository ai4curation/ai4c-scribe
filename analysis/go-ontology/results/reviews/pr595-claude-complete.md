---
ontology: go-ontology
issue_number: 31636
pr_number: 31925
eval_repo_pr: 595
agent: std_opencode_g54
model: gpt-5.4
runtime: opencode
agent_config_tag: v9
case_type: synonym_update
difficulty: simple
f1: 0.857
precision: 0.857
recall: 0.857
jaccard: 0.75
outcome: partial_success
failure_modes:
  - scope_creep
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent fully resolved issue #31636: renamed GO:1990334 from `Bfa1-Bub2 complex`
to `SIN/MEN two-component GAP complex`, added both requested NARROW synonyms
(`Bfa1-Bub2 complex`, `Byr4-Cdc16 GAP complex`), rewrote the definition as
species-agnostic, and added the `term_tracker_item` property value. Every
structural edit matches the gold PR #31925 exactly; the only divergence from
gold is the definition line. The metadiff F1 of 0.857 **under-represents**
quality — it reflects a single free-text definition line plus a minor
definition-xref change, not a substantive error.

## Strengths

- Exact match with the human PR on the label change, both NARROW synonyms in
  the order/scope the curator requested in the issue, the `is_a GO:1902773`
  parentage, the `part_of GO:0005816` relationship, and the
  `term_tracker_item` URL for issue #31636.
- Definition is genuinely species-agnostic as requested: it generalizes the
  GAP function across the septation initiation network (SIN, fission yeast)
  and mitotic exit network (MEN, budding yeast), while still anchoring the
  concrete Bub2-Bfa1 / Tem1 mechanism in budding yeast — closely tracking the
  human curator's own framing in the issue and PR comment.
- Tightly scoped to the single term and single file (`src/ontology/go-edit.obo`);
  no collateral edits to other terms or unrelated metadata.

## Issues

- **Scope creep on the definition xref (only divergence from gold).** The gold
  PR retained `[GOC:bhm, PMID:16449187]`. The agent changed the xref to
  `[PMID:16449187, PMID:22525225]`: it dropped the original `GOC:bhm` curator
  attribution and added an unrequested reference. PMID:22525225 (Hergovich &
  Hemmings, "Hippo signalling in the G2/M cell cycle phase: lessons learned
  from the yeast MEN and SIN pathways") is topically defensible for a
  species-agnostic definition spanning MEN/SIN, but it was neither asked for
  in the issue nor present in the gold, and dropping `GOC:bhm` discards
  legitimate provenance for the original definition. This is the source of the
  precision/recall gap and is a minor, easily-correctable deviation rather
  than an ontological error.
- Definition prose differs stylistically from the human's wording, but is
  content-equivalent and faithfully species-agnostic; the resulting 1-line F1
  gap is largely a free-text comparison artifact.

No syntax, parentage, synonym-scope, or term-identity errors. The case is a
clean single-gold reference (METADATA `case_quality: good`); the F1 score
modestly under-represents the substantive quality of this attempt.
