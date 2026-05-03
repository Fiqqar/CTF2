png_signature = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"

with open("horee_mbg_datang.dat", "rb") as f:
    data = f.read()

ihdr_index = data.find(b"IHDR")

if ihdr_index != -1:
    start_png = ihdr_index - 4
    
    fixed_image = png_signature + data[start_png:]
    
    with open("menu_makan_siang.png", "wb") as out:
        out.write(fixed_image)
    
    print(f"[+] PNG ditemukan! Memulai carving dari offset: {hex(start_png)}")
    print("[+] File diperbaiki: menu_makan_siang.png")
else:
    print("[-] IHDR tidak ditemukan. Coba cek lagi binernya.")