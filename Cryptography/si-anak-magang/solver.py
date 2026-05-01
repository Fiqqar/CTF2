import base64

cipher = "6657747062584e766131397a595852706447356c5832467459584e795a574a66626d397964486c736233426661575266624774776530644d5546413d"

# 1. Hex Decode (Encode 16)
step1 = bytes.fromhex(cipher).decode()

# 2. Base64 Decode (Dasar 64)
step2 = base64.b64decode(step1).decode()

# 3. Reverse (Dibalik)
flag = step2[::-1]

print(f"Hasil Dekripsi: {flag}")