"""Scores overview analysis for the ontology agent evaluation paper."""

from pathlib import Path
import pandas as pd

from ai4c_scribe.analysis import (
    load_scores,
    load_reviews,
    summary_by_model,
    summary_by_runtime,
    pivot_scores,
    rubric_summary,
    outcome_distribution,
    failure_mode_counts,
)

# Load data
df = load_scores(Path("analysis/scores.tsv"))
reviews = load_reviews()

print(f"# Ontology Agent Evaluation — Scores Overview")
print(f"\n{len(df)} scored runs across {df['ontology'].nunique()} ontologies, "
      f"{df['model'].nunique()} models, {df['runtime'].nunique()} runtimes")
print(f"\n{len(reviews)} qualitative reviews completed")

# --- Section 1: Model comparison ---
print("\n## F1 Scores by Model\n")
print(summary_by_model(df).to_html())

print("\n## F1 Scores by Runtime\n")
print(summary_by_runtime(df).to_html())

# --- Section 2: Pivot tables ---
print("\n## Mean F1: Ontology x Model\n")
print(pivot_scores(df, rows="ontology", cols="model").to_html(na_rep="—"))

print("\n## Mean F1: Difficulty x Model\n")
print(pivot_scores(df, rows="difficulty", cols="model").to_html(na_rep="—"))

print("\n## Mean F1: Task Type x Runtime\n")
print(pivot_scores(df, rows="case_type", cols="runtime").to_html(na_rep="—"))

# --- Section 3: Config ablation ---
print("\n## Skills Ablation (GO + Mondo)\n")
ablation = df[df["agent_config_tag"].isin(["v8", "v8-noskills", "v9", "v2", "v2-noskills", "v3"])]
print(pivot_scores(ablation, rows="agent_config_tag", cols="runtime").to_html(na_rep="—"))

# --- Section 4: Non-zero analysis ---
nonzero = df[df["f1"] > 0]
print(f"\n## Non-zero Results Only ({len(nonzero)}/{len(df)} runs)\n")
print(summary_by_model(nonzero).to_html())

# --- Section 5: All runs detail ---
print("\n## All Scored Runs\n")
cols = ["ontology", "issue_number", "case_type", "difficulty", "agent_config_tag", "model", "runtime", "f1", "precision", "recall"]
print(df[cols].sort_values(["ontology", "issue_number", "model"]).to_html(index=False, float_format="%.3f"))

# --- Section 6: Reviews ---
if len(reviews) > 0:
    print("\n## Qualitative Reviews\n")
    print(f"\n### Rubric Scores by Model\n")
    rs = rubric_summary(reviews)
    if rs is not None:
        print(rs.to_html())

    print(f"\n### Outcome Distribution\n")
    od = outcome_distribution(reviews)
    if od is not None:
        print(od.to_html())

    print(f"\n### Failure Modes\n")
    fm = failure_mode_counts(reviews)
    if fm is not None:
        print(fm.to_frame("count").to_html())
