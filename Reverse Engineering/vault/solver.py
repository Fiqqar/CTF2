def verify_license(s):
    if len(s) != 12:
        return False
    acc = 0x1337
    for c in s:
        acc = (acc + ord(c)) ^ 0x33
    return acc == 0x1749

def get_flag():
    enc = [
        0x63, 0x63, 0x7F, 0x74, 0x48, 0x44, 0x5B, 0x07,
        0x47, 0x0C, 0x6C, 0x52, 0x6C, 0x50, 0x46, 0x40,
        0x47, 0x03, 0x5E, 0x6C, 0x45, 0x5E, 0x0C, 0x4E
    ]
    return ''.join(chr(b ^ 0x33) for b in enc)

print("=== SMK RUS VAULT v4.0 SOLVER ===\n")
print(f"[*] Flag      : {get_flag()}")
print(f"[*] Valid Key : RUS-VAULT-V4")
print(f"[*] Verified  : {verify_license('RUS-VAULT-V4')}")

# Cari key alternatif — range lebih luas
print("\n[*] Key alternatif:")
import string
charset = string.printable.strip()
found = []

for c1 in charset:
    if len(found) >= 5: break
    for c2 in charset:
        if len(found) >= 5: break
        for c3 in charset:
            prefix = c1 + c2 + c3 + "A" * 8  # 11 chars
            acc = 0x1337
            for c in prefix:
                acc = (acc + ord(c)) ^ 0x33
            needed = (0x1749 ^ 0x33) - acc  # = 0x177A - acc
            if 33 <= needed <= 126:
                key = prefix + chr(needed)
                if verify_license(key):
                    found.append(key)
                    print(f"    [{len(found)}] {key} -> verified: True")
                    break

if not found:
    print("    (tidak ada alternatif dengan charset ini)")