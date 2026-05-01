with open("flag.enc", "rb") as f:
    data = f.read()

# Kunci dari petunjuk pidato (0x42)
key = 0x42
flag = "".join([chr(b ^ key) for b in data])
print(f"FLAG NYA ADALAH: {flag}")