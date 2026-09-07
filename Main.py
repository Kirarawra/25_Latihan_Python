import ganjil_genap
import bilangan_prima
import luas_persegi_panjang
from auth import login, register

def main_menu():
    while True:
        print("\n----- MENU -----")
        print("1. Ganjil / Genap")
        print("2. Bilangan Prima")
        print("3. Luas Persegi Panjang")
        print("4. Exit")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            angka = int(input("Masukkan angka: "))
            print(ganjil_genap.ganjil_genap(angka))
        elif pilihan == "2":
            angka = int(input("Masukkan angka: "))
            print(bilangan_prima.bilangan_prima(angka))
        elif pilihan == "3":
            panjang = float(input("Masukkan panjang: "))
            lebar = float(input("Masukkan lebar: "))
            hasil = luas_persegi_panjang.luas_persegi_panjang(panjang, lebar)
            print("Luas persegi panjang =", hasil)
        elif pilihan == "4":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan menu tidak valid.")

if __name__ == "__main__":
    while True:
        print("\n=== SISTEM MASUK ===")
        print("1. Login")
        print("2. Buat Akun Baru (Register)")
        print("3. Keluar")
        
        akses = input("Pilih menu akses: ")
        
        if akses == "1":
            if login():
                main_menu()
        elif akses == "2":
            register()
        elif akses == "3":
            break
        else:
            print("Pilihan tidak valid.")