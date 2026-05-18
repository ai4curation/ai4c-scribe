---
ontology: uberon
issue_number: 3596
pr_number: 3597
eval_repo_pr: 631
agent: std_opencode_gpt55
model: gpt-5.5
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

The agent correctly resolved both taxon-constraint unsatisfiabilities flagged in issue #3596, producing a diff (blob `12c2854`) byte-identical to the gpt-5.4 opencode runs (#610, #666), the codex run (#384), and the prior claude runs (#251/#297). For the epiphyseal tract it made exactly the gold change (`intersection_of: innervates UBERON:0004869 ! parietal organ` → `UBERON:0015238 ! pineal complex`); for the adductor muscle of hip it chose strategy **B** from the issue (drop the tetrapod-specific `relationship: innervated_by UBERON:0005465 ! obturator nerve`) whereas the human PR #3597 chose strategy **A** (retighten the equivalence axiom from `part_of UBERON:0010709 ! pelvic complex` to `part_of UBERON:0001464 ! hip`). Both A and B are explicitly sanctioned by @gouttegd in the issue and both clear the ZFA:0000497/ZFA:0000592 unsats, so the metadiff F1=0.444 under-represents correctness on that line; the genuine extra is an unrequested rewrite of the epiphyseal-tract text `def:` line that gold left untouched.

## Strengths

- Epiphyseal-tract logical-definition fix (`intersection_of: innervates UBERON:0015238 ! pineal complex`) is exactly the gold axiom and exactly the fix prescribed in the issue (parietal organ UBERON:0004869 is one part of the pineal complex UBERON:0015238; the pineal tract UBERON:0034715 branch innervates the pineal body UBERON:0001905). The PR comment articulates this mechanism correctly.
- Both ZFA unsatisfiabilities (ZFA:0000497, ZFA:0000592) genuinely resolved: dropping the `innervated_by obturator nerve` axiom breaks the tetrapod-specific constraint that was propagating through the loose `part_of pelvic complex` equivalence — exactly the "loose definition, tight classification" mechanism the issue describes. Strategy B is a valid, issue-sanctioned resolution.
- Tightly scoped: only the two intended terms (UBERON:0034714, UBERON:0011144) touched, no collateral edits; used the project's `obo-checkout.pl`/`obo-checkin.pl` workflow.

## Issues

- **Wrong pattern vs human (defensible):** chose strategy B where gold chose strategy A for UBERON:0011144. The human kept the obturator-nerve innervation and instead retightened the equivalence axiom to `part_of UBERON:0001464 ! hip`. Strategy B leaves a vertebrate-wide `adductor muscle of hip` whose label/synonyms remain tetrapod-flavored — a modeling-philosophy divergence, not an error.
- **Extra edit (minor scope):** rewrote the text definition `def: "A cranial nerve fiber tract that innervates the parietal eye." → "...the pineal complex."`. Gold did **not** alter this `def:` line. Mirroring prose to the logical definition is defensible but unrequested, and it lowers precision vs gold while drifting the human-readable text away from the cited source.
- Metadiff F1=0.444 is a genuine score (real A-vs-B divergence on the adductor line + the extra def edit), not a poor-case artifact. It modestly under-represents quality because the adductor resolution is a valid issue-sanctioned alternative, but the def-text edit is a real extra not present in gold.
