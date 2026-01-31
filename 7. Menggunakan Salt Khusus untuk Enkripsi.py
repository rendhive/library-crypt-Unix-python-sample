import crypt

def custom_salt_hash_password(password, salt):
    return crypt.crypt(password, salt)

salt = "$6$rounds=5000$saltvalue$"
hashed_custom = custom_salt_hash_password("my_custom_password", salt)
print(f"Hashed Password dengan Salt Khusus: {hashed_custom}")
# Fungsi: Menghasilkan hash password menggunakan salt khusus yang ditentukan pengguna.
# Kondisi: Ketika Anda ingin menggunakan salt yang tidak random.