---
outcome: partial_success
failure_modes:
  - wrong_pattern
  - over_editing
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt gets the requested genus change right, but it also removes an
important differentia from the equivalent class. That makes the result a real
partial success rather than a scoring artifact.

The deleted restriction is not redundant CD11b content; it is the
CD8-alpha-negative marker restriction.

## Strengths

The genus is correctly changed from `CL_0000990` to `CL_0002465`, and the edit
stays within the intended class stanza.

The existing asserted `SubClassOf CL_0002465` remains.

## Issues

The attempt removes `ObjectSomeValuesFrom(obo:CL_4030046 obo:PR_000001084)`,
which encodes lack of CD8-alpha. The human PR preserved every differentia and
changed only the genus.

The PR rationale misidentifies the removed axiom as a redundant CD11b marker,
so the extra deletion is both unrequested and semantically wrong.
