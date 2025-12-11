import tkinter as tk
from tkinter import messagebox

# INTERPOLATION SEARCH ALGORITMA

def interpolation_search(arr, target):
    low, high = 0, len(arr) - 1
    langkah = f"Array: {arr}\n"
    langkah += f"Target: {target}\n\n"

    while low <= high and target >= arr[low] and target <= arr[high]:

        # Menghindari pembagian 0
        if arr[high] == arr[low]:
            if arr[low] == target:
                langkah += f"Semua elemen sama. Target ditemukan pada indeks {low}.\n"
                return langkah
            break

        # Rumus posisi interpolasi
        pos = low + int(((target - arr[low]) * (high - low)) / (arr[high] - arr[low]))

        langkah += f"Low={low}, High={high}, Posisi={pos}\n"
        langkah += f"Banding arr[{pos}] = {arr[pos]} dengan target {target}\n"

        if arr[pos] == target:
            langkah += f"\nHASIL: Data ditemukan pada indeks {pos}."
            return langkah
        elif arr[pos] < target:
            langkah += "Target lebih besar → Maju ke kanan.\n\n"
            low = pos + 1
        else:
            langkah += "Target lebih kecil → Mundur ke kiri.\n\n"
            high = pos - 1

    langkah += "\nHASIL: Data tidak ditemukan."
    return langkah


# APPLICATION

def mulai_cari():
    try:
        arr = list(map(int, entry_array.get().split(",")))
        target = int(entry_target.get())
    except:
        messagebox.showerror("Error", "Input salah!\nContoh array: 5,7,9,12,20")
        return

    arr.sort()  # Interpolation search membutuhkan array terurut

    hasil = interpolation_search(arr, target)

    # Tampilkan di text box
    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, hasil, "text")
    text_output.config(state=tk.DISABLED)


# GUI 

root = tk.Tk()
root.title("Interpolation Search - Tkinter GUI")
root.geometry("600x560")
root.config(bg="#1e1e2e")

# Judul
label_title = tk.Label(
    root,
    text="ALGORITMA INTERPOLATION SEARCH",
    font=("Arial", 20, "bold"),
    fg="#00eaff",
    bg="#1e1e2e"
)
label_title.pack(pady=15)

# Frame input
frame_input = tk.Frame(root, bg="#1e1e2e")
frame_input.pack(pady=10)

# Input array
tk.Label(frame_input, text="Masukkan Array (dipisah koma):",
         font=("Arial", 12), fg="white", bg="#1e1e2e").grid(row=0, column=0, sticky="w")
entry_array = tk.Entry(frame_input, width=40, font=("Arial", 12))
entry_array.grid(row=1, column=0, padx=5, pady=8)

# Input target
tk.Label(frame_input, text="Angka yang dicari:",
         font=("Arial", 12), fg="white", bg="#1e1e2e").grid(row=2, column=0, sticky="w")
entry_target = tk.Entry(frame_input, width=20, font=("Arial", 12))
entry_target.grid(row=3, column=0, padx=5, pady=8)

# Tombol Cari
btn_search = tk.Button(
    root,
    text="Mulai Pencarian",
    font=("Arial", 14, "bold"),
    bg="#6fcaf1",
    fg="white",
    width=20,
    command=mulai_cari
)
btn_search.pack(pady=15)

# Output text box
text_output = tk.Text(
    root,
    height=20,
    width=70,
    font=("Courier", 12),
    bg="#2b2b3b",
    fg="white"
)
text_output.pack(pady=10)
text_output.tag_config("text", foreground="#9dff6c")
text_output.config(state=tk.DISABLED)

root.mainloop()
