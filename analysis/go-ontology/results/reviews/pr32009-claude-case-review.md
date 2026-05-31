---
ontology: go-ontology
issue_number: 31963
pr_number: 32009
case_type: obsoletion
difficulty: simple
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
**eval-coverage gap, not an agent failure**. The deliverable is a case-level
assessment of the source issue, the gold PR, and dataset-readiness, plus
recording the no-attempt coverage gap.

## Source Issue

Issue #31963 ("Obsolete GO:0045550 geranylgeranyl reductase activity") reports
that GO:0045550 has no enzyme xref and describes the same reaction as the
existing GO:0102067 `geranylgeranyl diphosphate reductase activity`
(EC:1.3.1.83, RHEA:26229, PMID:9492312). The issue has three checkboxes: (1)
obsolete GO:0045550 and replace with GO:0102067; (2) update GO:0102067's
definition to match EC/RHEA wording; (3) add a sentence about
geranylgeranyl-chlorophyll a to GO:0102067's def. Only three annotations exist
on GO:0045550 (two human UniProt, one Arabidopsis).

The curator (@raymond91125) explicitly **sequenced the work in two requests**:
first "update GO:0102067 definition according to sjm41 comments. Do not close
this ticket. Obsoletion is to be completed later." Later: "please obsolete
GO:0045550."

## Gold PR Assessment

PR #32009 (merged 2026-04-28, author @dragon-ai-agent) implements the
obsoletion sub-task cleanly using the standard pattern in
`src/ontology/go-edit.obo`:

- GO:0045550: name → `obsolete geranylgeranyl reductase activity`; def
  prefixed `OBSOLETE.` (original text and `PMID:9492312` xref retained);
  `is_obsolete: true`; `replaced_by: GO:0102067`; explanatory `comment`;
  `term_tracker_item` for #31963; the sole `is_a: GO:0016491` axiom removed.

This is textbook obsoletion-with-replacement: a clean 1:1 mapping documented
in the issue, correct removal of logical axioms, correct `replaced_by` (safe
because the replacement is a same-namespace MF that already carries full
EC/RHEA axiomatization), and a rationale comment. The agent verified via
`obo-grep.pl` that no other stanza references GO:0045550, so no in-ontology
rewiring was needed. `make travis_build` passed.

**Step 3a result.** Issue #31963 was resolved across two PRs:

- **PR #32006** ("Update GO:0102067 definition per sjm41 comments (refs
  #31963)") — handled issue checkboxes 2 and 3 (the def/xref edits on the
  *replacement* term GO:0102067).
- **PR #32009** (this gold) — the obsoletion of GO:0045550 (checkbox 1, the
  issue title and primary ask).

Although technically a multi-PR resolution, the curator deliberately split it
into two independent, well-defined requests, and the obsoletion is the
issue's headline ask. PR #32009 is a complete, self-contained, correct
implementation of the obsoletion task — which is exactly what this case is
typed as (`obsoletion` / `single_term`). The companion PR #32006 edits a
*different* term (GO:0102067) and does not overlap. Gold is therefore
**sound** for the obsoletion eval target; the companion PR is noted for
completeness but does not make this a poor case.

## Recommendation

Suitable for future eval runs. Clean, canonical `simple` `obsoletion` case
with a documented 1:1 replacement and explicit curator authorization in the
issue thread. No quality flag required. Scorers should note the companion PR
#32006 exists but addresses a separate term and does not affect scoring of the
obsoletion target.
