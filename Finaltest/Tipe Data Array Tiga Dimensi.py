import tkinter as tk
from tkinter import messagebox

# ARRAY 3 DIMENSI 

array3d = []

# FUNCTION
def tambah_data():
    try:
        x = int(entry_x.get())
        y = int(entry_y.get())
        z = int(entry_z.get())
    except:
        messagebox.showerror("Error", "Index harus berupa angka!")
        return

    nilai = entry_nilai.get().strip()
    if nilai == "":
        messagebox.showwarning("Peringatan", "Nilai tidak boleh kosong!")
        return

    # Memperluas ukuran array otomatis
    while len(array3d) <= x:
        array3d.append([])
    while len(array3d[x]) <= y:
        array3d[x].append([])
    while len(array3d[x][y]) <= z:
        array3d[x][y].append("")

    array3d[x][y][z] = nilai

    tampilkan_array()

    entry_x.delete(0, tk.END)
    entry_y.delete(0, tk.END)
    entry_z.delete(0, tk.END)
    entry_nilai.delete(0, tk.END)


def tampilkan_array():
    listbox.delete(0, tk.END)
    for x in range(len(array3d)):
        for y in range(len(array3d[x])):
            for z in range(len(array3d[x][y])):
                value = array3d[x][y][z]
                listbox.insert(tk.END, f"[{x}][{y}][{z}]   ->   {value}")


# GUI 
root = tk.Tk()
root.title("Array 3 Dimensi - Tkinter Berwarna")
root.geometry("550x520")
root.config(bg="#1E1F26")   # DARK MODE

# Judul
tk.Label(root, text="ARRAY 3 DIMENSI",
         font=("Arial", 16, "bold"),
         bg="#1E1F26", fg="#00E5FF").pack(pady=10)

# Frame input index
frame = tk.Frame(root, bg="#1E1F26")
frame.pack(pady=10)

def mk_label(text):
    return tk.Label(frame, text=text, bg="#1E1F26", fg="#00E5FF", font=("Arial", 11, "bold"))

mk_label("X:").grid(row=0, column=0)
entry_x = tk.Entry(frame, width=6, font=("Arial", 11))
entry_x.grid(row=0, column=1, padx=5)

mk_label("Y:").grid(row=0, column=2)
entry_y = tk.Entry(frame, width=6, font=("Arial", 11))
entry_y.grid(row=0, column=3, padx=5)

mk_label("Z:").grid(row=0, column=4)
entry_z = tk.Entry(frame, width=6, font=("Arial", 11))
entry_z.grid(row=0, column=5, padx=5)

# Input nilai
tk.Label(root, text="Nilai:",
         bg="#1E1F26", fg="#00E5FF",
         font=("Arial", 12, "bold")).pack()
entry_nilai = tk.Entry(root, width=25, font=("Arial", 12))
entry_nilai.pack(pady=5)

# Tombol tambah
tk.Button(root, text="TAMBAHKAN DATA", command=tambah_data,
          bg="#60E239", fg="black", activebackground="#FB8C00",
          font=("Arial", 11, "bold"), width=20).pack(pady=10)

# Listbox output
tk.Label(root, text="Isi Array 3 Dimensi:",
         bg="#1E1F26", fg="#00E5FF",
         font=("Arial", 12, "bold")).pack(pady=5)

listbox = tk.Listbox(root, width=60, height=15,
                     bg="#2E3038", fg="white",
                     selectbackground="#00E5FF",
                     font=("Consolas", 11))
listbox.pack(pady=10)

# Jalankan TK
root.mainloop()
