import tkinter as tk
from tkinter import messagebox

# Dictionary utama
data_dict = {}

# Fungsi menambah data
def add_data():
    key = entry_key.get()
    value = entry_value.get()

    if key == "" or value == "":
        messagebox.showerror("Error", "Key dan Value tidak boleh kosong!")
        return

    data_dict[key] = value
    messagebox.showinfo("Sukses", f"Data '{key}: {value}' berhasil ditambahkan")
    update_display()

# Fungsi mencari data
def search_data():
    key = entry_key.get()

    if key in data_dict:
        messagebox.showinfo("Ditemukan", f"{key} : {data_dict[key]}")
    else:
        messagebox.showerror("Tidak ditemukan", f"Key '{key}' tidak ada dalam dictionary")

# Fungsi menghapus data
def delete_data():
    key = entry_key.get()

    if key in data_dict:
        del data_dict[key]
        messagebox.showinfo("Dihapus", f"Data dengan key '{key}' berhasil dihapus")
        update_display()
    else:
        messagebox.showerror("Tidak ditemukan", f"Key '{key}' tidak ada")

# Fungsi menampilkan dictionary
def update_display():
    text_area.config(state="normal")
    text_area.delete("1.0", tk.END)

    if not data_dict:
        text_area.insert(tk.END, "Dictionary masih kosong...\n")

    else:
        for k, v in data_dict.items():
            text_area.insert(tk.END, f"{k} : {v}\n")

    text_area.config(state="disabled")


# GUI

window = tk.Tk()
window.title("Program Dictionary Python dengan Tkinter")
window.geometry("600x400")
window.configure(bg="#1e1e1e")

title = tk.Label(window, text="PROGRAM DICTIONARY PYTHON", font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="white")
title.pack(pady=10)

frame_input = tk.Frame(window, bg="#1e1e1e")
frame_input.pack(pady=10)

label_key = tk.Label(frame_input, text="Key :", font=("Arial", 12),
                     bg="#1e1e1e", fg="white")
label_key.grid(row=0, column=0, padx=5)

entry_key = tk.Entry(frame_input, font=("Arial", 14), width=20)
entry_key.grid(row=0, column=1, padx=10)

label_value = tk.Label(frame_input, text="Value :", font=("Arial", 12),
                       bg="#1e1e1e", fg="white")
label_value.grid(row=1, column=0, padx=5, pady=5)

entry_value = tk.Entry(frame_input, font=("Arial", 14), width=20)
entry_value.grid(row=1, column=1, padx=10)

# Tombol-tombol
frame_buttons = tk.Frame(window, bg="#1e1e1e")
frame_buttons.pack(pady=10)

btn_add = tk.Button(frame_buttons, text="Tambah Data", width=15,
                    bg="#06B3B3", fg="white", font=("Arial", 12, "bold"),
                    command=add_data)
btn_add.grid(row=0, column=0, padx=10)

btn_search = tk.Button(frame_buttons, text="Cari Data", width=15,
                       bg="#3CFA65", fg="white", font=("Arial", 12, "bold"),
                       command=search_data)
btn_search.grid(row=0, column=1, padx=10)

btn_delete = tk.Button(frame_buttons, text="Hapus Data", width=15,
                       bg="#f44336", fg="white", font=("Arial", 12, "bold"),
                       command=delete_data)
btn_delete.grid(row=0, column=2, padx=10)

# Area tampil dictionary
text_area = tk.Text(window, font=("Consolas", 14), width=50, height=10,
                    bg="#252526", fg="white", insertbackground="white")
text_area.pack(pady=10)

update_display()

window.mainloop()
