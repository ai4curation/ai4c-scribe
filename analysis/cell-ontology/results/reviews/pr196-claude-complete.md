---
ontology: cell-ontology
issue_number: 3597
pr_number: 3598
eval_repo_pr: 196
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/cl-agent-config@v3
case_type: new_term
difficulty: hard
f1: 0.086
precision: 0.086
recall: 0.085
jaccard: 0.045
outcome: success
failure_modes: []
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This attempt (claude-opus-4.7) added all 8 requested oral/salivary-gland cell
types with the strongest methodology and explicit ontological reasoning of the
three attempts: it ran `robot convert` and `robot reason --reasoner ELK`
(no unsatisfiable classes), justified each EquivalentClasses-vs-SubClassOf choice,
and flagged the future-dated PMIDs in the issue. The reported F1 of 0.086
severely under-represents quality and is a **placeholder/off-by-one CL ID
artifact** plus an **OWL serialization-order artifact**: the agent allocated
CL_9900000–CL_9900007 while gold used CL_9900001–CL_9900008, and appended the
block at end-of-file (after the CL_0000540 taxon axiom) rather than gold's
mid-file location after CL_7770006, so every CL-ID-bearing line and surrounding
context line differs from gold. This is a genuine `success` whose score is an
artifact, not a poor-case flag — the issue has a single, clean, approved gold PR
(#3598), no companion PRs, no contamination, no curator repudiation.

## Strengths

- All 8 terms correctly modeled with the issue's requested parents, UBERON
  `part_of`, and GO `capable_of` targets (CL_0000313/UBERON:0001044/GO:0046541;
  CL_0000646/UBERON:0001837; CL_0000057/UBERON:0001044/GO:0030198;
  CL_0002077/UBERON:0001949/GO:0002227; CL_0002204/UBERON:0001831 & 0001832;
  CL_0005006/UBERON:0001044/GO:0050801; CL_0000185/UBERON:0001044/GO:0006939).
- Best ontological reasoning of the three: used `EquivalentClasses` genus-
  differentia definitions for the cleanly compositional terms (CL_9900001 basal
  duct, 9900004/5 tuft, 9900006 ionocyte, 9900007 myoepithelial) and explicitly
  argued for `SubClassOf`-only on demilune, periductal fibroblast, and
  junctional epithelial cell to avoid inappropriate equivalence with
  CL_4052065 (serous acinar) and CL_0002621 (gingival epithelial cell). This
  matches gold's *actual* treatment of the periductal and junctional terms,
  which gold also defined with SubClassOf only.
- Surfaced a real data-quality concern (future/recent PMIDs PMID:41686279 etc.
  and "Isola 2026"/"Uchida & Ovitt 2026" placeholder-style citations) and
  conservatively xref'd only verifiable issue-listed PMIDs — sound curatorial
  judgment.
- Reasoned correctly that gold's second parent for the sublingual tuft cell
  (CL_0002251, epithelial cell of alimentary canal) is entailed via the
  part_of chain, and documented the decision rather than silently dropping it.
- `IAO_0000233` term_tracker_item, ORCID contributor, and label/definition/
  synonym sets on all terms; ran ELK reasoning and ROBOT validation. Clean diff
  (114 additions, 0 deletions, single file), no base contamination.

## Issues

- Off-by-one ID allocation: CL_9900000–CL_9900007 vs gold's
  CL_9900001–CL_9900008. Unavoidable placeholder artifact and the primary cause
  of the near-zero F1; grade on substance, not the score.
- Serialization placement: appended the block at end-of-file (after the
  CL_0000540 NCBITaxon_7742 develops_from axiom), whereas gold inserted it
  mid-file after CL_7770006. Valid OWL but compounds context-line divergence.
- Syntax style: `IAO_0000233` value emitted as a quoted string literal
  (`"https://github.com/.../issues/3597"`) rather than gold's IRI form
  (`<https://github.com/.../issues/3597>`). Both parse, but the gold/CL
  convention is an IRI; minor deviation.
- Scope (minor extra vs gold): added `terms:creator "GitHub Copilot"` to every
  term — gold has no `terms:creator`. Harmless but unrequested.
- Definitions paraphrased and ASCII-normalized (alpha-amylase, IL-1alpha)
  relative to gold's Unicode text; defensible style difference, contributes to
  metadiff line mismatch beyond the ID offset.
