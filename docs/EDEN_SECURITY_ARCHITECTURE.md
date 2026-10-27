# OBSIDIAN OS — EDEN security architecture

Status: implementation plan. This document does not claim that the features are deployed.

## Core rules
- Local-first. No sensitive content sent to cloud without explicit policy authorization.
- EDEN Local handles offline analysis. EDEN Cloud is an optional, organization-controlled deployment of independently hosted models.
- The deterministic security engine continues working if AI is offline, unavailable, or compromised.
- Deny by default; least privilege; human authorization for high-impact changes.
- No hacking back, attacking third-party devices, or collecting unrelated personal information.
- Security claims require repeatable tests, logging, and independent review.

## Planned subsystems
1. EDEN Core: local inference interface, optional private cloud inference, model integrity verification, bounded tool permissions and offline fallback.
2. Guardian: endpoint monitoring, signed security policies, threat event correlation, malware and privacy investigation.
3. Network Guardian: WPA3-Enterprise / 802.1X EAP-TLS where supported, validated server certificates, segmentation, rogue AP detection, PMF, quarantine and firewall enforcement.
4. USB Guardian: block unknown device classes by default, removable-media policies, separate inspection station, disposable sandbox for files, extraction and resource limits, data loss prevention. Software cannot stop electrical USB damage.
5. Privacy Guardian: app network metadata and permission audits, evidence-based explanations, firewall restrictions, isolation and admin-approved uninstall.
6. Red Team: explicit scope, written authorization, non-destructive tests, separate credentials, safe test replicas, kill switch, independent logging and approval gates.
7. Application Manager: OBSIDIAN .obs manifest and signing specification; compatible Linux packages via trusted package managers; sandboxed application permissions.
8. OS Foundation: Linux-based desktop with verified boot, disk encryption, update rollback, security logging, and recovery tools.
9. Enterprise: policy administration, audit trails, opt-in fleet telemetry, access controls and incident reporting.

## Implementation milestones
- Phase 1: policy engine, event schema, package manifest validator and tests.
- Phase 2: Linux endpoint integration and USB/network event collectors with mock fixtures.
- Phase 3: sandboxed analysis station and administrator approval workflows.
- Phase 4: local model integration with offline evaluation and cloud opt-in.
- Phase 5: OS image, signed updates, hardware compatibility and independent security assessment.

## Privacy and limitations
Network access does not authorize inspection of personal devices. Network metadata is not equivalent to full device visibility. An AI finding is not proof of malicious intent. Risk cannot be eliminated and no product can guarantee zero breaches.
