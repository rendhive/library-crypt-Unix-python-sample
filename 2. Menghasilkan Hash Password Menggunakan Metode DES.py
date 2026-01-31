import crypt

def hash_password(password):
    return crypt.crypt(password, crypt.mksalt(crypt.METHOD_DES))

hashed = hash_password("my_password")
print(f"Hashed Password (DES): {hashed}")
# Fungsi: Menghasilkan hash untuk password menggunakan algoritma DES.
# Kondisi: Digunakan saat Anda ingin menyimpan password secara aman.