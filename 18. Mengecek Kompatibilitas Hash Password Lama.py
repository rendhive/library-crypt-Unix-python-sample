import crypt

def check_compatibility(old_hashed, password):
    return old_hashed == crypt.crypt(password, old_hashed)

old_hashed = hash_password("old_password")
is_old_compatible = check_compatibility(old_hashed, "old_password")
print(f"Kompatibilitas Hash Password Lama: {is_old_compatible}")
# Fungsi: Mengecek apakah password yang lama sesuai dengan hash yang lama.
# Kondisi: Ketika Anda melakukan migrasi dari sistem enkripsi yang lebih lama.