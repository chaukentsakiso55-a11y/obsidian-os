# OBSIDIAN OS reference-driven rebuild

## Inputs reviewed
- 17 PNG reference images supplied in `obsidian pictures.zip`, showing boot, desktop, EDEN's predecessor, security center, privacy, monitoring, file manager, terminal, network, settings, developer studio, and additional system screens.
- Claude's standalone HTML browser prototype, containing a boot flow, desktop shell, draggable windows, dock, app launcher, virtual filesystem and simulated apps.

## Visual direction
Use the user's original dark neon-blue wolf-and-mountain design as the primary visual reference. Preserve the Claude prototype's desktop/window behavior as the interaction baseline. The older name `OBSIDIAN AI` must be `EDEN AI` throughout.

## New enterprise apps
- Financial Integrity Guardian: independent reconciliation, separation of duties, evidence and audit reviews.
- Identity Guardian: employee offboarding, credential revocation, privileged identity audit.
- EDEN Developer Studio: app creation, image-to-interface workflow, Python packaging into planned `.obs` format.
- OBS Package Manager: signed manifests, sandbox permissions, verification and rollback.

## Delivery phases
1. Baseline: preserve existing desktop and app switching; rename old AI to EDEN.
2. Visual fidelity: reproduce reference-by-reference layout and styling; compare screenshots at matching viewport sizes.
3. Integrate new applications as separate desktop windows, not webpage navigation tabs.
4. Implement browser-safe local persistence and honest simulated workflows.
5. Extract shared shell into maintainable components and implement real Linux backend services in a separately tested environment.
6. Create a bootable Linux image only after installer, updates, signing, isolation, and device compatibility have been tested.

## Honest limitations
A browser prototype is not a full OS. No screenshot similarity percentage is verified yet. Security and finance screens must not claim to monitor real infrastructure without explicit authorized integrations.