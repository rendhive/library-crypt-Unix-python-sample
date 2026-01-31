import crypt

def hash_with_random_salt(password):
    salt = crypt.mksalt(crypt.METHOD_SHA256)
    return crypt.crypt(password, salt)

hashed_random_salt = hash_with_random_salt("another_secure_password")
print(f"Hashed dengan Salt Random: {hashed_random_salt}")
# Fungsi: Menghasilkan hash dengan salt yang dihasilkan secara acak.
# Kondisi: Ketika Anda ingin memastikan bahwa setiap password memiliki salt unik untuk lebih banyak keamanan.