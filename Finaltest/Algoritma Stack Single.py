import tkinter as tk
from tkinter import messagebox

# -----------------------------
#  STACK IMPLEMENTATION
# -----------------------------
stack = []

def push_item():
    item = entry_item.get()
    if item == "":
        messagebox.showwarning("Peringatan", "Input tidak boleh kosong!")
        return
    stack.append(item)
    entry_item.delete(0, tk.END)
    update_display()

def pop_item():
    if len(stack) == 0:
        messagebox.showwarning("Kosong", "Stack sedang kosong!")
        return
    popped = stack.pop()
    messagebox.showinfo("POP", f"Data yang keluar: {popped}")
    update_display()

def clear_stack():
    stack.clear()
    update_display()

def update_display():
    text_display.config(state=tk.NORMAL)
    text_display.delete("1.0", tk.END)

    if len(stack) == 0:
        text_display.insert(tk.END, "Stack kosong...\n", "info")
    else:
        text_display.insert(tk.END, "Isi Stack (TOP → BOTTOM):\n", "judul")
        for i in reversed(stack):
            text_display.insert(tk.END, f"[ {i} ]\n", "stack_item")

    text_display.config(state=tk.DISABLED)

# --------------------------------
#  TKINTER GUI
# --------------------------------
root = tk.Tk()
root.title("Program Stack (Single) - Python Tkinter")
root.geometry("450x500")
root.config(bg="#1e1e2e")

# Judul
label_title = tk.Label(root, text="ALGORITMA STACK (SINGLE)", 
                       font=("Arial", 18, "bold"), fg="#ffffff", bg="#1e1e2e")
label_title.pack(pady=15)

# Input frame
input_frame = tk.Frame(root, bg="#1e1e2e")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Masukkan Data:", font=("Arial", 12),
         fg="white", bg="#1e1e2e").grid(row=0, column=0, padx=5)

entry_item = tk.Entry(input_frame, font=("Arial", 12), width=20)
entry_item.grid(row=0, column=1, padx=5)

# Tombol-tombol
button_frame = tk.Frame(root, bg="#1e1e2e")
button_frame.pack(pady=10)

btn_push = tk.Button(button_frame, text="PUSH", width=10, font=("Arial", 12, "bold"),
                     bg="#f44b2d", fg="white", command=push_item)
btn_push.grid(row=0, column=0, padx=5)

btn_pop = tk.Button(button_frame, text="POP", width=10, font=("Arial", 12, "bold"),
                    bg="#ecfc3f", fg="white", command=pop_item)
btn_pop.grid(row=0, column=1, padx=5)

btn_clear = tk.Button(button_frame, text="CLEAR", width=10, font=("Arial", 12, "bold"),
                      bg="#6efc52", fg="white", command=clear_stack)
btn_clear.grid(row=0, column=2, padx=5)

# Display area
text_display = tk.Text(root, height=15, width=40, font=("Courier", 12), bg="#2b2b3b", fg="white")
text_display.pack(pady=20)
text_display.tag_config("judul", foreground="#00eaff", font=("Courier", 13, "bold"))
text_display.tag_config("stack_item", foreground="#9dff6c", font=("Courier", 12, "bold"))
text_display.tag_config("info", foreground="#ffaaff", font=("Courier", 12, "italic"))
text_display.config(state=tk.DISABLED)

update_display()

root.mainloop()
