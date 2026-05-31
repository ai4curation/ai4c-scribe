---
outcome: partial_success
failure_modes:
  - wrong_pattern
reviewed_by: codex
reviewed_at: "2026-05-16"
---

## Summary

The attempt fixed the two most visible taxonomy assertions by changing neurula
and pharyngula from Eumetazoa to Chordata, and it scoped the late embryonic
stage's pharyngula predecessor with a GCI annotation. It also added issue-source
annotations and tracker metadata.

The substantive weakness is the GCI relation choice. The accepted repair keeps
the predecessor relation and adds a Chordata taxon scope; this attempt uses
`in_taxon` as the GCI relation. That is close to the requested biological
constraint but not the same ontology pattern, so the result is only a partial
match.

## Strengths

- Correct target terms and correct direct taxon replacement for neurula and
  pharyngula.
- Recognizes that late embryonic stage should not globally be preceded by a
  pharyngula stage without taxon scoping.
- Adds provenance pointing back to the GitHub issue.

## Issues

- Uses the wrong GCI pattern for the scoped predecessor axiom:
  `gci_relation="in_taxon"` rather than the accepted taxon-scoped relation form.
- Omits the accepted definition wording that narrows neurula and pharyngula to
  chordate developmental stages.
