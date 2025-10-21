import tkinter as tk
from tkinter import messagebox
import math, numpy as np
from scipy.stats import rankdata

# --- EC Function (replace with yours) ---
def ec_formula(row):
    return 0.432357 + (-0.498752 * math.cos(
        0.594808 * (-4.10993 * math.cosh(row) -
        (0.590558 + math.atanh(math.cos(
        math.tan(math.cos(row/(-0.00153462))) + row*row))))))

def ec_cipher(N, key):
    arr = np.empty(N)
    arr[0] = key
    for i in range(N-1):
        arr[i+1] = ec_formula(arr[i])
    return arr

def transform_to_uniform(input_array):
    ranks = rankdata(input_array, method='average')
    cdf = (ranks - 1) / (len(input_array) - 1)
    return cdf

def generate_password(memorable, length):
    seed = sum(ord(c)/256 for c in memorable)
    stream = transform_to_uniform(ec_cipher(length, seed))
    password = ''.join(chr(int(abs(v*1000) % 94) + 33) for v in stream)
    return password

# --- GUI ---
def create_gui():
    win = tk.Tk()
    win.title("EC-Based Strong Password Generator")
    win.geometry("500x300")
    win.configure(bg="#222")

    tk.Label(win, text="Enter a memorable password:", fg="white", bg="#222").pack(pady=5)
    memorable_entry = tk.Entry(win, show="*")
    memorable_entry.pack(pady=5)

    tk.Label(win, text="Desired password length:", fg="white", bg="#222").pack(pady=5)
    length_entry = tk.Entry(win)
    length_entry.pack(pady=5)

    output_label = tk.Label(win, text="", fg="#0f0", bg="#222", wraplength=450)
    output_label.pack(pady=10)

    def on_generate():
        try:
            memorable = memorable_entry.get()
            length = int(length_entry.get())
            strong_pw = generate_password(memorable, length)
            output_label.config(text=f"Strong Password:\n{strong_pw}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(win, text="Generate", command=on_generate, bg="#444", fg="white").pack(pady=10)
    win.mainloop()

if __name__ == "__main__":
    print("Testing password generation without GUI...")
    print(generate_password("myweakpass", 12))
