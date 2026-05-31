---
ontology: uberon
issue_number: 3602
pr_number: 3603
eval_repo_pr: 668
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: simple
case_quality: good
f1: 0.923
precision: 1.000
recall: 0.857
jaccard: 0.857
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

gpt-5.4/opencode added `UBERON:8600149` "occlusal surface of tooth" as a
subclass of `UBERON:8600148` "tooth surface structure", reproducing the gold
PR #3603 term stanza essentially line-for-line on substantive content: same
ID, name, definition text with *both* issue cross-references
(`dentaleducationhub.com` and the HL7 `CodeSystem-FDI-surface.html`), the
EXACT synonym `"occlusal surface"` with the dentaleducationhub reference, the
correct `is_a` parent, and wdduncan's requester ORCID
(`0000-0001-9625-1899`). Metadiff F1=0.923 (P=1.000, R=0.857)
**under-represents** the quality: precision is perfect and the only recall
gap is (a) two extra metadata lines the project CLAUDE.md explicitly mandates
and (b) a single trailing-newline normalization from the required
`robot convert` reserialization. Clean `success`.

## Strengths

- **Term content matches gold exactly**: id `UBERON:8600149`, name, full
  definition text, *both* def xrefs (matching the two cross-references in
  issue #3602's body and the gold's two-xref def), EXACT synonym
  `"occlusal surface"` with the `dentaleducationhub.com/surfaces-of-the-teeth/`
  reference that @aleixpuigb explicitly instructed in the issue thread.
- **Correct parent and attribution**: `is_a: UBERON:8600148 ! tooth surface
  structure` as requested by @wdduncan; `relationship: dc-contributor
  https://orcid.org/0000-0001-9625-1899` — the exact ORCID the gold uses.
- **Followed CLAUDE.md "Other metadata" guidance**: added
  `property_value: term_tracker_item ".../issues/3602"` and
  `created_by: dragon-ai-agent`, both mandated by the agent config. The
  minimal gold stanza omits these, so metadiff counts them against recall,
  but they are correct practice per instructions.
- **Strong verification trail**: the PR comment documents parent-existence
  check, ID-availability check, sibling-pattern review (`distal/incisal
  surface of tooth`), source verification, and `robot convert` reserialization
  — exactly the workflow the config prescribes, with side effects disclosed.

## Issues

- **robot-convert trailing-newline churn (artifact, not a defect)**: the diff
  removes one trailing blank line at EOF (`vessel_supplies_blood_to`
  typedef), a benign side effect of the mandated `robot convert -f obo`
  reserialization. It is a minor recall contributor, not an ontological
  error, and was disclosed.
- **No genuine ontological issues.** The entire metadiff gap is
  CLAUDE.md-required metadata plus serialization normalization; the term is
  correct, complete, and well-formed.
