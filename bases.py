# Shoutout to  Sukhrobjon Golibboev (@Sukhrobjon) and Zurich! for help in walking me through the decode algorithm.
#!python

import string
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace

def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    result = 0
    power = 0
    
    letter_mapper = {
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14,
        'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19,
        'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24,
        'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29,
        'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35
    }

    for i in reversed(digits):
        if i.isalpha():
            result += letter_mapper[i.upper()] * (base ** power)
        else:       
            result += int(i) * (base ** power)
        power += 1

    return result

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)

    dividend = number
    result = ''
    magicAsciiNumber = 87

    if number == 0: # Edge Case
        return '0'

    while dividend != 0:
        remainder = dividend % base
        dividend = (dividend - remainder) // base
        if remainder > 9:
            remainder = chr(remainder + magicAsciiNumber) # asci table lower case, avoid magic numbers

        result += str(remainder)

    return result[::-1]

def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)

    number = decode(digits, base1)

    finalNumber = encode(number, base2)

    return finalNumber

def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
    # print(encode(100, 16))