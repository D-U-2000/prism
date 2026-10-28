# Roadmap proposal

Status: Proposed for owner and business review. Owner: @vothanhdat2000. Updated: 2026-10-28.
Proposal introduced in [PR #12](https://github.com/D-U-2000/prism/pull/12). Acceptance requires recorded engineering and business review.

## Purpose

Deliver the [payment exception workflow](product.md) in small, verifiable steps. The sandbox supplies evidence; investigation is the proposed product. No runnable implementation exists yet.

M0, M1 and M2 remain the milestone names. Their scope reflects the proposed investigation workflow; implementation has not started.

Each milestone starts only after the previous gate has recorded evidence and owner acceptance. Keep at most three active stories; finish a useful slice before opening another workstream.

## M0: One explainable payment exception

Provide one local synthetic case from input to evidence summary. Start with provider success followed by a timeout and a duplicate callback. Include an unresolved variant with insufficient evidence.

- Define the case bundle and expected findings first: amount/currency, source identifiers, timestamps, provenance and policy version.
- Build a deterministic minimal fixture generator or simulator and a read-only analyzer. A complete payment processor is not a prerequisite.
- Provide a CLI export and a minimal static case viewer showing timeline, evidence, discrepancy and next-action preconditions. This is the first visible app, not a production dashboard.
- Demonstrate repeatable output, no duplicate financial effect in the simulator, and no invented certainty when evidence is missing.

Exit evidence: reproducible commands, fixture versions, expected versus actual findings, failure cases and a maintainer walkthrough. A screenshot proves neither performance nor market value.

## M1: An operator can investigate independently

Extend the M0 viewer into a usable local workflow. Add case selection, evidence drill-down and export as needed for the task. Include delayed, out-of-order and conflicting evidence and a recording gap after a simulated crash.

Exit evidence: an observed user trial using the [validation method](product.md#validation-and-measures), with errors, assistance and incomplete tasks recorded. Unsafe recommendations must be corrected before release. Failure to improve the task triggers narrowing, not more features.

## M2: Repeatable operation under bounded load

Exercise multiple cases, restart/replay, resource limits and migration compatibility on an explicitly chosen storage design. Include concurrency tests where shared durable state is adopted. Measure processing cost and onboarding effort alongside throughput.

Exit evidence: workload, hardware, versions, seeds, repetitions, correctness results and known limits. Synthetic results do not establish production readiness.

## Decisions before code

- **Product acceptance:** this roadmap and [product brief](product.md), reviewed through a public pull request.
- **Domain scope:** reassess the money-policy draft and [payment specification](specs/m0-payment.md). Select the minimum policy and fixtures for M0. Refund/payout policy remains proposed; reconcile earlier proposals explicitly.
- **Language:** Compare Rust and Go with a bounded parsing, correlation, replay and domain-model spike. The previous ledger-only spike is a candidate to revise, not evidence already gathered.
- **Architecture:** Evaluate a modular monolith separating ingestion, evidence, analysis and presentation; isolate the simulator behind an adapter. One process is a candidate. Durable storage, locking, queues and outbox patterns need demonstrated requirements.
- **Contracts and tests:** use reserved ADR 0005/0006 when needed for test strategy and the versioned case/trace contract. Record consumers and upgrade implications.
- **Viewer:** choose the smallest rendering approach for M0; select a frontend framework only when required, using reserved ADR 0007. Observability and delivery retain ADR 0008/0009 at their gates.

Technology ADRs compare alternatives on the handbook scorecard: support horizon/EOL, license, supply chain, reversal cost, contributor cost and experiment evidence. LTS is a dependency support policy, not a property guaranteed by deployment topology. Record upgrade responsibility and revisit conditions.

Service extraction needs evidence for independent scaling, release ownership or failure isolation. A modular monolith can remain the long-term design; speculative scale is not a reason to distribute transactions.

## Before implementation

Accept the product scope, reconcile the earlier payment specification, and publish the selected case contract and expected findings. Banking remains deferred. [Payment orchestration research](research/payment-orchestration.md) is not an implementation commitment. No delivery dates are promised.

## Brand

Use the supplied wordmark as documented in the [brand guide](brand.md). A literal prism icon and bank-oriented visual narrative are no longer proposed. UI colors communicate evidence and uncertainty with text labels, never color alone.

## Beyond M2

Consider an adjacent domain after demonstrated operator value and a second real use case. Live integration, sensitive data, automated remediation and commercial operation each need new scope, security and business review. No banking milestone is precommitted.
