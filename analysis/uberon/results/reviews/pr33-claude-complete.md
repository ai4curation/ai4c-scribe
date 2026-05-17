---
ontology: uberon
issue_number: 3490
pr_number: 3585
eval_repo_pr: 33
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: axiom_repair
difficulty: hard
f1: 0.200
precision: 0.333
recall: 0.143
jaccard: 0.111
outcome: partial_success
failure_modes: [scope_creep, wrong_pattern]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent adopted the FBbt #2008 canonical def + comment ("A structure
mainly consisting of cell components, rather than complete cells." / "May
contain complete cells in addition to partial ones."), which is conceptually
the gold target. But it then made several unrequested decisions: it
**deleted** `xref: CARO:0001000`, changed the def's source bracket from
`[CARO:0001000]` to the issue URL, rewrote `external_ontology_notes`, and
added `term_tracker_item`. The CARO xref deletion and def-source change
contradict the gold approach (gold kept `[CARO:0001000]`) and rest on a
contestable equivalence-mapping argument. F1=0.200 (lowest of the set) is
driven by these extra/divergent lines; partial success.

## Strengths

- Core def + comment match the FBbt:00007060 canonical wording that gold PR
  #3585 derived from — conceptually the right resolution of issue #3490, and
  the comment is correctly unquoted OBO (better than gemma #135).
- Used the clean two-part def + comment structure that gold adopted.
- Reasoning is articulated (PR comment) rather than silent: the agent
  explicitly justified the CARO changes, so this is a deliberate (if
  debatable) call, not an accident.

## Issues

- Wrong pattern / over-reach: deleted `xref: CARO:0001000` and replaced the
  def source `[CARO:0001000]` with `[https://github.com/obophenotype/uberon/issues/3490]`.
  Rationale given ("CARO xrefs are equivalence mappings; the broadened class
  is broader than CARO:0001000") is plausible but speculative and was **not**
  the human curator's decision — gold deliberately kept `[CARO:0001000]` on
  the def and the `xref: CARO:0001000`. Removing a cross-ontology xref on an
  unstated inference is a significant scope/judgment overstep for an issue
  that only asked to relax the textual definition. Also drops the def's
  original CARO provenance.
- Scope creep: rewrote `external_ontology_notes` to add a "broader than
  CARO:0001000" clause, and added `property_value: term_tracker_item`. Both
  unrequested and not in the gold diff.
- Net: the central definition edit is correct, but the cascade of
  unrequested CARO-mapping changes plus note/metadata edits make this the
  most over-scoped attempt. partial_success: right idea, undisciplined and
  speculative execution; the low F1 is partly deserved here (unlike the
  scope-clean attempts where F1 is purely an artifact).
