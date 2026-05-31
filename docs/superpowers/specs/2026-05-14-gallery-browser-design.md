# Design: `ai4c-scribe gallery` — Static HTML Case Browser

## Summary

A new CLI command that generates a single self-contained HTML file for browsing evaluation case studies. The browser uses a sidebar-list + detail-pane layout (like a file browser or iPhoto), with cases grouped by ontology. It renders case metadata, narrative markdown, diffs, and agent attempt results — all from the `analysis/` directory tree.

## CLI Interface

```
ai4c-scribe gallery analysis/ -o gallery.html
```

- **Input**: path to analysis directory (contains `{ontology}/cases/`, `{ontology}/results/`)
- **Output**: single self-contained HTML file (`gallery.html` by default), all data embedded as JSON
- Opens in any browser, no server needed

### Arguments

| Argument | Type | Required | Default | Description |
|----------|------|----------|---------|-------------|
| `analysis_dir` | Path | yes | — | Analysis directory path |
| `--output / -o` | Path | no | `gallery.html` | Output HTML file path |

## Data Collection

The generator scans the analysis directory. There are two numbering schemes:

- **Source PR numbers**: used by cases and human diffs — these refer to the original repo (e.g., mondo PR #10202)
- **Eval repo PR numbers**: used by agent diffs — these refer to the shadow/eval repo (e.g., mondo-agent-config PR #428)

The `scores.tsv` file is the rosetta stone that maps between them.

### Sources

1. **Cases**: `{ont}/cases/pr{NUM}/METADATA.md` — keyed by source `pr_number`
2. **Human diffs**: `{ont}/results/diffs/human/pr{NUM}.diff` — keyed by source `pr_number`
3. **Agent diffs**: `{ont}/results/diffs/agent/pr{NUM}.diff` — keyed by `eval_repo_pr` (shadow repo PR number)
4. **Reviews**: `{ont}/results/reviews/pr{NUM}-*.md` — keyed by `eval_repo_pr`
5. **Scores**: `{ont}/results/scores.tsv` — contains both `pr_number` (source) and `eval_repo_pr` (shadow), plus model, runtime, f1, etc.

All sources are optional except cases — a case with no results simply shows metadata and narrative without the results sections.

### Joining Logic

1. Load all cases keyed by `(ontology, pr_number)`
2. Load `scores.tsv` — each row maps `(ontology, pr_number)` → `eval_repo_pr` + model/runtime/scores
3. For each score row, look up `diffs/agent/pr{eval_repo_pr}.diff` and `reviews/pr{eval_repo_pr}-*.md`
4. Group agent attempts under their parent case using `pr_number` from the scores row
5. A single case (e.g., mondo issue #9707, source PR #9745) may have many agent attempts across different models/runtimes, each with a different `eval_repo_pr`

### Data Model (embedded JSON)

```json
{
  "ontologies": {
    "mondo": {
      "cases": [
        {
          "pr_number": 9745,
          "ontology": "mondo",
          "metadata": {
            "repo": "monarch-initiative/mondo",
            "issue_number": 9707,
            "issue_title": "Reclassify ...",
            "task_type": "new_term",
            "difficulty": "hard",
            "scoping": "tightly_scoped",
            "scope": "single_term",
            "review_outcome": "approved_first_time",
            "pr_author": "...",
            "pr_merged_at": "2026-03-30",
            "curated_by": "claude-opus-4",
            "rationale": "..."
          },
          "narrative_md": "## Context\n\n...",
          "human_diff": "diff --git a/src/ontology/mondo-edit.obo ...",
          "agent_attempts": [
            {
              "eval_repo_pr": 427,
              "model": "claude-haiku-4.5",
              "runtime": "claude",
              "agent_config_tag": "v3",
              "agent": "std_claude_hai45",
              "f1": 0.216,
              "precision": 0.167,
              "recall": 0.308,
              "jaccard": 0.121,
              "diff": "diff --git ...",
              "review_md": null
            },
            {
              "eval_repo_pr": 407,
              "model": "claude-opus-4.7",
              "runtime": "claude",
              "agent_config_tag": "v3",
              "agent": "claude/claude-opus-4.7/v3",
              "f1": 0.311,
              "precision": 0.292,
              "recall": 0.333,
              "jaccard": 0.184,
              "diff": "diff --git ...",
              "review_md": "## Summary\n..."
            },
            {
              "eval_repo_pr": 261,
              "model": "kimi-k2.6",
              "runtime": "opencode",
              "agent_config_tag": "v3",
              "agent": "opencode/kimi-k2.6/v3",
              "f1": 0.615,
              "precision": 0.5,
              "recall": 0.8,
              "jaccard": 0.444,
              "diff": "diff --git ...",
              "review_md": null
            }
          ]
        }
      ]
    }
  }
}
```

## Layout

### Sidebar (left, ~280px, fixed height)

- **Filter input** at top — searches across issue_title, PR number, task_type
- **Collapsible ontology groups** — each headed by ontology name + case count badge
- **Case items** within each group:
  - `PR#{num}` in monospace, compact
  - Truncated `issue_title` (ellipsis overflow)
  - Difficulty color dot: green (simple), amber (medium), red (hard)
- Active case highlighted with accent background
- Keyboard navigation: up/down arrows move selection, Enter opens case

### Detail Pane (right, scrollable)

Sections rendered top-to-bottom:

1. **Header**: PR number, full issue title, GitHub links (issue + PR, constructed from repo/number)
2. **Metadata badges**: task_type, difficulty, scoping, review_outcome, scope, pr_author — styled as colored pills/tags
3. **Narrative body**: markdown rendered to HTML (Context, Changes Made, Resolution sections from the METADATA.md body)
4. **Human diff** (collapsible, collapsed by default): syntax-highlighted unified diff (green additions, red deletions, grey context)
5. **Agent Attempts** (collapsible, collapsed by default):
   - Sub-entry per agent run, identified by `model/runtime` (e.g., "claude-haiku-4.5 / claude")
   - Linked to source case via `scores.tsv` mapping (`pr_number` → `eval_repo_pr`)
   - Each shows: model name, runtime, eval PR link, score badges (f1, precision, recall, jaccard)
   - Expandable diff viewer per attempt (loaded from `diffs/agent/pr{eval_repo_pr}.diff`)
   - Expandable review text per attempt (loaded from `reviews/pr{eval_repo_pr}-*.md`)

Empty sections are hidden (e.g., if no agent attempts exist for a case, that section doesn't appear).

## Architecture

### New Files

- `src/ai4c_scribe/gallery.py` — data collection logic + HTML generation

### Modified Files

- `src/ai4c_scribe/cli.py` — add `gallery` command (thin wrapper)

### Implementation Approach

- `gallery.py` contains:
  - `collect_gallery_data(analysis_dir: Path) -> dict` — walks the directory tree, parses METADATA.md frontmatter+body, reads diffs, parses scores TSV, assembles the JSON structure
  - `generate_gallery(analysis_dir: Path, output: Path) -> Path` — calls collect, renders HTML template, writes file
- HTML template is a Python string constant in `gallery.py` with embedded CSS and JS
- Markdown rendering: use `marked.js` (~40KB) inlined in the HTML for client-side rendering
- Diff highlighting: CSS-only (lines starting with `+` get green background, `-` get red, `@@` get blue)
- All case data embedded as `<script id="gallery-data" type="application/json">...</script>`
- JS on page load: parse JSON, build sidebar, render first case, wire up click/keyboard handlers

### Dependencies

No new Python dependencies. The HTML is self-contained with inlined JS/CSS.

## Extensibility

The JSON data model has optional fields throughout. As new result types appear in `analysis/*/results/`:
- Add them to `collect_gallery_data()` scan
- Add a rendering section in the HTML template
- Sections with no data are automatically hidden

This means the gallery gracefully handles partial data — cases with only metadata, cases with human diffs but no agent attempts, cases with full results, etc.

## Testing

- `test_gallery.py`:
  - Test `collect_gallery_data()` with a fixture directory containing sample METADATA.md, diffs, scores.tsv
  - Test that `generate_gallery()` produces valid HTML containing expected case data
  - Test that missing optional data (no diffs, no scores) doesn't error
- Doctests in `gallery.py` for helper functions (frontmatter parsing reuse, diff line classification)
