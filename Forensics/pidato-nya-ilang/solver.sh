dd if=challenge.img of=hasil_carving.zip bs=1 skip=5242880 count=10240

unzip hasil_carving.zip

cat asset.txt

cat flag.enc

cat << 'EOF' > decrypt.py
with open("flag.enc", "rb") as f:
    data = f.read()

# Kunci dari petunjuk pidato (0x42)
key = 0x42
flag = "".join([chr(b ^ key) for b in data])
print(f"FLAG NYA ADALAH: {flag}")
EOF

python3 decrypt.py