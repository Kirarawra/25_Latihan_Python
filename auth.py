import mysql.connector

def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="312245", 
        database="db_aplikasi"
    )

def register():
    print("\n=== REGISTRASI AKUN BARU ===")
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    
    db = get_db()
    cursor = db.cursor()
    try:
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, password))
        db.commit()
        print("Registrasi berhasil! Silakan login.")
    except mysql.connector.Error as err:
        print(f"Gagal registrasi: {err}")
    finally:
        db.close()

def login():
    print("\n=== LOGIN APLIKASI ===")
    username = input("Username: ")
    password = input("Password: ")
    
    db = get_db()
    cursor = db.cursor()
    
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    user = cursor.fetchone()
    db.close()
    
    if user:
        print(f"\nSelamat datang, {username}!")
        return True
    else:
        print("\nUsername atau password salah!")
        return False