# Gallery Browser Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add an `ai4c-scribe gallery` CLI command that generates a single self-contained HTML file for browsing evaluation case studies with a sidebar-list + detail-pane layout.

**Architecture:** A new `gallery.py` module handles data collection (walking the analysis directory tree, parsing METADATA.md, reading diffs, joining scores.tsv) and HTML generation (embedding all data as JSON in a single HTML file with inlined CSS/JS). The CLI in `cli.py` gets a thin `gallery` command wrapper. The HTML uses marked.js for client-side markdown rendering and CSS-only diff highlighting.

**Tech Stack:** Python (yaml, csv, json, pathlib), HTML/CSS/JS (marked.js CDN-inlined), no new Python dependencies.

**Spec:** `docs/superpowers/specs/2026-05-14-gallery-browser-design.md`

---

### Task 1: Test fixtures for gallery data collection

Create a minimal fixture directory that mirrors the real `analysis/` layout with one ontology, two cases, scores, diffs, and a review file.

**Files:**
- Create: `tests/fixtures/gallery/test-ont/cases/pr100/METADATA.md`
- Create: `tests/fixtures/gallery/test-ont/cases/pr200/METADATA.md`
- Create: `tests/fixtures/gallery/test-ont/results/scores.tsv`
- Create: `tests/fixtures/gallery/test-ont/results/diffs/human/pr100.diff`
- Create: `tests/fixtures/gallery/test-ont/results/diffs/human/pr200.diff`
- Create: `tests/fixtures/gallery/test-ont/results/diffs/agent/pr10.diff`
- Create: `tests/fixtures/gallery/test-ont/results/diffs/agent/pr11.diff`
- Create: `tests/fixtures/gallery/test-ont/results/diffs/agent/pr12.diff`
- Create: `tests/fixtures/gallery/test-ont/results/reviews/pr10-claudecode-complete.md`

- [ ] **Step 1: Create case METADATA.md fixtures**

`tests/fixtures/gallery/test-ont/cases/pr100/METADATA.md`:
```markdown
---
repo: test-org/test-ont
issue_number: 90
pr_number: 100
issue_title: "Add new term: foo bar"
issue_created_at: "2026-01-01"
pr_author: alice
pr_merged_at: "2026-01-15"
pr_num_commits: 2
files_changed:
  - path: src/ontology/test.obo
    additions: 10
    deletions: 0
scoping: tightly_scoped
task_type: new_term
difficulty: simple
scope: single_term
review_outcome: approved_first_time
curated_by: claude-opus-4
curated_at: "2026-05-01"
rationale: Simple new term addition
---

## Context

Issue requested a new term for foo bar.

## Changes Made

Added the term with proper definition.

## Resolution

Approved on first review.
```

`tests/fixtures/gallery/test-ont/cases/pr200/METADATA.md`:
```markdown
---
repo: test-org/test-ont
issue_number: 190
pr_number: 200
issue_title: "Reclassify baz widget"
issue_created_at: "2026-02-01"
pr_author: bob
pr_merged_at: "2026-02-20"
pr_num_commits: 4
files_changed:
  - path: src/ontology/test.obo
    additions: 5
    deletions: 3
scoping: tightly_scoped
task_type: reclassification
difficulty: hard
scope: single_term
review_outcome: changes_requested
curated_by: claude-opus-4
curated_at: "2026-05-01"
rationale: Complex reclassification requiring domain knowledge
---

## Context

Issue requested reclassification of baz widget.

## Changes Made

Moved baz widget under new parent.

## Resolution

Reviewer requested changes to parent term placement.
```

- [ ] **Step 2: Create scores.tsv fixture**

`tests/fixtures/gallery/test-ont/results/scores.tsv` — two agent attempts for pr100 and one for pr200:
```tsv
ontology	issue_number	pr_number	case_type	difficulty	agent_config_tag	model	runtime	eval_repo_pr	f1	precision	recall	jaccard	case	agent
test-ont	90	100	new_term	simple	v3	claude-haiku-4.5	claude	10	0.8	0.667	1.0	0.667	test#90	std_claude_hai45
test-ont	90	100	new_term	simple	v3	claude-opus-4.7	claude	11	0.95	0.9	1.0	0.9	test#90	claude/claude-opus-4.7/v3
test-ont	190	200	reclassification	hard	v3	claude-haiku-4.5	claude	12	0.3	0.25	0.4	0.2	test#190	std_claude_hai45
```

- [ ] **Step 3: Create diff fixtures**

`tests/fixtures/gallery/test-ont/results/diffs/human/pr100.diff`:
```diff
diff --git a/src/ontology/test.obo b/src/ontology/test.obo
index aaa..bbb 100644
--- a/src/ontology/test.obo
+++ b/src/ontology/test.obo
@@ -100,0 +101,5 @@
+[Term]
+id: TEST:0001
+name: foo bar
+def: "A foo bar thing." [PMID:12345]
+is_a: TEST:0000
```

`tests/fixtures/gallery/test-ont/results/diffs/human/pr200.diff`:
```diff
diff --git a/src/ontology/test.obo b/src/ontology/test.obo
index ccc..ddd 100644
--- a/src/ontology/test.obo
+++ b/src/ontology/test.obo
@@ -50,3 +50,3 @@
-is_a: TEST:0010
+is_a: TEST:0020
```

`tests/fixtures/gallery/test-ont/results/diffs/agent/pr10.diff`:
```diff
diff --git a/src/ontology/test.obo b/src/ontology/test.obo
--- a/src/ontology/test.obo
+++ b/src/ontology/test.obo
@@ -100,0 +101,4 @@
+[Term]
+id: TEST:0099
+name: foo bar
+is_a: TEST:0000
```

`tests/fixtures/gallery/test-ont/results/diffs/agent/pr11.diff`:
```diff
diff --git a/src/ontology/test.obo b/src/ontology/test.obo
--- a/src/ontology/test.obo
+++ b/src/ontology/test.obo
@@ -100,0 +101,5 @@
+[Term]
+id: TEST:0001
+name: foo bar
+def: "A foo bar." [PMID:12345]
+is_a: TEST:0000
```

`tests/fixtures/gallery/test-ont/results/diffs/agent/pr12.diff`:
```diff
diff --git a/src/ontology/test.obo b/src/ontology/test.obo
--- a/src/ontology/test.obo
+++ b/src/ontology/test.obo
@@ -50,3 +50,3 @@
-is_a: TEST:0010
+is_a: TEST:0030
```

- [ ] **Step 4: Create review fixture**

`tests/fixtures/gallery/test-ont/results/reviews/pr10-claudecode-complete.md`:
```markdown
---
ontology: test-ont
issue_number: 90
pr_number: 100
eval_repo_pr: 10
model: claude-haiku-4.5
runtime: claude
f1: 0.8
outcome: partial_success
reviewed_by: claude-opus-4
reviewed_at: "2026-05-09"
---

## Summary

The agent created the term but missed the definition.

## Detailed Analysis

Missing def line compared to human PR.
```

- [ ] **Step 5: Commit**

```bash
git add tests/fixtures/gallery/
git commit -m "test: add gallery fixture data for gallery browser tests"
```

---

### Task 2: `collect_gallery_data()` — data collection with tests

Implement the core data collection function that walks the analysis directory tree, parses all sources, and produces the JSON-ready dict.

**Files:**
- Create: `tests/test_gallery.py`
- Create: `src/ai4c_scribe/gallery.py`

- [ ] **Step 1: Write failing tests for data collection**

`tests/test_gallery.py`:
```python
"""Tests for gallery browser generation."""

from pathlib import Path

from ai4c_scribe.gallery import collect_gallery_data


FIXTURE_DIR = Path("tests/fixtures/gallery")


def test_collect_discovers_ontologies():
    """Discovers ontology directories that contain cases/."""
    data = collect_gallery_data(FIXTURE_DIR)
    assert "test-ont" in data["ontologies"]


def test_collect_loads_cases():
    """Loads case metadata and narrative from METADATA.md."""
    data = collect_gallery_data(FIXTURE_DIR)
    cases = data["ontologies"]["test-ont"]["cases"]
    assert len(cases) == 2

    # Find pr100 case
    pr100 = next(c for c in cases if c["pr_number"] == 100)
    assert pr100["metadata"]["issue_title"] == "Add new term: foo bar"
    assert pr100["metadata"]["difficulty"] == "simple"
    assert pr100["metadata"]["task_type"] == "new_term"
    assert "Issue requested a new term" in pr100["narrative_md"]


def test_collect_loads_human_diffs():
    """Loads human diffs matched by source pr_number."""
    data = collect_gallery_data(FIXTURE_DIR)
    pr100 = next(
        c for c in data["ontologies"]["test-ont"]["cases"]
        if c["pr_number"] == 100
    )
    assert pr100["human_diff"] is not None
    assert "+name: foo bar" in pr100["human_diff"]


def test_collect_joins_agent_attempts_via_scores():
    """Agent attempts are joined through scores.tsv eval_repo_pr."""
    data = collect_gallery_data(FIXTURE_DIR)
    pr100 = next(
        c for c in data["ontologies"]["test-ont"]["cases"]
        if c["pr_number"] == 100
    )
    # pr100 has 2 agent attempts (eval_repo_pr 10 and 11)
    assert len(pr100["agent_attempts"]) == 2
    models = {a["model"] for a in pr100["agent_attempts"]}
    assert models == {"claude-haiku-4.5", "claude-opus-4.7"}

    # Check scores are attached
    haiku = next(a for a in pr100["agent_attempts"] if a["model"] == "claude-haiku-4.5")
    assert haiku["eval_repo_pr"] == 10
    assert haiku["f1"] == 0.8
    assert haiku["diff"] is not None
    assert "+name: foo bar" in haiku["diff"]


def test_collect_attaches_review_md():
    """Review markdown is attached to matching agent attempt."""
    data = collect_gallery_data(FIXTURE_DIR)
    pr100 = next(
        c for c in data["ontologies"]["test-ont"]["cases"]
        if c["pr_number"] == 100
    )
    haiku = next(a for a in pr100["agent_attempts"] if a["model"] == "claude-haiku-4.5")
    assert haiku["review_md"] is not None
    assert "missed the definition" in haiku["review_md"]


def test_collect_case_without_results():
    """Cases with no scores/diffs still load with empty agent_attempts."""
    # Create a minimal fixture with no results dir
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        case_dir = tmp_path / "myont" / "cases" / "pr999"
        case_dir.mkdir(parents=True)
        (case_dir / "METADATA.md").write_text(
            "---\n"
            "repo: test/repo\n"
            "issue_number: 998\n"
            "pr_number: 999\n"
            'issue_title: "Test case"\n'
            'issue_created_at: "2026-01-01"\n'
            "pr_author: tester\n"
            "scoping: tightly_scoped\n"
            "task_type: new_term\n"
            "difficulty: simple\n"
            "scope: single_term\n"
            "review_outcome: approved_first_time\n"
            "curated_by: test\n"
            'curated_at: "2026-01-01"\n'
            "rationale: test\n"
            "---\n\nBody text.\n"
        )
        data = collect_gallery_data(tmp_path)
        case = data["ontologies"]["myont"]["cases"][0]
        assert case["pr_number"] == 999
        assert case["human_diff"] is None
        assert case["agent_attempts"] == []
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_gallery.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'ai4c_scribe.gallery'`

- [ ] **Step 3: Implement `collect_gallery_data()`**

`src/ai4c_scribe/gallery.py`:
```python
"""Generate a static HTML gallery browser for evaluation case studies.

Walks an analysis directory tree containing case study METADATA.md files,
human/agent diffs, scores TSV, and review files. Produces a single
self-contained HTML file for browsing cases in a sidebar + detail layout.
"""

import csv
import json
from pathlib import Path

import yaml


def _parse_frontmatter_and_body(text: str) -> tuple[dict, str]:
    """Split markdown into YAML frontmatter dict and body string.

    >>> fm, body = _parse_frontmatter_and_body("---\\nk: v\\n---\\nHello\\n")
    >>> fm
    {'k': 'v'}
    >>> body.strip()
    'Hello'
    """
    parts = text.split("---", 2)
    frontmatter = yaml.safe_load(parts[1])
    body = parts[2] if len(parts) > 2 else ""
    return frontmatter, body


def _load_scores(scores_path: Path) -> list[dict]:
    """Load scores.tsv into a list of dicts.

    >>> import tempfile, os
    >>> with tempfile.NamedTemporaryFile(mode='w', suffix='.tsv', delete=False) as f:
    ...     _ = f.write("ontology\\tpr_number\\teval_repo_pr\\tf1\\n")
    ...     _ = f.write("ont1\\t100\\t10\\t0.8\\n")
    >>> rows = _load_scores(Path(f.name))
    >>> rows[0]['pr_number']
    '100'
    >>> os.unlink(f.name)
    """
    with open(scores_path) as f:
        reader = csv.DictReader(f, delimiter="\t")
        return list(reader)


def _discover_ontologies(analysis_dir: Path) -> list[str]:
    """Find subdirectories that contain a cases/ folder.

    >>> import tempfile
    >>> with tempfile.TemporaryDirectory() as tmp:
    ...     (Path(tmp) / "ont1" / "cases").mkdir(parents=True)
    ...     (Path(tmp) / "ont2" / "cases").mkdir(parents=True)
    ...     (Path(tmp) / "scripts").mkdir()  # no cases/ subfolder
    ...     sorted(_discover_ontologies(Path(tmp)))
    ['ont1', 'ont2']
    """
    return sorted(
        d.name for d in analysis_dir.iterdir()
        if d.is_dir() and (d / "cases").is_dir()
    )


def collect_gallery_data(analysis_dir: Path) -> dict:
    """Walk the analysis directory and assemble gallery data.

    Args:
        analysis_dir: Path containing ``{ont}/cases/`` and optionally
            ``{ont}/results/`` subdirectories.

    Returns:
        Dict with ``ontologies`` key mapping ontology names to their cases,
        each case containing metadata, narrative, diffs, and agent attempts.
    """
    ontologies: dict[str, dict] = {}

    for ont_name in _discover_ontologies(analysis_dir):
        ont_dir = analysis_dir / ont_name
        cases_dir = ont_dir / "cases"
        results_dir = ont_dir / "results"

        # Load scores.tsv if it exists — keyed by (pr_number -> list of attempts)
        scores_by_pr: dict[int, list[dict]] = {}
        scores_path = results_dir / "scores.tsv"
        if scores_path.exists():
            for row in _load_scores(scores_path):
                pr_num = int(row["pr_number"])
                scores_by_pr.setdefault(pr_num, []).append(row)

        # Load each case
        cases = []
        for case_dir in sorted(cases_dir.iterdir()):
            metadata_path = case_dir / "METADATA.md"
            if not metadata_path.exists():
                continue

            text = metadata_path.read_text()
            frontmatter, body = _parse_frontmatter_and_body(text)
            pr_number = int(frontmatter["pr_number"])

            # Human diff
            human_diff_path = results_dir / "diffs" / "human" / f"pr{pr_number}.diff"
            human_diff = human_diff_path.read_text() if human_diff_path.exists() else None

            # Agent attempts — joined via scores.tsv
            agent_attempts = []
            for score_row in scores_by_pr.get(pr_number, []):
                eval_pr = int(score_row["eval_repo_pr"])

                # Agent diff
                agent_diff_path = results_dir / "diffs" / "agent" / f"pr{eval_pr}.diff"
                agent_diff = agent_diff_path.read_text() if agent_diff_path.exists() else None

                # Review file(s) — match pr{eval_pr}-*.md
                review_md = None
                reviews_dir = results_dir / "reviews"
                if reviews_dir.exists():
                    for review_path in reviews_dir.glob(f"pr{eval_pr}-*.md"):
                        review_md = review_path.read_text()
                        break  # take first match

                agent_attempts.append({
                    "eval_repo_pr": eval_pr,
                    "model": score_row.get("model", ""),
                    "runtime": score_row.get("runtime", ""),
                    "agent_config_tag": score_row.get("agent_config_tag", ""),
                    "agent": score_row.get("agent", ""),
                    "f1": float(score_row.get("f1", 0)),
                    "precision": float(score_row.get("precision", 0)),
                    "recall": float(score_row.get("recall", 0)),
                    "jaccard": float(score_row.get("jaccard", 0)),
                    "diff": agent_diff,
                    "review_md": review_md,
                })

            # Serialize dates to strings for JSON
            metadata = dict(frontmatter)
            for key in ("issue_created_at", "pr_merged_at", "curated_at",
                        "issue_closed_at"):
                if key in metadata and hasattr(metadata[key], "isoformat"):
                    metadata[key] = metadata[key].isoformat()

            cases.append({
                "pr_number": pr_number,
                "ontology": ont_name,
                "metadata": metadata,
                "narrative_md": body,
                "human_diff": human_diff,
                "agent_attempts": agent_attempts,
            })

        ontologies[ont_name] = {"cases": cases}

    return {"ontologies": ontologies}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_gallery.py -v`
Expected: All 6 tests PASS

- [ ] **Step 5: Run doctests**

Run: `uv run pytest --doctest-modules src/ai4c_scribe/gallery.py -v`
Expected: All 3 doctests PASS

- [ ] **Step 6: Commit**

```bash
git add src/ai4c_scribe/gallery.py tests/test_gallery.py
git commit -m "feat: add collect_gallery_data() with tests and fixtures"
```

---

### Task 3: `generate_gallery()` — HTML generation with tests

Build the HTML template and the `generate_gallery()` function that embeds the collected data into a self-contained HTML file.

**Files:**
- Modify: `src/ai4c_scribe/gallery.py`
- Modify: `tests/test_gallery.py`

- [ ] **Step 1: Write failing tests for HTML generation**

Add to `tests/test_gallery.py`:
```python
def test_generate_gallery_creates_html(tmp_path):
    """generate_gallery() writes a valid HTML file."""
    output = tmp_path / "gallery.html"
    result = generate_gallery(FIXTURE_DIR, output)
    assert result == output
    assert output.exists()
    content = output.read_text()
    assert "<!DOCTYPE html>" in content
    assert "gallery-data" in content


def test_generate_gallery_embeds_case_data(tmp_path):
    """Generated HTML contains embedded case data as JSON."""
    output = tmp_path / "gallery.html"
    generate_gallery(FIXTURE_DIR, output)
    content = output.read_text()
    # The JSON blob should contain our fixture case titles
    assert "Add new term: foo bar" in content
    assert "Reclassify baz widget" in content


def test_generate_gallery_embeds_diff_data(tmp_path):
    """Generated HTML contains embedded diff content."""
    output = tmp_path / "gallery.html"
    generate_gallery(FIXTURE_DIR, output)
    content = output.read_text()
    assert "+name: foo bar" in content
```

Update import at the top of test file:
```python
from ai4c_scribe.gallery import collect_gallery_data, generate_gallery
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_gallery.py::test_generate_gallery_creates_html -v`
Expected: FAIL — `ImportError: cannot import name 'generate_gallery'`

- [ ] **Step 3: Implement `generate_gallery()` and the HTML template**

Add to `src/ai4c_scribe/gallery.py`:
```python
GALLERY_HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>ai4c-scribe Case Gallery</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
       display: flex; height: 100vh; background: #f5f5f5; color: #1a1a1a; }

/* Sidebar */
#sidebar { width: 300px; min-width: 300px; background: #fff; border-right: 1px solid #ddd;
           display: flex; flex-direction: column; height: 100vh; overflow: hidden; }
#filter { padding: 12px; border-bottom: 1px solid #eee; }
#filter input { width: 100%; padding: 8px 12px; border: 1px solid #ddd; border-radius: 6px;
                font-size: 14px; outline: none; }
#filter input:focus { border-color: #4a90d9; box-shadow: 0 0 0 2px rgba(74,144,217,0.2); }
#case-list { overflow-y: auto; flex: 1; }

/* Ontology groups */
.ont-group-header { padding: 10px 14px; background: #f8f8f8; border-bottom: 1px solid #eee;
                    cursor: pointer; display: flex; align-items: center; gap: 8px;
                    font-weight: 600; font-size: 13px; text-transform: uppercase;
                    color: #555; user-select: none; }
.ont-group-header:hover { background: #f0f0f0; }
.ont-group-header .arrow { transition: transform 0.2s; font-size: 10px; }
.ont-group-header.collapsed .arrow { transform: rotate(-90deg); }
.ont-group-header .count { background: #e0e0e0; border-radius: 10px; padding: 1px 8px;
                           font-size: 11px; font-weight: 500; }
.ont-group.collapsed .ont-cases { display: none; }

/* Case items */
.case-item { padding: 10px 14px; border-bottom: 1px solid #f0f0f0; cursor: pointer;
             display: flex; flex-direction: column; gap: 2px; }
.case-item:hover { background: #f5f8fc; }
.case-item.active { background: #e8f0fe; border-left: 3px solid #4a90d9; }
.case-item .case-pr { font-family: 'SF Mono', Monaco, monospace; font-size: 12px;
                      color: #666; display: flex; align-items: center; gap: 6px; }
.case-item .case-title { font-size: 13px; color: #333; white-space: nowrap;
                          overflow: hidden; text-overflow: ellipsis; }
.dot-simple { color: #22c55e; }
.dot-medium { color: #f59e0b; }
.dot-hard { color: #ef4444; }

/* Detail pane */
#detail { flex: 1; overflow-y: auto; padding: 32px 40px; }
#detail h1 { font-size: 22px; margin-bottom: 4px; }
#detail .pr-number { font-family: monospace; color: #666; font-size: 14px; }
.gh-links { margin: 8px 0 16px; display: flex; gap: 12px; }
.gh-links a { color: #4a90d9; text-decoration: none; font-size: 13px; }
.gh-links a:hover { text-decoration: underline; }

/* Badges */
.badges { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 20px; }
.badge { padding: 3px 10px; border-radius: 12px; font-size: 12px; font-weight: 500; }
.badge-type { background: #dbeafe; color: #1e40af; }
.badge-simple { background: #dcfce7; color: #166534; }
.badge-medium { background: #fef3c7; color: #92400e; }
.badge-hard { background: #fecaca; color: #991b1b; }
.badge-scoping { background: #f3e8ff; color: #6b21a8; }
.badge-outcome { background: #e0e7ff; color: #3730a3; }
.badge-author { background: #f1f5f9; color: #475569; }

/* Narrative */
.narrative { line-height: 1.65; margin-bottom: 24px; }
.narrative h2 { font-size: 16px; margin: 20px 0 8px; color: #333; }
.narrative p { margin-bottom: 10px; color: #444; }

/* Collapsible sections */
.collapsible { margin-bottom: 16px; border: 1px solid #e0e0e0; border-radius: 8px;
               overflow: hidden; }
.collapsible-header { padding: 12px 16px; background: #fafafa; cursor: pointer;
                      font-weight: 600; font-size: 14px; display: flex;
                      align-items: center; gap: 8px; user-select: none; }
.collapsible-header:hover { background: #f0f0f0; }
.collapsible-header .arrow { transition: transform 0.2s; font-size: 10px; }
.collapsible-header.open .arrow { transform: rotate(90deg); }
.collapsible-body { display: none; padding: 16px; background: #fff; }
.collapsible-body.open { display: block; }

/* Diff viewer */
.diff-viewer { font-family: 'SF Mono', Monaco, monospace; font-size: 12px;
               line-height: 1.5; overflow-x: auto; white-space: pre; }
.diff-viewer .diff-add { background: #dcfce7; color: #166534; }
.diff-viewer .diff-del { background: #fecaca; color: #991b1b; }
.diff-viewer .diff-hunk { background: #dbeafe; color: #1e40af; }
.diff-viewer .diff-header { color: #888; }

/* Agent attempts */
.attempt { border: 1px solid #e8e8e8; border-radius: 6px; margin-bottom: 10px; padding: 12px; }
.attempt-header { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; flex-wrap: wrap; }
.attempt-model { font-weight: 600; font-size: 14px; }
.attempt-runtime { color: #666; font-size: 12px; }
.score-pills { display: flex; gap: 4px; }
.score-pill { padding: 2px 8px; border-radius: 8px; font-size: 11px; font-family: monospace; }
.score-pill.good { background: #dcfce7; color: #166534; }
.score-pill.mid { background: #fef3c7; color: #92400e; }
.score-pill.low { background: #fecaca; color: #991b1b; }

/* Empty state */
#empty-state { display: flex; align-items: center; justify-content: center;
               height: 100%; color: #888; font-size: 16px; }
</style>
</head>
<body>

<div id="sidebar">
  <div id="filter"><input type="text" placeholder="Filter by title, PR#, type..." id="filter-input"></div>
  <div id="case-list"></div>
</div>
<div id="detail"><div id="empty-state">Select a case from the sidebar</div></div>

<script id="gallery-data" type="application/json">
__GALLERY_DATA__
</script>

<script>
const DATA = JSON.parse(document.getElementById('gallery-data').textContent);
const caseList = document.getElementById('case-list');
const detail = document.getElementById('detail');
const filterInput = document.getElementById('filter-input');
let allCases = [];
let activeCase = null;

// Build flat list with ontology info
for (const [ont, ontData] of Object.entries(DATA.ontologies).sort()) {
  for (const c of ontData.cases) {
    c._ont = ont;
    allCases.push(c);
  }
}

function difficultyDot(d) {
  const cls = d === 'simple' ? 'dot-simple' : d === 'medium' ? 'dot-medium' : 'dot-hard';
  return `<span class="${cls}">&bull;</span>`;
}

function difficultyBadgeClass(d) {
  return d === 'simple' ? 'badge-simple' : d === 'medium' ? 'badge-medium' : 'badge-hard';
}

function scoreClass(v) { return v >= 0.7 ? 'good' : v >= 0.4 ? 'mid' : 'low'; }

function renderSidebar(filter) {
  const q = (filter || '').toLowerCase();
  const grouped = {};
  for (const c of allCases) {
    const title = (c.metadata.issue_title || '').toLowerCase();
    const prStr = String(c.pr_number);
    const taskType = (c.metadata.task_type || '').toLowerCase();
    if (q && !title.includes(q) && !prStr.includes(q) && !taskType.includes(q)) continue;
    if (!grouped[c._ont]) grouped[c._ont] = [];
    grouped[c._ont].push(c);
  }

  caseList.innerHTML = '';
  for (const ont of Object.keys(grouped).sort()) {
    const cases = grouped[ont];
    const group = document.createElement('div');
    group.className = 'ont-group';
    group.innerHTML = `<div class="ont-group-header" onclick="this.classList.toggle('collapsed');this.parentElement.classList.toggle('collapsed')">
      <span class="arrow">&#9654;</span> ${ont} <span class="count">${cases.length}</span>
    </div><div class="ont-cases"></div>`;
    const casesContainer = group.querySelector('.ont-cases');
    for (const c of cases) {
      const item = document.createElement('div');
      item.className = 'case-item' + (activeCase === c ? ' active' : '');
      item.innerHTML = `<span class="case-pr">${difficultyDot(c.metadata.difficulty)} PR#${c.pr_number}</span>
        <span class="case-title">${c.metadata.issue_title || '(untitled)'}</span>`;
      item.onclick = () => selectCase(c);
      casesContainer.appendChild(item);
    }
    caseList.appendChild(group);
  }
}

function highlightDiff(text) {
  if (!text) return '';
  return text.split('\\n').map(line => {
    if (line.startsWith('+++') || line.startsWith('---') || line.startsWith('diff '))
      return `<span class="diff-header">${esc(line)}</span>`;
    if (line.startsWith('@@')) return `<span class="diff-hunk">${esc(line)}</span>`;
    if (line.startsWith('+')) return `<span class="diff-add">${esc(line)}</span>`;
    if (line.startsWith('-')) return `<span class="diff-del">${esc(line)}</span>`;
    return esc(line);
  }).join('\\n');
}

function esc(s) {
  return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
}

function collapsible(title, content, startOpen) {
  const openCls = startOpen ? ' open' : '';
  return `<div class="collapsible">
    <div class="collapsible-header${openCls}" onclick="this.classList.toggle('open');this.nextElementSibling.classList.toggle('open')">
      <span class="arrow">&#9654;</span> ${title}
    </div>
    <div class="collapsible-body${openCls}">${content}</div>
  </div>`;
}

function selectCase(c) {
  activeCase = c;
  renderSidebar(filterInput.value);
  const m = c.metadata;
  const repo = m.repo || '';
  const issueUrl = repo ? `https://github.com/${repo}/issues/${m.issue_number}` : '';
  const prUrl = repo ? `https://github.com/${repo}/pull/${c.pr_number}` : '';

  let html = `<span class="pr-number">PR #${c.pr_number} &mdash; ${c._ont}</span>
    <h1>${m.issue_title || '(untitled)'}</h1>
    <div class="gh-links">
      ${issueUrl ? `<a href="${issueUrl}" target="_blank">Issue #${m.issue_number}</a>` : ''}
      ${prUrl ? `<a href="${prUrl}" target="_blank">PR #${c.pr_number}</a>` : ''}
    </div>
    <div class="badges">
      <span class="badge badge-type">${m.task_type || ''}</span>
      <span class="badge ${difficultyBadgeClass(m.difficulty)}">${m.difficulty || ''}</span>
      <span class="badge badge-scoping">${m.scoping || ''}</span>
      <span class="badge badge-outcome">${m.review_outcome || ''}</span>
      ${m.scope ? `<span class="badge badge-scoping">${m.scope}</span>` : ''}
      <span class="badge badge-author">${m.pr_author || ''}</span>
    </div>`;

  // Narrative
  if (c.narrative_md) {
    html += `<div class="narrative">${typeof marked !== 'undefined' ? marked.parse(c.narrative_md) : c.narrative_md.replace(/\\n/g, '<br>')}</div>`;
  }

  // Human diff
  if (c.human_diff) {
    html += collapsible(
      `Human Diff (PR #${c.pr_number})`,
      `<div class="diff-viewer">${highlightDiff(c.human_diff)}</div>`,
      false
    );
  }

  // Agent attempts
  if (c.agent_attempts && c.agent_attempts.length > 0) {
    let attemptsHtml = '';
    const sorted = [...c.agent_attempts].sort((a, b) => b.f1 - a.f1);
    for (const a of sorted) {
      let innerHtml = `<div class="attempt-header">
        <span class="attempt-model">${a.model}</span>
        <span class="attempt-runtime">${a.runtime}</span>
        <div class="score-pills">
          <span class="score-pill ${scoreClass(a.f1)}">F1: ${a.f1.toFixed(3)}</span>
          <span class="score-pill ${scoreClass(a.precision)}">P: ${a.precision.toFixed(3)}</span>
          <span class="score-pill ${scoreClass(a.recall)}">R: ${a.recall.toFixed(3)}</span>
          <span class="score-pill ${scoreClass(a.jaccard)}">J: ${a.jaccard.toFixed(3)}</span>
        </div>
      </div>`;
      if (a.diff) {
        innerHtml += collapsible('Diff (eval PR #' + a.eval_repo_pr + ')',
          `<div class="diff-viewer">${highlightDiff(a.diff)}</div>`, false);
      }
      if (a.review_md) {
        innerHtml += collapsible('Review',
          `<div class="narrative">${typeof marked !== 'undefined' ? marked.parse(a.review_md) : a.review_md.replace(/\\n/g, '<br>')}</div>`, false);
      }
      attemptsHtml += `<div class="attempt">${innerHtml}</div>`;
    }
    html += collapsible(
      `Agent Attempts (${c.agent_attempts.length})`,
      attemptsHtml,
      false
    );
  }

  detail.innerHTML = html;
}

// Keyboard navigation
document.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT') return;
  const items = document.querySelectorAll('.case-item');
  if (!items.length) return;
  let idx = -1;
  items.forEach((el, i) => { if (el.classList.contains('active')) idx = i; });
  if (e.key === 'ArrowDown') { e.preventDefault(); if (idx < items.length - 1) items[idx + 1].click(); }
  if (e.key === 'ArrowUp') { e.preventDefault(); if (idx > 0) items[idx - 1].click(); }
});

filterInput.addEventListener('input', () => renderSidebar(filterInput.value));

// Initial render
renderSidebar('');
</script>
</body>
</html>
"""


def generate_gallery(analysis_dir: Path, output: Path) -> Path:
    """Generate a self-contained HTML gallery from an analysis directory.

    Args:
        analysis_dir: Path containing ``{ont}/cases/`` subdirectories.
        output: Path for the output HTML file.

    Returns:
        Path to the generated HTML file.
    """
    data = collect_gallery_data(analysis_dir)
    json_blob = json.dumps(data, indent=None, ensure_ascii=False)
    html = GALLERY_HTML_TEMPLATE.replace("__GALLERY_DATA__", json_blob)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(html)
    return output
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_gallery.py -v`
Expected: All 9 tests PASS

- [ ] **Step 5: Commit**

```bash
git add src/ai4c_scribe/gallery.py tests/test_gallery.py
git commit -m "feat: add generate_gallery() with HTML template"
```

---

### Task 4: CLI `gallery` command

Wire up the thin CLI wrapper.

**Files:**
- Modify: `src/ai4c_scribe/cli.py`
- Modify: `tests/test_gallery.py`

- [ ] **Step 1: Write failing test for CLI command**

Add to `tests/test_gallery.py`:
```python
from typer.testing import CliRunner
from ai4c_scribe.cli import app

runner = CliRunner()


def test_gallery_cli_generates_html(tmp_path):
    """CLI gallery command generates an HTML file."""
    output = tmp_path / "out.html"
    result = runner.invoke(app, ["gallery", str(FIXTURE_DIR), "-o", str(output)])
    assert result.exit_code == 0, result.output
    assert output.exists()
    assert "gallery.html" in result.output or "out.html" in result.output


def test_gallery_cli_default_output(tmp_path, monkeypatch):
    """CLI gallery command uses gallery.html as default output."""
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["gallery", str(FIXTURE_DIR)])
    assert result.exit_code == 0, result.output
    assert (tmp_path / "gallery.html").exists()
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `uv run pytest tests/test_gallery.py::test_gallery_cli_generates_html -v`
Expected: FAIL — no `gallery` command registered

- [ ] **Step 3: Add `gallery` command to CLI**

Add to `src/ai4c_scribe/cli.py`, after the existing imports:
```python
from ai4c_scribe.gallery import generate_gallery
```

Add the command (place after the `browse` command):
```python
@app.command()
def gallery(
    analysis_dir: Annotated[Path, typer.Argument(help="Analysis directory (contains {ont}/cases/ and {ont}/results/)")],
    output: Annotated[Path, typer.Option("--output", "-o", help="Output HTML file")] = Path("gallery.html"),
):
    """Generate a static HTML gallery browser for evaluation case studies.

    Scans the analysis directory for case study METADATA.md files, human/agent
    diffs, scores, and reviews. Produces a single self-contained HTML file with
    a sidebar-list + detail-pane layout for browsing cases.

    Example:
        ai4c-scribe gallery analysis/ -o gallery.html
        open gallery.html
    """
    typer.echo(f"Generating gallery from {analysis_dir}...")
    result = generate_gallery(analysis_dir, output)
    typer.echo(f"Gallery written to {result}")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run pytest tests/test_gallery.py -v`
Expected: All 11 tests PASS

- [ ] **Step 5: Run the full test suite**

Run: `just test`
Expected: All tests pass, mypy clean, ruff clean

- [ ] **Step 6: Commit**

```bash
git add src/ai4c_scribe/cli.py tests/test_gallery.py
git commit -m "feat: add gallery CLI command"
```

---

### Task 5: Smoke test with real data

Run the gallery command against the actual `analysis/` directory and verify the output works.

- [ ] **Step 1: Generate gallery from real analysis data**

Run: `uv run ai4c-scribe gallery analysis/ -o analysis/gallery.html`
Expected: Outputs a file path, no errors

- [ ] **Step 2: Verify the HTML file is reasonable**

Run: `wc -c analysis/gallery.html` — should be a few MB (embedded diffs are large)
Run: `grep -c '"pr_number"' analysis/gallery.html` — should be ~160 (40 cases x 4 ontologies)

- [ ] **Step 3: Open in browser and verify**

Run: `open analysis/gallery.html`
Verify: sidebar shows 4 ontology groups with cases, clicking a case shows detail pane with metadata, narrative, diffs, and agent attempts.

- [ ] **Step 4: Add gallery.html to .gitignore**

Add `analysis/gallery.html` to `.gitignore` (it's a generated artifact).

- [ ] **Step 5: Commit**

```bash
git add .gitignore
git commit -m "chore: add gallery.html to gitignore"
```
