flag = "PPLG{0m4_c4nt33n_53cr3t_vM}"
key = 0x33
bytecode = [ord(c) ^ key for c in flag]
print(bytecode)