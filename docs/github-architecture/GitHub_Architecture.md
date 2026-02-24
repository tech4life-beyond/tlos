---
document_id: TLOS-GH-ARCH-001
classification: Normative
status: Active
version: 1.0.1
effective_date: 2026-02-24
last_reviewed: 2026-02-24
owner: Tech4Life Governance (TLOS)
last_reviewed_by: Architect
---

# Tech4Life Operating System (TLOS)
## Block 8: GitHub Architecture

---

## 1. Purpose

This document defines GitHub as the **system of record** for Tech4Life & Beyond — where governance standards, products, registries, and controls are versioned, auditable, and traceable.

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

## 4. Official Repository Structure

**Current state (active):** Tech4Life uses a multi-repo structure inside the GitHub organization `tech4life-beyond`.

### Public repositories (ecosystem base)
- `tlos` — governance and doctrine (this repository)
- `toil` — license framework, templates, releases
- `product-registry` — canonical product ID registry + exports
- `product-creation-pipeline` — pack validation rules + CI profiles
- `kivai` — KIVAI platform reference (schema, SDK, runtime contracts)
- `products` — product packs (dossiers/artifacts by lifecycle stage)
- `community` — public participation and onboarding (when active)

### Private repositories (strategic core)
- `legal-private` — legal operations artifacts (templates, enforcement playbooks)
- `finance-private` — monetization logic, royalty controls, projections
- `armanu-curriculum` — contributor progression and assessment materials

**Rule:** GitHub is the system of record for decisions, releases, and traceability.  
Runtime implementations live in product-specific repos and must reference these governance standards.

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

<a id="7-kivai-project-decision-framework"></a>
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