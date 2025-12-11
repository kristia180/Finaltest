import tkinter as tk
from tkinter import messagebox
import time

def insertion_sort_visual(arr, labels, window):
    for i in range(1, len(arr)):
        key = arr[i]

        # Highlight key
        labels[i].config(bg="yellow")
        window.update()
        time.sleep(0.6)

        j = i - 1
        while j >= 0 and arr[j] > key:
            # Highlight comparison
            labels[j].config(bg="red")
            window.update()
            time.sleep(0.6)

            arr[j + 1] = arr[j]
            labels[j + 1].config(text=str(arr[j]))

            labels[j].config(bg="lightblue")
            window.update()
            time.sleep(0.4)

            j -= 1

        arr[j + 1] = key
        labels[j + 1].config(text=str(key), bg="lightgreen")
        window.update()
        time.sleep(0.6)

        # Reset all to blue
        for lbl in labels:
            lbl.config(bg="skyblue")

    messagebox.showinfo("Selesai", "Array berhasil diurutkan!")


def start_sort():
    data = entry.get()
    try:
        arr = list(map(int, data.split()))
    except:
        messagebox.showerror("Error", "Masukkan angka dipisah spasi!")
        return

    # Hapus label lama
    for lbl in frame_labels.winfo_children():
        lbl.destroy()

    labels = []
    for num in arr:
        lbl = tk.Label(frame_labels, text=str(num), font=("Arial", 16, "bold"),
                       width=4, height=2, bg="skyblue", relief="ridge", bd=3)
        lbl.pack(side="left", padx=5, pady=10)
        labels.append(lbl)

    insertion_sort_visual(arr, labels, window)


# GUI 
window = tk.Tk()
window.title("Insertion Sort Visualizer")
window.geometry("700x300")
window.configure(bg="#1e1e1e")

title = tk.Label(window, text="ALGORITMA INSERTION SORT", font=("Arial", 18, "bold"),
                 bg="#1e1e1e", fg="white")
title.pack(pady=10)

frame_input = tk.Frame(window, bg="#1e1e1e")
frame_input.pack()

lbl = tk.Label(frame_input, text="Masukkan angka (pisah dengan spasi):",
               font=("Arial", 12), bg="#1e1e1e", fg="white")
lbl.pack(side="left")

entry = tk.Entry(frame_input, font=("Arial", 14), width=25)
entry.pack(side="left", padx=10)

btn = tk.Button(window, text="Mulai Sorting", font=("Arial", 12, "bold"),
                bg="#4CAF50", fg="white", command=start_sort)
btn.pack(pady=10)

frame_labels = tk.Frame(window, bg="#1e1e1e")
frame_labels.pack()

window.mainloop()
