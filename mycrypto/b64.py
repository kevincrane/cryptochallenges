import base64


ALPHA = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
PADDING = '='


def tobase64(ptext, padded=True):
    """
    :param ptext: str to be converted to base64; e.g. 'hello world'
    :return: base64-encoded string
    Algorithm: http://en.wikipedia.org/wiki/Base64
        - Reads 3 bytes at a time
        - Convert 6 bits to corresponding char above
        - Repeat for each of 3 bytes in chunk, for whole string
    """
    ctext = ''
    padding = 0
    # Add 0x00 padding to make multiple of 3
    while len(ptext) % 3 != 0:
        ptext += chr(0x00)
        padding += 1

    # Read each chunk of 3 bytes, convert to 4 B64 chars (take 6 bits of each 8-bit char)
    #   3x bytes -> 4x b64 chars
    for chunk in [ptext[i:i+3] for i in range(0, len(ptext), 3)]:
        ctext += ALPHA[ord(chunk[0]) >> 2]

        second = (ord(chunk[0]) & 0x03) << 4 | (ord(chunk[1]) & 0xf0) >> 4
        ctext += ALPHA[second]

        third = (ord(chunk[1]) & 0x0f) << 2 | (ord(chunk[2]) & 0xc0) >> 6
        ctext += ALPHA[third]

        ctext += ALPHA[ord(chunk[2]) & 0x3f]

    # Add padding char to end to replace fake
    if padding > 0:
        ctext = ctext[:-padding]
        if padded:
            ctext += (PADDING * padding)
    return str(ctext)


def frombase64(ctext):
    """
    :param ctext: str to be converted back to ASCII; e.g. 'hello world'
    :return: ASCII-encoded string
    Algorithm: http://en.wikipedia.org/wiki/Base64
    """
    ptext = ''
    padding = 0
    # Add 0x00 padding to make multiple of 4
    while len(ctext) % 4 != 0:
        ctext += chr(0x00)
        padding += 1

    for chunk in [ctext[i:i+4] for i in range(0, len(ctext), 4)]:
        ptext += chr(ALPHA.index(chunk[0]) << 2 | (ALPHA.index(chunk[1]) & 0x30) >> 4)
        try:
            third = ALPHA.index(chunk[2])
        except ValueError:
            third = 0x00
        ptext += chr((ALPHA.index(chunk[1]) & 0x0f) << 4 | (third & 0x3c) >> 2)

        try:
            fourth = ALPHA.index(chunk[3])
        except ValueError:
            fourth = 0x00
        ptext += chr((third & 0x03) << 6 | fourth & 0x3f)
    return ptext