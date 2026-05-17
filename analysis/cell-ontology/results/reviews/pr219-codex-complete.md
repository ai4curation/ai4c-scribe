---
outcome: success
failure_modes: []
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

This attempt removes the imported `oboInOwl` annotation-property labels and adds an automated SPARQL validation check to keep them from being reintroduced. It covers the immediate issue and follows CL's existing style of `*-violation.sparql` checks, although the query is less general than the other SPARQL attempts because it hardcodes a property list.

The accepted PR used a narrower grep target in `cl.Makefile`, so the raw score understates the quality of this approach. The solution is broader than gold but still aligned with the issue.

## Strengths

- Removes the current imported `oboInOwl` label assertions.
- Adds an automated regression check.
- Includes enough context in the SPARQL file to explain the purpose of the check.
- Avoids unrelated ontology edits.

## Issues

- Uses a hardcoded list of imported properties, so future `oboInOwl` properties could be missed unless the list is maintained.
- Wires the check through `src/ontology/Makefile` instead of the accepted `cl.Makefile`.
- Removes a broader set of labels than the accepted PR.
