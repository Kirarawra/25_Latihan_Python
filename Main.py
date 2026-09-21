import tkinter as tk
from tkinter import ttk, messagebox

import auth
import ganjil_genap
import bilangan_prima
import luas_persegi_panjang


# ==========================================================
# WARNA
# ==========================================================

BG = "#0f172a"
CARD = "#1e293b"
CARD2 = "#334155"
TEXT = "#f8fafc"
MUTED = "#94a3b8"
PRIMARY = "#6366f1"
PRIMARY_HOVER = "#4f46e5"
DANGER = "#ef4444"
SUCCESS = "#22c55e"


# ==========================================================
# APLIKASI
# ==========================================================

class App:

    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Aplikasi")
        self.root.geometry("900x600")
        self.root.minsize(800, 550)
        self.root.configure(bg=BG)

        self.current_user = None

        self.setup_style()
        self.show_login()


    # ======================================================
    # STYLE
    # ======================================================

    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "TEntry",
            fieldbackground="#334155",
            foreground=TEXT,
            borderwidth=0,
            padding=10
        )

        style.configure(
            "TButton",
            font=("Segoe UI", 11),
            padding=10
        )


    # ======================================================
    # CLEAR WINDOW
    # ======================================================

    def clear(self):

        for widget in self.root.winfo_children():
            widget.destroy()


    # ======================================================
    # LOGIN
    # ======================================================

    def show_login(self):

        self.clear()

        container = tk.Frame(
            self.root,
            bg=BG
        )

        container.pack(
            expand=True
        )

        # Judul
        tk.Label(
            container,
            text="SISTEM APLIKASI",
            font=("Segoe UI", 28, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(pady=(30, 5))

        tk.Label(
            container,
            text="Silakan login untuk melanjutkan",
            font=("Segoe UI", 11),
            fg=MUTED,
            bg=BG
        ).pack(pady=(0, 25))


        # Card login
        card = tk.Frame(
            container,
            bg=CARD,
            width=400,
            height=300
        )

        card.pack()
        card.pack_propagate(False)


        tk.Label(
            card,
            text="LOGIN",
            font=("Segoe UI", 20, "bold"),
            fg=TEXT,
            bg=CARD
        ).pack(pady=(25, 20))


        # Username
        tk.Label(
            card,
            text="Username",
            font=("Segoe UI", 10),
            fg=MUTED,
            bg=CARD
        ).pack(anchor="w", padx=40)

        username_entry = ttk.Entry(
            card,
            width=40
        )

        username_entry.pack(
            padx=40,
            pady=(5, 15)
        )


        # Password
        tk.Label(
            card,
            text="Password",
            font=("Segoe UI", 10),
            fg=MUTED,
            bg=CARD
        ).pack(anchor="w", padx=40)

        password_entry = ttk.Entry(
            card,
            width=40,
            show="*"
        )

        password_entry.pack(
            padx=40,
            pady=(5, 15)
        )


        # Login
        def proses_login():

            username = username_entry.get().strip()
            password = password_entry.get()

            if not username or not password:

                messagebox.showwarning(
                    "Peringatan",
                    "Username dan password harus diisi!"
                )

                return


            berhasil, hasil = auth.login(
                username,
                password
            )

            if berhasil:

                self.current_user = hasil

                self.show_dashboard()

            else:

                messagebox.showerror(
                    "Login Gagal",
                    hasil
                )


        tk.Button(
            card,
            text="LOGIN",
            font=("Segoe UI", 11, "bold"),
            fg="white",
            bg=PRIMARY,
            activebackground=PRIMARY_HOVER,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=proses_login
        ).pack(
            fill="x",
            padx=40,
            pady=(5, 10)
        )


        # Register
        tk.Button(
            card,
            text="Belum punya akun? Register",
            font=("Segoe UI", 9),
            fg=MUTED,
            bg=CARD,
            activebackground=CARD,
            activeforeground=TEXT,
            relief="flat",
            cursor="hand2",
            command=self.show_register
        ).pack()


        username_entry.focus()


    # ======================================================
    # REGISTER
    # ======================================================

    def show_register(self):

        self.clear()

        container = tk.Frame(
            self.root,
            bg=BG
        )

        container.pack(
            expand=True
        )


        tk.Label(
            container,
            text="BUAT AKUN",
            font=("Segoe UI", 28, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(pady=(20, 5))


        tk.Label(
            container,
            text="Daftarkan akun baru",
            font=("Segoe UI", 11),
            fg=MUTED,
            bg=BG
        ).pack(pady=(0, 20))


        card = tk.Frame(
            container,
            bg=CARD,
            width=400,
            height=350
        )

        card.pack()
        card.pack_propagate(False)


        tk.Label(
            card,
            text="REGISTER",
            font=("Segoe UI", 20, "bold"),
            fg=TEXT,
            bg=CARD
        ).pack(pady=(25, 20))


        # Username
        tk.Label(
            card,
            text="Username",
            fg=MUTED,
            bg=CARD
        ).pack(anchor="w", padx=40)

        username_entry = ttk.Entry(
            card,
            width=40
        )

        username_entry.pack(
            padx=40,
            pady=(5, 15)
        )


        # Password
        tk.Label(
            card,
            text="Password",
            fg=MUTED,
            bg=CARD
        ).pack(anchor="w", padx=40)

        password_entry = ttk.Entry(
            card,
            width=40,
            show="*"
        )

        password_entry.pack(
            padx=40,
            pady=(5, 15)
        )


        # Konfirmasi password
        tk.Label(
            card,
            text="Konfirmasi Password",
            fg=MUTED,
            bg=CARD
        ).pack(anchor="w", padx=40)

        confirm_entry = ttk.Entry(
            card,
            width=40,
            show="*"
        )

        confirm_entry.pack(
            padx=40,
            pady=(5, 15)
        )


        def proses_register():

            username = username_entry.get().strip()
            password = password_entry.get()
            confirm = confirm_entry.get()


            if not username or not password or not confirm:

                messagebox.showwarning(
                    "Peringatan",
                    "Semua data harus diisi!"
                )

                return


            if password != confirm:

                messagebox.showerror(
                    "Error",
                    "Password dan konfirmasi password tidak sama!"
                )

                return


            berhasil, pesan = auth.register(
                username,
                password
            )


            if berhasil:

                messagebox.showinfo(
                    "Berhasil",
                    pesan
                )

                self.show_login()

            else:

                messagebox.showerror(
                    "Registrasi Gagal",
                    pesan
                )


        tk.Button(
            card,
            text="DAFTAR",
            font=("Segoe UI", 11, "bold"),
            fg="white",
            bg=PRIMARY,
            activebackground=PRIMARY_HOVER,
            relief="flat",
            cursor="hand2",
            command=proses_register
        ).pack(
            fill="x",
            padx=40,
            pady=(5, 10)
        )


        tk.Button(
            card,
            text="← Kembali ke Login",
            fg=MUTED,
            bg=CARD,
            activebackground=CARD,
            activeforeground=TEXT,
            relief="flat",
            cursor="hand2",
            command=self.show_login
        ).pack()


    # ======================================================
    # DASHBOARD
    # ======================================================

    def show_dashboard(self):

        self.clear()

        # Header
        header = tk.Frame(
            self.root,
            bg=CARD,
            height=75
        )

        header.pack(
            fill="x"
        )

        header.pack_propagate(False)


        tk.Label(
            header,
            text="SISTEM MATEMATIKA",
            font=("Segoe UI", 18, "bold"),
            fg=TEXT,
            bg=CARD
        ).pack(
            side="left",
            padx=30
        )


        user_frame = tk.Frame(
            header,
            bg=CARD
        )

        user_frame.pack(
            side="right",
            padx=25
        )


        tk.Label(
            user_frame,
            text=f"👤 {self.current_user}",
            font=("Segoe UI", 10),
            fg=TEXT,
            bg=CARD
        ).pack(
            side="left",
            padx=10
        )


        tk.Button(
            user_frame,
            text="Logout",
            font=("Segoe UI", 9),
            fg="white",
            bg=DANGER,
            activebackground="#dc2626",
            relief="flat",
            cursor="hand2",
            command=self.logout
        ).pack(
            side="left"
        )


        # Isi
        content = tk.Frame(
            self.root,
            bg=BG
        )

        content.pack(
            fill="both",
            expand=True,
            padx=50,
            pady=40
        )


        tk.Label(
            content,
            text=f"Selamat datang, {self.current_user}!",
            font=("Segoe UI", 25, "bold"),
            fg=TEXT,
            bg=BG
        ).pack()


        tk.Label(
            content,
            text="Pilih program yang ingin kamu gunakan",
            font=("Segoe UI", 11),
            fg=MUTED,
            bg=BG
        ).pack(
            pady=(5, 35)
        )


        # Cards
        cards = tk.Frame(
            content,
            bg=BG
        )

        cards.pack()


        self.create_card(
            cards,
            "1",
            "Ganjil / Genap",
            "Menentukan apakah sebuah angka ganjil atau genap",
            self.show_ganjil_genap,
            0,
            0
        )


        self.create_card(
            cards,
            "2",
            "Bilangan Prima",
            "Memeriksa apakah sebuah angka merupakan bilangan prima",
            self.show_bilangan_prima,
            0,
            1
        )


        self.create_card(
            cards,
            "3",
            "Luas Persegi Panjang",
            "Menghitung luas berdasarkan panjang dan lebar",
            self.show_luas,
            1,
            0
        )


        self.create_card(
            cards,
            "4",
            "Tentang",
            "Informasi mengenai aplikasi",
            self.show_about,
            1,
            1
        )


    # ======================================================
    # CARD
    # ======================================================

    def create_card(
        self,
        parent,
        nomor,
        title,
        description,
        command,
        row,
        column
    ):

        card = tk.Frame(
            parent,
            bg=CARD,
            width=330,
            height=150
        )

        card.grid(
            row=row,
            column=column,
            padx=12,
            pady=12
        )

        card.grid_propagate(False)


        tk.Label(
            card,
            text=nomor,
            font=("Segoe UI", 20, "bold"),
            fg=PRIMARY,
            bg=CARD
        ).pack(
            anchor="w",
            padx=20,
            pady=(15, 0)
        )


        tk.Label(
            card,
            text=title,
            font=("Segoe UI", 14, "bold"),
            fg=TEXT,
            bg=CARD
        ).pack(
            anchor="w",
            padx=20
        )


        tk.Label(
            card,
            text=description,
            font=("Segoe UI", 9),
            fg=MUTED,
            bg=CARD,
            wraplength=280,
            justify="left"
        ).pack(
            anchor="w",
            padx=20,
            pady=(5, 10)
        )


        tk.Button(
            card,
            text="Buka →",
            font=("Segoe UI", 9, "bold"),
            fg=TEXT,
            bg=CARD2,
            activebackground=PRIMARY,
            activeforeground="white",
            relief="flat",
            cursor="hand2",
            command=command
        ).place(
            x=240,
            y=108,
            width=70,
            height=28
        )


    # ======================================================
    # GANJIL GENAP
    # ======================================================

    def show_ganjil_genap(self):

        window = tk.Toplevel(self.root)

        window.title("Ganjil / Genap")
        window.geometry("450x350")
        window.configure(bg=BG)
        window.resizable(False, False)


        tk.Label(
            window,
            text="GANJIL / GENAP",
            font=("Segoe UI", 22, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(pady=(35, 10))


        tk.Label(
            window,
            text="Masukkan sebuah angka",
            fg=MUTED,
            bg=BG
        ).pack()


        entry = ttk.Entry(
            window,
            font=("Segoe UI", 14),
            justify="center"
        )

        entry.pack(
            padx=80,
            pady=20,
            fill="x"
        )


        hasil = tk.Label(
            window,
            text="",
            font=("Segoe UI", 16, "bold"),
            fg=SUCCESS,
            bg=BG
        )

        hasil.pack(
            pady=15
        )


        def proses():

            try:

                angka = int(entry.get())

                hasil.config(
                    text=ganjil_genap.ganjil_genap(angka)
                )

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Masukkan angka yang valid!",
                    parent=window
                )


        tk.Button(
            window,
            text="CEK",
            font=("Segoe UI", 11, "bold"),
            fg="white",
            bg=PRIMARY,
            relief="flat",
            command=proses
        ).pack(
            ipadx=50,
            ipady=5
        )


    # ======================================================
    # BILANGAN PRIMA
    # ======================================================

    def show_bilangan_prima(self):

        window = tk.Toplevel(self.root)

        window.title("Bilangan Prima")
        window.geometry("450x350")
        window.configure(bg=BG)
        window.resizable(False, False)


        tk.Label(
            window,
            text="BILANGAN PRIMA",
            font=("Segoe UI", 22, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(pady=(35, 10))


        tk.Label(
            window,
            text="Masukkan sebuah angka",
            fg=MUTED,
            bg=BG
        ).pack()


        entry = ttk.Entry(
            window,
            font=("Segoe UI", 14),
            justify="center"
        )

        entry.pack(
            padx=80,
            pady=20,
            fill="x"
        )


        hasil = tk.Label(
            window,
            text="",
            font=("Segoe UI", 16, "bold"),
            fg=SUCCESS,
            bg=BG
        )

        hasil.pack(
            pady=15
        )


        def proses():

            try:

                angka = int(entry.get())

                hasil.config(
                    text=bilangan_prima.bilangan_prima(angka)
                )

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Masukkan angka yang valid!",
                    parent=window
                )


        tk.Button(
            window,
            text="CEK",
            font=("Segoe UI", 11, "bold"),
            fg="white",
            bg=PRIMARY,
            relief="flat",
            command=proses
        ).pack(
            ipadx=50,
            ipady=5
        )


    # ======================================================
    # LUAS PERSEGI PANJANG
    # ======================================================

    def show_luas(self):

        window = tk.Toplevel(self.root)

        window.title("Luas Persegi Panjang")
        window.geometry("450x450")
        window.configure(bg=BG)
        window.resizable(False, False)


        tk.Label(
            window,
            text="LUAS PERSEGI PANJANG",
            font=("Segoe UI", 21, "bold"),
            fg=TEXT,
            bg=BG
        ).pack(pady=(35, 25))


        # Panjang
        tk.Label(
            window,
            text="Panjang",
            fg=MUTED,
            bg=BG
        ).pack()

        panjang = ttk.Entry(
            window,
            font=("Segoe UI", 13),
            justify="center"
        )

        panjang.pack(
            padx=80,
            pady=(5, 20),
            fill="x"
        )


        # Lebar
        tk.Label(
            window,
            text="Lebar",
            fg=MUTED,
            bg=BG
        ).pack()

        lebar = ttk.Entry(
            window,
            font=("Segoe UI", 13),
            justify="center"
        )

        lebar.pack(
            padx=80,
            pady=(5, 20),
            fill="x"
        )


        hasil = tk.Label(
            window,
            text="",
            font=("Segoe UI", 16, "bold"),
            fg=SUCCESS,
            bg=BG
        )

        hasil.pack(pady=20)


        def proses():

            try:

                p = float(panjang.get())
                l = float(lebar.get())

                luas = luas_persegi_panjang.luas_persegi_panjang(
                    p,
                    l
                )

                hasil.config(
                    text=f"Luas = {luas}"
                )

            except ValueError:

                messagebox.showerror(
                    "Error",
                    "Panjang dan lebar harus berupa angka!",
                    parent=window
                )


        tk.Button(
            window,
            text="HITUNG",
            font=("Segoe UI", 11, "bold"),
            fg="white",
            bg=PRIMARY,
            relief="flat",
            command=proses
        ).pack(
            ipadx=40,
            ipady=5
        )


    # ======================================================
    # ABOUT
    # ======================================================

    def show_about(self):

        messagebox.showinfo(
            "Tentang Aplikasi",
            "SISTEM MATEMATIKA\n\n"
            "Aplikasi sederhana menggunakan Python + Tkinter + MySQL.\n\n"
            "Fitur:\n"
            "• Login & Register\n"
            "• Ganjil / Genap\n"
            "• Bilangan Prima\n"
            "• Luas Persegi Panjang",
            parent=self.root
        )


    # ======================================================
    # LOGOUT
    # ======================================================

    def logout(self):

        konfirmasi = messagebox.askyesno(
            "Logout",
            "Apakah kamu yakin ingin logout?",
            parent=self.root
        )

        if konfirmasi:

            self.current_user = None
            self.show_login()


# ==========================================================
# START PROGRAM
# ==========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = App(root)

    root.mainloop()
