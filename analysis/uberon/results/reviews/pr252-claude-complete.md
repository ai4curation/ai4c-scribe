---
ontology: uberon
issue_number: 3602
pr_number: 3603
eval_repo_pr: 252
agent: std_claude_op47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: new_term
difficulty: simple
f1: 0.632
precision: 1.000
recall: 0.462
jaccard: 0.462
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

claude-opus-4.7/claude added `UBERON:8600149` "occlusal surface of tooth" as a
subclass of `UBERON:8600148` "tooth surface structure", reproducing the gold PR
#3603 term stanza essentially line-for-line on the substantive content
(id, name, def with both issue cross-references, EXACT synonym with the
dentaleducationhub reference, `is_a`, wdduncan's ORCID contributor, dcterms-date).
The metadiff F1=0.632 (P=1.000, R=0.462) **substantially under-represents** the
quality: precision is perfect, and recall is depressed only by (a) three
`robot convert` reserialization label-refresh hunks on unrelated classes and
(b) three extra metadata lines that the project CLAUDE.md explicitly requires.
This is a clean `success`.

## Strengths

- **Term content matches gold exactly**: same ID `UBERON:8600149`, name,
  definition text, *both* definition xrefs (`dentaleducationhub.com` and the
  HL7 `CodeSystem-FDI-surface.html`) — matching the gold's two-xref def and
  the two cross-references listed in issue #3602's body. Sonnet's attempt
  (#298) dropped the second xref; opus got it right.
- **Correct parent and synonym**: `is_a: UBERON:8600148 ! tooth surface
  structure` as requested by @wdduncan in the issue body and used by all
  sibling tooth-surface terms; EXACT synonym `"occlusal surface"` with the
  `https://dentaleducationhub.com/surfaces-of-the-teeth/` reference exactly as
  @aleixpuigb instructed in the issue thread (gold uses the same).
- **Correct attribution**: includes wdduncan's requester ORCID
  `0000-0001-9625-1899` (the one the gold uses); additionally credits the
  carrying curator Aleix Puig-Barbé (`0000-0001-6677-8489`), consistent with
  the sibling-term pattern in this 8600xxx family and with @aleixpuigb's
  "I will add" comment. Defensible extra, not an error.
- **Followed CLAUDE.md "Other metadata" guidance**: added
  `property_value: term_tracker_item ".../issues/3602"` and
  `created_by: dragon-ai-agent` — both explicitly mandated by the agent config
  ("Link back to the issue ... using `term_tracker_item`"; "You can sign terms
  as `created_by: dragon-ai-agent`"). The gold stanza omits these, so metadiff
  counts them against recall, but they are correct practice per instructions.
- **Reserialized via `robot convert`** as the CLAUDE.md workflow requires, and
  **transparently disclosed** the resulting label-only side effects in the PR
  comment ("Side effects of reserialization").
- **Sound verification trail**: PR checklist confirms parent existence, ID
  availability, search for pre-existing "occlusal" terms, and sibling-pattern
  modeling.

## Issues

- **robot-convert reserialization churn (artifact, not a substantive error)**:
  three hunks refresh `!` label comments on classes unrelated to issue #3602 —
  `CL:0000649` (`prickle cell` → `spinous cell of epidermis`) and `GO:0098643`
  (`banded collagen fibril` → `fibrillar collagen`, two occurrences). The
  underlying logical references (`CL:0000649`, `GO:0098643`) are unchanged;
  these are upstream label syncs produced by the mandated
  `robot convert -f obo` step. They are the dominant contributor to the
  depressed recall but are not a quality defect; the agent flagged them
  explicitly. Not scored as a failure mode.
- **No genuine ontological issues.** The metadiff gap is entirely (a)
  CLAUDE.md-required metadata absent from a minimal gold stanza and (b)
  reserialization label churn. Substantively the term is correct, complete,
  and well-formed.

Note: the gold PR #3603 is the *sole and complete* human resolution of issue
#3602 (it was itself authored by dragon-ai-agent). The later PRs #3633 / WIP
#3632 ("Update occlusal surface of tooth term") belong to a *different* issue,
#3631, and are not companions for this case — so this is not a multi-PR /
partial-gold situation. F1 here is a metadiff-convention undercount, not a
poor-case signal; the case quality is fine.
