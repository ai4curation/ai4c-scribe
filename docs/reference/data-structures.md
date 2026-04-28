# Data structures reference

Complete reference for all Pydantic models used in ai4c-scribe.

## PR Mining Models

### PRMiningRecord

Top-level container for a mined PR.

```python
class PRMiningRecord(BaseModel):
    pr_number: int
    repository: str                        # "owner/repo"
    category: PRCategory
    metadata: PRMetadata
    commits: PRCommitInfo
    reviews: PRReviewInfo
    issues: PRIssueInfo
    diff_info: PRDiffInfo
    pr_comments: list[PRComment]
    time_to_merge_hours: Optional[float]
    time_to_first_review_hours: Optional[float]
```

---

### PRCategory

Enum for PR categorization.

```python
class PRCategory(str, Enum):
    MERGED_NO_MODS = "merged_no_mods"
    MERGED_WITH_MODS = "merged_with_mods"
    REVISED_ABANDONED = "revised_abandoned"
```

---

### PRMetadata

Basic PR information.

```python
class PRMetadata(BaseModel):
    number: int
    title: str
    body: str
    author: str                            # GitHub username
    state: str                             # MERGED, CLOSED, OPEN
    created_at: datetime
    merged_at: Optional[datetime]
    closed_at: Optional[datetime]
    url: str
```

---

### PRCommitInfo

Container for commit data.

```python
class PRCommitInfo(BaseModel):
    total_commits: int
    initial_commit_sha: str
    initial_commit_date: datetime
    post_review_commits: int
    commit_details: list[PRCommit]
```

### PRCommit

Individual commit with diff.

```python
class PRCommit(BaseModel):
    sha: str                               # Full commit SHA
    message_headline: str                  # First line
    message_body: str                      # Rest of message
    author_name: str
    author_email: str
    authored_date: datetime
    committed_date: datetime
    parent_shas: list[str]
    diff: Optional[str]                    # Patch for this commit
```

---

### PRReviewInfo

Container for review data.

```python
class PRReviewInfo(BaseModel):
    review_count: int
    comment_count: int
    changes_requested_count: int
    approved_count: int
    reviews: list[PRReview]
    review_comments: list[PRReviewComment]
    first_review_date: Optional[datetime]
```

### PRReview

Top-level review.

```python
class PRReview(BaseModel):
    id: str
    author: str
    state: str                             # APPROVED, CHANGES_REQUESTED, COMMENTED, DISMISSED
    body: str
    submitted_at: datetime
    commit_id: str
```

### PRReviewComment

Line-specific inline comment.

```python
class PRReviewComment(BaseModel):
    id: str
    review_id: str                         # Parent review ID
    author: str
    body: str
    created_at: datetime
    path: str                              # File path
    commit_id: str
    diff_hunk: str                         # Diff context
    url: str
```

---

### PRIssueInfo

Container for linked issue data.

```python
class PRIssueInfo(BaseModel):
    linked_issues: list[int]
    is_one_to_one: bool
    issue_details: list[PRLinkedIssue]
```

### PRLinkedIssue

Full issue with comments.

```python
class PRLinkedIssue(BaseModel):
    number: int
    title: str
    author: str
    body: str
    created_at: datetime
    url: str
    comments_before_pr: list[PRComment]
    all_comments: list[PRComment]
```

---

### PRDiffInfo

Initial and final diff comparison.

```python
class PRDiffInfo(BaseModel):
    initial_diff: Optional[str]
    final_diff: Optional[str]
    diffs_are_identical: bool
    initial_diff_size_lines: int
    final_diff_size_lines: int
```

---

### PRComment

Generic comment model.

```python
class PRComment(BaseModel):
    id: str
    author: str
    body: str
    created_at: datetime
    url: str
```

---

## Review Case Models

### ReviewCase

Training case for LLM code reviewers.

```python
class ReviewCase(BaseModel):
    pr_number: int
    repository: str
    linked_issue_number: Optional[int]
    linked_issue_title: Optional[str]
    issue_context: str                     # Issue discussion before PR
    parent_commit_sha: str                 # Repo state before PR
    cumulative_diff_at_first_review: str
    first_revision_action: str             # APPROVED, CHANGES_REQUESTED, COMMENTED
    num_reviews_in_first_revision: int
    first_revision_reviews: str            # Formatted markdown
```

**Methods:**

```python
def to_markdown(self) -> str:
    """Convert to markdown format."""
```

---

## Distilled Review Case Models

### DistilledReviewCase

AI-refined review case with quality ratings.

```python
class DistilledReviewCase(BaseModel):
    pr_number: int
    repository: str
    linked_issue_number: Optional[int]
    first_revision_action: str
    num_reviews_in_first_revision: int
    clarity: int                           # 1-5 rating
    difficulty: int                        # 1-5 rating
    quality_issues: Optional[str]
```

**Methods:**

```python
def to_yaml_frontmatter(self) -> str:
    """Convert to YAML frontmatter string."""
```

---

## Cache Models

### CacheStats

Cache statistics.

```python
class CacheStats(BaseModel):
    num_files: int
    total_bytes: int
    total_mb: float
    avg_file_size_kb: float
```

---

## Serialization

All models are Pydantic `BaseModel` instances with:

- JSON serialization via `model_dump_json()`
- JSON deserialization via `Model.model_validate(data)`
- JSONL format: one JSON object per line

**Example:**

```python
# Serialize
json_str = record.model_dump_json()

# Deserialize
record = PRMiningRecord.model_validate(json.loads(json_str))
```

---

## DateTime handling

All datetime fields are timezone-aware (UTC):

```python
# Parsing
dt = datetime.fromisoformat(date_string.replace("Z", "+00:00"))

# Serialization
json_str = dt.isoformat()  # "2024-08-27T06:25:10+00:00"
```

---

## See also

- [Python API](python-api.md): Functions using these models
- [Output format](output-format.md): File format details
- [Data model explanation](../explanation/data-model.md): Conceptual overview
