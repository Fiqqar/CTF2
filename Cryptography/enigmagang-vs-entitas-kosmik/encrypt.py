from enigma.machine import EnigmaMachine

def encrypt_flag(plaintext):
    machine = EnigmaMachine.from_key_sheet(
        rotors='VI I III',           
        reflector='B',               
        ring_settings=[1, 1, 1],     
        plugboard_settings='PN LK YT' 
    )
    
    machine.set_display('AQL')
    
    clean_text = plaintext.upper().replace(" ", "")
    
    return machine.process_text(clean_text)

if __name__ == "__main__":
    flag_content = "pkldipolytronbersamaentitaskosmik"
    ciphertext = encrypt_flag(flag_content)
    print(f"Plaintext  : {flag_content}")
    print(f"Ciphertext : {ciphertext}")