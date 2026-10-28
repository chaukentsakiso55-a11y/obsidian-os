# EDEN Identity and Access Guardian

Status: planned module. No live identity-provider or banking integrations.

## Threat model
A former employee may retain passwords, API keys, sessions, certificates, delegated access, recovery methods or hidden accounts after resignation, retirement or dismissal.

## Offboarding workflow
1. Verify departure event and effective date through authorized HR workflow.
2. Inventory the employee's identities, privileged roles, devices, service accounts and third-party access.
3. Revoke individual sessions, tokens, certificates and authentication factors.
4. Rotate shared secrets and credentials known to the departing employee.
5. Transfer ownership of subscriptions, infrastructure and recovery accounts.
6. Remove banking/payment approval authority using the provider's authorized administrative processes.
7. Review dormant accounts, recently created identities, delegation and unusual privilege changes.
8. Preserve access logs and evidence in a tamper-evident system.
9. Verify revocation across each connected provider and escalate incomplete steps.
10. Continue risk-based monitoring of company systems without tracking the former employee's private devices or accounts.

## Response to suspected post-employment misuse
- Investigate access attempts and financial discrepancies with documented evidence.
- Block unauthorized access to company systems, revoke credentials and require stronger approval for high-value transfers.
- Preserve chain of custody and refer suspected crimes to authorized investigators.
- Never hack back, monitor private accounts without lawful authorization or presume guilt from an anomaly.

## Implementation priorities
Build a provider-neutral offboarding checklist and evidence model, then add approved identity-provider and finance connectors with explicit permissions, test fixtures, and reversible administrative actions.
