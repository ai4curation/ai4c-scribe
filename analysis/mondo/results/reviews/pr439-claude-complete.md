---
ontology: mondo
issue_number: 9937
pr_number: 10112
eval_repo_pr: 439
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: new_term
difficulty: medium
f1: 0.609
precision: 0.583
recall: 0.636
jaccard: 0.438
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9937 is a fully-specified ClinGen new-term request: create "KY-related neuromyopathy"
under `MONDO:0100546` (hereditary neuromuscular disease), with a gene-disease logical
definition on `KY` (HGNC:26576), the four cited PMIDs, the ClinGen affiliation URL, and three
existing terms (MONDO:0014922, MONDO:0044648, MONDO:0044647) reclassified as children. It was
resolved by a single human PR (#10112), approved first time — the gold is the complete and only
resolution, so this is a sound evaluation case. This attempt produced an ontologically correct
term and correctly reclassified all three children; the F1 of 0.609 (the best of the nine
attempts) materially **under-represents** its quality because the bulk of the penalty is the
unavoidable new-term-ID mismatch (`MONDO:7770012` vs gold `MONDO:1010194`), which propagates
onto the three child `is_a:` lines, plus free-text provenance and definition-wording
conventions the agent cannot infer.

## Strengths

- Correct genus-differentia axiom: `intersection_of: MONDO:0100546` plus `intersection_of:
  has_material_basis_in_germline_mutation_in http://identifiers.org/hgnc/26576`, exactly the
  gold logical definition and faithful to the `disease_series_by_gene` pattern.
- Correct asserted parent `is_a: MONDO:0100546` and correct gene identifier (KY = HGNC:26576),
  matching the issue's explicit instruction.
- All three requested children reclassified by adding `is_a: MONDO:7770012` while preserving
  their existing parents — matches the human's approach and the issue request precisely.
- Definition follows the requested template ("Any ... in which the cause of the disease is a
  mutation in the KY gene") with all four PMIDs (27484770, 27485408, 28488683, 32818658) and
  the ClinGen affiliation URL as sources.
- Included `IAO:0000233` issue tracker link to #9937 and a `dc:creator` ORCID — both present
  in gold.
- Clean, tightly scoped diff: only the new term plus the three child edges, no gratuitous
  changes elsewhere.

## Issues

- New-term ID `MONDO:7770012` differs from gold `MONDO:1010194`. This is unavoidable (the
  agent cannot know which ID the human will mint) but it is the single largest contributor to
  the F1 gap, since the differing ID also appears on each of the three child `is_a:` lines.
- Definition genus is "hereditary neuromuscular disease" rather than gold's "neuromyopathy".
  Both are defensible; the issue body itself wrote "Any neuromyopathy ...", so gold actually
  tracks the requester wording while the agent tracks its chosen genus class. Substantively
  equivalent.
- `dc:creator` is the requester ORCID `0000-0002-2078-7280` (from the issue) rather than the
  Mondo curator ORCID `0000-0002-5002-8648` used in gold. Defensible — the issue lists the
  requester ORCID as the nano-attribution — but it is a convention mismatch.
- Added a standalone `relationship: has_material_basis_in_germline_mutation_in` line that gold
  omits (gold relies on `intersection_of` only). This is conventional in Mondo and arguably
  more complete, but counts against recall as a minor over-edit.
- Omitted the gold's explicit `synonym: "KY-related neuromyopathy" EXACT ... {OMO:0002001=...}`
  and the gold's `excluded_from_qc_check` QC-suppression on MONDO:0044647 — the latter is an
  internal QC artifact no agent could anticipate and is a pure recall penalty, not a quality
  defect.

Overall this is a correct, well-scoped solution; the metadiff score should be read as a floor,
not a ceiling, on its quality.
