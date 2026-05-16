---
ontology: go-ontology
repo: geneontology/go-ontology
issue_number: 31670
pr_number: 31676
issue_title: 'Taxon constraint: please add for GO:0070478 and similar terms'
pr_author: pgaudet
pr_merged_at: '2026-04-20'
task_type: new_term
difficulty: hard
scoping: mostly_scoped
scope: multi_term
review_outcome: multiple_rounds
num_agent_attempts: 10
generated_at: '2026-05-15'
scoping_notes: Primary goal was adding taxon constraints for specific terms. Also
  fixed a formatting error in the migrasome entry (extra NCBITaxon column) which was
  incidental cleanup.
domain_area: biological_process
best_f1: 0.571
best_model: kimi-k2.6
---

# PR #31676 — Taxon constraint: please add for GO:0070478 and similar terms

**go-ontology** | [geneontology/go-ontology](https://github.com/geneontology/go-ontology) | [Issue #31670](https://github.com/geneontology/go-ontology/issues/31670) | [PR #31676](https://github.com/geneontology/go-ontology/pull/31676) | @pgaudet | merged 2026-04-20

`new_term` `hard` `mostly_scoped` `multiple_rounds`

## Context

A request was made to add "only_in_taxon" constraints for GO:0070478 and related terms. Taxon constraints restrict which organisms a GO term can be applied to (e.g., "maternal mRNA clearance" only makes sense in Eukaryota). The issue was closed quickly but the PR took 6 weeks to merge due to iterative review.

## Changes Made

In `src/taxon_constraints/only_in_taxon.tsv`:

**Added taxon constraints** (Eukaryota-only):
- GO:0141065 "maternal mRNA clearance" -> NCBITaxon:2759 (Eukaryota)
- GO:0000958 "mitochondrial mRNA catabolic process" -> NCBITaxon:2759 (Eukaryota)
- GO:0000956 "nuclear-transcribed mRNA catabolic process" -> NCBITaxon:2759 (Eukaryota)

**Fixed formatting**:
- GO:0140494 "migrasome": corrected malformed entry that had an extra NCBITaxon:7742 column

## Resolution

The PR went through 3 rounds of formal review over 10 commits. Key discussion points:
1. Whether "mitochondrial mRNA catabolic process" should be Eukaryota-only (bacteria have different mRNA degradation machinery but the term specifically refers to mitochondrial context)
2. Whether to add constraints to parent terms or only leaf terms
3. Formatting of the TSV entries (evidence column with PMIDs)

Hard difficulty because taxon constraint decisions require biological reasoning about which organisms possess the relevant cellular machinery, and reviewers disagreed on scope.

## Human Diff

```diff
diff --git a/src/taxon_constraints/only_in_taxon.tsv b/src/taxon_constraints/only_in_taxon.tsv
index 3266d81e16..e3ab62640b 100644
--- a/src/taxon_constraints/only_in_taxon.tsv
+++ b/src/taxon_constraints/only_in_taxon.tsv
@@ -941,7 +941,7 @@ GO:0044311	exoneme	NCBITaxon:2759	Eukaryota
 GO:0061468	karyomere	NCBITaxon:2759	Eukaryota	
 GO:0070074	mononeme	NCBITaxon:2759	Eukaryota	
 GO:0071212	subsynaptic reticulum	NCBITaxon:2759	Eukaryota	
-GO:0140494	migrasome	NCBITaxon:7742	NCBITaxon:2759	Eukaryota  PMID:40712579|PMID:25342562
+GO:0140494	migrasome	NCBITaxon:2759	Eukaryota	PMID:40712579|PMID:25342562
 GO:0160045	TMEM240-body	NCBITaxon:2759	Eukaryota	
 GO:0160201	polaroplast	NCBITaxon:2759	Eukaryota	
 GO:0160208	fibrous body-membranous organelle	NCBITaxon:6231	Nematoda	
@@ -949,5 +949,8 @@ GO:1990413	eyespot apparatus	NCBITaxon:2759	Eukaryota
 GO:1990462	omegasome	NCBITaxon:2759	Eukaryota	
 GO:0019905	syntaxin binding	NCBITaxon:2	Bacteria	
 GO:0098795	global gene silencing by mRNA cleavage	NCBITaxon:2	Bacteria	
+GO:0141065	maternal mRNA clearance	NCBITaxon:2759	Eukaryota	
+GO:0000958	mitochondrial mRNA catabolic process	NCBITaxon:2759	Eukaryota	
+GO:0000956	nuclear-transcribed mRNA catabolic process	NCBITaxon:2759	Eukaryota	
 GO:0140400	embryonic sheath	NCBITaxon:6231	Nematoda	PMID:28526752
 GO:0019658	bifid shunt	NCBITaxon:2	Bacteria	

```

## Agent Attempts (10)

| # | Model | Runtime | F1 | P | R | Blob | Eval PR | Detail |
|---|-------|---------|-----|-----|-----|------|---------|--------|
| 1 | kimi-k2.6 | opencode | 0.571 | 0.400 | 1.000 | `3b53a69` | [#263](https://github.com/ai4curation/eval-ont-agent-go/pull/263) | [attempt](attempts/pr263.md) |
| 2 | gpt-5.4 | codex | 0.571 | 0.400 | 1.000 | `f9cc0a6` | [#177](https://github.com/ai4curation/eval-ont-agent-go/pull/177) | [attempt](attempts/pr177.md) |
| 3 | claude-sonnet-4.5 | claude | 0.011 | 0.800 | 0.006 | `768023b` | [#470](https://github.com/ai4curation/eval-ont-agent-go/pull/470) | [attempt](attempts/pr470.md) |
| 4 | claude-sonnet-4.5 | copilot | 0.006 | 0.400 | 0.003 | `33dfe93` | [#385](https://github.com/ai4curation/eval-ont-agent-go/pull/385) | [attempt](attempts/pr385.md) |
| 5 | gpt-5.5 | opencode | 0.005 | 0.400 | 0.002 | `048e8a8` | [#92](https://github.com/ai4curation/eval-ont-agent-go/pull/92) | [attempt](attempts/pr92.md) |
| 6 | gpt-5.5 | opencode | 0.005 | 0.400 | 0.002 | `048e8a8` | [#67](https://github.com/ai4curation/eval-ont-agent-go/pull/67) | [attempt](attempts/pr67.md) |
| 7 | gpt-5.5 | codex | 0.005 | 0.400 | 0.002 | `048e8a8` | [#64](https://github.com/ai4curation/eval-ont-agent-go/pull/64) | [attempt](attempts/pr64.md) |
| 8 | claude-sonnet-4.5 | copilot | 0.000 | 0.000 | 0.000 | `7602abc` | [#413](https://github.com/ai4curation/eval-ont-agent-go/pull/413) | [attempt](attempts/pr413.md) |
| 9 | claude-opus-4.7 | claude | 0.000 | 0.000 | 0.000 | `fcd6636` | [#328](https://github.com/ai4curation/eval-ont-agent-go/pull/328) | [attempt](attempts/pr328.md) |
| 10 | claude-haiku-4.5 | claude | 0.000 | 0.000 | 0.000 | `b6e9be2` | [#199](https://github.com/ai4curation/eval-ont-agent-go/pull/199) | [attempt](attempts/pr199.md) |
