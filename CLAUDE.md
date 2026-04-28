# CLAUDE.md for ai4c-scribe

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**ai4c-scribe** extracts training/evaluation datasets from GitHub repositories by mining pull requests. It analyzes PR metadata, code reviews, commit history, and linked issues to create rich datasets for training LLMs on code review workflows.

The project uses `uv` for dependency management and `just` as the command runner.

## Core Purpose

1. **Extract PR data** from any GitHub repository
2. **Categorize PRs** into: merged_no_mods, merged_with_mods, revised_abandoned
3. **Preserve rich context**: commits with diffs, reviews, comments, linked issues
4. **Export to JSONL** for training LLM-as-judge frameworks

## IMPORTANT INSTRUCTIONS

- We use test driven development, write tests first before implementing a feature
- Do not try and 'cheat' by making mock tests (unless asked)
- If functionality does not work, keep trying, do not relax the test just to get poor code in
- Always run tests
- Use docstrings and doctests extensively

We make heavy use of doctests, these serve as both docs and tests. `just test` will include these,
or do `just doctest` just to write doctests.

In general AVOID try/except blocks, except when these are truly called for, for example
when interfacing with external systems. For wrapping deterministic code, these are ALMOST
NEVER required, if you think you need them, it's likely a bad smell that your logic is wrong.

## Essential Commands

### Testing and Quality
- `just test` - Run all tests, type checking, and formatting checks
- `just pytest` - Run Python tests only
- `just mypy` - Run type checking
- `just format` - Run ruff linting/formatting checks
- `uv run pytest tests/test_pr_mining.py::test_mine_pr_mondo_8116` - Run a specific test

### Running the CLI
- `uv run ai4c-scribe --help` - Show all commands
- `uv run ai4c-scribe extract monarch-initiative/mondo -o output.jsonl -l 10` - Extract 10 PRs
- `uv run ai4c-scribe create-review-cases prs.jsonl -o review-cases.jsonl` - Create review cases as JSONL (formal reviews only)
- `uv run ai4c-scribe create-review-cases prs.jsonl -o review-cases.jsonl --include-implicit` - Create review cases including implicit reviews
- `uv run ai4c-scribe create-review-cases prs.jsonl -o review-cases.md -f markdown --include-implicit` - Create review cases as markdown with implicit reviews
- `uv run ai4c-scribe distill review-cases.jsonl -o vignettes/` - Distill review cases into AI-refined vignettes

### Cache Management
- `uv run ai4c-scribe cache stats` - View global cache stats
- `uv run ai4c-scribe cache stats --repo owner/name` - Repo-specific stats
- `uv run ai4c-scribe cache clear` - Clear all cache (with confirmation)
- `uv run ai4c-scribe cache clear --repo owner/name` - Clear repo cache

### Documentation
- `just _serve` - Run local documentation server with mkdocs

## Project Architecture

### Core Structure

```
src/ai4c_scribe/
├── api.py          # Clean Python API - main entry point for library users
├── cache.py        # Explicit file-based caching with structured layout
├── cli.py          # Thin CLI wrapper around api.py (presentation layer)
├── pr_mining.py    # Core PR mining logic and Pydantic models
└── _version.py     # Dynamic versioning

tests/
├── test_api.py         # Tests for Python API
├── test_cache.py       # Tests for caching (future)
├── test_cli.py         # Tests for CLI commands
├── test_pr_mining.py   # Tests for mining functionality
└── test_simple.py      # Basic smoke tests
```

### Key Design Principles

1. **Clean API Layer**: `api.py` contains all business logic. `cli.py` is just presentation.
2. **Explicit Caching**: Custom file-based cache in `.ai4cscribe/cache/` - no external dependencies
3. **Rich Models**: Pydantic models preserve all context (not just strings)
4. **GitHub CLI**: Uses `gh` CLI for API calls (simple auth, easy caching)

### Technology Stack

- **Python 3.10+** with `uv` for dependency management
- **Pydantic** for data models and validation
- **Typer** for CLI interface
- **pytest** for testing
- **mypy** for type checking
- **ruff** for linting and formatting
- **GitHub CLI (gh)** for GitHub API access

### Dependencies

Core:
- `pydantic >= 2.0.0` - Data models
- `typer >= 0.9.0` - CLI framework
- `pyyaml >= 6.0` - YAML serialization for frontmatter
- `linkml-runtime >= 1.9.4` - (legacy, may be removed)

Optional (AI features):
- `cyberian >= 0.1.0` - AI agent framework for distillation

**Note**: We do NOT use `diskcache` - we have our own explicit caching system.

## Cache System

### Cache Structure

```
.ai4cscribe/cache/
├── {org}/
│   └── {repo}/
│       ├── pr/
│       │   └── {pr_number}/
│       │       ├── pr_data.json
│       │       ├── reviews.json
│       │       ├── comments.json
│       │       ├── commits_detailed_raw.json
│       │       ├── conversation_comments.json
│       │       ├── diff_final.json
│       │       └── linked_issues.json
│       ├── issue/
│       │   └── {issue_number}/
│       │       └── issue_data.json
│       └── commit/
│           └── {sha}.json
```

### Cache Implementation

Located in `src/ai4c_scribe/cache.py`:

- `@cached_pr_endpoint(name)` - Decorator for PR-related API calls
- `@cached_issue_endpoint(name)` - Decorator for issue-related API calls
- `@cached_commit()` - Decorator for commit-related API calls
- `get_cache_stats(repo)` - Get cache statistics (returns CacheStats object)
- `clear_cache(repo)` - Clear cache for repo or all repos

**Important**: Cache decorators handle serialization/deserialization of Pydantic models automatically.

## Python API (api.py)

Library users should import from `ai4c_scribe.api`:

```python
from ai4c_scribe.api import extract_prs, create_review_cases, distill_review_cases
from ai4c_scribe.cache import get_cache_stats, clear_cache

# Extract PRs
result = extract_prs(
    repo="monarch-initiative/mondo",
    output="prs.jsonl",  # Optional
    limit=100,
    start_from=8000,  # Optional: start from PR #8000
    state="merged",   # merged, closed, or all
    one_to_one_only=False
)

# Access extraction results
print(result.total_count)              # Number of PRs extracted
print(result.category_counts)          # Dict of category -> count
print(result.one_to_one_count)         # PRs with 1-to-1 issue mapping
print(result.avg_time_to_merge_hours)  # Average merge time

# Iterate through PR records
for record in result.records:
    print(record.pr_number)
    print(record.metadata.title)
    print(record.category)  # merged_no_mods, merged_with_mods, revised_abandoned
    print(record.commits.total_commits)
    print(record.reviews.review_count)

# Create review cases from extracted PRs (JSONL format)
review_result = create_review_cases(
    input_file="prs.jsonl",
    output="review-cases.jsonl",  # Optional
    skip_no_reviews=True,
    format="jsonl"  # or "markdown"
)

# Or create as markdown
review_result_md = create_review_cases(
    input_file="prs.jsonl",
    output="review-cases.md",
    format="markdown"
)

# Access review case results
print(review_result.total_input_records)   # Number of input PRs
print(review_result.total_review_cases)    # Number of review cases created
print(review_result.skipped_no_reviews)    # PRs skipped (no reviews)

# Iterate through review cases
for case in review_result.cases:
    print(case.pr_number)
    print(case.parent_commit_sha)                  # Commit before PR
    print(case.first_revision_action)              # APPROVED, CHANGES_REQUESTED, COMMENTED
    print(case.num_reviews_in_first_revision)      # Number of reviews
    print(case.cumulative_diff_at_first_review)    # Cumulative diff
    print(case.first_revision_reviews)             # Formatted reviews markdown

# Distill review cases using AI agent (requires cyberian)
distill_result = distill_review_cases(
    input_file="review-cases.jsonl",
    output_dir="vignettes/",  # Optional
    agent_port=3284,
    input_format="jsonl"
)

# Access distillation results
print(distill_result.total_input_cases)         # Number of input cases
print(distill_result.total_distilled)           # Number of distilled cases
print(distill_result.avg_clarity)               # Average clarity rating (1-5)
print(distill_result.avg_difficulty)            # Average difficulty rating (1-5)
print(distill_result.cases_with_quality_issues) # Cases with quality issues

# Iterate through distilled cases
for distilled in distill_result.cases:
    print(distilled.pr_number)
    print(distilled.clarity)          # 1-5 rating
    print(distilled.difficulty)       # 1-5 rating
    print(distilled.quality_issues)   # Optional quality notes

# Cache management
stats = get_cache_stats("monarch-initiative/mondo")
print(f"{stats.num_files} files, {stats.total_mb:.2f} MB")
clear_cache("monarch-initiative/mondo")
```

## Data Models (pr_mining.py)

### Core Models

All models are Pydantic BaseModel instances:

**PR Mining Models:**
- `PRMiningRecord` - Top-level container for a mined PR
- `PRMetadata` - Basic PR info (number, title, body, author, dates, state)
- `PRCommitInfo` - Container for commit analysis
- `PRCommit` - Individual commit with full metadata, diff, and parent SHAs
- `PRReviewInfo` - Container for review analysis
- `PRReview` - Top-level review (APPROVED, CHANGES_REQUESTED, etc.)
- `PRReviewComment` - Line-specific code review comment (includes review_id)
- `PRIssueInfo` - Container for linked issue info
- `PRLinkedIssue` - Full issue details with comments
- `PRDiffInfo` - Initial vs final diff comparison
- `PRComment` - Generic comment model
- `PRCategory` - Enum: merged_no_mods, merged_with_mods, revised_abandoned
- `ReviewAction` - Enum for review case actions (APPROVED, CHANGES_REQUESTED, COMMENTED, IMPLICIT_REVIEW)

**Review Case Models:**
- `ReviewCase` - Review case for LLM training, capturing state at "first revision"
  - Contains: parent commit SHA, issue context, cumulative diff, and first revision reviews
  - Created from PRMiningRecord using `create_review_case_from_record(include_implicit=False)`
  - Supports both formal GitHub reviews and implicit reviews (PRs with post-PR commits + comments)
  - `first_revision_action` is a `ReviewAction` enum with values:
    - `APPROVED`: Formal review approving the PR
    - `CHANGES_REQUESTED`: Formal review requesting changes
    - `COMMENTED`: Formal review with comments only
    - `IMPLICIT_REVIEW`: No formal reviews, but evidence of iteration (commits + comments)
  - Can be exported to markdown using `.to_markdown()` method

**Distilled Review Case Models:**
- `DistilledReviewCase` - AI-refined review case with quality ratings
  - Contains: PR metadata, review state, clarity/difficulty ratings (1-5), quality issues
  - Created using `distill_review_case()` with cyberian TaskRunner
  - Can be exported to YAML frontmatter using `.to_yaml_frontmatter()` method
  - Used for creating curated training vignettes

### Key Functions

**PR Mining:**
- `mine_pr(repo, pr_number, issue_pr_graph)` - Mine a single PR
- `mine_repository(repo, limit, state, one_to_one_only, start_from)` - Mine multiple PRs
- `build_issue_pr_graph(repo, pr_numbers)` - Build issue->PR mapping
- `categorize_pr(state, merged_at, total_commits, post_review_commits)` - Categorize a PR

**Review Case Creation:**
- `detect_implicit_review_signals(record)` - Detect if PR has implicit review signals (commits after PR creation + comments)
- `create_implicit_review_case(record)` - Create ReviewCase with IMPLICIT_REVIEW action for PRs without formal reviews
- `create_review_case_from_record(record, include_implicit=False)` - Create ReviewCase from PRMiningRecord
  - Returns formal review case if available
  - If `include_implicit=True`, also creates implicit review cases when signals detected
  - Implicit reviews capture post-PR commits and discussion as evidence of iteration
- `format_comments_as_markdown(comments)` - Format comments as flat markdown
- `format_review_comments_as_markdown(reviews, comments)` - Format review feedback

**Review Case Distillation:**
- `distill_review_case(case, agent_runner)` - Distill ReviewCase using AI agent
  - Returns: `(DistilledReviewCase, vignette_text)` tuple
  - Requires cyberian TaskRunner instance
  - Agent assigns clarity and difficulty ratings, notes quality issues

## CLI Architecture (cli.py)

The CLI is a **thin wrapper** around the Python API. It only handles:
- Argument parsing (Typer)
- Progress messages
- Formatting output for terminal display
- Error handling and exit codes

**All business logic lives in api.py and pr_mining.py.**

### Commands

- `extract` - Extract PRs (calls `api.extract_prs()`)
- `create-review-cases` - Create review cases from extracted PRs (calls `api.create_review_cases()`)
- `distill` - Distill review cases into AI-refined vignettes (calls `api.distill_review_cases()`)
- `review` - Placeholder for future markdown vignette generation
- `learn` - Placeholder for end-to-end training pipeline
- `cache` - Manage cache (calls `cache.get_cache_stats()` and `cache.clear_cache()`)

## Testing

### Test Files

- `test_api.py` - Test Python API functions
- `test_cli.py` - Test CLI commands (using CliRunner)
- `test_pr_mining.py` - Test mining functions and models
- `test_simple.py` - Basic smoke tests

### Important Test Cases

- `test_mine_pr_mondo_8116` - Canonical test using PR #8116 from mondo
  - 12 commits
  - 3 CHANGES_REQUESTED reviews
  - 22 review comments
  - 1 linked issue (#7712)
  - Perfect example of review workflow

### Running Tests

```bash
just test              # All tests + mypy + ruff
just pytest            # Just pytest
uv run pytest -v       # Verbose pytest
uv run pytest tests/test_pr_mining.py::test_mine_pr_mondo_8116  # Specific test
```

## Common Tasks

### Adding a New CLI Command

1. Add function to `api.py` with business logic
2. Add thin wrapper in `cli.py` that calls the API
3. Add tests in `tests/test_api.py` and `tests/test_cli.py`
4. Run `just test`

### Adding a New Cache Endpoint

1. Add `@cached_pr_endpoint("name")` decorator to function in `pr_mining.py`
2. Ensure function signature is `(repo: str, pr_number: int, ...)`
3. Return JSON-serializable data or Pydantic models
4. Cache handles serialization automatically

### Debugging Cache Issues

```python
# Check what's cached
from ai4c_scribe.cache import get_cache_dir
print(get_cache_dir())  # .ai4cscribe/cache

# View cache structure
ls -R .ai4cscribe/cache/monarch-initiative/mondo/pr/8116/

# Clear and re-run
uv run ai4c-scribe cache clear --repo monarch-initiative/mondo
```

## Documentation

See also:
- `PR_REVIEW_DOCS.md` - Detailed documentation of PR mining data structure
- `README.md` - User-facing documentation
- Docstrings in code - Comprehensive function documentation

## Key Configuration Files

- `pyproject.toml` - Python project configuration, dependencies, and tool settings
- `justfile` - Command runner recipes for common development tasks
- `.gitignore` - Includes `.ai4cscribe/` cache directory
- `mkdocs.yml` - Documentation configuration
- `uv.lock` - Locked dependency versions

## Development Workflow

1. Dependencies are managed via `uv` - use `uv add` for new dependencies
2. All commands are run through `just` or `uv run`
3. The project uses dynamic versioning from git tags
4. Always run `just test` before committing
5. Keep CLI thin - put logic in `api.py`

## Future Work

Placeholders for future development:
- `review` command - Convert PRs to markdown vignettes
- `learn` command - End-to-end pipeline: extract → review → train
- Integration with LLM-as-judge frameworks (e.g., from langchain)
