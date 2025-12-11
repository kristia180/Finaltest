import tkinter as tk
from tkinter import messagebox

def proses_integer():
    angka = entry.get()

    # Cek apakah input integer
    if not angka.isdigit():
        messagebox.showerror("Error", "Masukkan hanya angka bulat (Integer)!")
        return

    angka = int(angka)

    # Menampilkan informasi tentang integer
    result = (
        f"Angka yang dimasukkan : {angka}\n"
        f"Tipe data : {type(angka)}\n\n"
        f"OPERASI INTEGER:\n"
        f"{angka} + 10 = {angka + 10}\n"
        f"{angka} - 5 = {angka - 5}\n"
        f"{angka} * 2 = {angka * 2}\n"
        f"{angka} / 3 = {angka / 3:.2f}\n"
    )

    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, result)
    text_area.config(state="disabled")


# GUI 

window = tk.Tk()
window.title("Program Tipe Data Integer - Tkinter")
window.geometry("600x350")
window.configure(bg="#1e1e1e")

title = tk.Label(window, text="TIPE DATA INTEGER (int)", font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="white")
title.pack(pady=10)

lbl = tk.Label(window, text="Masukkan Angka Integer:",
               font=("Arial", 12), bg="#1e1e1e", fg="white")
lbl.pack()

entry = tk.Entry(window, font=("Arial", 14), width=20)
entry.pack(pady=5)

btn = tk.Button(window, text="Proses", font=("Arial", 12, "bold"),
                bg="#4CAF50", fg="white", width=15, command=proses_integer)
btn.pack(pady=10)

text_area = tk.Text(window, font=("Consolas", 14), width=50, height=10,
                    bg="#252526", fg="white", insertbackground="white")
text_area.pack(pady=10)

window.mainloop()
