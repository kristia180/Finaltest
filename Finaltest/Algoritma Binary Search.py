import tkinter as tk
from tkinter import messagebox

# BINARY SEARCH FUNCTION

def binary_search(arr, target, display):
    left, right = 0, len(arr) - 1
    step_text = ""

    step_text += f"Array: {arr}\n"
    step_text += f"Mencari: {target}\n\n"

    while left <= right:
        mid = (left + right) // 2
        step_text += f"Left={left}, Right={right}, Mid={mid}\n"
        step_text += f"Bandingkan target({target}) dengan arr[{mid}] = {arr[mid]}\n"

        if arr[mid] == target:
            step_text += "\nHASIL: Data ditemukan!\n"
            return step_text

        elif arr[mid] < target:
            step_text += f"Target lebih besar → Geser ke kanan.\n\n"
            left = mid + 1
        else:
            step_text += f"Target lebih kecil → Geser ke kiri.\n\n"
            right = mid - 1

    step_text += "\nHASIL: Data TIDAK ditemukan!"
    return step_text


# TKINTER UI

def mulai_pencarian():
    try:
        # Ambil input
        arr = list(map(int, entry_array.get().split(",")))
        target = int(entry_target.get())
    except:
        messagebox.showerror("Error", "Input tidak valid!\nGunakan format: 7,4,2,9,1")
        return

    # Urutkan array
    arr.sort()

    # Jalankan binary search
    hasil = binary_search(arr, target, text_display)

    # Tampilkan hasil
    text_display.config(state=tk.NORMAL)
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, hasil, "normal")
    text_display.config(state=tk.DISABLED)


# GUI

root = tk.Tk()
root.title("Binary Search - Tkinter")
root.geometry("600x550")
root.config(bg="#1e1e2e")

# Judul
label_title = tk.Label(root, text="ALGORITMA BINARY SEARCH",
                       font=("Arial", 20, "bold"), fg="#00eaff", bg="#1e1e2e")
label_title.pack(pady=15)

# FRAME INPUT
frame_input = tk.Frame(root, bg="#1e1e2e")
frame_input.pack(pady=10)

# Input array
tk.Label(frame_input, text="Masukkan Array (pisahkan dengan koma):",
         font=("Arial", 12), fg="white", bg="#1e1e2e").grid(row=0, column=0, sticky="w")
entry_array = tk.Entry(frame_input, width=40, font=("Arial", 12))
entry_array.grid(row=1, column=0, padx=5, pady=5)

# Input angka target
tk.Label(frame_input, text="Angka yang dicari:",
         font=("Arial", 12), fg="white", bg="#1e1e2e").grid(row=2, column=0, sticky="w")
entry_target = tk.Entry(frame_input, width=20, font=("Arial", 12))
entry_target.grid(row=3, column=0, padx=5, pady=5)

# Tombol mulai
btn_cari = tk.Button(root, text="Mulai Pencarian",
                     font=("Arial", 14, "bold"), bg="#4caf50",
                     fg="white", width=20, command=mulai_pencarian)
btn_cari.pack(pady=15)

# TEXT OUTPUT
text_display = tk.Text(root, height=18, width=70,
                       font=("Courier", 12), bg="#2b2b3b", fg="white")
text_display.pack(pady=10)

# Warna teks
text_display.tag_config("normal", foreground="#9dff6c")

text_display.config(state=tk.DISABLED)

root.mainloop()
