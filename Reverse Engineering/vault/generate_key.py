import string

# Step 1: Generate enc[] yang benar
flag = "PPLG{wh4t?_a_cust0m_vm?}"
enc = [ord(c) ^ 0x33 for c in flag]
print("enc[] yang benar:")
print("{" + ", ".join(f"0x{b:02X}" for b in enc) + "};")
print(f"Panjang enc: {len(enc)}")

# Verifikasi decode
decoded = ''.join(chr(b ^ 0x33) for b in enc)
print(f"Decode check: {decoded}")

# Step 2: Cari key 12 char yang valid dan keren
def sim_acc(key):
    acc = 0x1337
    for c in key:
        acc = (acc + ord(c)) ^ 0x33  # tanpa & 0xFFFFFFFF, sama seperti C++
    return acc

# Kandidat key 12 char
candidates = [
    "SMKRUS-V4-KY",   # 12
    "PPLG-KEY-2024",  # 13 - skip
    "RUS-VAULT-V4",   # 12
    "SMK-RUS-HARD",   # 12
    "VAULT-KEY-V4A",  # 13 - skip
    "CTF-SMKRUS-V4",  # 13 - skip
    "KERNEL-AUTH-1",  # 13 - skip
    "SMKRUS--HARD",   # 12
    "RUS-KEY-V4-0",   # 12
]

print("\n=== Kandidat Key ===")
for key in candidates:
    if len(key) == 12:
        acc = sim_acc(key)
        print(f"Key: '{key}' (len={len(key)}) -> acc: 0x{acc:04X}")

# Step 3: Pilih key terbaik, ambil acc-nya sebagai target
chosen_key = "RUS-VAULT-V4"
target_acc = sim_acc(chosen_key)
print(f"\nChosen Key : '{chosen_key}'")
print(f"Target acc : 0x{target_acc:04X}")
print(f"\n--- Update di C++ ---")
print(f"return (acc == 0x{target_acc:04X});")