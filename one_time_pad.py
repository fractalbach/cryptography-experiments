import secrets
import binascii

class OneTimePad:

    def __init__(self):
        pass

    def encrypt(self, message):
        pass

    def decrypt(self, ciphertext):
        pass

    def key_gen(self, l):
        return secrets.randbits(l)

if __name__ == "__main__":
    msg = "hello"
    pad = OneTimePad()
    k = pad.key_gen(10)
    print(bin(k))