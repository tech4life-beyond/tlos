---
document_id: TLOS-ADR-001
classification: Normative
status: Active
version: 1.0.0
effective_date: 2026-02-13
last_reviewed: 2026-02-13
owner: Tech4Life Governance (TLOS)
---
# ADR-001: Versioning Convention

## Context
TLOS mixed `vMAJOR.MINOR` and `MAJOR.MINOR.PATCH` expressions across normative and release guidance.

## Decision
Adopt `MAJOR.MINOR.PATCH` as the single normative version convention.

- Normative docs store version as `MAJOR.MINOR.PATCH`.
- Human-readable references MAY prepend `v`.
- Git tags use `tlos-vMAJOR.MINOR.PATCH`.

## Alternatives considered
- Keep split model (`vMAJOR.MINOR` for standard + SemVer for repo tags).
- Use `YEAR.SEQ` calendar versioning.

## Consequences
- Simpler audits and tooling.
- Clear mapping between document versions and release artifacts.
