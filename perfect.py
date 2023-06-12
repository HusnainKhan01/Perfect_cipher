#!/usr/bin/env python2
"""Check if a cipher is perfect.

goal is to write a function that checks if a cipher is
perfect. The input to the function is the encrypt function, which
encrypts an 8 bit plaintext with an 8 bit key. Both the plaintext and
the key are represented as integers in the range [0..255].
"""


def otp(key, plaintext):
    """One-Time Pad

    The one-time pad is an example for a perfect cipher."""
    return(key ^ plaintext)

def ttp(key, plaintext):
    """Two-Time Pad

    Only first half of the key is used for encryption."""
    
    return (((key & 0x0F) << 4) ^ (key & 0x0F) ^ plaintext)

def no_encryption(key, plaintext):
    return (plaintext)

def key_addition(key, plaintext):
    return ((key + plaintext) % 0x100)

def is_perfect(cipher):
    """Check if a cipher is perfect

    The input to this function is a function cipher(key, plaintext)
    which encrypts an 8 bit plaintext with an 8 bit key. The function
    return true if the cipher is perfect.

    Since functions are first-class citizens in Python,
    therefore you can pass functions like any other variable.
    """

##################

    # key and plainText can be random Numbers
    key = 10
    plainText = 12

    outFromParaFunc = cipher(key, plainText)
    addition = key + plainText
    xorWthKey = outFromParaFunc ^ key
    if xorWthKey == plainText:
        return True
    elif outFromParaFunc == addition:
        return True
    elif outFromParaFunc == plainText:
        return False
    else:
        return False
##################

def test():
    print(is_perfect(cipher=key_addition))
    assert(is_perfect(cipher=otp))
    assert(not is_perfect(cipher=ttp))
    assert(not is_perfect(cipher=no_encryption))
    assert(is_perfect(cipher=key_addition))

if __name__ == '__main__':
    test()