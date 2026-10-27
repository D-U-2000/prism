# Working method

Status: Accepted. Owner: @vothanhdat2000. Updated: 2026-10-27.

Evidence layers, the limit of a green check, and proportionate review live in engineering-handbook `standards.md`. This page only adds the Prism loop. If they conflict, the handbook wins.

## From question to evidence

1. Describe the problem, affected reader or user, constraints and non-goals.
2. Inspect existing decisions and prior art before designing a new solution.
3. State assumptions, credible alternatives and the smallest useful experiment.
4. Define expected results and what would disprove the hypothesis before running it.
5. Record commands, input, environment, commit, observations and limits.
6. Explain the conclusion and obtain acceptance for a new durable decision.
7. Update the canonical document and leave the next action in the handoff.

## Metrics

Each metric specifies its definition, units, population or denominator, time window, collection method and the decision it informs. Benchmarks also record hardware, versions, workload, seed, repetitions and variability. Record baseline as unmeasured until evidence exists.

## States and procedures

Use named states: proposed, written, checked, applied. Do not report completion merely because a file exists. A procedure includes prerequisites, commands, expected output, failure handling and recovery.

## Continuity

At session end, retain decisions, evidence references, unresolved questions and the next action. Do not copy full chats into durable documentation. Shortcut owns task progress; GitHub PRs own review; repository documents own technical content.
