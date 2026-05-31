---
outcome: partial_success
failure_modes:
  - under_editing
  - missed_requirement
case_quality: ok
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
agent: std_opencode_gpt5.4
---

## Summary

Eval PR #625 (gpt-5.4 / opencode) against human PR #32040 / issue #31295
(new_term, medium, single_term). This attempt's diff is byte-identical to
eval PR #674 (same blob `97be466`, same F1=0.700, P=0.583, R=0.875): it
creates `GO:7770070 p24 cargo receptor complex` with the correct parent and
process relationship but a thin definition, no synonyms, and 3 of 5
references. Metadiff slightly under-represents the correct ontological
placement while fairly reflecting the synonym/definition omissions. Outcome:
partial_success.

## Strengths

- Created `GO:7770070` with the correct identifier, label `p24 cargo receptor
  complex`, and `namespace: cellular_component` as requested.
- Parent placement exactly correct: `is_a: GO:0062137 ! cargo receptor
  complex` — the parent explicitly requested by ValWood in the issue.
- Correctly added `relationship: capable_of_part_of GO:0006888 !
  endoplasmic reticulum to Golgi vesicle-mediated transport`, byte-identical
  to gold and consistent with the `GO:0061852` sibling precedent.
- Included `term_tracker_item`, `created_by`, and `creation_date` metadata,
  matching gold structure.
- Scope discipline is good: no spurious `intersection_of` axioms or
  location assertions; the patch is confined to the single intended term.

## Issues

- Omission (synonyms): none of the four gold synonyms were added — `p24
  complex` (EXACT) and `Emp24-Erv25 complex` / `p24 family complex` / `TMED
  complex` (RELATED). The EXACT synonym is the most impactful loss for
  curation lookup.
- Omission (definition substance): the agent's single-clause definition omits
  the curator-supplied content ValWood dictated and the gold PR adopted:
  selective recruitment of GPI-anchored proteins, maintenance of early
  secretory pathway organization, and the alpha/beta/gamma/delta subfamily
  composition. The issue thread contained an explicit curator-specified
  definition that was not used — a `missed_requirement`.
- Omission (references): cites `PMID:32456004, PMID:34647572, PMID:19566487`
  only; gold adds `PMID:26224213` and `PMID:27569046`.
- Metadiff interpretation: R (0.875) > P (0.583) reflects missing synonym
  lines, i.e. under-editing rather than over-editing. The core ontological
  placement is correct; the gap is definition richness and synonyms.
- Note: identical diff to eval PR #625's sibling run #674 — a reproducibility
  data point (same model/runtime converged to the same output), not an
  independent quality signal.
