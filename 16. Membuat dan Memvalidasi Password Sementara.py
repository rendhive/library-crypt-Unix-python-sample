import crypt
import secrets

def create_temp_password():
    temp_password = secrets.token_urlsafe(8)
    return temp_password, hash_password(temp_password)

temp_pw, temp_hashed = create_temp_password()
print(f"Temporary Password: {temp_pw}\nHashed: {temp_hashed}")
# Fungsi: Membuat password sementara dan hash-nya.
# Kondisi: Untuk memberikan akses sementara kepada pengguna tanpa mengubah password utama.