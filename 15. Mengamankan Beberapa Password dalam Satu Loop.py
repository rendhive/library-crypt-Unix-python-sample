import crypt

passwords = ["alpha", "beta", "gamma"]
hashed_pw_list = []

for pw in passwords:
    hashed_pw_list.append(hash_password(pw))

print("Hashed Passwords:")
for h in hashed_pw_list:
    print(h)
# Fungsi: Menghasilkan dan mencetak hash dari beberapa password.
# Kondisi: Ketika Anda memiliki banyak password yang perlu di-hash dan disimpan.