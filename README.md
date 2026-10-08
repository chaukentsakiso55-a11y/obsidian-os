# OBSIDIAN

Privacy-first cross-platform cybersecurity guardian prototype by Cyber Pulse.

## Components

- `obsidian/`: Python heuristic analyzer and scoring library
- `apps/android/`: native Kotlin Android prototype
- `apps/web/`: offline React/TypeScript security dashboard
- `apps/desktop/`: Tauri desktop shell using the web dashboard
- `tests/`: Python unit tests

## Commands

- Python tests: `python -m unittest discover -s tests -v`
- Python CLI: `python -m obsidian.cli text "Act immediately and send your password"`
- Web: `cd apps/web && npm install && npm run build`
- Android: `gradle -p apps/android :app:assembleDebug` (requires Android SDK and Gradle 8.9)
- Desktop: install Rust, Node and Tauri system dependencies; then `cd apps/desktop && npm install && npm run desktop`

## Scope and privacy

The current analyzers are offline heuristics, not antivirus products. They do not upload inputs, fetch remote reputation data, or monitor devices. An unknown/zero score does not mean safe. Android and web currently implement separate equivalents of the same basic scoring rules; a future shared Rust engine is planned. No API keys should be committed.
