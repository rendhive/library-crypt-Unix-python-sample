import crypt

def simulate_database():
    return {}

def store_hashed_password(database, username, password):
    database[username] = hash_password(password)

db = simulate_database()
store_hashed_password(db, "user1", "my_secure_password")
print(f"Stored Password Hash: {db['user1']}")
# Fungsi: Menyimpan hash password dalam struktur data (simulasi database).
# Kondisi: Ketika Anda perlu menyimpan password dengan aman dalam aplikasi.