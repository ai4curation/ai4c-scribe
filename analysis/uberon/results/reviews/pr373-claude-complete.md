---
ontology: uberon
issue_number: 3602
pr_number: 3603
eval_repo_pr: 373
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
name, parent, definition text, and wdduncan's requester ORCID
`0000-0001-9625-1899`. The diff is identical to the sibling haiku run #501:
the core term is correct but the metadata is impoverished — it **dropped the
second definition xref** (HL7 `CodeSystem-FDI-surface.html`) and left the
**synonym xref empty (`[]`)** despite @aleixpuigb's explicit instruction in
issue #3602 to reference the synonym with
`https://dentaleducationhub.com/surfaces-of-the-teeth/`. Metadiff F1=0.667
(balanced P=R=0.667) is a *fair* assessment here — these are genuine
omissions, not metadiff artifacts. `partial_success`.

## Strengths

- **Correct term skeleton**: id `UBERON:8600149`, name `occlusal surface of
  tooth`, `is_a: UBERON:8600148 ! tooth surface structure` exactly as
  requested by @wdduncan — right parent and ID.
- **Correct definition text**: "A tooth surface structure that forms the
  biting or grinding surface of a molar or premolar." matches the gold and
  issue-body wording verbatim.
- **Correct requester attribution**: `relationship: dc-contributor
  https://orcid.org/0000-0001-9625-1899` (wdduncan's ORCID, as the gold
  uses), with `! Wendy Duncan` label.
- **Tight scope**: clean single-stanza insertion, no reserialization churn.

## Issues

- **Omission — empty synonym xref (`synonym: "occlusal surface" EXACT []`)**:
  ignores @aleixpuigb's explicit issue instruction to reference the synonym
  with `https://dentaleducationhub.com/surfaces-of-the-teeth/`; the gold
  carries that reference. Missed explicit requirement. (`under_editing`)
- **Omission — dropped second def xref**: the issue body and gold list *two*
  definition cross-references (`dentaleducationhub.com` *and* HL7
  `CodeSystem-FDI-surface.html`); this attempt kept only the first, dropping
  the authoritative HL7 FDI surface reference.
- **Missing CLAUDE.md-mandated metadata**: no `term_tracker_item` linking to
  issue #3602 and no real `created_by`/`dcterms-date` (placeholder
  `2026-05-16T00:00:00Z`), unlike the gpt-5.x attempts. Reinforces the
  under-editing pattern.
- Net: usable but under-specified; a curator would need to restore the
  synonym and definition references the issue explicitly supplied. Same
  shortfall as run #501.
