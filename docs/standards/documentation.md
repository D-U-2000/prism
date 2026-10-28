# Documentation standard

Status: Accepted by the project owner in the planning conversation on 2026-10-26.
Owner: @vothanhdat2000. Updated: 2026-10-27.

One canonical page, evidence, and review live in engineering-handbook `standards.md`. This page only adds Prism rules. If they conflict, the handbook wins.

## Lifecycle and precedence

Proposals move from draft to accepted or rejected. Replaced decisions become superseded and link to their successor; preserve their historical rationale.

Accepted specifications define intended behavior. Code and observations establish actual behavior. A mismatch is an issue to resolve, not permission to silently rewrite either side. User authorization governs action; AI suggestions do not constitute approval.

Update documents when their dependencies or behavior change. An updated date alone is not evidence of accuracy. Record the inspected commit or version for audits and experiments.

Document behavior changes in the same PR as the code change.

Public documentation must explain scope, status and contribution steps without access to internal planning tools. Link public issues, PRs and repository documents for reader-facing context; keep internal ticket links in PR tracking metadata. Maintainers remain responsible for internal delivery tracking.

## Review and exceptions

Deterministic checks cover structure and links; humans assess usefulness, assumptions and evidence. AI findings must point to a specific passage and explain the consequence; they are advisory until checked.

An exception records the rule, reason, responsible person, approver and review trigger. Change standards through a reviewed PR when experience justifies it.

Apply this page to the M0 specification before adding more templates or automation. Measure retrieval difficulty and reproduction failures from actual attempts; no baseline has been measured yet.
