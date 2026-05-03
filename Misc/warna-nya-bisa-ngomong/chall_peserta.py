from PIL import Image
flag = "PPLG{FAKE_FLAG}"
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
bf_code = generate_bf(flag)
mapping = {
    '+': (255, 0, 0),    '-': (0, 255, 0),
    '>': (0, 0, 255),    '<': (255, 255, 0),
    '[': (255, 0, 255),  ']': (0, 255, 255),
    '.': (255, 255, 255),',': (0, 0, 0)
}
img = Image.new('RGB', (len(bf_code), 10), color=(51, 60, 58)) 
pixels = img.load()

for i, char in enumerate(bf_code):
    pixels[i, 0] = mapping[char]

img.save("mysterious_sprite.png")
print(f"Selesai! Flag '{flag}' sudah dikonversi jadi warna.")
print(f"Panjang kode: {len(bf_code)} pixel.")