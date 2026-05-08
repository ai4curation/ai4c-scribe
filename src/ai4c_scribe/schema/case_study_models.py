from datetime import (
    date
)
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel
)


metamodel_version = "None"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )
    pass




class LinkMLMeta(RootModel):
    root: Dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'https://w3id.org/ai4c-scribe/case-study/',
     'default_range': 'string',
     'description': 'Schema for evaluation case study frontmatter. Each case study '
                    'describes one issue/PR pair suitable for agent evaluation '
                    'replay.',
     'id': 'https://w3id.org/ai4c-scribe/case-study',
     'imports': ['linkml:types'],
     'name': 'case_study',
     'prefixes': {'ai4cs': {'prefix_prefix': 'ai4cs',
                            'prefix_reference': 'https://w3id.org/ai4c-scribe/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'}},
     'source_file': 'src/ai4c_scribe/schema/case_study.yaml',
     'title': 'Case Study Schema'} )

class TaskTypeEnum(str, Enum):
    """
    The primary type of work performed in the PR
    """
    # Adding a new ontology term
    new_term = "new_term"
    # Obsoleting an existing term
    obsoletion = "obsoletion"
    # Moving a term in the hierarchy
    reclassification = "reclassification"
    # Adding or modifying synonyms
    synonym_update = "synonym_update"
    # Fixing logical axioms or definitions
    axiom_repair = "axiom_repair"
    # Batch changes across many terms
    bulk_edit = "bulk_edit"
    # Documentation or metadata-only changes
    documentation = "documentation"
    # Does not fit other categories
    other = "other"


class DifficultyEnum(str, Enum):
    """
    Estimated difficulty for an agent to reproduce the fix
    """
    # Straightforward, mechanical change
    simple = "simple"
    # Requires some domain knowledge or multi-step reasoning
    medium = "medium"
    # Complex reasoning, multiple interacting changes, or deep domain expertise
    hard = "hard"


class ScopeEnum(str, Enum):
    """
    Scope of the changes in the PR
    """
    # Changes affect a single term
    single_term = "single_term"
    # Changes affect multiple terms
    multi_term = "multi_term"
    # Broad structural or organizational changes
    structural_refactor = "structural_refactor"


class ReviewOutcomeEnum(str, Enum):
    """
    How the PR review process went
    """
    # PR approved without revision requests
    approved_first_time = "approved_first_time"
    # One round of changes requested before merge
    changes_requested = "changes_requested"
    # Multiple rounds of review feedback before merge
    multiple_rounds = "multiple_rounds"


class ScopingEnum(str, Enum):
    """
    How well-scoped the PR is relative to its issue
    """
    # All changes directly address the issue, no unrelated modifications
    tightly_scoped = "tightly_scoped"
    # Primary changes address the issue, minor incidental cleanup included
    mostly_scoped = "mostly_scoped"
    # Significant unrelated changes mixed in, harder to isolate the fix
    loosely_scoped = "loosely_scoped"



class FileChange(ConfiguredBaseModel):
    """
    A single file changed in the PR, with line counts.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4c-scribe/case-study'})

    path: str = Field(default=..., description="""File path relative to repo root""", json_schema_extra = { "linkml_meta": {'alias': 'path', 'domain_of': ['FileChange']} })
    additions: int = Field(default=..., description="""Number of lines added""", json_schema_extra = { "linkml_meta": {'alias': 'additions', 'domain_of': ['FileChange']} })
    deletions: int = Field(default=..., description="""Number of lines deleted""", json_schema_extra = { "linkml_meta": {'alias': 'deletions', 'domain_of': ['FileChange']} })


class CaseStudy(ConfiguredBaseModel):
    """
    A single issue/PR evaluation case. Represented as YAML frontmatter in a markdown file, with the markdown body containing an agentic narrative summary of the issue and its resolution.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://w3id.org/ai4c-scribe/case-study'})

    repo: str = Field(default=..., description="""Repository in owner/name format""", json_schema_extra = { "linkml_meta": {'alias': 'repo',
         'domain_of': ['CaseStudy'],
         'examples': [{'value': 'geneontology/go-ontology'},
                      {'value': 'monarch-initiative/mondo'}]} })
    issue_number: int = Field(default=..., description="""GitHub issue number""", json_schema_extra = { "linkml_meta": {'alias': 'issue_number', 'domain_of': ['CaseStudy']} })
    pr_number: int = Field(default=..., description="""PR number of the human's actual fix""", json_schema_extra = { "linkml_meta": {'alias': 'pr_number', 'domain_of': ['CaseStudy']} })
    issue_title: str = Field(default=..., description="""Issue title at time of curation""", json_schema_extra = { "linkml_meta": {'alias': 'issue_title', 'domain_of': ['CaseStudy']} })
    issue_labels: Optional[List[str]] = Field(default=None, description="""GitHub labels on the issue""", json_schema_extra = { "linkml_meta": {'alias': 'issue_labels', 'domain_of': ['CaseStudy']} })
    issue_created_at: date = Field(default=..., description="""When the issue was created""", json_schema_extra = { "linkml_meta": {'alias': 'issue_created_at', 'domain_of': ['CaseStudy']} })
    issue_closed_at: Optional[date] = Field(default=None, description="""When the issue was closed""", json_schema_extra = { "linkml_meta": {'alias': 'issue_closed_at', 'domain_of': ['CaseStudy']} })
    pr_author: str = Field(default=..., description="""PR author GitHub username""", json_schema_extra = { "linkml_meta": {'alias': 'pr_author', 'domain_of': ['CaseStudy']} })
    pr_merged_at: Optional[date] = Field(default=None, description="""When the PR was merged""", json_schema_extra = { "linkml_meta": {'alias': 'pr_merged_at', 'domain_of': ['CaseStudy']} })
    pr_num_commits: Optional[int] = Field(default=None, description="""Number of commits in the PR""", json_schema_extra = { "linkml_meta": {'alias': 'pr_num_commits', 'domain_of': ['CaseStudy']} })
    milestone: Optional[str] = Field(default=None, description="""GitHub milestone name""", json_schema_extra = { "linkml_meta": {'alias': 'milestone', 'domain_of': ['CaseStudy']} })
    files_changed: Optional[List[FileChange]] = Field(default=None, description="""Files modified in the PR with line change counts""", json_schema_extra = { "linkml_meta": {'alias': 'files_changed', 'domain_of': ['CaseStudy']} })
    scoping: ScopingEnum = Field(default=..., description="""Assessment of how well-scoped the PR is""", json_schema_extra = { "linkml_meta": {'alias': 'scoping', 'domain_of': ['CaseStudy']} })
    scoping_notes: Optional[str] = Field(default=None, description="""Brief explanation of scoping assessment. Note any unrelated changes, scope creep, or reasons the PR is not cleanly scoped.""", json_schema_extra = { "linkml_meta": {'alias': 'scoping_notes', 'domain_of': ['CaseStudy']} })
    task_type: TaskTypeEnum = Field(default=..., description="""Primary task type for this case""", json_schema_extra = { "linkml_meta": {'alias': 'task_type', 'domain_of': ['CaseStudy']} })
    difficulty: DifficultyEnum = Field(default=..., description="""Estimated difficulty level""", json_schema_extra = { "linkml_meta": {'alias': 'difficulty', 'domain_of': ['CaseStudy']} })
    scope: ScopeEnum = Field(default=..., description="""Scope of changes in the PR""", json_schema_extra = { "linkml_meta": {'alias': 'scope', 'domain_of': ['CaseStudy']} })
    review_outcome: ReviewOutcomeEnum = Field(default=..., description="""How the review process went""", json_schema_extra = { "linkml_meta": {'alias': 'review_outcome', 'domain_of': ['CaseStudy']} })
    domain_area: Optional[str] = Field(default=None, description="""Free-form domain area (e.g. cellular-component, infectious-disease)""", json_schema_extra = { "linkml_meta": {'alias': 'domain_area', 'domain_of': ['CaseStudy']} })
    tags: Optional[List[str]] = Field(default=None, description="""Free-form additional tags for filtering""", json_schema_extra = { "linkml_meta": {'alias': 'tags', 'domain_of': ['CaseStudy']} })
    curated_by: str = Field(default=..., description="""Who or what created this case study (agent model, human username)""", json_schema_extra = { "linkml_meta": {'alias': 'curated_by', 'domain_of': ['CaseStudy']} })
    curated_at: date = Field(default=..., description="""When this case study was curated""", json_schema_extra = { "linkml_meta": {'alias': 'curated_at', 'domain_of': ['CaseStudy']} })
    rationale: str = Field(default=..., description="""One-liner explaining why this is a good test case""", json_schema_extra = { "linkml_meta": {'alias': 'rationale', 'domain_of': ['CaseStudy']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
CaseStudy.model_rebuild()
FileChange.model_rebuild()

