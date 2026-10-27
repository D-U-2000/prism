# Roadmap proposal

Status: Draft for owner and business review. Owner: @vothanhdat2000. Updated: 2026-10-27.
Acceptance needed: @vothanhdat2000 (engineering) and @lvphuyn1500 (business), recorded as PR review.

## Vision

Prism is a place where money moves in plain sight and every unit is explained. One payment goes in; a spectrum of balanced journal entries comes out, and none is lost.

The ambition is to hold Prism to the same money discipline a State Bank of Vietnam-licensed intermediary payment provider must hold under Decree 52/2024/ND-CP and Circular 40/2024/TT-NHNN as amended: correct invariants, an auditable journal, provable recovery from failure. Prism earns that discipline without the license, because no real money and no real customer ever passes through it. That is a deliberate boundary, not a lower bar: it proves the hardest engineering question (does the money always add up, under every failure) before the hardest business question (capital, licensing, regulated operation) is ever in play. Whether that discipline is later aimed at an actual licensed product is a separate, future decision; nothing here commits to it.

The project is evidence for two things: how a correct money system behaves, and how D&U 2000 makes decisions, verifies behavior and learns from delivery.

Prism is not an end-user product and will not hold real customer money. It handles virtual money and simulated providers only ([ADR 0001](adr/0001-project-foundation.md)).

## Readers, in priority order

1. **Engineers learning payment infrastructure** run a scenario, inject a failure and watch the ledger balance again.
2. **People evaluating the team** (hiring managers, partners, contributors) read the decisions, PRs and demo trace, and judge the method as well as the code.
3. **The business maintainer** applies the business handbook's acceptance method to a domain with money. Money policy is the first decision reviewed jointly by engineering and business.

## Milestones

Each milestone opens only when the previous one has recorded evidence.

| Milestone | Question it answers | Evidence |
|---|---|---|
| M0 | Is one payment's money correct through capture, refund and payout, including failures? | Scenario tests, failure simulations, reconciliation output, CLI trace |
| M1 | Can a reader see why it is correct? | Scenario runner, timeline and ledger views over the M0 trace |
| M2 | Does it stay correct under concurrent payments? | Concurrency tests against the real database |
| Later | Banking features | Gated on M0–M2 evidence |

## Decisions, in dependency order

| # | Decision | Recommendation | Record | Decides |
|---|---|---|---|---|
| 1 | Purpose and readers | This page | This proposal | Owner + business |
| 2 | Money policy | Fee leaves the guarantee fund at payout settlement; full refund returns the fee; payout is in M0 with a success and a returned path; refund is rejected after payout settles; partial refund is out of M0 | ADR 0002 | Owner + business |
| 3 | Implementation language | One-day Rust spike of the payment and payout state machine with the journal, no database. Rust for the ledger core if the compiler catches real state errors within the day; otherwise Go, with a revisit condition | ADR 0003 | Owner |
| 4 | Architecture | Modular monolith in one process. Ledger core as a pure library, provider simulator behind an adapter, Postgres with per-payment locking and an idempotency table, injected clock and randomness. Append-only journal plus an operations table, not full event sourcing | ADR 0004 | Owner |
| 5 | Demo scope | M0: CLI, JSON trace and one static viewer page. Full UI in M1 | This proposal | Owner + business |
| 6 | Brand | Short design brief, time-boxed, in parallel after the spike; needed before M1 UI | Design brief | Owner + business |

Decision 1 shapes 5 and 6; decision 2 blocks the M0 specification update; decision 3 precedes 4.

## Brand and UX direction

Direction only, not a design.

- **Metaphor:** a prism splits light into a spectrum, as a payment splits into journal entries. Logo and motion use the same idea.
- **Logo:** a minimal single-colour prism, legible at 16 px. The organization uses a simple monogram.
- **Theme:** neutral background, one accent, light and dark modes. Semantic colours for money states (pending, settled, returned, refunded), never distinguished by red and green alone. Tabular figures for amounts.
- **Motion:** only when it carries meaning, such as money moving between accounts during replay; 150–250 ms steps; honour `prefers-reduced-motion`.
- **M1 views:** scenario runner (choose a scenario, step through it, inject failures); timeline of requests and events; ledger balances per account with an invariant status.
- **Prior art:** design tokens on an existing component library (Radix or shadcn/ui); no custom design system.
- **Display language:** English, amounts as `1,000,000 VND`. A Vietnamese toggle is decided after M1.

## Non-goals

Real money, real providers, production deployment, end-user accounts and microservices.

## Evidence

None yet. This page records intent and proposed decisions; each decision becomes accepted only in its own record with an approval reference.

## Open questions

- Does Prism need to run without Docker? If so, SQLite replaces Postgres for M0 and loses the real concurrency demonstration, which moves to M2.
- Which consumer-protection rules apply if a refund ever withholds the fee? Not checked; not needed for the recommended M0 policy.
