# Agent Configurations Across Ontology Repos

## Summary Matrix

| Repo | Primary Agent | Workflow | Instruction Files | Skills/Subagents | Copilot Support |
|------|---------------|----------|-------------------|------------------|-----------------|
| **GO** | Dragon AI | `ai-agent.yml` | `CLAUDE.md` | `.claude/settings.json` only | `copilot-instructions.md` |
| **MONDO** | Dragon AI | `ai-agent.yml` (v1.0.0+ actions) | `CLAUDE.md` | 6 subagents + 1 skill | `copilot-instructions.md` |
| **Uberon** | Dragon AI | `ai-agent.yml` | `CLAUDE.md` | 6 subagents | `copilot-instructions.md` |
| **CL** | Copilot SWE | `copilot-setup-steps.yml` | `CLAUDE.md` | None | `copilot-instructions.md` |
| **EFO** | Copilot SWE | `copilot-setup-steps.yml` | None at root | None | `.github/copilot-instructions.md` |

---

## Agent Solutions by Type

### 1. Dragon AI Agent (GO, MONDO, Uberon)

**Architecture:**
- GitHub Action triggered by `@dragon-ai-agent` mentions
- Uses `dragon-ai-agent/run-goose-obo` action (wraps Claude Code)
- Controller whitelist in `.github/ai-controllers.json`
- Requires `PAT_FOR_PR` secret for PR creation

**Workflow file:** `.github/workflows/ai-agent.yml`

**Triggers:**
- Issue opened/edited
- Issue comment created/edited
- PR opened/edited
- PR review comment created/edited

**Example (MONDO - newest version):**
```yaml
- name: Respond with AI Agent
  uses: dragon-ai-agent/run-goose-obo@v1.0.4
```

**Older version (GO, Uberon):**
- Uses inline JavaScript in `actions/github-script@v6`
- Loads allowed users from `.github/ai-controllers.json`
- More complex, less modular

---

### 2. Copilot SWE Agent (CL, EFO)

**Architecture:**
- GitHub Copilot Workspace integration
- Setup steps in `.github/workflows/copilot-setup-steps.yml`
- Prepares environment (ROBOT, tools) for Copilot operations
- Copilot given its own token for operations

**Workflow file:** `.github/workflows/copilot-setup-steps.yml`

**Key difference from Dragon AI:**
- Less autonomous - requires Copilot Workspace interface
- No direct PR creation from issue mentions
- Relies on GitHub's native Copilot infrastructure

---

## Instruction Files Comparison

### GO

**Files:**
- `CLAUDE.md` - Main instructions
- `copilot-instructions.md` - Copilot-specific (likely symlink or duplicate)
- `.claude/settings.json` - Claude Code settings

**Instruction approach:** Standard ODK patterns, uses `grep/rg` for searching

---

### MONDO

**Files:**
- `CLAUDE.md` - Main instructions
- `copilot-instructions.md` - Copilot-specific
- `.claude/settings.json`
- `.claude/agents/` - 6 subagent definitions
- `.claude/skills/analyse-issue` - 1 skill

**Subagents (`.claude/agents/`):**
1. `deep-research-specialist.md`
2. `design-pattern-advisor.md`
3. `identifier-validator.md`
4. `metadata-checker.md`
5. `ontology-reasoner.md`
6. `task-coordinator.md`

**Skills (`.claude/skills/`):**
- `analyse-issue` - Issue analysis skill

**Instruction approach:** Most advanced - has specialized subagents for different task types

---

### Uberon

**Files:**
- `CLAUDE.md` - Main instructions
- `copilot-instructions.md` - Copilot-specific
- `.claude/settings.json`
- `.claude/agents/` - 6 subagent definitions (same as MONDO)

**Subagents (`.claude/agents/`):**
1. `deep-research-specialist.md`
2. `design-pattern-advisor.md`
3. `identifier-validator.md`
4. `metadata-checker.md`
5. `ontology-reasoner.md`
6. `task-coordinator.md`

**Instruction approach:** Same subagent structure as MONDO, likely from shared template

---

### CL (Cell Ontology)

**Files:**
- `CLAUDE.md` - Main instructions at root
- `copilot-instructions.md` - Copilot-specific
- No `.claude/` directory

**Key instructions in CLAUDE.md:**
- Uses `.owl` functional syntax (one axiom per line)
- Search via grep: `grep -i CL_0004177 src/ontology/cl-edit.owl`
- NTR IDs must start with CL_99xxxxx
- Signs as "GitHub Copilot"

**Instruction approach:** Minimal - relies on inline CLAUDE.md only

---

### EFO

**Files:**
- `.github/copilot-instructions.md` - In `.github/` not root
- No `CLAUDE.md` at root
- No `.claude/` directory

**Instruction approach:** Bare minimum - only copilot instructions in .github

---

## Configuration Maturity Levels

| Level | Description | Repos |
|-------|-------------|-------|
| **Advanced** | Subagents/multi-agent, Dragon AI or specialized Copilot | MONDO, Uberon, EFO* |
| **Standard** | Dragon AI workflow, CLAUDE.md, settings | GO |
| **Basic** | Copilot workflow, CLAUDE.md only | CL |

*EFO uses multi-agent Copilot system with @EFO-curator, @EFO-importer, @EFO-ontologist coordination.

---

## Correlation with Success Rates

| Repo | Config Level | First-Try Rate | Notes |
|------|--------------|----------------|-------|
| GO | Standard | 65.0% | Highest success despite simpler config |
| Uberon | Advanced | 42.9% | Subagents may help with complex tasks |
| MONDO | Advanced | 26.7% | Subagents not preventing failures |
| EFO | Advanced* | ~15%* | Multi-agent improving; early data was pessimistic |
| CL | Basic | 5.6% | Minimal config, every PR needs fixes |

*EFO reassessed per @aleixpuigb feedback - recent PRs (Nov-Dec 2025) show first-try successes.

**Key insight:** Configuration maturity correlates with success, but not perfectly. GO's higher success may reflect issue quality and simpler tasks, not just configuration.

---

## Recommendations by Repo

### CL: Urgent Upgrades Needed

1. **Add `.claude/` directory** with settings
2. **Create specialized subagents** for:
   - hasDbXref format validation
   - Synonym type checking
   - Species suffix validation
3. **Add pre-edit hooks** for format checking
4. **Consider Dragon AI workflow** instead of Copilot-only

### EFO: Major Configuration Gap

1. **Add `CLAUDE.md` at root** (not just in .github)
2. **Add `.claude/` directory** with settings
3. **Add Dragon AI workflow** or improve Copilot integration
4. **Create duplicate PR prevention** instructions prominently

### GO: Consider Adding Subagents

1. **Add specialized obsoletion subagent** - GO's main failure mode
2. **Consider identifier validator** subagent for term IDs

### MONDO/Uberon: Refine Existing Subagents

1. **Add duplicate PR detection** to task-coordinator
2. **Enhance identifier-validator** for PMID format
3. **Add annotation format checker** for MONDO-specific patterns

---

## Template Recommendations

Based on this analysis, ontology repos should adopt:

```
repo/
├── CLAUDE.md                    # Main agent instructions
├── AGENTS.md                    # -> symlink to CLAUDE.md (future standard)
├── copilot-instructions.md      # -> symlink to CLAUDE.md
├── .claude/
│   ├── settings.json            # Claude Code settings
│   ├── agents/                  # Subagent definitions
│   │   ├── task-coordinator.md
│   │   ├── identifier-validator.md
│   │   ├── metadata-checker.md
│   │   └── [ontology-specific].md
│   └── skills/                  # Reusable skills
│       └── [ontology-specific]/
└── .github/
    ├── workflows/
    │   ├── ai-agent.yml         # Dragon AI triggers
    │   └── copilot-setup-steps.yml
    ├── ai-controllers.json      # Allowed users
    └── copilot-instructions.md  # Backup copy
```

---

## Version Comparison: Dragon AI Workflows

### Newer (MONDO)
```yaml
uses: dragon-ai-agent/github-mention-detector@v1.0.0
uses: dragon-ai-agent/run-goose-obo@v1.0.4
```
- Modular action components
- Cleaner, more maintainable

### Older (GO, Uberon)
```yaml
uses: actions/github-script@v6
# Inline JavaScript for detection
```
- Complex inline scripts
- Harder to maintain/update

**Recommendation:** All repos should upgrade to the MONDO-style modular actions.

---

## Instruction Content Analysis

### Line Count Summary

| Repo | Instruction File | Lines | Words (approx) |
|------|------------------|-------|----------------|
| **EFO** | `.github/copilot-instructions.md` | 636 | ~4,500 |
| **MONDO** | `CLAUDE.md` | 432 | ~3,000 |
| **GO** | `CLAUDE.md` | 190 | ~1,400 |
| **Uberon** | `CLAUDE.md` | 148 | ~1,100 |
| **CL** | `CLAUDE.md` | 133 | ~1,000 |

**Insight:** EFO has by far the most verbose instructions (636 lines) but 0% first-try success rate. This suggests instruction volume alone doesn't drive success - instruction quality and specificity matter more.

---

### GO Instructions Summary (190 lines)

**Key Characteristics:**
- Uses `.obo` format with checkout/checkin workflow
- Search via `obo-grep.pl` (custom tool)
- NTR IDs start with `GO:777xxxx`
- Signs commits as `@dragon-ai-agent`

**Unique Features:**
- **Namespace requirements:** GO requires `namespace:` tag on all terms
- **Logical definitions:** Detailed guidance on genus-differentia form
- **Reaction terms:** Special guidance for RHEA mappings with skos qualifiers
- **Taxon constraints:** Separate files in `src/taxon_constraints/`

**Obsoletion Pattern (detailed):**
```obo
[Term]
id: GO:0000170
name: obsolete sphingosine hydroxylase activity
namespace: molecular_function
def: "OBSOLETE. ..." [PMID:xxx]
comment: The reason for obsoletion...
property_value: term_tracker_item "https://github.com/.../issues/29717" xsd:anyURI
is_obsolete: true
replaced_by: GO:0102772
```

**Validation:** `robot convert --catalog ... -i go-edit.obo -f obo -o go-edit.TMP.obo`

---

### MONDO Instructions Summary (432 lines)

**Key Characteristics:**
- Uses `.obo` format with checkout/checkin workflow
- Search via `obo-grep.pl --noheader`
- NTR IDs start with `MONDO:777xxxx`
- Requires `sh run.sh make NORM` before committing

**Unique Features:**
- **Excluded subclass tracking:** When removing is_a, add `excluded_subClassOf` annotation
- **Mapping metadata:** Complex `source` qualifier patterns (e.g., `MONDO:equivalentTo`)
- **Gene-disease naming:** Explicit pattern `{GENE}-related {disease description}`
- **Synonym attribution:** All synonyms MUST have citations (never `[]`)
- **Design pattern compliance:** Must check `src/patterns/dosdp-patterns/*.yaml`

**Obsoletion Pattern:**
```obo
[Term]
id: MONDO:0100334
name: obsolete viral infectious disease or sequela
property_value: http://purl.org/dc/terms/creator https://orcid.org/...
property_value: IAO:0000231 MONDO:TermsMerged  # or OMO:0001000
property_value: IAO:0000233 "https://github.com/.../issues/XXXX" xsd:anyURI
is_obsolete: true
replaced_by: MONDO:0100321
```

**Extensive sections on:**
- Gene identifier verification (HGNC for human, NCBI Gene for other species)
- Susceptibility vs disease relationships
- Complete exemplar stanzas

---

### Uberon Instructions Summary (148 lines)

**Key Characteristics:**
- Uses `.obo` format with checkout/checkin workflow
- Search via `obo-grep.pl`
- NTR IDs start with `UBERON:99xxxxx`
- Requires `robot convert -i uberon-edit.obo -f obo -o uberon-edit.obo` before commit

**Unique Features:**
- **Contributor metadata required:** New terms MUST have:
  ```obo
  relationship: dc-contributor https://orcid.org/<ORCID> ! <NAME>
  property_value: dcterms-date "<ISO-TIMESTAMP>" xsd:dateTime
  ```
- **Part_of relationships:** Many anatomical terms have part_of to other UBERON terms

**Obsoletion Pattern (simpler than GO/MONDO):**
```obo
[Term]
id: UBERON:0001050
name: obsolete atrium
comment: obsoleted because...
is_obsolete: true
consider: FMA:85574
consider: UBERON:0002081
```

---

### CL Instructions Summary (133 lines)

**Key Characteristics:**
- Uses `.owl` functional syntax (one axiom per line)
- Search via `grep` directly on `cl-edit.owl`
- NTR IDs start with `CL_99xxxxx`
- Signs as "GitHub Copilot"

**Notable Gaps (contributing to low success rate):**
- No explicit hasDbXref format guidance (major failure pattern)
- No synonym type guidance (EXACT vs RELATED)
- No species suffix guidance (Mmus)
- No example obsoletion stanza
- No mention of the checkout/checkin workflow

**Search Pattern:**
```bash
grep -i CL_0004177 src/ontology/cl-edit.owl
grep 'AnnotationAssertion(rdfs:label "neuron"' src/ontology/cl-edit.owl
```

**What's missing vs GO/MONDO:**
- No detailed obsoletion conventions
- No logical definition examples
- No contributor metadata requirements
- No normalization step before commit

---

### EFO Instructions Summary (636 lines)

**Key Characteristics:**
- Uses `.owl` OWL/XML format
- Search via `grep` on `efo-edit.owl`
- NTR IDs start with `EFO_092xxxx`
- Requires `make normalize_src` after edits

**Unique Features:**
- **Multi-agent coordination:** Explicit workflow with 3 specialized agents:
  - `@EFO-curator` - Literature research, evidence gathering
  - `@EFO-importer` - External term imports (MUST be delegated)
  - `@EFO-ontologist` - Direct OWL/XML editing
- **Import policy:** ALL imports delegated to @EFO-importer agent
- **PMID requirements:** Minimum 2 PMIDs required for new terms
- **OLS search mandatory:** Must check OLS before creating terms

**Obsoletion Pattern:**
```xml
<owl:Class rdf:about="http://www.ebi.ac.uk/efo/EFO_1000022">
    <obo:IAO_0100001>http://www.ebi.ac.uk/efo/EFO_1000172</obo:IAO_0100001>
    <efo:obsoleted_in_version>2.65</efo:obsoleted_in_version>
    <efo:reason_for_obsolescence>use : EFO_1000172...</efo:reason_for_obsolescence>
    <rdfs:label>obsolete_cervical squamous cell carcinoma</rdfs:label>
    <owl:deprecated rdf:datatype="...">true</owl:deprecated>
</owl:Class>
```

**Updated Assessment (per @aleixpuigb feedback):**
- Our original data extraction missed recent successful PRs (Nov-Dec 2025)
- Recent PRs show improved success: #2583, #2581, #2550 were first-try successes
- The multi-agent system appears to be maturing
- Early failures (duplicate PRs for #2490) may not reflect current performance

**Remaining concerns:**
- 636 lines is still verbose - could be streamlined
- Multi-agent coordination adds complexity that may confuse some tasks
- Import delegation workflow creates dependencies between agents

---

### Instruction Quality vs Success Rate

| Repo | Lines | Key Sections | Obsoletion Example | First-Try Rate |
|------|-------|--------------|-------------------|----------------|
| GO | 190 | Layout, Edit workflow, OBO guidelines, Obsoletion, Logical defs | Yes (detailed) | **65.0%** |
| MONDO | 432 | Layout, Edit workflow, Mappings, Obsoletion, Design patterns, Genes | Yes (with IAO) | 26.7% |
| Uberon | 148 | Layout, Edit workflow, Obsoletion, Contributor metadata | Yes (simple) | 42.9% |
| CL | 133 | Layout, Grep search, GitHub process, OBO guidelines | **None** | **5.6%** |
| EFO | 636 | Multi-agent, Imports, Obsoletion, Validation, OLS search | Yes (XML) | **~15%*** |

*EFO rate updated per @aleixpuigb feedback - recent PRs (Nov-Dec 2025) show improved success not captured in original extraction.

**Key Observations:**

1. **GO succeeds with moderate instructions** - Focused, clear, includes key examples
2. **MONDO has most detailed instructions** but complex multi-pattern requirements hurt
3. **CL lacks critical examples** - No obsoletion, no format guidance = systematic failures
4. **EFO's multi-agent system is improving** - Recent PRs show better success than early data suggested

---

### Common Instruction Patterns That Work

All successful repos share:
1. **Explicit search commands** - `obo-grep.pl` or `grep` patterns
2. **Checkout/checkin workflow** - For .obo format repos
3. **NTR ID range** - Clear guidance on new term IDs
4. **Validation command** - `robot convert` with specific flags
5. **At least one obsoletion example** - Shows exact format

### Missing Patterns in Failing Repos

**CL is missing:**
- Obsoletion example stanza
- hasDbXref format guidance
- Synonym type rules (EXACT vs RELATED)
- Species suffix convention

**EFO is missing:**
- Simple, direct instructions (buried in multi-agent complexity)
- Focus on preventing duplicate PRs
- Learning from prior failures

---

### Recommendations for Instruction Improvement

**For CL (to improve from 5.6%):**
```markdown
## hasDbXref Format (CRITICAL)
For PMID citations, use oboInOwl:hasDbXref:
- CORRECT: hasDbXref "PMID:12345678"
- WRONG: dc:source "PMID:12345678"

## Synonym Types
- EXACT: True synonyms with identical meaning
- RELATED: Abbreviations, informal names
- When in doubt, use RELATED

## Species Suffix
For mouse-specific terms, add "(Mmus)" to label:
- CORRECT: "alpha retinal ganglion cell (Mmus)"
- WRONG: "alpha retinal ganglion cell"

## Obsoletion Example
[Add concrete .owl example here]
```

**For EFO (continue improving from ~15%):**
1. Add `CLAUDE.md` at root (not buried in .github) - for discoverability
2. Consider streamlining the 636-line instructions - focus on most common tasks
3. The multi-agent system is working - document successful patterns from recent PRs
4. Continue emphasis on duplicate PR prevention (early failures were mostly duplicates)
5. Add pre-submission checklist based on recent success patterns

---

*Generated: 2025-12-22*
*Based on GitHub API inspection of 5 ontology repos*
