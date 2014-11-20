#!/usr/bin/env python2.7
import binascii
from challenges import challenge, expect
from mycrypto import b64, cry1

num = 1
name = 'Basics'
challenges = {}


@challenge(0, 'Base64 Impl', challenges)
def challenge1_fake():
    """ Convert hex to base64
        Bonus: strings to base64
    """
    print 'Testing Challenge 1'
    print b64.tobase64('Hello world!!!')
    print b64.tobase64('Hello world!!')
    print b64.tobase64('Hello world!')
    print b64.frombase64('SGVsbG8gd29ybGQhISE=')
    print b64.frombase64('SGVsbG8gd29ybGQhIQ==')
    print b64.frombase64('SGVsbG8gd29ybGQh')
    print 'Decode(encode(ptext)) = ptext?'
    print '"Hello world!!" -> "%s"' % b64.frombase64(b64.tobase64('Hello world!!'))


@challenge(1, 'Hex str -> Base64', challenges)
def challenge1():
    given = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
    output = cry1.hex_str_to_base64(given)
    expect(output, expected)


# TODO: KEVIN - stuck here, turns out bitwise operations are complete shit in Python; or at least very confusing
#   - Please come back here someday if you think about it: http://cryptopals.com/

@challenge(2, 'Fixed XOR', challenges)
def challenge2():
    in1 = '1c0111001f010100061a024b53535009181c'
    in2 = '686974207468652062756c6c277320657965'
    expected = '746865206b696420646f6e277420706c6179'
    output = cry1.crypt_xor(cry1.hex_to_bytes(in1), cry1.hex_to_bytes(in2))
    print output
    # output = cry1.fixed_xor(cry1.hex_to_bytes(in1), cry1.hex_to_bytes(in2))
    expect(cry1.bytes_to_hex(output), expected)