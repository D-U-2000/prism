# ADR 0010: Payment operations as the product entry point

- Status: Proposed
- Date: 2026-10-28
- Owner: @vothanhdat2000
- Review: @vothanhdat2000 and @lvphuyn1500

## Context

[ADR 0001](0001-project-foundation.md) started Prism as a glass-box payment sandbox. The owner now wants a focused, lean operational product, with fintech as the first domain and a supplied brand identity. The repository contains design documents, not an implemented financial engine.

## Proposed decision

Make payment exception investigation the first user-facing job. Keep a deterministic sandbox to supply controlled failures and expected outcomes. Follow the [product brief](../product.md) and [roadmap](../roadmap.md); do not add banking as the automatic next step.

If accepted, this supersedes ADR 0001's product purpose and sequencing. It retains synthetic data, virtual money, provider isolation and reproducible correctness evidence. It selects no language, datastore, framework or production integration. IDs 0002–0009 remain reserved for tracked decisions; 0010 avoids colliding with drafts on other machines.

## Alternatives

- Educational payment engine as the entire product: useful for learning, but operator value is indirect. Retain as fallback if the product hypothesis fails.
- Complete payment processor or broad bank sandbox: adds domain scope before proving an operational task. Defer.
- Generic incident management: broad integration and workflow obligations without evidence for replacing existing tools. Reject for the initial scope.
- Read-only payment investigation backed by simulation: recommended because it connects correctness to an observable operator task while bounding integration risk.

## Consequences and revisit

Reassess existing tickets and money-policy requirements before implementation. Preserve their history and do not approve drafts implicitly. Small fixtures can precede a complete ledger engine, but every financial finding must cite explicit policy and evidence.

No customer demand, ROI, comparative superiority or production reliability is demonstrated. Revisit if users misinterpret cases, the tool adds work, or integrations defeat the lean scope. Expansion needs a second validated use case.

## Acceptance record

Proposal introduced in [PR #12](https://github.com/D-U-2000/prism/pull/12). Explicit engineering and business acceptance is not recorded in this ADR. On acceptance, update this status, record the approval reference and mark affected parts of ADR 0001 superseded. Merging a draft alone does not accept it.
