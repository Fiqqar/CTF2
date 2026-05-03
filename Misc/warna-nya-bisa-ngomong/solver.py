from PIL import Image
img = Image.open("mysterious_sprite.png")
pixels = img.load()
width, height = img.size
inverse_mapping = {
    (255, 0, 0): '+',   (0, 255, 0): '-',
    (0, 0, 255): '>',   (255, 255, 0): '<',
    (255, 0, 255): '[', (0, 255, 255): ']',
    (255, 255, 255): '.', (0, 0, 0): ','
}
bf_code = ""
for x in range(width):
    color = pixels[x, 0][:3]
    if color in inverse_mapping:
        bf_code += inverse_mapping[color]

print(f"Extracted BF: {bf_code}\n")
def brainfuck(code):
    tape = [0] * 30000
    ptr = 0
    pc = 0
    output = ""
    
    stack = []
    jump_map = {}
    for i, char in enumerate(code):
        if char == '[': stack.append(i)
        elif char == ']':
            start = stack.pop()
            jump_map[start] = i
            jump_map[i] = start

    while pc < len(code):
        char = code[pc]
        if char == '+': tape[ptr] = (tape[ptr] + 1) % 256
        elif char == '-': tape[ptr] = (tape[ptr] - 1) % 256
        elif char == '>': ptr += 1
        elif char == '<': ptr -= 1
        elif char == '.': output += chr(tape[ptr])
        elif char == '[' and tape[ptr] == 0: pc = jump_map[pc]
        elif char == ']' and tape[ptr] != 0: pc = jump_map[pc]
        pc += 1
    return output

print(f"Result: {brainfuck(bf_code)}")