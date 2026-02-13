# Contributing to TLOS

TLOS (Tech4Life Operating System) is the **governance and doctrine** layer for the Tech4Life & Beyond ecosystem.
Changes here affect downstream repositories (TOIL, product-registry, product-creation-pipeline, products, community, and product runtimes).

## Core rules

1. **PRs only.** No direct commits to `main`.
2. **Small, auditable changes.** Prefer multiple small PRs over one large PR.
3. **Normative vs informative.**
   - **Normative** statements define requirements (use **MUST / MUST NOT / SHOULD / MAY**).
   - **Informative** statements explain context or rationale.
4. **No silent breaking changes.** If a change alters meaning or expected behavior:
   - update `CHANGELOG.md`
   - add a migration note (what changed, who is impacted, what to do)
   - version appropriately (see `RELEASING.md`)
5. **Keep TLOS scoped.** TLOS is the source of truth for **governance standards** and **factory doctrine**, not for product-specific facts.

## Branch naming

Use one of:

- `tlos/p0-<short-scope>`
- `tlos/p1-<short-scope>`
- `tlos/p2-<short-scope>`

Examples:
- `tlos/p0-governance-baseline`
- `tlos/p1-canonical-lifecycle-authority`

## Commit message style

Use imperative, present tense:

- `Add ...`
- `Fix ...`
- `Clarify ...`
- `Document ...`

## Documentation style guide

### File structure
- Keep documents under `docs/<topic>/`.
- Add new topics only when necessary (avoid deep nesting).

### Required header metadata (for **normative** docs)
At the top of each normative document, include:

- **Status:** Draft | Active | Deprecated
- **Version:** `vX.Y`
- **Effective date:** `YYYY-MM-DD`
- **Owner:** `Tech4Life & Beyond LLC`
- **Last reviewed:** `YYYY-MM-DD`

### Language
- Use clear, unambiguous language.
- Prefer short paragraphs and bullets.
- Define terms once in `docs/glossary.md` and use them consistently.

## Review checklist (before you open a PR)

- [ ] Does the change alter a requirement? If yes: updated `CHANGELOG.md` and added migration notes.
- [ ] Are links valid?
- [ ] Are terms consistent with `docs/glossary.md`?
- [ ] If you introduced/changed policy language: did you update version/effective date?

## Reporting issues

Open a GitHub Issue with:
- what is wrong
- where (file + section)
- the proposed fix (ideal wording)
