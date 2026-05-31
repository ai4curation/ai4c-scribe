---
outcome: failure
failure_modes:
  - over_editing
  - scope_creep
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This attempt removes the intended six redundant `oboInOwl` synonym/xref labels,
but it substantially over-deletes beyond the issue. In addition to the extra
labels removed by PRs #145 and #202, it also strips labels from the UBERON
synonym-type annotation properties `HUMAN_PREFERRED`, `LATIN`, and `PLURAL`.

That makes the result worse than a merely incomplete gold match. It applies the
wrong rule to the annotation-property block and removes labels that are not the
redundant imported labels targeted by the human PR.

## Strengths

The six gold-targeted redundant labels are included in the deletion set, so the
attempt did identify the central issue.

The edit is still localized to the annotation-property area of `cl-edit.owl` and
does not add unrelated ontology axioms.

## Issues

The deletion set is too broad. It removes `obo:IAO_0000028`,
`oboInOwl:SubsetProperty`, `oboInOwl:consider`, `oboInOwl:inSubset`,
`rdfs:seeAlso`, and the UBERON synonym-type labels, none of which are part of
the human PR's six-property cleanup.

The attempt also leaves local structure untidy by removing label assertions
without removing all matching comment blocks. That is exactly the kind of
annotation-property drift the issue was meant to reduce.

Because it deletes real local labels, this is a failure despite including the
correct six removals.
