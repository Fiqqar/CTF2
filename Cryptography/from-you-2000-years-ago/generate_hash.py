from Crypto.Cipher import AES
import hashlib

def generate_2000_theme():
    link_drive = "https://drive.google.com/file/d/1J83QhKbxXnN5hGagTORaa_71Ly_-OvFo/view?usp=sharing" 
    
    key = hashlib.sha256("pplg".encode()).digest()
    
    nonce = b"000000002000"
    
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(link_drive.encode())
    
    print(f"Ciphertext: {ciphertext.hex()}")
    print(f"Tag: {tag.hex()}")
    print(f"Nonce (hex): {nonce.hex()}")

if __name__ == "__main__":
    generate_2000_theme()