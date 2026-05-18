---
ontology: uberon
issue_number: 3490
pr_number: 3585
eval_repo_pr: 443
agent: std_opencode_k26
model: kimi-k2.6
runtime: opencode
agent_config_tag: v3
case_type: axiom_repair
difficulty: hard
case_quality: ok
case_quality_reason: metadiff_tiny_freetext_def_ceiling
f1: 0.250
precision: 0.333
recall: 0.200
jaccard: 0.143
outcome: partial_success
failure_modes: [scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent rewrote the UBERON:0005162 def to the FBbt #2008 canonical form
("A structure mainly consisting of cell components, rather than complete
cells.") and added a glia-free but on-point comment ("May contain complete
cells in addition to partial ones."), retaining `[CARO:0001000]`. The core
semantic change is correct and conceptually equivalent to gold PR #3585.
However it bundled five extra metadata/xref lines, the heaviest scope load of
any attempt on this case, so F1=0.250 (recall 0.200, the lowest in the set)
is depressed by both tiny-free-text metadiff geometry and real scope creep —
substance is partial_success.

## Strengths

- Core def + comment match the FBbt:00007060 canonical proposal that gold
  itself derived from; the def is near-verbatim the FBbt source ("mainly
  consisting of cell components, rather than complete cells") and the comment
  conveys the same "complete cells in addition to partial ones" idea as
  gold's comment. Conceptually as correct as gold on the actual ask.
- Retained `[CARO:0001000]` on the def — correct provenance, better than
  gpt-5.5 codex #33 which deleted the CARO xref.
- Preserved `composed_primarily_of GO:0005575` and the is_a parentage;
  correctly reasoned (PR comment) that the OWL axiom already encodes "mainly
  cell components" so no logical change was needed — accurate.
- Documented methodology: read the linked FBbt #2008 issue,
  obo-checkout/checkin, diff review before commit.

## Issues

- Scope creep (the differentiator here): five lines beyond gold —
  `xref: FBbt:00007060`, an added `[CARO:0001000, FBbt:00007060]` source on
  the def, `term_tracker_item ...#3490`, `dc-contributor` Clare Pilgrim,
  `dcterms-date 2026-05-16`, and `created_by: dragon-ai-agent`. Gold added
  none of these.
- The FBbt:00007060 xref/def-source addition is actively contrary to the
  issue: the issue says "If not we can remove our mapping" — i.e. the FBbt
  mapping's fate was conditional and a curator decision, not an instruction
  to assert a new `xref: FBbt:00007060`. Adding it is an unrequested,
  speculative mapping edit (same over-reach family as #33's CARO swap).
- Attributing authorship to "Clare Pilgrim" via `dc-contributor` is
  incorrect provenance — she is the issue reporter (Clare72), not the editor
  of this change.
- Comment omits the glia example that gold and #249 included; minor, the
  concept is still conveyed.
- Net: correct target, correct semantic edit, but the heaviest unrequested
  metadata/mapping bundle of the case. partial_success; metadiff understates
  the core def correctness but the scope problems are genuine.
