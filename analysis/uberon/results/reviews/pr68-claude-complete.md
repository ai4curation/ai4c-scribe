---
ontology: uberon
issue_number: 3490
pr_number: 3585
eval_repo_pr: 68
agent: std_opencode_gpt55
model: gpt-5.5
runtime: opencode
agent_config_tag: v3
case_type: axiom_repair
difficulty: hard
f1: 0.333
precision: 0.333
recall: 0.333
jaccard: 0.200
outcome: success
failure_modes: [scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

The agent rewrote the UBERON:0005162 def to permit some whole cells while
keeping the "primarily multiple cell components / not itself a cell" core,
retained `[CARO:0001000]`, and added a `term_tracker_item` linking issue
#3490. The definition correctly resolves the issue and is semantically
equivalent to gold PR #3585, though it is more verbose than gold's crisp
form and adds no clarifying `comment:`. F1=0.333 is largely a tiny-diff
artifact (single rewritten def line + an extra metadata line); the core edit
is sound.

## Strengths

- Definition is biologically and ontologically correct: "...consisting
  primarily of multiple cell components from two or more cells, which is not
  itself a cell and may include some whole cells as additional parts."
  removes exactly the restriction issue #3490 targeted while preserving the
  upper-level concept and the FMA "two or more cells" framing.
- Retained `[CARO:0001000]` def xref (provenance preserved) — better than
  the gemma attempt #135.
- `term_tracker_item` linking #3490 is a defensible provenance addition; it
  is a metadiff-ignored/under-weighted field and matches common Uberon
  practice even though gold did not add it here.

## Issues

- Scope: the added `property_value: term_tracker_item` is not part of the
  gold diff and not requested by the issue. Defensible (standard provenance),
  but it is the extra line that, with the reworded def, holds recall at
  0.333. Categorized as mild scope_creep, not an error.
- Omission vs gold: no `comment:` clarifying the glia-in-nervous-system case.
  Gold (and FBbt canonical) split the nuance into a comment; folding it into
  the def yields a wordier, slightly less reusable definition. Not wrong,
  stylistically inferior to gold.
- Footer mislabels the runtime as "pi agent" in the PR comment though the
  config tag is opencode/gpt-5.5; cosmetic, no impact on the edit.
