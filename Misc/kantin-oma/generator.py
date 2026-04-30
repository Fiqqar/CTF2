from PIL import Image, ImageDraw
import zipfile
import os
import io

def generate_hard_challenge():
    filename = "oma_archive.png"
    # Bytecode flag lo: PPLG{m15c_p0lygl0t_15_h4rd}
    flag_ciphertext = [99, 99, 127, 116, 72, 3, 94, 7, 108, 80, 7, 93, 71, 0, 0, 93, 108, 6, 0, 80, 65, 0, 71, 108, 69, 126, 78]
    
    # 1. Bikin gambar PNG asli (Outline tetep #333c3a)
    img = Image.new('RGB', (255, 100), color=(51, 60, 58))
    d = ImageDraw.Draw(img)
    d.text((15, 45), "PPLG{p0lyglot_1s_kinda_h4rd}", fill=(255, 255, 255))
    img.save("base.png")

    # 2. Bikin isi script Python (__main__.py)
    # Karena ini bakal ada di dalem ZIP, Python gak akan protes soal data PNG di luarnya
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

    # 3. Bikin file ZIP di dalam Memory (RAM), lalu masukin __main__.py ke dalamnya
    zip_buffer = io.BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zf:
        zf.writestr('__main__.py', python_payload)

    # 4. GABUNGKAN KEDUANYA! (PNG di atas, ZIP di bawah)
    with open("base.png", "rb") as f:
        png_data = f.read()

    with open(filename, "wb") as f:
        f.write(png_data) # Header & Data PNG (Dibaca oleh Image Viewer)
        f.write(zip_buffer.getvalue()) # Data ZIP (Dibaca oleh interpreter Python)

    if os.path.exists("base.png"): 
        os.remove("base.png")
        
    print(f"Sukses! Perfect Polyglot berhasil dibuat.")
    print(f"Coba eksekusi: python {filename}")

if __name__ == "__main__":
    generate_hard_challenge()