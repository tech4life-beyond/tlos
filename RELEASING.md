# Releasing & Versioning (TLOS)

TLOS is a governance standard. It evolves, but changes must be **auditable** and **predictable**.

## Two kinds of versions

1) **TLOS Standard Version** (governance spec)
- Applies to normative doctrine (governance model, lifecycle doctrine, integration requirements).
- Format: `vMAJOR.MINOR`

2) **Repository Release Version**
- Applies to tagged GitHub releases of this repository.
- Format: `tlos-vMAJOR.MINOR.PATCH`

In early stages you may keep both aligned, but the distinction matters once tooling and downstream dependencies rely on TLOS.

## Compatibility rules

- **MAJOR**: breaking governance change (meaning changes, required artifacts change, role model change).
- **MINOR**: additive change (new optional guidance, new profiles, clarifications that do not change obligations).
- **PATCH**: typo fixes, link fixes, formatting, non-substantive edits.

## Required artifacts for a release

Before tagging a release:
- `CHANGELOG.md` updated
- Any breaking change includes a migration note
- Normative docs updated with version/effective date/last reviewed metadata
- Links validated

## Tagging

Recommended:
- Tag: `tlos-v0.1.0`, `tlos-v0.2.0`, etc.
- Release notes should summarize governance-impact changes.

## Decision records (optional but recommended)

For governance-impact changes, add an ADR under `docs/adr/` describing:
- context
- decision
- alternatives considered
- implications for downstream repos
