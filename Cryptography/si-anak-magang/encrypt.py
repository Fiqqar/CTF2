import base64

def generate_easy():
    # Flag original
    flag = "PPLG{aku_pengen_magang_di_polytron}"
    
    # 1. Reverse String
    rev = flag[::-1]
    
    # 2. Base64 Encoding
    b64 = base64.b64encode(rev.encode()).decode()
    
    # 3. Hex Encoding (Biar makin pusing liat angkanya)
    final_cipher = b64.encode().hex()
    
    print(f"Target Cipher: {final_cipher}")

if __name__ == "__main__":
    generate_easy()