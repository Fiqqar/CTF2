with open("flag.enc", "rb") as f:
    data = f.read()
key = 0x42
flag = "".join([chr(b ^ key) for b in data])
print(f"FLAG NYA ADALAH: {flag}")