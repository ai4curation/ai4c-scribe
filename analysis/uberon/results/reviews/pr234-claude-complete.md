---
ontology: uberon
issue_number: 3478
pr_number: 3479
eval_repo_pr: 234
agent: std_claude_opus47
model: claude-opus-4-7
runtime: claude
agent_config_tag: ai4curation/uberon-agent-config@v3
case_type: axiom_repair
difficulty: hard
f1: 0.273
precision: 0.375
recall: 0.214
jaccard: 0.158
outcome: partial_success
failure_modes: [missed_requirement, scope_creep]
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-16
---

## Summary

This is the most thoroughly reasoned attempt in the case — the agent correctly
performed the three core edits (Chordata `in_taxon` on UBERON:0000110 and
UBERON:0004707, GCI conversion on UBERON:0007220) and wrote an exemplary PR comment
explaining its GCI relation choice and disclosing an unrelated artifact — yet it
scored the lowest F1 (0.273) of all seven attempts. The reason is a
robot-reserialization over-edit: `robot convert` re-synced ~10 cached CL labels from
a newer CL import into uberon-edit.obo, flooding the diff with issue-irrelevant
lines and cratering recall to 0.214. The metadiff badly under-represents the
substantive quality of the core change while correctly penalising the scope creep.

## Strengths

- Both taxon edits (UBERON:0000110, UBERON:0004707) are byte-identical to gold:
  `in_taxon NCBITaxon:6072 ! Eumetazoa` → `in_taxon NCBITaxon:7711 ! Chordata`.
- GCI on UBERON:0007220 uses `gci_relation="part_of"`, `gci_filler="NCBITaxon:7711"`
  — a defensible choice, explicitly justified in the PR comment by the pre-existing
  same-stanza rat GCI (`RnorDv:0000010 {gci_relation="part_of",
  gci_filler="NCBITaxon:10116"}`) and by the dominance of `part_of`-style taxon GCIs
  on life-cycle stages elsewhere in the file. It correctly noted the issue proposed
  `occurs in` (BFO:0000066) and offered a one-line switch.
- Best-in-class methodology and transparency: accurately diagnosed the latent
  taxon-constraint mechanism (RO:0002162 not propagating over temporal relations),
  documented its verification steps, and proactively disclosed the unrelated CL
  label refresh in a dedicated "Note on unrelated lines" section, offering to strip
  it.

## Issues

- Scope creep (dominant score driver): ~10 lines of unrelated CL label refreshes
  introduced by `robot convert` re-serializing against a newer merged CL import —
  CL:1000271 "lung ciliated cell" → "lung multiciliated epithelial cell",
  CL:0002145, CL:0002332, CL:1000223 "lung neuroendocrine cell" → "pulmonary
  neuroendocrine cell", CL:0000150 "glandular epithelial cell" → "glandular
  secretory epithelial cell" across UBERON:0003504, UBERON:0006524, UBERON:0006525
  and several glandular-epithelium terms. This is an ODK/robot-reserialization
  artifact, NOT eval-base contamination: it appears only in this attempt, not in the
  other six (verified — none of pr336/pr321/pr279/pr20/pr57/pr38 contain these
  hunks). The agent should have stripped these to keep an issue-only diff
  (`obo-checkin.pl`/targeted edit rather than whole-file reserialize) instead of
  leaving them in.
- Omission: definition-text rewrites of `neurula stage` and `pharyngula stage`
  ("A chordate developmental stage ...") not made (defensible — not in the issue
  body; all seven attempts missed this).
- Net: substance of the issue fix is correct and well-argued; F1=0.273 is
  artifact-driven and materially under-represents the core repair, but the over-edit
  is a real precision/recall problem the agent had the means to avoid.
