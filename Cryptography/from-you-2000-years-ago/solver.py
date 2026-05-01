from Crypto.Cipher import AES
import binascii
import hashlib

# Data dari soal
ciphertext_hex = "81ca7d85cef7e78d0e34c709775e221ee2d96247df70be6dd52574df45d5291d0228e20ecdf0db87a06fecbca99255658054f51ffefb40c9d63953088171363ba1bd41e6e420f9b277a2fa60f17f727ed7e0"
tag_hex = "7ce83465082df66e24f2ec35b772736d"

ciphertext = binascii.unhexlify(ciphertext_hex)
tag = binascii.unhexlify(tag_hex)

# Nonce yang sudah dikonfirmasi
nonce = b"000000002000" 

# Daftar kemungkinan Key (menggunakan 'pplg')
possible_keys = [
    hashlib.sha256(b"pplg").digest(),         # SHA-256 (32 byte)
    hashlib.md5(b"pplg").digest(),            # MD5 (16 byte)
    b"pplg".ljust(16, b'\0'),                 # 16 byte null padding (belakang)
    b"pplg".rjust(16, b'\0'),                 # 16 byte null padding (depan)
    b"pplg".ljust(32, b'\0'),                 # 32 byte null padding
    (b"pplg" * 8)[:32],                       # Repeated 32 byte
]

def solve():
    print(f"Target Nonce: {nonce.decode()}")
    print("-" * 30)
    
    for i, k in enumerate(possible_keys):
        try:
            cipher = AES.new(k, AES.MODE_GCM, nonce=nonce)
            decrypted = cipher.decrypt_and_verify(ciphertext, tag)
            
            print(f"[+] BERHASIL PADA PERCOBAAN KE-{i+1}!")
            print(f"Key (Hex): {k.hex()}")
            print(f"Flag: {decrypted.decode()}")
            return
        except ValueError:
            # Ini biasanya terjadi kalau panjang key tidak sesuai (bukan 16, 24, 32)
            continue
        except Exception:
            # MAC check failed masuk ke sini
            continue
            
    print("[-] Masih gagal. Coba cek apakah ada string lain selain 'pplg' atau format kuncinya berbeda.")

solve()