import tkinter as tk
from tkinter import messagebox

# SELECTION SORT ALGORITHM

def selection_sort(arr):
    langkah = "=== PROSES SELECTION SORT ===\n\n"
    n = len(arr)

    for i in range(n - 1):
        min_idx = i
        langkah += f"Pass {i+1}:\n"
        langkah += f"  Mulai dari indeks {i}, nilai awal minimum = {arr[min_idx]}\n"

        # Mencari index minimum
        for j in range(i + 1, n):
            langkah += f"    Bandingkan {arr[j]} dengan {arr[min_idx]}"
            if arr[j] < arr[min_idx]:
                min_idx = j
                langkah += " → Minimum baru!\n"
            else:
                langkah += " → Tetap\n"

        # Swap jika perlu
        if min_idx != i:
            langkah += f"  Swap {arr[i]} dengan {arr[min_idx]}\n"
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        else:
            langkah += f"  Tidak ada swap, {arr[i]} sudah minimum\n"

        langkah += f"  Hasil sementara: {arr}\n\n"

    langkah += f"\nHASIL AKHIR: {arr}"
    return langkah


# GUI

def mulai_sort():
    try:
        arr = list(map(int, entry_array.get().split(",")))
    except:
        messagebox.showerror("Error", "Format array salah!\nContoh: 7,3,5,1,9")
        return

    hasil = selection_sort(arr.copy())

    text_output.config(state=tk.NORMAL)
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, hasil, "text")
    text_output.config(state=tk.DISABLED)


# GUI WINDOW
root = tk.Tk()
root.title("Selection Sort - Tkinter GUI")
root.geometry("600x600")
root.config(bg="#1e1e2e")

# Judul
label_title = tk.Label(
    root,
    text="ALGORITMA SELECTION SORT",
    font=("Arial", 20, "bold"),
    fg="#00eaff",
    bg="#1e1e2e"
)
label_title.pack(pady=15)

# Frame Input
frame_input = tk.Frame(root, bg="#1e1e2e")
frame_input.pack(pady=10)

tk.Label(
    frame_input,
    text="Masukkan Array (pisahkan dengan koma):",
    font=("Arial", 12),
    fg="white",
    bg="#1e1e2e"
).grid(row=0, column=0, sticky="w")

entry_array = tk.Entry(frame_input, width=40, font=("Arial", 12))
entry_array.grid(row=1, column=0, padx=5, pady=8)

# Tombol Sort
btn_sort = tk.Button(
    root,
    text="Mulai Sorting",
    font=("Arial", 14, "bold"),
    bg="#4caf50",
    fg="white",
    width=20,
    command=mulai_sort
)
btn_sort.pack(pady=15)

# Kotak Output
text_output = tk.Text(
    root,
    height=22,
    width=70,
    font=("Courier", 12),
    bg="#2b2b3b",
    fg="white"
)
text_output.pack(pady=10)

text_output.tag_config("text", foreground="#9dff6c")
text_output.config(state=tk.DISABLED)

root.mainloop()
