import crypt

def hash_password_sha512(password):
    return crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

hashed_sha512 = hash_password_sha512("my_password")
print(f"Hashed Password (SHA-512): {hashed_sha512}")
# Fungsi: Menghasilkan hash untuk password menggunakan algoritma SHA-512.
# Kondisi: Ketika Anda ingin keamanan maksimal untuk menyimpan password