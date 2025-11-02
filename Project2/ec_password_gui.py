#!/usr/bin/env python3
# ec_password_gui.py
#
# GUI wrapper for the EC-based strong password generator (Project 2).
# Requires ec_password_generator.py in the same directory.

import os
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox

from Project1 import ec_password_generator as ec  


class PasswordGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("EC-Based Strong Password Generator")
        self.geometry("600x400")
        self.configure(bg="#141414")

        # Fonts and colors
        self.primary_color = "#4CAF50"
        self.text_color = "#FFFFFF"
        self.entry_bg = "#1E1E1E"

        self._build_widgets()

    def _build_widgets(self):
        # Title
        title = tk.Label(
            self,
            text="Strong Password Generator",
            font=("Segoe UI", 20, "bold"),
            fg=self.primary_color,
            bg="#141414",
        )
        title.pack(pady=20)

        # Frame for inputs
        frame_inputs = tk.Frame(self, bg="#141414")
        frame_inputs.pack(pady=10)

        # Memorable password input
        tk.Label(
            frame_inputs,
            text="Memorable Password:",
            font=("Segoe UI", 12),
            fg=self.text_color,
            bg="#141414",
        ).grid(row=0, column=0, sticky="e", padx=10, pady=5)
        self.entry_memorable = tk.Entry(
            frame_inputs,
            font=("Consolas", 12),
            width=30,
            bg=self.entry_bg,
            fg=self.text_color,
            relief="flat",
            insertbackground=self.text_color,
        )
        self.entry_memorable.grid(row=0, column=1, pady=5)

        # Length input
        tk.Label(
            frame_inputs,
            text="Desired Length:",
            font=("Segoe UI", 12),
            fg=self.text_color,
            bg="#141414",
        ).grid(row=1, column=0, sticky="e", padx=10, pady=5)
        self.entry_length = tk.Entry(
            frame_inputs,
            font=("Consolas", 12),
            width=10,
            bg=self.entry_bg,
            fg=self.text_color,
            relief="flat",
            insertbackground=self.text_color,
        )
        self.entry_length.grid(row=1, column=1, sticky="w", pady=5)

        # Generate button
        btn_generate = tk.Button(
            self,
            text="Generate Password",
            bg=self.primary_color,
            fg="white",
            font=("Segoe UI", 12, "bold"),
            relief="flat",
            command=self._on_generate,
        )
        btn_generate.pack(pady=20)

        # Output field
        tk.Label(
            self,
            text="Generated Strong Password:",
            font=("Segoe UI", 12),
            fg=self.text_color,
            bg="#141414",
        ).pack(pady=(10, 0))

        self.output_box = tk.Text(
            self,
            height=2,
            width=45,
            font=("Consolas", 14),
            bg="#1E1E1E",
            fg="#00FF7F",
            relief="flat",
            wrap="none",
            state="disabled",
        )
        self.output_box.pack(pady=10)

        # Save button
        btn_save = tk.Button(
            self,
            text="Save to File",
            bg="#2196F3",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            relief="flat",
            command=self._save_to_file,
        )
        btn_save.pack(pady=5)

        # Status bar
        self.status_label = tk.Label(
            self,
            text="Ready",
            font=("Segoe UI", 10),
            fg="#AAAAAA",
            bg="#141414",
        )
        self.status_label.pack(side="bottom", pady=5)

    # ----------------------------------------------------------------------
    # Event handlers
    # ----------------------------------------------------------------------
    def _on_generate(self):
        memorable = self.entry_memorable.get().strip()
        length_text = self.entry_length.get().strip()

        if not memorable or not length_text:
            messagebox.showerror("Error", "Please enter both fields.")
            return

        try:
            length = int(length_text)
            if length <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Length must be a positive integer.")
            return

        # Run generation on separate thread (avoid freezing UI)
        threading.Thread(target=self._generate_password, args=(memorable, length)).start()

    def _generate_password(self, memorable: str, length: int):
        self._set_status("Generating...")
        try:
            strong = ec.generate_ec_strong_password(memorable, length, ec.ec_formula)
            self._show_password(strong)
            self._set_status("Password generated successfully.")
        except Exception as e:
            self._set_status("Error generating password.")
            messagebox.showerror("Generation Error", str(e))

    def _show_password(self, password: str):
        self.output_box.config(state="normal")
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, password)
        self.output_box.config(state="disabled")

    def _save_to_file(self):
        content = self.output_box.get("1.0", tk.END).strip()
        if not content:
            messagebox.showinfo("No password", "No password to save yet.")
            return

        filename = filedialog.asksaveasfilename(
            title="Save Password",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
        )
        if filename:
            try:
                ec._secure_write_text_file(filename, content + "\n")
                messagebox.showinfo("Saved", f"Password saved to {filename}")
            except Exception as e:
                messagebox.showerror("Save Error", str(e))

    def _set_status(self, msg: str):
        self.status_label.config(text=msg)


if __name__ == "__main__":
    app = PasswordGUI()
    app.mainloop()
