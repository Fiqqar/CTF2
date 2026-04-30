from PIL import Image

# 1. Masukkan Flag-nya di sini
flag = "PPLG{FAKE_FLAG}"

# 2. Fungsi sederhana buat convert String ke Brainfuck
def generate_bf(text):
    bf = ""
    last_val = 0
    for char in text:
        target = ord(char)
        diff = target - last_val
        if diff > 0:
            bf += "+" * diff
        elif diff < 0:
            bf += "-" * abs(diff)
        bf += "."
        last_val = target
    return bf

# Generate kode BF berdasarkan isi variabel flag
bf_code = generate_bf(flag)

# 3. Mapping warna ke simbol Brainfuck
mapping = {
    '+': (255, 0, 0),    '-': (0, 255, 0),
    '>': (0, 0, 255),    '<': (255, 255, 0),
    '[': (255, 0, 255),  ']': (0, 255, 255),
    '.': (255, 255, 255),',': (0, 0, 0)
}

# 4. Membuat gambar (Background tetap #333c3a)
# Lebar gambar otomatis menyesuaikan panjang kode BF
img = Image.new('RGB', (len(bf_code), 10), color=(51, 60, 58)) 
pixels = img.load()

# Gambar kode BF di baris paling atas
for i, char in enumerate(bf_code):
    pixels[i, 0] = mapping[char]

img.save("mysterious_sprite.png")
print(f"Selesai! Flag '{flag}' sudah dikonversi jadi warna.")
print(f"Panjang kode: {len(bf_code)} pixel.")