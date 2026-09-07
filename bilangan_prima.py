def bilangan_prima(angka):
    if angka < 2:
        return "Bukan Bilangan Prima"
    
    for i in range(2, angka):
        if angka % i == 0:
            return "Bukan Bilangan Prima"
            
    return "Bilangan Prima"