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
    assert case.task_type == "new_term"
    assert case.difficulty == "simple"
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
