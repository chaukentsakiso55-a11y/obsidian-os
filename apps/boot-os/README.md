# OBSIDIAN Boot OS

OBSIDIAN Boot OS is a Debian 12 amd64 live system with an XFCE desktop and a native offline Python/Tkinter security dashboard. It boots independently from Windows; it does not overwrite the internal drive. The current security engine provides heuristic message and URL scoring, not antivirus or comprehensive endpoint protection.

## Build

Use the GitHub Actions workflow `OBSIDIAN Boot OS` (manual dispatch), or build in a dedicated Debian/Ubuntu build VM:

```bash
sudo apt-get update
sudo apt-get install -y live-build
sudo bash apps/boot-os/build-live.sh
```

Output: `apps/boot-os/live-image-amd64.hybrid.iso` (filename may vary with live-build version). Requires internet access, several gigabytes of free disk space, and an amd64 CPU.

## Use

Test the ISO in a virtual machine before writing it to USB. Open **OBSIDIAN Security Center** from the desktop or application menu. Select Message or URL, enter input, and choose Analyze locally. Command-line scans are also available through `obsidian-scan text "example"` and `obsidian-scan url "https://example.com"`.

The ISO does not automatically enable persistence or install onto a disk. No remote management or background malware scanning is claimed. Existing OS and disks should not be modified by the build or normal live boot. Do not treat this experimental build as production-ready until the ISO is built and tested in a VM.
