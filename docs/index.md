# TLOS Documentation Index

**Status:** Active  
**Version:** v0.1  
**Effective date:** 2026-02-13  
**Owner:** Tech4Life & Beyond LLC  
**Last reviewed:** 2026-02-13

---

## What belongs in TLOS

TLOS is the **governance and doctrine** layer for the Tech4Life ecosystem.

TLOS is the source of truth for:
- Governance model and contributor levels
- Factory doctrine (how products are created and progressed)
- Integration principles (how TOIL, registry, pipeline, and products relate)

TLOS is *not* the source of truth for:
- Product-specific facts (those live in `products/` and the `product-registry` export)
- Legal template text (canonical text lives in `toil/` and `legal-private/`)
- Financial models (canonical in `finance-private/`)

---

## Normative hierarchy

When documents conflict, interpret in this order:

1. Foundation principles (`docs/foundation/`)
2. Governance model (`docs/governance/`)
3. Contributor levels (`docs/contributor-levels/`)
4. Product Factory doctrine (`docs/product-factory/`)
5. Product Pipeline doctrine (`docs/product-pipeline/`)
6. TOIL integration (`docs/toil-integration/`)
7. GitHub architecture (`docs/github-architecture/`)

---

## Start here

- Foundation: `docs/foundation/Tech4Life_Foundation.md`
- Governance model: `docs/governance/TLOS_Governance_Model.md`
- Contributor levels: `docs/contributor-levels/Contributor_Level_System.md`
- Factory doctrine: `docs/product-factory/Tech4Life_Product_Factory.md`
- Pipeline doctrine: `docs/product-pipeline/Product_Creation_Pipeline.md`
- TOIL integration: `docs/toil-integration/TOIL_Integration_Framework.md`
- GitHub architecture: `docs/github-architecture/GitHub_Architecture.md`

---

## Cross-repo dependencies (informative)

- **TOIL:** legal baseline and templates (`toil/`)
- **Product Registry:** canonical machine-readable product index (`product-registry/`)
- **Factory Validator:** rules + tooling (`product-creation-pipeline/`)
- **Products:** product packs and dossiers (`products/`)
- **Community:** onboarding, contribution norms, and collaboration (`community/`)
