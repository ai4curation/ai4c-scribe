"""Scores overview analysis.

Run with: uv run marimo edit analysis/notebooks/01_scores_overview.py
Or as script: uv run python analysis/notebooks/01_scores_overview.py
"""
# %% Imports
from pathlib import Path
import pandas as pd

from ai4c_scribe.analysis import (
    load_scores,
    summary_by_model,
    summary_by_runtime,
    pivot_scores,
)

# %% Load data
df = load_scores(Path("analysis/scores.tsv"))
print(f"Loaded {len(df)} scored runs across {df['ontology'].nunique()} ontologies")
print(f"Models: {sorted(df['model'].unique())}")
print(f"Runtimes: {sorted(df['runtime'].unique())}")
print()

# %% Summary by model
print("=== F1 by Model ===")
print(summary_by_model(df))
print()

# %% Summary by runtime
print("=== F1 by Runtime ===")
print(summary_by_runtime(df))
print()

# %% Pivot: ontology x model
print("=== Mean F1: Ontology x Model ===")
print(pivot_scores(df, rows="ontology", cols="model"))
print()

# %% Pivot: difficulty x model
print("=== Mean F1: Difficulty x Model ===")
print(pivot_scores(df, rows="difficulty", cols="model"))
print()

# %% Pivot: task_type x runtime
print("=== Mean F1: Task Type x Runtime ===")
print(pivot_scores(df, rows="case_type", cols="runtime"))
print()

# %% Config ablation
print("=== Skills Ablation ===")
ablation = df[df["agent_config_tag"].str.contains("noskills|v8$|v9$|v2$|v3$", regex=True, na=False)]
print(pivot_scores(ablation, rows="agent_config_tag", cols="runtime"))
print()

# %% Non-zero results only
print("=== Non-zero F1 results ===")
nonzero = df[df["f1"] > 0]
print(f"{len(nonzero)} of {len(df)} runs produced non-zero F1")
print(summary_by_model(nonzero))
