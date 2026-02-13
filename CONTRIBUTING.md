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
Normative docs must include YAML front matter at the top of the file.

Required structure:

```yaml
---
classification: Normative
status: Draft | Active | Deprecated
version: 1.0.0
effective_date: 2026-02-13
owner: Tech4Life & Beyond LLC
last_reviewed: 2026-02-13
---
```

### Optional (recommended)

```yaml
document_id: TLOS-<AREA>-###
```

Stable identifier for audit trails.

**Rule:** The required keys must exist and must be accurate.

### Language
- Use clear and unambiguous wording.
- Normative statements should use **MUST / SHOULD / MAY** where appropriate.
- Avoid vague wording ("some", "often", "usually") in normative rules.

## Review checklist
Before opening a PR, confirm:
- [ ] Links work
- [ ] Normative docs include required metadata
- [ ] No contradictions introduced (pipeline, TOIL, governance, roles)
- [ ] Version references are consistent
- [ ] Changes are documented in `CHANGELOG.md` when doctrinal

## Governance note
TLOS is a governance repo. Small wording changes can create real operational drift.
Prefer smaller PRs and explicit rationales.
