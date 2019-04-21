#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome ife it reads the sam forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    return is_palindrome_iterative(text)


def is_palindrome_iterative(text):
    """
        is_palindrome_iterative() checks to see if a given text is a palindrome
        meaning its characters flipped would be the same word from the beginning.

        Args:       text (string)
        Returns:    is_palindrome (bool)

        Time:       O(n)
        Space:       O(n)
    """
    
    source = text.lower()   # Time: O(n), Space: O(n) 🏃‍
    print('source:', source)
    # left & right index of source
    left = 0
    right = len(source) - 1    # O(1) 💨

    while left <= right:    # while left 🛑✋'s before passing right
        if text[left] in string.punctuation or text[left] == ' ':
            left += 1
            continue
        if text[right] in string.punctuation or text[right] == ' ':
            right -= 1
            continue
        if source[left] != source[right]:
            return False    # 😭
        left += 1
        right -= 1

    is_palindrome = True    # 🤩

    return is_palindrome

    # Easy Way 😛
    # rvs_text = text[::-1]
    # if text == rvs_text:
    #     return True
    # else:
    #     return False


def is_palindrome_recursive(text, left=None, right=None):
    """
        is_palindrome_recursive() checks to see if a given text is a palindrome
        meaning its characters flipped would be the same word from the beginning.

        Args:       text (string)
        Returns:    is_palindrome (bool)

        Time:       O(n)
        Space:      O(1)
    """
    # source = text.lower()   # When doing this recursively this operation is called each time
    if left == None and right == None:
        left = 0
        right = len(text) - 1
    if left >= right: # Base Case
        return True
    if text[left] in string.punctuation or text[left] == ' ':
        return is_palindrome_recursive(text, left + 1, right)
    if text[right] in string.punctuation or text[right] == ' ':
        return is_palindrome_recursive(text, left, right - 1)
    if text[left].lower() == text[right].lower():
        return is_palindrome_recursive(text, left + 1, right - 1)

    return False

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()