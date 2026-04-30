# Hitung bytecode di terminal python lo dulu buat dapet angkanya:
flag = "PPLG{0m4_c4nt33n_53cr3t_vM}"
key = 0x33 # Kunci XOR (sesuai outline #333c3a)
bytecode = [ord(c) ^ key for c in flag]
print(bytecode)