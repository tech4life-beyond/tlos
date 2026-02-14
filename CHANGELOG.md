# Changelog

All notable changes to TLOS are documented here.

This project follows the governance-oriented versioning approach described in `RELEASING.md`.

## Unreleased
### breaking
- Unified normative versioning convention to `MAJOR.MINOR.PATCH` in governance release policy (removes previous split-model guidance for the standard format).

### additive
- Added explicit pipeline precedence clause in `docs/product-pipeline/Product_Creation_Pipeline.md`.
- Declared `docs/product-factory/Tech4Life_Product_Factory.md` as an implementation profile and linked to canonical pipeline sections.
- Formalized founder intervention protocol with trigger, maximum duration, mandatory review, rollback, and appeal path.
- Added authority matrix in `docs/index.md`.
- Added `docs/adr/` with ADR-001 (versioning convention) and ADR-002 (front matter standard).
- Added docs-quality CI workflow and validator for UTF-8, front matter, internal anchors, and relative links.
- Added PR template with doctrinal checklist.
- Added normative language guidance and optional `last_reviewed_by` metadata in `CONTRIBUTING.md`.
- Added “Status del estándar” section in README.

### editorial
- Normalized metadata keys across normative docs (including `LICENSE.md`) to snake_case schema.
- Normalized block titles in architecture/factory docs (`Block N: ...`).
