import secrets
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(characters) for _ in range(length))

random_password = generate_random_password()
print(f"Password Acak: {random_password}")
# Fungsi: Menghasilkan password acak dengan panjang tertentu.
# Kondisi: Ketika Anda perlu menghasilkan password untuk pengguna baru.