import hashlib

secret_lang = "Zig" # Bahasa target
salt_value = 337    # Angka antara 0-511
encoding = "utf-16-le"

# 1. Ubah ke lowercase
lang_lower = secret_lang.lower() 
# 2. Ubah salt ke string hex (misal: 337 -> '151')
salt_hex = format(salt_value, 'x') 
# 3. Gabungkan: 'zig151' lalu encode ke UTF-16LE
payload = (lang_lower + salt_hex).encode(encoding)
# 4. Generate SHA-256
target_hash = hashlib.sha256(payload).hexdigest()

print(f"Target Hash buat ditaruh di soal: {target_hash}")