print("--- Welcome to the Secure Python Shell ---")
print("Coba baca flag.txt kalau bisa!")

blacklist = ["import", "os", "sys", "eval", "exec", "open", "read", "system"]

while True:
    user_input = input(">>> ")
    
    if any(word in user_input for word in blacklist):
        print("Akses Ditolak! Kata terlarang terdeteksi.")
        continue
        
    try:
        result = str(eval(user_input))
        print(result)
        break
    except Exception as e:
        print(f"Error: {e}")