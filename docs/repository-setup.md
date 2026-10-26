# Repository setup

Owner: @vothanhdat2000. Observed: 2026-10-26 via GitHub API.

## Confirmed configuration

- Organization has two members: vothanhdat2000 and lvphuyn1500. No invitation is needed to establish initial membership.
- Prism main requires a PR, repository-hygiene check, current base, linear history and resolved conversations. Admin enforcement is enabled; force pushes and deletion are disabled.
- Required approving reviews are zero. PR requirement does not imply independent human approval.
- Actions default token permissions are read; Actions cannot approve PR reviews.
- Dependabot alerts and automatic security fixes were enabled during foundation setup.

## Explicitly deferred

Organization base permission is admin. The owner chose to keep it unchanged pending a later decision. The organization does not require two-factor authentication. Do not change membership or access without specific authorization.

Secret scanning and push protection were disabled at inspection. Merge and rebase methods were enabled alongside squash; automatic branch deletion was disabled. These observations are not a claim of security certification.

## Delivery boundaries

The current CI checks repository hygiene only. Application correctness checks will be added with the implementation. No deployment target or CD pipeline exists. Documentation and workflow changes must go through PR review; setup is not complete merely because onboarding cards disappear.

Auto-assignment is proposed for new Prism issues to @vothanhdat2000, the initial triage maintainer. This does not assign organization-wide responsibility.
