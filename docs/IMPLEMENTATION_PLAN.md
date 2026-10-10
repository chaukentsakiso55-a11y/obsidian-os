# OBSIDIAN Implementation Baseline

Target: Science Expo March 2027. Status: early implementation, not a finished OS.

## Approved reference specification

The user supplied 30 numbered reference screens plus five hidden-settings screens. Visual identity: cybernetic hooded wolf, electric-blue moon and mountains, dark glass panels, cyan/blue/violet highlights, metallic OBSIDIAN logotype, DarthWolf watermark, top bar, left navigation, bottom dock. Reference imagery should be used only with appropriate rights. Do not substitute arbitrary wallpaper and call it an exact match.

Desktop design baseline: top system bar 44px; sidebar 212px; bottom dock 60px. At smaller widths use adaptive layouts rather than shrinking desktop controls. The reference screenshots remain the visual acceptance standard; token values in packages/design-system/obsidian.css are initial measurements and subject to screenshot comparison.

## Delivery stages

0. Establish design tokens, screen inventory, visual comparisons, and architecture.
1. Fix and verify Debian Boot OS build; desktop shell, launcher, file manager, settings, persistence and recovery.
2. Implement local privacy classification, offline model routing and permission-checked AI system actions.
3. Implement defensive static file and URL analysis, quarantine and explainable reporting. Only execute samples in properly isolated disposable environments.
4. Integrate Android, Windows and web companion interfaces within their actual platform capabilities.
5. Validate security, accessibility, performance, offline operation, boot recovery and expo demonstrations.

## Safety and truthfulness requirements

- Never represent mock CPU, RAM, network, scan, or threat numbers as live telemetry.
- Unknown or unsigned apps are not inherently malicious; classify observed evidence and uncertainty.
- Confidential prompts and file content never silently fall back to cloud models.
- No unrestricted AI root access; high-impact actions require explicit authorization.
- Do not automatically visit tokenized, payment, authentication, reset or state-changing URLs.
- Browser/file analysis environments have no access to user credentials or host files.
- Advanced offensive security tools and unsafe hidden settings remain unimplemented placeholders pending appropriate review.
- No API secrets in source control, client bundles, APKs or diagnostic logs.
- A successful build and a working bootable ISO must be separately verified; neither is claimed by this document.

## First committed implementation

- Correct the Boot OS cybersecurity launcher generation in build-live.sh.
- Add reusable shared CSS tokens.
- Record architecture, reference requirements and acceptance boundaries here.

## Acceptance gates

Boot ISO in VM; launcher executable; real local security results; privacy tests demonstrating no cloud transmission of confidential inputs; functional permission prompts; sandbox isolation tests; pixel-level visual review against approved references; manual mobile and desktop usability checks.
