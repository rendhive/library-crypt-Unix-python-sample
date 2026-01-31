import secrets

def generate_user_id():
    return secrets.token_hex(8)

user_id = generate_user_id()
print(f"Generated User ID: {user_id}")
# Fungsi: Menghasilkan user ID yang unik dan aman.
# Kondisi: Ketika Anda perlu memberikan identifikasi unik untuk setiap pengguna.