---
ontology: go-ontology
issue_number: 31295
pr_number: 32040
eval_repo_pr: 196
agent: std_claude_hai45
model: claude-haiku-4.5
runtime: claude
agent_config_tag: v9
case_type: new_term
difficulty: medium
f1: 0.636
precision: 0.583
recall: 0.7
jaccard: 0.467
outcome: partial_success
failure_modes: [over_editing, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

# Review: Eval PR #196 (claude-haiku-4.5 / claude) — Issue #31295 / Gold PR #32040

## Summary

The agent created `GO:7770070 p24 cargo receptor complex` under `GO:0062137` with
a four-PMID definition and two synonyms. F1 is 0.636. The committed
axiomatization asserts `part_of GO:0070971 ! endoplasmic reticulum exit site`
and **omits** the gold's `capable_of_part_of GO:0006888` process relationship —
so it both over-localizes (ERES partonomy) and under-specifies (no transport
process link). A partial success: ID/name/parent/definition are correct and
biologically sound, but the relationship modeling diverges from the gold and the
sibling precedent on both axes.

## Strengths

- **Correct parent, namespace, metadata**: `is_a: GO:0062137`,
  `cellular_component`, tracker item to #31295, `created_by`, `creation_date`.
- **Accurate, comprehensive definition**: hetero-oligomeric, ERES localization,
  ER↔Golgi cycling, GPI-anchored COPII cargo, plus the retrograde COPI role —
  matching ValWood's issue discussion. Four PMIDs (32456004, 34647572, 27569046,
  19566487).
- **Strong methodology and documentation**: detailed per-PMID relevance notes,
  explicit reasoning about why the parent's logical def is inherited rather than
  re-asserted, and a clear reviewer-notes section. The agent's analysis quality
  exceeds its metadiff score.
- **Added "p24 complex" EXACT synonym** matching gold's primary synonym.

## Issues

- **Over-localized with `part_of GO:0070971 endoplasmic reticulum exit site`**
  (`wrong_pattern` / `over_editing`): the gold author explicitly rejected any
  fixed anatomical `part_of` because the complex cycles through ER, ERGIC, Golgi
  and vesicle membranes. The agent's own definition states the complex "cycles
  between the ER and Golgi," which is internally inconsistent with asserting a
  single ERES partonomy.
- **Missing the gold's process relationship** (omission): no `capable_of_part_of
  GO:0006888 endoplasmic reticulum to Golgi vesicle-mediated transport`. The gold
  and sibling `GO:0061852` both carry a `capable_of_part_of <transport process>`
  axiom; this attempt has neither that nor a substitute process link, leaving the
  term less connected to the transport hierarchy than gold.
- **Synonym differs from gold** (style): "p24-type cargo receptor complex" RELATED
  is non-standard; gold used "Emp24-Erv25 complex"/"p24 family complex"/"TMED
  complex" RELATED.
- Definition wording differs from gold (style). The term is accurate but its
  relationship axiomatization is among the weakest fits to GO convention in the
  cohort (over-localized AND missing the process axiom).
