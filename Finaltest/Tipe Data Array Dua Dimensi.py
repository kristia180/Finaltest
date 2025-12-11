import tkinter as tk
from tkinter import messagebox, simpledialog

# Array dua dimensi

class ArrayApp:
    def __init__(self, master):
        self.master = master
        master.title("Array 1 Dimensi - Tkinter Berwarna")
        master.geometry("450x420")
        master.config(bg="#1E1F26")  # background utama gelap elegan

        # DATA ARRAY 
        self.arr = []

        # FRAME INPUT 
        top_frame = tk.Frame(master, bg="#1E1F26")
        top_frame.pack(pady=10, fill="x")

        tk.Label(top_frame, text="Masukkan nilai:",
                 bg="#1E1F26", fg="white",
                 font=("Arial", 11, "bold")).grid(row=0, column=0, padx=6)

        self.entry = tk.Entry(top_frame, font=("Arial", 11))
        self.entry.grid(row=0, column=1, padx=6, sticky="we")
        top_frame.columnconfigure(1, weight=1)

        btn_add = tk.Button(top_frame, text="Tambah",
                            command=self.add_item,
                            bg="#4CAF50", fg="white", width=10,
                            activebackground="#45A049")
        btn_add.grid(row=0, column=2, padx=6)

        # TOMBOL INSERT INDEX 
        btn_insert = tk.Button(
            top_frame,
            text="Insert di index...",
            command=self.insert_at_index,
            bg="#2196F3", fg="white",
            activebackground="#1E88E5"
        )
        btn_insert.grid(row=1, column=0, columnspan=3, pady=8)

        # LISTBOX 
        list_frame = tk.Frame(master, bg="#1E1F26")
        list_frame.pack(fill="both", expand=True, padx=10)

        self.listbox = tk.Listbox(
            list_frame,
            height=12,
            bg="#2E3038",
            fg="white",
            font=("Consolas", 11),
            selectbackground="#00E5FF"
        )
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(side="right", fill="y")
        self.listbox.config(yscrollcommand=scrollbar.set)

        # FRAME TOMBOL AKSI 
        action_frame = tk.Frame(master, bg="#1E1F26")
        action_frame.pack(pady=10)

        def make_btn(text, cmd, color):
            return tk.Button(
                action_frame, text=text,
                command=cmd, width=12,
                bg=color, fg="white",
                activebackground=color
            )

        make_btn("Hapus Terpilih", self.remove_selected, "#FC8178").grid(row=0, column=0, padx=5, pady=4)
        make_btn("Urutkan ASC", self.sort_asc, "#D886E7").grid(row=0, column=1, padx=5, pady=4)
        make_btn("Urutkan DESC", self.sort_desc, "#C072F0").grid(row=0, column=2, padx=5, pady=4)
        make_btn("Cari", self.search_item, "#60E892").grid(row=0, column=3, padx=5, pady=4)

        make_btn("Tampilkan Semua", self.show_all, "#607D8B").grid(row=1, column=0, columnspan=2, pady=6)
        make_btn("Bersihkan Array", self.clear_array, "#F5724B").grid(row=1, column=2, columnspan=2, pady=6)

        # STATUS BAR 
        self.status_var = tk.StringVar(value="Array kosong")
        tk.Label(master, textvariable=self.status_var,
                 bg="#1E1F26", fg="#00E5FF",
                 font=("Arial", 10, "bold"),
                 anchor="w").pack(fill="x", padx=10, pady=(0,10))

    # FUNGSI DASAR ARRAY 
    def add_item(self):
        val = self.entry.get().strip()
        if not val:
            messagebox.showwarning("Peringatan", "Masukkan nilai terlebih dahulu.")
            return
        self.arr.append(val)
        self.entry.delete(0, tk.END)
        self.refresh_list()
        self.update_status()

    def insert_at_index(self):
        if not self.entry.get().strip():
            messagebox.showwarning("Peringatan", "Isi nilai dulu.")
            return

        idx = simpledialog.askinteger("Index", "Masukkan index (0..n):")
        if idx is None:
            return
        if idx < 0 or idx > len(self.arr):
            idx = len(self.arr)

        self.arr.insert(idx, self.entry.get().strip())
        self.entry.delete(0, tk.END)
        self.refresh_list()
        self.update_status()

    def remove_selected(self):
        sel = self.listbox.curselection()
        if not sel:
            messagebox.showinfo("Info", "Pilih item dahulu.")
            return
        self.arr.pop(sel[0])
        self.refresh_list()
        self.update_status()

    def sort_asc(self):
        self.arr.sort()
        self.refresh_list()
        self.update_status("Diurutkan ASC")

    def sort_desc(self):
        self.arr.sort(reverse=True)
        self.refresh_list()
        self.update_status("Diurutkan DESC")

    def search_item(self):
        q = simpledialog.askstring("Cari", "Masukkan nilai:")
        if q is None:
            return
        try:
            idx = self.arr.index(q)
            self.listbox.selection_clear(0, tk.END)
            self.listbox.selection_set(idx)
            self.listbox.see(idx)
            messagebox.showinfo("Ditemukan", f"'{q}' ditemukan di index {idx}")
        except ValueError:
            messagebox.showinfo("Tidak Ada", f"'{q}' tidak ditemukan.")

    def show_all(self):
        content = ", ".join(self.arr)
        messagebox.showinfo("Isi Array", content if content else "(Kosong)")

    def clear_array(self):
        if messagebox.askyesno("Hapus Semua", "Kosongkan array?"):
            self.arr.clear()
            self.refresh_list()
            self.update_status("Array kosong")

    def refresh_list(self):
        self.listbox.delete(0, tk.END)
        for i, v in enumerate(self.arr):
            self.listbox.insert(tk.END, f"[{i}]  {v}")

    def update_status(self, info=""):
        status = f"Jumlah elemen: {len(self.arr)}"
        if info:
            status += f" — {info}"
        self.status_var.set(status)

# RUN TKINTER 
if __name__ == "__main__":
    root = tk.Tk()
    app = ArrayApp(root)
    root.mainloop()
