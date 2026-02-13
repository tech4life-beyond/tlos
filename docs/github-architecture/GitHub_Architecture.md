---
document_id: TLOS-GH-ARCH-001
classification: Normative
status: Active
version: 1.0.0
effective_date: 2026-02-13
last_reviewed: 2026-02-13
owner: Tech4Life Governance (TLOS)
---
# Tech4Life Operating System (TLOS)
## BLOCK 8 — GitHub Architecture

---

## 1. Purpose

This document defines GitHub as the **system of record** for Tech4Life & Beyond — where governance standards, products, registries, and controls are versioned, auditable, and traceable.

GitHub is not only a code repository.
It is:
- A collaboration hub
- A transparency layer
- A timestamped public record
- A protection mechanism for TOIL

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

Includes:
- Product TOIL registrations
- Sell sheets
- Public documentation
- Ethical declarations

---

### B. Restricted Layer (Private)
Purpose:
- Active collaboration
- Team coordination
- Early-stage development

Includes:
- Work-in-progress designs
- Internal discussions
- Draft documentation

Access is level-based.

---

### C. Core Layer (Private)
Purpose:
- Protection of the operating system
- Cultural and ethical coherence

Includes:
- TLOS documents
- Governance model
- Internal curriculum
- Contributor evaluation logic

Access is invitation-only.

---

## 4. Official Repository Structure (Current)

Tech4Life & Beyond is organized as a **multi-repo factory system** inside one GitHub organization.

### Public repositories (ecosystem base)
- `tlos` — governance & doctrine (how we operate)
- `toil` — legal/license baseline + templates
- `product-registry` — canonical product ID registry + machine-readable exports
- `product-creation-pipeline` — validation rules + tooling for product packs
- `products` — product packs / dossiers (one folder per product)
- `kivai` — interoperability protocol + runtime reference (product-specific)
- `community` — onboarding, contribution pathways, and collaborator guidance

### Private repositories (strategic core)
- `armanu-curriculum` — internal contributor capability progression & training ops
- `finance-private` — financial ops, royalty controls, projections, investor reporting
- `legal-private` — enforcement readiness, contract ops, IP chain-of-title controls

**Rule:** GitHub is the auditable record. The *source of truth* is **distributed by domain**:
- Governance truth → `tlos`
- License truth → `toil`
- Product identity truth → `product-registry`
- Product-pack quality gates → `product-creation-pipeline`
- Product dossiers → `products`
- Legal/finance controls → private repos

## 5. Access Control Model

Access is governed by contributor level:

- Observer → Public Layer
- Contributor → Restricted Layer
- Creator → Restricted + limited Core
- Architect → Full Core access

No one has automatic promotion.

---

## 6. Authorship & Traceability

Every contribution must:
- Be committed under a real identity
- Reference the contributor level
- Include a contribution summary

GitHub commit history is considered a legal and ethical record.

---

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
