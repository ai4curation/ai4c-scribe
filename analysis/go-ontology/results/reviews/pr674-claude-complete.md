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

Eval PR #674 (gpt-5.4 / opencode) against human PR #32040 / issue #31295
(new_term, medium, single_term). The agent created `GO:7770070 p24 cargo
receptor complex` with the correct parent and process relationship, but with a
thin definition, no synonyms, and only 3 of 5 references. Metadiff is F1=0.700
(P=0.583, R=0.875); this slightly under-represents the correct ontological
placement while fairly reflecting the genuine omission of synonyms and the
curator-specified definition text. Outcome: partial_success.

## Strengths

- Created `GO:7770070` with the exact identifier, label `p24 cargo receptor
  complex`, and `namespace: cellular_component` requested in the issue.
- Parent placement is exactly correct: `is_a: GO:0062137 ! cargo receptor
  complex` — the parent the requester (ValWood) explicitly asked for.
- Correctly added `relationship: capable_of_part_of GO:0006888 !
  endoplasmic reticulum to Golgi vesicle-mediated transport`, byte-identical
  to the gold PR and matching the sibling `GO:0061852` precedent the
  dragon-ai-agent itself cited for the anterograde role.
- Included `term_tracker_item`, `created_by`, and `creation_date` metadata.
- PR comment documents a sound methodology: issue/comment review, precedent
  consultation (`GO:0062137`, `GO:0061852`), `RESEARCH.md`/`DESIGN_PATTERNS.md`
  notes, reference validation, and `make travis_build` before and after.
- Correctly declined to add `intersection_of` axioms or an ER-exit-site
  `part_of` location — a defensible scope judgment for a named complex with no
  applicable compositional design pattern.

## Issues

- Omission (synonyms): the gold term carries four synonyms — `p24 complex`
  (EXACT), `Emp24-Erv25 complex`, `p24 family complex`, `TMED complex`
  (RELATED). None were added. The EXACT synonym in particular is high-value
  for annotation lookup.
- Omission (definition substance): the agent's one-line definition ("A
  conserved hetero-oligomeric cargo receptor complex of the early secretory
  pathway that mediates selective cargo export from the endoplasmic reticulum
  in COPII-coated vesicles") drops the curator-supplied specifics that
  ValWood explicitly provided and the gold PR adopted: selective recruitment
  of GPI-anchored proteins, maintenance of early secretory pathway
  organization, and the compositional statement that a functional complex
  contains one member of each of the alpha/beta/gamma/delta subfamilies. This
  is a `missed_requirement`: the issue thread contains an explicit
  curator-dictated definition that was not used.
- Omission (references): only `PMID:32456004, PMID:34647572, PMID:19566487`
  cited; the gold set adds `PMID:26224213` and `PMID:27569046` (the latter
  was named in the original issue body).
- Metadiff interpretation: recall (0.875) > precision (0.583) reflects the
  missing synonym lines, not over-editing. The codex review's `over_editing`
  flag mischaracterizes this; the dominant failure mode is under-editing /
  missed requirement. The placement substance is fully correct.
