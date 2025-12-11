import tkinter as tk
from tkinter import messagebox

def proses_float():
    angka = entry.get()

    try:
        # Coba ubah ke float
        nilai = float(angka)
    except:
        messagebox.showerror("Error", "Masukkan angka desimal (float)!")
        return

    # Menampilkan informasi tentang float
    result = (
        f"Angka yang dimasukkan : {nilai}\n"
        f"Tipe data : {type(nilai)}\n\n"
        f"OPERASI FLOAT:\n"
        f"{nilai} + 2.5 = {nilai + 2.5}\n"
        f"{nilai} - 1.2 = {nilai - 1.2}\n"
        f"{nilai} * 3 = {nilai * 3}\n"
        f"{nilai} / 2 = {nilai / 2}\n"
    )

    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)
    text_area.insert(tk.END, result)
    text_area.config(state="disabled")


# GUI 

window = tk.Tk()
window.title("Program Tipe Data Float - Tkinter")
window.geometry("600x350")
window.configure(bg="#1e1e1e")

title = tk.Label(window, text="TIPE DATA FLOAT (float)", font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="white")
title.pack(pady=10)

lbl = tk.Label(window, text="Masukkan Angka Float (desimal):",
               font=("Arial", 12), bg="#1e1e1e", fg="white")
lbl.pack()

entry = tk.Entry(window, font=("Arial", 14), width=20)
entry.pack(pady=5)

btn = tk.Button(window, text="Proses", font=("Arial", 12, "bold"),
                bg="#2196F3", fg="white", width=15, command=proses_float)
btn.pack(pady=10)

text_area = tk.Text(window, font=("Consolas", 14), width=50, height=10,
                    bg="#252526", fg="white", insertbackground="white")
text_area.pack(pady=10)

window.mainloop()
