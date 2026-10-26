# Working method

Status: Accepted. Owner: @vothanhdat2000. Updated: 2026-10-26.

## From question to evidence

1. Describe the problem, affected reader or user, constraints and non-goals.
2. Inspect existing decisions and prior art before designing a new solution.
3. State assumptions, credible alternatives and the smallest useful experiment.
4. Define expected results and what would disprove the hypothesis before running it.
5. Record commands, input, environment, commit, observations and limits.
6. Explain the conclusion and obtain acceptance for a new durable decision.
7. Update the canonical document and leave the next action in the handoff.

## Evidence and metrics

Distinguish observed fact, inference, unknown and accepted decision. A matching implementation or a green check does not establish correctness beyond what was checked.

Each metric specifies its definition, units, population or denominator, time window, collection method and the decision it informs. Benchmarks also record hardware, versions, workload, seed, repetitions and variability. Record baseline as unmeasured until evidence exists.

## Proportionate review

Wording changes need a content and link review. Contract or invariant changes need scenario evidence and affected-consumer analysis. Ledger, security and access changes require explicit failure analysis and appropriate human review.

Use named states: proposed, written, checked, applied. Do not report completion merely because a file exists. A procedure includes prerequisites, commands, expected output, failure handling and recovery.

## Continuity

At session end, retain decisions, evidence references, unresolved questions and the next action. Do not copy full chats into durable documentation. Shortcut owns task progress; GitHub PRs own review; repository documents own technical content.
