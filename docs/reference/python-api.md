# Python API reference

For developers who want to use ai4c-scribe as a library.

## Installation

```bash
# Basic installation
uv sync

# With AI dependencies (for distill)
uv pip install -e ".[ai]"
```

## Import

```python
from ai4c_scribe.api import extract_prs, create_review_cases, distill_review_cases
from ai4c_scribe.cache import get_cache_stats, clear_cache
from ai4c_scribe.pr_mining import (
    mine_pr,
    mine_repository,
    PRMiningRecord,
    ReviewCase,
    create_review_case_from_record,
)
```

---

## High-level API (api.py)

### extract_prs

Extract PRs from a GitHub repository.

```python
def extract_prs(
    repo: str,
    output: Optional[str] = None,
    limit: int = 50,
    start_from: Optional[int] = None,
    state: str = "merged",
    one_to_one_only: bool = False,
) -> ExtractionResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `repo` | str | Required | Repository in `owner/repo` format |
| `output` | str | None | Output JSONL file path |
| `limit` | int | 50 | Maximum PRs to process |
| `start_from` | int | None | Start from this PR number |
| `state` | str | "merged" | PR state filter |
| `one_to_one_only` | bool | False | Only 1-to-1 issue mappings |

**Returns:** `ExtractionResult`

**Example:**

```python
from ai4c_scribe.api import extract_prs

# Extract and save to file
result = extract_prs(
    "monarch-initiative/mondo",
    output="prs.jsonl",
    limit=100
)

print(f"Extracted {result.total_count} PRs")
print(f"Categories: {result.category_counts}")

# Access records directly
for record in result.records:
    print(f"PR #{record.pr_number}: {record.metadata.title}")
```

---

### create_review_cases

Create review cases from extracted PRs.

```python
def create_review_cases(
    input_file: str,
    output: Optional[str] = None,
    skip_no_reviews: bool = True,
    format: str = "jsonl",
) -> CreateReviewCasesResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_file` | str | Required | Input JSONL from `extract_prs` |
| `output` | str | None | Output file path |
| `skip_no_reviews` | bool | True | Skip PRs without reviews |
| `format` | str | "jsonl" | Output format |

**Returns:** `CreateReviewCasesResult`

**Example:**

```python
from ai4c_scribe.api import create_review_cases

result = create_review_cases(
    "prs.jsonl",
    output="cases.jsonl"
)

print(f"Created {result.total_review_cases} review cases")
print(f"Skipped {result.skipped_no_reviews} PRs without reviews")

for case in result.cases:
    print(f"PR #{case.pr_number}: {case.first_revision_action}")
```

---

### distill_review_cases

Distill review cases into AI-refined vignettes.

```python
def distill_review_cases(
    input_file: str,
    output_dir: Optional[str] = None,
    input_format: str = "jsonl",
    working_dir: Optional[str] = None,
    repo_worktree: Optional[str] = None,
    verbose: int = 0,
) -> DistillResult
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_file` | str | Required | Input from `create_review_cases` |
| `output_dir` | str | None | Output directory for vignettes |
| `input_format` | str | "jsonl" | Input format |
| `working_dir` | str | None | Working directory for agents |
| `repo_worktree` | str | None | Git worktree for exploration |
| `verbose` | int | 0 | Verbosity level |

**Returns:** `DistillResult`

**Example:**

```python
from ai4c_scribe.api import distill_review_cases

result = distill_review_cases(
    "cases.jsonl",
    output_dir="vignettes/"
)

print(f"Distilled {result.total_distilled} cases")
print(f"Average clarity: {result.avg_clarity:.2f}")
print(f"Average difficulty: {result.avg_difficulty:.2f}")
```

---

## Result classes

### ExtractionResult

```python
class ExtractionResult:
    records: list[PRMiningRecord]
    output_file: Optional[Path]
    total_count: int
    category_counts: dict[str, int]
    one_to_one_count: int
    avg_time_to_merge_hours: Optional[float]
```

### CreateReviewCasesResult

```python
class CreateReviewCasesResult:
    cases: list[ReviewCase]
    output_file: Optional[Path]
    total_input_records: int
    total_review_cases: int
    skipped_no_reviews: int
```

### DistillResult

```python
class DistillResult:
    cases: list[DistilledReviewCase]
    output_directory: Optional[Path]
    total_input_cases: int
    total_distilled: int
    avg_clarity: float
    avg_difficulty: float
    cases_with_quality_issues: int
```

---

## Cache API (cache.py)

### get_cache_stats

Get cache statistics.

```python
def get_cache_stats(repo: Optional[str] = None) -> CacheStats
```

**Example:**

```python
from ai4c_scribe.cache import get_cache_stats

# Global stats
stats = get_cache_stats()
print(f"Total: {stats.num_files} files, {stats.total_mb:.2f} MB")

# Repository-specific
stats = get_cache_stats("monarch-initiative/mondo")
print(f"Mondo: {stats.num_files} files")
```

### clear_cache

Clear cached data.

```python
def clear_cache(repo: Optional[str] = None) -> None
```

**Example:**

```python
from ai4c_scribe.cache import clear_cache

# Clear specific repo
clear_cache("monarch-initiative/mondo")

# Clear all
clear_cache()
```

### CacheStats

```python
class CacheStats:
    num_files: int
    total_bytes: int
    total_mb: float
    avg_file_size_kb: float
```

---

## Low-level API (pr_mining.py)

For advanced use cases, access the mining functions directly.

### mine_pr

Mine a single PR.

```python
def mine_pr(
    repo: str,
    pr_number: int,
    issue_pr_graph: Optional[dict[int, list[int]]] = None,
) -> PRMiningRecord
```

**Example:**

```python
from ai4c_scribe.pr_mining import mine_pr

record = mine_pr("monarch-initiative/mondo", 8116)
print(f"Title: {record.metadata.title}")
print(f"Commits: {record.commits.total_commits}")
print(f"Reviews: {record.reviews.review_count}")
```

### mine_repository

Mine multiple PRs from a repository.

```python
def mine_repository(
    repo: str,
    limit: Optional[int] = None,
    state: str = "merged",
    one_to_one_only: bool = False,
    start_from: Optional[int] = None,
) -> list[PRMiningRecord]
```

### create_review_case_from_record

Create a ReviewCase from a PRMiningRecord.

```python
def create_review_case_from_record(record: PRMiningRecord) -> Optional[ReviewCase]
```

Returns `None` if the PR has no reviews.

---

## See also

- [Data structures](data-structures.md): Pydantic model reference
- [CLI reference](cli.md): Command-line interface
- [How-to guides](../how-to/index.md): Practical examples
