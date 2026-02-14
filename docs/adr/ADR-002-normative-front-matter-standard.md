---
document_id: TLOS-ADR-002
classification: Normative
status: Active
version: 1.0.0
effective_date: 2026-02-13
last_reviewed: 2026-02-13
owner: Tech4Life Governance (TLOS)
---
# ADR-002: Unified Normative Front Matter Standard

## Context
Normative metadata keys were inconsistent (`document-id` vs `document_id`, `effective-date` vs `effective_date`) and not uniformly enforced.

## Decision
Use a single required front matter contract for all normative docs:

- `document_id`
- `classification`
- `status`
- `version`
- `effective_date`
- `last_reviewed`
- `owner`

Optional:
- `last_reviewed_by`

## Alternatives considered
- Allow per-document custom metadata schemas.
- Exempt legal documents from metadata harmonization.

## Consequences
- Consistent validation in CI.
- Easier governance audit and traceability.
