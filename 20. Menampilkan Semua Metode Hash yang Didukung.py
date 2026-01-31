import crypt

def list_supported_methods():
    methods = {
        crypt.METHOD_DES: "DES",
        crypt.METHOD_MD5: "MD5",
        crypt.METHOD_SHA256: "SHA-256",
        crypt.METHOD_SHA512: "SHA-512",
    }
    return methods

methods = list_supported_methods()
print("Supported Hashing Methods:")
for key, value in methods.items():
    print(f"{key}: {value}")
# Fungsi: Menampilkan semua metode hashing yang didukung oleh modul crypt.
# Kondisi: Ketika Anda ingin tahu metode hashing yang bisa digunakan untuk password.