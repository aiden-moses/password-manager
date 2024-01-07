

def decrypt_function(cipher, encrypted_text):
    return cipher.decrypt(encrypted_text.encode()).decode()
