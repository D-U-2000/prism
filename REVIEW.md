# Review guide

Status: Draft. Owner: @vothanhdat2000. Updated: 2026-10-27.

Read by human and AI reviewers. Org rules: [engineering standards, Code review](https://github.com/D-U-2000/engineering-handbook/blob/main/standards.md#code-review). This page adds only what failure means in Prism.

## What counts as broken

- **Ledger:** a transaction that does not balance; a liability account or `provider_clearing` that goes negative; `provider_clearing` not equal to the sum of liabilities plus pending reconciliation.
- **Amounts:** any floating-point type on a money path. Amounts are integer VND.
- **Journal:** an edit or delete of a posted entry, including in a migration. Corrections are linked compensating entries.
- **Idempotency:** a replay with the same key and input that creates a second financial effect; a reused key with different input that posts money.
- **State:** a refund or payout transition outside the state rules in ADR 0002, or two transitions on one payment that can run concurrently.
- **Docs:** a spec, ADR or README that disagrees with the code.

## High-risk paths (human approval required)

Ledger and money-policy code, `docs/adr/`, `docs/specs/`, `.github/workflows/`, `.github/CODEOWNERS`. Everything else is routine: CI plus an AI review may be enough.

## How to report

- Cite `file:line` for every finding; do not guess file names.
- No style nitpicks; formatting belongs to tools.
- Mark a finding pre-existing when the PR did not introduce it.
- Start with a summary and a count. When nothing is wrong, say "No issues found".

## Ignored paths

None yet.
