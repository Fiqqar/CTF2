from PIL import Image, ImageDraw
import zipfile
import os
import io

def generate_hard_challenge():
    filename = "oma_archive.png"
    
    flag_ciphertext = [99, 99, 127, 116, 72, 3, 94, 7, 108, 80, 7, 93, 71, 0, 0, 93, 108, 6, 0, 80, 65, 0, 71, 108, 69, 126, 78]
    
    img = Image.new('RGB', (255, 100), color=(51, 60, 58))
    d = ImageDraw.Draw(img)
    d.text((15, 45), "PPLG{p0lyglot_1s_kinda_h4rd}", fill=(255, 255, 255))
    img.save("base.png")
    
    
    
    python_payload = f"""import sys

def oma_vm():
    print("\\n--- OMA VIRTUAL MACHINE v1.0 ---")
    data = {flag_ciphertext}
    key = 0x33
    inp = input("Masukkan Passphrase: ")
    if inp == "open_the_canteen":
        decoded = "".join([chr(b ^ key) for b in data])
        print("Flag: " + decoded)
    else:
        print("Akses Ditolak!")

if __name__ == "__main__":
    oma_vm()
"""

    
    
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('__main__.py', python_payload)

    with open("base.png", "rb") as f:
        png_data = f.read()

    with open(filename, "wb") as f:
        f.write(png_data)
        f.write(zip_buffer.getvalue())

    if os.path.exists("base.png"):
        os.remove("base.png")
        
    print(f"Sukses! Perfect Polyglot berhasil dibuat.")
    print(f"Coba eksekusi: python {filename}")

if __name__ == "__main__":
    generate_hard_challenge()