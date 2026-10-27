# Southeast Asian payment orchestration

Status: Research, not an accepted scope change. Owner: @vothanhdat2000. Updated: 2026-10-27.
Tracking: [sc-86](https://app.shortcut.com/du-1/story/86).
Baseline inspected: Prism main `ad1a55e`; engineering-handbook main `a192f0e`.

## Question and conclusion

Can fragmented local payment methods provide a useful future simulation problem for Prism? Yes, as a research proposal: demonstrate capability-aware routing and recovery across simulated providers after the current money-correctness milestones. The existing [roadmap](../roadmap.md) remains a draft and this note does not accept its proposed technology or money-policy choices.

The input is a user-supplied market narrative. Treat its competitive claims as hypotheses, not evidence of demand, market leadership or guaranteed performance.

## Evidence and corrections

- Stripe documents multiple payment-method families, including bank and local methods. Describing today's Stripe as only a card abstraction would be misleading. [Supported methods](https://docs.stripe.com/payments/payment-methods/overview).
- Xendit's channel documentation distinguishes country, currency, amount limits and channel behavior. A common API does not make all providers or methods interchangeable. [Available channels](https://docs.xendit.co/docs/en/available-payment-channels).
- 2C2P publishes payment types, channels and agents. This supports its relevance as integration prior art, not the narrative's ranking or customer-scale claims. [Channel reference](https://devzone.2c2p.com/docs/payment-type-channel-and-agent).
- Bank of Thailand documents cross-border QR linkages, including Vietnam with participating institutions. This is evidence of payment-network connectivity, not permission for an arbitrary application to settle or convert funds. [Cross-border payment](https://www.bot.or.th/en/financial-innovation/digital-finance/digital-payment/cross-border-payment.html).
- Stripe documents request idempotency within its API. That mechanism does not establish a shared deduplication boundary across two unrelated providers. [Idempotent requests](https://docs.stripe.com/api/idempotent_requests).

Razorpay/UPI pricing, Vietnam-Cambodia coverage, market dominance, merchant demand and claims of optimal FX are not verified in this review. India is a separate comparison market, not a Southeast Asian country. Do not reuse these claims as established facts.

## Engineering implications (inference)

Aggregation combines methods; orchestration chooses and coordinates routes; settlement and FX move or convert obligations. They need distinct contracts even if one supplier offers all three.

A timeout may occur after provider A accepted a payment. Blindly sending the payment to B can charge twice. Keep the operation unresolved and query or reconcile A before a new financial attempt is allowed by an explicit policy. Changing providers may also invalidate a QR session or require renewed customer action. Seamless failover cannot be promised for every method.

Route eligibility must precede optimization: currency, country, payment method, amount, merchant enablement and current operation state constrain the candidates. Lowest fee and highest success rate can conflict; historical estimates are not guarantees. Location or device alone should not override a customer's available methods.

## Bounded simulation proposal

After current milestone evidence, consider two fictional adapters with different capabilities, configurable fees and deterministic failures. No live integrations, cross-border settlement or FX implementation are proposed for M0.

Run a fixed-seed workload containing a normal capture, pre-send unavailability, timeout after acceptance, duplicate callback and delayed reconciliation. Expose eligibility decisions, attempted route, unresolved state, ledger effect and recovery timeline.

Compare a fixed eligible route with a declared routing policy on the same workload. Record duplicate financial effects, unresolved amounts, completion rate, recovery time and simulated fee per completed payment. Define the observation window and denominator; retain pending outcomes rather than reporting them as failures or successes prematurely. All baselines are unmeasured.

Acceptance for a future experiment: demonstrate no duplicate financial effect in the specified scenarios and explain each route decision. Any real integration, stack selection or milestone change needs its own story and decision review.

## Repository continuity findings

The latest roadmap and review guide were read before this change. The review guide references ADR 0002, but that file is absent from the inspected main tree; the roadmap lists it as planned. Do not treat its proposed policy as an accepted ADR. This pre-existing gap needs owner/business resolution before payment implementation.
