# Case Study Schema Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a LinkML-backed case study system where markdown files with validated frontmatter replace inline `input_sets` in workflow configs, and a new skill helps agents curate these case studies.

**Architecture:** LinkML schema generates Pydantic models. A `case_studies` module provides load/validate functions. The workflow config gains an `input_sets_dir` field that loads case study files and injects them as `input_sets`. A new Claude Code skill guides agents through curating case studies.

**Tech Stack:** LinkML, Pydantic (generated), PyYAML (frontmatter parsing), pytest, typer (CLI)

---

## File Structure

| File | Responsibility |
|------|---------------|
| `src/ai4c_scribe/schema/case_study.yaml` | LinkML schema (already created) |
| `src/ai4c_scribe/case_studies.py` | Load, parse, validate case study markdown files |
| `src/ai4c_scribe/workflows/models.py` | Add `input_sets_dir` field to `WorkflowConfig` |
| `src/ai4c_scribe/workflows/config.py` | Load case studies when `input_sets_dir` is set |
| `.claude/skills/find-training-cases/SKILL.md` | Agent skill for curating case studies |
| `tests/case_studies/test_case_studies.py` | Tests for loading/validation |
| `tests/case_studies/__init__.py` | Package init |
| `tests/workflows/test_config.py` | Add test for `input_sets_dir` loading |
| `tests/fixtures/cases/sample-case.md` | Test fixture |

---

### Task 1: Generate Pydantic models from LinkML schema

**Files:**
- Modify: `pyproject.toml` (add gen-pydantic to build/dev deps if needed)
- Create: `src/ai4c_scribe/schema/__init__.py`
- Create: `src/ai4c_scribe/schema/case_study_models.py` (generated)

- [ ] **Step 1: Generate Pydantic models**

```bash
uv run gen-pydantic src/ai4c_scribe/schema/case_study.yaml > src/ai4c_scribe/schema/case_study_models.py
```

- [ ] **Step 2: Create schema package init**

Create `src/ai4c_scribe/schema/__init__.py`:

```python
"""LinkML schema and generated models for ai4c-scribe."""

from ai4c_scribe.schema.case_study_models import (
    CaseStudy,
    DifficultyEnum,
    ReviewOutcomeEnum,
    ScopeEnum,
    TaskTypeEnum,
)

__all__ = [
    "CaseStudy",
    "DifficultyEnum",
    "ReviewOutcomeEnum",
    "ScopeEnum",
    "TaskTypeEnum",
]
```

- [ ] **Step 3: Verify import works**

```bash
uv run python -c "from ai4c_scribe.schema import CaseStudy; print(CaseStudy.model_fields.keys())"
```

Expected: prints the field names from the schema.

- [ ] **Step 4: Commit**

```bash
git add src/ai4c_scribe/schema/
git commit -m "feat: add LinkML schema and generated Pydantic models for case studies"
```

---

### Task 2: Case study loader module

**Files:**
- Create: `src/ai4c_scribe/case_studies.py`
- Create: `tests/case_studies/__init__.py`
- Create: `tests/case_studies/test_case_studies.py`
- Create: `tests/fixtures/cases/sample-case.md`

- [ ] **Step 1: Create test fixture**

Create `tests/fixtures/cases/sample-case.md`:

```markdown
---
repo: geneontology/go-ontology
issue_number: 31158
pr_number: 31262
issue_title: "Add new term: foo bar activity"
issue_labels:
  - new term request
  - molecular_function
issue_created_at: "2025-11-03"
issue_closed_at: "2025-11-15"
pr_author: ValWood
pr_merged_at: "2025-11-15"
pr_num_commits: 3
task_type: new_term
difficulty: simple
scope: single_term
review_outcome: changes_requested
domain_area: molecular_function
tags:
  - catalytic-activity
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Clean new-term request with one round of review feedback on definition wording
---

## Context

Issue requested a new MF term for foo bar activity, needed for annotation of S. pombe genes.

## Resolution

Reviewer requested rewording of the definition to follow genus-differentia pattern. Author revised in a follow-up commit.
```

- [ ] **Step 2: Write failing tests**

Create `tests/case_studies/__init__.py` (empty) and `tests/case_studies/test_case_studies.py`:

```python
"""Tests for case study loading and validation."""

from pathlib import Path

import pytest

from ai4c_scribe.case_studies import (
    load_case_study,
    load_case_studies_dir,
    case_study_to_input_set,
)
from ai4c_scribe.schema import CaseStudy


FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "cases"


def test_load_case_study():
    """Load a single case study from markdown file."""
    case = load_case_study(FIXTURES_DIR / "sample-case.md")
    assert isinstance(case, CaseStudy)
    assert case.repo == "geneontology/go-ontology"
    assert case.issue_number == 31158
    assert case.pr_number == 31262
    assert case.task_type.value == "new_term"
    assert case.difficulty.value == "simple"
    assert "new term request" in case.issue_labels


def test_load_case_studies_dir():
    """Load all case studies from a directory."""
    cases = load_case_studies_dir(FIXTURES_DIR)
    assert len(cases) >= 1
    assert all(isinstance(c, CaseStudy) for c in cases)


def test_case_study_to_input_set():
    """Convert case study to workflow input_set dict."""
    case = load_case_study(FIXTURES_DIR / "sample-case.md")
    input_set = case_study_to_input_set(case)
    assert input_set["issue_number"] == "31158"
    assert input_set["pr_number"] == "31262"


def test_load_invalid_frontmatter(tmp_path):
    """Invalid frontmatter raises ValidationError."""
    bad_file = tmp_path / "bad.md"
    bad_file.write_text("---\nrepo: foo/bar\n---\nNo required fields.\n")
    with pytest.raises(Exception):
        load_case_study(bad_file)
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
uv run pytest tests/case_studies/test_case_studies.py -v
```

Expected: FAIL with `ImportError: cannot import name 'load_case_study'`

- [ ] **Step 4: Implement case_studies module**

Create `src/ai4c_scribe/case_studies.py`:

```python
"""Load and validate case study markdown files.

Case studies are markdown files with YAML frontmatter validated against
the CaseStudy LinkML schema. The markdown body is an agentic narrative
summary (not parsed by the runner).

Example:
    >>> from pathlib import Path
    >>> from ai4c_scribe.case_studies import load_case_study
    >>> case = load_case_study(Path("tests/fixtures/cases/sample-case.md"))
    >>> case.repo
    'geneontology/go-ontology'
    >>> case.issue_number
    31158
"""

from pathlib import Path

import yaml

from ai4c_scribe.schema import CaseStudy


def parse_frontmatter(text: str) -> dict:
    """Extract YAML frontmatter from markdown text.

    Expects the file to start with '---' and have a closing '---'.

    Example:
        >>> data = parse_frontmatter("---\\nfoo: bar\\n---\\nbody text\\n")
        >>> data
        {'foo': 'bar'}
    """
    if not text.startswith("---"):
        raise ValueError("File does not start with YAML frontmatter delimiter '---'")

    # Find closing delimiter
    end_idx = text.index("---", 3)
    yaml_text = text[3:end_idx]
    return yaml.safe_load(yaml_text)


def load_case_study(path: Path) -> CaseStudy:
    """Load and validate a single case study from a markdown file.

    Args:
        path: Path to the markdown file with YAML frontmatter

    Returns:
        Validated CaseStudy instance

    Example:
        >>> from pathlib import Path
        >>> case = load_case_study(Path("tests/fixtures/cases/sample-case.md"))
        >>> case.pr_number
        31262
    """
    text = path.read_text()
    data = parse_frontmatter(text)
    return CaseStudy(**data)


def load_case_studies_dir(directory: Path) -> list[CaseStudy]:
    """Load all case study markdown files from a directory.

    Reads all .md files in the directory (non-recursive).

    Args:
        directory: Path to directory containing case study .md files

    Returns:
        List of validated CaseStudy instances

    Example:
        >>> from pathlib import Path
        >>> cases = load_case_studies_dir(Path("tests/fixtures/cases"))
        >>> len(cases) >= 1
        True
    """
    cases = []
    for md_file in sorted(directory.glob("*.md")):
        cases.append(load_case_study(md_file))
    return cases


def case_study_to_input_set(case: CaseStudy) -> dict[str, str]:
    """Convert a CaseStudy to a workflow input_set dict.

    The runner expects string values for issue_number and pr_number.

    Args:
        case: Validated CaseStudy

    Returns:
        Dict with string-typed issue_number and pr_number

    Example:
        >>> from pathlib import Path
        >>> case = load_case_study(Path("tests/fixtures/cases/sample-case.md"))
        >>> input_set = case_study_to_input_set(case)
        >>> input_set["issue_number"]
        '31158'
    """
    return {
        "issue_number": str(case.issue_number),
        "pr_number": str(case.pr_number),
    }
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
uv run pytest tests/case_studies/test_case_studies.py -v
```

Expected: all 4 tests PASS

- [ ] **Step 6: Run doctests**

```bash
uv run pytest --doctest-modules src/ai4c_scribe/case_studies.py -v
```

Expected: PASS

- [ ] **Step 7: Commit**

```bash
git add src/ai4c_scribe/case_studies.py tests/case_studies/ tests/fixtures/cases/
git commit -m "feat: add case study loader with frontmatter parsing and validation"
```

---

### Task 3: Wire input_sets_dir into workflow config

**Files:**
- Modify: `src/ai4c_scribe/workflows/models.py:66-116`
- Modify: `src/ai4c_scribe/workflows/config.py:38-76`
- Modify: `tests/workflows/test_config.py`
- Create: `tests/fixtures/cases/second-case.md` (for multi-file loading test)

- [ ] **Step 1: Create second test fixture**

Create `tests/fixtures/cases/second-case.md`:

```markdown
---
repo: geneontology/go-ontology
issue_number: 27880
pr_number: 27886
issue_title: "Obsolete redundant term"
issue_labels:
  - obsoletion
issue_created_at: "2025-08-10"
issue_closed_at: "2025-08-12"
pr_author: pgaudet
pr_merged_at: "2025-08-12"
pr_num_commits: 1
task_type: obsoletion
difficulty: simple
scope: single_term
review_outcome: approved_first_time
domain_area: biological_process
tags:
  - redundancy
curated_by: claude-opus-4
curated_at: "2026-05-03"
rationale: Simple obsoletion with clear replacement term, approved without changes
---

## Context

Term was flagged as redundant with an existing parent term.

## Resolution

Author obsoleted the term and added a replaced_by annotation. Approved on first review.
```

- [ ] **Step 2: Write failing test for input_sets_dir**

Add to `tests/workflows/test_config.py`:

```python
from pathlib import Path

from ai4c_scribe.workflows.config import load_config


FIXTURES_DIR = Path(__file__).parent.parent / "fixtures"


def test_load_config_with_input_sets_dir(tmp_path):
    """Config with input_sets_dir loads case studies as input_sets."""
    # Write a config that points to our fixture cases
    config_yaml = tmp_path / "config.yaml"
    cases_dir = FIXTURES_DIR / "cases"
    config_yaml.write_text(
        f"workflow: test.yml\n"
        f"repo: owner/repo\n"
        f"input_sets_dir: {cases_dir}\n"
        f"inputs:\n"
        f"  model: claude-sonnet-4-5-20250929\n"
    )
    config = load_config(config_yaml)
    assert len(config.input_sets) >= 2
    # Check that input_sets have the expected keys
    assert config.input_sets[0]["issue_number"] == "27880"  # sorted by filename
    assert config.input_sets[0]["pr_number"] == "27886"
```

- [ ] **Step 3: Run test to verify it fails**

```bash
uv run pytest tests/workflows/test_config.py::test_load_config_with_input_sets_dir -v
```

Expected: FAIL (field doesn't exist yet)

- [ ] **Step 4: Add input_sets_dir to WorkflowConfig**

In `src/ai4c_scribe/workflows/models.py`, add to `WorkflowConfig` class:

```python
    input_sets_dir: Optional[Path] = Field(
        default=None,
        description="Directory of case study .md files to load as input_sets",
    )
```

- [ ] **Step 5: Update load_config to resolve input_sets_dir**

In `src/ai4c_scribe/workflows/config.py`, update `load_config` to load case studies when `input_sets_dir` is present:

```python
from ai4c_scribe.case_studies import load_case_studies_dir, case_study_to_input_set


def load_config(config_path: Path) -> WorkflowConfig:
    """Load workflow configuration from YAML file.

    Args:
        config_path: Path to YAML config file

    Returns:
        Validated WorkflowConfig

    Raises:
        FileNotFoundError: If config file doesn't exist
        ValidationError: If config is invalid

    Example:
        >>> from pathlib import Path
        >>> # Would load from actual file:
        >>> # config = load_config(Path("workflows/eval.yaml"))
    """
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")

    with open(config_path) as f:
        data = yaml.safe_load(f)

    if data is None:
        data = {}

    # Handle limits
    limits = WorkflowLimits()
    if "limits" in data:
        limits = WorkflowLimits(**data.pop("limits"))

    # Handle input_sets_dir: load case studies and convert to input_sets
    input_sets_dir = data.pop("input_sets_dir", None)
    if input_sets_dir is not None:
        cases_dir = Path(input_sets_dir)
        # Resolve relative paths against config file location
        if not cases_dir.is_absolute():
            cases_dir = config_path.parent / cases_dir
        cases = load_case_studies_dir(cases_dir)
        # Merge with any existing input_sets
        case_input_sets = [case_study_to_input_set(c) for c in cases]
        existing = data.get("input_sets", [])
        data["input_sets"] = existing + case_input_sets

    return WorkflowConfig(
        limits=limits,
        **data,
    )
```

- [ ] **Step 6: Run test to verify it passes**

```bash
uv run pytest tests/workflows/test_config.py::test_load_config_with_input_sets_dir -v
```

Expected: PASS

- [ ] **Step 7: Run full workflow test suite**

```bash
uv run pytest tests/workflows/ -v
```

Expected: all existing tests still pass

- [ ] **Step 8: Commit**

```bash
git add src/ai4c_scribe/workflows/models.py src/ai4c_scribe/workflows/config.py tests/workflows/test_config.py tests/fixtures/cases/second-case.md
git commit -m "feat: add input_sets_dir support to workflow config for case study loading"
```

---

### Task 4: CLI command to validate case studies

**Files:**
- Modify: `src/ai4c_scribe/cli.py`
- Create: `tests/cli/test_case_studies_cli.py`

- [ ] **Step 1: Write failing CLI test**

Create `tests/cli/test_case_studies_cli.py`:

```python
"""Tests for case study CLI commands."""

from pathlib import Path

from typer.testing import CliRunner

from ai4c_scribe.cli import app

runner = CliRunner()
FIXTURES_DIR = Path(__file__).parent.parent / "fixtures" / "cases"


def test_validate_cases_valid():
    """Validate command succeeds on valid case studies."""
    result = runner.invoke(app, ["cases", "validate", str(FIXTURES_DIR)])
    assert result.exit_code == 0
    assert "valid" in result.stdout.lower()


def test_validate_cases_invalid(tmp_path):
    """Validate command reports errors on invalid case studies."""
    bad_file = tmp_path / "bad.md"
    bad_file.write_text("---\nrepo: foo/bar\n---\nMissing fields.\n")
    result = runner.invoke(app, ["cases", "validate", str(tmp_path)])
    assert result.exit_code == 1


def test_list_cases():
    """List command shows case studies."""
    result = runner.invoke(app, ["cases", "list", str(FIXTURES_DIR)])
    assert result.exit_code == 0
    assert "31158" in result.stdout
```

- [ ] **Step 2: Run tests to verify they fail**

```bash
uv run pytest tests/cli/test_case_studies_cli.py -v
```

Expected: FAIL (no `cases` subcommand)

- [ ] **Step 3: Add cases subcommand to CLI**

Add a `cases` command group to `src/ai4c_scribe/cli.py`:

```python
import typer
from pathlib import Path
from ai4c_scribe.case_studies import load_case_study, load_case_studies_dir

cases_app = typer.Typer(help="Manage case study files.")
app.add_typer(cases_app, name="cases")


@cases_app.command()
def validate(directory: Path = typer.Argument(..., help="Directory of case study .md files")):
    """Validate all case study files in a directory."""
    errors = []
    count = 0
    for md_file in sorted(directory.glob("*.md")):
        count += 1
        try:
            load_case_study(md_file)
        except Exception as e:
            errors.append((md_file.name, str(e)))

    if errors:
        typer.echo(f"Found {len(errors)} invalid case studies:")
        for name, err in errors:
            typer.echo(f"  {name}: {err}")
        raise typer.Exit(code=1)
    else:
        typer.echo(f"All {count} case studies valid.")


@cases_app.command("list")
def list_cases(directory: Path = typer.Argument(..., help="Directory of case study .md files")):
    """List case studies with summary info."""
    cases = load_case_studies_dir(directory)
    for case in cases:
        typer.echo(
            f"#{case.issue_number} -> PR#{case.pr_number} "
            f"[{case.task_type.value}] [{case.difficulty.value}] "
            f"{case.issue_title}"
        )
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
uv run pytest tests/cli/test_case_studies_cli.py -v
```

Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add src/ai4c_scribe/cli.py tests/cli/test_case_studies_cli.py
git commit -m "feat: add 'cases validate' and 'cases list' CLI commands"
```

---

### Task 5: Create find-training-cases skill

**Files:**
- Create: `.claude/skills/find-training-cases/SKILL.md`

- [ ] **Step 1: Write the skill**

Create `.claude/skills/find-training-cases/SKILL.md`:

```markdown
---
name: find-training-cases
description: |
  Find diverse, high-quality PR test cases in a GitHub repository for agent evaluation.
  Use when building a case study folder for eval replay. Searches for PRs with clean
  issue-to-PR mappings and writes markdown case study files with validated frontmatter.
---

# Find Training Cases

Curate evaluation case studies from a GitHub repository. Each case study is a markdown file
with YAML frontmatter conforming to the CaseStudy schema.

## Inputs

Ask the user for:
- **Source repo**: GitHub repository to mine (e.g., `geneontology/go-ontology`)
- **Output directory**: Where to write case study .md files (e.g., `cases/go-ontology/`)
- **Number of cases**: How many to find (default: 20)
- **Diversity criteria**: Any specific axes to cover (task types, difficulty spread, etc.)

## Selection Criteria

A good case study has:
1. **Clean issue-PR mapping**: One issue, one PR that fixes it. Use `gh pr list --search "fixes #N"` to verify.
2. **Focused changes**: The PR diff is primarily about the issue, not unrelated cleanup.
3. **Clear intent**: The issue title and body explain what needs to be done.
4. **Reproducible**: An agent given the issue text could plausibly produce a fix.

## Diversity Axes

Aim for coverage across:
- **Task type**: new_term, obsoletion, reclassification, synonym_update, axiom_repair, bulk_edit, documentation
- **Difficulty**: simple, medium, hard (roughly equal split, or as user requests)
- **Scope**: single_term, multi_term, structural_refactor
- **Review outcome**: Mix of approved_first_time, changes_requested, multiple_rounds

## Process

1. Use `gh` CLI to search for recent merged PRs with linked issues:
   ```bash
   gh pr list --repo REPO --state merged --limit 100 --json number,title,labels,createdAt,mergedAt,author,body
   ```

2. For each candidate PR, check:
   - Does it reference exactly one issue? (`fixes #N`, `closes #N` in body)
   - Is the diff focused? (check file count and diff size with `gh pr diff --stat`)
   - Does the issue have clear acceptance criteria?

3. For selected cases, gather metadata:
   ```bash
   gh issue view N --repo REPO --json title,labels,createdAt,closedAt,milestone
   gh pr view N --repo REPO --json commits,reviews
   ```

4. Write each case study as a markdown file:
   - Filename: `{issue_number}.md`
   - YAML frontmatter with all required fields from the CaseStudy schema
   - Markdown body: 2-3 paragraph summary of context and resolution

5. Validate all generated files:
   ```bash
   uv run ai4c-scribe cases validate OUTPUT_DIR
   ```

## Frontmatter Schema

Required fields:
- `repo`, `issue_number`, `pr_number`
- `issue_title`, `issue_created_at`, `pr_author`
- `task_type`, `difficulty`, `scope`, `review_outcome`
- `curated_by`, `curated_at`, `rationale`

Optional fields:
- `issue_labels`, `issue_closed_at`, `pr_merged_at`, `pr_num_commits`
- `milestone`, `domain_area`, `tags`

## Difficulty Heuristics

- **simple**: 1-2 commits, single file changed, mechanical edit (add term, add synonym)
- **medium**: 2-5 commits, needs domain knowledge, definition rewording, placement decisions
- **hard**: 5+ commits or complex axiom work, multiple related terms, structural reasoning

## Output

After curating, report:
- Total cases found
- Distribution by task_type, difficulty, and review_outcome
- Any gaps in coverage
```

- [ ] **Step 2: Commit**

```bash
git add .claude/skills/find-training-cases/
git commit -m "feat: add find-training-cases skill for agentic case study curation"
```

---

### Task 6: Run full test suite and verify

**Files:** None (verification only)

- [ ] **Step 1: Run all tests**

```bash
uv run pytest -v
```

Expected: all tests pass

- [ ] **Step 2: Run type checking**

```bash
uv run mypy src/ai4c_scribe/case_studies.py src/ai4c_scribe/schema/
```

Expected: no errors (or minor issues from generated code that can be ignored)

- [ ] **Step 3: Run doctests**

```bash
uv run pytest --doctest-modules src/ai4c_scribe/case_studies.py -v
```

Expected: PASS

- [ ] **Step 4: Run linting**

```bash
uv run ruff check src/ai4c_scribe/case_studies.py src/ai4c_scribe/schema/__init__.py
```

Expected: no errors

- [ ] **Step 5: Final commit if any fixes needed**

```bash
git add -A
git commit -m "fix: address lint/type issues from case study implementation"
```

---

## Summary

| Task | What it does | Depends on |
|------|-------------|------------|
| 1 | Generate Pydantic models from LinkML | Schema (already done) |
| 2 | Case study loader module (parse, validate, convert) | Task 1 |
| 3 | Wire `input_sets_dir` into workflow config | Task 2 |
| 4 | CLI `cases validate` and `cases list` commands | Task 2 |
| 5 | `find-training-cases` agent skill | Task 4 (references CLI) |
| 6 | Full verification pass | Tasks 1-5 |
