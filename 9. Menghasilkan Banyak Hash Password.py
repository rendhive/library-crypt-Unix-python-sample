import crypt

def hash_multiple_passwords(passwords):
    return {password: hash_password(password) for password in passwords}

passwords = ["password1", "password2", "password3"]
hashed_passwords = hash_multiple_passwords(passwords)
for pwd, h in hashed_passwords.items():
    print(f"Password: {pwd} - Hashed: {h}")
# Fungsi: Menghasilkan hash untuk beberapa password sekaligus.
# Kondisi: Ketika Anda memiliki banyak pengguna dan password untuk di-hash.