import base64

def solve():
    cipher_hex = "66573576636e52356247397758326c6b5832647559576468625639755a5764755a584266645774686530644d5546413d"
    
    # 1. Decode Hex ke String (Base64)
    b64_string = bytes.fromhex(cipher_hex).decode()
    
    # 2. Decode Base64 ke String (Reversed Flag)
    reversed_flag = base64.b64decode(b64_string).decode()
    
    # 3. Reverse balik buat dapet Flag asli
    flag = reversed_flag[::-1]
    
    print(f"Flag Ketemu: {flag}")

if __name__ == "__main__":
    solve()