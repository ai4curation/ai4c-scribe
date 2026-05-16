---
ontology: go-ontology
issue_number: 31863
pr_number: 32012
case_type: obsoletion
difficulty: hard
num_agent_attempts: 0
agent_coverage: none
gold_assessment: partial
case_quality: poor
reviewed_by: claude-opus-4.7
reviewed_at: 2026-05-15
---

## Status

No agent attempts were generated for this case as of 2026-05-15. There is no
`attempts/` subdirectory and `num_agent_attempts: 0`. This is an
**eval-coverage gap, not an agent failure**. The deliverable is a case-level
assessment of the source issue, the gold PR, and dataset-readiness, plus
recording the no-attempt coverage gap. During this review a significant
**issue-to-gold-PR misattribution** was found (see Gold PR Assessment).

## Source Issue

Issue #31863 ("NTR: MF vesicle membrane tethering activity") is a **new-term
request**. It asks for a single new MF term `vesicle membrane tethering
activity` under GO:0140177 `membrane-membrane adaptor activity`, with a
supplied definition, PMID:19887069, a gene-product list, and a request to
extend GO:0140177's definition to include "vesicle". The curator
(@raymond91125) iterated in comments on the references and the GO:0140177 def
extension. The issue's entire scope is: create one MF term + extend one parent
definition.

## Gold PR Assessment

The selected gold PR #32012 ("Obsolete 5 vesicle tethering BP terms; rewire
complexes to new MF GO:7770062", merged 2026-04-29, @dragon-ai-agent) does
**not resolve issue #31863**. Its own body states it
"Closes/addresses: #31868, #31871, #31872, #31881" — a completely different
set of issues. PR #32012:

- Obsoletes 5 BP terms (GO:0099022 `vesicle tethering`, GO:0099069, GO:0090522,
  GO:0099041, GO:0099044) with `OBSOLETE.` def prefixes, `obsolete ` name
  prefixes, `is_obsolete: true`, `consider:` pointers (to GO:7770062 and
  process terms), `term_tracker_item`s, and rationale comments.
- Rewires 8 complex/CC terms (GO:0000145 exocyst, GO:0000938 GARP,
  GO:0017119 COG, GO:0030008 TRAPP, GO:0030897 HOPS, GO:0033263 CORVET,
  GO:0070939 Dsl1/NZR, GO:0099023) from `capable_of_part_of <obsoleted-BP>`
  to `capable_of GO:7770062 ! vesicle membrane tethering activity`.

**Step 3a result — issue/gold linkage is misattributed; gold is partial for
#31863.** The actual resolution of issue #31863 (the new-term request) is
**PR #31895** ("NTR: vesicle membrane tethering activity (GO:7770062) (fixes
#31863)"), which created GO:7770062 and extended GO:0140177's definition. PR
#32012 is a *downstream cascade* that consumes GO:7770062 to obsolete the
legacy BP terms for issues #31868/#31871/#31872/#31881. The case METADATA and
CASE_BRIEF link the case to issue #31863, but the gold PR neither creates the
requested term nor resolves #31863's asks.

Consequences for evaluation:

- An agent prompted with issue #31863 would correctly produce a new-term
  creation (≈ PR #31895), and would score ≈ F1 0 against the obsoletion-and-
  rewiring diff of PR #32012 — a structural artifact of the mislinked
  gold, not an agent failure.
- The gold PR #32012 is internally well-formed and ontologically sound *as an
  obsoletion-cascade PR*, but it is the wrong reference for issue #31863.

PR #32012 is itself good work, but as an eval case the issue→gold pairing is
broken: it is neither the whole nor a sub-step of issue #31863's resolution —
it resolves *other* issues. This is a `case_quality: poor`
(`gold_pr_wrong_issue`) situation. Companion/related PRs: #31895 (the true
resolution of #31863); #32012 actually belongs to issues #31868, #31871,
#31872, #31881.

## Recommendation

**Flag poor.** Do not use this case as-is for scoring. Two viable
remediations for a future curator: (a) re-pair the case so the gold is
**PR #31895** if the eval target is "resolve issue #31863" (new-term
creation); or (b) re-label the case so the prompt is the obsoletion-cascade
work and the issue references are corrected to #31868/#31871/#31872/#31881
(matching what #32012 actually does). Until re-paired, judge any future
attempt against the issue's actual ask (create GO:7770062 + extend GO:0140177)
and the union represented by #31895, not against #32012's metadiff.
