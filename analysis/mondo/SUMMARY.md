# Mondo-Level Evaluation Summary

## Scope

The Mondo evaluation set contains 40 case directories and 382 scored agent
attempts using the `v3` Mondo agent configuration. Only 37 human PRs are scored
directly: PRs #10107, #10108, and #10109 are companion human PRs for the same
OMIM-merge issue as scored PR #10110, and are present as case context rather
than separate score rows.

The case set is broad:

| Dimension | Distribution |
| --- | --- |
| Difficulty | 17 simple, 18 medium, 5 hard |
| Scope | 33 single-term, 6 multi-term, 1 structural refactor |
| Scoping | 37 tightly scoped, 3 loosely scoped |
| Review outcome | 28 approved first time, 12 required changes |
| Task type | 12 new term, 10 synonym update, 8 obsoletion, 5 other, 3 reclassification, 1 axiom repair, 1 bulk edit |

## Bottom Line

Mondo did not turn out to be impossible, but it did turn out to be much messier
than a pure line-diff benchmark. At the ontology level, the set is useful because
it captures real disease-curation work: obsoletions, merges, synonym scope
decisions, new term creation, xref cleanup, disease-gene conventions, and
evidence/provenance judgment. Those are exactly the things an ontology agent has
to handle.

The caveat is that raw metadiff F1 is not enough. Many Mondo cases are good
qualitative tests of agent behavior, but a substantial fraction have some
combination of incomplete gold, reviewer-only decisions, private curator
judgment, scope expansion, issue/gold mismatch, or provenance details that no
single-shot agent could reliably infer from the issue text. The right conclusion
is:

- Mondo is a realistic, high-friction benchmark.
- It should not be treated as a clean leaderboard without case-level
  adjudication.
- Low F1 often identifies a real failure, but sometimes identifies a mismatch
  between the issue, the final human PR, and the metric.

## What Mondo Tests Well

The strongest Mondo cases are the ones where the issue text and final human PR
align closely. In those cases, metadiff generally tracks quality. The best
examples are narrow axiom repairs, ordinary obsoletions, small xref fixes,
straightforward synonym additions, and single-term edits with explicit requested
content.

These cases test useful capabilities:

- finding the correct disease term and editing the right stanza;
- preserving Mondo OBO syntax and stanza conventions;
- using the right obsoletion or merge workflow;
- carrying tracker provenance and xref source qualifiers;
- applying synonym scope carefully, especially `EXACT` vs `RELATED`;
- using Mondo-specific annotations such as `MONDO:equivalentObsolete`,
  `replaced_by`, `consider`, and ClinGen `OMO:0002001`.

When the task was explicit and mechanically bounded, agents often produced
substantively good work. Obsoletion cases and axiom-repair cases were especially
tractable. New-term cases were mixed but often partially successful when the
agent captured the label, parentage, xrefs, definition, and basic provenance.

## What Made Mondo Hard

The hard part was rarely plain syntax. The hard part was curatorial judgment.
Agents struggled when a case required them to decide whether a PMID really
supported the term, whether an upstream disease concept had already been merged,
whether an apparent new term was actually an existing disease under another
label, or whether a requested synonym should be exact, related, historical, or
ClinGen-preferred.

The most common substantive failure modes were:

- under-editing: doing the obvious local edit but missing required companion
  changes;
- over-editing: adding plausible but unrequested ontology changes;
- wrong workflow: treating a merge as a simple obsoletion, or vice versa;
- missing Mondo metadata: term trackers, creator ORCIDs, synonym annotations,
  source qualifiers, and obsolete-equivalence markers;
- weak evidence handling: accepting bad PMIDs, missing supplied sources, or
  inventing/omitting provenance;
- synonym-scope errors: especially around ClinGen gene-centric disease names and
  historical disease labels.

These are real ontology-agent problems, not artifacts. Mondo is therefore useful
for studying whether agents can behave like curators rather than just patch
files.

## Where The Benchmark Is Messy

Several cases should be down-weighted or excluded from raw aggregate scoring.
They are still informative, but they are not clean gold-standard line-diff
targets.

The clearest poor or gold-mismatched cases include:

- #10110: the scored gold PR is only one of four PRs that resolved issue #9795.
  Agents that correctly performed all four requested OMIM merges are penalized
  as over-editing against the selected single-PR gold.
- #10117: the issue asks for a narrow synonym fix, while the gold PR is a
  5,103-line ontology-wide synonym purge. Correct narrow fixes are capped near
  zero F1 by construction.
- #10123: the gold PR uses a minimal model, while the documented
  susceptibility-by-gene design pattern calls for richer logical axioms.
  Pattern-faithful agents are penalized for following the prescribed pattern.
- #10102: the gold obsoletion leaves a dangling `replaced_by` reference to the
  newly obsolete term. Agents that repair that dangling reference are penalized
  for an extra but valid edit.
- #10201, #10206, #10207, and #10208: the final human PRs include scope
  expansions, curator reinterpretations, or provenance choices that are not
  fully recoverable from the issue text.

The important distinction is that these cases are not all "impossible" in the
same way. Some are genuinely poor gold references. Some are good curation
stories but bad raw metadiff targets. Some reveal realistic ambiguity that an
agent should flag rather than silently decide.

## Metadiff And ID Masking

OBO metadiff masks CURIE IDs, including primary `id:` lines. This was verified
directly on Mondo #10084 and #10126: normalized common changes include
`id: MONDO:NNNNNNN`. Therefore, a placeholder `MONDO:777xxxx` primary ID is not
by itself a raw F1 penalty.

That correction matters. Earlier case notes that attribute low F1 mainly to the
primary ID mismatch should be interpreted cautiously. The remaining score loss
in those cases comes from other differences: definition wording, comments,
source and evidence annotations, creator ORCIDs, synonym form, insertion context,
and surrounding stanza changes. ID-related scoring caveats still exist, but the
primary ID line alone is not the explanation.

## Scores

Across all 382 scored attempts, mean F1 is 0.452 and median F1 is 0.431.

Runtime-level performance:

| Runtime | Attempts | Mean F1 | Median F1 |
| --- | ---: | ---: | ---: |
| claude | 141 | 0.396 | 0.385 |
| opencode | 111 | 0.519 | 0.500 |
| codex | 84 | 0.479 | 0.462 |
| copilot | 46 | 0.412 | 0.376 |

For `gpt-5.5` on Codex specifically, there are 41 attempts with mean F1 0.464
and median F1 0.455. The manual review outcomes for those attempts are 3
successes, 30 partial successes, and 8 failures.

Manual review outcomes across all 382 Mondo attempts:

| Outcome | Attempts | Mean F1 | Median F1 |
| --- | ---: | ---: | ---: |
| success | 36 | 0.963 | 0.968 |
| partial_success | 257 | 0.503 | 0.500 |
| failure | 89 | 0.100 | 0.095 |

Case-level mean F1 also shows the ontology-specific pattern. Axiom repair and
obsoletion were the most tractable categories, while synonym update,
reclassification, and the one bulk-edit case were much less reliable under raw
metadiff:

| Case Type | Scored Cases | Mean Case F1 |
| --- | ---: | ---: |
| axiom_repair | 1 | 0.921 |
| obsoletion | 5 | 0.667 |
| other | 5 | 0.538 |
| new_term | 12 | 0.446 |
| synonym_update | 10 | 0.302 |
| reclassification | 3 | 0.294 |
| bulk_edit | 1 | 0.003 |

## Interpretation

Mondo should be analyzed with case-level adjudication layered on top of metadiff.
Raw F1 remains useful as a triage signal, but it compresses several different
phenomena into the same number:

- genuine agent failure;
- correct work against a partial or scope-mismatched gold PR;
- defensible curation choices that differ from the human curator's wording;
- missing reviewer-dialogue changes that were not available in the original
  issue;
- missing Mondo-specific metadata and provenance details.

For downstream evaluation, the cleanest approach is to separate cases into three
buckets:

1. clean benchmark cases where issue, gold, and metric align;
2. scoring-caveated cases where metadiff under-represents plausible good work;
3. poor gold cases where raw F1 should be excluded or heavily down-weighted.

At the level of Mondo itself, the main lesson is that disease ontology curation
is learnable but not reducible to textual patch matching. The benchmark is
valuable precisely because it exposes that gap.
