from enigma.machine import EnigmaMachine

def encrypt_flag(plaintext):
    # Balik urutan rotor agar III menjadi rotor paling kanan (yang berputar tiap huruf)
    # Ini untuk menyesuaikan visual dari simulator yang kamu gunakan
    machine = EnigmaMachine.from_key_sheet(
        rotors='VI I III',           
        reflector='B',               
        ring_settings=[1, 1, 1],     
        plugboard_settings='PN LK YT' 
    )
    
    # Gunakan set_display sesuai urutan Rotor di atas (A=VI, Q=I, L=III)
    machine.set_display('AQL')
    
    # Enigma hanya memproses huruf. Kita pastikan semua kapital dan tanpa spasi.
    clean_text = plaintext.upper().replace(" ", "")
    
    return machine.process_text(clean_text)

if __name__ == "__main__":
    # Pastikan plaintext benar-benar hanya isinya
    flag_content = "pkldipolytronbersamaentitaskosmik"
    ciphertext = encrypt_flag(flag_content)
    print(f"Plaintext  : {flag_content}")
    print(f"Ciphertext : {ciphertext}")