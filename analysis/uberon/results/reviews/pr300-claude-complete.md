---
ontology: uberon
issue_number: 3448
pr_number: 3506
eval_repo_pr: 300
agent: std_claude_son45
model: claude-sonnet-4.5
runtime: claude
agent_config_tag: v3
case_type: axiom_repair
difficulty: simple
f1: 0.0
precision: 0.0
recall: 0.0
jaccard: 0.0
outcome: success
failure_modes: []
case_quality: poor
case_quality_reason: metadiff_line_atomic_def_xref
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent reproduced the gold definition prose **verbatim** for both
UBERON:0013540 (Brodmann area 9) and UBERON:0034891 (insular cortex) — the
def text strings are byte-identical to gold PR #3506 — yet scores F1=0.000.
This is the clearest demonstration that the score is a **line-atomic metadiff
artifact**: the only delta from gold on the def lines is the xref bracket
(agent `[Wikipedia:Brodmann_area_9]` / `[Wikipedia:Insular_cortex, MESH:D000087623]`
vs gold `[Wikipedia:Brodmann_area_9, https://orcid.org/...]` /
`[Wikipedia:INSULA, MESH:D007419, https://orcid.org/...]`). Because the
metadiff compares whole normalized lines as set members, a perfect definition
with a differently-formatted xref earns zero credit. Substantively this is a
clean success and arguably the best attempt in the set.

## Strengths

- Definition prose for **both** terms is identical to the human expert text
  in issue #3448 and to gold PR #3506 — no paraphrase drift, no fabricated
  cytoarchitectural detail.
- Correctly followed agent config: added `dc-contributor` (with `! Dana
  Gabuxda` label), `dcterms-date`, `term_tracker_item` linking to issue
  #3448, and `created_by: dragon-ai-agent` — all explicitly requested by
  CLAUDE.md, even though the gold human PR omitted them.
- Added a defensible MeSH xref to the insular cortex def
  (`MESH:D000087623`, the current MeSH descriptor for insular cortex) —
  more modern/accurate than gold's legacy `MESH:D007419`, though it does not
  match Uberon's internal convention.
- Tight scope: only `src/ontology/uberon-edit.obo` touched; clean stanza
  structure preserved.

## Issues

- Def xref does not match gold's idiosyncratic, unspecified combination
  (ORCID inside the def bracket; `Wikipedia:INSULA` legacy identifier). This
  was not derivable from the issue and is the sole reason for the zero score.
- Inserted `relationship: dc-contributor` *between* the existing `is_a` and
  `part_of` lines rather than after structural axioms; cosmetically suboptimal
  ordering but semantically inert (and dc-contributor is a metadiff-ignored
  key).
- No substantive ontological error. F1 of 0.000 is the strongest single
  signal in this case that the metadiff under-represents quality; true
  outcome is success.
