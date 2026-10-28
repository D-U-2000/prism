# Review guide

Status: Draft. Owner: @vothanhdat2000. Updated: 2026-10-28.

Read by human and AI reviewers. Org rules: [engineering standards, Code review](https://github.com/D-U-2000/engineering-handbook/blob/main/standards.md#code-review). This page adds only what failure means in Prism.

## What counts as broken

- **Ledger:** an unbalanced transaction or a claim of financial correctness without named policy and evidence. Account taxonomy, clearing equations and nonnegative-account rules remain proposed until the money-policy ADR is accepted. Do not invent an equation from a reconciliation label.
- **Amounts:** any floating-point type on a money path. Amounts are integer VND.
- **Journal:** an edit or delete of a posted entry, including in a migration. Corrections are linked compensating entries.
- **Idempotency:** a replay with the same key and input that creates a second financial effect; a reused key with different input that posts money.
- **State:** a transition violating accepted policy, or a race that bypasses it. ADR 0002 is absent from the inspected baseline; its draft requires review before refund/payout rules become authoritative.
- **Investigation:** inference presented as fact, unmatched records silently attached to a payment, unresolved outcomes presented as success or failure, or a next action that can duplicate a financial effect.
- **Authority:** changing source financial records from the read-only investigation surface, or treating case closure as proof of settlement.
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
