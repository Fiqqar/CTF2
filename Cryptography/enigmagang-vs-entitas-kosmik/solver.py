from enigma.machine import EnigmaMachine

def solve_enigma(ciphertext):
    machine = EnigmaMachine.from_key_sheet(
        rotors='VI I III',
        reflector='B',
        ring_settings=[1, 1, 1],
        plugboard_settings='PN LK YT'
    )
    
    machine.set_display('AQL')
    
    decrypted_text = machine.process_text(ciphertext)
    
    return decrypted_text.lower()

if __name__ == "__main__":
    cipher = "YQSZFLPZCGZKHQJKWCOYNDLGIOHAAVHCA"
    result = solve_enigma(cipher)
    
    print("--- ENIGMA DECODER ---")
    print(f"Ciphertext : {cipher}")
    print(f"Result     : {result}")
    print(f"Final Flag : PPLG{{{result}}}")