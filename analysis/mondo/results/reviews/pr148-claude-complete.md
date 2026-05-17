---
ontology: mondo
issue_number: 9896
pr_number: 10207
eval_repo_pr: 148
agent: std_opencode_g55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: synonym_update
difficulty: simple
f1: 0.235
precision: 0.5
recall: 0.154
jaccard: 0.133
outcome: failure
failure_modes: [over_editing, scope_creep, wrong_pattern, missed_requirement]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

Issue #9896 requested the ClinGen preferred label "GCSH-related glycine
encephalopathy" for MONDO:0957382. The curator deliberately declined to rename
the term (citing the scope conflict with MONDO:0011612 'glycine encephalopathy'
and the OMIM:620423 equivalence) and added it only as an EXACT synonym. This
attempt did the opposite of the curator's decision: it **renamed** the primary
label to "GCSH-related glycine encephalopathy", rewrote the definition with a
"glycine encephalopathy" genus, added an `intersection_of` logical definition,
a `clingen` subset, an extra `curated_content_resource` relationship, and a
second parent. F1=0.235 (precision 0.5, recall 0.154) is roughly fair: it
matched the synonym and tracker but performed the exact rename and logical
restructuring the curator explicitly chose not to do.

## Strengths

- The ClinGen synonym line is well-formed and fully attributed:
  `synonym: "GCSH-related glycine encephalopathy" EXACT [https://clinicalgenome.org/affiliation/40011/, https://orcid.org/0000-0002-7437-8060] {OMO:0002001="https://w3id.org/information-resource-registry/clingen"}`
  — byte-identical to the gold synonym, better attributed than attempt #255.
- Added `property_value: IAO:0000233 ".../issues/9896"` issue tracker, matching gold.
- Preserved the existing `is_a: MONDO:0017338` parent and added MONDO:0011612
  as an *additional* parent rather than replacing it, respecting the config's
  no-parent-removal rule (unlike the haiku/sonnet attempts).

## Issues

- Wrong approach / instruction outcome: renamed MONDO:0957382 to
  "GCSH-related glycine encephalopathy". The curator explicitly raised the
  scope conflict and decided **not** to rename (issue comments
  2026-04-29 and 2026-05-01). The agent's PR comment claims the issue needed
  clarification yet still committed the full rename, an internal contradiction.
- Wrong def genus: gold kept "Any multiple mitochondrial dysfunctions
  syndrome..."; the agent wrote "Any glycine encephalopathy in which the cause
  of the disease is a mutation in the GCSH gene." with sources
  `[https://clinicalgenome.org/affiliation/40011/, OMIM:620423]` — not the
  gold's `[https://orcid.org/0000-0002-7638-4659, OMIM:620423]`.
- Scope creep / over-editing: added `intersection_of` axioms (a full logical
  definition / equivalence), a `clingen` subset, and
  `relationship: curated_content_resource https://search.clinicalgenome.org/...`
  — none requested by the issue, all absent from gold, and the equivalence
  axiom would force MONDO:0957382 to be equivalent to the GCSH-restricted
  glycine encephalopathy intersection, a substantive classification change the
  curator did not sanction.
- Net: failure — the synonym/tracker were correct but the rename + logical
  restructuring is precisely the change the curator examined and rejected.
