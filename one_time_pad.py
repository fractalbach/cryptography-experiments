import secrets


# ONE TIME PAD ENCRYPTION SCHEME
# ==============================================================================

# Begin with a message that you want to send
message:str = "yao bad"

# Convert the message into bytes
msg:bytes = message.encode('utf8')

# KEY GENERATION
# ------------------------------------------------------------------------------
# One Time Pad encryption scheme uses a key that is exactly the same length as
# the message being encrypted. We will only use this key one time.
length:int = len(msg)
key:bytes = secrets.token_bytes(length)

# ENCRYPT
# ------------------------------------------------------------------------------
# XOR the key with the message to create ciphertext.
cipher:bytes = bytes(msg[i] ^ key[i] for i in range(length))

# DECRYPT
# ------------------------------------------------------------------------------
# You can retrieve the original messsage from the ciphertext with another XOR
# between the ciphertext and the key.
output:bytes = bytes(cipher[i] ^ key[i] for i in range(length))


# PRINT OUTPUT
# ==============================================================================

# Displays each byte in a fancy way with "lights" for each bit.
def mybin(b:bytes) -> str:
    off = '▢'; on = '▣'
    return ''.join(f'{x:08b} ' for x in b).replace('0', off).replace('1', on)

# Print everything so we can see how we did.
print(f'''
message in  : {message}
------------+----------------
message     : {mybin(msg)}
key         : {mybin(key)}
ciphertext  : {mybin(cipher)}
decrypted   : {mybin(output)}
------------+----------------
message out : {output.decode('utf8')}
''')

