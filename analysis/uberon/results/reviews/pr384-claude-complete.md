---
ontology: uberon
issue_number: 3596
pr_number: 3597
eval_repo_pr: 384
agent: std_codex_gpt54
model: gpt-5.4
runtime: codex
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

The agent correctly resolved both taxon-constraint unsatisfiabilities from issue #3596, producing a diff (blob `12c2854`) byte-identical to the gpt-5.x opencode runs (#631, #572, #610, #666). Epiphyseal tract: exactly the gold change (`intersection_of: innervates UBERON:0004869 ! parietal organ` → `UBERON:0015238 ! pineal complex`). Adductor muscle of hip: it explicitly chose strategy **B** (remove `relationship: innervated_by UBERON:0005465 ! obturator nerve`) whereas the human PR #3597 chose strategy **A** (retighten the equivalence axiom from `part_of UBERON:0010709 ! pelvic complex` to `part_of UBERON:0001464 ! hip`). Both A and B are explicitly sanctioned in the issue by @gouttegd and both clear the ZFA:0000497/ZFA:0000592 unsats, so F1=0.444 under-represents correctness on that axiom; the only genuine extra is the unrequested rewrite of the epiphyseal-tract text `def:` line.

## Strengths

- Epiphyseal-tract logical fix (`intersection_of: innervates UBERON:0015238 ! pineal complex`) is exactly the gold axiom and exactly the issue prescription; the PR comment correctly explains that the pineal-tract (UBERON:0034715) branch innervates the pineal body (UBERON:0001905), so the whole tract innervates more than just the parietal organ.
- Both ZFA unsatisfiabilities (ZFA:0000497, ZFA:0000592) genuinely resolved by removing the tetrapod-specific `innervated_by obturator nerve` axiom, breaking propagation through the loose `part_of pelvic complex` equivalence — exactly the "loose definition, tight classification" mechanism in the issue.
- Strong methodology: explicitly named the strategy A/B trade-off and justified B; used `obo-checkout.pl`/`obo-checkin.pl`; honestly disclosed that `robot convert` reserialization could not run because `robot` was not installed in the sandbox (deferred to CI). Tightly scoped to the two intended terms (UBERON:0034714, UBERON:0011144).

## Issues

- **Wrong pattern vs human (defensible):** strategy B vs gold's strategy A for UBERON:0011144 — a modeling-philosophy divergence (B leaves a vertebrate-wide term with a tetrapod-flavored label), not an error, and one the agent flagged explicitly for reviewer input.
- **Extra edit (minor scope):** rewrote `def: "...innervates the parietal eye." → "...the pineal complex."`. Gold did not change this `def:` line; unrequested, lowers precision vs gold.
- Metadiff F1=0.444 is a genuine, non-artifactual score. It modestly under-represents quality (the adductor resolution is a valid sanctioned alternative; methodology documentation is strong) but the def-text edit is a real extra not present in gold.
