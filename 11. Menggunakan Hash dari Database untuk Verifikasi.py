import crypt

def verify_stored_password(database, username, password):
    if username in database:
        return verify_password(password, database[username])
    return False

db = {"user1": hash_password("my_secure_password")}
is_valid = verify_stored_password(db, "user1", "my_secure_password")
print(f"Password valid for user1: {is_valid}")
# Fungsi: Memverifikasi password pengguna terhadap yang disimpan di 'database'.
# Kondisi: Ketika pengguna mencoba login ke aplikasi.