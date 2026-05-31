---
repo: obophenotype/cell-ontology
issue_number: 3559
pr_number: 3564
issue_title: "[Synonym] abbreviations like PBMC"
issue_created_at: "2026-01-23"
issue_closed_at: "2026-02-06"
pr_author: RiveraAndrea83
pr_merged_at: "2026-02-06"
pr_num_commits: 2
files_changed:
  - path: src/ontology/cl-edit.owl
    additions: 3
    deletions: 0
scoping: tightly_scoped
task_type: synonym_update
difficulty: simple
scope: multi_term
review_outcome: approved_first_time
domain_area: cell-biology
tags:
  - synonyms
  - abbreviations
  - PBMC
  - WBC
  - leukocyte
curated_by: claude-opus-4
curated_at: "2026-05-08"
rationale: Clean synonym addition case demonstrating how common abbreviations are added with appropriate synonym scope
case_quality: ok
case_quality_reason: metadiff_underrepresents_substance
companion_prs: []
scoring_caveat: "Gold PR #3564 is the sole, complete, curator-approved human resolution (all 3 synonyms). However all 3 gold lines carry Annotation(oboInOwl:hasDbXref \"PMID:...\") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) axiom annotations; both agent attempts added the correct 3 synonyms to the correct 3 terms with the correct exact scope but omitted the PMID xref + OMO synonym type, so metadiff F1=0.0 by construction. F1=0.0 here means partial_success (~70% correct substance), NOT failure. Also note: the CASE_BRIEF Context/Changes Made text understates the gold to 2 terms (PBMC, WBC) — the issue, curators, and gold PR all include RPE for CL:0002586 (3 terms total)."
quality_flagged_by: claude-opus-4.7
quality_flagged_at: "2026-05-16"
---

## Context

A community request asked for standard abbreviations to be added as synonyms for commonly referenced cell types. Specifically, PBMC (peripheral blood mononuclear cell) and WBC (white blood cell / leukocyte) are widely used abbreviations in clinical and research literature that were missing from the ontology.

## Changes Made

Added 3 exact synonym annotations to `cl-edit.owl`: "PBMC" for peripheral blood mononuclear cell (CL:2000001) with a literature reference, and "WBC" for leukocyte (CL:0000738). Each synonym includes appropriate database cross-references.

## Resolution

Approved on first review. This is a straightforward synonym addition requiring knowledge of OWL synonym annotation patterns (exact vs. related scope) and proper cross-referencing. An agent would need to identify the correct terms and apply the right synonym type with provenance.

## Curation Note (data quality)

Flagged by claude-opus-4.7 on 2026-05-16 during attempt review.

**Gold PR is valid and complete.** PR #3564 is the sole human resolution of
issue #3559: a single PR by RiveraAndrea83, approved first-time by dosumis,
adding all three requested synonyms. There are no companion PRs. The issue
explicitly requested PBMC, WBC, **and RPE**, and curators addiehl and scheuerm
confirmed all three (RPE specifically approved for CL:0002586). So this is NOT
a Step 3a multi-PR partial-gold case, and NOT a Step 3b poor case — gold is
correct, complete, in-scope, and curator-approved. `case_quality: ok`.

**Metadiff under-represents agent quality (scoring caveat).** All three gold
lines carry axiom annotations:
`AnnotationAssertion(Annotation(oboInOwl:hasDbXref "PMID:...") Annotation(oboInOwl:hasSynonymType obo:OMO_0003000) oboInOwl:hasExactSynonym obo:CL_xxxx "ABBR")`
— PMID:40794848 (WBC/CL:0000738), PMID:35835183 (RPE/CL:0002586),
PMID:27696124 (PBMC/CL:2000001). Both agent attempts (#210 sonnet-4.5, #149
haiku-4.5) added the correct three abbreviations to the correct three terms
with the correct `hasExactSynonym` scope, but as bare assertions without the
PMID xref or OMO_0003000 synonym type. Because zero agent lines match a gold
line byte-for-byte, metadiff returns F1=precision=recall=0.0 by construction.
This is a real omission (the issue asked for "reference(s)" and the
cl-agent-config CLAUDE.md demonstrates the exact OMO_0003000 pattern), so
both attempts are scored `partial_success` (~70% correct substance), not
`failure`. Aggregations should not read F1=0.0 here as "agent did nothing."

**CASE_BRIEF text inaccuracy (informational).** The auto-generated
CASE_BRIEF.md (and the Context/Changes Made prose mirrored above) describes
the gold as adding only PBMC and WBC (2 terms), omitting RPE for CL:0002586.
The actual gold PR diff and the issue both cover all three. CASE_BRIEF.md is
derived/auto-generated and was not edited; this note records the discrepancy
for downstream consumers.
