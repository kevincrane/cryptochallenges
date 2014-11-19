#!/usr/bin/env python2.7
from challenges import challenge, expect
from mycrypto import b64

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
    output = b64.hex_str_to_base64(given)
    expect(output, expected)