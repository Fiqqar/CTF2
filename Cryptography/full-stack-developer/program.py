import hashlib
import random
import sys
import os

def main():
    languages = [
        "Python", "JavaScript", "C++", "Rust", "C#", "Go", "Java", 
        "PHP", "Swift", "Kotlin", "Zig", "Solidity", "Assembly", 
        "Cobol", "Pascal", "Fortran"
    ]

    secret_lang = random.choice(languages).lower()
    salt_value = random.randint(0, 511)
    salt_hex = format(salt_value, 'x')
    
    target_payload = (secret_lang + salt_hex).encode("utf-16-le")
    target_hash = hashlib.sha256(target_payload).hexdigest()

    print("====================================================")
    print("gw mau belajar programming language baru, tebak coba apa?")
    print("kalo salah KELUAR DARI SINI")
    print(f"Nih hash bahasa yang gw pelajarin : {target_hash}")
    print("====================================================\n")

    encrypt_limit = 3
    
    while True:
        print(f"Pilihan:")
        print(f"1. Encrypt string (Sisa kesempatan: {encrypt_limit})")
        print(f"2. Tebak Bahasa")
        print(f"3. Keluar")
        
        try:
            choice = input("\nMasukkan pilihan (1/2/3): ")
        except EOFError:
            sys.exit()

        if choice == '1':
            if encrypt_limit > 0:
                to_encrypt = input("Masukkan string yang mau di-hash: ").lower()
                res_hash = hashlib.sha256((to_encrypt + salt_hex).encode("utf-16-le")).hexdigest()
                print(f"Result (SHA-256 UTF-16LE + Secret Salt): {res_hash}\n")
                encrypt_limit -= 1
            else:
                print("Kesempatan encrypt sudah habis. Silakan langsung tebak.\n")

        elif choice == '2':
            guess_lang = input("Tebak bahasanya: ").strip().lower()
            guess_payload = (guess_lang + salt_hex).encode("utf-16-le")
            guess_hash = hashlib.sha256(guess_payload).hexdigest()

            if guess_hash == target_hash:
                print(f"\nBenar!")
                try:
                    with open("flag.txt", "r") as f:
                        print(f"Flag: {f.read().strip()}")
                except FileNotFoundError:
                    print("Error: File flag.txt tidak ditemukan. Hubungi admin.")
                sys.exit()
            else:
                print("\nJawaban salah. Akses ditolak.")
                sys.exit()

        elif choice == '3':
            print("Sesi diakhiri.")
            sys.exit()
        
        else:
            print("Input tidak valid.\n")

if __name__ == "__main__":
    main()