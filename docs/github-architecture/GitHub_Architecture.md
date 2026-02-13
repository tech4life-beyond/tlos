---
document-id: TLOS-GH-ARCH-001
version: 1.0.0
status: Normative
effective-date: 2026-02-13
last-reviewed: 2026-02-13
owner: Tech4Life Governance (TLOS)
---

# Tech4Life Operating System (TLOS)
## BLOCK 8 — GitHub Architecture

---

## 1. Purpose

This document defines GitHub as the **single source of truth for governance, specs, and product records** within the Tech4Life & Beyond ecosystem.

GitHub is not only a code repository.
It is:
- A collaboration hub
- A transparency layer
- A timestamped public record
- A protection mechanism for TOIL

**Scope boundary (important):**
- TLOS is the source of truth for *governance + standards*.
- Product truth is carried by: `products` (packs) + `product-registry` (IDs/index) + audit-ready artifacts in `legal-private` and `finance-private`.

---

## 2. Core Principles

- Documentation precedes execution
- Transparency where possible, privacy where necessary
- Public benefit without loss of control
- Traceability of authorship and responsibility

---

## 3. Repository Categories

Tech4Life GitHub is organized into **three layers**:

### A. Public Layer (Open)
Purpose:
- Prior art
- Transparency
- Global visibility

Includes (public repos):
- Product dossiers/packs
- Product registry index/exports
- Licensing framework (TOIL)
- Governance standards (TLOS)
- Public community onboarding

---

### B. Restricted Layer (Private)
Purpose:
- Active collaboration
- Team coordination
- Sensitive internal operations

Includes (private repos):
- Curriculum and internal enablement
- Finance operations and models
- Legal operations and enforcement readiness

Access is role-based and least-privilege.

---

### C. Core Layer (Protected Subset of Private)
Purpose:
- Protection of the operating system
- Cultural and ethical coherence
- Legal/financial defensibility

Includes:
- Legal enforcement artifacts
- Investor-ready finance artifacts
- Sensitive contributor/identity records (if introduced later)

Access is invitation-only and audited.

---

## 4. Official Repository Structure (Current State)

**Current state (authoritative):** Tech4Life & Beyond operates as a **multi-repo ecosystem** under the GitHub organization `tech4life-beyond`.

### Public repositories (ecosystem base)
- `tlos` — governance, doctrine, factory standards
- `toil` — license + legal templates (public baseline)
- `product-registry` — canonical product IDs + machine-readable exports
- `product-creation-pipeline` — validator, rules, and CI gates for product packs
- `products` — product packs/dossiers (per product folder)
- `community` — onboarding, collaboration rules, contributor guidance
- `kivai` — protocol/runtime infrastructure (product-level technical repo)

### Private repositories (core operations)
- `armanu-curriculum` — internal curriculum for capability progression
- `finance-private` — monetization logic, registers, projections, reporting templates
- `legal-private` — legal ops, enforcement playbooks, templates, evidence standards

**Source-of-truth mapping (must stay consistent):**
- Governance standards: `tlos`
- License baseline + public templates: `toil`
- Canonical product IDs and registry exports: `product-registry`
- Product packs (the dossiers that pipeline validates): `products`
- Validation rules + tooling: `product-creation-pipeline`
- People onboarding + collaboration model: `community`
- Enforcement and confidential operations: `legal-private`, `finance-private`, `armanu-curriculum`

---

## 5. Access Control Model

Access is governed by contributor level:

- Observer → Public Layer
- Contributor → Public + limited collaboration areas (as defined in community)
- Creator → Collaboration privileges + product workstreams (as granted)
- Architect → Governance-impact privileges (as granted)

No one has automatic promotion.

---

## 6. Authorship & Traceability

Every contribution must:
- Be committed under a real identity
- Reference the contributor level (when relevant)
- Include a contribution summary

GitHub commit history is considered a legal and ethical record.

---

<a id="7-kivai-project-decision"></a>
## 7. Kivai Project Decision Framework

Existing projects (e.g., Kivai) are evaluated by:
- Relevance to current humanity needs
- Alignment with Tech4Life mission
- Energy vs impact ratio

Outcomes:
- Continue
- Archive (read-only)
- Retire

No deletion of historical work.

---

## 8. Public vs Private Philosophy

Not everything must be public to serve humanity.

What matters is:
- Outcomes are open
- Methods are responsible
- Core culture is protected

---

## 9. Automation Roadmap (Future)

Planned:
- Automated TOIL registration via GitHub Actions
- Contribution tracking
- Royalty linkage
- Compliance checks

---

## 10. Living Architecture

This structure evolves.

Any change requires:
- Documentation
- Ethical review
- Architect-level approval

---

**GitHub is our memory.
We do not erase memory.**
