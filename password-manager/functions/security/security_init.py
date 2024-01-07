# Imports
import os
from cryptography.fernet import Fernet


def generate_key_function():
    return Fernet.generate_key()


def init_cipher_function(key):
    return Fernet(key)


def security_init_function(username):
    key_file_name = 'encryption.key'
    key_directory = f'data/{username}'
    key_file_location = key_directory + '/' + key_file_name

    if os.path.exists(key_file_location):
        with open(key_file_location, 'rb') as key_file:
            key = key_file.read()
    else:
        key = generate_key_function()
        with open(key_file_location, 'wb') as key_file:
            key_file.write(key)
    cipher = init_cipher_function(key)
    return cipher
