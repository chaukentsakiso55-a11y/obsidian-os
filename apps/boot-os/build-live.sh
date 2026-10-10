#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$ROOT/../.." && pwd)"
if [[ "${EUID}" -ne 0 ]]; then
  echo "Run as root inside a disposable Debian build environment" >&2
  exit 1
fi
command -v lb >/dev/null || { echo "Install live-build" >&2; exit 1; }
test -f "$REPO/obsidian/scoring.py" || { echo "Missing shared security engine" >&2; exit 1; }
test -f "$ROOT/desktop/obsidian_gui.py" || { echo "Missing desktop dashboard" >&2; exit 1; }
mkdir -p "$ROOT/config/includes.chroot/opt/obsidian" "$ROOT/config/includes.chroot/usr/local/bin"
cp -r "$REPO/obsidian" "$ROOT/config/includes.chroot/opt/obsidian/"
cp "$ROOT/desktop/obsidian_gui.py" "$ROOT/config/includes.chroot/opt/obsidian/obsidian_gui.py"
printf '%s\n' '#!/bin/sh' 'exec python3 /opt/obsidian/obsidian_gui.py "$@"' > "$ROOT/config/includes.chroot/usr/local/bin/obsidian-gui"
printf '%s\n' '#!/bin/sh' 'cd /opt/obsidian' 'exec python3 -m obsidian.cli "$@"' > "$ROOT/config/includes.chroot/usr/local/bin/obsidian-scan"
chmod 755 "$ROOT/config/includes.chroot/usr/local/bin/obsidian-gui" "$ROOT/config/includes.chroot/usr/local/bin/obsidian-scan"
cd "$ROOT"
lb config --mode debian --distribution bookworm --architectures amd64 --binary-images iso-hybrid --debian-installer none --archive-areas main --bootappend-live "boot=live components"
lb build
