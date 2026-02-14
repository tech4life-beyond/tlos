---
document_id: TLOS-RELEASE-001
classification: Normative
status: Active
version: 1.0.0
effective_date: 2026-02-13
last_reviewed: 2026-02-13
owner: Tech4Life Governance (TLOS)
last_reviewed_by: optional
---
# Releasing & Versioning (TLOS)

TLOS is a governance standard. It evolves, but changes MUST be auditable and predictable.

## Versioning convention

### Normative standard version
- Applies to normative doctrine (governance model, lifecycle doctrine, integration requirements).
- Format: `MAJOR.MINOR.PATCH`.
- Human-readable references MAY use `v` prefix (example: `v1.0.0`).

### Repository release tag
- Applies to GitHub releases of this repository.
- Format: `tlos-vMAJOR.MINOR.PATCH`.

## Compatibility rules
- **MAJOR**: breaking governance change.
- **MINOR**: additive change.
- **PATCH**: editorial or non-substantive fix.

## Definition of breaking governance change
A change is **breaking** when at least one current compliant implementation would become non-compliant without action.

Concrete examples:
- Required artifact added/removed/renamed in canonical pipeline.
- Mandatory role responsibilities changed (e.g., who can approve, veto, or register).
- Legal/governance precedence changed between normative documents.
- Normative metadata contract changed (required key rename/removal).

Non-breaking examples:
- Added optional guidance.
- Clarified language without obligation changes.
- Typo/link/format fixes.

## Required artifacts for a release
Before tagging a release:
- `CHANGELOG.md` updated with impact class (`breaking`, `additive`, `editorial`).
- Any breaking change includes migration guidance.
- Normative docs updated with required metadata.
- ADR added for governance-impacting decisions.
- Links and anchors validated by CI.

## Tagging
Recommended tags:
- `tlos-v1.0.0`
- `tlos-v1.1.0`
- `tlos-v2.0.0`

Release notes SHOULD summarize governance-impact changes and reference ADRs.

## Decision records
Governance-impact changes MUST include an ADR under `docs/adr/` describing:
- context
- decision
- alternatives considered
- implications for downstream repos
