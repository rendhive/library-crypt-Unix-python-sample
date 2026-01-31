import crypt

def update_password(old_password, new_password, stored_hash):
    if verify_password(old_password, stored_hash):
        return hash_password(new_password)
    return None

old_hash = hash_password("old_password")
new_hashed = update_password("old_password", "new_password", old_hash)
print(f"Updated Hashed Password: {new_hashed}")
# Fungsi: Memperbarui password dan hash-nya jika password lama benar.
# Kondisi: Ketika pengguna melakukan permintaan untuk mengubah password mereka.