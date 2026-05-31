---
ontology: uberon
issue_number: 3596
pr_number: 3597
eval_repo_pr: 610
agent: std_opencode_gpt54
model: gpt-5.4
runtime: opencode
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
case_quality: ok
f1: 0.444
precision: 0.500
recall: 0.400
jaccard: 0.286
outcome: partial_success
failure_modes:
  - wrong_pattern
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-17
---

## Summary

The agent correctly resolved both taxon-constraint unsatisfiabilities from issue #3596, producing a diff (blob `12c2854`) byte-identical to the other gpt-5.x opencode runs (#631, #572, #666) and the codex run (#384). Epiphyseal tract: exactly the gold change (`intersection_of: innervates UBERON:0004869 ! parietal organ` → `UBERON:0015238 ! pineal complex`). Adductor muscle of hip: strategy **B** (remove `relationship: innervated_by UBERON:0005465 ! obturator nerve`) whereas the human PR #3597 chose strategy **A** (retighten the equivalence axiom from `part_of UBERON:0010709 ! pelvic complex` to `part_of UBERON:0001464 ! hip`). Both are explicitly sanctioned by the issue and both clear the ZFA:0000497/ZFA:0000592 unsats, so F1=0.444 under-represents correctness on that axiom; the only genuine extra is the unrequested rewrite of the epiphyseal-tract text `def:` line.

## Strengths

- Epiphyseal-tract logical fix (`intersection_of: innervates UBERON:0015238 ! pineal complex`) is exactly the gold axiom and exactly the issue prescription (parietal organ UBERON:0004869 is one part of the pineal complex UBERON:0015238; pineal tract UBERON:0034715 branch innervates pineal body UBERON:0001905).
- Both ZFA unsatisfiabilities (ZFA:0000497, ZFA:0000592) genuinely resolved: dropping the tetrapod-specific `innervated_by obturator nerve` axiom breaks the constraint propagating through the loose `part_of pelvic complex` equivalence — the exact "loose definition, tight classification" mechanism described in the issue. Strategy B is valid and issue-sanctioned.
- Tightly scoped to the two intended terms (UBERON:0034714, UBERON:0011144); no collateral edits. (Diff-only attempt record — no PR comment present, so methodology narrative could not be assessed.)

## Issues

- **Wrong pattern vs human (defensible):** strategy B vs gold's strategy A for UBERON:0011144 — a modeling-philosophy divergence (B leaves a vertebrate-wide term with a tetrapod-flavored label), not an error.
- **Extra edit (minor scope):** rewrote `def: "...innervates the parietal eye." → "...the pineal complex."`. Gold did not change this `def:` line; unrequested, lowers precision vs gold.
- Metadiff F1=0.444 is a genuine, non-artifactual score. It modestly under-represents quality (the adductor resolution is a valid sanctioned alternative) but the def-text edit is a real extra not present in gold.
