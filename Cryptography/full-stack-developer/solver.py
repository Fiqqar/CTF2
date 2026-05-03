import hashlib

def solve():
    languages = [
        "Python", "JavaScript", "C++", "Rust", "C#", "Go", "Java", 
        "PHP", "Swift", "Kotlin", "Zig", "Solidity", "Assembly", 
        "Cobol", "Pascal", "Fortran"
    ]
    
    print("--- Solver Mode ---")
    print("Caranya: Masukkan sembarang string ke menu encrypt di program utama,")
    print("terus masukin hasilnya ke sini buat nyari pattern salt-nya.\n")
    
    test_str = input("String yang lo encrypt tadi: ").lower()
    received_hash = input("Hasil hash dari program: ").strip()

    found_salt = None
    for s in range(512):
        hex_s = format(s, 'x')
        check = (test_str + hex_s).encode("utf-16-le")
        if hashlib.sha256(check).hexdigest() == received_hash:
            found_salt = hex_s
            print(f"[+] Ketemu! Salt yang dipake program adalah: {found_salt}")
            break
    
    if not found_salt:
        print("[-] Salt gak ketemu. Pastikan string dan hash-nya bener.")
        return

    print("\n[+] Sekarang lo bisa tebak bahasanya. Cobain satu-satu manual atau brute-force di sini.")