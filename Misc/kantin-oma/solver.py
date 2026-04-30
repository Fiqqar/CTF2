import zipfile

# Nama file tantangan lo
file_target = "oma_archive.png"

try:
    # Kita perlakukan file PNG sebagai ZIP (karena data ZIP ditempel di belakang)
    with zipfile.ZipFile(file_target, "r") as z:
        # Baca isi file __main__.py yang ada di dalam ZIP tersebut
        content = z.read("__main__.py").decode()
        print("--- ISI SCRIPT TERSEMBUNYI ---")
        print(content)
        print("------------------------------")
except Exception as e:
    print(f"Gagal ekstrak: {e}")