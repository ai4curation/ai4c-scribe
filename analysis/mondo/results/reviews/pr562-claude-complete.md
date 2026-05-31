---
ontology: mondo
issue_number: 9875
pr_number: 10202
eval_repo_pr: 562
agent: std_codex_g55
model: gpt-5.5
runtime: codex
agent_config_tag: v3
case_type: other
difficulty: simple
f1: 0.75
precision: 1.0
recall: 0.6
jaccard: 0.6
outcome: success
failure_modes: [over_editing]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Summary

The gpt-5.5 / codex run produced the **most complete and arguably best** solution of the eight attempts. It made the human's exact two edits to MONDO:0700039 (the `name:` typo fix *and* the `property_value: IAO:0000233 ".../issues/9875"` term-tracker-item provenance line — the only attempt besides #399's partial that engaged provenance, and the only one that added it to MONDO:0700039 matching gold), and additionally fixed the same misspelling where it survived as a NARROW synonym on the parent term MONDO:0017919, adding a parallel issue xref/tracker item there. Metadiff F1 of 0.75 (P=1.0, R=0.6) **under-represents** quality: precision is perfect (every line it changed, the human also changed or is a defensible improvement); recall is lowered only because the extra MONDO:0017919 consistency edits aren't in the narrow human PR.

## Strengths

- Reproduced both of the human's edits on MONDO:0700039 exactly: the label fix **and** the `IAO:0000233 "...issues/9875"` term-tracker-item annotation — the only standard-config attempt to add the gold provenance line on the target term (P = 1.0).
- Caught the pre-existing duplicate of the misspelling that the human PR missed: the NARROW synonym `"bladder exstrophy-epispadias-cloacal extrophy complex"` on MONDO:0017919 (exstrophy-epispadias complex). Correcting it removes the last `extrophy` instance from `mondo-edit.obo` and keeps the parent's synonym consistent with the corrected child label — a justified thoroughness improvement over the gold.
- Followed MONDO provenance convention consistently: attached `IAO:0000233 ".../issues/9875"` and an issue xref on the synonym to MONDO:0017919 as well, mirroring how the curator annotated MONDO:0700039.

## Issues

- Scope (defensible, not an error): the MONDO:0017919 synonym fix and its tracker item are beyond the literal issue ask (which named only MONDO:0700039) and beyond the human PR, which is why recall is 0.6. This is justified cleanup of a genuine pre-existing inconsistency, not gratuitous over-editing — it improves on the gold rather than diverging from it.
- No correctness or syntax problems found; the only "failure mode" recorded (`over_editing`) is the strict-metadiff label for defensible extra work.
