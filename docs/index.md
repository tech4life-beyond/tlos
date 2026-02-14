---
document_id: TLOS-INDEX-001
classification: Normative
status: Active
version: 1.0.0
effective_date: 2026-02-13
last_reviewed: 2026-02-13
owner: Tech4Life Governance (TLOS)
last_reviewed_by: optional
---
# TLOS Documentation Index

## What belongs in TLOS

TLOS is the **governance and doctrine** layer for the Tech4Life ecosystem.

TLOS contains:
- Governance standards and decision logic
- Normative doctrine (how we operate)
- Factory standards (how we create products)
- Terminology and definitions
- Cross-repo operating contracts (high-level)

TLOS does NOT contain:
- Product-specific facts (those live in `products/` and the `product-registry` export)
- Canonical legal templates (those live in `toil/` and `legal-private/`)
- Financial models (canonical in `finance-private/`)
- Implementation-specific runtime details (those live in product repos)

---

## Normative hierarchy (highest to lowest)
1. Foundation
2. Governance Model
3. Product Creation Lifecycle (Pipeline)
4. TOIL Integration Framework
5. GitHub Architecture
6. Contributor Level System

---

## Canonical documents
- Foundation: `docs/foundation/Tech4Life_Foundation.md`
- Governance: `docs/governance/TLOS_Governance_Model.md`
- Lifecycle (canonical): `docs/product-pipeline/Product_Creation_Pipeline.md`
- Factory (profile/implementation framing): `docs/product-factory/Tech4Life_Product_Factory.md`
- TOIL Integration: `docs/toil-integration/TOIL_Integration_Framework.md`
- GitHub Architecture: `docs/github-architecture/GitHub_Architecture.md`
- Contributor Levels: `docs/contributor-levels/Contributor_Level_System.md`

---

## Authority matrix (owner by domain)

| Domain | Canonical owner document | Notes |
|---|---|---|
| Governance | `docs/governance/TLOS_Governance_Model.md` | Decision model, intervention protocol, accountability. |
| Legal / license baseline | `LICENSE.md` + `docs/toil-integration/TOIL_Integration_Framework.md` | Legal text in LICENSE, operational integration in TOIL framework. |
| Registry / records | `docs/github-architecture/GitHub_Architecture.md` | Registry structure, repositories, traceability boundaries. |
| Factory / lifecycle execution | `docs/product-pipeline/Product_Creation_Pipeline.md` | Canonical lifecycle authority; factory doc is implementation profile. |

---

## Normative vs informative rule
Normative statements MUST be auditable and written for compliance.  
Informative docs may explain, guide, or give examples.

If unclear, treat the document as normative.
