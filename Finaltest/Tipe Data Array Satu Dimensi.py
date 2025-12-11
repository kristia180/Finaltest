import tkinter as tk

# Array satu dimensi

angka = [15, 25, 30, 45, 55]

def tampilkan_array():
    output = ""
    output += "Isi Array:\n"
    output += str(angka) + "\n\n"

    output += f"Elemen pertama: {angka[0]}\n"
    output += f"Elemen ketiga: {angka[2]}\n\n"

    # operasi perubahan nilai
    angka[1] = 20
    output += f"Setelah mengubah elemen kedua menjadi 25:\n{angka}\n\n"

    # tambah elemen
    angka.append(65)
    output += f"Setelah menambah elemen 65:\n{angka}\n\n"

    # hapus elemen
    angka.remove(30)
    output += f"Setelah menghapus elemen 30:\n{angka}\n\n"

    output += f"Panjang array: {len(angka)}"

    text_area.config(state='normal')
    text_area.delete(1.0, tk.END)
    text_area.insert(tk.END, output)
    text_area.config(state='disabled')

# Membuat window Tkinter
root = tk.Tk()
root.title("Contoh Array Satu Dimensi (Tkinter)")
root.geometry("500x400")
root.config(bg="#1e1f26")  # warna background window

# Tombol untuk menampilkan hasil
btn = tk.Button(
    root, 
    text="Tampilkan Array", 
    command=tampilkan_array, 
    font=("Arial", 12),
    bg="#4CAF50",        # warna tombol
    fg="white",          # warna teks tombol
    activebackground="#45a049"
)
btn.pack(pady=10)

# Area teks untuk output
text_area = tk.Text(
    root, 
    height=20, 
    width=60, 
    font=("Consolas", 10),
    bg="#f2f3f8",        # warna latar
    fg="#111212",        # warna teks
    insertbackground="white"
)
text_area.pack()

root.mainloop()
