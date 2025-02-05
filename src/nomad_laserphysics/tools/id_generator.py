import hashlib

# 62 possible values
ALPHABET = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode(num, length=5):
    encoded = ""
    for _ in range(length):
        num, rem = divmod(num, 62)
        encoded = ALPHABET[rem] + encoded
    return encoded

def generate_id(name): # use 5 characters -> 16^5 values
    hash_value = int(hashlib.sha1(name.encode()).hexdigest(), 16) #160 Bit Hash
    short_id = encode(hash_value % (62**5), 5)
    return short_id

print(generate_id("04-02-24_testname"))