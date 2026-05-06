import hashlib

def get_sha(text):
    hash_object = hashlib.sha256(text.encode('utf-8'))
    hash_hex = hash_object.hexdigest()
    return hash_hex