#!/usr/bin/env bash
set -euo pipefail
if [[ "${EUID}" -ne 0 ]]; then
  echo "Run in a dedicated Debian build VM as root" >&2
  exit 1
fi
if ! command -v lb >/dev/null; then
  echo "Install live-build first: apt install live-build" >&2
  exit 1
fi
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT"
lb config --mode debian --distribution bookworm --architectures amd64 --binary-images iso-hybrid --debian-installer none --archive-areas "main" --bootappend-live "boot=live components persistence"
lb build
