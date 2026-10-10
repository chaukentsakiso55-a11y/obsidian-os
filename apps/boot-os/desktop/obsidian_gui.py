#!/usr/bin/env python3
import json
import os
import sys
import tkinter as tk
from tkinter import ttk

sys.path.insert(0, "/opt/obsidian")
from obsidian.scoring import analyze

BG = "#080f1e"
PANEL = "#101e33"
FG = "#e0f2ff"
ACCENT = "#3bc9f5"

class ObsidianDesktop(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("OBSIDIAN | Security Center")
        self.geometry("1000x690")
        self.minsize(720, 500)
        self.configure(bg=BG)
        self.kind = tk.StringVar(value="text")
        self.status = tk.StringVar(value="Ready. Analysis runs locally; no input is uploaded.")
        self.build()

    def build(self):
        header = tk.Frame(self, bg=BG, padx=28, pady=22)
        header.pack(fill="x")
        tk.Label(header, text="◈ OBSIDIAN", font=("DejaVu Sans", 28, "bold"), fg=ACCENT, bg=BG).pack(anchor="w")
        tk.Label(header, text="BOOT OS  /  OFFLINE SECURITY WORKSPACE", font=("DejaVu Sans", 11), fg=FG, bg=BG).pack(anchor="w")
        body = tk.Frame(self, bg=PANEL, padx=24, pady=20)
        body.pack(fill="both", expand=True, padx=28, pady=(0, 20))
        tk.Label(body, text="Local threat assessment", font=("DejaVu Sans", 18, "bold"), fg=FG, bg=PANEL).pack(anchor="w")
        controls = tk.Frame(body, bg=PANEL)
        controls.pack(fill="x", pady=12)
        for label, value in (("Message", "text"), ("URL", "url")):
            tk.Radiobutton(controls, text=label, variable=self.kind, value=value, bg=PANEL, fg=FG, selectcolor=BG, activebackground=PANEL, activeforeground=FG).pack(side="left", padx=(0, 20))
        tk.Label(body, text="Paste a message or website address to inspect:", bg=PANEL, fg=FG).pack(anchor="w")
        self.input = tk.Text(body, height=7, bg=BG, fg=FG, insertbackground=ACCENT, wrap="word", relief="flat", padx=12, pady=12, font=("DejaVu Sans Mono", 11))
        self.input.pack(fill="x", pady=10)
        buttons = tk.Frame(body, bg=PANEL)
        buttons.pack(fill="x")
        tk.Button(buttons, text="Analyze locally", command=self.assess, bg=ACCENT, fg=BG, padx=18, pady=8).pack(side="left")
        tk.Button(buttons, text="Clear", command=self.clear, padx=16, pady=8).pack(side="left", padx=12)
        self.output = tk.Text(body, height=10, bg=BG, fg=FG, relief="flat", wrap="word", state="disabled", padx=12, pady=12, font=("DejaVu Sans Mono", 10))
        self.output.pack(fill="both", expand=True, pady=14)
        tk.Label(self, textvariable=self.status, bg=BG, fg=ACCENT, anchor="w").pack(fill="x", padx=28, pady=(0, 16))

    def assess(self):
        value = self.input.get("1.0", "end-1c").strip()
        if not value:
            self.status.set("Enter a message or URL first.")
            return
        try:
            result = analyze(self.kind.get(), value)
            self.display(json.dumps(result, indent=2))
            self.status.set("Completed locally. Heuristic results are not a guarantee of safety.")
        except (ValueError, TypeError) as exc:
            self.display(str(exc))
            self.status.set("Analysis could not complete.")

    def display(self, value):
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.insert("1.0", value)
        self.output.configure(state="disabled")

    def clear(self):
        self.input.delete("1.0", "end")
        self.display("")
        self.status.set("Ready.")

if __name__ == "__main__":
    ObsidianDesktop().mainloop()
