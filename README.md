# Prism

![Prism wordmark](assets/brand/prism-wordmark-dark.svg)

**Make complex operations understandable, recoverable, and verifiable.**

Prism is an open-source project exploring payment exception investigation: help payment engineers and operations teams understand what happened, identify what remains unknown, and choose a safe next step with traceable evidence.

## The first problem

A provider accepts a payment, the request times out, and the order stays pending. A callback arrives twice. An operator needs to know whether retrying could charge the customer again.

The proposed first app brings the payment timeline, provider observations, journal evidence and unresolved discrepancies into one case. It distinguishes confirmed facts, inferences and missing evidence. Closing a case must not invent a successful payment.

## Status

**Design stage. No runnable payment engine or investigation app exists yet.** Team acceptance of this product proposal is tracked in [sc-77](https://app.shortcut.com/du-1/story/77). Product value, performance and willingness to pay have not been validated.

The first milestones use synthetic data, virtual money and simulated providers only. Investigation is read-only with respect to source financial records. A deterministic sandbox supplies reproducible failures and ground truth; it is the proving environment for the product.

## First useful experience

- Open a synthetic exception case and follow its evidence timeline.
- Compare provider observations with local payment and ledger records.
- Recognize duplicates, missing evidence and conflicting outcomes.
- Explain a safe next step and export a summary with evidence references.

These are planned capabilities, not shipped features. Live provider connections, real customer data, automated refunds and a general incident-management platform are outside initial scope.

## Direction and contribution

Start with the [product brief](docs/product.md), [roadmap](docs/roadmap.md) and [documentation index](docs/README.md). The [brand guide](docs/brand.md) describes the supplied wordmark and its use.

Language, database, frontend and deployment choices remain open. A modular monolith is a candidate, subject to a scored architecture decision. There is no requirement to adopt microservices as the project grows.

See [CONTRIBUTING.md](CONTRIBUTING.md), [working rules](AGENTS.md) and [SECURITY.md](SECURITY.md). Shortcut owns work status; Git owns specifications; GitHub PRs hold review and verification evidence.

## License

Apache-2.0. See [LICENSE](LICENSE) and [NOTICE](NOTICE). Prism is independent; references to other products do not imply affiliation or endorsement.
