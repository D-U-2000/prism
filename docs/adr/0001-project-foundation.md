# ADR 0001: Project foundation

- Status: Accepted
- Date: 2026-10-26

Direction change under review: [ADR 0010](0010-payment-operations-direction.md) proposes a payment-operations product with this sandbox as its proving environment. This accepted record remains authoritative until the successor is explicitly accepted; a merged proposal is not acceptance.

## Context

Prism needs to demonstrate payment infrastructure behavior without real money or provider credentials. The repository must make its scope, evidence, and safety boundaries clear to contributors.

## Decision

Start with a deterministic payment core and an explicit ledger. Keep provider behavior behind an adapter. Treat tests, failure simulations, reconciliation output, and the demo trace as first-class evidence.

The implementation language remains open until a short design spike compares Rust and Go for correctness, iteration speed, observability, and contributor onboarding.

## Consequences

- The first release can be run locally and inspected end to end.
- Banking features are gated on payment-core evidence.
- No live payment provider or production deployment is required for the initial milestones.
