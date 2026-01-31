import crypt

def hash_password_md5(password):
    return crypt.crypt(password, crypt.mksalt(crypt.METHOD_MD5))

hashed_md5 = hash_password_md5("my_password")
print(f"Hashed Password (MD5): {hashed_md5}")
# Fungsi: Menghasilkan hash untuk password menggunakan algoritma MD5.
# Kondisi: Ketika Anda memerlukan cara hashing yang lebih aman daripada DES.