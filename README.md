# Prism

Prism is a glass-box financial systems sandbox for learning, testing, and explaining payment infrastructure.

The first milestone models a virtual payment flow in Vietnamese đồng with a deterministic provider adapter, an append-only ledger, idempotency, refunds, reconciliation, and failure injection. The system is designed to make correctness visible before adding banking features.

## Status

Early development. The repository is being built in public-ready form; no real money, credentials, customer data, or production integrations are used.

## Scope

- Payment core first: authorization, capture, refund, payout, and reconciliation.
- Deterministic simulations for retries, duplicate events, timeouts, and crashes.
- Explicit invariants and an audit trail that can be inspected from a demo.
- Later expansion only after the payment core passes correctness and demonstration gates.

Stripe, Monzo, Wise, and Starling are study references. Prism is an independent educational and engineering project.

## Development

The implementation language is intentionally left open until the first design spike compares Rust and Go against the project constraints.

```text
docs/              decision records and system design
crates/            Rust workspace boundary (when selected)
services/          service boundaries and adapters
```

## Working agreement

1. Define the scenario and invariants.
2. Implement the smallest deterministic slice.
3. Prove behavior with tests and failure simulations.
4. Show the flow through a glass-box demo.
5. Record evidence before expanding scope.

Start with the [documentation index](docs/README.md) and [working rules](AGENTS.md). See [CONTRIBUTING.md](CONTRIBUTING.md) for contributions and [SECURITY.md](SECURITY.md) for reporting.

## License

Apache-2.0. See [LICENSE](LICENSE).
