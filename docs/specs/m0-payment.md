# M0: Virtual marketplace payment

Status: Draft for domain review. Owner: @vothanhdat2000. Updated: 2026-10-26.
Delivery reference: [Shortcut story 57](https://app.shortcut.com/du-1/story/57).

## Purpose and scope

Give implementers and reviewers one scenario for demonstrating correct money movement. A simulated provider captures 1,000,000 VND for a marketplace seller. A provisional 20,000 VND platform fee leaves 980,000 VND payable to the seller. These fee values are proposed test fixtures, not product pricing.

Use integer VND amounts, a unique payment ID, a stable idempotency key and provider event IDs. Capture means provider confirmation; payout means simulated transfer of the seller payable.

## Proposed invariants

- Every journal transaction balances debits and credits within one currency.
- Posted journal entries are immutable; corrections use linked compensating entries.
- Repeating an operation with the same key and identical input has one financial effect.
- Reusing a key with different input returns a conflict without posting money.
- Duplicate provider events do not create duplicate postings.
- Refund totals cannot exceed captured value.
- A timeout is an unknown provider outcome until reconciled; it is not automatically a failed capture.

## Acceptance scenarios

Demonstrate capture and fee allocation, duplicate requests, duplicate events, out-of-order events, timeout after provider success, and crash between provider confirmation and local recording. For each case, inspect the journal, operation status and reconciliation outcome after replay.

## Open decisions

Fee reversal on refunds, partial refunds, payout eligibility, account taxonomy, event ordering policy and durable recovery design require review before implementation. Rust versus Go remains open.

## Evidence

No implementation or correctness results exist yet. The next step is to review these proposed invariants and define expected postings for each acceptance scenario. Real payment providers and real money are outside scope.
