# Contributing to Prism

Prism is exploring payment exception investigation, backed by a deterministic financial sandbox. Contributions should help operators understand evidence and choose a justified next action. Read the [product brief](docs/product.md) for proposed scope and maturity.

## Before opening a pull request

- Maintainers must track work in Shortcut before implementation and link the story in the PR. External contributors may open a GitHub issue first; a maintainer creates or links its Shortcut story before work begins.
- Keep one behavioral change per pull request.
- Add or update the invariant, test, or simulation that proves the change.
- Run the local checks described in the repository Makefile.
- Run `python tools/check_docs.py` (Python 3) for document structure and local file links. It does not check external URLs, anchors or factual accuracy.
- Follow the [documentation standard](docs/standards/documentation.md) and [working method](docs/standards/method.md).
- Do not include secrets, real payment data, or provider credentials.

## Pull request checklist

- [ ] Scope and failure behavior are documented.
- [ ] Tests cover the changed invariant.
- [ ] Idempotency and retry behavior are considered where relevant.
- [ ] Documentation and decision records are updated when behavior or boundaries change.
- [ ] No real money or production integration is involved.
