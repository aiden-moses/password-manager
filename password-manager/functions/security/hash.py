# Imports
import hashlib


def hash_function(text):
    text = text.encode()
    blake2b = hashlib.blake2b()
    blake2b.update(text)
    return blake2b.hexdigest()
