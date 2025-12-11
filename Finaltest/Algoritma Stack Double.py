import tkinter as tk
from tkinter import messagebox

#   DOUBLE STACK IMPLEMENTATION

MAX = 10
data = [None] * MAX
top1 = -2          # Stack 1 mulai dari kiri
top2 = MAX         # Stack 2 mulai dari kanan


def push_stack1():
    global top1, top2
    item = entry_input.get()

    if item == "":
        messagebox.showwarning("Peringatan", "Data tidak boleh kosong!")
        return

    if top1 + 1 == top2:
        messagebox.showerror("Penuh", "Memori Double Stack penuh!")
        return

    top1 += 1
    data[top1] = item
    entry_input.delete(0, tk.END)
    update_display()


def push_stack2():
    global top1, top2
    item = entry_input.get()

    if item == "":
        messagebox.showwarning("Peringatan", "Data tidak boleh kosong!")
        return

    if top2 - 1 == top1:
        messagebox.showerror("Penuh", "Memori Double Stack penuh!")
        return

    top2 -= 1
    data[top2] = item
    entry_input.delete(0, tk.END)
    update_display()


def pop_stack1():
    global top1
    if top1 == -1:
        messagebox.showinfo("Kosong", "Stack 1 kosong!")
        return

    removed = data[top1]
    data[top1] = None
    top1 -= 1
    messagebox.showinfo("POP STACK 1", f"Data keluar: {removed}")
    update_display()


def pop_stack2():
    global top2
    if top2 == MAX:
        messagebox.showinfo("Kosong", "Stack 2 kosong!")
        return

    removed = data[top2]
    data[top2] = None
    top2 += 1
    messagebox.showinfo("POP STACK 2", f"Data keluar: {removed}")
    update_display()


def clear_all():
    global data, top1, top2
    data = [None] * MAX
    top1 = -2
    top2 = MAX
    update_display()


def update_display():
    text_display.config(state=tk.NORMAL)
    text_display.delete("1.0", tk.END)

    text_display.insert(tk.END, " DOUBLE STACK VISUALISASI \n\n", "judul")

    text_display.insert(tk.END, "Stack 1 (kiri → kanan):\n", "subjudul")
    if top1 == -2:
        text_display.insert(tk.END, "  [KOSONG]\n\n", "kosong")
    else:
        for i in range(0, top1 + 1):
            text_display.insert(tk.END, f"  [ {data[i]} ]\n", "stack1")

    text_display.insert(tk.END, "\nStack 2 (kanan → kiri):\n", "subjudul")
    if top2 == MAX:
        text_display.insert(tk.END, "  [KOSONG]\n\n", "kosong")
    else:
        for i in range(MAX - 2, top2 - 2, -2):
            text_display.insert(tk.END, f"  [ {data[i]} ]\n", "stack2")

    text_display.config(state=tk.DISABLED)


#               TKINTER GUI

root = tk.Tk()
root.title("Double Stack - Python Tkinter")
root.geometry("520x620")
root.config(bg="#1e1e2e")

# Judul
label_title = tk.Label(root, text="ALGORITMA DOUBLE STACK",
                       font=("Arial", 20, "bold"), fg="#ffffff", bg="#1e1e2e")
label_title.pack(pady=15)

# Input
frame_input = tk.Frame(root, bg="#1e1e2e")
frame_input.pack()

tk.Label(frame_input, text="Masukkan Data:",
         font=("Arial", 12), fg="white", bg="#1e1e2e").grid(row=0, column=0, padx=5)

entry_input = tk.Entry(frame_input, font=("Arial", 12), width=20)
entry_input.grid(row=0, column=1, padx=5)

# Tombol-tombol
frame_btn = tk.Frame(root, bg="#1e1e2e")
frame_btn.pack(pady=10)

btn_push1 = tk.Button(frame_btn, text="PUSH S1", width=10,
                      bg="#74f55a", fg="white", font=("Arial", 12, "bold"),
                      command=push_stack1)
btn_push1.grid(row=0, column=0, padx=5)

btn_push2 = tk.Button(frame_btn, text="PUSH S2", width=10,
                      bg="#8df555", fg="white", font=("Arial", 12, "bold"),
                      command=push_stack2)
btn_push2.grid(row=0, column=1, padx=5)

btn_pop1 = tk.Button(frame_btn, text="POP S1", width=10,
                     bg="#78e9fd", fg="white", font=("Arial", 12, "bold"),
                     command=pop_stack1)
btn_pop1.grid(row=1, column=0, padx=5, pady=5)

btn_pop2 = tk.Button(frame_btn, text="POP S2", width=10,
                     bg="#6ad9f8", fg="white", font=("Arial", 12, "bold"),
                     command=pop_stack2)
btn_pop2.grid(row=1, column=1, padx=5, pady=5)

btn_clear = tk.Button(frame_btn, text="CLEAR ALL", width=22,
                      bg="#33f44d", fg="white", font=("Arial", 12, "bold"),
                      command=clear_all)
btn_clear.grid(row=2, column=0, columnspan=2, pady=10)

# Display
text_display = tk.Text(root, height=20, width=55,
                       font=("Courier", 12), bg="#141415", fg="white")
text_display.pack(pady=10)

# Warna teks
text_display.tag_config("judul", foreground="#938af6", font=("Courier", 14, "bold"))
text_display.tag_config("subjudul", foreground="#a9ff67", font=("Courier", 12, "bold"))
text_display.tag_config("stack1", foreground="#66ebf7")
text_display.tag_config("stack2", foreground="#7ae0ff")
text_display.tag_config("kosong", foreground="#faf2f2", font=("Courier", 11, "italic"))

update_display()
root.mainloop()
