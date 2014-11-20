import base64
import binascii
from itertools import cycle


def hex_to_bytes(hexstr):
    """ Convert a hex string to bytes """
    return bytearray.fromhex(hexstr)


def bytes_to_hex(b):
    """ Convert bytes to a hex string """
    return binascii.b2a_hex(b).decode()


def hex_str_to_base64(s):
    """ Turn string of hex chars to string of Base64 """
    return base64.b64encode(s.decode('hex'))


def crypt_xor(plainbytes, keybytes):
    """
    Take a plaintext bytes object and xor it with the given key bytes. Key
    will be cycled if it is shorter than plaintext. Returns bytes.
    """
    return bytes([b1 ^ b2 for b1, b2 in zip(plainbytes, cycle(keybytes))])
