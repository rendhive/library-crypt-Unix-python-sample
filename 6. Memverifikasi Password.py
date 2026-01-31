import crypt

def verify_password(password, hashed):
    return crypt.crypt(password, hashed) == hashed

hashed = hash_password("my_password")
is_valid = verify_password("my_password", hashed)
print(f"Password valid: {is_valid}")
# Fungsi: Memverifikasi bahwa password yang diberikan cocok dengan hash yang disimpan.
# Kondisi: Ketika Anda perlu melakukan autentikasi pengguna.