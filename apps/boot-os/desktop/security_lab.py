#!/usr/bin/env python3
import json
import os
import platform
import shutil
import socket
import tkinter as tk
from tkinter import ttk

BG = "#080f1e"
PANEL = "#10223a"
FG = "#e4f4ff"
CYAN = "#50cfff"

MODULES = [
    ("Reconnaissance Lab", "Placeholder only — no network scanning"),
    ("Penetration Testing Lab", "Placeholder only — no exploitation"),
    ("Wireless Research Lab", "Placeholder only — no wireless attacks"),
    ("Forensics Lab", "Future authorized investigation workspace"),
    ("Security Automation", "Future reviewed and permission-gated workflows"),
]

def local_health():
    disk = shutil.disk_usage(os.path.expanduser("~"))
    return {
        "hostname": socket.gethostname(),
        "system": platform.system(),
        "kernel": platform.release(),
        "architecture": platform.machine(),
        "home_disk_free_gb": round(disk.free / 1024**3, 2),
        "home_disk_total_gb": round(disk.total / 1024**3, 2),
        "network_scan": "not performed",
    }

def main():
    root = tk.Tk()
    root.title("OBSIDIAN | Cybersecurity Center")
    root.geometry("880x640")
    root.configure(bg=BG)
    tk.Label(root, text="OBSIDIAN / CYBERSECURITY CENTER", fg=CYAN, bg=BG, font=("DejaVu Sans", 20, "bold")).pack(anchor="w", padx=25, pady=20)
    tabs = ttk.Notebook(root)
    tabs.pack(fill="both", expand=True, padx=24, pady=10)
    defense = tk.Frame(tabs, bg=PANEL)
    lab = tk.Frame(tabs, bg=PANEL)
    tabs.add(defense, text="Defense & Health")
    tabs.add(lab, text="Future Research Labs")
    tk.Label(defense, text="Local device information (read-only)", fg=FG, bg=PANEL, font=("DejaVu Sans", 14)).pack(anchor="w", padx=15, pady=15)
    output = tk.Text(defense, bg=BG, fg=FG, height=16, font=("DejaVu Sans Mono", 11))
    output.pack(fill="both", expand=True, padx=15, pady=10)
    def refresh():
        output.delete("1.0", "end")
        output.insert("1.0", json.dumps(local_health(), indent=2))
    tk.Button(defense, text="Refresh local status", command=refresh).pack(anchor="w", padx=15, pady=10)
    refresh()
    tk.Label(lab, text="Science expo demonstration modules — intentionally inactive", fg=CYAN, bg=PANEL, font=("DejaVu Sans", 12)).pack(anchor="w", padx=15, pady=18)
    for name, description in MODULES:
        item = tk.Frame(lab, bg=BG, padx=14, pady=10)
        item.pack(fill="x", padx=15, pady=4)
        tk.Label(item, text=name, fg=FG, bg=BG, font=("DejaVu Sans", 12, "bold")).pack(anchor="w")
        tk.Label(item, text=description, fg=CYAN, bg=BG).pack(anchor="w")
    tk.Label(root, text="No intrusive tests are performed. Future modules require authorization and independent review.", fg=FG, bg=BG).pack(padx=20, pady=15)
    root.mainloop()

if __name__ == "__main__":
    main()
