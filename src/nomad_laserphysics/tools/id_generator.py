import hashlib

# 62 possible values
BASE62_ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode(num, length=4):
    encoded = ""
    for _ in range(length):
        num, rem = divmod(num, 62)
        encoded = BASE62_ALPHABET[rem] + encoded
    return encoded

def generate_id(name): # use 4 characters -> 16^4 values
    hash_value = int(hashlib.sha1(name.encode()).hexdigest(), 16)
    short_id = encode(hash_value % (62**4), 4)
    return short_id

print(generate_id("04-02-24_testname"))