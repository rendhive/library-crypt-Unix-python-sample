import crypt

def pretty_print_hash(password):
    hashed = hash_password(password)
    print(f"Password: {password}\nHashed: {hashed}\n")

pretty_print_hash("user_password")
# Fungsi: Mencetak password dan hash-nya dengan format yang rapi.
# Kondisi: Ketika Anda ingin menunjukkan hasil hashing di terminal dengan bersih.