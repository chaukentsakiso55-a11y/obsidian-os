# OBSIDIAN OS — Full Linux Operating System Architecture

**Scope:** The user's screenshots and Claude HTML desktop prototype describe the ENTIRE OBSIDIAN operating system, not merely the web app. The browser prototype is a visual and interaction reference, not the OS implementation.

## Platform layers
1. **Linux base:** select a stable distribution and reproducible image build, secure boot strategy, disk encryption, signed updates, device drivers, recovery, and installer.
2. **Desktop shell:** native Linux Wayland compositor integration, taskbar/dock, window management, launcher, notifications, workspaces, accessibility and settings. Preserve the original reference visual design.
3. **Native apps:** File Manager, Terminal, Settings, Network Center, System Monitor, Privacy Guardian, Security Center, EDEN AI, Developer Studio, OBS Package Manager, Financial Integrity and Identity Guardian.
4. **EDEN services:** unprivileged AI inference separate from independently testable deterministic security policy engine; local-first, optional self-hosted service. Explicit authorization and human approval for high-impact operations.
5. **OBS app ecosystem:** manifest, signatures, sandbox, package validation, install/uninstall/update, runtime compatibility and SDK for Python/Rust/JS.
6. **Enterprise integrations:** identity offboarding, audit retention, financial reconciliation, USB/network telemetry; permissions, least privilege, evidence provenance, privacy protections.

## Reference fidelity rules
- The 17 original screenshots are the visual source of truth for system-wide UI, not just a website.
- Use Claude's HTML prototype for behavioral inspiration (windows, desktop, dock), not as the native compositor.
- Rename all obsolete 'Obsidian AI' labels to 'EDEN AI'.
- Add features discussed after the screenshots as native system applications, consistent with the visual language.
- Do not claim 100% fidelity until native screenshots are compared at matched resolutions.

## Build phases
- Phase 0: archive screenshots, identify each screen and define visual tokens.
- Phase 1: Linux VM image boots into a working desktop session, with launcher, windows and settings.
- Phase 2: native applications and EDEN UI, then real file operations and safe OS integrations.
- Phase 3: deterministic defensive telemetry, policy engine, audit logs and permissions.
- Phase 4: signed .obs package builder/installer and EDEN Developer Studio.
- Phase 5: enterprise modules, threat modeling, testing, image signing, installation and recovery.
- Phase 6: hardware compatibility and independent security review.

## Acceptance criteria
- Reproducible bootable VM image with a documented build procedure.
- Native desktop apps open in independent movable/resizable windows.
- System settings persist; file manager and terminal operate against the intended Linux user environment.
- Security alerts must reflect real authorized telemetry or be clearly marked simulated.
- CI verifies builds, tests and signed artifacts where configured.

## Current implementation truth
Existing GitHub changes are documentation, a Python policy prototype, and browser UI extensions. **No complete bootable OBSIDIAN Linux image has been built or validated yet.** Do not confuse a browser HTML demo with an OS.
