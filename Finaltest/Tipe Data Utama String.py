import tkinter as tk
from tkinter import messagebox

def proses_string():
    teks = entry.get()

    if teks == "":
        messagebox.showwarning("Peringatan", "Input string tidak boleh kosong!")
        return

    result = (
        f"String yang dimasukkan : '{teks}'\n"
        f"Tipe data : {type(teks)}\n\n"
        f"INFORMASI STRING:\n"
        f"Panjang string               : {len(teks)}\n"
        f"Huruf besar (upper)      : {teks.upper()}\n"
        f"Huruf kecil (lower)       : {teks.lower()}\n"
        f"Karakter pertama          : {teks[0]}\n"
        f"Karakter terakhir         : {teks[-1]}\n"
        f"Alfabet semua?            : {teks.isalpha()}\n"
        f"Angka semua?              : {teks.isdigit()}\n"
    )

    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, result)
    text_area.config(state="disabled")


# GUI 

window = tk.Tk()
window.title("Program Tipe Data String - Tkinter")
window.geometry("650x380")
window.configure(bg="#1e1e1e")

title = tk.Label(window, text="TIPE DATA STRING (str)", font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="white")
title.pack(pady=10)

lbl = tk.Label(window, text="Masukkan Teks (String):",
               font=("Arial", 12), bg="#1e1e1e", fg="white")
lbl.pack()

entry = tk.Entry(window, font=("Arial", 14), width=30)
entry.pack(pady=5)

btn = tk.Button(window, text="Proses", font=("Arial", 12, "bold"),
                bg="#ff9800", fg="white", width=15, command=proses_string)
btn.pack(pady=10)

text_area = tk.Text(window, font=("Consolas", 14), width=55, height=11,
                    bg="#252526", fg="white", insertbackground="white")
text_area.pack(pady=10)

window.mainloop()
