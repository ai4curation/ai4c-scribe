---
ontology: uberon
issue_number: 3602
pr_number: 3603
eval_repo_pr: 501
agent: std_claude_haiku45
model: claude-haiku-4-5
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: simple
case_quality: good
f1: 0.667
precision: 0.667
recall: 0.667
jaccard: 0.500
outcome: partial_success
failure_modes:
  - under_editing
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

claude-haiku-4.5/claude added `UBERON:8600149` "occlusal surface of tooth" as
a subclass of `UBERON:8600148` "tooth surface structure" with the correct ID,
name, parent, and wdduncan's requester ORCID `0000-0001-9625-1899`. The core
new term is correct, but the metadata is impoverished relative to both the
gold and the issue's explicit instructions: it **dropped the second
definition xref** (HL7 `CodeSystem-FDI-surface.html`) and left the **synonym
xref empty (`[]`)** even though @aleixpuigb explicitly told the agent to use
`https://dentaleducationhub.com/surfaces-of-the-teeth/` to reference the
synonym. Metadiff F1=0.667 (balanced P=R=0.667) here is a *fair*
representation — these are genuine omissions, not metadiff-convention
artifacts. `partial_success`.

## Strengths

- **Correct term skeleton**: id `UBERON:8600149`, name `occlusal surface of
  tooth`, `is_a: UBERON:8600148 ! tooth surface structure` exactly as
  requested by @wdduncan in the issue body — the right parent and ID.
- **Correct definition text**: "A tooth surface structure that forms the
  biting or grinding surface of a molar or premolar." matches the gold and
  issue-body wording verbatim (no extra "tooth", unlike the gpt-5.5 runs).
- **Correct requester attribution**: `relationship: dc-contributor
  https://orcid.org/0000-0001-9625-1899` — wdduncan's ORCID, the one the
  gold uses; also added the `! Wendy Duncan` label inline.
- **Tight scope, no churn**: clean single-stanza insertion, no
  reserialization side effects.

## Issues

- **Omission — empty synonym xref (`synonym: "occlusal surface" EXACT []`)**:
  @aleixpuigb's issue comment explicitly instructed "you can use
  'https://dentaleducationhub.com/surfaces-of-the-teeth/' to reference it"
  for the synonym. The gold carries that reference; this attempt left the
  bracket empty. A missed explicit requirement. (`under_editing`)
- **Omission — dropped second def xref**: the issue body and gold both list
  *two* cross-references for the definition (`dentaleducationhub.com` *and*
  the HL7 `CodeSystem-FDI-surface.html`); this attempt kept only the first.
  The HL7 FDI surface code system is the authoritative dental-surface
  reference and should not have been dropped.
- **Missing CLAUDE.md-mandated metadata**: no `term_tracker_item` linking
  back to issue #3602 and no `created_by`/`dcterms-date` consistent with the
  config's "Other metadata" guidance (only a placeholder
  `dcterms-date "2026-05-16T00:00:00Z"`). The gpt-5.x attempts included
  these; haiku did not. Minor relative to the xref omissions, but reinforces
  the under-editing pattern.
- Net: the term is usable but under-specified; a curator would have to add
  back the synonym and definition references the issue explicitly supplied.
