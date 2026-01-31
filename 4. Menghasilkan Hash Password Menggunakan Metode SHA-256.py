import crypt

def hash_password_sha256(password):
    return crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA256))

hashed_sha256 = hash_password_sha256("my_password")
print(f"Hashed Password (SHA-256): {hashed_sha256}")
# Fungsi: Menghasilkan hash untuk password menggunakan algoritma SHA-256.
# Kondisi: Saat Anda ingin menggunakan kekuatan hashing yang lebih tinggi.