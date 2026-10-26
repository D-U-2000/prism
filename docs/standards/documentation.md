# Documentation standard v1

Status: Accepted by the project owner in the planning conversation on 2026-10-26.
Owner: @vothanhdat2000. Updated: 2026-10-26.

## Purpose

Help a new contributor find an answer, an AI session resume correctly, and another engineer reproduce evidence.

## Required rules

- One subject has one canonical home. Use relative links inside the repository.
- State purpose and audience when they are not obvious. Put the useful answer first.
- Write simple English, one main idea per paragraph, descriptive headings and meaningful link text.
- Use lists for parallel items or steps. Use tables only for comparisons. Avoid empty headings, repeated status fields and decorative badges.
- Explain unfamiliar terms on first use. Keep terminology consistent with the specification.
- Every decision, proposal and experiment records its status, responsible person and date. Add stable IDs only when other documents need to reference them.
- Use the structure appropriate to the document type; front matter is optional until tooling requires it.
- Claims that affect a decision need a source or reproducible evidence. Mark assumptions and unknowns explicitly.
- Document behavior changes in the same PR as the code change.

## Lifecycle and precedence

Proposals move from draft to accepted or rejected. Replaced decisions become superseded and link to their successor; preserve their historical rationale.

Accepted specifications define intended behavior. Code and observations establish actual behavior. A mismatch is an issue to resolve, not permission to silently rewrite either side. User authorization governs action; AI suggestions do not constitute approval.

Update documents when their dependencies or behavior change. An updated date alone is not evidence of accuracy. Record the inspected commit or version for audits and experiments.

## Review and exceptions

Deterministic checks cover structure and links; humans assess usefulness, assumptions and evidence. AI findings must point to a specific passage and explain the consequence; they are advisory until checked.

An exception records the rule, reason, responsible person, approver and review trigger. Change standards through a reviewed PR when experience justifies it.

Apply this v1 to the M0 specification before adding more templates or automation. Measure retrieval difficulty and reproduction failures from actual attempts; no baseline has been measured yet.
