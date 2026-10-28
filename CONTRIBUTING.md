# Contributing to Prism

Prism is exploring payment exception investigation, backed by a deterministic financial sandbox. Contributions should help operators understand evidence and choose a justified next action. Read the [product brief](docs/product.md) for proposed scope and maturity.

## Before opening a pull request

- Start with a [GitHub issue](https://github.com/D-U-2000/prism/issues) for a bug, question or proposed change. Discuss larger changes before implementation, then link the issue in your PR. No account in the team’s internal planning tools is required; maintainers handle internal tracking.
- Keep one behavioral change per pull request.
- Add or update the invariant, test, or simulation that proves the change.
- Run checks relevant to the change. The repository currently contains documentation and assets; application test and formatting targets are not implemented yet.
- Run `python tools/check_docs.py` (Python 3) for document structure and local file links. It does not check external URLs, anchors or factual accuracy.
- Follow the [documentation standard](docs/standards/documentation.md) and [working method](docs/standards/method.md).
- Do not include secrets, real payment data, or provider credentials.

## Pull request checklist

- [ ] Scope and failure behavior are documented.
- [ ] Tests cover the changed invariant.
- [ ] Idempotency and retry behavior are considered where relevant.
- [ ] Documentation and decision records are updated when behavior or boundaries change.
- [ ] No real money or production integration is involved.
