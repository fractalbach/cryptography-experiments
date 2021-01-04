import secrets

class OneTimePad:
    def key_gen(self, number_of_bits):
        return secrets.randbits(number_of_bits)

def str_to_int(s):
    return int(''.join(format(ord(x), 'b') for x in s), 2)

def nice_bin(integer, bit_length):
    return format(integer, f'0{bit_length}b')

if __name__ == "__main__":
    pad = OneTimePad()
    msg = "hello"

    msg_int = str_to_int(msg)
    bit_length = msg_int.bit_length()

    key_int = pad.key_gen(bit_length)

    cipher_int = msg_int ^ key_int

    key_bits = nice_bin(key_int, bit_length)
    msg_bits = nice_bin(msg_int, bit_length)
    cipher_bits = nice_bin(cipher_int, bit_length)

    print(f'message = "{msg}"')
    print(f'message [{len(msg_bits)}]', msg_bits)
    print(f'key     [{len(key_bits)}]', key_bits)
    print(f'cipher  [{len(cipher_bits)}]', cipher_bits)

