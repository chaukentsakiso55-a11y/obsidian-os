# OBSIDIAN Boot OS (experimental)

This is a Debian 12 live ISO configuration with XFCE and an offline OBSIDIAN Python analyzer. It is **not** a new kernel, a Windows replacement, or a production security distribution.

Build inside a disposable Debian 12 VM with sufficient disk space:

```sh
sudo apt-get update
sudo apt-get install -y live-build
sudo bash apps/boot-os/build-live.sh
```

A built ISO should be tested in a virtual machine first. Do not install to internal disks. USB persistence is optional and must be configured separately; the boot parameter alone does not create a persistent volume.

The live configuration copies the Python `obsidian` package into `/usr/local/share/obsidian` during CI or before the build. The desktop shortcut is a demo only and must be revised before release.
