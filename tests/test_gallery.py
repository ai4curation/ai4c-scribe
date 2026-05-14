"""Tests for gallery browser generation."""

from pathlib import Path

from ai4c_scribe.gallery import collect_gallery_data, generate_gallery


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
    assert "Add new term: foo bar" in content
    assert "Reclassify baz widget" in content


def test_generate_gallery_embeds_diff_data(tmp_path):
    """Generated HTML contains embedded diff content."""
    output = tmp_path / "gallery.html"
    generate_gallery(FIXTURE_DIR, output)
    content = output.read_text()
    assert "+name: foo bar" in content


def test_collect_case_without_results():
    """Cases with no scores/diffs still load with empty agent_attempts."""
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
