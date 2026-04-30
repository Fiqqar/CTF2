from Crypto.Cipher import AES
import hashlib

def generate_2000_theme():
    # 1. Masukkan Link Google Drive foto batu lo
    link_drive = "https://drive.google.com/file/d/1J83QhKbxXnN5hGagTORaa_71Ly_-OvFo/view?usp=sharing" 
    
    # 2. Key: SHA256 dari 'pplg' (Identitas kita)
    key = hashlib.sha256("pplg".encode()).digest()
    
    # 3. Nonce: "2000" yang di-padding jadi 12 byte
    # Kita bikin simpel: "000000002000"
    nonce = b"000000002000" 
    
    # 4. Encrypt AES-GCM
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    ciphertext, tag = cipher.encrypt_and_digest(link_drive.encode())
    
    print(f"Ciphertext: {ciphertext.hex()}")
    print(f"Tag: {tag.hex()}")
    print(f"Nonce (hex): {nonce.hex()}")

if __name__ == "__main__":
    generate_2000_theme()