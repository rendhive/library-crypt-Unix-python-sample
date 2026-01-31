import crypt

def hash_password_with_method(password, method):
    if method not in [crypt.METHOD_DES, crypt.METHOD_MD5, crypt.METHOD_SHA256, crypt.METHOD_SHA512]:
        raise ValueError("Unsupported hashing method!")
    return crypt.crypt(password, crypt.mksalt(method))

hashed = hash_password_with_method("my_password", crypt.METHOD_SHA512)
print(f"Hashed Password menggunakan SHA-512: {hashed}")
# Fungsi: Menghasilkan hash untuk password dengan metode yang ditentukan.
# Kondisi: Ketika Anda ingin memilih algoritma hashing berdasarkan kebutuhan.