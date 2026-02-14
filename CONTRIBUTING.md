---
document_id: TLOS-CONTRIB-001
classification: Normative
status: Active
version: 1.0.0
effective_date: 2026-02-13
last_reviewed: 2026-02-13
owner: Tech4Life Governance (TLOS)
last_reviewed_by: optional
---
# Contributing to TLOS

This repository is the governance and doctrine layer for Tech4Life & Beyond.

## Scope
- Governance standards
- Normative doctrine (how we operate)
- Factory standards (how we create products)
- Terminology and definitions
- Cross-repo operating contracts (high-level)

## Contribution workflow
1. Create a branch from `main`
2. Make focused changes
3. Ensure the repo remains internally consistent
4. Open a Pull Request (PR)
5. Merge only after checks pass and required reviewers approve

## Document standards

### Normative vs informative
- **Normative** documents define mandatory standards.
- **Informative** documents explain, guide, or provide examples.

If a document is normative, it must be auditable and versioned.

### Required header metadata (for normative docs)

Normative docs MUST include YAML front matter at the top of the file.

Required structure:

```yaml
---
document_id: TLOS-<AREA>-###      # stable identifier for audit trails
classification: Normative
status: Draft | Active | Deprecated
version: 1.0.0
effective_date: YYYY-MM-DD
last_reviewed: YYYY-MM-DD
owner: <owner>
---
```

### Optional (recommended)

```yaml
last_reviewed_by: <name or role>
```

**Rule:** Required keys must exist and be accurate.

### Normative language
Use RFC-2119 style language in normative content:
- **MUST / MUST NOT**: non-negotiable requirement or prohibition.
- **SHOULD / SHOULD NOT**: strong recommendation; deviations require explicit rationale.
- **MAY**: optional behavior.

Do not use MUST/SHOULD/MAY for narrative text, examples, aspirations, or historical context.

### Versioning rule
TLOS normative documents use `MAJOR.MINOR.PATCH`.

## Review checklist
Before opening a PR, confirm:
- [ ] Links work
- [ ] Normative docs include required metadata
- [ ] No contradictions introduced (pipeline, TOIL, governance, roles)
- [ ] Versioning and changelog are updated if needed
- [ ] ADR included for governance-impacting decisions

## Pull requests
PRs should include:
- What changed
- Why it changed
- Whether it is breaking/additive/editorial
- Any migration implications

Use `.github/pull_request_template.md` checklist for doctrinal compliance.
