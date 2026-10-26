# Contributing to Prism

Prism is an educational financial systems project. Contributions should make system behavior easier to understand and verify.

## Before opening a pull request

- Link the change to a Shortcut story or a GitHub issue.
- Keep one behavioral change per pull request.
- Add or update the invariant, test, or simulation that proves the change.
- Run the local checks described in the repository Makefile.
- Do not include secrets, real payment data, or provider credentials.

## Pull request checklist

- [ ] Scope and failure behavior are documented.
- [ ] Tests cover the changed invariant.
- [ ] Idempotency and retry behavior are considered where relevant.
- [ ] Documentation and decision records are updated when behavior or boundaries change.
- [ ] No real money or production integration is involved.
