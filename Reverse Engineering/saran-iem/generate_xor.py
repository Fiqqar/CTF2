flag = "PPLG{r3v3rsing_n4n0_h34dph0n3}"
xor_key = 0x33
ciphertext = [ord(c) ^ xor_key for c in flag]
print(ciphertext)