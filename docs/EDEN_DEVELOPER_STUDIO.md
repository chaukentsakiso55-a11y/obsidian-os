# EDEN Developer Studio and OBSIDIAN SDK

Status: planned. No working AI code generator or .obs packager exists yet.

## Features
- Natural-language app specification and project generation.
- User-provided reference images and authorized website visual references.
- Design customization, project preview, iterative revisions, and user approval.
- Python, JavaScript/TypeScript, and Rust project templates.
- Convert compatible existing projects to OBSIDIAN .obs packages.
- Programming tutor and explainable build diagnostics.
- Opt-in, revocable, local-first preference learning; no covert employee profiling.
- Offline model inference where supported, optional privately hosted EDEN cloud.
- Automated lint, dependency review, tests and isolated execution.

## Proposed .obs SDK
- Manifest schema: app ID, name, version, entry point, runtime, permissions, supported architectures and publisher.
- Reproducible package assembly and content hashing.
- Publisher signing and signature verification.
- Runtime dependency resolution and sandbox permissions.
- Explicit elevation approval for system-level capabilities.
- CLI commands: obs init, obs validate, obs build, obs sign, obs verify.
- Python wrapper for SDK commands and an app-building UI.
- Compatibility path for existing Linux application formats.

## Security boundaries
AI-generated code is untrusted until reviewed and tested. Never execute generated code with unrestricted host privileges. Use isolated build runners with resource and network limits, signed artifacts, audit logs and administrator approvals. Reference images and websites are untrusted input; respect licenses and permissions. Do not claim perfect visual fidelity, zero vulnerabilities, or guaranteed build success.

## Build order
1. Formalize manifest schema and threat model.
2. Implement a minimal .obs archive builder and validator.
3. Add isolated package installation and app permissions.
4. Add developer templates and automated tests.
5. Integrate EDEN's code generation, image interpretation and iterative previews.
6. Add enterprise policies, signed releases and independent security review.
