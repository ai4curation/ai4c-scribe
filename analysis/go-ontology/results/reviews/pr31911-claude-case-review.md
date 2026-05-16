---
ontology: go-ontology
issue_number: 19185
pr_number: 31911
case_type: new_term
difficulty: hard
num_agent_attempts: 0
agent_coverage: none
gold_assessment: sound
case_quality: good
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Status

No agent attempts were generated for this case as of 2026-05-15. There is no
`attempts/` subdirectory and `num_agent_attempts: 0`. This is an
**eval-coverage gap, not an agent failure** — no model was run against this
case, so there is nothing to score. The deliverable here is a case-level
assessment of the source issue and the human gold PR to confirm the case is a
sound target for future eval runs.

## Source Issue

Issue #19185 (open since 2020-03-29) is a long-standing MF-in-BP refactoring
request. The original BP term GO:0051764 `actin crosslink formation` describes
what is really a molecular function (an adaptor activity that bridges two
actin filaments). The requester (@ValWood) asked @dragon-ai-agent for two
concrete edits:

1. Create a new MF term `actin-filament cross-linking activity` with the
   definition "An adaptor activity that brings together two actin filaments,
   enabling the bundling or networking of actin filaments (F-actin)." as a
   descendant of GO:0008093.
2. Swap the primary label and synonym of GO:0008093: make
   `cytoskeletal adaptor activity` the primary label and
   `cytoskeletal anchor activity` a narrow synonym.

Obsoletion of GO:0051764 was explicitly **deferred** to a later step (pgaudet:
"you need to first create the new term to allow people to move their
annotations"). There was substantive post-request discussion: @pgaudet
challenged the covalent-vs-non-covalent framing of "cross-linking" and asked
for a supporting PMID before accepting a leaf term without a reference.

## Gold PR Assessment

PR #31911 (merged 2026-04-17, author @dragon-ai-agent) makes exactly the two
requested edits in `src/ontology/go-edit.obo`:

- Adds new MF term **GO:7770064** `actin-filament cross-linking activity`,
  `is_a: GO:0008093`, `has_part: GO:0051015 actin filament binding`, three
  EXACT synonyms (cross-linking / crosslinking spelling variants and
  `F-actin cross-linking activity`), the requested verbatim definition, and a
  `term_tracker_item` to #19185. The definition xref `PMID:37025173` was added
  in a follow-up commit to satisfy @pgaudet's request for a reference.
- Renames **GO:0008093**: primary label → `cytoskeletal adaptor activity`,
  with `cytoskeletal anchor activity` retained as a NARROW synonym, plus a new
  `term_tracker_item` for #19185.

The PR is well-formed, correctly scoped, and self-contained. The agent made a
defensible naming choice (hyphenated `actin-filament cross-linking activity`)
to avoid a label collision with the legacy obsolete GO:0003780
`actin cross-linking activity`, with the unhyphenated form kept as an EXACT
synonym. Validation (SPARQL QC, ELK reasoning) was run.

**Step 3a result:** `gh search prs` for "19185" returns only PR #31911 and an
unrelated 2017-era PR (#19203, "removed 3 digit exrefs ... per ticket 19185")
whose ticket number reference is a historical coincidence, not this NTR. The
deferred obsoletion of GO:0051764 was a deliberately separate future step that
the requester had not yet authorized at merge time, so PR #31911 is the
**complete human resolution of what was actually asked in this round**. Gold
is **sound** and is a single, coherent eval target.

One minor caveat for scorers: the merged term carries `created_by:
dragon-ai-agent` provenance and a `term_tracker_item`; metadiff normalizes
these, so a faithful future attempt may score F1 < 1.0 purely on
provenance/tracker convention differences — that is normal metadiff
under-representation, not a quality defect.

## Recommendation

Suitable for future eval runs. This is a good `hard` `new_term` case: it
combines a new-term creation with a coordinated parent-term label/synonym
swap, exercising naming-collision awareness and MF-vs-BP reasoning. Gold is
sound and complete for the round; no quality flag required.
