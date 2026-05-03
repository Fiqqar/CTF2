import zipfile

file_target = "oma_archive.png"

try:
    with zipfile.ZipFile(file_target, "r") as z:
        content = z.read("__main__.py").decode()
        print("--- ISI SCRIPT TERSEMBUNYI ---")
        print(content)
        print("------------------------------")
except Exception as e:
    print(f"Gagal ekstrak: {e}")