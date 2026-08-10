while True:
    inputan = input("Masukkan angka (ketik 'q' untuk keluar): ")
    
    if inputan == 'q':
        break
        
    angka = int(inputan)
    status = "Genap" if angka % 2 == 0 else "Ganjil"
    print(angka, "adalah", status, "\n")