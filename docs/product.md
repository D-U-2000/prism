# Product direction

Status: Proposed. Owner: @vothanhdat2000. Updated: 2026-10-28.
Review: engineering by @vothanhdat2000 and business by @lvphuyn1500 in [the product-direction PR](https://github.com/D-U-2000/prism/pull/12).

## Positioning

Prism helps payment teams investigate and resolve payment exceptions with traceable evidence. The first deliverable supports investigation and a documented next action; it does not execute remediation against financial systems.

The long-term promise is to make complex operations understandable, recoverable and verifiable. Payments are the first domain in which to test that promise, not a claim that one workflow already fits every industry.

Customer demand, differentiation and commercial viability remain hypotheses. Acceptance of a design is not customer validation.

## User and job

The primary user is a payment engineer or operations specialist investigating an ambiguous payment across application records, provider events and the ledger. SREs and production engineers help diagnose and recover the system; maintainers need repeatable cases and explicit contracts.

Their job: establish what is known about one payment, identify a discrepancy, and hand off a justified next action without causing another financial effect. Technical evaluators can also inspect the team's engineering through the sandbox; that audience is secondary to the operator workflow.

Initial commercial hypothesis: teams with recurring exceptions may value less manual investigation. Buyer, frequency, current tooling, budget and willingness to pay are unknown. No revenue projection is justified yet.

## First workflow

1. Load a versioned synthetic case bundle. Validate its schema and provenance; reject malformed input without changing an existing case.
2. Correlate records by explicit payment, operation and provider identifiers. Unmatched records stay unmatched; amount or timestamp similarity alone does not establish identity.
3. Show an evidence timeline with source event time and observation time distinguished. Late arrival must not silently become causal order.
4. Compare local status, provider observations and expected journal evidence under a named policy version. Separate confirmed facts, derived findings and unknowns.
5. Explain a next action and its preconditions, such as obtaining a provider status observation before another charge. Missing evidence leaves the case unresolved.
6. Export a reproducible summary with input references, rule version, findings and remaining questions. Case notes and review status remain separate from financial state.

The first synthetic example is provider capture success followed by a client timeout and a duplicate callback. Variants include missing confirmation, out-of-order evidence, conflicting observations and a local recording gap after a crash. The sandbox owns expected truth; the investigator must not assume access to hidden simulator state.

## Boundaries

- No real money, credentials, customer data or live provider connections in M0–M2.
- No autonomous retry, refund, payout, journal edit or account mutation from the investigation surface.
- A reviewed case does not mean a settled payment or a resolved discrepancy.
- No generic observability backend, on-call scheduler, bank core, payment aggregator or marketplace in the initial scope.
- AI is optional future assistance. The first explanation must be reproducible from rules and evidence without an LLM. AI cannot invent observations or authorize money movement.

## Lean by design

Keep one user workflow, a small deployable footprint and low support effort. Inspect native capabilities and mature open-source components before building infrastructure. Build the domain-specific evidence model only where it creates demonstrable value.

Optimize correctness and operator understanding before throughput. Every optimization records baseline, workload, result and extra maintenance cost. Price/performance includes infrastructure, investigation time, onboarding, support and upgrades. A low hosting bill alone does not establish good economics.

## Validation and measures

All baselines are unmeasured. This is a proposed experiment, not a success claim or release SLO.

Compare raw-fixture investigation with Prism on equivalent synthetic cases. Counterbalance case order to reduce learning bias. Record participant role, difficulty, assistance, sample size and individual results. A small convenience sample cannot establish market-wide effects.

- **Correct interpretation:** correct answers divided by attempted cases, scored against a prewritten answer key. Reward recognizing unknown outcomes rather than guessing.
- **Time to a justified next action:** elapsed minutes from opening a case to a supported conclusion among completed cases. Report incomplete cases separately; retain errors alongside time.
- **Manual effort:** source switches and manual lookup steps per case, observed in both conditions.
- **Unsafe recommendations:** actions violating case policy or acting on an unresolved outcome. Any such result blocks release of the workflow until understood and corrected.
- **Reproducibility:** matching findings for identical bundle and rule versions divided by replay runs. Record seed, versions and commands.
- **Operating cost:** processing time, peak memory and bundle size on declared hardware; contributor setup time and support interventions per observed trial. Do not extrapolate production costs.

Continue only if correct interpretation is preserved and effort falls in observed cases without unsafe recommendations. If existing tools solve the task better or no recurring need appears, narrow or stop the product hypothesis. Research does not block a bounded learning prototype; it does gate commercial claims and expansion.

## Expansion and alternatives

Billing, marketplace payouts and order reconciliation are possible adjacent domains. Add one only after a real second use case demonstrates demand and reusable concepts. Keep domain policies separate; do not build a universal workflow engine in advance. Banking and cross-border orchestration are no longer assumed next milestones.

The useful analogy to [incident.io](https://incident.io/hubs/on-call/announcing-on-call) is a focused operational workflow and expansion into adjacent needs. Prism is independent and claims neither its capabilities nor its commercial results.

Before implementation, compare provider dashboards, existing logs, spreadsheets and established reconciliation tools on the same case. A product must justify switching cost. Stripe's [idempotency contract](https://docs.stripe.com/api/idempotent_requests) and the [orchestration research](research/payment-orchestration.md) inform failure semantics, not evidence of demand.

Retain a pure educational sandbox if operator validation fails. Defer a complete payment processor and reject generic incident management for the initial scope: both add responsibilities beyond the first job. The [roadmap](roadmap.md) defines delivery gates; the [direction record](adr/0010-payment-operations-direction.md) preserves the change in purpose.
