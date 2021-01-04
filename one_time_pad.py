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

def binstr(s):
    return int(''.join(format(ord(x), 'b') for x in s), 2)

def unbinstr(binstr):
    return binstr.decode('utf-8')

if __name__ == "__main__":
    pad = OneTimePad()
    msg = "hello"
    bmsg = binstr(msg)
    k = pad.key_gen(bmsg.bit_length())

    print(f'message = "{msg}"')
    print("converting message to binary...")
    print(f'msg[{bmsg.bit_length()}]', bin(bmsg))
    print("generating key of the same length...")
    print(f'key[{k.bit_length()}]', bin(k))

