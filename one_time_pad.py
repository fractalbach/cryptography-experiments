import secrets

class OneTimePad:
    def key_gen(self, number_of_bits: int) -> int:
        return secrets.randbits(number_of_bits)

def str_to_int(s: str) -> int:
    # return int.from_bytes('hello'.encode(), 'big')
    return int(''.join(format(ord(x), '08b') for x in s), 2)
    # return s.encode('utf-8')

def str_to_bits(s: str) -> str:
    return ''.join(format(x, '08b') for x in s.encode('utf-8'))

def bits_to_str(b: str) -> str:
    if len(b) % 8 != 0: raise ValueError('input bits do not make 8-bit bytes.')
    bytearray(int(b[8*i : 8*(i+1)], 2) for i in range(len(b) // 8)).decode('utf-8')

def xor(bits1: str, bits2: str) -> str:
    pass

def int_to_str(n: int) -> str:
    pass

def bin_to_str(s: str) -> str:
    return int_to_str(int(s, 2))

def nice_bin(n: int, bit_length: int) -> str:
    return format(n, f'0{bit_length}b')

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

